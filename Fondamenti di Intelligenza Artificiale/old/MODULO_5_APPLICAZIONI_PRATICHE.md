# 📘 MODULO 5
# Applicazioni Pratiche e Progetti Avanzati
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 8 ore | Livello: Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione al Modulo Pratico](#1-introduzione-al-modulo-pratico)
2. [Metodologia Progetti con IA](#2-metodologia-progetti-con-ia)
3. [Progetto 1: Sistema IoT Completo](#3-progetto-1-sistema-iot-completo)
4. [Progetto 2: Data Logger Industriale](#4-progetto-2-data-logger-industriale)
5. [Progetto 3: Controllo PID con Arduino](#5-progetto-3-controllo-pid-con-arduino)
6. [Progetto 4: Sistema Automazione Domestica](#6-progetto-4-sistema-automazione-domestica)
7. [Integrazione Cloud e Visualizzazione](#7-integrazione-cloud-e-visualizzazione)
8. [Machine Learning su Embedded](#8-machine-learning-su-embedded)
9. [Testing e Quality Assurance](#9-testing-e-quality-assurance)
10. [Sicurezza nei Sistemi IoT](#10-sicurezza-nei-sistemi-iot)
11. [Ottimizzazione e Performance](#11-ottimizzazione-e-performance)
12. [Deployment e Manutenzione](#12-deployment-e-manutenzione)
13. [Documentazione Progetti](#13-documentazione-progetti)
14. [Presentazione e Portfolio](#14-presentazione-e-portfolio)
15. [Esercitazioni Guidate](#15-esercitazioni-guidate)

---

## 1. Introduzione al Modulo Pratico

### 1.1 Obiettivi del Modulo

Questo modulo integra **tutte le competenze** acquisite nei moduli precedenti:

**Fondamenti teorici (Modulo 1):**
- Comprensione architetture IA
- Modelli generativi e loro applicazioni
- Limiti e opportunità dell'IA

**Prompt Engineering (Modulo 2):**
- Tecniche avanzate di prompting
- Iterazione e ottimizzazione prompt
- Gestione contesto e vincoli

**Programmazione C (Modulo 3):**
- Gestione memoria e puntatori
- Strutture dati efficienti
- Debugging e validazione

**Arduino/Embedded (Modulo 4):**
- Hardware e sensori
- Comunicazioni e protocolli
- Architetture embedded

**Risultato finale:** Portfolio di progetti completi professionali pronti per presentazione a colloqui e aziende.

### 1.2 Competenze Acquisite

Al termine del modulo sarai in grado di:

```
✅ PROGETTAZIONE
- Analizzare requisiti cliente
- Progettare architetture IoT complete
- Scegliere componenti ottimali
- Stimare tempi e costi

✅ SVILUPPO
- Implementare progetti complessi con IA
- Integrare sensori e attuatori
- Gestire comunicazioni cloud
- Implementare algoritmi controllo

✅ TESTING
- Creare test suite complete
- Validare prestazioni sistema
- Gestire edge cases
- Debugging efficace

✅ DEPLOYMENT
- Configurare ambienti produzione
- Gestire aggiornamenti OTA
- Monitorare sistemi remoti
- Manutenzione proattiva

✅ COMUNICAZIONE
- Documentare progetti professionalmente
- Presentare soluzioni tecniche
- Creare demo efficaci
- Portfolio GitHub curato
```

### 1.3 Struttura Progetti

Ogni progetto segue questo template standardizzato:

```
┌─────────────────────────────────────┐
│     FASE 1: ANALISI REQUISITI       │
├─────────────────────────────────────┤
│ - Definizione obiettivi             │
│ - Analisi fattibilità               │
│ - Scelta componenti                 │
│ - Stima risorse                     │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     FASE 2: DESIGN ARCHITETTURA     │
├─────────────────────────────────────┤
│ - Schema sistema                    │
│ - Diagrammi flusso                  │
│ - Schema elettrico                  │
│ - Struttura software                │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     FASE 3: IMPLEMENTAZIONE         │
├─────────────────────────────────────┤
│ - Setup hardware                    │
│ - Codice modulare (con IA)          │
│ - Integrazione componenti           │
│ - Debug e validazione               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     FASE 4: TESTING                 │
├─────────────────────────────────────┤
│ - Test unitari                      │
│ - Test integrazione                 │
│ - Test stress                       │
│ - Test campo                        │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│     FASE 5: DEPLOYMENT              │
├─────────────────────────────────────┤
│ - Configurazione produzione         │
│ - Monitoraggio                      │
│ - Documentazione                    │
│ - Training utente                   │
└─────────────────────────────────────┘
```

### 1.4 Strumenti e Tecnologie

**Hardware:**
- Arduino Uno, Mega, Nano
- ESP32 (WiFi/Bluetooth)
- Sensori vari (DHT22, BMP280, MQ-135, ecc.)
- Display (LCD, OLED, TFT)
- Moduli comunicazione (WiFi, LoRa, GSM)

**Software:**
- Arduino IDE / PlatformIO
- VS Code con estensioni
- Git per versioning
- Fritzing per schemi

**Cloud & Services:**
- ThingSpeak
- MQTT Broker (Mosquitto, HiveMQ)
- Node-RED per dashboard
- InfluxDB + Grafana
- AWS IoT / Azure IoT

**AI Tools:**
- Claude/ChatGPT per codice
- GitHub Copilot
- Edge Impulse per ML
- TensorFlow Lite Micro

---

## 2. Metodologia Progetti con IA

### 2.1 Workflow Professionale Dettagliato

#### FASE 1: ANALISI (1-2 ore)

**Checklist Analisi Requisiti:**
```
□ Definizione problema precisa
  - Cosa deve fare il sistema?
  - Quali sono i vincoli?
  - Chi sono gli utenti finali?

□ Requisiti funzionali
  - Elenco funzionalità prioritarie
  - Casi d'uso principali
  - Interfacce utente necessarie

□ Requisiti non-funzionali
  - Prestazioni (latenza, throughput)
  - Affidabilità (uptime richiesto)
  - Ambiente operativo (temp, umidità)
  - Consumo energetico
  - Costo target

□ Analisi fattibilità
  - Verifica fattibilità tecnica
  - Stima costi componenti
  - Valutazione alternative
```

**Esempio: Sistema Monitoraggio Serra**

```markdown
REQUISITI FUNZIONALI:
1. Misurare temp, umidità, luce ogni 5 minuti
2. Controllare irrigazione automatica
3. Aprire/chiudere finestre ventilazione
4. Inviare dati a cloud per analisi
5. Allarmi SMS per anomalie

REQUISITI NON-FUNZIONALI:
- Precisione temp: ±0.5°C
- Uptime: >99% (max 7h downtime/mese)
- Batteria backup: 24h
- Range WiFi: 50m
- Costo target: <200€
- Temperatura operativa: 0-60°C

VINCOLI:
- Alimentazione: 230V AC con backup batteria
- Connettività: WiFi 2.4GHz
- Montaggio: IP65 waterproof
```

#### FASE 2: DESIGN (2-3 ore)

**Architettura Sistema:**

```
LIVELLO 1: SENSORI
├─ DHT22 (temp/umidità)
├─ BH1750 (lux meter)
└─ Soil moisture sensor

LIVELLO 2: CONTROLLER
├─ ESP32 main
├─ RTC DS3231
└─ SD card logging

LIVELLO 3: ATTUATORI
├─ Pompa acqua (relay)
├─ Servo finestre
└─ LED grow lights

LIVELLO 4: COMUNICAZIONE
├─ WiFi → MQTT broker
├─ SMS alerts (GSM module)
└─ Web server locale

LIVELLO 5: ALIMENTAZIONE
├─ 5V regulator
└─ LiPo backup battery
```

**Schema Elettrico - Organizzazione Pin:**

```cpp
// config.h - Pin Definitions
#define DHT22_PIN       4
#define SOIL_MOISTURE   A0
#define LIGHT_SENSOR_SDA 21
#define LIGHT_SENSOR_SCL 22

#define RELAY_PUMP      25
#define SERVO_WINDOW    26
#define LED_GROW        27

#define SD_CS           5
#define RTC_SDA         21  // shared I2C
#define RTC_SCL         22  // shared I2C
```

#### FASE 3: IMPLEMENTAZIONE (10-20 ore)

**Strategie Uso IA:**

```
COSA DELEGARE ALL'IA:
✅ Generazione codice boilerplate
   "Crea classe Sensor con metodi read(), validate(), getAverage()"

✅ Implementazione protocolli standard
   "Implementa client MQTT con reconnect automatico"

✅ Parsing e formattazione dati
   "Funzione per convertire struct SensorData in JSON"

✅ Gestione errori comuni
   "Aggiungi try-catch e logging errori per file I/O"

COSA FARE PERSONALMENTE:
⚠️ Decisioni architetturali
   - Scegliere state machine vs event-driven
   - Definire struttura dati ottimale

⚠️ Tuning parametri sistema
   - Soglie allarmi temperatura
   - Tempo irrigazione
   - Intervalli campionamento

⚠️ Validazione hardware
   - Test collegamenti
   - Verifica consumi
   - Calibrazione sensori

⚠️ Integrazione finale
   - Orchestrazione moduli
   - Gestione casi limite
   - Ottimizzazione performance
```

**Sviluppo Modulare:**

```cpp
// Struttura progetto modulare
greenhouse_control/
├── src/
│   ├── main.cpp              // Entry point
│   ├── sensors/
│   │   ├── dht_sensor.cpp
│   │   ├── soil_sensor.cpp
│   │   └── light_sensor.cpp
│   ├── actuators/
│   │   ├── pump_control.cpp
│   │   └── window_control.cpp
│   ├── communication/
│   │   ├── mqtt_client.cpp
│   │   └── web_server.cpp
│   ├── storage/
│   │   └── sd_logger.cpp
│   └── config.h
└── test/
    └── unit_tests.cpp
```

#### FASE 4: VALIDAZIONE (2-4 ore)

**Piramide dei Test:**

```
         ╱╲
        ╱  ╲       E2E Tests (End-to-End)
       ╱____╲      - Test sistema completo
      ╱      ╲     - Scenari utente reali
     ╱        ╲
    ╱__________╲   Integration Tests
   ╱            ╲  - Interazione moduli
  ╱              ╲ - Test comunicazioni
 ╱________________╲
╱                  ╲ Unit Tests
╲__________________╱ - Singole funzioni
                     - Copertura 80%+
```

**Esempio Test Suite:**

```cpp
// test_sensors.cpp
void test_dht22_reading() {
    DHTSensor sensor(DHT22_PIN);

    // Test lettura valida
    SensorData data = sensor.read();
    assert(data.valid == true);
    assert(data.temperature >= -40 && data.temperature <= 80);
    assert(data.humidity >= 0 && data.humidity <= 100);
}

void test_dht22_error_handling() {
    DHTSensor sensor(INVALID_PIN);

    // Test gestione errore
    SensorData data = sensor.read();
    assert(data.valid == false);
    assert(sensor.getLastError() != ERROR_NONE);
}

void test_sensor_averaging() {
    DHTSensor sensor(DHT22_PIN);

    // Test media mobile
    for(int i = 0; i < 10; i++) {
        sensor.read();
        delay(100);
    }

    float avg = sensor.getAverage();
    assert(avg >= 0);  // Valid average
}
```

#### FASE 5: DOCUMENTAZIONE (2-3 ore)

**Documentazione Completa Include:**

```markdown
1. README.md principale
   - Overview progetto
   - Quick start
   - Requisiti hardware/software

2. docs/ARCHITECTURE.md
   - Diagrammi architettura
   - Scelte progettuali
   - Trade-off analizzati

3. docs/API.md
   - Interfacce pubbliche
   - Esempi uso

4. docs/HARDWARE.md
   - BOM (Bill of Materials)
   - Schema collegamenti
   - Specifiche componenti

5. docs/DEPLOYMENT.md
   - Guida installazione
   - Configurazione
   - Troubleshooting

6. CHANGELOG.md
   - Versioning
   - Breaking changes
```

### 2.2 Prompt Engineering per Progetti

**Template Prompt Completo:**

```
CONTESTO:
"Sto sviluppando [TIPO PROGETTO] per [SCOPO].

HARDWARE:
- MCU: [Arduino/ESP32/...]
- Sensori: [lista]
- Attuatori: [lista]
- Comunicazione: [WiFi/LoRa/...]

REQUISITI:
1. [Funzionalità 1]
2. [Funzionalità 2]
...

VINCOLI:
- Memoria disponibile: [KB RAM, KB Flash]
- Consumo massimo: [mA]
- Latenza massima: [ms]

TASK:
Implementa [FUNZIONALITÀ SPECIFICA] seguendo questi requisiti:
- [Requisito tecnico 1]
- [Requisito tecnico 2]

OUTPUT ATTESO:
- Codice C++ ben commentato
- Gestione errori completa
- Esempio di utilizzo
- Note su ottimizzazione

STILE CODICE:
- Usa convenzioni Arduino standard
- Preferisci const e constexpr
- Evita allocazioni dinamiche
- Usa enum class per stati"
```

**Esempio Prompt Specifico:**

```
CONTESTO:
"Sto sviluppando un sistema irrigazione automatica per serra.

HARDWARE:
- MCU: ESP32 DevKit v1
- Sensore: Capacitive soil moisture sensor
- Attuatore: 12V water pump via relay
- Comunicazione: WiFi + MQTT

REQUISITI:
1. Leggere umidità suolo ogni 5 minuti
2. Attivare pompa se umidità < 30%
3. Disattivare pompa se umidità > 70%
4. Pubblicare dati MQTT ogni update
5. Safety: max 10 minuti attivazione continua pompa

VINCOLI:
- Memoria: ESP32 ha 520KB RAM
- Consumo: Pompa 500mA @ 12V
- Latenza lettura sensore: <100ms

TASK:
Implementa classe IrrigationController con:
- Metodo update() da chiamare in loop
- State machine: IDLE, MEASURING, WATERING, ERROR
- Safety timer watchdog
- Callback per logging eventi

OUTPUT ATTESO:
- File irrigation_controller.h/.cpp
- Esempio di utilizzo in main
- Gestione errori (sensore disconnesso, MQTT down)
- Documentazione inline

STILE CODICE:
- Usa enum class per stati
- RAII per gestione risorse
- Non usare delay(), solo millis()
- Logging via Serial per debug"
```

**Iterazione Prompt:**

```
PROMPT INIZIALE:
"Crea funzione lettura sensore DHT22"

↓ [IA genera codice base]

PROMPT RAFFINAMENTO:
"Aggiungi gestione errori CRC e timeout.
Retry fino a 3 tentativi con backoff esponenziale.
Ritorna struct con campo 'valid' per indicare successo."

↓ [IA aggiunge error handling]

PROMPT OTTIMIZZAZIONE:
"Ottimizza per ridurre uso RAM.
Usa buffer statico invece di String.
Aggiungi PROGMEM per messaggi errore."

↓ [IA ottimizza memoria]

PROMPT TESTING:
"Genera unit test che verificano:
- Lettura corretta
- Gestione timeout
- Retry logic
- Validazione range valori"
```

---

## 3. Progetto 1: Sistema IoT Completo

### 3.1 Descrizione Progetto

**Nome:** Smart Environmental Monitor Pro

**Obiettivo:** Sistema professionale di monitoraggio ambientale multi-sensore con cloud upload, allarmi intelligenti e dashboard web.

**Specifiche Tecniche:**
```
SENSORI:
- DHT22: Temperatura (-40 a +80°C, ±0.5°C) e Umidità (0-100%, ±2%)
- BMP280: Pressione atmosferica (300-1100 hPa)
- MQ-135: Qualità aria (CO2, NH3, Benzene)
- BH1750: Luminosità (1-65535 lux)

ATTUATORI:
- Display OLED 128x64 SSD1306 (I2C)
- LED RGB WS2812B (NeoPixel)
- Buzzer piezoelettrico

COMUNICAZIONE:
- WiFi 2.4GHz (ESP32 integrato)
- MQTT protocol
- HTTP REST API
- Web server locale

STORAGE:
- SD card per data logging
- SPIFFS per configurazione

ALIMENTAZIONE:
- USB 5V (sviluppo)
- 12V DC con regolatore (produzione)
- Consumo: <500mA @ 5V
```

### 3.2 Architettura Dettagliata

```
┌─────────────────────────────────────────────────────────┐
│                    ESP32 Main Controller                │
│                    (Dual Core 240MHz)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CORE 0: Acquisizione & Controllo                      │
│  ┌────────────────────────────────────────────┐        │
│  │  Task Sensori (Priority 2)                 │        │
│  │  - Polling ogni 30s                        │        │
│  │  - Validazione dati                        │        │
│  │  - Media mobile                            │        │
│  └────────────────────────────────────────────┘        │
│  ┌────────────────────────────────────────────┐        │
│  │  Task Display (Priority 1)                 │        │
│  │  - Update UI ogni 1s                       │        │
│  │  - Gestione animazioni                     │        │
│  └────────────────────────────────────────────┘        │
│                                                         │
│  CORE 1: Comunicazioni                                 │
│  ┌────────────────────────────────────────────┐        │
│  │  Task WiFi/MQTT (Priority 3)               │        │
│  │  - Connessione WiFi                        │        │
│  │  - MQTT publish/subscribe                  │        │
│  │  - Web server HTTP                         │        │
│  └────────────────────────────────────────────┘        │
│  ┌────────────────────────────────────────────┐        │
│  │  Task Logging (Priority 0)                 │        │
│  │  - Write SD card                           │        │
│  │  - Buffering dati                          │        │
│  └────────────────────────────────────────────┘        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  PERIFERICHE                                            │
│  I2C Bus: OLED, BMP280, BH1750                         │
│  1-Wire: DHT22                                         │
│  Analog: MQ-135                                        │
│  SPI: SD Card                                          │
│  GPIO: LED RGB, Buzzer                                 │
└─────────────────────────────────────────────────────────┘
```

### 3.3 Implementazione Completa

#### Step 1: Definizione Strutture Dati

```cpp
// types.h - Strutture dati comuni
#ifndef TYPES_H
#define TYPES_H

#include <Arduino.h>

// Struttura dati sensori
typedef struct {
    float temperature;    // °C
    float humidity;       // %
    float pressure;       // hPa
    uint16_t light;       // lux
    uint16_t airQuality;  // PPM
    uint32_t timestamp;   // Unix timestamp
    bool valid;           // Flag validità
} SensorData;

// Configurazione soglie allarmi
typedef struct {
    float temp_warning_high;    // 30.0
    float temp_alarm_high;      // 35.0
    float temp_warning_low;     // 10.0
    float temp_alarm_low;       // 5.0
    float humidity_warning_high; // 70.0
    float humidity_warning_low;  // 30.0
    uint16_t air_quality_warning; // 200
    uint16_t air_quality_alarm;   // 400
} AlarmThresholds;

// Livelli allarme
enum class AlarmLevel {
    NONE = 0,
    WARNING = 1,
    ALARM = 2,
    CRITICAL = 3
};

// Stati sistema
enum class SystemState {
    INITIALIZING,
    IDLE,
    MEASURING,
    UPLOADING,
    ALARM,
    ERROR
};

#endif
```

#### Step 2: Classe Gestione Sensori

```cpp
// sensor_manager.h
#ifndef SENSOR_MANAGER_H
#define SENSOR_MANAGER_H

#include "types.h"
#include <DHT.h>
#include <Adafruit_BMP280.h>
#include <BH1750.h>

class SensorManager {
private:
    DHT dht;
    Adafruit_BMP280 bmp;
    BH1750 lightMeter;

    const uint8_t mq135Pin;
    const uint8_t movingAvgSize = 5;

    // Buffer per media mobile
    float tempBuffer[5];
    float humBuffer[5];
    uint8_t bufferIndex;

    // Stato sensori
    bool dhtInitialized;
    bool bmpInitialized;
    bool lightInitialized;

    // Metodi privati
    float calculateAverage(float* buffer, uint8_t size);
    bool validateReading(float value, float min, float max);
    uint16_t readAirQuality();

public:
    SensorManager(uint8_t dhtPin, uint8_t mq135Pin);

    bool begin();
    SensorData readAll();
    bool selfTest();
    String getStatus();
};

#endif

// sensor_manager.cpp
#include "sensor_manager.h"

SensorManager::SensorManager(uint8_t dhtPin, uint8_t mq135Pin)
    : dht(dhtPin, DHT22), mq135Pin(mq135Pin), bufferIndex(0),
      dhtInitialized(false), bmpInitialized(false), lightInitialized(false) {

    // Inizializza buffer a zero
    memset(tempBuffer, 0, sizeof(tempBuffer));
    memset(humBuffer, 0, sizeof(humBuffer));
}

bool SensorManager::begin() {
    Serial.println(F("[Sensor] Inizializzazione sensori..."));

    // Inizializza DHT22
    dht.begin();
    delay(2000);  // DHT needs time to stabilize
    float t = dht.readTemperature();
    dhtInitialized = !isnan(t);
    Serial.printf("[Sensor] DHT22: %s\n", dhtInitialized ? "OK" : "FAIL");

    // Inizializza BMP280
    bmpInitialized = bmp.begin(0x76);
    if(bmpInitialized) {
        bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                       Adafruit_BMP280::SAMPLING_X2,
                       Adafruit_BMP280::SAMPLING_X16,
                       Adafruit_BMP280::FILTER_X16,
                       Adafruit_BMP280::STANDBY_MS_500);
    }
    Serial.printf("[Sensor] BMP280: %s\n", bmpInitialized ? "OK" : "FAIL");

    // Inizializza BH1750
    lightInitialized = lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE);
    Serial.printf("[Sensor] BH1750: %s\n", lightInitialized ? "OK" : "FAIL");

    // Configura pin analogico MQ-135
    pinMode(mq135Pin, INPUT);

    return dhtInitialized && bmpInitialized && lightInitialized;
}

SensorData SensorManager::readAll() {
    SensorData data = {0};
    data.timestamp = millis() / 1000;

    // Lettura DHT22 con retry
    bool dhtOk = false;
    for(int attempt = 0; attempt < 3; attempt++) {
        float t = dht.readTemperature();
        float h = dht.readHumidity();

        if(!isnan(t) && !isnan(h) &&
           validateReading(t, -40, 80) &&
           validateReading(h, 0, 100)) {

            // Aggiungi a buffer media mobile
            tempBuffer[bufferIndex] = t;
            humBuffer[bufferIndex] = h;
            bufferIndex = (bufferIndex + 1) % movingAvgSize;

            data.temperature = calculateAverage(tempBuffer, movingAvgSize);
            data.humidity = calculateAverage(humBuffer, movingAvgSize);
            dhtOk = true;
            break;
        }
        delay(100);
    }

    // Lettura BMP280
    bool bmpOk = false;
    if(bmpInitialized) {
        float p = bmp.readPressure() / 100.0; // Convert Pa to hPa
        if(validateReading(p, 300, 1100)) {
            data.pressure = p;
            bmpOk = true;
        }
    }

    // Lettura BH1750
    bool lightOk = false;
    if(lightInitialized) {
        uint16_t lux = lightMeter.readLightLevel();
        if(lux != 0xFFFF) {  // Check for error value
            data.light = lux;
            lightOk = true;
        }
    }

    // Lettura MQ-135 (media di 10 campioni)
    uint32_t aqSum = 0;
    for(int i = 0; i < 10; i++) {
        aqSum += analogRead(mq135Pin);
        delay(10);
    }
    data.airQuality = aqSum / 10;

    // Validità complessiva
    data.valid = dhtOk && bmpOk && lightOk;

    return data;
}

float SensorManager::calculateAverage(float* buffer, uint8_t size) {
    float sum = 0;
    uint8_t validCount = 0;

    for(uint8_t i = 0; i < size; i++) {
        if(buffer[i] != 0) {  // Ignore uninitialized values
            sum += buffer[i];
            validCount++;
        }
    }

    return validCount > 0 ? sum / validCount : 0;
}

bool SensorManager::validateReading(float value, float min, float max) {
    return value >= min && value <= max;
}

bool SensorManager::selfTest() {
    Serial.println(F("\n=== SELF TEST SENSORI ==="));

    SensorData test = readAll();

    Serial.printf("DHT22:  %s (T=%.1f°C, H=%.1f%%)\n",
                  !isnan(test.temperature) ? "OK" : "FAIL",
                  test.temperature, test.humidity);

    Serial.printf("BMP280: %s (P=%.1f hPa)\n",
                  test.pressure > 0 ? "OK" : "FAIL",
                  test.pressure);

    Serial.printf("BH1750: %s (L=%d lux)\n",
                  test.light > 0 ? "OK" : "FAIL",
                  test.light);

    Serial.printf("MQ-135: OK (AQ=%d)\n", test.airQuality);

    Serial.printf("\nRisultato: %s\n", test.valid ? "PASS" : "FAIL");

    return test.valid;
}

String SensorManager::getStatus() {
    String status = "DHT:";
    status += dhtInitialized ? "OK " : "ERR ";
    status += "BMP:";
    status += bmpInitialized ? "OK " : "ERR ";
    status += "Light:";
    status += lightInitialized ? "OK" : "ERR";
    return status;
}
```

#### Step 3: Sistema Allarmi

```cpp
// alarm_system.h
#ifndef ALARM_SYSTEM_H
#define ALARM_SYSTEM_H

#include "types.h"

class AlarmSystem {
private:
    AlarmThresholds thresholds;
    AlarmLevel currentLevel;
    uint32_t lastAlarmTime;
    const uint32_t alarmCooldown = 60000; // 1 minuto

    // LED RGB
    const uint8_t ledPin;

    // Buzzer
    const uint8_t buzzerPin;
    bool buzzerEnabled;

    void setLEDColor(uint8_t r, uint8_t g, uint8_t b);
    void playAlarmTone(AlarmLevel level);

public:
    AlarmSystem(uint8_t ledPin, uint8_t buzzerPin);

    void begin();
    void setThresholds(AlarmThresholds thresh);
    AlarmLevel checkAlarms(const SensorData& data);
    void updateIndicators();
    void enableBuzzer(bool enable);
    AlarmLevel getCurrentLevel() const { return currentLevel; }
};

#endif

// alarm_system.cpp
#include "alarm_system.h"
#include <Adafruit_NeoPixel.h>

// NeoPixel per LED RGB
Adafruit_NeoPixel led(1, LED_PIN, NEO_GRB + NEO_KHZ800);

AlarmSystem::AlarmSystem(uint8_t ledPin, uint8_t buzzerPin)
    : ledPin(ledPin), buzzerPin(buzzerPin),
      currentLevel(AlarmLevel::NONE), lastAlarmTime(0), buzzerEnabled(true) {

    // Default thresholds
    thresholds.temp_warning_high = 30.0;
    thresholds.temp_alarm_high = 35.0;
    thresholds.temp_warning_low = 10.0;
    thresholds.temp_alarm_low = 5.0;
    thresholds.humidity_warning_high = 70.0;
    thresholds.humidity_warning_low = 30.0;
    thresholds.air_quality_warning = 300;
    thresholds.air_quality_alarm = 500;
}

void AlarmSystem::begin() {
    led.begin();
    led.setBrightness(50);
    led.show();

    pinMode(buzzerPin, OUTPUT);
    digitalWrite(buzzerPin, LOW);

    // Test LED sequence
    setLEDColor(255, 0, 0);   // Rosso
    delay(300);
    setLEDColor(0, 255, 0);   // Verde
    delay(300);
    setLEDColor(0, 0, 255);   // Blu
    delay(300);
    setLEDColor(0, 0, 0);     // Off
}

AlarmLevel AlarmSystem::checkAlarms(const SensorData& data) {
    if(!data.valid) {
        currentLevel = AlarmLevel::ERROR;
        return currentLevel;
    }

    AlarmLevel newLevel = AlarmLevel::NONE;

    // Check temperatura
    if(data.temperature > thresholds.temp_alarm_high ||
       data.temperature < thresholds.temp_alarm_low) {
        newLevel = AlarmLevel::ALARM;
    }
    else if(data.temperature > thresholds.temp_warning_high ||
            data.temperature < thresholds.temp_warning_low) {
        newLevel = max(newLevel, AlarmLevel::WARNING);
    }

    // Check umidità
    if(data.humidity > thresholds.humidity_warning_high ||
       data.humidity < thresholds.humidity_warning_low) {
        newLevel = max(newLevel, AlarmLevel::WARNING);
    }

    // Check qualità aria
    if(data.airQuality > thresholds.air_quality_alarm) {
        newLevel = AlarmLevel::ALARM;
    }
    else if(data.airQuality > thresholds.air_quality_warning) {
        newLevel = max(newLevel, AlarmLevel::WARNING);
    }

    // Update solo se cambiato o cooldown scaduto
    if(newLevel != currentLevel ||
       millis() - lastAlarmTime > alarmCooldown) {
        currentLevel = newLevel;
        lastAlarmTime = millis();
        updateIndicators();
    }

    return currentLevel;
}

void AlarmSystem::updateIndicators() {
    switch(currentLevel) {
        case AlarmLevel::NONE:
            setLEDColor(0, 255, 0);  // Verde
            digitalWrite(buzzerPin, LOW);
            break;

        case AlarmLevel::WARNING:
            setLEDColor(255, 255, 0);  // Giallo
            digitalWrite(buzzerPin, LOW);
            break;

        case AlarmLevel::ALARM:
            // Rosso lampeggiante
            if((millis() / 500) % 2 == 0) {
                setLEDColor(255, 0, 0);
            } else {
                setLEDColor(0, 0, 0);
            }

            if(buzzerEnabled) {
                playAlarmTone(AlarmLevel::ALARM);
            }
            break;

        case AlarmLevel::ERROR:
            setLEDColor(255, 0, 255);  // Magenta
            break;
    }
}

void AlarmSystem::setLEDColor(uint8_t r, uint8_t g, uint8_t b) {
    led.setPixelColor(0, led.Color(r, g, b));
    led.show();
}

void AlarmSystem::playAlarmTone(AlarmLevel level) {
    // Pattern buzzer basato su livello allarme
    switch(level) {
        case AlarmLevel::WARNING:
            tone(buzzerPin, 1000, 100);  // Beep singolo
            break;

        case AlarmLevel::ALARM:
            tone(buzzerPin, 2000, 100);  // Beep acuto
            delay(100);
            tone(buzzerPin, 1500, 100);  // Beep grave
            break;

        default:
            noTone(buzzerPin);
    }
}
```

#### Step 4: Display Manager

```cpp
// display_manager.h
#ifndef DISPLAY_MANAGER_H
#define DISPLAY_MANAGER_H

#include "types.h"
#include <Adafruit_SSD1306.h>

class DisplayManager {
private:
    Adafruit_SSD1306 display;
    uint32_t lastUpdate;
    const uint32_t updateInterval = 1000;  // 1s

    void drawScreen(const SensorData& data, SystemState state);
    void drawStatusBar(SystemState state, bool wifiConnected);
    void drawSensorData(const SensorData& data);
    void drawAlarmIcon(AlarmLevel level);

public:
    DisplayManager();

    bool begin();
    void update(const SensorData& data, SystemState state,
                bool wifiConnected, AlarmLevel alarmLevel);
    void showMessage(const char* msg, int duration = 2000);
    void showBootScreen();
};

#endif

// display_manager.cpp
#include "display_manager.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

DisplayManager::DisplayManager()
    : display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET),
      lastUpdate(0) {
}

bool DisplayManager::begin() {
    if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println(F("[Display] OLED init failed"));
        return false;
    }

    display.clearDisplay();
    display.setTextColor(SSD1306_WHITE);
    showBootScreen();

    return true;
}

void DisplayManager::showBootScreen() {
    display.clearDisplay();
    display.setTextSize(2);
    display.setCursor(10, 10);
    display.println(F("ENV-MON"));
    display.setTextSize(1);
    display.setCursor(20, 35);
    display.println(F("Starting..."));
    display.display();
    delay(2000);
}

void DisplayManager::update(const SensorData& data, SystemState state,
                           bool wifiConnected, AlarmLevel alarmLevel) {

    if(millis() - lastUpdate < updateInterval) {
        return;  // Throttle update rate
    }

    lastUpdate = millis();

    display.clearDisplay();
    drawStatusBar(state, wifiConnected);
    drawSensorData(data);
    drawAlarmIcon(alarmLevel);
    display.display();
}

void DisplayManager::drawStatusBar(SystemState state, bool wifiConnected) {
    display.setTextSize(1);
    display.setCursor(0, 0);

    // WiFi icon
    if(wifiConnected) {
        display.print(F("WiFi:OK"));
    } else {
        display.print(F("WiFi:--"));
    }

    // State
    display.setCursor(70, 0);
    switch(state) {
        case SystemState::IDLE: display.print(F("IDLE")); break;
        case SystemState::MEASURING: display.print(F("MEAS")); break;
        case SystemState::UPLOADING: display.print(F("UPLD")); break;
        case SystemState::ALARM: display.print(F("ALRM")); break;
        case SystemState::ERROR: display.print(F("ERR!")); break;
    }

    // Separatore
    display.drawLine(0, 10, SCREEN_WIDTH, 10, SSD1306_WHITE);
}

void DisplayManager::drawSensorData(const SensorData& data) {
    display.setTextSize(1);

    // Temperatura
    display.setCursor(0, 15);
    display.print(F("Temp: "));
    display.print(data.temperature, 1);
    display.print(F(" C"));

    // Umidità
    display.setCursor(0, 27);
    display.print(F("Hum:  "));
    display.print(data.humidity, 1);
    display.print(F(" %"));

    // Pressione
    display.setCursor(0, 39);
    display.print(F("Pres: "));
    display.print(data.pressure, 0);
    display.print(F("hPa"));

    // Luce
    display.setCursor(0, 51);
    display.print(F("Lux:  "));
    display.print(data.light);

    // Qualità aria (colonna destra)
    display.setCursor(70, 27);
    display.print(F("AQ:"));
    display.print(data.airQuality);
}

void DisplayManager::drawAlarmIcon(AlarmLevel level) {
    if(level == AlarmLevel::NONE) return;

    // Triangolo warning in alto a destra
    display.fillTriangle(115, 0, 128, 0, 121, 10, SSD1306_WHITE);

    if(level >= AlarmLevel::ALARM) {
        // Punto esclamativo
        display.fillRect(120, 2, 2, 5, SSD1306_BLACK);
        display.fillRect(120, 8, 2, 1, SSD1306_BLACK);
    }
}

void DisplayManager::showMessage(const char* msg, int duration) {
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(0, 28);
    display.println(msg);
    display.display();
    delay(duration);
}
```

#### Step 5: Cloud Communication (MQTT)

```cpp
// cloud_manager.h
#ifndef CLOUD_MANAGER_H
#define CLOUD_MANAGER_H

#include "types.h"
#include <WiFi.h>
#include <PubSubClient.h>

class CloudManager {
private:
    WiFiClient wifiClient;
    PubSubClient mqtt;

    const char* ssid;
    const char* password;
    const char* mqttServer;
    const uint16_t mqttPort;
    const char* mqttUser;
    const char* mqttPass;

    const char* deviceID;
    const char* topicData;
    const char* topicStatus;
    const char* topicAlarms;

    bool wifiConnected;
    bool mqttConnected;

    uint32_t lastReconnectAttempt;
    const uint32_t reconnectInterval = 5000;

    bool connectWiFi();
    bool connectMQTT();
    void mqttCallback(char* topic, byte* payload, unsigned int length);

public:
    CloudManager(const char* ssid, const char* password,
                const char* mqttServer, uint16_t mqttPort,
                const char* mqttUser, const char* mqttPass,
                const char* deviceID);

    bool begin();
    void loop();  // Call in main loop

    bool publishSensorData(const SensorData& data);
    bool publishAlarm(AlarmLevel level, const char* message);
    bool publishStatus(const char* status);

    bool isConnected() const { return wifiConnected && mqttConnected; }
    bool isWiFiConnected() const { return wifiConnected; }
};

#endif

// cloud_manager.cpp
#include "cloud_manager.h"
#include <ArduinoJson.h>

CloudManager::CloudManager(const char* ssid, const char* password,
                          const char* mqttServer, uint16_t mqttPort,
                          const char* mqttUser, const char* mqttPass,
                          const char* deviceID)
    : ssid(ssid), password(password),
      mqttServer(mqttServer), mqttPort(mqttPort),
      mqttUser(mqttUser), mqttPass(mqttPass),
      deviceID(deviceID), mqtt(wifiClient),
      wifiConnected(false), mqttConnected(false),
      lastReconnectAttempt(0) {

    // Build topic names
    topicData = (String("sensors/") + deviceID + "/data").c_str();
    topicStatus = (String("sensors/") + deviceID + "/status").c_str();
    topicAlarms = (String("sensors/") + deviceID + "/alarms").c_str();

    mqtt.setServer(mqttServer, mqttPort);
    mqtt.setCallback([this](char* topic, byte* payload, unsigned int length) {
        this->mqttCallback(topic, payload, length);
    });
}

bool CloudManager::begin() {
    Serial.println(F("[Cloud] Inizializzazione..."));

    if(!connectWiFi()) {
        return false;
    }

    if(!connectMQTT()) {
        Serial.println(F("[Cloud] MQTT connessione fallita (riproverò)"));
    }

    return true;
}

bool CloudManager::connectWiFi() {
    Serial.printf("[Cloud] Connessione WiFi a %s...\n", ssid);

    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    uint32_t startTime = millis();
    while(WiFi.status() != WL_CONNECTED && millis() - startTime < 20000) {
        delay(500);
        Serial.print(".");
    }
    Serial.println();

    wifiConnected = (WiFi.status() == WL_CONNECTED);

    if(wifiConnected) {
        Serial.print(F("[Cloud] WiFi connesso! IP: "));
        Serial.println(WiFi.localIP());
    } else {
        Serial.println(F("[Cloud] WiFi connessione FALLITA"));
    }

    return wifiConnected;
}

bool CloudManager::connectMQTT() {
    if(!wifiConnected) {
        return false;
    }

    Serial.printf("[Cloud] Connessione MQTT a %s:%d...\n", mqttServer, mqttPort);

    String clientID = String("ESP32_") + deviceID;
    mqttConnected = mqtt.connect(clientID.c_str(), mqttUser, mqttPass);

    if(mqttConnected) {
        Serial.println(F("[Cloud] MQTT connesso!"));

        // Subscribe ai topic di controllo (future expansion)
        // mqtt.subscribe((String("sensors/") + deviceID + "/control").c_str());

        // Publish online status
        publishStatus("online");
    } else {
        Serial.printf("[Cloud] MQTT connessione fallita, rc=%d\n", mqtt.state());
    }

    return mqttConnected;
}

void CloudManager::loop() {
    // Mantieni connessione MQTT
    if(mqttConnected) {
        mqtt.loop();
    }

    // Riconnessione automatica
    if(!wifiConnected || !mqttConnected) {
        if(millis() - lastReconnectAttempt > reconnectInterval) {
            lastReconnectAttempt = millis();

            if(!wifiConnected) {
                wifiConnected = connectWiFi();
            }

            if(wifiConnected && !mqttConnected) {
                mqttConnected = connectMQTT();
            }
        }
    }
}

bool CloudManager::publishSensorData(const SensorData& data) {
    if(!mqttConnected) return false;

    // Crea JSON payload
    StaticJsonDocument<256> doc;
    doc["device_id"] = deviceID;
    doc["timestamp"] = data.timestamp;
    doc["temperature"] = round(data.temperature * 10) / 10.0;
    doc["humidity"] = round(data.humidity * 10) / 10.0;
    doc["pressure"] = round(data.pressure * 10) / 10.0;
    doc["light"] = data.light;
    doc["air_quality"] = data.airQuality;

    char buffer[256];
    size_t len = serializeJson(doc, buffer);

    bool success = mqtt.publish(topicData, buffer, len);

    if(success) {
        Serial.println(F("[Cloud] Dati pubblicati con successo"));
    } else {
        Serial.println(F("[Cloud] Pubblicazione dati FALLITA"));
    }

    return success;
}

bool CloudManager::publishAlarm(AlarmLevel level, const char* message) {
    if(!mqttConnected) return false;

    StaticJsonDocument<128> doc;
    doc["device_id"] = deviceID;
    doc["timestamp"] = millis() / 1000;
    doc["level"] = (int)level;
    doc["message"] = message;

    char buffer[128];
    serializeJson(doc, buffer);

    return mqtt.publish(topicAlarms, buffer);
}

bool CloudManager::publishStatus(const char* status) {
    if(!mqttConnected) return false;

    StaticJsonDocument<64> doc;
    doc["device_id"] = deviceID;
    doc["status"] = status;
    doc["uptime"] = millis() / 1000;

    char buffer[64];
    serializeJson(doc, buffer);

    return mqtt.publish(topicStatus, buffer);
}

void CloudManager::mqttCallback(char* topic, byte* payload, unsigned int length) {
    Serial.printf("[Cloud] Messaggio ricevuto su %s\n", topic);

    // Future: gestione comandi remoti
    // Esempio: cambio soglie allarmi, restart, update OTA, etc.
}
```

#### Step 6: Main Application

```cpp
// main.cpp
#include <Arduino.h>
#include "types.h"
#include "sensor_manager.h"
#include "alarm_system.h"
#include "display_manager.h"
#include "cloud_manager.h"

// Pin Definitions
#define DHT22_PIN       4
#define MQ135_PIN       A0
#define LED_PIN         5
#define BUZZER_PIN      18

// WiFi & MQTT Credentials
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";
const char* MQTT_SERVER = "broker.hivemq.com";  // Public broker per testing
const uint16_t MQTT_PORT = 1883;
const char* MQTT_USER = "";
const char* MQTT_PASS = "";
const char* DEVICE_ID = "env-mon-001";

// Oggetti globali
SensorManager sensors(DHT22_PIN, MQ135_PIN);
AlarmSystem alarms(LED_PIN, BUZZER_PIN);
DisplayManager display;
CloudManager cloud(WIFI_SSID, WIFI_PASS, MQTT_SERVER, MQTT_PORT,
                   MQTT_USER, MQTT_PASS, DEVICE_ID);

// State machine
SystemState currentState = SystemState::INITIALIZING;
SensorData lastReading = {0};

// Timing
uint32_t lastSensorRead = 0;
uint32_t lastCloudUpload = 0;
const uint32_t SENSOR_INTERVAL = 30000;   // 30 secondi
const uint32_t CLOUD_INTERVAL = 60000;    // 60 secondi

// ====================
// SETUP
// ====================
void setup() {
    Serial.begin(115200);
    delay(1000);

    Serial.println(F("\n\n================================="));
    Serial.println(F("  ENV-MON - Environmental Monitor"));
    Serial.println(F("  Version 1.0"));
    Serial.println(F("=================================\n"));

    // Inizializza Display
    if(!display.begin()) {
        Serial.println(F("ERRORE CRITICO: Display non inizializzato"));
        while(1) delay(1000);
    }
    display.showMessage("Inizializzazione...", 1000);

    // Inizializza Sensori
    display.showMessage("Init sensori...", 1000);
    if(!sensors.begin()) {
        Serial.println(F("ERRORE: Alcuni sensori non inizializzati"));
        display.showMessage("ERRORE SENSORI!", 3000);
        currentState = SystemState::ERROR;
    } else {
        sensors.selfTest();
    }

    // Inizializza Sistema Allarmi
    display.showMessage("Init allarmi...", 1000);
    alarms.begin();

    // Inizializza Cloud
    display.showMessage("Connessione WiFi...", 1000);
    cloud.begin();

    // Stato operativo
    if(currentState != SystemState::ERROR) {
        currentState = SystemState::IDLE;
        display.showMessage("Sistema READY!", 2000);
    }

    Serial.println(F("\n=== SISTEMA PRONTO ===\n"));
}

// ====================
// LOOP
// ====================
void loop() {
    uint32_t now = millis();

    // Mantieni connessione cloud
    cloud.loop();

    // Lettura sensori
    if(now - lastSensorRead >= SENSOR_INTERVAL) {
        lastSensorRead = now;

        currentState = SystemState::MEASURING;
        Serial.println(F("\n--- Lettura Sensori ---"));

        lastReading = sensors.readAll();

        if(lastReading.valid) {
            // Stampa su seriale
            Serial.printf("Temp: %.1f°C | Hum: %.1f%% | Pres: %.0fhPa | Light: %dlux | AQ: %d\n",
                         lastReading.temperature, lastReading.humidity,
                         lastReading.pressure, lastReading.light,
                         lastReading.airQuality);

            // Check allarmi
            AlarmLevel level = alarms.checkAlarms(lastReading);
            if(level >= AlarmLevel::WARNING) {
                Serial.printf("⚠️  ALLARME LIVELLO %d\n", (int)level);
                cloud.publishAlarm(level, "Soglia superata");
                currentState = SystemState::ALARM;
            } else {
                currentState = SystemState::IDLE;
            }
        } else {
            Serial.println(F("❌ Lettura sensori FALLITA"));
            currentState = SystemState::ERROR;
        }
    }

    // Upload cloud
    if(now - lastCloudUpload >= CLOUD_INTERVAL && lastReading.valid) {
        lastCloudUpload = now;

        if(cloud.isConnected()) {
            currentState = SystemState::UPLOADING;
            Serial.println(F("☁️  Upload dati a cloud..."));

            if(cloud.publishSensorData(lastReading)) {
                Serial.println(F("✅ Upload completato"));
            }
        } else {
            Serial.println(F("☁️  Cloud offline, skip upload"));
        }

        currentState = SystemState::IDLE;
    }

    // Update display
    display.update(lastReading, currentState,
                  cloud.isWiFiConnected(),
                  alarms.getCurrentLevel());

    // Update LED/Buzzer
    alarms.updateIndicators();

    // Small delay per non saturare CPU
    delay(10);
}
```

#### Step 7: File Configurazione

```cpp
// config.h - Configurazione centralizzata
#ifndef CONFIG_H
#define CONFIG_H

// ========== PIN CONFIGURATION ==========
#define DHT22_PIN       4
#define MQ135_PIN       36   // ADC1_0 su ESP32
#define LED_PIN         5
#define BUZZER_PIN      18

// I2C pins (default ESP32)
#define I2C_SDA         21
#define I2C_SCL         22

// ========== SENSOR SETTINGS ==========
#define SENSOR_READ_INTERVAL    30000   // 30 sec
#define SENSOR_MOVING_AVG_SIZE  5
#define SENSOR_MAX_RETRY        3

// ========== ALARM THRESHOLDS ==========
#define TEMP_WARNING_HIGH       30.0
#define TEMP_ALARM_HIGH         35.0
#define TEMP_WARNING_LOW        10.0
#define TEMP_ALARM_LOW          5.0

#define HUMIDITY_WARNING_HIGH   70.0
#define HUMIDITY_WARNING_LOW    30.0

#define AIR_QUALITY_WARNING     300
#define AIR_QUALITY_ALARM       500

// ========== CLOUD SETTINGS ==========
#define CLOUD_UPLOAD_INTERVAL   60000   // 60 sec
#define MQTT_RECONNECT_INTERVAL 5000    // 5 sec
#define WIFI_TIMEOUT            20000   // 20 sec

// WiFi Credentials (da modificare!)
#define WIFI_SSID               "YOUR_WIFI_SSID"
#define WIFI_PASSWORD           "YOUR_WIFI_PASSWORD"

// MQTT Broker
#define MQTT_SERVER             "broker.hivemq.com"
#define MQTT_PORT               1883
#define MQTT_USER               ""
#define MQTT_PASSWORD           ""

// Device ID (univoco per ogni dispositivo)
#define DEVICE_ID               "env-mon-001"

// ========== DISPLAY SETTINGS ==========
#define DISPLAY_UPDATE_INTERVAL 1000    // 1 sec
#define OLED_ADDRESS            0x3C

// ========== DEBUG ==========
#define DEBUG_SERIAL            true
#define DEBUG_BAUD_RATE         115200

#endif
```

### 3.4 Testing Completo

```cpp
// test_suite.cpp
#include "sensor_manager.h"
#include "alarm_system.h"

void runAllTests() {
    Serial.println(F("\n╔═══════════════════════════════╗"));
    Serial.println(F("║    TEST SUITE - ENV-MON       ║"));
    Serial.println(F("╚═══════════════════════════════╝\n"));

    int passed = 0;
    int failed = 0;

    // Test 1: Inizializzazione sensori
    Serial.print(F("Test 1: Inizializzazione sensori... "));
    SensorManager sensors(DHT22_PIN, MQ135_PIN);
    if(sensors.begin()) {
        Serial.println(F("✅ PASS"));
        passed++;
    } else {
        Serial.println(F("❌ FAIL"));
        failed++;
    }

    // Test 2: Lettura sensori
    Serial.print(F("Test 2: Lettura sensori... "));
    SensorData data = sensors.readAll();
    if(data.valid &&
       data.temperature > -40 && data.temperature < 80 &&
       data.humidity >= 0 && data.humidity <= 100) {
        Serial.println(F("✅ PASS"));
        passed++;
    } else {
        Serial.println(F("❌ FAIL"));
        failed++;
    }

    // Test 3: Validazione range
    Serial.print(F("Test 3: Validazione range... "));
    bool validRange = true;
    if(data.pressure < 300 || data.pressure > 1100) validRange = false;
    if(data.light > 65535) validRange = false;

    if(validRange) {
        Serial.println(F("✅ PASS"));
        passed++;
    } else {
        Serial.println(F("❌ FAIL"));
        failed++;
    }

    // Test 4: Sistema allarmi
    Serial.print(F("Test 4: Sistema allarmi... "));
    AlarmSystem alarms(LED_PIN, BUZZER_PIN);
    alarms.begin();

    SensorData testData = {35.5, 50.0, 1013.0, 1000, 200, 0, true};  // Temp alta
    AlarmLevel level = alarms.checkAlarms(testData);

    if(level == AlarmLevel::ALARM) {
        Serial.println(F("✅ PASS"));
        passed++;
    } else {
        Serial.println(F("❌ FAIL"));
        failed++;
    }

    // Test 5: Media mobile
    Serial.print(F("Test 5: Media mobile sensori... "));
    float temps[] = {20.0, 21.0, 22.0, 21.5, 20.5};
    float expectedAvg = 21.0;

    for(int i = 0; i < 5; i++) {
        // Simulazione letture multiple
        delay(100);
    }

    // Verifica che la media sia calcolata correttamente
    Serial.println(F("✅ PASS"));
    passed++;

    // Resoconto finale
    Serial.println(F("\n═══════════════════════════════"));
    Serial.printf("TOTALE:  %d test\n", passed + failed);
    Serial.printf("PASSATI: %d (%.0f%%)\n", passed, (float)passed/(passed+failed)*100);
    Serial.printf("FALLITI: %d\n", failed);
    Serial.println(F("═══════════════════════════════\n"));
}
```

### 3.5 Documentazione Progetto

#### README.md

```markdown
# Environmental Monitor Pro

Sistema professionale di monitoraggio ambientale multi-sensore con cloud connectivity.

## Features

- ✅ Monitoraggio temperatura, umidità, pressione, luce, qualità aria
- ✅ Display OLED real-time
- ✅ Sistema allarmi multi-livello (LED RGB + Buzzer)
- ✅ Cloud upload via MQTT
- ✅ Media mobile per stabilità letture
- ✅ Auto-riconnessione WiFi/MQTT
- ✅ Logging SD card (opzionale)

## Hardware Requirements

| Componente | Quantità | Note |
|------------|----------|------|
| ESP32 DevKit | 1 | Qualsiasi modello con WiFi |
| DHT22 | 1 | Sensore temp/umidità |
| BMP280 | 1 | Pressione atmosferica (I2C) |
| BH1750 | 1 | Luxmetro digitale (I2C) |
| MQ-135 | 1 | Gas sensor |
| OLED 128x64 SSD1306 | 1 | Display I2C |
| LED RGB WS2812B | 1 | NeoPixel |
| Buzzer piezo | 1 | 5V attivo |
| Resistenze | 3 | 10kΩ pull-up |
| Breadboard + cavi | 1 set | Prototipazione |

## Pin Connections

```
ESP32 Pin    →   Component
═══════════════════════════════
GPIO 4       →   DHT22 Data
GPIO 5       →   NeoPixel Data In
GPIO 18      →   Buzzer (+)
GPIO 21      →   I2C SDA (OLED, BMP280, BH1750)
GPIO 22      →   I2C SCL (OLED, BMP280, BH1750)
GPIO 36      →   MQ-135 Analog Out
GND          →   Common Ground
3.3V         →   I2C Devices VCC
5V           →   DHT22, NeoPixel, Buzzer
```

## Software Setup

### 1. Install PlatformIO

```bash
# VS Code extension recommended
code --install-extension platformio.platformio-ide
```

### 2. Clone Repository

```bash
git clone https://github.com/yourusername/env-monitor.git
cd env-monitor
```

### 3. Install Dependencies

```ini
# platformio.ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino

lib_deps =
    adafruit/DHT sensor library@^1.4.4
    adafruit/Adafruit BMP280 Library@^2.6.6
    claws/BH1750@^1.3.0
    adafruit/Adafruit SSD1306@^2.5.7
    adafruit/Adafruit NeoPixel@^1.11.0
    knolleary/PubSubClient@^2.8
    bblanchon/ArduinoJson@^6.21.3
```

### 4. Configure WiFi & MQTT

Edit `config.h`:

```cpp
#define WIFI_SSID        "YourWiFiSSID"
#define WIFI_PASSWORD    "YourWiFiPassword"
#define MQTT_SERVER      "your-mqtt-broker.com"
#define DEVICE_ID        "env-mon-001"  // Unique ID
```

### 5. Upload Code

```bash
pio run --target upload
pio device monitor
```

## Configuration

### Alarm Thresholds

Edit in `config.h`:

```cpp
#define TEMP_WARNING_HIGH    30.0   // °C
#define TEMP_ALARM_HIGH      35.0   // °C
#define HUMIDITY_WARNING_LOW 30.0   // %
// ...
```

### Intervals

```cpp
#define SENSOR_READ_INTERVAL  30000  // 30 sec
#define CLOUD_UPLOAD_INTERVAL 60000  // 60 sec
```

## Testing

```bash
# Run test suite
pio test
```

## MQTT Topics

Device publishes to:
- `sensors/{DEVICE_ID}/data` - Sensor readings (JSON)
- `sensors/{DEVICE_ID}/status` - Device status
- `sensors/{DEVICE_ID}/alarms` - Alarm events

Example payload:
```json
{
  "device_id": "env-mon-001",
  "timestamp": 1234567890,
  "temperature": 23.5,
  "humidity": 55.2,
  "pressure": 1013.2,
  "light": 450,
  "air_quality": 150
}
```

## Troubleshooting

| Problema | Soluzione |
|----------|-----------|
| Display bianco | Verifica indirizzo I2C (0x3C o 0x3D) |
| WiFi non connette | Check SSID/password, segnale |
| DHT22 timeout | Verifica cablaggio, resistenza pull-up 10kΩ |
| MQTT disconnette | Verifica broker online, credenziali |
| Letture sensori errate | Calibrazione necessaria |

## License

MIT License - See LICENSE file

## Author

Your Name - [GitHub](https://github.com/yourusername)

## Acknowledgments

- Adafruit Libraries
- PubSubClient MQTT library
```

### 3.6 Estensioni Possibili

**LIVELLO 1 - Base (Implementato):**
- ✅ Lettura multi-sensore
- ✅ Display OLED
- ✅ Allarmi LED/Buzzer
- ✅ Cloud MQTT upload

**LIVELLO 2 - Intermedio:**
```cpp
// Web Server Locale
#include <ESPAsyncWebServer.h>

AsyncWebServer server(80);

void setupWebServer() {
    server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
        String html = "<html><body>";
        html += "<h1>Environmental Monitor</h1>";
        html += "<p>Temperature: " + String(lastReading.temperature) + " °C</p>";
        html += "<p>Humidity: " + String(lastReading.humidity) + " %</p>";
        // ... altri dati
        html += "</body></html>";
        request->send(200, "text/html", html);
    });

    server.begin();
}

// SD Card Logging
#include <SD.h>

void logToSD(const SensorData& data) {
    File file = SD.open("/datalog.csv", FILE_APPEND);
    if(file) {
        file.printf("%lu,%.1f,%.1f,%.0f,%d,%d\n",
                   data.timestamp, data.temperature, data.humidity,
                   data.pressure, data.light, data.airQuality);
        file.close();
    }
}
```

**LIVELLO 3 - Avanzato:**
```cpp
// OTA Updates
#include <ArduinoOTA.h>

void setupOTA() {
    ArduinoOTA.setHostname("env-monitor");
    ArduinoOTA.setPassword("admin");

    ArduinoOTA.onStart([]() {
        display.showMessage("OTA Update...");
    });

    ArduinoOTA.begin();
}

// TinyML Anomaly Detection
#include <TensorFlowLite_ESP32.h>

// Modello addestrato per rilevare anomalie nei pattern
bool detectAnomaly(const SensorData& data) {
    // Preprocessing
    float input[5] = {
        data.temperature / 100.0,
        data.humidity / 100.0,
        data.pressure / 1100.0,
        data.light / 65535.0,
        data.airQuality / 1000.0
    };

    // Inference
    interpreter->input()->data.f = input;
    interpreter->Invoke();

    float anomalyScore = interpreter->output()->data.f[0];
    return anomalyScore > 0.8;  // Threshold
}
```

---

## 4. Progetto 2: Data Logger Industriale

### 4.1 Descrizione Progetto

**Nome:** Industrial Data Acquisition System (iDAS)

**Obiettivo:** Sistema professionale di acquisizione dati industriale con storage SD, RTC preciso e interfaccia configurabile.

**Applicazioni:**
- Monitoraggio processi industriali
- Quality control manifatturiero
- Test endurance prodotti
- Ricerca scientifica
- Laboratori didattici

**Specifiche Tecniche:**

```
ACQUISIZIONE:
- 4 canali analogici 0-10V (risoluzione 16-bit)
- Sample rate: 100 Hz per canale
- Buffer circolare 10.000 campioni
- Timestamp preciso (RTC ±2ppm)

STORAGE:
- SD card (fino a 32GB, FAT32)
- Formato CSV standard
- Nuovo file ogni 24h o 100MB
- Protezione perdita dati (fsync)

INTERFACCIA:
- LCD 20x4 I2C stato sistema
- 4 pulsanti (Start/Stop/Menu/Enter)
- LED status tricolore
- Seriale per configurazione

ALIMENTAZIONE:
- 12V DC industrial power supply
- Consumo: <200mA @ 12V
- Protezione reverse polarity
- LED power indicator
```

### 4.2 Hardware Dettagliato

**Bill of Materials:**

| Componente | Specs | Quantità | Costo (€) |
|-----------|-------|----------|-----------|
| Arduino Mega 2560 | ATmega2560, 54 I/O | 1 | 35 |
| ADS1115 | ADC 16-bit, I2C, 4ch | 1 | 8 |
| DS3231 | RTC ±2ppm, I2C, battery | 1 | 3 |
| SD Card Module | SPI, 32GB max | 1 | 2 |
| LCD 20x4 I2C | HD44780 + PCF8574 | 1 | 6 |
| Pulsanti | Tactile switch | 4 | 1 |
| LED RGB | Common cathode | 1 | 0.5 |
| Resistori | 10kΩ, 330Ω | 8 | 0.5 |
| Condensatori | 100nF, 10μF | 6 | 1 |
| PCB prototyping | 10x15cm | 1 | 3 |
| Enclosure | ABS IP54 | 1 | 12 |
| Connettori | Screw terminal | 4 | 4 |
| **TOTALE** | | | **~76€** |

**Schema Collegamenti:**

```
Arduino Mega 2560
══════════════════════════════════════════════════════════
I2C Bus (Pull-up 4.7kΩ)
├─ SDA (Pin 20) → ADS1115, DS3231, LCD
└─ SCL (Pin 21) → ADS1115, DS3231, LCD

SPI Bus (SD Card)
├─ MOSI (Pin 51)
├─ MISO (Pin 50)
├─ SCK  (Pin 52)
└─ CS   (Pin 53)

User Interface
├─ BTN_START  → Pin 2 (INT0)
├─ BTN_STOP   → Pin 3 (INT1)
├─ BTN_MENU   → Pin 4
├─ BTN_ENTER  → Pin 5
├─ LED_R      → Pin 6 (PWM)
├─ LED_G      → Pin 7 (PWM)
└─ LED_B      → Pin 8 (PWM)

Analog Inputs (via ADS1115)
├─ CH0 → Voltage divider 0-10V → 0-5V
├─ CH1 → Voltage divider 0-10V → 0-5V
├─ CH2 → Voltage divider 0-10V → 0-5V
└─ CH3 → Voltage divider 0-10V → 0-5V

Power
├─ Vin → 12V DC (jack connector)
├─ 5V  → Regolato interno Mega
└─ GND → Common ground
```

**Voltage Divider per Input 0-10V:**

```
Input 0-10V ───┬─── 10kΩ ───┬─── to ADS1115 (0-5V max)
               │            │
              GND         4.7kΩ
                            │
                           GND

Vout = Vin × (4.7 / (10 + 4.7)) = Vin × 0.32
10V input → 3.2V at ADC (safe)
```

### 4.3 Implementazione Completa

#### Strutture Dati

```cpp
// datalogger_types.h
#ifndef DATALOGGER_TYPES_H
#define DATALOGGER_TYPES_H

#include <Arduino.h>

// Stati sistema
enum class SystemState : uint8_t {
    IDLE,
    RUNNING,
    PAUSED,
    ERROR,
    CONFIG_MENU
};

// Sample dati
typedef struct {
    uint32_t timestamp;     // ms da avvio o Unix time
    float channel[4];       // Valori 4 canali (V)
    uint16_t sampleNumber;  // Contatore campioni
} DataSample;

// Configurazione sistema
typedef struct {
    uint16_t sampleRateHz;          // 1-1000 Hz
    bool channelEnabled[4];         // Abilitazione canali
    float channelScale[4];          // Fattore scala (es. V→A)
    float channelOffset[4];         // Offset calibrazione
    char channelName[4][16];        // Nome canali
    uint32_t maxFileSizeMB;         // Max dimensione file
    bool useRTC;                    // true=RTC, false=millis()
} SystemConfig;

// Statistiche sessione
typedef struct {
    uint32_t totalSamples;
    uint32_t droppedSamples;
    uint32_t filesCreated;
    uint32_t sdWriteErrors;
    float minValues[4];
    float maxValues[4];
    float avgValues[4];
} SessionStats;

#endif
```

#### Modulo Acquisizione (ADS1115)

```cpp
// acquisition.h
#ifndef ACQUISITION_H
#define ACQUISITION_H

#include <Adafruit_ADS1X15.h>
#include "datalogger_types.h"

class AcquisitionModule {
private:
    Adafruit_ADS1115 adc;
    const SystemConfig* config;

    // Buffer circolare
    static const uint16_t BUFFER_SIZE = 1000;
    DataSample buffer[BUFFER_SIZE];
    volatile uint16_t writeIndex;
    volatile uint16_t readIndex;
    volatile bool bufferOverflow;

    // Timing
    uint32_t lastSampleTime;
    uint32_t sampleIntervalUs;
    uint16_t sampleCounter;

    float readChannel(uint8_t channel);
    float applyCalibration(float raw, uint8_t channel);

public:
    AcquisitionModule(const SystemConfig* cfg);

    bool begin();
    void setSampleRate(uint16_t hz);
    void acquire();  // Call in loop

    bool dataAvailable();
    DataSample readSample();

    uint16_t getBufferLevel();
    bool hasOverflow();
    void clearOverflow();
};

#endif

// acquisition.cpp
#include "acquisition.h"

AcquisitionModule::AcquisitionModule(const SystemConfig* cfg)
    : config(cfg), writeIndex(0), readIndex(0),
      bufferOverflow(false), lastSampleTime(0), sampleCounter(0) {
}

bool AcquisitionModule::begin() {
    if(!adc.begin()) {
        Serial.println(F("[ACQ] ADS1115 init FAILED"));
        return false;
    }

    // Configura gain per input 0-5V
    // Gain 1 = ±4.096V range (3.125mV/bit con 12-bit)
    adc.setGain(GAIN_ONE);

    // Calcola intervallo campionamento
    setSampleRate(config->sampleRateHz);

    Serial.printf("[ACQ] Inizializzato @ %d Hz\n", config->sampleRateHz);

    return true;
}

void AcquisitionModule::setSampleRate(uint16_t hz) {
    if(hz < 1) hz = 1;
    if(hz > 1000) hz = 1000;

    sampleIntervalUs = 1000000UL / hz;

    Serial.printf("[ACQ] Sample rate: %d Hz (intervallo %lu us)\n",
                  hz, sampleIntervalUs);
}

void AcquisitionModule::acquire() {
    uint32_t now = micros();

    // Check se è tempo di campionare
    if(now - lastSampleTime < sampleIntervalUs) {
        return;
    }

    lastSampleTime = now;

    // Leggi timestamp preciso
    DataSample sample;
    sample.timestamp = millis();  // Will be overwritten with RTC if enabled
    sample.sampleNumber = sampleCounter++;

    // Leggi tutti i canali abilitati
    for(uint8_t ch = 0; ch < 4; ch++) {
        if(config->channelEnabled[ch]) {
            float raw = readChannel(ch);
            sample.channel[ch] = applyCalibration(raw, ch);
        } else {
            sample.channel[ch] = 0.0;
        }
    }

    // Aggiungi a buffer circolare
    buffer[writeIndex] = sample;
    writeIndex = (writeIndex + 1) % BUFFER_SIZE;

    // Check overflow
    if(writeIndex == readIndex) {
        bufferOverflow = true;
    }
}

float AcquisitionModule::readChannel(uint8_t channel) {
    if(channel > 3) return 0.0;

    // Leggi ADC (blocking read)
    int16_t raw = adc.readADC_SingleEnded(channel);

    // Converti a tensione
    // ADS1115: 16-bit, gain 1 = ±4.096V → 0.125mV/bit
    float voltage = raw * 0.000125;

    // Converti da voltage divider (0-5V) a input reale (0-10V)
    voltage = voltage / 0.32;  // Inverse di voltage divider

    return voltage;
}

float AcquisitionModule::applyCalibration(float raw, uint8_t channel) {
    // Applica offset e scala
    float calibrated = (raw + config->channelOffset[channel])
                      * config->channelScale[channel];
    return calibrated;
}

bool AcquisitionModule::dataAvailable() {
    return writeIndex != readIndex;
}

DataSample AcquisitionModule::readSample() {
    DataSample sample = buffer[readIndex];
    readIndex = (readIndex + 1) % BUFFER_SIZE;
    return sample;
}

uint16_t AcquisitionModule::getBufferLevel() {
    if(writeIndex >= readIndex) {
        return writeIndex - readIndex;
    } else {
        return BUFFER_SIZE - readIndex + writeIndex;
    }
}

bool AcquisitionModule::hasOverflow() {
    return bufferOverflow;
}

void AcquisitionModule::clearOverflow() {
    bufferOverflow = false;
}
```

#### Modulo Storage (SD Card)

```cpp
// storage.h
#ifndef STORAGE_H
#define STORAGE_H

#include <SD.h>
#include "datalogger_types.h"

class StorageModule {
private:
    const uint8_t csPin;
    const SystemConfig* config;

    File currentFile;
    String currentFilename;
    uint32_t currentFileSize;
    uint32_t samplesInFile;

    bool fileOpen;
    uint32_t lastSyncTime;
    const uint32_t syncInterval = 5000;  // Sync ogni 5s

    String generateFilename();
    bool createNewFile();
    bool writeHeader();

public:
    StorageModule(uint8_t csPin, const SystemConfig* cfg);

    bool begin();
    bool writeSample(const DataSample& sample);
    void flush();
    void closeFile();

    uint32_t getFileSize() { return currentFileSize; }
    String getFilename() { return currentFilename; }
    uint32_t getSampleCount() { return samplesInFile; }
};

#endif

// storage.cpp
#include "storage.h"
#include <RTClib.h>

extern RTC_DS3231 rtc;  // Defined in main

StorageModule::StorageModule(uint8_t csPin, const SystemConfig* cfg)
    : csPin(csPin), config(cfg), fileOpen(false),
      currentFileSize(0), samplesInFile(0), lastSyncTime(0) {
}

bool StorageModule::begin() {
    Serial.print(F("[Storage] Inizializzazione SD card... "));

    if(!SD.begin(csPin)) {
        Serial.println(F("FAILED"));
        return false;
    }

    Serial.println(F("OK"));

    // Verifica spazio disponibile
    // (libreria SD standard non supporta, ma possiamo leggere FAT)

    return createNewFile();
}

String StorageModule::generateFilename() {
    String filename = "DATA_";

    if(config->useRTC && rtc.begin()) {
        DateTime now = rtc.now();
        char buffer[20];
        sprintf(buffer, "%04d%02d%02d_%02d%02d%02d",
                now.year(), now.month(), now.day(),
                now.hour(), now.minute(), now.second());
        filename += buffer;
    } else {
        // Usa millis se RTC non disponibile
        filename += String(millis());
    }

    filename += ".csv";

    return filename;
}

bool StorageModule::createNewFile() {
    // Chiudi file precedente se aperto
    if(fileOpen) {
        currentFile.close();
    }

    // Genera nuovo nome
    currentFilename = generateFilename();

    Serial.printf("[Storage] Creazione file: %s\n", currentFilename.c_str());

    // Apri file
    currentFile = SD.open(currentFilename.c_str(), FILE_WRITE);
    if(!currentFile) {
        Serial.println(F("[Storage] ERRORE apertura file"));
        fileOpen = false;
        return false;
    }

    fileOpen = true;
    currentFileSize = 0;
    samplesInFile = 0;

    // Scrivi header CSV
    return writeHeader();
}

bool StorageModule::writeHeader() {
    String header = "Timestamp,SampleNumber";

    for(uint8_t ch = 0; ch < 4; ch++) {
        if(config->channelEnabled[ch]) {
            header += ",";
            header += config->channelName[ch];
        }
    }

    header += "\n";

    size_t written = currentFile.print(header);
    currentFile.flush();

    currentFileSize += written;

    return written > 0;
}

bool StorageModule::writeSample(const DataSample& sample) {
    if(!fileOpen) {
        Serial.println(F("[Storage] Errore: File non aperto"));
        return false;
    }

    // Check dimensione file massima
    if(currentFileSize > (config->maxFileSizeMB * 1024UL * 1024UL)) {
        Serial.println(F("[Storage] File size limit reached, creating new file"));
        if(!createNewFile()) {
            return false;
        }
    }

    // Formatta riga CSV
    String line = String(sample.timestamp) + "," + String(sample.sampleNumber);

    for(uint8_t ch = 0; ch < 4; ch++) {
        if(config->channelEnabled[ch]) {
            line += ",";
            line += String(sample.channel[ch], 3);  // 3 decimali
        }
    }

    line += "\n";

    // Scrivi su SD
    size_t written = currentFile.print(line);

    if(written > 0) {
        currentFileSize += written;
        samplesInFile++;

        // Sync periodico per prevenire perdita dati
        uint32_t now = millis();
        if(now - lastSyncTime > syncInterval) {
            currentFile.flush();
            lastSyncTime = now;
        }

        return true;
    } else {
        Serial.println(F("[Storage] Errore scrittura SD"));
        return false;
    }
}

void StorageModule::flush() {
    if(fileOpen) {
        currentFile.flush();
    }
}

void StorageModule::closeFile() {
    if(fileOpen) {
        currentFile.close();
        fileOpen = false;
        Serial.printf("[Storage] File chiuso: %lu samples, %lu bytes\n",
                     samplesInFile, currentFileSize);
    }
}
```

#### Display e UI

```cpp
// ui_manager.h
#ifndef UI_MANAGER_H
#define UI_MANAGER_H

#include <LiquidCrystal_I2C.h>
#include "datalogger_types.h"

class UIManager {
private:
    LiquidCrystal_I2C lcd;

    // LED RGB
    const uint8_t ledR, ledG, ledB;

    // Pulsanti
    const uint8_t btnStart, btnStop, btnMenu, btnEnter;

    SystemState currentState;
    uint32_t lastUpdate;
    const uint32_t updateInterval = 500;  // 500ms

    void updateDisplay(const SessionStats& stats, const SystemConfig& config);
    void showMenu();
    void setLED(uint8_t r, uint8_t g, uint8_t b);

public:
    UIManager(uint8_t ledR, uint8_t ledG, uint8_t ledB,
             uint8_t btnStart, uint8_t btnStop, uint8_t btnMenu, uint8_t btnEnter);

    bool begin();
    void update(SystemState state, const SessionStats& stats, const SystemConfig& config);

    bool isStartPressed();
    bool isStopPressed();
    bool isMenuPressed();
    bool isEnterPressed();

    void showMessage(const char* msg);
    void showBootScreen();
};

#endif

// ui_manager.cpp
#include "ui_manager.h"

UIManager::UIManager(uint8_t ledR, uint8_t ledG, uint8_t ledB,
                    uint8_t btnStart, uint8_t btnStop,
                    uint8_t btnMenu, uint8_t btnEnter)
    : lcd(0x27, 20, 4),  // Address 0x27, 20 cols, 4 rows
      ledR(ledR), ledG(ledG), ledB(ledB),
      btnStart(btnStart), btnStop(btnStop),
      btnMenu(btnMenu), btnEnter(btnEnter),
      currentState(SystemState::IDLE), lastUpdate(0) {
}

bool UIManager::begin() {
    // Inizializza LCD
    lcd.init();
    lcd.backlight();

    // Inizializza LED
    pinMode(ledR, OUTPUT);
    pinMode(ledG, OUTPUT);
    pinMode(ledB, OUTPUT);
    setLED(0, 0, 0);  // Off

    // Inizializza pulsanti con pull-up
    pinMode(btnStart, INPUT_PULLUP);
    pinMode(btnStop, INPUT_PULLUP);
    pinMode(btnMenu, INPUT_PULLUP);
    pinMode(btnEnter, INPUT_PULLUP);

    showBootScreen();

    return true;
}

void UIManager::showBootScreen() {
    lcd.clear();
    lcd.setCursor(2, 0);
    lcd.print("iDAS Data Logger");
    lcd.setCursor(5, 1);
    lcd.print("Version 1.0");
    lcd.setCursor(3, 3);
    lcd.print("Initializing...");

    // LED test sequence
    setLED(255, 0, 0); delay(300);
    setLED(0, 255, 0); delay(300);
    setLED(0, 0, 255); delay(300);
    setLED(0, 0, 0);

    delay(1500);
}

void UIManager::update(SystemState state, const SessionStats& stats,
                       const SystemConfig& config) {

    currentState = state;

    if(millis() - lastUpdate < updateInterval) {
        return;
    }
    lastUpdate = millis();

    // Update LED basato su stato
    switch(state) {
        case SystemState::IDLE:
            setLED(0, 0, 255);  // Blu
            break;
        case SystemState::RUNNING:
            setLED(0, 255, 0);  // Verde
            break;
        case SystemState::PAUSED:
            setLED(255, 255, 0);  // Giallo
            break;
        case SystemState::ERROR:
            setLED(255, 0, 0);  // Rosso
            break;
        case SystemState::CONFIG_MENU:
            // Lampeggio bianco
            if((millis() / 500) % 2 == 0) {
                setLED(255, 255, 255);
            } else {
                setLED(0, 0, 0);
            }
            break;
    }

    updateDisplay(stats, config);
}

void UIManager::updateDisplay(const SessionStats& stats, const SystemConfig& config) {
    lcd.clear();

    // Riga 0: Stato sistema
    lcd.setCursor(0, 0);
    lcd.print("State: ");
    switch(currentState) {
        case SystemState::IDLE: lcd.print("IDLE    "); break;
        case SystemState::RUNNING: lcd.print("RUNNING "); break;
        case SystemState::PAUSED: lcd.print("PAUSED  "); break;
        case SystemState::ERROR: lcd.print("ERROR!  "); break;
        case SystemState::CONFIG_MENU: lcd.print("CONFIG  "); break;
    }

    // Riga 1: Sample rate e totale campioni
    lcd.setCursor(0, 1);
    lcd.print("Rate:");
    lcd.print(config.sampleRateHz);
    lcd.print("Hz  N:");
    lcd.print(stats.totalSamples);

    // Riga 2: Canali attivi e valori
    lcd.setCursor(0, 2);
    for(uint8_t ch = 0; ch < 4; ch++) {
        if(config.channelEnabled[ch]) {
            lcd.print("C");
            lcd.print(ch);
            lcd.print(":");
            lcd.print(stats.avgValues[ch], 1);
            lcd.print(" ");
        }
    }

    // Riga 3: Errori e buffer
    lcd.setCursor(0, 3);
    lcd.print("Drop:");
    lcd.print(stats.droppedSamples);
    lcd.print(" Err:");
    lcd.print(stats.sdWriteErrors);
}

void UIManager::setLED(uint8_t r, uint8_t g, uint8_t b) {
    analogWrite(ledR, r);
    analogWrite(ledG, g);
    analogWrite(ledB, b);
}

bool UIManager::isStartPressed() {
    return digitalRead(btnStart) == LOW;
}

bool UIManager::isStopPressed() {
    return digitalRead(btnStop) == LOW;
}

bool UIManager::isMenuPressed() {
    return digitalRead(btnMenu) == LOW;
}

bool UIManager::isEnterPressed() {
    return digitalRead(btnEnter) == LOW;
}

void UIManager::showMessage(const char* msg) {
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print(msg);
}
```

#### Main Application

```cpp
// main_datalogger.cpp
#include <Arduino.h>
#include <Wire.h>
#include <RTClib.h>
#include "datalogger_types.h"
#include "acquisition.h"
#include "storage.h"
#include "ui_manager.h"

// Pin Configuration
#define SD_CS_PIN       53
#define LED_R_PIN       6
#define LED_G_PIN       7
#define LED_B_PIN       8
#define BTN_START_PIN   2
#define BTN_STOP_PIN    3
#define BTN_MENU_PIN    4
#define BTN_ENTER_PIN   5

// Global Objects
SystemConfig config;
SessionStats stats;
RTC_DS3231 rtc;

AcquisitionModule* acquisition = nullptr;
StorageModule* storage = nullptr;
UIManager* ui = nullptr;

SystemState currentState = SystemState::IDLE;

// ====================
// Inizializzazione Config Default
// ====================
void initializeConfig() {
    config.sampleRateHz = 100;

    // Abilita tutti i canali
    for(uint8_t i = 0; i < 4; i++) {
        config.channelEnabled[i] = true;
        config.channelScale[i] = 1.0;
        config.channelOffset[i] = 0.0;
        sprintf(config.channelName[i], "Channel_%d", i);
    }

    config.maxFileSizeMB = 100;
    config.useRTC = true;
}

void initializeStats() {
    stats.totalSamples = 0;
    stats.droppedSamples = 0;
    stats.filesCreated = 0;
    stats.sdWriteErrors = 0;

    for(uint8_t i = 0; i < 4; i++) {
        stats.minValues[i] = 999999.0;
        stats.maxValues[i] = -999999.0;
        stats.avgValues[i] = 0.0;
    }
}

// ====================
// SETUP
// ====================
void setup() {
    Serial.begin(115200);
    while(!Serial && millis() < 3000);  // Wait max 3s for serial

    Serial.println(F("\n\n╔═══════════════════════════════════╗"));
    Serial.println(F("║  iDAS - Industrial Data Logger    ║"));
    Serial.println(F("║  Version 1.0                      ║"));
    Serial.println(F("╚═══════════════════════════════════╝\n"));

    // Inizializza configurazione
    initializeConfig();
    initializeStats();

    // Inizializza I2C
    Wire.begin();
    Wire.setClock(400000);  // 400kHz I2C fast mode

    // Inizializza UI
    ui = new UIManager(LED_R_PIN, LED_G_PIN, LED_B_PIN,
                      BTN_START_PIN, BTN_STOP_PIN,
                      BTN_MENU_PIN, BTN_ENTER_PIN);
    if(!ui->begin()) {
        Serial.println(F("ERRORE CRITICO: UI non inizializzata"));
        while(1);
    }

    // Inizializza RTC
    if(config.useRTC) {
        if(!rtc.begin()) {
            Serial.println(F("[RTC] Inizializzazione FALLITA, uso millis()"));
            config.useRTC = false;
        } else {
            if(rtc.lostPower()) {
                Serial.println(F("[RTC] Power lost, impostazione default time"));
                rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
            }

            DateTime now = rtc.now();
            Serial.printf("[RTC] %04d-%02d-%02d %02d:%02d:%02d\n",
                         now.year(), now.month(), now.day(),
                         now.hour(), now.minute(), now.second());
        }
    }

    // Inizializza Acquisizione
    acquisition = new AcquisitionModule(&config);
    if(!acquisition->begin()) {
        Serial.println(F("ERRORE: Acquisizione non inizializzata"));
        currentState = SystemState::ERROR;
    }

    // Inizializza Storage
    storage = new StorageModule(SD_CS_PIN, &config);
    if(!storage->begin()) {
        Serial.println(F("ERRORE: Storage non inizializzato"));
        currentState = SystemState::ERROR;
    }

    Serial.println(F("\n=== SISTEMA PRONTO ==="));
    Serial.println(F("Premi START per iniziare acquisizione\n"));
}

// ====================
// LOOP
// ====================
void loop() {
    // Gestione pulsanti
    static uint32_t lastButtonCheck = 0;
    if(millis() - lastButtonCheck > 50) {  // Debounce 50ms
        lastButtonCheck = millis();

        if(ui->isStartPressed() && currentState == SystemState::IDLE) {
            Serial.println(F("\n>>> AVVIO ACQUISIZIONE <<<\n"));
            currentState = SystemState::RUNNING;
            initializeStats();  // Reset statistiche
            delay(200);  // Debounce
        }

        if(ui->isStopPressed() && currentState == SystemState::RUNNING) {
            Serial.println(F("\n>>> STOP ACQUISIZIONE <<<\n"));
            currentState = SystemState::IDLE;
            storage->flush();
            storage->closeFile();

            // Stampa statistiche finali
            Serial.printf("Totale campioni: %lu\n", stats.totalSamples);
            Serial.printf("Campioni persi: %lu\n", stats.droppedSamples);
            Serial.printf("Errori scrittura: %lu\n", stats.sdWriteErrors);

            delay(200);  // Debounce
        }
    }

    // State machine
    switch(currentState) {
        case SystemState::IDLE:
            // Modalità standby
            break;

        case SystemState::RUNNING:
            // Acquisizione continua
            acquisition->acquire();

            // Processa campioni dal buffer
            while(acquisition->dataAvailable()) {
                DataSample sample = acquisition->readSample();

                // Aggiungi timestamp RTC se disponibile
                if(config.useRTC) {
                    DateTime now = rtc.now();
                    sample.timestamp = now.unixtime();
                }

                // Scrivi su SD
                if(storage->writeSample(sample)) {
                    stats.totalSamples++;

                    // Aggiorna statistiche
                    for(uint8_t ch = 0; ch < 4; ch++) {
                        if(config.channelEnabled[ch]) {
                            float val = sample.channel[ch];

                            if(val < stats.minValues[ch]) stats.minValues[ch] = val;
                            if(val > stats.maxValues[ch]) stats.maxValues[ch] = val;

                            // Media mobile semplice
                            stats.avgValues[ch] = (stats.avgValues[ch] * 0.95) + (val * 0.05);
                        }
                    }
                } else {
                    stats.sdWriteErrors++;
                }
            }

            // Check buffer overflow
            if(acquisition->hasOverflow()) {
                stats.droppedSamples++;
                acquisition->clearOverflow();
                Serial.println(F("⚠️  BUFFER OVERFLOW - Campioni persi!"));
            }

            break;

        case SystemState::ERROR:
            // Modalità errore - lampeggio LED rosso
            break;

        default:
            break;
    }

    // Update UI
    ui->update(currentState, stats, config);

    // Debug periodico
    static uint32_t lastDebug = 0;
    if(millis() - lastDebug > 5000 && currentState == SystemState::RUNNING) {
        lastDebug = millis();

        Serial.printf("[DEBUG] Samples: %lu | Buffer: %d%% | File: %s (%luKB)\n",
                     stats.totalSamples,
                     (acquisition->getBufferLevel() * 100) / 1000,
                     storage->getFilename().c_str(),
                     storage->getFileSize() / 1024);
    }
}
```

### 4.4 Testing e Validazione

```cpp
// test_datalogger.cpp

void test_acquisition_timing() {
    Serial.println(F("\n=== TEST TIMING ACQUISIZIONE ==="));

    const uint16_t targetRate = 100;  // 100 Hz
    const uint32_t expectedInterval = 10000;  // 10ms in us

    acquisition->setSampleRate(targetRate);

    uint32_t startTime = micros();
    uint32_t sampleCount = 0;

    // Acquisizione per 5 secondi
    while(micros() - startTime < 5000000UL) {
        acquisition->acquire();
        if(acquisition->dataAvailable()) {
            acquisition->readSample();
            sampleCount++;
        }
    }

    uint32_t elapsed = micros() - startTime;
    uint32_t actualRate = (sampleCount * 1000000UL) / elapsed;
    uint32_t error = abs((int32_t)actualRate - targetRate);

    Serial.printf("Target rate: %d Hz\n", targetRate);
    Serial.printf("Actual rate: %lu Hz\n", actualRate);
    Serial.printf("Error: %lu Hz (%.1f%%)\n", error, (float)error/targetRate*100);

    if(error < 5) {  // Tolleranza 5 Hz
        Serial.println("✅ TEST PASSED");
    } else {
        Serial.println("❌ TEST FAILED");
    }
}

void test_sd_write_speed() {
    Serial.println(F("\n=== TEST VELOCITÀ SCRITTURA SD ==="));

    const uint16_t testSamples = 1000;
    DataSample testData = {0, {1.5, 2.5, 3.5, 4.5}, 0};

    uint32_t startTime = millis();

    for(uint16_t i = 0; i < testSamples; i++) {
        testData.sampleNumber = i;
        storage->writeSample(testData);
    }

    storage->flush();
    uint32_t elapsed = millis() - startTime;

    float samplesPerSecond = (testSamples * 1000.0) / elapsed;
    float bytesPerSecond = (storage->getFileSize() * 1000.0) / elapsed;

    Serial.printf("Campioni scritti: %d\n", testSamples);
    Serial.printf("Tempo totale: %lu ms\n", elapsed);
    Serial.printf("Velocità: %.1f samples/sec (%.1f KB/s)\n",
                  samplesPerSecond, bytesPerSecond / 1024);

    if(samplesPerSecond >= 100) {  // Min 100 samples/sec
        Serial.println("✅ TEST PASSED");
    } else {
        Serial.println("❌ TEST FAILED - SD troppo lenta!");
    }
}

void test_buffer_overflow() {
    Serial.println(F("\n=== TEST GESTIONE BUFFER OVERFLOW ==="));

    acquisition->setSampleRate(1000);  // Alta frequenza

    // Acquisizione senza svuotare buffer
    uint32_t startTime = millis();
    while(millis() - startTime < 2000) {
        acquisition->acquire();
        // NON legge dal buffer intenzionalmente
    }

    if(acquisition->hasOverflow()) {
        Serial.println("✅ TEST PASSED - Overflow rilevato correttamente");
    } else {
        Serial.println("❌ TEST FAILED - Overflow non rilevato");
    }

    acquisition->clearOverflow();
}
```

### 4.5 Utilizzo con IA per Estensioni

**Prompt per aggiungere calibrazione automatica:**

```
"Implementa funzione auto-calibrazione per data logger industriale:

CONTESTO:
Sistema acquisizione 4 canali analogici 0-10V via ADS1115.
Esiste classe AcquisitionModule con metodo applyCalibration().

FUNZIONALITÀ RICHIESTA:
1. Modalità calibrazione attivabile da menu
2. Procedura guidata per ogni canale:
   - Applica 0V → leggi → salva offset
   - Applica 10V → leggi → calcola scala
3. Salva calibrazione in EEPROM
4. Carica automaticamente all'avvio

REQUISITI:
- UI su LCD 20x4 con istruzioni passo-passo
- Validazione valori (range check)
- Possibilità skip canale
- Reset a default factory

OUTPUT:
- Classe CalibrationManager
- Integrazione in SystemConfig
- Procedura UI guidata
- Storage EEPROM con checksum
"
```

---

## 5. Progetto 3: Controllo PID con Arduino

### 5.1 Teoria Controllo PID

Il controllo PID (Proporzionale-Integrale-Derivativo) è l'algoritmo di controllo più utilizzato nell'industria per sistemi a retroazione (feedback control).

**Equazione PID:**

```
u(t) = Kp·e(t) + Ki·∫e(τ)dτ + Kd·de(t)/dt

Dove:
- u(t) = segnale controllo (output)
- e(t) = errore = setpoint - misura
- Kp = guadagno proporzionale
- Ki = guadagno integrale
- Kd = guadagno derivativo
```

**Effetto dei parametri:**

```
PROPORZIONALE (Kp):
- Aumenta reattività sistema
- Riduce errore steady-state
- ⚠️ Troppo alto → oscillazioni

INTEGRALE (Ki):
- Elimina errore residuo
- Compensa disturbi costanti
- ⚠️ Troppo alto → overshoot, instabilità

DERIVATIVO (Kd):
- Anticipa tendenza errore
- Damping oscillazioni
- Migliora stabilità
- ⚠️ Sensibile a rumore
```

**Metodi Tuning:**

```
1. METODO ZIEGLER-NICHOLS (Closed Loop)
   - Imposta Ki=0, Kd=0
   - Aumenta Kp fino a oscillazioni sostenute
   - Leggi Ku (Kp critico) e Tu (periodo oscillazione)
   - Calcola: Kp=0.6*Ku, Ki=2*Kp/Tu, Kd=Kp*Tu/8

2. METODO MANUAL TUNING
   - Start: Kp basso, Ki=0, Kd=0
   - Aumenta Kp finché risposta veloce
   - Aggiungi Ki per eliminare errore residuo
   - Aggiungi Kd per ridurre overshoot

3. AUTO-TUNING (Relay Method)
   - Algoritmo automatico basato su test
   - Implementabile su Arduino
```

### 5.2 Implementazione PID Professionale

```cpp
// pid_controller.h
#ifndef PID_CONTROLLER_H
#define PID_CONTROLLER_H

#include <Arduino.h>

class PIDController {
private:
    // Parametri PID
    float Kp, Ki, Kd;

    // Stati interni
    float integral;
    float prevError;
    float prevMeasurement;  // Per derivativo sul processo (non errore)

    // Limiti
    float outMin, outMax;
    float integralMin, integralMax;  // Anti-windup

    // Timing
    uint32_t lastTime;
    float sampleTime;  // secondi

    // Modalità
    bool autoMode;
    bool derivativeOnMeasurement;  // true = usa dM/dt invece di dE/dt

public:
    PIDController(float Kp, float Ki, float Kd);

    void setTunings(float Kp, float Ki, float Kd);
    void setOutputLimits(float min, float max);
    void setIntegralLimits(float min, float max);
    void setSampleTime(float seconds);
    void setDerivativeOnMeasurement(bool enable);

    float compute(float setpoint, float measurement);
    void reset();
    void setMode(bool autoMode);

    // Getters per diagnostica
    float getProportional() const;
    float getIntegral() const { return integral; }
    float getDerivative() const;
    float getError() const;
};

#endif

// pid_controller.cpp
#include "pid_controller.h"

PIDController::PIDController(float Kp, float Ki, float Kd)
    : Kp(Kp), Ki(Ki), Kd(Kd),
      integral(0), prevError(0), prevMeasurement(0),
      outMin(0), outMax(255),
      integralMin(-100), integralMax(100),
      lastTime(0), sampleTime(0.1),
      autoMode(false), derivativeOnMeasurement(true) {
}

void PIDController::setTunings(float Kp, float Ki, float Kd) {
    if(Kp < 0 || Ki < 0 || Kd < 0) return;

    this->Kp = Kp;
    this->Ki = Ki;
    this->Kd = Kd;
}

void PIDController::setOutputLimits(float min, float max) {
    if(min >= max) return;

    outMin = min;
    outMax = max;

    // Clamp integral se necessario
    if(integral > integralMax) integral = integralMax;
    if(integral < integralMin) integral = integralMin;
}

void PIDController::setIntegralLimits(float min, float max) {
    if(min >= max) return;

    integralMin = min;
    integralMax = max;
}

void PIDController::setSampleTime(float seconds) {
    if(seconds > 0) {
        sampleTime = seconds;
    }
}

void PIDController::setDerivativeOnMeasurement(bool enable) {
    derivativeOnMeasurement = enable;
}

float PIDController::compute(float setpoint, float measurement) {
    if(!autoMode) return 0;

    // Calcola dt
    uint32_t now = millis();
    float dt = (now - lastTime) / 1000.0;  // Convert to seconds

    if(lastTime == 0 || dt < sampleTime) {
        lastTime = now;
        return 0;  // Skip this cycle
    }

    lastTime = now;

    // Calcola errore
    float error = setpoint - measurement;

    // ========== PROPORZIONALE ==========
    float P = Kp * error;

    // ========== INTEGRALE ==========
    integral += error * dt;

    // Anti-windup: clamp integral
    if(integral > integralMax) integral = integralMax;
    if(integral < integralMin) integral = integralMin;

    float I = Ki * integral;

    // ========== DERIVATIVO ==========
    float D = 0;

    if(derivativeOnMeasurement) {
        // Derivativo sulla misura (evita "derivative kick")
        float derivative = -(measurement - prevMeasurement) / dt;
        D = Kd * derivative;
        prevMeasurement = measurement;
    } else {
        // Derivativo sull'errore (classico)
        float derivative = (error - prevError) / dt;
        D = Kd * derivative;
        prevError = error;
    }

    // ========== OUTPUT ==========
    float output = P + I + D;

    // Clamp output
    if(output > outMax) output = outMax;
    if(output < outMin) output = outMin;

    return output;
}

void PIDController::reset() {
    integral = 0;
    prevError = 0;
    prevMeasurement = 0;
    lastTime = 0;
}

void PIDController::setMode(bool autoMode) {
    if(autoMode && !this->autoMode) {
        // Transizione MANUAL → AUTO: reset integratore
        reset();
    }
    this->autoMode = autoMode;
}
```

### 5.3 Sistema Controllo Temperatura

```cpp
// temperature_controller.h
#ifndef TEMPERATURE_CONTROLLER_H
#define TEMPERATURE_CONTROLLER_H

#include "pid_controller.h"
#include <max6675.h>

class TemperatureController {
private:
    // Hardware
    MAX6675 thermocouple;
    const uint8_t heaterPin;
    const uint8_t fanPin;

    // PID
    PIDController pid;

    // State
    float setpoint;
    float currentTemp;
    float output;

    // Safety
    const float MAX_TEMP = 300.0;
    const float THERMAL_RUNAWAY_THRESHOLD = 10.0;  // °C/min max rate
    uint32_t lastTempCheckTime;
    float lastTempCheckValue;
    bool thermalRunawayDetected;

    // Profili temperatura
    struct TempProfile {
        const char* name;
        float temps[10];      // Temperature steps
        uint32_t times[10];   // Duration (seconds)
        uint8_t numSteps;
    };

    TempProfile* activeProfile;
    uint8_t currentProfileStep;
    uint32_t profileStepStartTime;

    bool checkSafety();
    void updateHeater(float power);

public:
    TemperatureController(uint8_t thermoDO, uint8_t thermoCS, uint8_t thermoCLK,
                         uint8_t heaterPin, uint8_t fanPin);

    void begin();
    void setSetpoint(float temp);
    void update();

    float getTemperature() const { return currentTemp; }
    float getSetpoint() const { return setpoint; }
    float getOutput() const { return output; }
    bool isSafe() const { return !thermalRunawayDetected; }

    void setPIDTunings(float Kp, float Ki, float Kd);
    void startProfile(TempProfile* profile);
    void stopProfile();

    void emergencyStop();
};

#endif

// temperature_controller.cpp
#include "temperature_controller.h"

TemperatureController::TemperatureController(
    uint8_t thermoDO, uint8_t thermoCS, uint8_t thermoCLK,
    uint8_t heaterPin, uint8_t fanPin)
    : thermocouple(thermoCLK, thermoCS, thermoDO),
      heaterPin(heaterPin), fanPin(fanPin),
      pid(2.0, 0.5, 1.0),  // Initial PID tunings
      setpoint(25.0), currentTemp(0), output(0),
      lastTempCheckTime(0), lastTempCheckValue(0),
      thermalRunawayDetected(false),
      activeProfile(nullptr), currentProfileStep(0) {
}

void TemperatureController::begin() {
    pinMode(heaterPin, OUTPUT);
    pinMode(fanPin, OUTPUT);

    // Sicurezza: heater OFF
    analogWrite(heaterPin, 0);
    digitalWrite(fanPin, HIGH);  // Fan ON per raffreddamento

    // Configura PID
    pid.setOutputLimits(0, 255);  // PWM range
    pid.setIntegralLimits(-50, 50);
    pid.setSampleTime(0.1);  // 100ms
    pid.setDerivativeOnMeasurement(true);  // Evita derivative kick
    pid.setMode(true);  // Auto mode

    Serial.println(F("[TempCtrl] Initialized"));

    // Test lettura termocoppia
    delay(500);
    currentTemp = thermocouple.readCelsius();

    if(isnan(currentTemp) || currentTemp < 0) {
        Serial.println(F("[TempCtrl] ⚠️  Thermocouple error!"));
    } else {
        Serial.printf("[TempCtrl] Current temp: %.1f°C\n", currentTemp);
    }
}

void TemperatureController::setSetpoint(float temp) {
    if(temp < 0 || temp > MAX_TEMP) {
        Serial.printf("[TempCtrl] ⚠️  Setpoint %.1f°C fuori range!\n", temp);
        return;
    }

    setpoint = temp;
    Serial.printf("[TempCtrl] Setpoint: %.1f°C\n", setpoint);
}

void TemperatureController::update() {
    // Lettura temperatura
    float newTemp = thermocouple.readCelsius();

    if(!isnan(newTemp) && newTemp >= 0 && newTemp <= MAX_TEMP + 50) {
        currentTemp = newTemp;
    } else {
        Serial.println(F("[TempCtrl] ⚠️  Thermocouple read error"));
        emergencyStop();
        return;
    }

    // Safety check
    if(!checkSafety()) {
        emergencyStop();
        return;
    }

    // Calcola PID
    output = pid.compute(setpoint, currentTemp);

    // Applica output
    updateHeater(output);

    // Gestione profili temperatura
    if(activeProfile != nullptr) {
        uint32_t elapsed = (millis() - profileStepStartTime) / 1000;

        if(elapsed >= activeProfile->times[currentProfileStep]) {
            // Next step
            currentProfileStep++;

            if(currentProfileStep >= activeProfile->numSteps) {
                // Profilo completato
                Serial.println(F("[TempCtrl] Profilo completato"));
                stopProfile();
            } else {
                // Carica nuovo setpoint
                setSetpoint(activeProfile->temps[currentProfileStep]);
                profileStepStartTime = millis();
                Serial.printf("[TempCtrl] Profilo step %d/%d: %.1f°C per %lus\n",
                             currentProfileStep + 1, activeProfile->numSteps,
                             activeProfile->temps[currentProfileStep],
                             activeProfile->times[currentProfileStep]);
            }
        }
    }
}

bool TemperatureController::checkSafety() {
    // 1. Check temperatura massima assoluta
    if(currentTemp > MAX_TEMP) {
        Serial.printf("[TempCtrl] 🚨 TEMP MAX EXCEEDED: %.1f°C\n", currentTemp);
        thermalRunawayDetected = true;
        return false;
    }

    // 2. Check thermal runaway (rate eccessivo)
    uint32_t now = millis();
    if(lastTempCheckTime > 0) {
        uint32_t dt = now - lastTempCheckTime;
        if(dt >= 60000) {  // Check ogni minuto
            float tempChange = currentTemp - lastTempCheckValue;
            float rate = (tempChange / dt) * 60000;  // °C/min

            if(rate > THERMAL_RUNAWAY_THRESHOLD) {
                Serial.printf("[TempCtrl] 🚨 THERMAL RUNAWAY: %.1f°C/min\n", rate);
                thermalRunawayDetected = true;
                return false;
            }

            lastTempCheckTime = now;
            lastTempCheckValue = currentTemp;
        }
    } else {
        lastTempCheckTime = now;
        lastTempCheckValue = currentTemp;
    }

    // 3. Check termocoppia disconnessa
    if(currentTemp < -10) {  // MAX6675 returns ~0 when disconnected
        Serial.println(F("[TempCtrl] 🚨 THERMOCOUPLE DISCONNECTED"));
        return false;
    }

    return true;
}

void TemperatureController::updateHeater(float power) {
    // Converti power (0-255) in PWM
    uint8_t pwm = constrain((int)power, 0, 255);

    analogWrite(heaterPin, pwm);

    // Gestione fan: ON se temp > 50°C o heater > 50%
    if(currentTemp > 50.0 || pwm > 127) {
        digitalWrite(fanPin, HIGH);
    } else {
        digitalWrite(fanPin, LOW);
    }
}

void TemperatureController::emergencyStop() {
    Serial.println(F("[TempCtrl] 🚨🚨🚨 EMERGENCY STOP 🚨🚨🚨"));

    analogWrite(heaterPin, 0);  // Heater OFF
    digitalWrite(fanPin, HIGH);  // Fan ON max

    pid.setMode(false);  // PID in manual
    stopProfile();

    thermalRunawayDetected = true;
}

void TemperatureController::setPIDTunings(float Kp, float Ki, float Kd) {
    pid.setTunings(Kp, Ki, Kd);
    Serial.printf("[TempCtrl] PID tunings: Kp=%.2f Ki=%.2f Kd=%.2f\n", Kp, Ki, Kd);
}

void TemperatureController::startProfile(TempProfile* profile) {
    if(profile == nullptr || profile->numSteps == 0) {
        Serial.println(F("[TempCtrl] ⚠️  Profilo non valido"));
        return;
    }

    activeProfile = profile;
    currentProfileStep = 0;
    profileStepStartTime = millis();

    setSetpoint(profile->temps[0]);

    Serial.printf("[TempCtrl] Profilo '%s' avviato (%d steps)\n",
                 profile->name, profile->numSteps);
}

void TemperatureController::stopProfile() {
    if(activeProfile != nullptr) {
        Serial.printf("[TempCtrl] Profilo '%s' fermato\n", activeProfile->name);
    }

    activeProfile = nullptr;
    currentProfileStep = 0;
}
```

### 5.4 Profili Temperatura Predefiniti

```cpp
// temperature_profiles.h

// Profilo Reflow Soldering (lead-free)
TemperatureController::TempProfile PROFILE_REFLOW = {
    .name = "Reflow Solder",
    .temps = {
        25,   // Ambiente
        150,  // Preheat
        180,  // Soak
        220,  // Reflow peak
        180,  // Cool down start
        100,
        50,
        25    // Finale
    },
    .times = {
        0,    // Start
        90,   // 90s to preheat
        120,  // 120s soak
        30,   // 30s peak
        60,   // 60s cool
        120,
        180,
        240   // Total ~11 minutes
    },
    .numSteps = 8
};

// Profilo Incubazione (biologica)
TemperatureController::TempProfile PROFILE_INCUBATOR = {
    .name = "Incubator 37C",
    .temps = {
        25,   // Ambiente
        37,   // Target stabile
    },
    .times = {
        0,
        300,  // 5 min ramp
    },
    .numSteps = 2
};

// Profilo Stress Test
TemperatureController::TempProfile PROFILE_STRESS_TEST = {
    .name = "Stress Test",
    .temps = {25, 100, 25, 150, 25, 200, 25},
    .times = {0, 300, 600, 900, 1200, 1500, 1800},  // Cicli 5 min
    .numSteps = 7
};
```

### 5.5 Auto-Tuning PID

```cpp
// pid_autotuner.h
#ifndef PID_AUTOTUNER_H
#define PID_AUTOTUNER_H

#include <Arduino.h>

class PIDAutoTuner {
private:
    float outputStep;
    float noiseBand;
    uint32_t lookbackMs;

    enum class TuningState {
        IDLE,
        RELAY_POSITIVE,
        RELAY_NEGATIVE,
        ANALYZING,
        COMPLETE
    };

    TuningState state;

    // Rilevamento oscillazioni
    float peakHigh, peakLow;
    uint32_t peakTime[2];
    uint8_t peakCount;

    // Risultati
    float Ku, Tu;  // Ultimate gain and period
    float Kp, Ki, Kd;

    bool detectPeak(float measurement);
    void calculatePID();

public:
    PIDAutoTuner(float outputStep, float noiseBand, uint32_t lookbackMs);

    void start();
    float update(float measurement, float setpoint);
    bool isComplete();

    void getTunings(float& Kp, float& Ki, float& Kd);
    String getReport();
};

#endif

// pid_autotuner.cpp
#include "pid_autotuner.h"

PIDAutoTuner::PIDAutoTuner(float outputStep, float noiseBand, uint32_t lookbackMs)
    : outputStep(outputStep), noiseBand(noiseBand), lookbackMs(lookbackMs),
      state(TuningState::IDLE), peakHigh(0), peakLow(1000), peakCount(0),
      Ku(0), Tu(0), Kp(0), Ki(0), Kd(0) {
}

void PIDAutoTuner::start() {
    state = TuningState::RELAY_POSITIVE;
    peakCount = 0;
    peakHigh = 0;
    peakLow = 1000;

    Serial.println(F("[AutoTune] Avvio procedura auto-tuning..."));
    Serial.println(F("[AutoTune] Metodo: Relay Feedback"));
}

float PIDAutoTuner::update(float measurement, float setpoint) {
    if(state == TuningState::IDLE || state == TuningState::COMPLETE) {
        return 0;
    }

    // Rileva picchi
    detectPeak(measurement);

    // Logica relay
    float output = 0;

    if(measurement < setpoint) {
        output = outputStep;
        state = TuningState::RELAY_POSITIVE;
    } else {
        output = 0;
        state = TuningState::RELAY_NEGATIVE;
    }

    // Check se abbiamo abbastanza dati
    if(peakCount >= 5) {  // Almeno 2-3 oscillazioni complete
        state = TuningState::ANALYZING;
        calculatePID();
        state = TuningState::COMPLETE;

        Serial.println(F("[AutoTune] ✅ Auto-tuning completato!"));
        Serial.println(getReport());
    }

    return output;
}

bool PIDAutoTuner::detectPeak(float measurement) {
    static float lastMeasurement = 0;
    static float lastLastMeasurement = 0;
    static uint32_t lastPeakTime = 0;

    // Rileva picco locale (max o min)
    bool isPeak = false;

    // Picco massimo
    if(measurement > lastMeasurement && lastMeasurement > lastLastMeasurement) {
        if(measurement > peakHigh + noiseBand) {
            peakHigh = measurement;
            peakTime[peakCount % 2] = millis();
            peakCount++;
            isPeak = true;

            Serial.printf("[AutoTune] Peak HIGH: %.2f (count=%d)\n", peakHigh, peakCount);
        }
    }

    // Picco minimo
    if(measurement < lastMeasurement && lastMeasurement < lastLastMeasurement) {
        if(measurement < peakLow - noiseBand) {
            peakLow = measurement;
            peakTime[peakCount % 2] = millis();
            peakCount++;
            isPeak = true;

            Serial.printf("[AutoTune] Peak LOW: %.2f (count=%d)\n", peakLow, peakCount);
        }
    }

    lastLastMeasurement = lastMeasurement;
    lastMeasurement = measurement;

    return isPeak;
}

void PIDAutoTuner::calculatePID() {
    // Calcola periodo oscillazione (Tu)
    if(peakCount >= 2) {
        Tu = (peakTime[1] - peakTime[0]) / 1000.0;  // Convert to seconds
    }

    // Calcola ampiezza oscillazione
    float amplitude = (peakHigh - peakLow) / 2.0;

    // Calcola ultimate gain (Ku)
    Ku = (4.0 * outputStep) / (M_PI * amplitude);

    // Formula Ziegler-Nichols per PID
    Kp = 0.6 * Ku;
    Ki = 2.0 * Kp / Tu;
    Kd = Kp * Tu / 8.0;

    Serial.printf("[AutoTune] Ku=%.3f, Tu=%.3fs\n", Ku, Tu);
}

bool PIDAutoTuner::isComplete() {
    return state == TuningState::COMPLETE;
}

void PIDAutoTuner::getTunings(float& Kp, float& Ki, float& Kd) {
    Kp = this->Kp;
    Ki = this->Ki;
    Kd = this->Kd;
}

String PIDAutoTuner::getReport() {
    String report = "\n=== AUTO-TUNING RISULTATI ===\n";
    report += "Ultimate Gain (Ku): " + String(Ku, 3) + "\n";
    report += "Ultimate Period (Tu): " + String(Tu, 3) + " s\n";
    report += "----------------------------\n";
    report += "PID Tunings (Ziegler-Nichols):\n";
    report += "  Kp = " + String(Kp, 3) + "\n";
    report += "  Ki = " + String(Ki, 3) + "\n";
    report += "  Kd = " + String(Kd, 3) + "\n";
    report += "============================\n";

    return report;
}
```

### 5.6 Main Application con TFT Display

```cpp
// main_temperature_controller.cpp
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include "temperature_controller.h"
#include "pid_autotuner.h"

// Pin Definitions
#define THERMO_DO   12
#define THERMO_CS   10
#define THERMO_CLK  13
#define HEATER_PIN  9  // PWM
#define FAN_PIN     8

#define TFT_CS      7
#define TFT_DC      6
#define TFT_RST     5

// Objects
Adafruit_ILI9341 tft(TFT_CS, TFT_DC, TFT_RST);
TemperatureController tempCtrl(THERMO_DO, THERMO_CS, THERMO_CLK,
                                HEATER_PIN, FAN_PIN);

PIDAutoTuner autotuner(128, 1.0, 10000);  // 50% output, 1°C noise, 10s lookback

bool autotuning = false;

// ====================
// SETUP
// ====================
void setup() {
    Serial.begin(115200);

    Serial.println(F("\n╔══════════════════════════════════╗"));
    Serial.println(F("║  PID Temperature Controller      ║"));
    Serial.println(F("║  Version 1.0                     ║"));
    Serial.println(F("╚══════════════════════════════════╝\n"));

    // Inizializza TFT
    tft.begin();
    tft.setRotation(1);  // Landscape
    tft.fillScreen(ILI9341_BLACK);
    tft.setTextColor(ILI9341_WHITE);
    tft.setTextSize(2);
    tft.setCursor(10, 10);
    tft.println("Temp Controller");
    tft.println("Initializing...");

    // Inizializza controller
    tempCtrl.begin();
    tempCtrl.setSetpoint(25.0);  // Ambient

    delay(2000);
}

// ====================
// LOOP
// ====================
void loop() {
    // Update controller
    if(!autotuning) {
        tempCtrl.update();
    } else {
        // Auto-tuning mode
        float output = autotuner.update(tempCtrl.getTemperature(),
                                       tempCtrl.getSetpoint());

        // Applica output direttamente (bypass PID)
        analogWrite(HEATER_PIN, (uint8_t)output);

        if(autotuner.isComplete()) {
            float Kp, Ki, Kd;
            autotuner.getTunings(Kp, Ki, Kd);
            tempCtrl.setPIDTunings(Kp, Ki, Kd);
            autotuning = false;

            Serial.println(F("Auto-tuning completato, PID aggiornato"));
        }
    }

    // Update display
    updateDisplay();

    // Debug seriale
    static uint32_t lastDebug = 0;
    if(millis() - lastDebug > 1000) {
        lastDebug = millis();

        Serial.printf("SP:%.1f PV:%.1f OUT:%.1f%%\n",
                     tempCtrl.getSetpoint(),
                     tempCtrl.getTemperature(),
                     (tempCtrl.getOutput() / 255.0) * 100);
    }

    delay(100);
}

void updateDisplay() {
    static uint32_t lastUpdate = 0;
    if(millis() - lastUpdate < 500) return;
    lastUpdate = millis();

    tft.fillScreen(ILI9341_BLACK);

    // Setpoint
    tft.setCursor(10, 10);
    tft.setTextColor(ILI9341_YELLOW);
    tft.setTextSize(2);
    tft.print("SP: ");
    tft.print(tempCtrl.getSetpoint(), 1);
    tft.println(" C");

    // Current temp (grande)
    tft.setCursor(10, 50);
    tft.setTextColor(ILI9341_WHITE);
    tft.setTextSize(4);
    tft.print(tempCtrl.getTemperature(), 1);
    tft.println(" C");

    // Output power
    tft.setCursor(10, 110);
    tft.setTextColor(ILI9341_CYAN);
    tft.setTextSize(2);
    tft.print("PWR: ");
    tft.print((int)((tempCtrl.getOutput() / 255.0) * 100));
    tft.println(" %");

    // Safety status
    tft.setCursor(10, 140);
    if(tempCtrl.isSafe()) {
        tft.setTextColor(ILI9341_GREEN);
        tft.print("SAFE");
    } else {
        tft.setTextColor(ILI9341_RED);
        tft.print("ALARM!");
    }

    // Progress bar output
    int barWidth = 300;
    int barHeight = 20;
    int barX = 10;
    int barY = 180;

    tft.drawRect(barX, barY, barWidth, barHeight, ILI9341_WHITE);

    int fillWidth = (tempCtrl.getOutput() / 255.0) * (barWidth - 4);
    tft.fillRect(barX + 2, barY + 2, fillWidth, barHeight - 4, ILI9341_GREEN);
}
```

### 5.7 Uso con IA per Testing

**Prompt per generare test PID:**

```
"Genera test suite completa per controllore PID temperatura:

SISTEMA:
- Classe PIDController con metodo compute()
- TemperatureController con MAX6675
- Auto-tuner Ziegler-Nichols

TEST RICHIESTI:
1. Test risposta step (setpoint 25→100°C)
   - Misura rise time, overshoot, settling time
   - Verifica steady-state error < 1°C

2. Test disturbance rejection
   - Applica disturbo esterno (es. porta aperta)
   - Verifica recupero entro 2 minuti

3. Test thermal runaway protection
   - Simula sensor failure
   - Verifica emergency stop

4. Test auto-tuning
   - Esegui procedura completa
   - Valida parametri calcolati in range accettabile

OUTPUT:
- Funzioni test C++ eseguibili
- Simulazione processo termico (transfer function)
- Logging dati CSV per analisi offline
- Plot risultati (descrizione verbale)
"
```

Continuo il documento nel prossimo messaggio per completare i progetti rimanenti e le sezioni finali...

---

*[Il documento continua con Progetto 4, Cloud Integration, ML, Testing, Security, Optimization, Deployment, Documentation e Exercises per raggiungere circa 2000 righe totali]*

---

## 6. Progetto 4: Sistema Automazione Domestica

### 6.1 Descrizione Progetto

**Nome:** Smart Home Hub

**Obiettivo:** Sistema centralizzato controllo automazione domestica multi-protocollo con intelligenza locale.

**Funzionalità:**
- Controllo luci (dimming PWM + relay)
- Gestione termostato intelligente
- Rilevazione presenza (PIR + ultrasonic)
- Controllo serrande automatiche
- Monitoring consumi elettrici
- Allarme intrusioniintegrato
- Voice control (via MQTT)
- Web dashboard

### 6.2 Architettura Sistema

```
┌──────────────────────────────────────────────┐
│         ESP32 Main Controller                │
│         (Hub Centrale)                       │
├──────────────────────────────────────────────┤
│                                              │
│  SENSORI INPUT                               │
│  ├─ 4x PIR motion (GPIO)                     │
│  ├─ 2x Door sensor (magnetic)               │
│  ├─ DHT22 temp/humidity                     │
│  ├─ LDR light level                         │
│  └─ Current sensor ACS712                   │
│                                              │
│  ATTUATORI OUTPUT                            │
│  ├─ 4x Relay 220V (luci, prese)            │
│  ├─ 2x MOSFET PWM (LED dimming)            │
│  ├─ Servo motore (serranda)                │
│  └─ Buzzer allarme                          │
│                                              │
│  COMUNICAZIONE                               │
│  ├─ WiFi (controllo remoto)                │
│  ├─ MQTT (integrazione HA)                  │
│  ├─ HTTP REST API                           │
│  └─ WebSocket (real-time)                   │
│                                              │
│  INTERFACCIA                                 │
│  ├─ TFT touch 3.5" (controllo locale)      │
│  └─ LED status RGB                          │
└──────────────────────────────────────────────┘
```

### 6.3 Implementazione Core

```cpp
// home_automation.h
#ifndef HOME_AUTOMATION_H
#define HOME_AUTOMATION_H

#include <Arduino.h>
#include <vector>

// Device types
enum class DeviceType {
    LIGHT_RELAY,      // On/Off relay
    LIGHT_DIMMABLE,   // PWM dimming
    OUTLET_SWITCH,    // Smart plug
    WINDOW_BLIND,     // Servo controlled
    THERMOSTAT,       // Temperature control
    SENSOR_MOTION,
    SENSOR_DOOR,
    SENSOR_TEMP
};

// Device states
struct DeviceState {
    bool isOn;
    uint8_t brightness;  // 0-100%
    float temperature;
    bool detected;       // For sensors
};

// Abstract device class
class SmartDevice {
protected:
    String name;
    String id;
    DeviceType type;
    DeviceState state;

public:
    SmartDevice(String name, String id, DeviceType type)
        : name(name), id(id), type(type) {
        state = {false, 0, 0, false};
    }

    virtual void update() = 0;
    virtual void setState(DeviceState newState) = 0;
    virtual DeviceState getState() = 0;

    String getName() { return name; }
    String getID() { return id; }
    DeviceType getType() { return type; }
};

// Smart Light (Dimmable)
class SmartLight : public SmartDevice {
private:
    uint8_t pin;

public:
    SmartLight(String name, String id, uint8_t pin)
        : SmartDevice(name, id, DeviceType::LIGHT_DIMMABLE), pin(pin) {
        pinMode(pin, OUTPUT);
    }

    void update() override {
        // Apply PWM based on brightness
        uint8_t pwm = map(state.brightness, 0, 100, 0, 255);
        analogWrite(pin, state.isOn ? pwm : 0);
    }

    void setState(DeviceState newState) override {
        state.isOn = newState.isOn;
        state.brightness = constrain(newState.brightness, 0, 100);
        update();
    }

    DeviceState getState() override {
        return state;
    }
};

// Motion Sensor
class MotionSensor : public SmartDevice {
private:
    uint8_t pin;
    uint32_t lastDetection;
    const uint32_t TIMEOUT_MS = 60000;  // 1 min

public:
    MotionSensor(String name, String id, uint8_t pin)
        : SmartDevice(name, id, DeviceType::SENSOR_MOTION),
          pin(pin), lastDetection(0) {
        pinMode(pin, INPUT);
    }

    void update() override {
        bool detected = digitalRead(pin) == HIGH;

        if(detected) {
            lastDetection = millis();
            state.detected = true;
        } else {
            // Timeout after no detection
            if(millis() - lastDetection > TIMEOUT_MS) {
                state.detected = false;
            }
        }
    }

    void setState(DeviceState newState) override {
        // Read-only sensor
    }

    DeviceState getState() override {
        return state;
    }
};

// Home Automation Manager
class HomeAutomationManager {
private:
    std::vector<SmartDevice*> devices;

    // Automation rules
    struct AutomationRule {
        String name;
        String triggerDeviceID;
        String actionDeviceID;
        bool (*condition)(DeviceState);
        DeviceState targetState;
        bool enabled;
    };

    std::vector<AutomationRule> rules;

public:
    void addDevice(SmartDevice* device) {
        devices.push_back(device);
    }

    void update() {
        // Update all devices
        for(auto device : devices) {
            device->update();
        }

        // Check automation rules
        checkRules();
    }

    SmartDevice* getDevice(String id) {
        for(auto device : devices) {
            if(device->getID() == id) {
                return device;
            }
        }
        return nullptr;
    }

    void addRule(AutomationRule rule) {
        rules.push_back(rule);
    }

    void checkRules() {
        for(auto& rule : rules) {
            if(!rule.enabled) continue;

            SmartDevice* trigger = getDevice(rule.triggerDeviceID);
            SmartDevice* action = getDevice(rule.actionDeviceID);

            if(trigger && action) {
                DeviceState triggerState = trigger->getState();

                if(rule.condition(triggerState)) {
                    action->setState(rule.targetState);
                }
            }
        }
    }
};

#endif
```

### 6.4 Regole Automazione

```cpp
// automation_rules.cpp

// Regola: Accendi luce quando rileva movimento
bool motionDetectedCondition(DeviceState state) {
    return state.detected == true;
}

void setupAutomationRules(HomeAutomationManager& manager) {
    // Regola 1: Motion → Light ON
    HomeAutomationManager::AutomationRule rule1;
    rule1.name = "Motion Activated Light";
    rule1.triggerDeviceID = "sensor_motion_living";
    rule1.actionDeviceID = "light_living_main";
    rule1.condition = motionDetectedCondition;
    rule1.targetState = {true, 80, 0, false};  // ON, 80% brightness
    rule1.enabled = true;

    manager.addRule(rule1);

    // Regola 2: Sunset → Lights ON
    // ...

    Serial.println(F("[Automation] Rules loaded"));
}
```

---

## 7. Integrazione Cloud e Visualizzazione

### 7.1 Dashboard Node-RED

**Installazione Node-RED:**

```bash
# Su Raspberry Pi o server Linux
sudo npm install -g --unsafe-perm node-red

# Avvio
node-red

# Accesso: http://localhost:1880
```

**Flow Example - MQTT to Dashboard:**

```json
[
    {
        "id": "mqtt_in",
        "type": "mqtt in",
        "topic": "sensors/+/data",
        "broker": "mqtt_broker",
        "name": "Sensor Data"
    },
    {
        "id": "json_parse",
        "type": "json"
    },
    {
        "id": "gauge_temp",
        "type": "ui_gauge",
        "min": 0,
        "max": 50,
        "label": "Temperature"
    },
    {
        "id": "chart_history",
        "type": "ui_chart",
        "label": "Last Hour"
    }
]
```

### 7.2 InfluxDB + Grafana

**Setup su Docker:**

```bash
# docker-compose.yml
version: '3'
services:
  influxdb:
    image: influxdb:2.7
    ports:
      - "8086:8086"
    volumes:
      - influxdb_data:/var/lib/influxdb2

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - influxdb

volumes:
  influxdb_data:
  grafana_data:
```

**ESP32 → InfluxDB:**

```cpp
#include <InfluxDbClient.h>

InfluxDBClient client("http://192.168.1.100:8086", "org", "bucket", "token");

void sendToInfluxDB(SensorData data) {
    Point point("environment");

    point.addTag("device", "esp32_001");
    point.addTag("location", "living_room");

    point.addField("temperature", data.temperature);
    point.addField("humidity", data.humidity);
    point.addField("pressure", data.pressure);

    if(!client.writePoint(point)) {
        Serial.print("InfluxDB write failed: ");
        Serial.println(client.getLastErrorMessage());
    }
}
```

---

## 8. Machine Learning su Embedded

### 8.1 TensorFlow Lite Micro - Anomaly Detection

```cpp
// ml_anomaly_detection.cpp
#include <TensorFlowLite_ESP32.h>
#include "model_data.h"  // Generated from TFLite model

namespace {
    tflite::MicroErrorReporter micro_error_reporter;
    tflite::ErrorReporter* error_reporter = &micro_error_reporter;

    const tflite::Model* model = nullptr;
    tflite::MicroInterpreter* interpreter = nullptr;
    TfLiteTensor* input = nullptr;
    TfLiteTensor* output = nullptr;

    constexpr int kTensorArenaSize = 20000;
    uint8_t tensor_arena[kTensorArenaSize];
}

bool setupML() {
    // Load model
    model = tflite::GetModel(g_model_data);
    if(model->version() != TFLITE_SCHEMA_VERSION) {
        Serial.println("Model schema mismatch!");
        return false;
    }

    // Setup interpreter
    static tflite::MicroMutableOpResolver<5> resolver;
    resolver.AddFullyConnected();
    resolver.AddRelu();
    resolver.AddSoftmax();

    static tflite::MicroInterpreter static_interpreter(
        model, resolver, tensor_arena, kTensorArenaSize, error_reporter);
    interpreter = &static_interpreter;

    // Allocate tensors
    if(interpreter->AllocateTensors() != kTfLiteOk) {
        Serial.println("AllocateTensors failed!");
        return false;
    }

    input = interpreter->input(0);
    output = interpreter->output(0);

    Serial.println("ML Model loaded successfully");
    return true;
}

bool detectAnomaly(const SensorData& data) {
    // Preprocessing: normalize inputs
    input->data.f[0] = (data.temperature - 20.0) / 30.0;     // Norm to ~[-1,1]
    input->data.f[1] = (data.humidity - 50.0) / 50.0;
    input->data.f[2] = (data.pressure - 1000.0) / 100.0;
    input->data.f[3] = data.light / 65535.0;
    input->data.f[4] = data.airQuality / 1000.0;

    // Inference
    if(interpreter->Invoke() != kTfLiteOk) {
        Serial.println("Inference failed!");
        return false;
    }

    // Output: anomaly score [0,1]
    float anomalyScore = output->data.f[0];

    Serial.printf("Anomaly score: %.3f\n", anomalyScore);

    return anomalyScore > 0.75;  // Threshold
}
```

### 8.2 Edge Impulse Integration

**Workflow:**

1. **Data Collection:**
```cpp
// Collect training data
void collectTrainingData() {
    for(int i = 0; i < 1000; i++) {
        SensorData data = sensors.readAll();

        // Format: timestamp, feature1, feature2, ..., label
        Serial.printf("%lu,%.2f,%.2f,%.2f,%d,%d,%s\n",
                     millis(),
                     data.temperature,
                     data.humidity,
                     data.pressure,
                     data.light,
                     data.airQuality,
                     "normal");  // or "anomaly"

        delay(100);
    }
}
```

2. **Train on Edge Impulse** (cloud platform)
3. **Export as Arduino library**
4. **Deploy:**

```cpp
#include <env_monitor_inferencing.h>

void runInference() {
    float features[5] = {
        data.temperature,
        data.humidity,
        data.pressure,
        (float)data.light,
        (float)data.airQuality
    };

    ei_impulse_result_t result;

    signal_t signal;
    signal.total_length = 5;
    signal.get_data = &get_signal_data;

    run_classifier(&signal, &result);

    // Results
    for(int i = 0; i < EI_CLASSIFIER_LABEL_COUNT; i++) {
        Serial.printf("%s: %.2f\n",
                     result.classification[i].label,
                     result.classification[i].value);
    }
}
```

---

## 9. Testing e Quality Assurance

### 9.1 Unit Testing Framework

```cpp
// test_framework.h
#ifndef TEST_FRAMEWORK_H
#define TEST_FRAMEWORK_H

#include <Arduino.h>

class TestFramework {
private:
    int totalTests;
    int passedTests;
    int failedTests;

public:
    TestFramework() : totalTests(0), passedTests(0), failedTests(0) {}

    void assertTrue(bool condition, const char* message) {
        totalTests++;
        if(condition) {
            Serial.printf("✅ PASS: %s\n", message);
            passedTests++;
        } else {
            Serial.printf("❌ FAIL: %s\n", message);
            failedTests++;
        }
    }

    void assertEqual(float expected, float actual, const char* message, float tolerance = 0.01) {
        totalTests++;
        if(abs(expected - actual) < tolerance) {
            Serial.printf("✅ PASS: %s (%.2f == %.2f)\n", message, expected, actual);
            passedTests++;
        } else {
            Serial.printf("❌ FAIL: %s (expected %.2f, got %.2f)\n", message, expected, actual);
            failedTests++;
        }
    }

    void printSummary() {
        Serial.println("\n═══════════════════════════════");
        Serial.printf("Total Tests:  %d\n", totalTests);
        Serial.printf("Passed:       %d (%.0f%%)\n", passedTests, (float)passedTests/totalTests*100);
        Serial.printf("Failed:       %d\n", failedTests);
        Serial.println("═══════════════════════════════");
    }
};

#endif
```

### 9.2 Integration Tests

```cpp
// integration_tests.cpp

void testFullDataPipeline() {
    Serial.println("\n=== INTEGRATION TEST: Full Pipeline ===");

    TestFramework test;

    // 1. Sensor reading
    SensorData data = sensors.readAll();
    test.assertTrue(data.valid, "Sensor reading valid");

    // 2. Alarm check
    AlarmLevel level = alarms.checkAlarms(data);
    test.assertTrue(level != AlarmLevel::ERROR, "Alarm system functional");

    // 3. Cloud upload
    bool uploaded = cloud.publishSensorData(data);
    test.assertTrue(uploaded, "Cloud upload successful");

    // 4. Display update
    display.update(data, SystemState::IDLE, true, level);
    // Visual check

    test.printSummary();
}
```

---

## 10. Sicurezza nei Sistemi IoT

### 10.1 Autenticazione e Crittografia

```cpp
// secure_mqtt.cpp
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

WiFiClientSecure secureClient;
PubSubClient mqttSecure(secureClient);

// Certificati (salvare in separate file)
const char* ca_cert = R"EOF(
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
)EOF";

void setupSecureMQTT() {
    secureClient.setCACert(ca_cert);

    mqttSecure.setServer("mqtt.example.com", 8883);  // SSL port
    mqttSecure.connect("ESP32Client", "username", "password");
}
```

### 10.2 OTA Sicuro

```cpp
// secure_ota.cpp
#include <ArduinoOTA.h>
#include <ESPmDNS.h>

void setupSecureOTA() {
    ArduinoOTA.setHostname("env-monitor");
    ArduinoOTA.setPassword("strong_password_here");

    ArduinoOTA.onStart([]() {
        Serial.println("OTA Start");
        display.showMessage("OTA Update...");
    });

    ArduinoOTA.onEnd([]() {
        Serial.println("OTA Complete");
    });

    ArduinoOTA.onError([](ota_error_t error) {
        Serial.printf("OTA Error[%u]: ", error);
        if(error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
        else if(error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
        else if(error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
        else if(error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
        else if(error == OTA_END_ERROR) Serial.println("End Failed");
    });

    ArduinoOTA.begin();
}
```

---

## 11. Ottimizzazione e Performance

### 11.1 Profiling Memoria

```cpp
void printMemoryStats() {
    Serial.println("\n=== MEMORY STATS ===");
    Serial.printf("Free Heap: %d bytes\n", ESP.getFreeHeap());
    Serial.printf("Heap Size: %d bytes\n", ESP.getHeapSize());
    Serial.printf("Min Free Heap: %d bytes\n", ESP.getMinFreeHeap());
    Serial.printf("Max Alloc Heap: %d bytes\n", ESP.getMaxAllocHeap());
    Serial.println("====================\n");
}
```

### 11.2 Power Optimization

```cpp
// deep_sleep.cpp
#include <esp_sleep.h>

void enterDeepSleep(uint32_t seconds) {
    Serial.printf("Entering deep sleep for %lu seconds\n", seconds);

    // Salva stato in RTC memory se necessario
    // ...

    esp_sleep_enable_timer_wakeup(seconds * 1000000ULL);

    // Cleanup
    cloud.publishStatus("sleeping");
    WiFi.disconnect();

    esp_deep_sleep_start();
}

void wakeupCallback() {
    esp_sleep_wakeup_cause_t wakeup_reason = esp_sleep_get_wakeup_cause();

    switch(wakeup_reason) {
        case ESP_SLEEP_WAKEUP_TIMER:
            Serial.println("Wakeup from timer");
            break;
        case ESP_SLEEP_WAKEUP_EXT0:
            Serial.println("Wakeup from external signal");
            break;
        default:
            Serial.printf("Wakeup from unknown: %d\n", wakeup_reason);
    }
}
```

---

## 12. Deployment e Manutenzione

### 12.1 Configuration Management

```cpp
// config_manager.h
#include <Preferences.h>

class ConfigManager {
private:
    Preferences prefs;

public:
    bool begin() {
        return prefs.begin("env-mon", false);
    }

    void saveWiFiCredentials(const char* ssid, const char* password) {
        prefs.putString("wifi_ssid", ssid);
        prefs.putString("wifi_pass", password);
    }

    String getWiFiSSID() {
        return prefs.getString("wifi_ssid", "");
    }

    String getWiFiPassword() {
        return prefs.getString("wifi_pass", "");
    }

    void saveAlarmThresholds(AlarmThresholds thresh) {
        prefs.putFloat("temp_warn_hi", thresh.temp_warning_high);
        prefs.putFloat("temp_alarm_hi", thresh.temp_alarm_high);
        // ... altre soglie
    }

    AlarmThresholds loadAlarmThresholds() {
        AlarmThresholds thresh;
        thresh.temp_warning_high = prefs.getFloat("temp_warn_hi", 30.0);
        thresh.temp_alarm_high = prefs.getFloat("temp_alarm_hi", 35.0);
        // ... altre soglie
        return thresh;
    }
};
```

### 12.2 Remote Monitoring

```cpp
// health_check.cpp

struct SystemHealth {
    uint32_t uptime;
    uint32_t freeHeap;
    int8_t wifiRSSI;
    uint32_t errorCount;
    float cpuTemperature;
};

void publishHealthCheck() {
    SystemHealth health;

    health.uptime = millis() / 1000;
    health.freeHeap = ESP.getFreeHeap();
    health.wifiRSSI = WiFi.RSSI();
    health.errorCount = stats.sdWriteErrors + stats.droppedSamples;
    health.cpuTemperature = temperatureRead();  // ESP32 internal sensor

    StaticJsonDocument<256> doc;
    doc["uptime"] = health.uptime;
    doc["free_heap"] = health.freeHeap;
    doc["wifi_rssi"] = health.wifiRSSI;
    doc["errors"] = health.errorCount;
    doc["cpu_temp"] = health.cpuTemperature;

    char buffer[256];
    serializeJson(doc, buffer);

    cloud.publishStatus(buffer);
}
```

---

## 13. Documentazione Progetti

### 13.1 Template README Completo

```markdown
# Environmental Monitor Pro

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

Sistema professionale di monitoraggio ambientale IoT.

## 🎯 Features

- ✅ Multi-sensor monitoring (temp, humidity, pressure, light, air quality)
- ✅ Real-time OLED display
- ✅ Cloud connectivity (MQTT)
- ✅ Intelligent alarms
- ✅ Web dashboard
- ✅ Machine learning anomaly detection
- ✅ OTA updates

## 📦 Hardware Requirements

Full BOM in [docs/BOM.md](docs/BOM.md)

| Component | Specs | Qty | Est. Cost |
|-----------|-------|-----|-----------|
| ESP32 DevKit | WiFi/BT | 1 | $8 |
| DHT22 | Temp/Hum | 1 | $5 |
| ... | ... | ... | ... |
| **TOTAL** | | | **~$50** |

## 🔌 Wiring Diagram

![Wiring](docs/wiring_diagram.png)

See [docs/HARDWARE.md](docs/HARDWARE.md) for detailed connections.

## 🚀 Quick Start

### 1. Install Platform IO

```bash
pip install platformio
```

### 2. Clone & Build

```bash
git clone https://github.com/user/env-monitor.git
cd env-monitor
pio run
```

### 3. Configure

Edit `src/config.h`:

```cpp
#define WIFI_SSID "YourWiFi"
#define WIFI_PASSWORD "YourPassword"
#define MQTT_SERVER "broker.hivemq.com"
```

### 4. Upload

```bash
pio run --target upload
pio device monitor
```

## 📊 Data Format

MQTT topic: `sensors/{DEVICE_ID}/data`

```json
{
  "device_id": "env-mon-001",
  "timestamp": 1234567890,
  "temperature": 23.5,
  "humidity": 55.2,
  "pressure": 1013.2,
  "light": 450,
  "air_quality": 150
}
```

## 🔧 Configuration

See [docs/CONFIGURATION.md](docs/CONFIGURATION.md)

## 🧪 Testing

```bash
pio test
```

## 📈 Dashboard

Access web dashboard: `http://{ESP32_IP}/`

Node-RED flow: [flows/nodered_dashboard.json](flows/nodered_dashboard.json)

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| WiFi not connecting | Check SSID/password, signal strength |
| Sensor timeout | Verify wiring, add pull-up resistor |
| MQTT disconnects | Check broker URL, credentials |

Full guide: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

## 🤝 Contributing

Pull requests welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 👤 Author

**Your Name**
- GitHub: [@username](https://github.com/username)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Adafruit for sensor libraries
- PubSubClient MQTT library
- Edge Impulse for ML tools
```

---

## 14. Presentazione e Portfolio

### 14.1 Slide Presentation Template

```markdown
SLIDE 1: TITLE
─────────────────
Environmental Monitor Pro
Your Name
ITS Course 2025

[Foto progetto]

SLIDE 2: PROBLEMA
─────────────────
❌ Problemi attuali:
- Ambienti non monitorati
- Consumi energetici elevati
- Reazione lenta a emergenze

✅ Soluzione:
Sistema IoT intelligente real-time

SLIDE 3: ARCHITETTURA
─────────────────────
[Diagramma blocchi]

Sensori → ESP32 → Cloud → Dashboard

SLIDE 4: DEMO HARDWARE
──────────────────────
[Video/Foto hardware assemblato]

Componenti chiave:
- ESP32 (cervello)
- 5 sensori ambientali
- Display OLED
- Cloud MQTT

SLIDE 5: FUNZIONALITÀ
─────────────────────
1. Monitoring real-time
2. Allarmi intelligenti
3. Cloud storage
4. ML anomaly detection
5. OTA updates

SLIDE 6: TECNOLOGIE
───────────────────
Hardware:
- ESP32, sensori vari

Software:
- C++ / Arduino
- MQTT protocol
- TensorFlow Lite

AI Tools:
- Claude per codice
- Edge Impulse per ML

SLIDE 7: SFIDE SUPERATE
───────────────────────
1. Gestione memoria limitata
   → Ottimizzazione buffer

2. Connettività instabile
   → Auto-reconnect + buffer locale

3. Consumo energetico
   → Deep sleep mode

SLIDE 8: RISULTATI
──────────────────
✅ 99.5% uptime
✅ <500mA consumo
✅ Anomaly detection 95% accuracy
✅ Sub-second alarm response

SLIDE 9: SVILUPPI FUTURI
────────────────────────
- Integrazione voice assistant
- App mobile dedicata
- Multi-device mesh network
- Predictive maintenance

SLIDE 10: GRAZIE
────────────────
Q&A

Contatti:
GitHub: github.com/yourname/env-monitor
Email: your@email.com
```

### 14.2 Video Demo Script

```
INTRO (15 sec)
──────────────
"Ciao, sono [Nome]. Vi presento Environmental Monitor Pro,
un sistema IoT per monitoraggio ambientale intelligente."

[Mostra hardware assemblato]

PROBLEMA (30 sec)
─────────────────
"Negli ambienti domestici e industriali, il controllo ambientale
è spesso reattivo invece che proattivo. Il mio sistema risolve
questo problema con monitoring real-time e allarmi predittivi."

HARDWARE (60 sec)
─────────────────
[Panoramica componenti]
"Il cuore del sistema è un ESP32, connesso a 5 sensori ambientali:
temperatura, umidità, pressione, luce e qualità dell'aria.

I dati vengono mostrati su display OLED locale e inviati al cloud
via MQTT per analisi e storico."

[Mostra collegamenti principali]

DEMO LIVE (90 sec)
──────────────────
[Accensione sistema]
"All'avvio, il sistema si connette automaticamente al WiFi..."

[Mostra display]
"...e inizia il monitoring. Ogni 30 secondi legge tutti i sensori."

[Simulazione allarme - avvicina fonte calore]
"Quando la temperatura supera la soglia, il sistema attiva
l'allarme visivo e sonoro, e invia notifica al cloud."

[Mostra dashboard web]
"La dashboard web mostra dati real-time e storico."

TECNICA (45 sec)
────────────────
"Dal punto di vista tecnico, ho usato:
- C++ su piattaforma ESP32
- Librerie Adafruit per sensori
- Protocollo MQTT per cloud
- TensorFlow Lite per anomaly detection

Ho sviluppato con supporto IA (Claude) per accelerare
implementazione moduli standard, concentrandomi su
architettura e integrazione."

CONCLUSIONI (15 sec)
────────────────────
"Il sistema è completamente funzionante, open-source su GitHub,
e pronto per deployment reale. Grazie per l'attenzione!"

[Fade to credits con link GitHub]
```

---

## 15. Esercitazioni Guidate

### Esercitazione 1: Estendere Progetto 1 con Database Locale

**Obiettivo:** Aggiungere storage SQLite locale per backup dati quando cloud offline.

**Step:**
1. Installa libreria `sqlite3` per ESP32
2. Crea database con tabella `sensor_data`
3. Implementa classe `LocalStorage` con metodi `insert()` e `syncToCloud()`
4. Modifica main per usare storage ibrido

**Prompt IA:**
```
"Implementa classe LocalStorage per ESP32 con:
- SQLite database su SPIFFS
- Tabella sensor_data (timestamp, temp, hum, ...)
- Metodo insert() per salvare campione
- Metodo syncToCloud() per upload batch quando online
- Gestione limite size database (max 10MB)
- Auto-cleanup dati vecchi (>7 giorni)"
```

### Esercitazione 2: PID Auto-Tuning Avanzato

**Obiettivo:** Implementare auto-tuning PID con metodo Relay Feedback.

**Step:**
1. Studia teoria relay feedback
2. Implementa classe `RelayAutoTuner`
3. Integra in `TemperatureController`
4. Test con sistema reale

**Challenge:** Ottimizza per processi lenti (es. forno) vs veloci (es. motor control).

### Esercitazione 3: Dashboard React Personalizzata

**Obiettivo:** Creare dashboard web moderna con React.

**Stack:**
- React + TypeScript
- MQTT.js per real-time
- Recharts per grafici
- Material-UI per UI

**Step:**
1. Setup progetto React
2. Implementa MQTT client
3. Crea componenti display dati
4. Deploy su ESP32 SPIFFS o server esterno

---

## ✅ Checklist Completamento Modulo

Verifica di aver completato:

**Progettazione:**
- [ ] Analisi requisiti completa per almeno 1 progetto
- [ ] Architettura sistema documentata
- [ ] Schema elettrico validato
- [ ] BOM (Bill of Materials) con costi

**Implementazione:**
- [ ] Codice modulare e ben strutturato
- [ ] Gestione errori completa
- [ ] Comunicazione cloud funzionante
- [ ] Testing unitari e integrazione

**IA e Automazione:**
- [ ] Uso strategico IA per codice boilerplate
- [ ] Prompt engineering efficace
- [ ] Validazione manuale output IA
- [ ] Comprensione profonda codice generato

**Documentazione:**
- [ ] README professionale
- [ ] Commenti codice chiari
- [ ] Guida troubleshooting
- [ ] Schema collegamenti hardware

**Presentazione:**
- [ ] Almeno 1 progetto completo funzionante
- [ ] Video demo (3-5 min)
- [ ] Repository GitHub pubblico
- [ ] Slide presentazione tecnica

**Competenze Avanzate:**
- [ ] Integrazione ML (anche base)
- [ ] Ottimizzazione performance
- [ ] Sicurezza implementata
- [ ] OTA updates funzionanti

---

**Fine Modulo 5**

*Prossimo: Modulo 6 - Verifica Finale e Certificazione*

---

**Versione:** 2.0 | **Ultimo aggiornamento:** Dicembre 2024 | **Corso ITS - Fondamenti IA**

**Repository Codice Esempio:** https://github.com/its-ai-course/modulo5-progetti

**Supporto:** Canale Discord corso ITS - #modulo5-progetti
