# 🔧 APPENDICE: ARDUINO E SISTEMI EMBEDDED CON IA
## Materiale di Riferimento Opzionale - Corso ITS

**Nota:** Questa appendice è materiale **opzionale** per studenti che hanno accesso a hardware Arduino e vogliono applicare le competenze IA a sistemi embedded.

---

## 📋 Indice

1. [Introduzione ad Arduino](#1-introduzione-ad-arduino)
2. [Setup Ambiente di Sviluppo](#2-setup-ambiente-di-sviluppo)
3. [Primi Passi con IA](#3-primi-passi-con-ia)
4. [Progetti Arduino con IA](#4-progetti-arduino-con-ia)
5. [Best Practices Embedded](#5-best-practices-embedded)
6. [Risorse e Riferimenti](#6-risorse-e-riferimenti)

---

## 1. INTRODUZIONE AD ARDUINO

### 1.1 Cos'è Arduino?

**Arduino** è una piattaforma di prototipazione elettronica open-source basata su hardware e software facili da usare.

**Componenti principali:**
- **Microcontrollore** (es: ATmega328P su Arduino Uno)
- **Pin I/O digitali e analogici**
- **Interfaccia USB** per programmazione
- **Alimentazione** (USB o batteria)

**Modelli comuni:**

| Modello | MCU | Clock | RAM | Flash | I/O | Prezzo |
|---------|-----|-------|-----|-------|-----|--------|
| **Uno** | ATmega328P | 16MHz | 2KB | 32KB | 14D/6A | ~€20 |
| **Nano** | ATmega328P | 16MHz | 2KB | 32KB | 14D/8A | ~€5 |
| **Mega** | ATmega2560 | 16MHz | 8KB | 256KB | 54D/16A | ~€35 |
| **Due** | AT91SAM3X8E | 84MHz | 96KB | 512KB | 54D/12A | ~€35 |

**Nota RAM:** 2KB di RAM è MOLTO poco! Importanza gestione memoria.

### 1.2 Arduino vs C Standard

**Differenze chiave:**

```cpp
// Arduino (sketch)
void setup() {
    // Esegue UNA VOLTA all'avvio
    pinMode(13, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    // Esegue INFINITAMENTE
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
}
```

```c
// C standard
int main() {
    // Setup
    init_peripherals();

    // Loop infinito
    while(1) {
        do_something();
        delay_ms(1000);
    }

    return 0; // Mai raggiunto in embedded
}
```

**Linguaggio:** Arduino usa C++ (subset), ma molto codice è compatibile con C.

**Librerie standard NON disponibili:**
- ❌ `malloc()` / `free()` (sconsigliato su Arduino)
- ❌ `printf()` (usa `Serial.print()`)
- ❌ File I/O standard (serve SD library)
- ✅ Stringhe limitate (classe `String`, meglio `char[]`)

### 1.3 Quando Usare Arduino per Progetti ITS

**✅ Arduino è ottimo per:**
- Prototipazione rapida
- Progetti didattici
- Sensori e attuatori
- IoT semplice
- Imparare embedded programming

**❌ Arduino NON è ideale per:**
- Produzione industriale (meglio STM32, ESP32)
- Elaborazione pesante (poca RAM/CPU)
- Real-time critico (no RTOS)
- Progetti professionali complessi

**Per ITS:** Arduino è perfetto per **imparare** e **prototipare**.

---

## 2. SETUP AMBIENTE DI SVILUPPO

### 2.1 Arduino IDE (Opzione 1 - Più Semplice)

**Download:**
https://www.arduino.cc/en/software

**Installazione:**
1. Scarica installer per tuo OS
2. Installa (next, next, finish)
3. Collega Arduino via USB
4. Tools → Board → Seleziona tuo modello
5. Tools → Port → Seleziona porta COM/USB

**Test:**
```cpp
// File → Examples → 01.Basics → Blink
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Upload (Ctrl+U) → LED dovrebbe lampeggiare!

### 2.2 PlatformIO (Opzione 2 - Più Professionale)

**Vantaggi:**
- ✅ Integrato in VSCode
- ✅ Migliore autocomplete
- ✅ Supporto multi-board
- ✅ Gestione librerie avanzata
- ✅ Debugging (su board compatibili)

**Installazione:**
1. Installa VSCode
2. Extensions → Cerca "PlatformIO IDE"
3. Install
4. Restart VSCode

**Nuovo progetto:**
1. PlatformIO Home → New Project
2. Nome: "MyProject"
3. Board: "Arduino Uno"
4. Framework: "Arduino"
5. Create

**Struttura progetto:**
```
MyProject/
├── src/
│   └── main.cpp      ← Il tuo sketch
├── lib/              ← Librerie custom
├── include/          ← Header files
└── platformio.ini    ← Config
```

### 2.3 Simulatori (Senza Hardware)

**Tinkercad Circuits (Online, Gratuito)**

https://www.tinkercad.com/circuits

- ✅ Simula Arduino + componenti
- ✅ Visualizzazione real-time
- ✅ Nessuna installazione
- ✅ Perfetto per imparare

**Wokwi (Online, Gratuito)**

https://wokwi.com/

- ✅ Supporta ESP32, Arduino, Raspberry Pi Pico
- ✅ Debugging integrato
- ✅ Librerie custom

**Proteus (Software, A Pagamento)**

- ✅ Simulazione professionale
- ✅ PCB design
- ❌ Costoso (~€200+)

---

## 3. PRIMI PASSI CON IA

### 3.1 Usare IA per Arduino

**IA può aiutare con Arduino per:**

1. **Spiegare concetti embedded**
2. **Generare codice sketch**
3. **Debuggare problemi hardware/software**
4. **Suggerire librerie appropriate**
5. **Ottimizzare per memoria limitata**

**⚠️ Attenzione:** IA potrebbe suggerire codice che:
- Usa troppa RAM (overflow su Arduino Uno)
- Usa librerie inesistenti
- Non gestisce interrupt correttamente
- Ha timing issues

**SEMPRE testare su hardware reale o simulatore!**

### 3.2 Prompt Efficaci per Arduino

**Template base:**

```
Contesto: Sto programmando Arduino [modello] con [sensore/attuatore].

Task: [cosa vuoi fare]

Vincoli:
- RAM disponibile: [es: 2KB per Uno]
- Velocità richiesta: [es: lettura ogni 100ms]
- Librerie disponibili: [lista se sai]

Requisiti:
- Codice ottimizzato per memoria
- Gestione errori (se sensore disconnesso)
- Commenti chiari

Output: Sketch completo con setup() e loop()
```

**Esempio concreto:**

```
Contesto: Arduino Uno, sensore temperatura DHT22, LED RGB.

Task: Accendi LED verde se temperatura < 20°C, giallo se 20-30°C, rosso se > 30°C.

Vincoli:
- DHT22 legge max ogni 2 secondi
- Usa libreria DHT ufficiale
- Pin DHT: 2, Pin LED RGB: 9,10,11

Requisiti:
- Stampa temperatura su Serial Monitor
- Gestisci errore lettura DHT (timeout)
- Smooth LED transitions (PWM fade)

Output: Sketch completo testabile.
```

### 3.3 Validare Codice Arduino Generato da IA

**Checklist:**

**✅ Controllo Pin:**
- [ ] Pin usati sono disponibili su tuo board
- [ ] Pin analogici solo per analogRead (A0-A5 su Uno)
- [ ] Pin PWM solo se necessari (~)

**✅ Controllo Memoria:**
```cpp
// Aggiungi per debug RAM
void printFreeRAM() {
    extern int __heap_start, *__brkval;
    int v;
    Serial.print("Free RAM: ");
    Serial.println((int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval));
}
```

**✅ Controllo Librerie:**
- [ ] Librerie esistono (controlla Library Manager)
- [ ] Versioni compatibili

**✅ Controllo Timing:**
- [ ] `delay()` non blocca troppo a lungo
- [ ] Interrupt service routines sono veloci
- [ ] Millis() overflow gestito (dopo 49 giorni)

**✅ Controllo Voltage:**
- [ ] Sensori 3.3V o 5V compatibili con board
- [ ] Assorbimento corrente OK (max 40mA per pin)

---

## 4. PROGETTI ARDUINO CON IA

### 4.1 Progetto 1: Termostato Intelligente

**Obiettivo:** Sistema che controlla temperatura ambiente e attiva riscaldamento/raffrescamento.

**Hardware necessario:**
- Arduino Uno
- Sensore temperatura DHT22 o DS18B20
- 2 LED (rosso = caldo, blu = freddo)
- 2 resistenze 220Ω

**Prompt per IA:**

```
Progetto: Termostato Arduino con isteresi

Hardware:
- Arduino Uno
- DHT22 su pin 2
- LED rosso (riscaldamento) su pin 8
- LED blu (raffrescamento) su pin 9

Logica:
- Target temperatura: 22°C
- Isteresi: ±1°C
- Se temp < 21°C → accendi LED rosso (simula riscaldamento)
- Se temp > 23°C → accendi LED blu (simula AC)
- Altrimenti → entrambi spenti

Funzionalità:
- Leggi temperatura ogni 2 secondi
- Stampa su Serial: "Temp: 23.5C [HEATING/COOLING/OK]"
- Implementa isteresi (evita on/off rapido)

Gestione errori:
- Se DHT22 fallisce lettura → stampa "Sensor error"

Output: Sketch completo con commenti.
```

**Codice atteso:**

```cpp
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22
#define LED_HEAT 8
#define LED_COOL 9

DHT dht(DHTPIN, DHTTYPE);

const float TARGET_TEMP = 22.0;
const float HYSTERESIS = 1.0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_HEAT, OUTPUT);
  pinMode(LED_COOL, OUTPUT);
  dht.begin();

  Serial.println("Thermostat initialized");
}

void loop() {
  delay(2000); // DHT22 richiede min 2sec tra letture

  float temp = dht.readTemperature();

  // Gestione errore
  if (isnan(temp)) {
    Serial.println("Sensor error!");
    return;
  }

  // Logica termostato con isteresi
  if (temp < TARGET_TEMP - HYSTERESIS) {
    // Troppo freddo → riscalda
    digitalWrite(LED_HEAT, HIGH);
    digitalWrite(LED_COOL, LOW);
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.println("C [HEATING]");
  }
  else if (temp > TARGET_TEMP + HYSTERESIS) {
    // Troppo caldo → raffredda
    digitalWrite(LED_HEAT, LOW);
    digitalWrite(LED_COOL, HIGH);
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.println("C [COOLING]");
  }
  else {
    // OK
    digitalWrite(LED_HEAT, LOW);
    digitalWrite(LED_COOL, LOW);
    Serial.print("Temp: ");
    Serial.print(temp);
    Serial.println("C [OK]");
  }
}
```

**Test:**
1. Upload sketch
2. Apri Serial Monitor (9600 baud)
3. Osserva letture temperatura
4. Scalda sensore con dita → LED rosso si accende
5. Soffia aria fredda → LED blu si accende

### 4.2 Progetto 2: Data Logger su SD

**Obiettivo:** Registrare dati sensori su SD card con timestamp.

**Hardware:**
- Arduino Uno/Mega
- Modulo SD card (SPI)
- Sensore temperatura
- RTC module (opzionale, per timestamp reali)

**Prompt IA:**

```
Progetto: Data logger temperatura su SD card

Hardware:
- Arduino Uno
- SD card module (CS pin 10)
- DHT22 su pin 2

Funzionalità:
- Leggi temperatura ogni 10 secondi
- Salva su file "datalog.txt" formato CSV
- CSV: timestamp,temperatura
- Timestamp in millisecondi (millis())
- LED integrato lampeggia ad ogni scrittura

Gestione errori:
- Se SD non inizializza → blocca e stampa errore
- Se scrittura fallisce → stampa warning

Output: Sketch con librerie SD.h e DHT.h
```

**Codice atteso:**

```cpp
#include <SPI.h>
#include <SD.h>
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22
#define CS_PIN 10

DHT dht(DHTPIN, DHTTYPE);
File dataFile;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  // Init DHT
  dht.begin();

  // Init SD
  Serial.print("Initializing SD card...");
  if (!SD.begin(CS_PIN)) {
    Serial.println("FAILED!");
    while(1); // Blocca
  }
  Serial.println("OK");

  // Crea header se file non esiste
  if (!SD.exists("datalog.txt")) {
    dataFile = SD.open("datalog.txt", FILE_WRITE);
    if (dataFile) {
      dataFile.println("timestamp_ms,temperature_C");
      dataFile.close();
      Serial.println("Created datalog.txt");
    }
  }
}

void loop() {
  // Leggi temperatura
  float temp = dht.readTemperature();

  if (isnan(temp)) {
    Serial.println("DHT read error");
  } else {
    // Salva su SD
    dataFile = SD.open("datalog.txt", FILE_WRITE);

    if (dataFile) {
      unsigned long timestamp = millis();

      dataFile.print(timestamp);
      dataFile.print(",");
      dataFile.println(temp);
      dataFile.close();

      // Feedback
      digitalWrite(LED_BUILTIN, HIGH);
      delay(50);
      digitalWrite(LED_BUILTIN, LOW);

      Serial.print("Logged: ");
      Serial.print(timestamp);
      Serial.print("ms, ");
      Serial.print(temp);
      Serial.println("C");
    } else {
      Serial.println("SD write error");
    }
  }

  delay(10000); // 10 secondi
}
```

**Test:**
1. Inserisci SD formattata FAT32
2. Upload sketch
3. Lascia girare 1 minuto
4. Rimuovi SD, leggi con PC
5. Apri datalog.txt → dovrebbe contenere 6 righe dati

### 4.3 Progetto 3: Controllo Remoto Seriale

**Obiettivo:** Controllare Arduino da PC via comandi seriali.

**Comandi:**
- `LED ON` → accendi LED
- `LED OFF` → spegni LED
- `STATUS` → leggi sensori
- `HELP` → mostra comandi

**Prompt IA:**

```
Progetto: Interfaccia seriale comandi per Arduino

Features:
- Ricevi comandi via Serial (9600 baud)
- Comandi supportati:
  - "LED ON" → digitalWrite(13, HIGH)
  - "LED OFF" → digitalWrite(13, LOW)
  - "STATUS" → stampa temperatura DHT22
  - "HELP" → lista comandi
- Comando non valido → "Unknown command"

Implementazione:
- Usa Serial.readStringUntil('\n')
- Trim whitespace
- Case insensitive
- Prompt ">" per indicare pronto

Codice pulito con funzioni separate per ogni comando.
```

**Codice atteso:**

```cpp
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22
#define LED_PIN 13

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  dht.begin();

  Serial.println("=== Arduino Command Interface ===");
  Serial.println("Type HELP for commands");
  Serial.print("> ");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    command.toUpperCase();

    processCommand(command);

    Serial.print("> ");
  }
}

void processCommand(String cmd) {
  if (cmd == "LED ON") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED turned ON");
  }
  else if (cmd == "LED OFF") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED turned OFF");
  }
  else if (cmd == "STATUS") {
    float temp = dht.readTemperature();
    if (isnan(temp)) {
      Serial.println("Sensor error");
    } else {
      Serial.print("Temperature: ");
      Serial.print(temp);
      Serial.println(" C");
    }
  }
  else if (cmd == "HELP") {
    Serial.println("Available commands:");
    Serial.println("  LED ON    - Turn LED on");
    Serial.println("  LED OFF   - Turn LED off");
    Serial.println("  STATUS    - Read sensors");
    Serial.println("  HELP      - Show this message");
  }
  else {
    Serial.print("Unknown command: ");
    Serial.println(cmd);
  }
}
```

**Test:**
1. Upload
2. Serial Monitor (9600 baud)
3. Scrivi: `LED ON` → Enter
4. LED si accende
5. Scrivi: `STATUS` → Mostra temperatura
6. Scrivi: `HELP` → Lista comandi

### 4.4 Progetto 4: Sistema Allarme PIR

**Hardware:**
- Arduino
- Sensore PIR (motion detection)
- Buzzer
- LED

**Logica:**
- Se PIR rileva movimento → allarme (buzzer + LED)
- Bottone per armare/disarmare
- Stati: ARMED, DISARMED, ALARM

**Prompt IA:**

```
Progetto: Sistema allarme con PIR

