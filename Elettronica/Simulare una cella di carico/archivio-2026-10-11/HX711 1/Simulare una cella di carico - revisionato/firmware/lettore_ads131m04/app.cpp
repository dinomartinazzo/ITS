// app.cpp — acquisizione simultanea: 3 celle + eccitazione, rapporto calcolato campione per campione
#include "app.h"
#include "config.h"
#include "ads131m04_driver.h"
#include "dsp.h"
#include "serial_ui.h"
#include <math.h>

namespace {

enum class Task : uint8_t { Idle, Tare, Stats };

constexpr double NVV_PER_MVV = 1.0e6;   // i filtri lavorano in nV/V interi

Ads131m04Driver adc({cfg::PIN_SCLK, cfg::PIN_MISO, cfg::PIN_MOSI, cfg::PIN_CS, cfg::PIN_DRDY, cfg::PIN_SYNC,
                     cfg::PIN_CLKIN},
                    cfg::SPI_HZ);
SerialUi ui(Serial);

MovingAverage<cfg::FILTER_LEN> filters[cfg::CELL_CHANNELS];
RunningStats acc[cfg::CELL_CHANNELS];
double tareMvV[cfg::CELL_CHANNELS] = {};
double lastVex = 0.0;
int32_t lastRaw[cfg::CHANNELS] = {};

uint8_t osrCode = cfg::OSR_CODE;
bool globalChop = cfg::GLOBAL_CHOP;
Task task = Task::Idle;
bool streaming = true;
bool rawMode = false;
bool configOk = false;
uint8_t discardLeft = cfg::DISCARD_FRAMES;
uint32_t crcErrors = 0;
uint32_t frames = 0;
uint32_t lastFrameMs = 0;
uint32_t rateStartMs = 0;
uint32_t rateFrames = 0;
double measuredSps = 0.0;
uint32_t lastPrintMs = 0;
uint32_t lastWarnMs = 0;
bool timeoutReported = false;
double clkinHz = 0.0;

// --- Conversioni ---

uint8_t gainCode(uint8_t gain) {         // codice = log2(guadagno)
  uint8_t code = 0;
  while ((1u << code) < gain && code < 7) {
    ++code;
  }
  return code;
}

double countsToVolts(int32_t counts, uint8_t gain) {
  return counts * (cfg::VREF_V / gain) / 8388608.0;   // 1 LSB = (1,2 V / gain) / 2^23
}

// Invalida anche lo streaming: nessun valore precedente deve apparire come attuale.
void invalidateMeasurement() {
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    filters[i].reset();
    acc[i].reset();
  }
  if (task != Task::Idle) {
    ui.message("operazione annullata: misura non valida o configurazione cambiata");
  }
  task = Task::Idle;
  lastVex = 0.0;
}

// --- Configurazione ---

bool applyConfig() {
  invalidateMeasurement();
  if (clkinHz <= 0.0 || (adc.id() & 0xFF00) != 0x2400) {
    return false;
  }
  const uint16_t clock = static_cast<uint16_t>(0x0F00 | ((osrCode & 0x07) << 2) | 0x02);  // 4 canali, OSR, alta risoluzione
  uint16_t gain = 0;
  for (uint8_t ch = 0; ch < cfg::CHANNELS; ++ch) {
    gain |= static_cast<uint16_t>(gainCode(cfg::GAIN[ch]) << (4 * ch));
  }
  const uint16_t gc = static_cast<uint16_t>(((cfg::GC_DLY_CODE & 0x0F) << 9) | (globalChop ? 0x0100 : 0x0000));

  const bool ok = adc.writeRegister(Ads131m04Driver::REG_CLOCK, clock) &&
                  adc.writeRegister(Ads131m04Driver::REG_GAIN, gain) &&
                  adc.writeRegister(Ads131m04Driver::REG_CFG, gc);
  adc.sync();                              // riallinea i filtri e svuota le FIFO
  discardLeft = cfg::DISCARD_FRAMES;
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    filters[i].reset();
  }
  rateFrames = 0;
  rateStartMs = millis();
  return ok;
}

