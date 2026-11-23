// config.h — parametri del progetto (unico file da modificare per adattare l'hardware)
#pragma once
#include <stdint.h>
#include <stddef.h>

namespace cfg {

// --- Pin HX711 (evitare i pin di strapping 0, 2, 5, 12, 15) ---
constexpr uint8_t PIN_HX_DOUT = 16;  // ingresso dati (DT del modulo)
constexpr uint8_t PIN_HX_SCK  = 4;   // uscita clock (SCK del modulo)

// --- Seriale ---
constexpr uint32_t SERIAL_BAUD = 115200;

// --- HX711 ---
// Impulsi aggiuntivi dopo i 24 bit: 1 = canale A gain 128, 2 = canale B gain 32, 3 = canale A gain 64
constexpr uint8_t  HX_EXTRA_PULSES      = 1;
constexpr float    HX_GAIN              = 128.0f;  // deve corrispondere a HX_EXTRA_PULSES
constexpr uint32_t HX_READY_TIMEOUT_MS  = 1000;    // nessun dato oltre questo tempo: modulo assente
constexpr uint8_t  HX_WARMUP_SAMPLES    = 4;       // campioni scartati dopo l'accensione

// --- Elaborazione ---
constexpr size_t   FILTER_LEN       = 8;    // lunghezza media mobile [campioni]
constexpr size_t   STATS_SAMPLES    = 50;   // campioni per tara, statistiche, span
constexpr uint32_t PRINT_PERIOD_MS  = 200;  // periodo di stampa in streaming
constexpr uint32_t WARN_PERIOD_MS   = 2000; // periodo minimo tra due avvisi uguali

// --- Cella di carico simulata (conversione in unità ingegneristiche) ---
constexpr float CELL_SENS_MV_V = 2.0f;   // sensibilità nominale a fondo scala [mV/V]
constexpr float CELL_CAPACITY  = 10.0f;  // portata nominale
constexpr char  CELL_UNIT[]    = "kg";

}  // namespace cfg