Hardware:
- PIR su pin 2
- Buzzer su pin 8
- LED rosso su pin 9
- Pulsante su pin 3 (pull-up interno)

Stati:
- DISARMED: tutto spento
- ARMED: LED lampeggia lento
- ALARM: buzzer + LED lampeggio veloce

Logica:
- Pulsante toggle ARMED/DISARMED
- In ARMED: se PIR rileva movimento → ALARM
- In ALARM: buzzer per 5 secondi, poi torna ARMED
- Debounce pulsante

Serial output:
- "System ARMED"
- "System DISARMED"
- "ALARM! Motion detected"

Implementa con enum per stati e millis() per timing non-bloccante.
```

---

## 5. BEST PRACTICES EMBEDDED

### 5.1 Gestione Memoria su Arduino

**Problema:** Arduino Uno ha solo 2KB RAM!

**Evitare:**

```cpp
// ❌ MALE - consuma troppa RAM
String message = "Hello World"; // String class usa heap
char bigBuffer[1000]; // 1KB = 50% della RAM!
float matrix[50][50]; // 10KB - overflow!
```

**Preferire:**

```cpp
// ✅ BENE
const char message[] PROGMEM = "Hello"; // In flash, non RAM
char buffer[50]; // Solo quello che serve
// Usa int invece di float se possibile (più veloce, meno RAM)
```

**Misurare RAM:**

```cpp
int freeRam() {
  extern int __heap_start, *__brkval;
  int v;
  return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval);
}

