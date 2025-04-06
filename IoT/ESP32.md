# ESP32 - Guida Completa

## Panoramica
ESP32 è un microcontrollore System-on-Chip (SoC) sviluppato da Espressif Systems che integra Wi-Fi e Bluetooth in un unico chip.

## Caratteristiche Hardware Principali

### Processore
- CPU dual-core Xtensa LX6 32-bit fino a 240MHz
- Processore ULP (Ultra Low Power) per operazioni in standby
- 520 KB di SRAM
- 448 KB di ROM

### Connettività Wireless
- Wi-Fi 802.11 b/g/n
- Bluetooth 4.2 e BLE (Bluetooth Low Energy)
- Antenna integrata
- Range fino a 400m

### GPIO e Interfacce
- 34 GPIO programmabili
- 12-bit ADC fino a 18 canali
- 2 DAC a 8-bit
- 10 sensori touch capacitivi
- 4 interfacce SPI
- 2 interfacce I²C
- 2 interfacce I²S
- 3 UART
- Host SD/SDIO/MMC
- Ethernet MAC interface
- CAN 2.0
- IR (TX/RX)
- Motore PWM

### Caratteristiche di Sicurezza
- Supporto per crittografia:
  - AES
  - SHA
  - RSA
  - ECC
  - RNG (Random Number Generator)
- Secure Boot
- Flash encryption

## Varianti Principali

### ESP32-WROOM
- Modulo più comune
- Flash memory integrata
- Antenna PCB
- Ideale per applicazioni IoT generiche

### ESP32-WROVER
- Simile al WROOM
- Include PSRAM aggiuntiva
- Migliore per applicazioni con maggiore necessità di memoria

### ESP32-SOLO
- Versione single-core
- Costo ridotto
- Consumi inferiori

### ESP32-PICO
- Design ultra-compatto
- Integrazione maggiore
- Ideale per dispositivi indossabili

## Modalità di Risparmio Energetico
1. Active Mode: ~160-260mA
2. Modem-sleep: ~3-20mA
3. Light-sleep: ~0.8mA
4. Deep-sleep: ~10µA

## Applicazioni Tipiche
- IoT (Internet of Things)
- Automazione domestica
- Dispositivi indossabili
- Controllo industriale
- Reti mesh
- Beacon Bluetooth
- Sistemi di sicurezza
- Audio wireless

## Ambienti di Sviluppo
- Arduino IDE
- ESP-IDF (Framework ufficiale Espressif)
- PlatformIO
- MicroPython
- LUA (NodeMCU)

## Caratteristiche Speciali
- Boot rapido da deep sleep (<1ms)
- Supporto per RTOS
- Correzione errori cache
- DMA su tutte le periferiche
- Filtro di rumore digitale
- Hall sensor
- Sensore di temperatura

## Risorse e Link Utili
- [Documentazione Ufficiale ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [ESP32 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)
- [GitHub Espressif](https://github.com/espressif)

## Note sulla Programmazione
- Supporto per FreeRTOS
- Programmabile in:
  - C/C++
  - MicroPython
  - JavaScript (Espruino)
  - LUA
  - Arduino framework