void printInfo() {
  Serial.printf("# ID=0x%04X  CLKIN=%.0f Hz  OSR=%u  global-chop=%s  config=%s\n", adc.id(), clkinHz,
                128u << osrCode, globalChop ? "si" : "no", configOk ? "ok" : "ERRORE");
  Serial.printf("# campioni/s misurati=%.1f  trame=%lu  errori CRC=%lu  Vex=%.4f V\n", measuredSps,
                static_cast<unsigned long>(frames), static_cast<unsigned long>(crcErrors), lastVex);
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    Serial.printf("# c%u gain=%u tara=%.5f mV/V\n", i + 1, cfg::GAIN[i], tareMvV[i]);
  }
}

void startTask(Task t) {
  if (!configOk) {
    ui.message("operazione rifiutata: configurazione ADC non valida");
    return;
  }
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    acc[i].reset();
  }
  task = t;
  ui.message("acquisizione in corso...");
}

void finishTask() {
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    const double mean = acc[i].mean() / NVV_PER_MVV;          // mV/V
    const double stdUvV = acc[i].stddev() / 1000.0;            // da nV/V a uV/V
    if (task == Task::Tare) {
      tareMvV[i] += mean;
      Serial.printf("# c%u tara: %.5f mV/V (std %.4f uV/V)\n", i + 1, tareMvV[i], stdUvV);
    } else {
      Serial.printf("# c%u media=%.5f mV/V  rumore=%.4f uV/V rms = %.1f nV rms all'ingresso\n", i + 1, mean,
                    stdUvV, stdUvV * lastVex * 1000.0);
    }
  }
  if (task == Task::Tare) {
    for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
      filters[i].reset();   // la media precedente usava la vecchia tara
    }
  }
  task = Task::Idle;
}

void handleCommand(const Command &cmd) {
  switch (cmd.type) {
    case Command::Type::None:
      break;
    case Command::Type::Tare:
      startTask(Task::Tare);
      break;
    case Command::Type::Stats:
      startTask(Task::Stats);
      break;
    case Command::Type::Osr:
      if (cmd.hasArg && cmd.arg >= 0 && cmd.arg <= 7) {
        osrCode = static_cast<uint8_t>(cmd.arg);
        configOk = applyConfig();
        Serial.printf("# OSR=%u %s\n", 128u << osrCode, configOk ? "" : "(ERRORE di scrittura)");
      } else {
        ui.message("uso: o <0-7>");
      }
      break;
    case Command::Type::GlobalChop:
      globalChop = !globalChop;
      configOk = applyConfig();
      ui.message(globalChop ? "global-chop attivo" : "global-chop disattivo");
      break;
    case Command::Type::ToggleRaw:
      rawMode = !rawMode;
      ui.message(rawMode ? "uscita grezza" : "uscita ingegneristica");
      break;
    case Command::Type::Pause:
      streaming = !streaming;
      ui.message(streaming ? "streaming attivo" : "streaming in pausa");
      break;
    case Command::Type::Info:
      printInfo();
      break;
    case Command::Type::Help:
      ui.help();
      break;
    case Command::Type::Unknown:
      ui.message("comando non riconosciuto (h per l'aiuto)");
      break;
  }
}

// --- Acquisizione ---

void warn(uint32_t now, const char *text) {
  if (now - lastWarnMs > cfg::WARN_PERIOD_MS) {
    ui.message(text);
    lastWarnMs = now;
  }
}

