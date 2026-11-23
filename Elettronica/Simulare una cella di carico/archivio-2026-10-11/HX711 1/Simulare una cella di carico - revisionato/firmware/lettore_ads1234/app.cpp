// app.cpp — scansione multicanale ADS1234: un canale alla volta, dato assestato a ogni cambio
#include "app.h"
#include "config.h"
#include "ads123x_driver.h"
#include "dsp.h"
#include "load_model.h"
#include "serial_ui.h"

namespace {

enum class Task : uint8_t { Idle, Tare, Stats };

Ads123xDriver adc({cfg::PIN_DOUT, cfg::PIN_SCLK, cfg::PIN_A0, cfg::PIN_A1, cfg::PIN_PDWN, cfg::PIN_SPEED});
SerialUi ui(Serial);

LoadModel models[cfg::CHANNELS_MAX] = {
    LoadModel(cfg::ADC_GAIN, cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY),
    LoadModel(cfg::ADC_GAIN, cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY),
    LoadModel(cfg::ADC_GAIN, cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY),
    LoadModel(cfg::ADC_GAIN, cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY),
};
MovingAverage<cfg::FILTER_LEN> filters[cfg::CHANNELS_MAX];
RunningStats acc[cfg::CHANNELS_MAX];
int32_t lastRaw[cfg::CHANNELS_MAX] = {};
bool fresh[cfg::CHANNELS_MAX] = {};

uint8_t activeChannels = cfg::START_CHANNELS;
uint8_t current = 0;
Task task = Task::Idle;
bool streaming = true;
bool rawMode = false;
bool calibratePending = false;
bool calibrating = false;
bool timeoutReported = false;
uint32_t waitSinceMs = 0;
uint32_t lastPrintMs = 0;
uint32_t lastSatWarnMs = 0;
uint32_t scanStartMs = 0;
uint32_t lastScanMs = 0;

// --- Utilità ---

uint32_t timeoutMs() {
  if (calibrating) {
    return adc.fast() ? cfg::CAL_TIMEOUT_FAST_MS : cfg::CAL_TIMEOUT_SLOW_MS;
  }
  return adc.fast() ? cfg::SETTLE_TIMEOUT_FAST_MS : cfg::SETTLE_TIMEOUT_SLOW_MS;
}

void resetBuffers() {
  for (uint8_t i = 0; i < cfg::CHANNELS_MAX; ++i) {
    filters[i].reset();
    acc[i].reset();
    fresh[i] = false;
  }
}

void restartScan(uint32_t now) {
  current = 0;
  adc.selectChannel(current);
  resetBuffers();
  task = Task::Idle;
  waitSinceMs = now;
  scanStartMs = now;
}

void startTask(Task t) {
  for (uint8_t i = 0; i < cfg::CHANNELS_MAX; ++i) {
    acc[i].reset();
  }
  task = t;
  ui.message("acquisizione in corso...");
}

void printInfo() {
  Serial.printf("# DOUT=GPIO%u SCLK=GPIO%u A0=GPIO%u A1=GPIO%u PDWN=GPIO%u SPEED=GPIO%u\n",
                cfg::PIN_DOUT, cfg::PIN_SCLK, cfg::PIN_A0, cfg::PIN_A1, cfg::PIN_PDWN, cfg::PIN_SPEED);
  Serial.printf("# gain=%.0f  velocita'=%s  canali attivi=%u  scansione completa=%lu ms\n",
                cfg::ADC_GAIN, adc.fast() ? "80 SPS" : "10 SPS", activeChannels,
                static_cast<unsigned long>(lastScanMs));
  for (uint8_t i = 0; i < activeChannels; ++i) {
    Serial.printf("# ch%u offset=%.1f cnt\n", i + 1, models[i].offset());
  }
}

bool taskComplete() {
  for (uint8_t i = 0; i < activeChannels; ++i) {
    if (acc[i].count() < cfg::STATS_SAMPLES) {
      return false;
    }
  }
  return true;
}

void finishTask() {
  for (uint8_t i = 0; i < activeChannels; ++i) {
    if (task == Task::Tare) {
      models[i].setOffset(acc[i].mean());
      Serial.printf("# ch%u tara: offset=%.1f cnt (std %.1f)\n", i + 1, acc[i].mean(), acc[i].stddev());
    } else {
      const double uvv = acc[i].stddev() * models[i].mvvPerCount() * 1000.0;
      Serial.printf("# ch%u media=%.5f mV/V  rumore=%.4f uV/V rms = %.1f nV rms  p-p=%ld cnt\n",
                    i + 1, models[i].countsToMvV(acc[i].mean()), uvv, uvv * cfg::VREF_V * 1000.0,
                    static_cast<long>(acc[i].max() - acc[i].min()));
    }
  }
  task = Task::Idle;
}

// --- Comandi ---

void handleCommand(const Command &cmd, uint32_t now) {
  switch (cmd.type) {
    case Command::Type::None:
      break;
    case Command::Type::Tare:
      startTask(Task::Tare);
      break;
    case Command::Type::Stats:
      startTask(Task::Stats);
      break;
    case Command::Type::OffsetCal:
      calibratePending = true;
      ui.message("calibrazione offset alla prossima lettura");
      break;
    case Command::Type::Speed:
      adc.setSpeed(!adc.fast());
      restartScan(now);
      ui.message(adc.fast() ? "80 SPS" : "10 SPS");
      break;
    case Command::Type::Channels:
      if (cmd.hasArg && cmd.arg >= 1 && cmd.arg <= cfg::CHANNELS_MAX) {
        activeChannels = static_cast<uint8_t>(cmd.arg);
        restartScan(now);
        Serial.printf("# canali attivi: %u\n", activeChannels);
      } else {
        ui.message("uso: n <1-4>");
      }
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

void acquire(uint32_t now) {
  int32_t raw = 0;
  const bool cal = calibratePending;
  const Ads123xDriver::Status st = adc.read(raw, cal);

  if (st == Ads123xDriver::Status::NotReady) {
    if (!timeoutReported && now - waitSinceMs > timeoutMs()) {
      ui.message("ERRORE: DRDY non scende (alimentazioni, PDWN, cablaggio DOUT/SCLK)");
      timeoutReported = true;
    }
    return;
  }
  waitSinceMs = now;
  if (timeoutReported) {
    ui.message("ADC di nuovo presente");
    timeoutReported = false;
  }

  if (cal) {                         // il dato letto viene scartato, l'ADC si sta calibrando
    calibratePending = false;
    calibrating = true;
    return;
  }
  if (calibrating) {
    calibrating = false;
    ui.message("calibrazione offset completata");
  }

  if (st == Ads123xDriver::Status::Saturated && now - lastSatWarnMs > cfg::WARN_PERIOD_MS) {
    Serial.printf("# ATTENZIONE: ch%u in saturazione\n", current + 1);
    lastSatWarnMs = now;
  }

  lastRaw[current] = raw;
  filters[current].push(raw);
  fresh[current] = true;
  if (task != Task::Idle) {
    acc[current].push(raw);
    if (taskComplete()) {
      finishTask();
    }
  }

  if (activeChannels > 1) {          // passa al canale successivo: il prossimo dato sarà già assestato
    current = static_cast<uint8_t>((current + 1) % activeChannels);
    adc.selectChannel(current);
    waitSinceMs = millis();
  }
  if (current == 0) {
    lastScanMs = now - scanStartMs;
    scanStartMs = now;
  }
}

void report(uint32_t now) {
  if (!streaming || task != Task::Idle || now - lastPrintMs < cfg::PRINT_MIN_PERIOD_MS) {
    return;
  }
  for (uint8_t i = 0; i < activeChannels; ++i) {
    if (!fresh[i]) {
      return;                        // stampa solo a scansione completa
    }
  }
  lastPrintMs = now;

  double total = 0.0;
  for (uint8_t i = 0; i < activeChannels; ++i) {
    fresh[i] = false;
    if (rawMode) {
      Serial.printf("raw%u:%ld\t", i + 1, static_cast<long>(lastRaw[i]));
    } else {
      const double mvv = models[i].countsToMvV(filters[i].mean());
      total += models[i].mvvToLoad(mvv);
      Serial.printf("ch%u:%.4f\t", i + 1, mvv);
    }
  }
  if (!rawMode) {
    Serial.printf("tot_%s:%.3f", cfg::CELL_UNIT, total);
  }
  Serial.println();
}

}  // namespace

namespace app {

void setup() {
  Serial.begin(cfg::SERIAL_BAUD);
  delay(200);
  adc.begin(cfg::START_FAST);
  restartScan(millis());
  ui.banner();
  ui.message("eseguire 't' con tutti i simulatori allo zero");
}

void loop() {
  const uint32_t now = millis();
  handleCommand(ui.poll(), now);
  acquire(now);
  report(now);
}

}  // namespace app