void setup() {
  Serial.begin(9600);
  Serial.print("Free RAM: ");
  Serial.println(freeRam());
}
```

### 5.2 Timing Non-Bloccante

**❌ MALE - delay() blocca tutto:**

```cpp
void loop() {
  digitalWrite(LED, HIGH);
  delay(1000); // ← BLOCCATO per 1 secondo!
  digitalWrite(LED, LOW);
  delay(1000);

  // Non può fare altro mentre aspetta!
}
```

**✅ BENE - millis() non-bloccante:**

```cpp
unsigned long previousMillis = 0;
const long interval = 1000;

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Toggle LED
    digitalWrite(LED, !digitalRead(LED));
  }

  // Può fare altro qui senza bloccare!
  checkSensor();
  processSerial();
}
```

### 5.3 Interrupt vs Polling

**Polling (controllo continuo):**

```cpp
void loop() {
  if (digitalRead(BUTTON) == LOW) {
    handleButton();
  }
  // Potrebbe perdere press brevi!
}
```

**Interrupt (hardware trigger):**

```cpp
volatile bool buttonPressed = false;

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(BUTTON), buttonISR, FALLING);
}

void buttonISR() {
  // Interrupt Service Routine - BREVE!
  buttonPressed = true;
}

void loop() {
  if (buttonPressed) {
    buttonPressed = false;
    handleButton(); // Elaborazione lunga fuori da ISR
  }
}
```

**Regole ISR:**
- ⚡ Più breve possibile
- ❌ NO Serial.print()
- ❌ NO delay()
- ❌ NO operazioni lunghe
- ✅ Solo setta flag

### 5.4 Debouncing

**Problema:** Pulsanti "rimbalzano" (multiple trigger in ms)

**Software debounce:**

```cpp
const int DEBOUNCE_DELAY = 50; // ms
int buttonState;
int lastButtonState = HIGH;
unsigned long lastDebounceTime = 0;

