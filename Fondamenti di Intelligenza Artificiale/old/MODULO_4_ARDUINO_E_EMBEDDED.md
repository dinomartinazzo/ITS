# 📘 MODULO 4
# Arduino e Sistemi Embedded con IA
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita 2025
### Durata: 6 ore | Livello: Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione a Arduino e Sistemi Embedded](#1-introduzione-a-arduino-e-sistemi-embedded)
2. [Setup Ambiente di Sviluppo](#2-setup-ambiente-di-sviluppo)
3. [Fondamenti Hardware Arduino](#3-fondamenti-hardware-arduino)
4. [Gestione Pin e I/O Digitale](#4-gestione-pin-e-io-digitale)
5. [Input Analogico e PWM](#5-input-analogico-e-pwm)
6. [Timing: millis() vs delay()](#6-timing-millis-vs-delay)
7. [Comunicazione Seriale](#7-comunicazione-seriale)
8. [Sensori e Attuatori](#8-sensori-e-attuatori)
9. [Display e Interfacce Utente](#9-display-e-interfacce-utente)
10. [Interrupt e Gestione Eventi](#10-interrupt-e-gestione-eventi)
11. [Comunicazioni I2C e SPI](#11-comunicazioni-i2c-e-spi)
12. [ESP32: WiFi e Bluetooth](#12-esp32-wifi-e-bluetooth)
13. [Librerie Arduino](#13-librerie-arduino)
14. [Progetti IoT Completi](#14-progetti-iot-completi)
15. [Debugging Hardware e Software](#15-debugging-hardware-e-software)
16. [Best Practices Embedded](#16-best-practices-embedded)
17. [TinyML: Machine Learning su Arduino](#17-tinyml-machine-learning-su-arduino)
18. [Esercizi Pratici](#18-esercizi-pratici)

---

## 1. Introduzione a Arduino e Sistemi Embedded

### 1.1 Cos'è Arduino

**Arduino** è una piattaforma open-source per prototipazione elettronica rapida, creata nel 2005 in Italia.

**Caratteristiche Chiave:**
- ✅ **Hardware open-source** - Schemi pubblici, cloni permessi
- ✅ **Software gratuito** - IDE multipiattaforma
- ✅ **Semplicità** - API intuitive nascondono complessità
- ✅ **Community enorme** - Milioni di progetti, tutorial, librerie
- ✅ **Ecosistema ricco** - Migliaia di shield e moduli compatibili

**Perché Arduino per ITS 2025:**
- Skill richiesto nell'industria IoT/Industria 4.0
- Prototipazione rapida (ore invece di settimane)
- Base perfetta per comprendere sistemi embedded
- Transizione facile verso STM32, ESP32 professionali

### 1.2 Modelli Arduino Principali

**Arduino Uno (Entry Level)**
```
Microcontrollore: ATmega328P (8-bit AVR)
Clock: 16 MHz
Flash: 32 KB (programma)
SRAM: 2 KB (variabili runtime)
EEPROM: 1 KB (storage permanente)
Pin Digitali: 14 (6 con PWM)
Pin Analogici: 6 (ADC 10-bit, 0-1023)
Alimentazione: 5V
USB: USB-B (seriale)
Prezzo: ~€20-25

Ideale per: Progetti didattici, prototipazione base
```

**Arduino Mega 2560 (Più Potente)**
```
Microcontrollore: ATmega2560 (8-bit AVR)
Clock: 16 MHz
Flash: 256 KB
SRAM: 8 KB
EEPROM: 4 KB
Pin Digitali: 54 (15 PWM)
Pin Analogici: 16
Alimentazione: 5V

Ideale per: Progetti complessi, molti sensori/attuatori
```

**Arduino Nano (Compatto)**
```
Microcontrollore: ATmega328P
Identico a Uno ma formato breadboard-friendly
Mini USB invece di USB-B
Prezzo: ~€15-20

Ideale per: Progetti finali compatti, wearables
```

**ESP32 (Moderno, WiFi/BT)**
```
Microcontrollore: Dual-core Xtensa 32-bit
Clock: 240 MHz (15x più veloce di Uno!)
Flash: 4 MB
SRAM: 520 KB
WiFi: 802.11 b/g/n
Bluetooth: 4.2 + BLE
GPIO: 34 pin
ADC: 12-bit (0-4095)
Alimentazione: 3.3V
Prezzo: ~€5-10

Ideale per: IoT, progetti connessi, AI on edge
```

### 1.3 Sistemi Embedded vs PC

**Differenze Fondamentali:**

| Aspetto | PC | Arduino/Embedded |
|---------|-----|------------------|
| RAM | 8-32 GB | 2-520 KB (migliaia di volte meno!) |
| Storage | 256 GB - 2 TB SSD | 32 KB - 4 MB Flash |
| OS | Windows/Linux/Mac | Bare metal (no OS) |
| Multitasking | Sì (migliaia processi) | No (un loop) |
| Boot time | 10-60 secondi | < 1 secondo |
| Consumo | 50-200W | 0.05-2W |
| Affidabilità | Crash, aggiornamenti | Esecuzione continua 24/7 |
| Costo | €500-2000 | €5-30 |

**Implicazioni per Programmazione:**
```cpp
// ❌ Su PC puoi fare:
int huge_array[1000000];  // 4 MB
String text = "Hello " + world;  // Allocazioni dinamiche

// ✅ Su Arduino (2 KB RAM!) devi:
int small_array[100];     // 400 byte
char text[50];
snprintf(text, sizeof(text), "Hello %s", world);
```

### 1.4 Arduino vs C/C++ Puro AVR

**Arduino nasconde complessità:**

```cpp
// ===============================
// ARDUINO (SEMPLICE)
// ===============================
void setup() {
    pinMode(13, OUTPUT);  // Pin 13 come output
}

void loop() {
    digitalWrite(13, HIGH);  // LED acceso
    delay(1000);
    digitalWrite(13, LOW);   // LED spento
    delay(1000);
}

// ===============================
// C PURO AVR (COMPLESSO)
// ===============================
#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    // Pin 13 = PB5 su ATmega328P
    DDRB |= (1 << DDB5);  // Imposta PB5 come output (bit manipulation)

    while(1) {
        PORTB |= (1 << PORTB5);   // Scrivi HIGH su PB5
        _delay_ms(1000);
        PORTB &= ~(1 << PORTB5);  // Scrivi LOW su PB5
        _delay_ms(1000);
    }

    return 0;  // Mai raggiunto
}
```

**Arduino:**
- Pro: Codice leggibile, portabile, veloce da scrivere
- Contro: Overhead minimo (~1-2% performance)

**C Puro:**
- Pro: Controllo totale, massima efficienza
- Contro: Codice complesso, specifico per MCU, lento da scrivere

**Per questo corso: Arduino!**
- Produttività >> Ottimizzazione prematura
- Imparato Arduino, C puro AVR diventa facile

### 1.5 Applicazioni Reali Sistemi Embedded

**Industria 4.0:**
- Monitoraggio macchine CNC
- Sensori temperatura/vibrazione linee produzione
- Controllo robot collaborativi
- Manutenzione predittiva

**IoT (Internet of Things):**
- Smart home (termostati, luci, sicurezza)
- Agricoltura di precisione (irrigazione, clima serre)
- Wearables (fitness tracker, smartwatch)
- Smart cities (parcheggi, illuminazione, qualità aria)

**Automotive:**
- Centraline motore (ECU)
- ABS, airbag, cruise control
- Sensori parcheggio, telecamere

**Medicale:**
- Monitor vitali pazienti
- Pompe insulina
- Ventilatori polmonari

---

## 2. Setup Ambiente di Sviluppo

### 2.1 Arduino IDE (Raccomandato per Principianti)

**Download e Installazione:**
```
1. Vai a: https://www.arduino.cc/en/software
2. Scarica per il tuo OS (Windows/Mac/Linux)
3. Installa (non serve configurazione)
4. Apri IDE

Versione raccomandata: Arduino IDE 2.x (nuova, più veloce)
```

**Prima Configurazione:**
```
1. Strumenti → Scheda → Arduino Uno (o tua scheda)
2. Strumenti → Porta → COMx (Windows) o /dev/ttyUSBx (Linux)
3. File → Esempi → 01.Basics → Blink
4. Click "Carica" (freccia →)

LED sulla scheda lampeggia → SUCCESS!
```

### 2.2 PlatformIO (Raccomandato per Progetti Grandi)

**Setup in VSCode:**
```
1. Installa VSCode: https://code.visualstudio.com/
2. Estensioni → Cerca "PlatformIO IDE"
3. Installa (richiede 5-10 min prima volta)
4. PlatformIO → New Project
   Nome: MyProject
   Board: Arduino Uno
   Framework: Arduino

5. Struttura creata:
   src/main.cpp         // Codice principale
   platformio.ini       // Configurazione progetto
```

**Vantaggi PlatformIO:**
- ✅ IntelliSense (autocomplete intelligente)
- ✅ Gestione librerie migliore
- ✅ Unit testing integrato
- ✅ Debug avanzato
- ✅ Multi-board support
- ✅ Versioning librerie

**Svantaggi:**
- Curva apprendimento più ripida
- Setup iniziale più lento
- Richiede più spazio disco

**Raccomandazione:**
- Principianti → Arduino IDE
- Progetti seri → PlatformIO

### 2.3 Driver e Troubleshooting

**Problema Comune: Porta Non Riconosciuta**

**Windows:**
```
1. Gestione Dispositivi → Porte COM
2. Se "Dispositivo sconosciuto":
   - Arduino Uno/Nano originale: Driver automatico
   - Clone CH340: Download driver CH340

Download CH340: http://www.wch.cn/downloads/CH341SER_EXE.html
```

**Linux:**
```bash
# Aggiungi user al gruppo dialout
sudo usermod -a -G dialout $USER

# Logout/login per applicare

# Verifica porta
ls /dev/ttyUSB*
ls /dev/ttyACM*
```

**macOS:**
```bash
# Installa driver CH340 se clone
# Verifica porta
ls /dev/cu.*

# Se problemi permessi
sudo chmod 666 /dev/cu.usbserial-*
```

### 2.4 Primo Sketch con IA

**Prompt per IA:**
```
Scrivi sketch Arduino Uno che:

HARDWARE:
- LED integrato (pin 13)

FUNZIONALITÀ:
- LED lampeggia: 500ms ON, 500ms OFF
- Invia "LED ON" e "LED OFF" su seriale ad ogni cambio
- Commenti esplicativi

REQUISITI:
- Standard Arduino (no librerie esterne)
- Codice pulito e leggibile
```

**Output IA (Validato):**
```cpp
/**
 * @file blink_serial.ino
 * @brief LED lampeggiante con debug seriale
 * @author Corso ITS 2025
 */

// Costante per pin LED (pin 13 = LED integrato)
const int LED_PIN = 13;

// Costante intervallo lampeggio (millisecondi)
const int BLINK_INTERVAL = 500;

/**
 * @brief Setup: eseguita una sola volta all'avvio
 */
void setup() {
    // Inizializza comunicazione seriale a 9600 baud
    Serial.begin(9600);

    // Configura pin LED come OUTPUT
    pinMode(LED_PIN, OUTPUT);

    // Messaggio iniziale
    Serial.println("=== Sistema Avviato ===");
    Serial.println("LED Blink con Seriale");
}

/**
 * @brief Loop: eseguita continuamente
 */
void loop() {
    // Accendi LED
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED ON");
    delay(BLINK_INTERVAL);

    // Spegni LED
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED OFF");
    delay(BLINK_INTERVAL);
}
```

**Test:**
```
1. Carica sketch su Arduino
2. Apri Serial Monitor (Strumenti → Serial Monitor)
3. Imposta baud rate: 9600
4. Verifica output:
   === Sistema Avviato ===
   LED Blink con Seriale
   LED ON
   LED OFF
   LED ON
   ...
```

---

## 3. Fondamenti Hardware Arduino

### 3.1 Anatomia Scheda Arduino Uno

```
                    USB-B Connector
                          |
        +-----------------------------------+
        |  [RESET]                  [POWER] |
        |                                   |
   [PWR]|  13 12 11 10  9  8         GND   |[ANALOG IN]
        |  ○  ○  ○  ○  ○  ○          ○  ○  |  A0 A1 A2
   [DIG]|                                   |  A3 A4 A5
        |   7  6  5  4  3  2  1  0   5V ○  |
        |   ○  ○  ○  ○  ○  ○  ○  ○      ○  |
        +-----------------------------------+
              ATmega328P
              (sotto)

LEGENDA:
[PWR]  = Power (Vin, GND, 5V, 3.3V)
[DIG]  = Digital Pin (0-13)
        Pin ~ (3,5,6,9,10,11) = PWM capable
[ANALOG IN] = Analog Input (A0-A5)
```

### 3.2 Alimentazione

**Opzioni Alimentazione:**

1. **USB (5V)** - Durante programmazione/debug
   - Corrente max: ~500 mA
   - Sufficiente per: Arduino + pochi LED/sensori

2. **Jack DC (7-12V)** - Alimentazione esterna
   - Voltage regulator interno → 5V
   - Corrente: Dipende da alimentatore
   - Ideale: 9V 1A

3. **Pin Vin (7-12V)** - Alimentazione header
   - Equivalente a Jack DC
   - Utile per progetti custom

**Limiti Corrente Critici:**
```
Pin singolo:        Max 40 mA
Tutti pin insieme:  Max 200 mA
Regolatore 5V:      Max 1 A (con dissipatore)
Pin 3.3V:           Max 50 mA (ATTENZIONE!)
```

**Esempio Calcolo:**
```
LED standard: ~20 mA ciascuno
Voglio 5 LED:
  5 × 20 mA = 100 mA ✅ OK (< 200 mA)

Voglio 15 LED:
  15 × 20 mA = 300 mA ❌ TROPPO!
  Soluzione: Usa driver esterno (ULN2003, transistor)
```

### 3.3 Pin Digitali

**Configurazione:**
```cpp
pinMode(pin, MODE);

// MODE:
OUTPUT       // Pilota LED, relay, ecc.
INPUT        // Legge pulsante, sensore digitale
INPUT_PULLUP // Input con resistenza pull-up interna (~20kΩ)
```

**Lettura/Scrittura:**
```cpp
// OUTPUT
digitalWrite(pin, HIGH);  // 5V
digitalWrite(pin, LOW);   // 0V

// INPUT
int state = digitalRead(pin);  // HIGH (1) o LOW (0)
```

**Livelli Logici:**
```
HIGH (1) = Tensione > 3V   (tipicamente 5V)
LOW  (0) = Tensione < 1.5V (tipicamente 0V)

Zona indefinita (1.5V - 3V) → EVITARE!
```

### 3.4 Pin Analogici

**ADC (Analog to Digital Converter):**
```
Arduino Uno: 10-bit
Risoluzione: 2^10 = 1024 livelli (0-1023)
Range: 0V - 5V

Formula conversione:
Valore_digitale = (Tensione_analogica / 5.0) × 1023

Esempio:
2.5V → (2.5 / 5.0) × 1023 = 511.5 ≈ 512
```

**Lettura:**
```cpp
int value = analogRead(A0);  // Valore 0-1023

// Conversione a volt
float voltage = value * (5.0 / 1023.0);

// Conversione a percentuale
float percent = (value / 1023.0) * 100.0;
```

**Nota:** Pin analogici possono essere usati come digitali!
```cpp
pinMode(A0, OUTPUT);
digitalWrite(A0, HIGH);  // A0 usato come pin digitale
```

### 3.5 PWM (Pulse Width Modulation)

**Pin PWM su Uno:** 3, 5, 6, 9, 10, 11 (marcati con ~)

**Duty Cycle:**
```
0% (sempre OFF)   ███████████  GND
25%               ██░░░░░░░░░  ~1.25V (media)
50%               ████░░░░░░░  ~2.5V
75%               ██████░░░░░  ~3.75V
100% (sempre ON)  ██████████   5V

█ = HIGH
░ = LOW
```

**Uso:**
```cpp
analogWrite(pin, value);  // value: 0-255

analogWrite(9, 0);     // 0% duty = OFF
analogWrite(9, 64);    // 25% duty
analogWrite(9, 128);   // 50% duty
analogWrite(9, 192);   // 75% duty
analogWrite(9, 255);   // 100% duty = ON
```

**Applicazioni:**
- Controllo luminosità LED
- Controllo velocità motore DC
- Generazione toni audio (tone())
- Simulazione segnale analogico

**Frequenza PWM:**
```
Pin 5, 6:      ~980 Hz
Pin 3,9,10,11: ~490 Hz

Modificabile ma avanzato (timer hardware)
```

---

## 4. Gestione Pin e I/O Digitale

### 4.1 LED Base

**Circuito:**
```
Arduino Pin 13 ──────┬───[220Ω]───(LED)───── GND
                     │
                  [Arduino]
```

**Calcolo Resistenza LED:**
```
LED tipico:
  Tensione diretta (Vf): ~2V
  Corrente desiderata (If): 20 mA

Resistenza = (Vsource - Vf) / If
           = (5V - 2V) / 0.020 A
           = 3V / 0.020 A
           = 150Ω

Valore commerciale più vicino: 220Ω (riduce corrente a ~14mA, OK)
```

**Codice:**
```cpp
const int LED_PIN = 13;

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_PIN, HIGH);  // LED acceso
    delay(1000);
    digitalWrite(LED_PIN, LOW);   // LED spento
    delay(1000);
}
```

### 4.2 Pulsante (Button)

**Circuito con Pull-up Esterno:**
```
                    +5V
                     |
                   [10kΩ]  ← Pull-up resistor
                     |
Arduino Pin 2 ───────┼──── Pulsante ──── GND
```

**Circuito con Pull-up Interno (RACCOMANDATO):**
```
Arduino Pin 2 ──── Pulsante ──── GND

(Pull-up 20kΩ interno attivato via software)
```

**Codice:**
```cpp
const int BUTTON_PIN = 2;
const int LED_PIN = 13;

void setup() {
    pinMode(BUTTON_PIN, INPUT_PULLUP);  // Pull-up interno
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    int buttonState = digitalRead(BUTTON_PIN);

    // NOTA: INPUT_PULLUP → LOW quando premuto!
    if (buttonState == LOW) {
        digitalWrite(LED_PIN, HIGH);  // Pulsante premuto
    } else {
        digitalWrite(LED_PIN, LOW);   // Pulsante rilasciato
    }
}
```

**Perché INPUT_PULLUP è LOW quando premuto?**
```
Pulsante RILASCIATO:
Pin ─── [20kΩ] ─── +5V    → Legge HIGH

Pulsante PREMUTO:
Pin ─── [20kΩ] ─── +5V
  └──── Pulsante ─── GND   → GND vince (più forte) → Legge LOW
```

### 4.3 Debouncing

**Problema: Rimbalzi Meccanici**
```
Pulsante fisico non cambia stato istantaneamente!

Pressione reale:
  _____________
 |             |___________
        ↑
    1 pressione

Segnale elettrico (con rimbalzi):
  __  _  __  ___
 |  ||_|| _||   |_________
      ↑
  Letto come 4-5 pressioni!

Durata rimbalzi: 5-50 ms
```

**Soluzione 1: Debouncing Software Base**
```cpp
const int BUTTON_PIN = 2;
const int DEBOUNCE_DELAY = 50;  // 50 ms

int lastButtonState = HIGH;
int buttonState = HIGH;
unsigned long lastDebounceTime = 0;

void loop() {
    int reading = digitalRead(BUTTON_PIN);

    // Se stato cambiato, resetta timer
    if (reading != lastButtonState) {
        lastDebounceTime = millis();
    }

    // Se passato tempo debounce, accetta nuovo stato
    if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
        if (reading != buttonState) {
            buttonState = reading;

            // EDGE DETECTION: rileva transizione HIGH→LOW
            if (buttonState == LOW) {
                Serial.println("Pulsante premuto!");
                // Azione su pressione
            }
        }
    }

    lastButtonState = reading;
}
```

**Soluzione 2: Libreria Bounce2 (RACCOMANDATO)**
```cpp
#include <Bounce2.h>

const int BUTTON_PIN = 2;

Bounce button = Bounce();

void setup() {
    Serial.begin(9600);

    button.attach(BUTTON_PIN, INPUT_PULLUP);
    button.interval(50);  // 50 ms debounce
}

void loop() {
    button.update();

    if (button.fell()) {  // Transizione HIGH → LOW
        Serial.println("Pulsante premuto!");
    }

    if (button.rose()) {  // Transizione LOW → HIGH
        Serial.println("Pulsante rilasciato!");
    }
}
```

**Installazione Bounce2:**
```
Arduino IDE → Tools → Manage Libraries
Cerca: "Bounce2"
Installa
```

### 4.4 Toggle LED con Pulsante

```cpp
#include <Bounce2.h>

const int BUTTON_PIN = 2;
const int LED_PIN = 13;

Bounce button = Bounce();
bool ledState = false;

void setup() {
    pinMode(LED_PIN, OUTPUT);
    button.attach(BUTTON_PIN, INPUT_PULLUP);
    button.interval(50);
}

void loop() {
    button.update();

    if (button.fell()) {
        // Toggle stato
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }
}
```

### 4.5 Prompt IA per Pulsante

```
Scrivi sketch Arduino con debouncing pulsante professionale:

HARDWARE:
- Pulsante su pin 2 (INPUT_PULLUP)
- LED su pin 13

FUNZIONALITÀ:
- Click pulsante → toggle LED
- Doppio click (< 300ms tra click) → lampeggio veloce 5 volte
- Pressione lunga (> 2 sec) → LED always ON fino a nuovo click

REQUISITI:
- Debouncing 50ms
- Logica non-bloccante
- Usa millis()
- Commenti esplicativi
```

---

## 5. Input Analogico e PWM

### 5.1 Potenziometro

**Circuito:**
```
        +5V
         |
      ┌──┴──┐
      │ POT │  Potenziometro 10kΩ
      └──┬──┘
         ├────── Arduino A0 (wiper/cursore)
         |
        GND
```

**Codice Lettura:**
```cpp
const int POT_PIN = A0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int rawValue = analogRead(POT_PIN);  // 0-1023

    // Conversione a volt
    float voltage = rawValue * (5.0 / 1023.0);

    // Conversione a percentuale
    float percent = (rawValue / 1023.0) * 100.0;

    Serial.print("Raw: ");
    Serial.print(rawValue);
    Serial.print(" | Voltage: ");
    Serial.print(voltage, 2);  // 2 decimali
    Serial.print("V | Percent: ");
    Serial.print(percent, 1);
    Serial.println("%");

    delay(500);
}
```

### 5.2 Controllo Luminosità LED con Potenziometro

```cpp
const int POT_PIN = A0;
const int LED_PIN = 9;  // Pin PWM!

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    int potValue = analogRead(POT_PIN);  // 0-1023

    // Mappa da range ADC (0-1023) a range PWM (0-255)
    int brightness = map(potValue, 0, 1023, 0, 255);

    analogWrite(LED_PIN, brightness);

    delay(10);  // Piccolo delay per stabilità
}
```

**Funzione map():**
```cpp
int map(int value, int fromLow, int fromHigh, int toLow, int toHigh);

// Esempi:
map(512, 0, 1023, 0, 255)   // → 127 (metà)
map(0, 0, 1023, 0, 255)     // → 0
map(1023, 0, 1023, 0, 255)  // → 255

// Scala invertita:
map(512, 0, 1023, 255, 0)   // → 127 (da destra a sinistra)
```

### 5.3 Sensore Temperatura TMP36

**TMP36 Analog Temperature Sensor:**
```
Caratteristiche:
- Tensione output: 0.1V a -40°C, 0.75V a 25°C, 1.75V a 125°C
- Linearità: 10 mV/°C
- Offset: 500 mV a 0°C

Formula:
Temperatura (°C) = [(Vout in mV) - 500] / 10

Esempio:
Vout = 750 mV
Temp = (750 - 500) / 10 = 250 / 10 = 25°C
```

**Circuito:**
```
TMP36:
  Pin 1 (+5V)  ──── Arduino 5V
  Pin 2 (Vout) ──── Arduino A0
  Pin 3 (GND)  ──── Arduino GND
```

**Codice:**
```cpp
const int TEMP_PIN = A0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int reading = analogRead(TEMP_PIN);

    // Conversione a volt
    float voltage = reading * (5.0 / 1023.0);

    // Conversione a °C
    float temperatureC = (voltage - 0.5) * 100.0;

    Serial.print("Temperatura: ");
    Serial.print(temperatureC);
    Serial.println(" °C");

    delay(1000);
}
```

**Versione con Filtro (Riduce Rumore):**
```cpp
const int TEMP_PIN = A0;
const int NUM_SAMPLES = 10;

float readTemperature() {
    long sum = 0;

    // Media di N letture
    for (int i = 0; i < NUM_SAMPLES; i++) {
        sum += analogRead(TEMP_PIN);
        delay(10);
    }

    int average = sum / NUM_SAMPLES;
    float voltage = average * (5.0 / 1023.0);
    return (voltage - 0.5) * 100.0;
}

void loop() {
    float temp = readTemperature();

    Serial.print("Temperatura filtrata: ");
    Serial.print(temp, 1);
    Serial.println(" °C");

    delay(1000);
}
```

### 5.4 Fade LED (PWM)

```cpp
const int LED_PIN = 9;

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    // Fade in (0 → 255)
    for (int brightness = 0; brightness <= 255; brightness++) {
        analogWrite(LED_PIN, brightness);
        delay(10);  // 10ms × 255 = 2.55 secondi fade in
    }

    // Fade out (255 → 0)
    for (int brightness = 255; brightness >= 0; brightness--) {
        analogWrite(LED_PIN, brightness);
        delay(10);
    }
}
```

### 5.5 Controllo Motore DC con L293D

**L293D Motor Driver:**
```
Caratteristiche:
- 2 canali (2 motori DC)
- 600 mA per canale
- Diodi protezione integrati
- Controllo direzione + velocità

Pin:
IN1, IN2: Controllo direzione Motore A
EN1:      Enable PWM Motore A (velocità)
```

**Circuito:**
```
L293D Pin 1  (EN1)  ──── Arduino Pin 9 (PWM)
L293D Pin 2  (IN1)  ──── Arduino Pin 8
L293D Pin 7  (IN2)  ──── Arduino Pin 7
L293D Pin 8  (VCC2) ──── Batteria 9V (+)
L293D Pin 16 (VCC1) ──── Arduino 5V
L293D Pins 4,5,12,13 ─── GND

Motore ──── L293D Pin 3 e 6
```

**Codice:**
```cpp
const int ENABLE_PIN = 9;   // PWM
const int IN1_PIN = 8;
const int IN2_PIN = 7;

void setup() {
    pinMode(ENABLE_PIN, OUTPUT);
    pinMode(IN1_PIN, OUTPUT);
    pinMode(IN2_PIN, OUTPUT);
}

// Imposta velocità motore: -255 (indietro full) a +255 (avanti full)
void setMotorSpeed(int speed) {
    if (speed > 0) {
        // Avanti
        digitalWrite(IN1_PIN, HIGH);
        digitalWrite(IN2_PIN, LOW);
        analogWrite(ENABLE_PIN, speed);
    } else if (speed < 0) {
        // Indietro
        digitalWrite(IN1_PIN, LOW);
        digitalWrite(IN2_PIN, HIGH);
        analogWrite(ENABLE_PIN, -speed);  // Valore assoluto
    } else {
        // Stop (freno)
        digitalWrite(IN1_PIN, LOW);
        digitalWrite(IN2_PIN, LOW);
        analogWrite(ENABLE_PIN, 0);
    }
}

void loop() {
    // Avanti velocità crescente
    for (int speed = 0; speed <= 255; speed += 5) {
        setMotorSpeed(speed);
        delay(50);
    }

    delay(1000);

    // Indietro velocità crescente
    for (int speed = 0; speed <= 255; speed += 5) {
        setMotorSpeed(-speed);
        delay(50);
    }

    delay(1000);

    // Stop
    setMotorSpeed(0);
    delay(2000);
}
```

---

## 6. Timing: millis() vs delay()

### 6.1 Problema con delay()

**delay() blocca l'intero programma!**

```cpp
// ❌ CODICE BLOCCANTE (CATTIVO)
void loop() {
    digitalWrite(LED, HIGH);
    delay(1000);  // ← Sistema CONGELATO per 1 secondo
    digitalWrite(LED, LOW);
    delay(1000);  // ← Sistema CONGELATO per altro secondo

    // Durante delay():
    // - Non può leggere sensori
    // - Non può rispondere a pulsanti
    // - Non può fare comunicazione seriale
    // - Sistema MORTO
}
```

**Quando delay() è accettabile:**
- ✅ Setup iniziale
- ✅ Delay brevissimi (< 10 ms)
- ✅ Progetti semplicissimi educativi
- ❌ MAI in sistemi reattivi/IoT/controllo

### 6.2 Soluzione: millis()

**millis() → Tempo in millisecondi dall'avvio**

```cpp
unsigned long currentTime = millis();
// Ritorna millisecondi da quando Arduino è stato acceso
// Esempio: 5432 ms = 5.432 secondi

// Overflow dopo 49.7 giorni:
// 2^32 ms = 4,294,967,296 ms ≈ 49.7 giorni
```

**Pattern Base: Blink NON-Bloccante**
```cpp
const int LED_PIN = 13;
const unsigned long INTERVAL = 1000;  // 1 secondo

bool ledState = false;
unsigned long previousMillis = 0;

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();

    // Controlla se è passato abbastanza tempo
    if (currentMillis - previousMillis >= INTERVAL) {
        previousMillis = currentMillis;  // Salva timestamp

        // Toggle LED
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }

    // Codice qui è eseguito CONTINUAMENTE (migliaia volte/secondo)
    // Sistema REATTIVO!
}
```

**Gestione Overflow millis():**
```cpp
// ✅ SICURO: Sottrazione gestisce overflow automaticamente
unsigned long currentMillis = millis();
unsigned long previousMillis = ...;

if (currentMillis - previousMillis >= INTERVAL) {
    // OK anche se millis() ha fatto overflow!
}

// SPIEGAZIONE:
// Se previousMillis = 4,294,967,200 (vicino a overflow)
// E INTERVAL = 200
// currentMillis potrebbe = 100 (dopo overflow)
// currentMillis - previousMillis = 100 - 4,294,967,200
//   = -4,294,967,100 (signed)
//   = 200 (unsigned wraparound!)
// 200 >= 200 → TRUE ✅
```

### 6.3 Multi-Tasking con millis()

**Eseguire più task indipendenti:**

```cpp
// Task 1: Blink LED ogni 500ms
unsigned long led_previousMillis = 0;
const unsigned long LED_INTERVAL = 500;
bool ledState = false;

// Task 2: Leggi sensore ogni 2 secondi
unsigned long sensor_previousMillis = 0;
const unsigned long SENSOR_INTERVAL = 2000;

// Task 3: Invia dati seriale ogni 5 secondi
unsigned long serial_previousMillis = 0;
const unsigned long SERIAL_INTERVAL = 5000;

void setup() {
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();

    // Task 1: LED
    if (currentMillis - led_previousMillis >= LED_INTERVAL) {
        led_previousMillis = currentMillis;
        ledState = !ledState;
        digitalWrite(13, ledState);
    }

    // Task 2: Sensore
    if (currentMillis - sensor_previousMillis >= SENSOR_INTERVAL) {
        sensor_previousMillis = currentMillis;
        int value = analogRead(A0);
        Serial.print("Sensore: ");
        Serial.println(value);
    }

    // Task 3: Heartbeat
    if (currentMillis - serial_previousMillis >= SERIAL_INTERVAL) {
        serial_previousMillis = currentMillis;
        Serial.println("Sistema OK");
    }

    // Altri task possono essere aggiunti facilmente!
}
```

### 6.4 Stato Macchina (State Machine) con millis()

```cpp
enum State {
    STATE_IDLE,
    STATE_HEATING,
    STATE_HOLDING,
    STATE_COOLING
};

State currentState = STATE_IDLE;
unsigned long stateStartTime = 0;

const unsigned long HEATING_TIME = 5000;   // 5 sec
const unsigned long HOLDING_TIME = 10000;  // 10 sec
const unsigned long COOLING_TIME = 3000;   // 3 sec

void setup() {
    Serial.begin(9600);
}

void loop() {
    unsigned long currentMillis = millis();
    unsigned long elapsedTime = currentMillis - stateStartTime;

    switch (currentState) {
        case STATE_IDLE:
            Serial.println("IDLE - Premi pulsante per iniziare");
            if (digitalRead(2) == LOW) {  // Pulsante premuto
                currentState = STATE_HEATING;
                stateStartTime = millis();
            }
            break;

        case STATE_HEATING:
            Serial.println("HEATING...");
            if (elapsedTime >= HEATING_TIME) {
                currentState = STATE_HOLDING;
                stateStartTime = millis();
            }
            break;

        case STATE_HOLDING:
            Serial.println("HOLDING temperature");
            if (elapsedTime >= HOLDING_TIME) {
                currentState = STATE_COOLING;
                stateStartTime = millis();
            }
            break;

        case STATE_COOLING:
            Serial.println("COOLING down");
            if (elapsedTime >= COOLING_TIME) {
                currentState = STATE_IDLE;
            }
            break;
    }

    delay(500);  // Solo per rallentare output seriale
}
```

### 6.5 Timeout con millis()

```cpp
const unsigned long TIMEOUT = 5000;  // 5 secondi
unsigned long startTime;
bool waiting = false;

void startWaiting() {
    startTime = millis();
    waiting = true;
}

void loop() {
    if (waiting) {
        if (millis() - startTime >= TIMEOUT) {
            Serial.println("TIMEOUT!");
            waiting = false;
        }
    }

    // Controlla condizione
    if (Serial.available() > 0) {
        char c = Serial.read();
        if (c == 'S') {
            Serial.println("Avvio attesa...");
            startWaiting();
        } else if (c == 'C' && waiting) {
            Serial.println("Annullato");
            waiting = false;
        }
    }
}
```

---

## 7. Comunicazione Seriale

### 7.1 Setup e Configurazione

**Baud Rate:**
```
Bit per secondo trasmessi

Comuni:
  9600   - Standard, affidabile
  115200 - Veloce per debug
  57600  - Compromesso

Formula tempo trasmissione:
  1 byte = 10 bit (1 start + 8 data + 1 stop)
  A 9600 baud: 960 bytes/sec = ~1 ms/byte
```

**Setup Base:**
```cpp
void setup() {
    Serial.begin(9600);  // Inizializza a 9600 baud

    // IMPORTANTE per boards native USB (Leonardo, Micro)
    while (!Serial) {
        ; // Attendi connessione Serial Monitor
    }

    Serial.println("Sistema pronto!");
}
```

### 7.2 Output Seriale

**Funzioni Base:**
```cpp
Serial.print("Testo");       // Stampa senza newline
Serial.println("Testo");     // Stampa con newline (\r\n)

Serial.print(42);            // Stampa numero
Serial.println(42);

Serial.print(3.14159, 2);    // Stampa float con 2 decimali: 3.14
Serial.println(42, BIN);     // Binario: 101010
Serial.println(42, HEX);     // Esadecimale: 2A
```

**Output Formattato:**
```cpp
int value = 42;
float temp = 25.67;

// Metodo 1: Concatenazione
Serial.print("Valore: ");
Serial.print(value);
Serial.print(", Temp: ");
Serial.print(temp, 2);
Serial.println(" °C");

// Metodo 2: sprintf (più efficiente)
char buffer[100];
sprintf(buffer, "Valore: %d, Temp: %.2f °C", value, (int)(temp*100)/100.0);
Serial.println(buffer);
// NOTA: sprintf su Arduino non supporta %f! Workaround: dtostrf()

// Metodo 3: dtostrf per float
char tempStr[10];
dtostrf(temp, 4, 2, tempStr);  // width 4, precision 2
sprintf(buffer, "Temp: %s °C", tempStr);
Serial.println(buffer);
```

**Tabelle Formattate:**
```cpp
void printTable() {
    Serial.println("┌──────┬──────┬──────┐");
    Serial.println("│  A0  │  A1  │  A2  │");
    Serial.println("├──────┼──────┼──────┤");

    for (int i = 0; i < 5; i++) {
        int a0 = analogRead(A0);
        int a1 = analogRead(A1);
        int a2 = analogRead(A2);

        char line[50];
        sprintf(line, "│ %4d │ %4d │ %4d │", a0, a1, a2);
        Serial.println(line);

        delay(1000);
    }

    Serial.println("└──────┴──────┴──────┘");
}
```

### 7.3 Input Seriale

**Controllo Disponibilità:**
```cpp
void loop() {
    if (Serial.available() > 0) {
        // Dati disponibili!
        char c = Serial.read();  // Legge 1 byte
        Serial.print("Ricevuto: ");
        Serial.println(c);
    }
}
```

**Lettura Riga Completa:**
```cpp
void loop() {
    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');  // Leggi fino a newline
        input.trim();  // Rimuovi spazi/newline

        Serial.print("Hai scritto: ");
        Serial.println(input);
    }
}
```

**Parsing Comandi:**
```cpp
void loop() {
    if (Serial.available() > 0) {
        String cmd = Serial.readStringUntil('\n');
        cmd.trim();
        cmd.toUpperCase();  // Converti a maiuscolo

        if (cmd == "ON") {
            digitalWrite(LED, HIGH);
            Serial.println("LED acceso");
        } else if (cmd == "OFF") {
            digitalWrite(LED, LOW);
            Serial.println("LED spento");
        } else if (cmd.startsWith("SET ")) {
            int value = cmd.substring(4).toInt();
            analogWrite(LED, value);
            Serial.print("Luminosità: ");
            Serial.println(value);
        } else if (cmd == "STATUS") {
            Serial.print("LED: ");
            Serial.println(digitalRead(LED) ? "ON" : "OFF");
        } else {
            Serial.println("Comando non riconosciuto");
            Serial.println("Comandi: ON, OFF, SET <0-255>, STATUS");
        }
    }
}
```

**Menu Interattivo:**
```cpp
void printMenu() {
    Serial.println("\n=== MENU ===");
    Serial.println("1. Accendi LED");
    Serial.println("2. Spegni LED");
    Serial.println("3. Blink LED");
    Serial.println("4. Leggi sensore");
    Serial.println("5. Status");
    Serial.println("============");
    Serial.print("Scelta: ");
}

void setup() {
    Serial.begin(9600);
    pinMode(13, OUTPUT);
    printMenu();
}

void loop() {
    if (Serial.available() > 0) {
        char choice = Serial.read();
        Serial.println(choice);  // Echo

        switch (choice) {
            case '1':
                digitalWrite(13, HIGH);
                Serial.println("LED ON");
                break;

            case '2':
                digitalWrite(13, LOW);
                Serial.println("LED OFF");
                break;

            case '3':
                Serial.println("Blinking 5 times...");
                for (int i = 0; i < 5; i++) {
                    digitalWrite(13, HIGH);
                    delay(200);
                    digitalWrite(13, LOW);
                    delay(200);
                }
                Serial.println("Done");
                break;

            case '4':
                int value = analogRead(A0);
                Serial.print("Sensore A0: ");
                Serial.println(value);
                break;

            case '5':
                Serial.print("LED: ");
                Serial.println(digitalRead(13) ? "ON" : "OFF");
                Serial.print("Uptime: ");
                Serial.print(millis() / 1000);
                Serial.println(" sec");
                break;

            default:
                Serial.println("Scelta non valida");
        }

        printMenu();
    }
}
```

### 7.4 Protocollo Custom Semplice

**Formato: `<CMD>:<PARAM1>,<PARAM2>;`**

```cpp
void processCommand(String cmd) {
    // Esempio: "LED:13,1;" → Accendi LED pin 13
    //          "PWM:9,128;" → PWM pin 9 valore 128
    //          "READ:A0;" → Leggi analog pin A0

    int colonPos = cmd.indexOf(':');
    int semicolonPos = cmd.indexOf(';');

    if (colonPos == -1 || semicolonPos == -1) {
        Serial.println("ERR:Formato non valido");
        return;
    }

    String command = cmd.substring(0, colonPos);
    String params = cmd.substring(colonPos + 1, semicolonPos);

    if (command == "LED") {
        int commaPos = params.indexOf(',');
        int pin = params.substring(0, commaPos).toInt();
        int state = params.substring(commaPos + 1).toInt();

        digitalWrite(pin, state);
        Serial.print("OK:LED ");
        Serial.print(pin);
        Serial.print(" = ");
        Serial.println(state);

    } else if (command == "PWM") {
        int commaPos = params.indexOf(',');
        int pin = params.substring(0, commaPos).toInt();
        int value = params.substring(commaPos + 1).toInt();

        analogWrite(pin, value);
        Serial.print("OK:PWM ");
        Serial.print(pin);
        Serial.print(" = ");
        Serial.println(value);

    } else if (command == "READ") {
        int pin = params.toInt();
        int value = analogRead(pin);
        Serial.print("OK:");
        Serial.println(value);

    } else {
        Serial.println("ERR:Comando sconosciuto");
    }
}

void loop() {
    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        input.trim();
        processCommand(input);
    }
}
```

---

## 8. Sensori e Attuatori

### 8.1 DHT22 - Temperatura e Umidità

**Specifiche DHT22:**
```
Temperatura: -40°C a +80°C (±0.5°C)
Umidità: 0-100% RH (±2%)
Protocollo: 1-Wire proprietario
Sampling: Max ogni 2 secondi
```

**Circuito:**
```
DHT22:
  Pin 1 (VCC) ──── Arduino 5V
  Pin 2 (DATA)──── Arduino Pin 2 ──┬─── [10kΩ] ─── 5V (pull-up)
  Pin 3 (NC)   (non connesso)      │
  Pin 4 (GND) ──── Arduino GND     └─ (oppure usa pull-up interno)
```

**Libreria:**
```
Arduino IDE → Tools → Manage Libraries
Cerca: "DHT sensor library" by Adafruit
Install (installa anche "Adafruit Unified Sensor")
```

**Codice:**
```cpp
#include <DHT.h>

#define DHTPIN 2       // Pin dati DHT22
#define DHTTYPE DHT22  // Tipo sensore

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    dht.begin();
    Serial.println("DHT22 Test");
}

void loop() {
    delay(2000);  // DHT22 richiede almeno 2 sec tra letture

    float humidity = dht.readHumidity();
    float tempC = dht.readTemperature();       // Celsius
    float tempF = dht.readTemperature(true);   // Fahrenheit

    // Controllo errori
    if (isnan(humidity) || isnan(tempC)) {
        Serial.println("Errore lettura DHT22!");
        return;
    }

    // Heat index (temperatura percepita)
    float heatIndex = dht.computeHeatIndex(tempF, humidity);

    // Output
    Serial.print("Umidità: ");
    Serial.print(humidity);
    Serial.print(" %\t");
    Serial.print("Temperatura: ");
    Serial.print(tempC);
    Serial.print(" °C / ");
    Serial.print(tempF);
    Serial.print(" °F\t");
    Serial.print("Percepita: ");
    Serial.print(heatIndex);
    Serial.println(" °F");
}
```

### 8.2 HC-SR04 - Sensore Distanza Ultrasuoni

**Funzionamento:**
```
1. Trigger pulse 10μs → emette ultrasuoni
2. Sensore rileva echo ritornato
3. Misura tempo echo
4. Calcola distanza:
   Distanza = (Tempo × Velocità suono) / 2
            = (Tempo × 343 m/s) / 2
            = (Tempo × 0.0343 cm/μs) / 2
```

**Specifiche:**
```
Range: 2 cm - 400 cm
Angolo: 15°
Precisione: ±3 mm
Tensione: 5V
```

**Circuito:**
```
HC-SR04:
  VCC  ──── Arduino 5V
  TRIG ──── Arduino Pin 9
  ECHO ──── Arduino Pin 10
  GND  ──── Arduino GND
```

**Codice:**
```cpp
const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

void setup() {
    Serial.begin(9600);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
}

// Ritorna distanza in cm
long readDistance() {
    // Pulisci trigger
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    // Genera pulse 10μs
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Leggi durata echo (μs)
    long duration = pulseIn(ECHO_PIN, HIGH, 30000);  // Timeout 30ms

    // Controllo timeout
    if (duration == 0) {
        return -1;  // Errore: nessun echo ricevuto
    }

    // Calcola distanza
    long distance = duration * 0.0343 / 2;  // cm

    return distance;
}

void loop() {
    long dist = readDistance();

    if (dist == -1) {
        Serial.println("Errore: fuori range");
    } else {
        Serial.print("Distanza: ");
        Serial.print(dist);
        Serial.println(" cm");
    }

    delay(500);
}
```

**Versione con Filtro (Media Mobile):**
```cpp
const int SAMPLES = 5;
long readings[SAMPLES];
int readIndex = 0;
long total = 0;

long readDistanceFiltered() {
    // Rimuovi lettura vecchia dalla somma
    total -= readings[readIndex];

    // Nuova lettura
    long newReading = readDistance();

    // Ignora errori
    if (newReading == -1) {
        newReading = readings[readIndex];  // Usa valore precedente
    }

    // Aggiungi a buffer
    readings[readIndex] = newReading;
    total += newReading;

    // Avanza indice (circolare)
    readIndex = (readIndex + 1) % SAMPLES;

    // Ritorna media
    return total / SAMPLES;
}

void setup() {
    Serial.begin(9600);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);

    // Inizializza buffer
    for (int i = 0; i < SAMPLES; i++) {
        readings[i] = 100;  // Valore default
    }
    total = 100 * SAMPLES;
}

void loop() {
    long dist = readDistanceFiltered();

    Serial.print("Distanza (filtrata): ");
    Serial.print(dist);
    Serial.println(" cm");

    delay(100);
}
```

### 8.3 Relay - Controllo Carichi AC

**Relay Module:**
```
Permette ad Arduino (5V DC) di controllare carichi AC (230V) o DC ad alta corrente

ATTENZIONE SICUREZZA:
- 230V AC PUÒ UCCIDERE!
- Solo personale qualificato
- Doppio controllo collegamenti
- Mai toccare sotto tensione
```

**Circuito:**
```
Relay Module:
  VCC ──── Arduino 5V
  GND ──── Arduino GND
  IN  ──── Arduino Pin 7

  COM ──── AC Line (fase)
  NO  ──── Lampada / Dispositivo
  (Dispositivo) ──── AC Neutral

NO = Normally Open (chiude al trigger)
NC = Normally Closed (apre al trigger)
COM = Common
```

**Codice:**
```cpp
const int RELAY_PIN = 7;

void setup() {
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW);  // Relay OFF all'avvio
}

void loop() {
    // Accendi per 5 secondi
    digitalWrite(RELAY_PIN, HIGH);  // Relay ON
    delay(5000);

    // Spegni per 5 secondi
    digitalWrite(RELAY_PIN, LOW);   // Relay OFF
    delay(5000);
}
```

**Controllo con Pulsante:**
```cpp
#include <Bounce2.h>

const int BUTTON_PIN = 2;
const int RELAY_PIN = 7;

Bounce button = Bounce();
bool relayState = false;

void setup() {
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW);

    button.attach(BUTTON_PIN, INPUT_PULLUP);
    button.interval(50);

    Serial.begin(9600);
}

void loop() {
    button.update();

    if (button.fell()) {
        relayState = !relayState;
        digitalWrite(RELAY_PIN, relayState);

        Serial.print("Relay: ");
        Serial.println(relayState ? "ON" : "OFF");
    }
}
```

### 8.4 Servo Motor

**Servo Standard (180°):**
```
Controllo posizione angolare 0-180°
Protocollo PWM: pulse 1-2 ms ogni 20ms
  1.0 ms → 0°
  1.5 ms → 90°
  2.0 ms → 180°
```

**Circuito:**
```
Servo (3 fili):
  Rosso   (VCC) ──── Arduino 5V (o alimentazione esterna se carico>500mA)
  Marrone (GND) ──── Arduino GND
  Giallo  (PWM) ──── Arduino Pin 9
```

**Codice:**
```cpp
#include <Servo.h>

Servo myServo;
const int SERVO_PIN = 9;

void setup() {
    myServo.attach(SERVO_PIN);
    myServo.write(90);  // Posizione centrale
    delay(1000);
}

void loop() {
    // Sweep 0° → 180°
    for (int pos = 0; pos <= 180; pos++) {
        myServo.write(pos);
        delay(15);  // Attendi movimento
    }

    delay(1000);

    // Sweep 180° → 0°
    for (int pos = 180; pos >= 0; pos--) {
        myServo.write(pos);
        delay(15);
    }

    delay(1000);
}
```

**Controllo con Potenziometro:**
```cpp
#include <Servo.h>

Servo myServo;
const int SERVO_PIN = 9;
const int POT_PIN = A0;

void setup() {
    myServo.attach(SERVO_PIN);
}

void loop() {
    int potValue = analogRead(POT_PIN);         // 0-1023
    int angle = map(potValue, 0, 1023, 0, 180); // 0-180°

    myServo.write(angle);
    delay(15);
}
```

---

## 9. Display e Interfacce Utente

### 9.1 LCD 16x2 con I2C

**Vantaggi I2C:**
- Solo 2 fili (SDA, SCL) invece di 6+ per parallel
- Indirizzo configurabile → multipli LCD su stesso bus

**Circuito:**
```
LCD I2C Module:
  GND ──── Arduino GND
  VCC ──── Arduino 5V
  SDA ──── Arduino A4 (SDA)
  SCL ──── Arduino A5 (SCL)
```

**Libreria:**
```
Arduino IDE → Manage Libraries
Cerca: "LiquidCrystal I2C" by Frank de Brabander
Install
```

**Trova Indirizzo I2C:**
```cpp
#include <Wire.h>

void setup() {
    Serial.begin(9600);
    Wire.begin();
    Serial.println("Scanning I2C bus...");

    for (byte addr = 1; addr < 127; addr++) {
        Wire.beginTransmission(addr);
        if (Wire.endTransmission() == 0) {
            Serial.print("Device found at 0x");
            if (addr < 16) Serial.print("0");
            Serial.println(addr, HEX);
        }
    }
    Serial.println("Scan complete");
}

void loop() {}
```

**Codice LCD:**
```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Indirizzo I2C, colonne, righe
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();           // Inizializza
    lcd.backlight();      // Accendi retroilluminazione

    // Riga 0, colonna 0
    lcd.setCursor(0, 0);
    lcd.print("Hello ITS!");

    // Riga 1, colonna 0
    lcd.setCursor(0, 1);
    lcd.print("Arduino 2025");
}

void loop() {
    // Vuoto
}
```

**Display Temperatura:**
```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT22

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    lcd.init();
    lcd.backlight();
    dht.begin();

    lcd.setCursor(0, 0);
    lcd.print("Temp & Humidity");
    delay(2000);
}

void loop() {
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();

    if (isnan(temp) || isnan(hum)) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Sensor Error!");
    } else {
        lcd.clear();

        // Riga 0: Temperatura
        lcd.setCursor(0, 0);
        lcd.print("Temp: ");
        lcd.print(temp, 1);
        lcd.print(" C");

        // Riga 1: Umidità
        lcd.setCursor(0, 1);
        lcd.print("Hum:  ");
        lcd.print(hum, 1);
        lcd.print(" %");
    }

    delay(2000);
}
```

**Custom Characters:**
```cpp
// Crea carattere cuore
byte heart[8] = {
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000,
    0b00000
};

void setup() {
    lcd.init();
    lcd.backlight();

    lcd.createChar(0, heart);  // Salva a indice 0

    lcd.setCursor(0, 0);
    lcd.print("I ");
    lcd.write(0);  // Stampa custom char 0
    lcd.print(" Arduino!");
}
```

### 9.2 OLED Display (128x64, I2C)

**Vantaggi OLED vs LCD:**
- Risoluzione alta (grafica pixel-perfect)
- Contrasto migliore
- Nessuna retroilluminazione (consuma meno)
- Più costoso

**Libreria:**
```
Manage Libraries → "Adafruit SSD1306" + "Adafruit GFX Library"
```

**Codice Base:**
```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1  // No reset pin

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("OLED init failed!");
        while (1);  // Stop
    }

    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0, 0);
    display.println("Hello");
    display.println("ITS 2025!");
    display.display();  // Aggiorna schermo
}

void loop() {}
```

**Grafica:**
```cpp
void loop() {
    display.clearDisplay();

    // Cerchio
    display.drawCircle(64, 32, 20, SSD1306_WHITE);

    // Rettangolo pieno
    display.fillRect(10, 10, 30, 20, SSD1306_WHITE);

    // Linea
    display.drawLine(0, 0, 127, 63, SSD1306_WHITE);

    // Testo
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.println("FPS Test");

    display.display();
    delay(100);
}
```

---

## 10. Interrupt e Gestione Eventi

### 10.1 Interrupt Esterni

**Cos'è un Interrupt:**
```
Evento hardware che INTERROMPE esecuzione normale
→ Salta immediatamente a ISR (Interrupt Service Routine)
→ Esegue ISR
→ Ritorna al codice normale

Vantaggio: Risposta ISTANTANEA (microsecondi)
Svantaggio: Complessità, limitazioni
```

**Pin Interrupt Arduino Uno:**
```
Pin 2 → Interrupt 0
Pin 3 → Interrupt 1

attachInterrupt(digitalPinToInterrupt(pin), ISR_function, MODE);
```

**Modi Trigger:**
```
LOW      → Interrupt quando pin è LOW
CHANGE   → Interrupt ad ogni cambio stato
RISING   → Interrupt su transizione LOW→HIGH
FALLING  → Interrupt su transizione HIGH→LOW
```

**Codice Base:**
```cpp
volatile int counter = 0;  // DEVE essere volatile!

void setup() {
    Serial.begin(9600);
    pinMode(2, INPUT_PULLUP);

    // Attach interrupt
    attachInterrupt(digitalPinToInterrupt(2), buttonPressed, FALLING);

    Serial.println("Premi pulsante...");
}

void buttonPressed() {
    // ISR: BREVE E VELOCE!
    counter++;
}

void loop() {
    static int lastCounter = 0;

    if (counter != lastCounter) {
        lastCounter = counter;
        Serial.print("Count: ");
        Serial.println(counter);
    }

    delay(100);
}
```

### 10.2 Regole per ISR

**✅ FARE in ISR:**
- Leggere/scrivere variabili `volatile`
- Settare flag boolean
- Incrementare contatori
- `digitalRead()`, `digitalWrite()`
- Operazioni VELOCI (<10 μs ideale)

**❌ NON FARE in ISR:**
- `delay()` - BLOCCA interrupt
- `millis()` - Non si aggiorna durante ISR
- `Serial.print()` - Troppo lento
- `analogRead()` - Richiede tempo
- `malloc()`, `free()` - Gestione memoria complessa
- Operazioni lunghe

**Esempio SBAGLIATO:**
```cpp
// ❌ CATTIVO: ISR troppo lenta
void ISR_slow() {
    Serial.println("Interrupt!");  // ❌ Seriale in ISR
    delay(1000);                   // ❌ Delay in ISR
    int value = analogRead(A0);    // ❌ ADC in ISR
}
```

**Esempio CORRETTO:**
```cpp
// ✅ BUONO: ISR setta solo flag
volatile bool dataReady = false;

void ISR_fast() {
    dataReady = true;  // ✅ Solo flag
}

void loop() {
    if (dataReady) {
        dataReady = false;

        // Processing nel loop (non in ISR)
        Serial.println("Data processing...");
        int value = analogRead(A0);
        delay(100);
    }
}
```

### 10.3 volatile Keyword

**Perché volatile:**
```cpp
// SENZA volatile
int counter = 0;

void ISR() {
    counter++;  // Modifica in ISR
}

void loop() {
    if (counter > 10) {  // Compilatore potrebbe ottimizzare via!
        // Codice potrebbe non eseguire
    }
}

// CON volatile
volatile int counter = 0;  // Dice al compilatore: "può cambiare inaspettatamente"

void ISR() {
    counter++;
}

void loop() {
    if (counter > 10) {  // Compilatore controlla sempre
        // Funziona correttamente
    }
}
```

**Regola:** Tutte le variabili condivise tra ISR e main loop DEVONO essere `volatile`.

### 10.4 Debouncing con Interrupt

```cpp
#include <Bounce2.h>

const int BUTTON_PIN = 2;
volatile bool buttonPressed = false;

Bounce button = Bounce();

void setup() {
    Serial.begin(9600);
    button.attach(BUTTON_PIN, INPUT_PULLUP);
    button.interval(50);

    attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), ISR_button, FALLING);
}

void ISR_button() {
    buttonPressed = true;  // Setta flag
}

void loop() {
    if (buttonPressed) {
        buttonPressed = false;
        button.update();  // Debounce in loop

        if (button.fell()) {
            Serial.println("Click valido!");
        }
    }
}
```

---

## 11. Comunicazioni I2C e SPI

### 11.1 I2C (Inter-Integrated Circuit)

**Caratteristiche:**
- 2 fili: SDA (data), SCL (clock)
- Multi-master, multi-slave
- Indirizzamento: 7-bit (128 dispositivi teorici)
- Velocità: Standard 100 kHz, Fast 400 kHz

**Pin Arduino Uno:**
```
SDA: A4
SCL: A5

(Mega, Due: pin dedicati SDA/SCL)
```

**Protocollo:**
```
Master invia:
  START → ADDRESS → R/W → DATA → ACK/NACK → STOP

Esempio lettura:
  START → 0x27 (indirizzo slave) → 1 (read) → [slave invia dati] → ACK → STOP
```

**Codice Master (Arduino legge da slave):**
```cpp
#include <Wire.h>

const byte SLAVE_ADDR = 0x27;

void setup() {
    Serial.begin(9600);
    Wire.begin();  // Inizializza come master
}

void loop() {
    Wire.requestFrom(SLAVE_ADDR, 2);  // Richiedi 2 byte

    if (Wire.available() >= 2) {
        byte b1 = Wire.read();
        byte b2 = Wire.read();

        Serial.print("Ricevuto: ");
        Serial.print(b1);
        Serial.print(", ");
        Serial.println(b2);
    }

    delay(1000);
}
```

**Codice Slave (Arduino risponde a richieste):**
```cpp
#include <Wire.h>

const byte MY_ADDR = 0x27;
int counter = 0;

void setup() {
    Wire.begin(MY_ADDR);  // Inizializza come slave
    Wire.onRequest(requestEvent);  // Callback su richiesta
}

void requestEvent() {
    // Master ha richiesto dati
    counter++;
    Wire.write(counter >> 8);    // High byte
    Wire.write(counter & 0xFF);  // Low byte
}

void loop() {
    delay(100);
}
```

### 11.2 SPI (Serial Peripheral Interface)

**Caratteristiche:**
- 4 fili: MOSI, MISO, SCK, SS (per slave)
- Full-duplex (trasmissione bidirezionale simultanea)
- Molto veloce (MHz range)
- Single master, multi slave (un SS per slave)

**Pin Arduino Uno:**
```
MOSI: 11 (Master Out Slave In)
MISO: 12 (Master In Slave Out)
SCK:  13 (Clock)
SS:   10 (Slave Select, configurabile)
```

**Codice Master:**
```cpp
#include <SPI.h>

const int SS_PIN = 10;

void setup() {
    Serial.begin(9600);
    pinMode(SS_PIN, OUTPUT);
    digitalWrite(SS_PIN, HIGH);  // Deseleziona slave

    SPI.begin();
    SPI.setClockDivider(SPI_CLOCK_DIV16);  // 1 MHz
}

void loop() {
    // Seleziona slave
    digitalWrite(SS_PIN, LOW);

    // Trasferisci byte (full-duplex: invia E riceve)
    byte received = SPI.transfer(0x55);  // Invia 0x55, ricevi risposta

    // Deseleziona slave
    digitalWrite(SS_PIN, HIGH);

    Serial.print("Ricevuto: 0x");
    Serial.println(received, HEX);

    delay(1000);
}
```

---

## 12. ESP32: WiFi e Bluetooth

### 12.1 ESP32 Overview

**Specifiche:**
```
MCU: Dual-core Xtensa 32-bit @ 240 MHz
RAM: 520 KB SRAM
Flash: 4 MB
WiFi: 802.11 b/g/n (2.4 GHz)
Bluetooth: Classic + BLE 4.2
GPIO: 34 pin (alcuni solo input)
ADC: 12-bit (0-4095)
DAC: 2× 8-bit
Tensione: 3.3V (NON 5V!)
Prezzo: €5-10

Vantaggi vs Arduino Uno:
  ✅ 15× più veloce
  ✅ 260× più RAM
  ✅ WiFi/Bluetooth integrati
  ✅ Più economico!
```

**Setup Arduino IDE per ESP32:**
```
1. File → Preferences
2. Additional Boards Manager URLs:
   https://dl.espressif.com/dl/package_esp32_index.json

3. Tools → Board → Boards Manager
4. Cerca "esp32" by Espressif Systems
5. Install

6. Tools → Board → ESP32 Arduino → ESP32 Dev Module
```

### 12.2 WiFi Client (Connessione a Router)

```cpp
#include <WiFi.h>

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
    Serial.begin(115200);

    // Connetti a WiFi
    Serial.print("Connessione a ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connesso!");
    Serial.print("Indirizzo IP: ");
    Serial.println(WiFi.localIP());
}

void loop() {
    // Mantieni connessione
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi disconnesso! Riconnetto...");
        WiFi.begin(ssid, password);
        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
        }
    }

    delay(1000);
}
```

### 12.3 Web Server su ESP32

```cpp
#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

WebServer server(80);  // Porta 80 (HTTP)

const int LED_PIN = 2;  // LED integrato ESP32
bool ledState = false;

void handleRoot() {
    String html = "<html><body>";
    html += "<h1>ESP32 Web Server</h1>";
    html += "<p>LED Status: ";
    html += ledState ? "ON" : "OFF";
    html += "</p>";
    html += "<a href='/on'><button>LED ON</button></a>";
    html += "<a href='/off'><button>LED OFF</button></a>";
    html += "</body></html>";

    server.send(200, "text/html", html);
}

void handleLedOn() {
    ledState = true;
    digitalWrite(LED_PIN, HIGH);
    server.sendHeader("Location", "/");
    server.send(303);  // Redirect
}

void handleLedOff() {
    ledState = false;
    digitalWrite(LED_PIN, LOW);
    server.sendHeader("Location", "/");
    server.send(303);
}

void setup() {
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWiFi connesso");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());

    server.on("/", handleRoot);
    server.on("/on", handleLedOn);
    server.on("/off", handleLedOff);

    server.begin();
    Serial.println("HTTP server avviato");
}

void loop() {
    server.handleClient();
}
```

**Uso:**
```
1. Carica sketch su ESP32
2. Apri Serial Monitor (115200 baud)
3. Leggi IP (es: 192.168.1.100)
4. Apri browser → http://192.168.1.100
5. Click pulsanti per controllare LED
```

### 12.4 HTTP Request (Invia Dati a Server)

```cpp
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

const char* serverURL = "http://api.thingspeak.com/update";
const char* apiKey = "YOUR_API_KEY";

void setup() {
    Serial.begin(115200);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
    Serial.println("WiFi OK");
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;

        // Leggi sensore
        int sensorValue = analogRead(34);  // GPIO 34

        // Costruisci URL
        String url = String(serverURL) + "?api_key=" + apiKey +
                     "&field1=" + String(sensorValue);

        http.begin(url);
        int httpCode = http.GET();

        if (httpCode > 0) {
            Serial.print("HTTP Response: ");
            Serial.println(httpCode);
            String payload = http.getString();
            Serial.println(payload);
        } else {
            Serial.println("HTTP Error");
        }

        http.end();
    }

    delay(15000);  // ThingSpeak: min 15 sec tra update
}
```

### 12.5 MQTT con ESP32

**MQTT (Message Queue Telemetry Transport):**
- Protocollo publish/subscribe
- Lightweight (ideale IoT)
- Broker centrale (es: Mosquitto, HiveMQ, broker.hivemq.com)

**Libreria:**
```
Manage Libraries → "PubSubClient" by Nick O'Leary
```

**Codice:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

const char* mqtt_server = "broker.hivemq.com";  // Broker pubblico test
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
    Serial.println("WiFi OK");
}

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Messaggio ricevuto [");
    Serial.print(topic);
    Serial.print("]: ");

    String message;
    for (int i = 0; i < length; i++) {
        message += (char)payload[i];
    }
    Serial.println(message);

    // Azione su messaggio
    if (message == "ON") {
        digitalWrite(2, HIGH);
    } else if (message == "OFF") {
        digitalWrite(2, LOW);
    }
}

void reconnect() {
    while (!client.connected()) {
        Serial.print("MQTT connessione...");

        String clientId = "ESP32Client-" + String(random(0xffff), HEX);

        if (client.connect(clientId.c_str())) {
            Serial.println("connesso");
            client.subscribe("test/led");  // Subscribe a topic
        } else {
            Serial.print("fallito, rc=");
            Serial.println(client.state());
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    pinMode(2, OUTPUT);

    setup_wifi();
    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);
}

void loop() {
    if (!client.connected()) {
        reconnect();
    }
    client.loop();

    // Pubblica temperatura ogni 10 sec
    static unsigned long lastPub = 0;
    if (millis() - lastPub > 10000) {
        lastPub = millis();

        float temp = 25.5;  // Leggi da sensore reale
        String payload = String(temp);

        client.publish("test/temperature", payload.c_str());
        Serial.println("Pubblicato: " + payload);
    }
}
```

---

## 13. Librerie Arduino

### 13.1 Installazione Librerie

**Metodo 1: Library Manager (Raccomandato)**
```
Sketch → Include Library → Manage Libraries
Cerca nome libreria
Click Install
```

**Metodo 2: ZIP File**
```
Download .zip da GitHub
Sketch → Include Library → Add .ZIP Library
Seleziona file
```

**Metodo 3: Manuale**
```
Copia cartella libreria in:
  Windows: Documents/Arduino/libraries/
  Linux: ~/Arduino/libraries/
  Mac: ~/Documents/Arduino/libraries/
Riavvia IDE
```

### 13.2 Librerie Essenziali

**Sensori:**
```cpp
// DHT (temperatura/umidità)
#include <DHT.h>

// BMP/BME (pressione/altitudine)
#include <Adafruit_BMP280.h>
#include <Adafruit_BME280.h>

// MPU6050 (accelerometro/giroscopio)
#include <MPU6050.h>

// DS18B20 (temperatura 1-wire)
#include <OneWire.h>
#include <DallasTemperature.h>
```

**Display:**
```cpp
// LCD I2C
#include <LiquidCrystal_I2C.h>

// OLED
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// TFT
#include <Adafruit_ST7735.h>
```

**Comunicazione:**
```cpp
// WiFi (ESP32/ESP8266)
#include <WiFi.h>

// Ethernet
#include <Ethernet.h>

// MQTT
#include <PubSubClient.h>

// HTTP
#include <HTTPClient.h>
```

**Attuatori:**
```cpp
// Servo
#include <Servo.h>

// Stepper
#include <Stepper.h>
#include <AccelStepper.h>

// NeoPixel (LED RGB)
#include <Adafruit_NeoPixel.h>
```

**Utility:**
```cpp
// Debouncing
#include <Bounce2.h>

// Timing avanzato
#include <elapsedMillis.h>

// EEPROM
#include <EEPROM.h>

// SD Card
#include <SD.h>

// RTC (Real Time Clock)
#include <RTClib.h>
```

---

## 14. Progetti IoT Completi

### 14.1 Stazione Meteo IoT

**Componenti:**
- ESP32
- DHT22 (temp/umidità)
- BMP280 (pressione)
- OLED display 128x64
- Pulsante (cambio schermata)

**Schema:** (omesso per brevità, vedi materiali corso)

**Codice Completo:** (circa 300 righe, estratto chiave)

```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Configurazione WiFi
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// MQTT
const char* mqtt_server = "broker.hivemq.com";
WiFiClient espClient;
PubSubClient mqtt(espClient);

// Sensori
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP280 bmp;

// Display
Adafruit_SSD1306 display(128, 64, &Wire, -1);

// Variabili
struct SensorData {
    float temperature;
    float humidity;
    float pressure;
    float altitude;
} data;

void readSensors() {
    data.temperature = dht.readTemperature();
    data.humidity = dht.readHumidity();
    data.pressure = bmp.readPressure() / 100.0;  // hPa
    data.altitude = bmp.readAltitude(1013.25);   // m
}

void updateDisplay() {
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);

    display.setCursor(0, 0);
    display.println("=== STAZIONE METEO ===");

    display.setCursor(0, 16);
    display.print("Temp:  ");
    display.print(data.temperature, 1);
    display.println(" C");

    display.setCursor(0, 28);
    display.print("Hum:   ");
    display.print(data.humidity, 1);
    display.println(" %");

    display.setCursor(0, 40);
    display.print("Press: ");
    display.print(data.pressure, 1);
    display.println(" hPa");

    display.setCursor(0, 52);
    display.print("Alt:   ");
    display.print(data.altitude, 0);
    display.println(" m");

    display.display();
}

void publishData() {
    if (mqtt.connected()) {
        char msg[100];
        sprintf(msg, "{\"temp\":%.1f,\"hum\":%.1f,\"press\":%.1f}",
                data.temperature, data.humidity, data.pressure);

        mqtt.publish("weather/station1", msg);
        Serial.println("Dati pubblicati");
    }
}

void setup() {
    Serial.begin(115200);

    // Init sensori
    dht.begin();
    if (!bmp.begin(0x76)) {
        Serial.println("BMP280 non trovato!");
    }

    // Init display
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("OLED non trovato!");
    }
    display.clearDisplay();
    display.display();

    // WiFi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi OK");

    // MQTT
    mqtt.setServer(mqtt_server, 1883);
}

void loop() {
    static unsigned long lastRead = 0;
    static unsigned long lastPublish = 0;

    unsigned long now = millis();

    // Leggi sensori ogni 2 sec
    if (now - lastRead >= 2000) {
        lastRead = now;
        readSensors();
        updateDisplay();
    }

    // Pubblica ogni 30 sec
    if (now - lastPublish >= 30000) {
        lastPublish = now;
        publishData();
    }

    // Mantieni connessione MQTT
    if (!mqtt.connected()) {
        // Riconnetti (codice omesso)
    }
    mqtt.loop();
}
```

### 14.2 Sistema Irrigazione Automatico

**Requisiti:**
- Rileva umidità suolo
- Attiva pompa se secco
- Safety: max 30 sec pompaggio
- Logging seriale + SD
- Controllo manuale con pulsante
- Display LCD stato

**(Codice completo nei materiali del corso)**

---

## 15. Debugging Hardware e Software

### 15.1 Debug Seriale Avanzato

**Macro Debug Condizionale:**
```cpp
#define DEBUG 1  // 1 = debug ON, 0 = OFF

#if DEBUG
  #define DEBUG_PRINT(x) Serial.print(x)
  #define DEBUG_PRINTLN(x) Serial.println(x)
#else
  #define DEBUG_PRINT(x)
  #define DEBUG_PRINTLN(x)
#endif

void loop() {
    int value = analogRead(A0);
    DEBUG_PRINT("Sensor: ");
    DEBUG_PRINTLN(value);

    // In produzione (DEBUG=0), nessun output seriale!
}
```

**Timestamp:**
```cpp
void log(String message) {
    unsigned long seconds = millis() / 1000;
    unsigned long minutes = seconds / 60;
    unsigned long hours = minutes / 60;

    Serial.print("[");
    Serial.print(hours % 24);
    Serial.print(":");
    Serial.print(minutes % 60);
    Serial.print(":");
    Serial.print(seconds % 60);
    Serial.print("] ");
    Serial.println(message);
}

void loop() {
    log("Lettura sensore...");
    int value = analogRead(A0);
    log("Valore: " + String(value));
}
```

### 15.2 LED Debug Pattern

**Codici Blink:**
```cpp
void errorBlink(int errorCode) {
    for (int i = 0; i < errorCode; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
    }
    delay(2000);
}

void loop() {
    if (!sensor.begin()) {
        errorBlink(3);  // 3 blink = errore sensore
        return;
    }

    if (!sd.begin()) {
        errorBlink(5);  // 5 blink = errore SD
        return;
    }

    // Codice normale...
}
```

### 15.3 Watchdog Timer

**Rileva e resetta sistema bloccato:**
```cpp
#include <avr/wdt.h>

void setup() {
    wdt_enable(WDTO_2S);  // Reset se bloccato > 2 sec
    Serial.begin(9600);
}

void loop() {
    wdt_reset();  // "Sono vivo!" - resetta timer

    // Codice normale
    doWork();

    // Se doWork() si blocca > 2 sec → watchdog resetta Arduino
}
```

### 15.4 Verifica Alimentazione

```cpp
// Leggi tensione alimentazione (AVR trick)
long readVcc() {
    long result;
    // Read 1.1V reference against AVcc
    ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
    delay(2);
    ADCSRA |= _BV(ADSC);
    while (bit_is_set(ADCSRA, ADSC));
    result = ADCL;
    result |= ADCH << 8;
    result = 1126400L / result; // Back-calculate AVcc in mV
    return result;
}

void setup() {
    Serial.begin(9600);
}

void loop() {
    long vcc = readVcc();
    Serial.print("VCC: ");
    Serial.print(vcc);
    Serial.println(" mV");

    if (vcc < 4500) {  // < 4.5V
        Serial.println("ATTENZIONE: Tensione bassa!");
    }

    delay(1000);
}
```

---

## 16. Best Practices Embedded

### 16.1 Gestione Memoria RAM

**Arduino Uno ha solo 2 KB RAM!**

**Evita String (usa char array):**
```cpp
// ❌ CATTIVO: String usa heap (frammentazione)
String message = "Sensor: ";
message += String(value);
message += " units";

// ✅ BUONO: char array su stack
char message[50];
snprintf(message, sizeof(message), "Sensor: %d units", value);
```

**Usa PROGMEM per costanti:**
```cpp
// ❌ CATTIVO: stringhe in RAM
const char text1[] = "Questa stringa molto lunga occupa RAM preziosa";
const char text2[] = "Anche questa occupa RAM";

// ✅ BUONO: stringhe in Flash (non RAM)
const char text1[] PROGMEM = "Questa stringa molto lunga è in Flash";
const char text2[] PROGMEM = "Anche questa è in Flash";

// Lettura da PROGMEM
char buffer[50];
strcpy_P(buffer, text1);  // Copia da PROGMEM a RAM
Serial.println(buffer);
```

**Verifica RAM Disponibile:**
```cpp
int freeRam() {
    extern int __heap_start, *__brkval;
    int v;
    return (int) &v - (__brkval == 0 ? (int) &__heap_start : (int) __brkval);
}

void setup() {
    Serial.begin(9600);
    Serial.print("RAM disponibile: ");
    Serial.print(freeRam());
    Serial.println(" byte");
}
```

### 16.2 Power Management

**Sleep Mode (batteria):**
```cpp
#include <avr/sleep.h>
#include <avr/power.h>

void enterSleep() {
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);  // Modalità massimo risparmio
    sleep_enable();

    // Disabilita periferiche non necessarie
    power_adc_disable();
    power_spi_disable();
    power_timer0_disable();
    power_timer1_disable();
    power_timer2_disable();
    power_twi_disable();

    sleep_mode();  // Dorme QUI

    // ===== RISVEGLIO (da interrupt) =====
    sleep_disable();

    // Riabilita periferiche
    power_all_enable();
}

void wakeUpISR() {
    // ISR vuota, solo per risveglio
}

void setup() {
    pinMode(2, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(2), wakeUpISR, LOW);
}

void loop() {
    // Lavoro
    doWork();

    // Dormi per risparmiare batteria
    enterSleep();
}
```

**Consumo Tipico:**
```
Arduino Uno:
  Normale: ~45 mA
  Sleep Power-Down: ~6 mA (con regolatore)
  Sleep Deep + regolatore rimosso: <1 mA

ESP32:
  Attivo: ~160 mA (WiFi ON)
  Modem sleep: ~20 mA
  Light sleep: ~0.8 mA
  Deep sleep: ~10 μA
```

### 16.3 Codice Non-Bloccante

```cpp
// ❌ BLOCCANTE: sistema morto durante delay
void loop() {
    readSensor();
    delay(5000);  // 5 secondi bloccato
    sendData();
    delay(5000);  // Altri 5 secondi bloccato
}

// ✅ NON-BLOCCANTE: sistema reattivo
unsigned long lastSensorRead = 0;
unsigned long lastDataSend = 0;

const unsigned long SENSOR_INTERVAL = 5000;
const unsigned long SEND_INTERVAL = 5000;

void loop() {
    unsigned long now = millis();

    // Task 1: Leggi sensore ogni 5 sec
    if (now - lastSensorRead >= SENSOR_INTERVAL) {
        lastSensorRead = now;
        readSensor();
    }

    // Task 2: Invia dati ogni 5 sec
    if (now - lastDataSend >= SEND_INTERVAL) {
        lastDataSend = now;
        sendData();
    }

    // Sistema può fare altro!
    checkButtons();
    updateDisplay();
}
```

### 16.4 Error Handling Robusto

```cpp
enum ErrorCode {
    ERR_OK = 0,
    ERR_SENSOR_INIT,
    ERR_SENSOR_READ,
    ERR_WIFI_CONNECT,
    ERR_SD_INIT
};

ErrorCode lastError = ERR_OK;

ErrorCode initSensors() {
    if (!dht.begin()) {
        return ERR_SENSOR_INIT;
    }

    if (!bmp.begin()) {
        return ERR_SENSOR_INIT;
    }

    return ERR_OK;
}

ErrorCode readSensorData(float *temp, float *hum) {
    *temp = dht.readTemperature();
    *hum = dht.readHumidity();

    if (isnan(*temp) || isnan(*hum)) {
        return ERR_SENSOR_READ;
    }

    return ERR_OK;
}

void setup() {
    Serial.begin(9600);

    lastError = initSensors();
    if (lastError != ERR_OK) {
        Serial.print("ERRORE INIT: ");
        Serial.println(lastError);
        while (1) {
            errorBlink(lastError);  // Blink codice errore
        }
    }

    Serial.println("Sistema OK");
}

void loop() {
    float temp, hum;

    ErrorCode err = readSensorData(&temp, &hum);
    if (err != ERR_OK) {
        Serial.print("Errore lettura: ");
        Serial.println(err);
        return;  // Skip questo ciclo
    }

    // Processa dati validi
    Serial.print("Temp: ");
    Serial.println(temp);
}
```

---

## 17. TinyML: Machine Learning su Arduino

### 17.1 Cos'è TinyML

**TinyML = Machine Learning su microcontrollori**

```
Modello AI tradizionale:
  Sensore → Cloud (via WiFi) → Server ML (GPU) → Risultato → Device
  Latenza: 100-1000ms
  Richiede connessione internet

TinyML:
  Sensore → MCU (inferenza on-device) → Risultato
  Latenza: <10ms
  NO internet necessario
  Privacy: dati non escono dal device
```

**Applicazioni:**
- Riconoscimento gesti (accelerometro)
- Keyword spotting (audio "OK Arduino")
- Anomaly detection (vibrazioni motore)
- Predictive maintenance

**Limitazioni:**
- Solo inferenza (no training su device)
- Modelli piccoli (quantized, pruned)
- Precisione ridotta vs cloud

### 17.2 TensorFlow Lite Micro

**Workflow:**
```
1. TRAINING (su PC con Python/TensorFlow):
   - Raccogli dataset
   - Addestra modello
   - Converti a TFLite
   - Quantizza (float32 → int8)

2. DEPLOYMENT (su Arduino):
   - Converti modello a C array
   - Include in sketch
   - Run inferenza
```

**Esempio: Riconoscimento Gesto "Sine Wave"**

```cpp
#include <TensorFlowLite.h>
#include <tensorflow/lite/micro/all_ops_resolver.h>
#include <tensorflow/lite/micro/micro_interpreter.h>
#include <tensorflow/lite/schema/schema_generated.h>

// Modello (generato da script Python)
#include "sine_model.h"

const int kTensorArenaSize = 2 * 1024;  // 2 KB
byte tensor_arena[kTensorArenaSize];

tflite::MicroInterpreter* interpreter = nullptr;

void setup() {
    Serial.begin(9600);

    // Carica modello
    const tflite::Model* model = tflite::GetModel(sine_model);

    // Inizializza interpreter
    static tflite::MicroMutableOpResolver<1> resolver;
    resolver.AddFullyConnected();

    static tflite::MicroInterpreter static_interpreter(
        model, resolver, tensor_arena, kTensorArenaSize);
    interpreter = &static_interpreter;

    interpreter->AllocateTensors();

    Serial.println("TinyML ready");
}

void loop() {
    // Input: valore 0-2π
    float input_value = (millis() % 6280) / 1000.0;  // 0-6.28

    // Scrivi input tensor
    interpreter->input(0)->data.f[0] = input_value;

    // Esegui inferenza
    interpreter->Invoke();

    // Leggi output (predicted sine value)
    float output = interpreter->output(0)->data.f[0];

    // Confronta con valore reale
    float real_sine = sin(input_value);

    Serial.print("Input: ");
    Serial.print(input_value);
    Serial.print(" | Predicted: ");
    Serial.print(output);
    Serial.print(" | Real: ");
    Serial.println(real_sine);

    delay(100);
}
```

**(Esempio semplificato - corso completo su TinyML nei materiali avanzati)**

---

## 18. Esercizi Pratici

### Esercizio 1: Semaforo
Implementa semaforo 3 LED (rosso, giallo, verde) con temporizzazioni realistiche.

### Esercizio 2: Termostato
Sistema che controlla riscaldamento: leggi temperatura, attiva relay se < setpoint.

### Esercizio 3: Parcheggio Smart
Sensore ultrasuoni rileva auto, display LCD mostra "Libero" / "Occupato".

### Esercizio 4: Logger SD
Registra temperatura su SD card ogni minuto con timestamp.

### Esercizio 5: Allarme Wireless
ESP32 invia notifica MQTT quando pulsante (finestra) viene aperto.

---

## ✅ Checklist Completamento Modulo

- [ ] Configuro correttamente pin Arduino/ESP32
- [ ] Implemento debouncing pulsanti professionale
- [ ] Uso millis() invece di delay() per logica non-bloccante
- [ ] Gestisco comunicazione seriale avanzata (parsing comandi)
- [ ] Integro sensori comuni (DHT, HC-SR04, etc.)
- [ ] Uso display LCD/OLED per interfaccia utente
- [ ] Implemento interrupt appropriatamente (con volatile)
- [ ] Comprendo differenze I2C vs SPI
- [ ] Connetto ESP32 a WiFi e creo web server
- [ ] Pubblico dati IoT con MQTT
- [ ] Debug efficacemente con seriale e LED patterns
- [ ] Gestisco memoria RAM in modo efficiente
- [ ] Applico best practices embedded (non-bloccante, error handling)
- [ ] Ho completato almeno 3 progetti completi

---

**Fine Modulo 4**

*Prossimo: Modulo 5 - Applicazioni Pratiche e Progetti Avanzati*

---

**Versione:** 3.0 | **Aggiornamento:** Gennaio 2025 | **Corso ITS - IA e Programmazione Assistita**
