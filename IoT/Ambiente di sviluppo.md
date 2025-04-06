# Ambiente di Sviluppo IoT

## Strumenti di Sviluppo Software

### Arduino IDE
- Versione: 2.3.5
- Caratteristiche:
  - Interfaccia moderna con editor di codice migliorato
  - Migliore segnalazione degli errori
  - Schede file per sketch multipli
  - Autocompletamento avanzato
  - Debugger in tempo reale
  - Funzione di archiviazione sketch

### Pacchetto Supporto ESP32

```cpp
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```
- Versione: 3.2.0
- Componenti:
  - Definizioni scheda ESP32
  - Librerie core
  - Livello di astrazione hardware

## Framework ESP-IDF
- Versione: 5.2.0 (rilasciato Gennaio 2024, compatibile con ESP32 v3.2.0)
- Caratteristiche principali:
  - Sistema operativo real-time FreeRTOS
  - Stack Wi-Fi e Bluetooth
  - Rete TCP/IP
  - Driver per periferiche
  - Funzionalità di sicurezza
  - Supporto Matter 1.0
  - Miglioramenti prestazioni Wi-Fi
  - Ottimizzazione consumo energetico
  - Supporto ESP RainMaker
  - Funzionalità avanzate Bluetooth 5.3

### Caratteristiche dell'Ambiente di Sviluppo
- Supporto multipiattaforma (Windows, macOS, Linux)
- Capacità di debug integrato
- Monitor seriale per comunicazione dispositivo
- Gestore librerie per facile gestione dipendenze
- Supporto per:
  - ESP32
  - ESP32-S2
  - ESP32-C3
  - ESP32-S3
  - ESP32-C6

### Sistema di Build
- Sistema di build basato su CMake
- Gestione automatizzata delle dipendenze
- Architettura basata su componenti
- Supporto tabella partizioni personalizzata

### Supporto Linguaggi di Programmazione
- C/C++
- MicroPython
- Compatibilità framework Arduino:
  - Supporto completo per librerie Arduino standard
  - Compatibilità con la maggior parte delle librerie di terze parti
  - API Arduino standard completamente implementate
  - Funzioni specifiche ESP32 accessibili attraverso Arduino
  - Gestione automatica della memoria Flash
  - Supporto per:
    - Tutti i pin GPIO
    - Comunicazione I2C/SPI/UART
    - ADC/DAC
    - Timer hardware
    - PWM
    - Interrupt hardware
  - Coesistenza con ESP-IDF nativi
  - Possibilità di utilizzare funzioni ESP-IDF all'interno di sketch Arduino