void loop() {
  int reading = digitalRead(BUTTON);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == LOW) {
        // Pulsante premuto (stabile)
        handleButtonPress();
      }
    }
  }

  lastButtonState = reading;
}
```

### 5.5 Power Management

**Per progetti a batteria:**

```cpp
#include <avr/sleep.h>
#include <avr/power.h>

void setup() {
  // Disabilita periferiche inutilizzate
  power_adc_disable(); // ADC
  power_spi_disable(); // SPI
  power_timer1_disable(); // Timer1
}

void goToSleep() {
  set_sleep_mode(SLEEP_MODE_PWR_DOWN);
  sleep_enable();
  sleep_mode(); // Sleep!

  // ... sveglia da interrupt ...

  sleep_disable();
}
```

---

## 6. RISORSE E RIFERIMENTI

### 6.1 Documentazione Ufficiale

**Arduino:**
- https://www.arduino.cc/reference/en/
- https://docs.arduino.cc/

**Librerie popolari:**
- DHT: https://github.com/adafruit/DHT-sensor-library
- SD: https://www.arduino.cc/en/Reference/SD
- Servo: https://www.arduino.cc/en/Reference/Servo
- LiquidCrystal: https://www.arduino.cc/en/Reference/LiquidCrystal

### 6.2 Tutorial e Guide

**Arduino Project Hub:**
https://create.arduino.cc/projecthub

**Adafruit Learn:**
https://learn.adafruit.com/

**SparkFun Tutorials:**
https://learn.sparkfun.com/

**DroneBot Workshop (YouTube):**
https://www.youtube.com/@Dronebotworkshop

### 6.3 Community

**Forum Arduino:**
https://forum.arduino.cc/

**Reddit:**
- r/arduino
- r/embedded
- r/AskElectronics

**Discord:**
Arduino Official Discord

### 6.4 Componenti e Kit

**Dove comprare (Italia):**
- **Robot-Italy** - https://www.robot-italy.com/
- **Futura Elettronica** - https://www.futurashop.it/
- **RS Components** - https://it.rs-online.com/
- **Amazon** - Kit starter economici

**Kit consigliati per iniziare:**
- **Elegoo Uno Starter Kit** (~€35) - completo
- **Arduino Official Starter Kit** (~€85) - premium
- **Component Kit** (~€20) - solo componenti

### 6.5 Progetti Avanzati

**Dopo aver imparato le basi:**

1. **IoT con ESP32/ESP8266**
   - WiFi integrato
   - MQTT per comunicazione
   - Web server

2. **Computer Vision con OpenMV**
   - Camera integrata
   - MicroPython
   - ML on-device

3. **RTOS con STM32**
   - Real-time OS
   - Multi-tasking
   - Professionale

4. **TinyML**
   - Machine learning su MCU
   - TensorFlow Lite Micro
   - Edge AI

---

## 🎯 CONCLUSIONE APPENDICE

### Ricapitolando

Questa appendice ha coperto:
- ✅ Introduzione ad Arduino
- ✅ Setup ambiente sviluppo
- ✅ Usare IA per progetti embedded
- ✅ 4 progetti pratici completi
- ✅ Best practices (memoria, timing, interrupt)
- ✅ Risorse per approfondire

### Prossimi Passi

**Se hai hardware Arduino:**

1. **Inizia con Blink** (LED integrato)
2. **Aggiungi sensore** (DHT22 o ultrasonico)
3. **Implementa un progetto** da questa appendice
4. **Usa IA per customizzare** secondo tue esigenze
5. **Condividi su GitHub** (portfolio!)

**Se NON hai hardware:**

1. **Usa simulatore** (Tinkercad/Wokwi)
2. **Impara concetti** (timing, interrupt, memory)
3. **Considera ESP32** (~€5, WiFi integrato, più potente)

### Link Veloce

**Inizia subito (senza hardware):**
https://www.tinkercad.com/circuits

**Compra kit starter:**
https://store.arduino.cc/products/arduino-starter-kit-multi-language

### Feedback

Questa appendice ti è stata utile? Hai suggerimenti?
[Link form feedback]

---

**🔧 Buon making con Arduino e IA! 🤖**

---

**Appendice Arduino - Corso ITS Intelligenza Artificiale 2025**