// app.cpp — logica applicativa: acquisizione, macchina a stati dei comandi, stampa
// Hardware: ESP32 DevKit + modulo HX711 + simulatore resistivo (configurazione A o B della dispensa)
#include "app.h"
#include "config.h"
#include "hx711_driver.h"
#include "dsp.h"
#include "load_model.h"
#include "serial_ui.h"

// Operazione in corso che accumula STATS_SAMPLES campioni
enum class Task : uint8_t { Idle, Tare, Stats, Span };

static Hx711Driver hx(cfg::PIN_HX_DOUT, cfg::PIN_HX_SCK, cfg::HX_EXTRA_PULSES);
static LoadModel model(cfg::HX_GAIN, cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY);
static SerialUi ui(Serial);
static MovingAverage<cfg::FILTER_LEN> filter;
static RunningStats acc;

static Task task = Task::Idle;
static double spanReference = 0.0;
static bool streaming = true;
static bool rawMode = false;
static int32_t lastRaw = 0;
static uint8_t warmupLeft = cfg::HX_WARMUP_SAMPLES;
static uint32_t lastSampleMs = 0;
static uint32_t lastPrintMs = 0;
static uint32_t lastSatWarnMs = 0;
static bool timeoutReported = false;

// --- Gestione comandi ---

static void startTask(Task t) {
  acc.reset();
  task = t;
  ui.message("acquisizione in corso...");
}

static void printInfo() {
  Serial.printf("# DT=GPIO%u  SCK=GPIO%u  gain=%.0f  impulsi extra=%u\n",
                cfg::PIN_HX_DOUT, cfg::PIN_HX_SCK, cfg::HX_GAIN, cfg::HX_EXTRA_PULSES);
  Serial.printf("# risoluzione teorica=%.4e mV/V per conteggio\n", model.mvvPerCount());
  Serial.printf("# cella: %.3f mV/V = %.3f %s\n", cfg::CELL_SENS_MV_V, cfg::CELL_CAPACITY, cfg::CELL_UNIT);
  Serial.printf("# offset=%.1f cnt  span=%.5f\n", model.offset(), model.spanFactor());
}

static void handleCommand(const Command &cmd) {
  switch (cmd.type) {
    case Command::Type::None:
      break;
    case Command::Type::Tare:
      startTask(Task::Tare);
      break;
    case Command::Type::Stats:
      startTask(Task::Stats);
      break;
    case Command::Type::Span:
      spanReference = cmd.arg;
      startTask(Task::Span);
      break;
    case Command::Type::SpanReset:
      model.resetSpan();
      ui.message("span azzerato (fattore 1)");
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

// --- Chiusura delle operazioni a campioni ---

static void finishTask() {
  switch (task) {
    case Task::Tare:
      model.setOffset(acc.mean());
      Serial.printf("# tara eseguita: offset=%.1f cnt (std %.1f)\n", acc.mean(), acc.stddev());
      break;
    case Task::Stats: {
      StatsReport r;
      r.n = acc.count();
      r.meanCounts = acc.mean();
      r.stdCounts = acc.stddev();
      r.minCounts = acc.min();
      r.maxCounts = acc.max();
      r.meanMvV = model.countsToMvV(acc.mean());
      r.stdUvV = acc.stddev() * model.mvvPerCount() * model.spanFactor() * 1000.0;
      ui.stats(r);
      break;
    }
    case Task::Span:
      if (model.calibrateSpan(acc.mean(), spanReference)) {
        Serial.printf("# span calibrato: fattore=%.5f\n", model.spanFactor());
      } else {
        ui.message("span rifiutato: segnale troppo piccolo o fattore fuori 0,5..2 (verificare tara e segno)");
      }
      break;
    case Task::Idle:
      break;
  }
  task = Task::Idle;
}

// --- Acquisizione ---

static void acquire(uint32_t now) {
  int32_t raw = 0;
  const Hx711Driver::Status st = hx.read(raw);

  if (st == Hx711Driver::Status::NotReady) {
    if (!timeoutReported && now - lastSampleMs > cfg::HX_READY_TIMEOUT_MS) {
      ui.message("ERRORE: nessun dato dall'HX711 (alimentazione, DT/SCK, GND comune)");
      timeoutReported = true;
    }
    return;
  }

  lastSampleMs = now;
  if (timeoutReported) {
    ui.message("HX711 di nuovo presente");
    timeoutReported = false;
  }

  if (warmupLeft > 0) {           // primi campioni dopo l'accensione: assestamento
    --warmupLeft;
    return;
  }

  if (st == Hx711Driver::Status::Saturated && now - lastSatWarnMs > cfg::WARN_PERIOD_MS) {
    ui.message("ATTENZIONE: ADC in saturazione (offset o fondo scala del simulatore eccessivi)");
    lastSatWarnMs = now;
  }

  lastRaw = raw;
  filter.push(raw);

  if (task != Task::Idle) {
    acc.push(raw);
    if (acc.count() >= cfg::STATS_SAMPLES) {
      finishTask();
    }
  }
}

static void report(uint32_t now) {
  if (!streaming || task != Task::Idle || !filter.full()) {
    return;
  }
  if (now - lastPrintMs < cfg::PRINT_PERIOD_MS) {
    return;
  }
  lastPrintMs = now;

  if (rawMode) {
    ui.sampleRaw(lastRaw, filter.mean());
  } else {
    const double mvv = model.countsToMvV(filter.mean());
    ui.sampleEng(mvv, model.mvvToLoad(mvv), cfg::CELL_UNIT);
  }
}

namespace app {

void setup() {
  Serial.begin(cfg::SERIAL_BAUD);
  delay(200);
  hx.begin();
  lastSampleMs = millis();
  ui.banner();
  ui.message("eseguire 't' a simulatore in posizione di zero");
}

void loop() {
  const uint32_t now = millis();
  handleCommand(ui.poll());
  acquire(now);
  report(now);
}

}  // namespace app