void acquire(uint32_t now) {
  if (!configOk) {
    return;
  }
  if (!adc.isReady()) {
    if (!timeoutReported && now - lastFrameMs > cfg::DRDY_TIMEOUT_MS) {
      ui.message("ERRORE: DRDY non scende (CLKIN, alimentazioni, cablaggio SPI)");
      timeoutReported = true;
      invalidateMeasurement();
    }
    return;
  }
  lastFrameMs = now;
  timeoutReported = false;

  Ads131m04Driver::Frame f;
  adc.readFrame(f);                      // tutti e quattro i canali dello stesso istante
  ++frames;
  ++rateFrames;
  if (now - rateStartMs >= 1000) {
    measuredSps = rateFrames * 1000.0 / (now - rateStartMs);
    rateFrames = 0;
    rateStartMs = now;
  }
  if (cfg::CHECK_CRC && !f.crcOk) {
    ++crcErrors;
    invalidateMeasurement();
    return;
  }
  if (discardLeft > 0) {                 // dati non assestati dopo reset o cambio di configurazione
    --discardLeft;
    return;
  }

  for (uint8_t ch = 0; ch < cfg::CHANNELS; ++ch) {
    lastRaw[ch] = f.ch[ch];
    if (f.ch[ch] >= Ads131m04Driver::RAW_MAX || f.ch[ch] <= Ads131m04Driver::RAW_MIN) {
      warn(now, "ERRORE: canale in saturazione; trama scartata");
      invalidateMeasurement();
      return;
    }
  }

  lastVex = countsToVolts(f.ch[cfg::VEX_CHANNEL], cfg::GAIN[cfg::VEX_CHANNEL]) * cfg::VEX_DIVIDER;
  if (lastVex < cfg::VEX_MIN_V) {
    warn(now, "ATTENZIONE: eccitazione assente o partitore scollegato");
    invalidateMeasurement();
    return;
  }

  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    const double mvv = countsToVolts(f.ch[i], cfg::GAIN[i]) / lastVex * 1000.0 - tareMvV[i];
    const int32_t nvv = static_cast<int32_t>(lround(mvv * NVV_PER_MVV));
    filters[i].push(nvv);
    if (task != Task::Idle) {
      acc[i].push(nvv);
    }
  }
  if (task != Task::Idle && acc[0].count() >= cfg::STATS_SAMPLES) {
    finishTask();
  }
}

void report(uint32_t now) {
  if (!configOk || !streaming || task != Task::Idle || !filters[0].full() || now - lastPrintMs < cfg::PRINT_PERIOD_MS) {
    return;
  }
  lastPrintMs = now;

  if (rawMode) {
    Serial.printf("raw0:%ld\traw1:%ld\traw2:%ld\traw3:%ld\n", static_cast<long>(lastRaw[0]),
                  static_cast<long>(lastRaw[1]), static_cast<long>(lastRaw[2]), static_cast<long>(lastRaw[3]));
    return;
  }
  double total = 0.0;
  for (uint8_t i = 0; i < cfg::CELL_CHANNELS; ++i) {
    const double mvv = filters[i].mean() / NVV_PER_MVV;
    total += mvv / cfg::CELL_SENS_MV_V * cfg::CELL_CAPACITY;
    Serial.printf("c%u:%.4f\t", i + 1, mvv);
  }
  Serial.printf("vex:%.4f\ttot_%s:%.3f\n", lastVex, cfg::CELL_UNIT, total);
}

}  // namespace

namespace app {

void setup() {
  Serial.begin(cfg::SERIAL_BAUD);
  delay(200);
  clkinHz = adc.begin(cfg::CLKIN_HZ, cfg::LEDC_CHANNEL);
  ui.banner();
  if ((adc.id() & 0xFF00) != 0x2400) {
    Serial.printf("# ERRORE: ID letto 0x%04X, atteso 0x24xx (SPI, CS, CLKIN, alimentazioni)\n", adc.id());
  }
  configOk = applyConfig();
  if (!configOk) {
    ui.message("ERRORE: scrittura registri non confermata");
  }
  lastFrameMs = millis();
  ui.message("eseguire 't' con le celle scariche");
}

void loop() {
  const uint32_t now = millis();
  handleCommand(ui.poll());
  acquire(now);
  report(now);
}

}  // namespace app
