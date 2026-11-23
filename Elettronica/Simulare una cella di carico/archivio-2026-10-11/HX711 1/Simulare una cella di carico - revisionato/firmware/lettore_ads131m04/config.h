// config.h — parametri del lettore ADS131M04 (unico file da modificare per adattare l'hardware)
#pragma once
#include <stdint.h>
#include <stddef.h>

namespace cfg {

// --- Pin ESP32 <-> ADS131M04 (evitati i pin di strapping 0, 2, 5, 12, 15) ---
constexpr uint8_t PIN_SCLK  = 18;  // SCLK
constexpr uint8_t PIN_MISO  = 19;  // DOUT dell'ADS131M04
constexpr uint8_t PIN_MOSI  = 23;  // DIN dell'ADS131M04
constexpr uint8_t PIN_CS    = 25;  // CS, attivo basso
constexpr uint8_t PIN_DRDY  = 26;  // DRDY, attivo basso
constexpr uint8_t PIN_SYNC  = 27;  // SYNC/RESET, attivo basso
constexpr uint8_t PIN_CLKIN = 32;  // clock master generato dall'ESP32 (LEDC)

// --- Clock e interfaccia ---
constexpr uint32_t CLKIN_HZ    = 8000000;  // 80 MHz / 10: esatto con LEDC; ammessi 0,3..8,4 MHz in alta risoluzione
constexpr uint8_t  LEDC_CHANNEL = 0;       // usato solo con core Arduino-ESP32 2.x
constexpr uint32_t SPI_HZ      = 8000000;  // SCLK; il dispositivo accetta fino a 25 MHz
constexpr uint32_t SERIAL_BAUD = 115200;

// --- Conversione ---
// OSR: 0=128, 1=256, 2=512, 3=1024, 4=2048, 5=4096, 6=8192, 7=16384
constexpr uint8_t OSR_CODE     = 7;
constexpr bool    GLOBAL_CHOP  = true;     // elimina l'offset interno, rumore / sqrt(2), dato ogni 3 conversioni
constexpr uint8_t GC_DLY_CODE  = 3;        // ritardo dopo l'inversione degli ingressi (valore di reset)
constexpr bool    CHECK_CRC    = true;     // verifica del CRC di uscita (CCITT, seme FFFFh)
constexpr uint8_t DISCARD_FRAMES = 4;      // il dispositivo non blocca i dati non assestati

// --- Canali: 0..2 celle, 3 misura dell'eccitazione tramite partitore ---
constexpr uint8_t CHANNELS      = 4;
constexpr uint8_t CELL_CHANNELS = 3;
constexpr uint8_t GAIN[CHANNELS] = {128, 128, 128, 1};  // potenze di 2 da 1 a 128
constexpr uint8_t VEX_CHANNEL   = 3;
constexpr float   VEX_DIVIDER   = 4.0f;    // Vex = V(ch3) x 4 con partitore 3 kOhm + 1 kOhm allo 0,1%
constexpr float   VEX_MIN_V     = 1.0f;    // sotto questa soglia l'eccitazione è considerata assente
constexpr float   VREF_V        = 1.2f;    // riferimento interno

// --- Elaborazione ---
constexpr size_t   FILTER_LEN      = 16;   // media mobile [campioni]
constexpr size_t   STATS_SAMPLES   = 200;  // circa 2,5 s a 81 campioni/s
constexpr uint32_t PRINT_PERIOD_MS = 200;
constexpr uint32_t WARN_PERIOD_MS  = 2000;
constexpr uint32_t DRDY_TIMEOUT_MS = 500;

// --- Celle di carico ---
constexpr float CELL_SENS_MV_V = 2.0f;
constexpr float CELL_CAPACITY  = 10.0f;
constexpr char  CELL_UNIT[]    = "kg";

}  // namespace cfg
