// config.h — parametri del lettore ADS1234 (unico file da modificare per adattare l'hardware)
#pragma once
#include <stdint.h>
#include <stddef.h>

namespace cfg {

// --- Pin ADS1234 <-> ESP32 (DVDD dell'ADS1234 a 3,3 V: livelli logici compatibili) ---
constexpr uint8_t PIN_DOUT  = 16;  // DRDY/DOUT (ingresso)
constexpr uint8_t PIN_SCLK  = 4;   // SCLK
constexpr uint8_t PIN_A0    = 25;  // selezione canale, bit 0
constexpr uint8_t PIN_A1    = 26;  // selezione canale, bit 1
constexpr uint8_t PIN_PDWN  = 27;  // power-down / reset (pull-down 100 kOhm consigliato)
constexpr uint8_t PIN_SPEED = 14;  // 0 = 10 SPS, 1 = 80 SPS

// --- Seriale ---
constexpr uint32_t SERIAL_BAUD = 115200;

// --- ADC ---
constexpr float   ADC_GAIN       = 128.0f;  // deve corrispondere a GAIN1/GAIN0 cablati (11 = 128)
constexpr float   VREF_V         = 5.0f;    // tensione su REFP-REFN, solo per esprimere il rumore in nV
constexpr bool    START_FAST     = false;   // false = 10 SPS (minimo rumore), true = 80 SPS
constexpr uint8_t CHANNELS_MAX   = 4;
constexpr uint8_t START_CHANNELS = 4;       // canali attivi all'avvio (1..4)

// Timeout di attesa dato: il cambio canale tiene DRDY alto 401 ms (10 SPS) o 51 ms (80 SPS);
// la calibrazione dell'offset 801 ms o 101 ms. Margine circa x2 per la tolleranza dell'oscillatore.
constexpr uint32_t SETTLE_TIMEOUT_SLOW_MS = 1000;
constexpr uint32_t SETTLE_TIMEOUT_FAST_MS = 200;
constexpr uint32_t CAL_TIMEOUT_SLOW_MS    = 1800;
constexpr uint32_t CAL_TIMEOUT_FAST_MS    = 300;

// --- Elaborazione ---
constexpr size_t   FILTER_LEN       = 4;    // media mobile per canale [campioni]
constexpr size_t   STATS_SAMPLES    = 20;   // campioni per canale per tara e statistiche
constexpr uint32_t PRINT_MIN_PERIOD_MS = 100;
constexpr uint32_t WARN_PERIOD_MS   = 2000;

// --- Celle di carico (uguali su tutti i canali) ---
constexpr float CELL_SENS_MV_V = 2.0f;   // sensibilità nominale a fondo scala [mV/V]
constexpr float CELL_CAPACITY  = 10.0f;  // portata nominale di ogni cella
constexpr char  CELL_UNIT[]    = "kg";

}  // namespace cfg
