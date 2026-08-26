# 📘 DISPENSA COMPLETA - MODULO 4
# Programmazione Arduino con Supporto di Intelligenza Artificiale
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 3 ore | Livello: Intermedio-Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti Arduino](#2-fondamenti-arduino)
3. [Architettura e Hardware](#3-architettura-e-hardware)
4. [Struttura Sketch Arduino](#4-struttura-sketch-arduino)
5. [Gestione Pin](#5-gestione-pin)
6. [Temporizzazione: delay vs millis](#6-temporizzazione-delay-vs-millis)
7. [Comunicazione Seriale](#7-comunicazione-seriale)
8. [Sensori Analogici](#8-sensori-analogici)
9. [Attuatori e PWM](#9-attuatori-e-pwm)
10. [Prompt Tecnici per Arduino](#10-prompt-tecnici-per-arduino)
11. [Errori Comuni Generati da IA](#11-errori-comuni-generati-da-ia)
12. [Debugging Arduino](#12-debugging-arduino)
13. [Progetti Completi Guidati](#13-progetti-completi-guidati)
14. [Librerie e Moduli](#14-librerie-e-moduli)
15. [Best Practices Embedded](#15-best-practices-embedded)

---

## 1. Introduzione e Obiettivi

### 1.1 Benvenuti al Modulo Arduino

Il **Modulo 4** applica tutto ciò che hai imparato nei moduli precedenti al mondo **embedded** con Arduino. Arduino è una piattaforma fondamentale per prototipazione rapida, IoT, automazione e sistemi embedded didattici.

L'IA può accelerare enormemente lo sviluppo Arduino, ma presenta sfide specifiche:
- Hardware specifico (pin, tensioni, correnti)
- Temporizzazione critica
- Risorse limitate (memoria)
- Librerie hardware-dipendenti

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Generare** sketch Arduino funzionanti con supporto IA  
✅ **Gestire** temporizzazione non-bloccante con `millis()`  
✅ **Interfacciare** sensori analogici e digitali  
✅ **Controllare** attuatori (LED, motori, servo)  
✅ **Debuggare** via seriale efficacemente  
✅ **Validare** cablaggi e schemi circuitali  
✅ **Ottimizzare** codice per risorse limitate  
✅ **Integrare** librerie hardware comuni  
✅ **Progettare** sistemi embedded completi  

### 1.3 Prerequisiti

- Moduli 1, 2, 3 completati
- Conoscenze base elettronica (tensione, corrente, resistenza)
- Arduino IDE installato
- Board Arduino (Uno o compatibile)
- Kit componenti base (LED, resistenze, pulsanti, sensori)
- Cavi jumper e breadboard

### 1.4 Materiale Hardware Necessario

```
KIT MINIMO:
□ Arduino Uno (o Nano/Mega)
□ Cavo USB
□ Breadboard
□ LED (vari colori) + resistenze 220Ω-330Ω
□ Pulsanti + resistenze 10kΩ (pull-up/down)
□ Potenziometro 10kΩ
□ Sensore temperatura TMP36 o DHT11
□ Fotoresistenza (LDR) + resistenza 10kΩ
□ Buzzer piezo
□ Servo motore (opzionale)
□ Cavi jumper M-M, M-F

KIT AVANZATO (opzionale):
□ Display LCD 16x2 I2C
□ Sensore ultrasuoni HC-SR04
□ Modulo LED RGB
□ Motore DC + driver L293D
□ Sensore PIR
```

### 1.5 Setup Ambiente di Sviluppo

```
1. INSTALLA ARDUINO IDE
   Download: https://www.arduino.cc/en/software
   Versione raccomandata: 2.x

2. CONFIGURA BOARD
   Tools → Board → Arduino AVR Boards → Arduino Uno

3. SELEZIONA PORTA
   Tools → Port → [COMx (Windows) o /dev/ttyUSBx (Linux)]

4. TEST CONNESSIONE
   File → Examples → 01.Basics → Blink
   Upload → LED onboard deve lampeggiare

5. INSTALLA LIBRERIE UTILI (opzionale)
   Tools → Manage Libraries:
   - DHT sensor library
   - Servo
   - LiquidCrystal_I2C
```

---

## 2. Fondamenti Arduino

### 2.1 Cos'è Arduino

> **Arduino**: Piattaforma open-source hardware/software per prototipazione elettronica rapida, basata su microcontrollore AVR (tipicamente ATmega328P su Uno).

**Caratteristiche Chiave:**
- Microcontrollore 8-bit
- Clock 16 MHz
- Memoria Flash 32KB (programma)
- SRAM 2KB (variabili runtime)
- EEPROM 1KB (storage persistente)
- 14 pin digitali I/O (6 PWM)
- 6 pin analogici input (ADC 10-bit)
- Tensione operativa: 5V
- Corrente max per pin: 40mA (20mA raccomandato)

### 2.2 Filosofia Arduino

```
PRINCIPI DESIGN ARDUINO:

1. SEMPLICITÀ
   - Setup e loop invece di main complesso
   - Funzioni high-level (digitalWrite, analogRead)
   - Astrazione hardware

2. PORTABILITÀ
   - Stesso codice su board diverse (con adattamenti)
   - Librerie standardizzate

3. OPEN SOURCE
   - Hardware schemi aperti
   - Software open
   - Community enorme

4. EDUCATIONAL
   - Ideale per imparare embedded
   - Documentazione estesa
   - Esempi abbondanti
```

### 2.3 Arduino IDE vs Linguaggio

```cpp
/*
 * CHIARIMENTO: "Linguaggio Arduino"
 * 
 * NON esiste un linguaggio "Arduino"!
 * Arduino usa C/C++ standard con:
 * - Framework Wiring (funzioni setup/loop)
 * - Librerie Arduino core
 * - Preprocessing automatico
 */

// Questo è C++ puro:
int ledPin = 13;

void setup() {
    pinMode(ledPin, OUTPUT);
}

void loop() {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
}

// Il preprocessor Arduino aggiunge automaticamente:
// #include <Arduino.h>
// int main() { init(); setup(); while(1) loop(); }
```

### 2.4 Ciclo di Vita Sketch

```
BOOT SEQUENCE:
┌─────────────────────────────────┐
│ 1. POWER ON / RESET             │
├─────────────────────────────────┤
│ 2. Bootloader (primi ~2 secondi)│
│    Attende upload o timeout     │
├─────────────────────────────────┤
│ 3. init() [Arduino core]        │
│    Inizializza hardware base    │
├─────────────────────────────────┤
│ 4. setup()  [TUO CODICE]        │
│    Eseguito UNA sola volta      │
│    Inizializza pin, seriale, ecc│
├─────────────────────────────────┤
│ 5. loop()   [TUO CODICE]        │
│    Eseguito INFINITAMENTE       │
│    ┌──────────────────┐         │
│    │ loop()           │         │
│    │   ↓              │         │
│    │ loop()           │         │
│    │   ↓              │         │
│    │ loop()           │         │
│    │   ↓              │         │
│    │ ...              │         │
│    └──────────────────┘         │
└─────────────────────────────────┘

IMPORTANTE: loop() viene chiamato continuamente,
NON c'è pausa automatica tra esecuzioni!
```

---

## 3. Architettura e Hardware

### 3.1 Pinout Arduino Uno

```
         ARDUINO UNO REV3
    ┌─────────────────────────┐
    │ ○ ○              RESET  │
    │ ○ ○              3.3V   │
    │ ○ ○              5V     │
    │ ○ ○              GND    │
    │ ○ ○              GND    │
    │ ○ ○              Vin    │
    │                         │
    │ A0 ○  ○ AREF            │
    │ A1 ○  ○ GND             │
    │ A2 ○  ○ 13   (LED, SCK) │
    │ A3 ○  ○ 12   (MISO)     │
    │ A4 ○  ○ ~11  (PWM, MOSI)│
    │ A5 ○  ○ ~10  (PWM, SS)  │
    │       ○ ~9   (PWM)      │
    │ 0  ○  ○ 8               │
    │ 1  ○  ○ 7               │
    │ 2  ○  ○ ~6   (PWM)      │
    │ ~3 ○  ○ ~5   (PWM)      │
    │ 4  ○  ○ 4               │
    └─────────────────────────┘
    
LEGENDA:
~ = PWM capable
0,1 = Serial (TX/RX)
13 = LED onboard
A0-A5 = Analog input (usabili come digital)
```

### 3.2 Specifiche Elettriche

```
TENSIONI:
┌─────────────────────────────────┐
│ Vcc:        5V (regolato)       │
│ Vin:        7-12V (raccomandato)│
│             6-20V (limiti)      │
│ 3.3V out:   50mA max            │
│ 5V out:     Dipende da fonte    │
│             - USB: 500mA        │
│             - Barrel: ~1A       │
│ Pin I/O:    0V (LOW) / 5V (HIGH)│
└─────────────────────────────────┘

CORRENTI:
┌─────────────────────────────────┐
│ Per pin:    40mA ASSOLUTO MAX   │
│             20mA RACCOMANDATO   │
│ Tutti pin:  200mA totale max    │
│ GND pin:    800mA max sink      │
└─────────────────────────────────┘

⚠️ ATTENZIONE: Superare questi limiti
   danneggia permanentemente il chip!
```

### 3.3 Memoria

```
ATMEGA328P (Arduino Uno):
┌────────────────────────────────┐
│ FLASH:   32 KB                 │
│          - 0.5KB bootloader    │
│          - 31.5KB disponibili  │
│          → Codice programma    │
│          → Costanti (PROGMEM)  │
├────────────────────────────────┤
│ SRAM:    2 KB                  │
│          → Variabili globali   │
│          → Variabili locali    │
│          → Stack               │
│          ⚠️ MOLTO LIMITATA!    │
├────────────────────────────────┤
│ EEPROM:  1 KB                  │
│          → Storage persistente │
│          → Sopravvive a reset  │
│          → Scritture limitate  │
│            (~100k cicli)       │
└────────────────────────────────┘

OTTIMIZZAZIONE SRAM:
// ❌ String occupa SRAM dinamicamente
String msg = "Hello World";

// ✅ PROGMEM: mantiene in Flash
const char msg[] PROGMEM = "Hello World";

// ✅ F() macro (per Serial.print)
Serial.println(F("Hello World"));
```

---

## 4. Struttura Sketch Arduino

### 4.1 Sketch Minimale

```cpp
/*
 * SKETCH MINIMO ARDUINO
 */

// Setup: eseguito UNA volta all'avvio
void setup() {
    // Inizializzazione qui
}

// Loop: eseguito INFINITAMENTE
void loop() {
    // Codice principale qui
}
```

### 4.2 Anatomia Sketch Completo

```cpp
/*
 * SKETCH COMPLETO ANNOTATO
 */

// === INCLUDES ===
#include <Wire.h>      // Librerie esterne

// === DEFINIZIONI COSTANTI ===
#define LED_PIN 13
#define BUTTON_PIN 2

// === COSTANTI ===
const int THRESHOLD = 100;
const unsigned long INTERVAL = 1000;  // ms

// === VARIABILI GLOBALI ===
int sensorValue = 0;
unsigned long previousMillis = 0;
bool ledState = false;

// === PROTOTIPI FUNZIONI (opzionali) ===
void blinkLED(void);
int readSensorWithFilter(void);

// === SETUP ===
void setup() {
    // 1. Inizializza seriale
    Serial.begin(9600);
    Serial.println(F("Sistema inizializzato"));
    
    // 2. Configura pin
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    
    // 3. Inizializza librerie
    Wire.begin();
    
    // 4. Setup iniziale
    digitalWrite(LED_PIN, LOW);
    
    // 5. Delay iniziale (opzionale)
    delay(100);
}

// === LOOP ===
void loop() {
    // Logica non-bloccante con millis()
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= INTERVAL) {
        previousMillis = currentMillis;
        
        // Azione periodica
        blinkLED();
    }
    
    // Lettura sensori
    sensorValue = analogRead(A0);
    
    // Logica condizionale
    if (sensorValue > THRESHOLD) {
        handleHighValue();
    }
    
    // NO delay() qui! (blocca tutto)
}

// === FUNZIONI AUSILIARIE ===
void blinkLED(void) {
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
}

void handleHighValue(void) {
    Serial.print(F("Valore alto: "));
    Serial.println(sensorValue);
}

int readSensorWithFilter(void) {
    // Media di 10 letture
    long sum = 0;
    for (int i = 0; i < 10; i++) {
        sum += analogRead(A0);
        delay(1);  // Piccolo delay OK qui
    }
    return sum / 10;
}
```

### 4.3 Buone Pratiche Struttura

```cpp
/*
 * ORGANIZZAZIONE CODICE ARDUINO
 */

// ✅ FARE:
// 1. Usare #define o const per pin
#define LED_PIN 13
const int BUTTON_PIN = 2;

// 2. Nomi descrittivi
unsigned long lastBlinkTime = 0;  // ✅ Chiaro
// NO: unsigned long t = 0;        // ❌ Criptico

// 3. Commenti per sezioni
// === SETUP HARDWARE ===
// === LOOP PRINCIPALE ===
// === FUNZIONI HELPER ===

// 4. Funzioni brevi e focused
void updateDisplay(void);      // Una sola responsabilità
void readAllSensors(void);

// 5. Evita codice duplicato
void setLED(int pin, bool state) {
    digitalWrite(pin, state ? HIGH : LOW);
}

// ❌ NON FARE:
// 1. Variabili globali eccessive
// 2. loop() con 500 righe di codice
// 3. delay() lunghi in loop
// 4. Blocking I/O operations
// 5. Ricorsione (stack piccolo!)
```

---

## 5. Gestione Pin

### 5.1 Pin Digitali

```cpp
/*
 * PIN DIGITALI - I/O
 */

void digital_pin_basics() {
    // === CONFIGURAZIONE ===
    
    // Output: LED, relè, motori
    pinMode(13, OUTPUT);
    
    // Input: pulsanti, sensori digitali
    pinMode(2, INPUT);
    
    // Input con pull-up interno (~20kΩ)
    pinMode(3, INPUT_PULLUP);
    // Equivale a avere resistenza pull-up esterna
    // Pulsante connesso tra pin e GND
    
    // === SCRITTURA (output) ===
    digitalWrite(13, HIGH);  // 5V
    digitalWrite(13, LOW);   // 0V
    
    // === LETTURA (input) ===
    int buttonState = digitalRead(2);
    if (buttonState == HIGH) {
        // Pulsante premuto (se pull-down)
    }
    
    // Con INPUT_PULLUP: logica invertita!
    int btn = digitalRead(3);
    if (btn == LOW) {  // LOW quando premuto!
        // Pulsante premuto
    }
}
```

### 5.2 Esempio Completo: LED e Pulsante

```cpp
/*
 * LED CONTROLLATO DA PULSANTE
 * Hardware:
 * - LED su pin 13 (con resistenza 220Ω a GND)
 * - Pulsante su pin 2 (con pull-up interno)
 */

const int LED_PIN = 13;
const int BUTTON_PIN = 2;

bool ledState = false;
bool lastButtonState = HIGH;  // Pull-up: HIGH quando non premuto
unsigned long lastDebounceTime = 0;
const unsigned long DEBOUNCE_DELAY = 50;  // ms

void setup() {
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    digitalWrite(LED_PIN, LOW);
}

void loop() {
    // Leggi stato pulsante
    bool reading = digitalRead(BUTTON_PIN);
    
    // Debouncing: ignora oscillazioni nei primi 50ms
    if (reading != lastButtonState) {
        lastDebounceTime = millis();
    }
    
    if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
        // Stato stabile: controlla se cambiato
        static bool buttonState = HIGH;
        
        if (reading != buttonState) {
            buttonState = reading;
            
            // Rileva fronte di discesa (pressione)
            if (buttonState == LOW) {
                // Toggle LED
                ledState = !ledState;
                digitalWrite(LED_PIN, ledState);
            }
        }
    }
    
    lastButtonState = reading;
}
```

### 5.3 Pin Analogici Input

```cpp
/*
 * LETTURA ANALOGICA (ADC 10-bit)
 */

void analog_input_basics() {
    // ADC: 0V → 0, 5V → 1023 (10-bit resolution)
    
    // Lettura semplice
    int value = analogRead(A0);  // Range: 0-1023
    
    // Conversione a tensione
    float voltage = value * (5.0 / 1023.0);
    
    // Conversione a percentuale
    float percent = (value / 1023.0) * 100.0;
}

/*
 * ESEMPIO: POTENZIOMETRO
 * Hardware: Potenziometro 10kΩ
 * - Pin centrale → A0
 * - Pin laterali → 5V e GND
 */

const int POT_PIN = A0;

void setup() {
    Serial.begin(9600);
    // Nessun pinMode necessario per analog input
}

void loop() {
    int rawValue = analogRead(POT_PIN);
    
    // Converti in tensione
    float voltage = rawValue * (5.0 / 1023.0);
    
    // Output su seriale
    Serial.print("Raw: ");
    Serial.print(rawValue);
    Serial.print(" | Voltage: ");
    Serial.print(voltage, 2);  // 2 decimali
    Serial.println("V");
    
    delay(500);  // OK in questo semplice esempio
}
```

### 5.4 PWM (Analog Output)

```cpp
/*
 * PWM - PULSE WIDTH MODULATION
 * Simula output analogico modulando duty cycle
 * 
 * Pin PWM su Uno: 3, 5, 6, 9, 10, 11 (marcati ~)
 * Frequenza: ~490Hz (pin 3,9,10,11) o ~980Hz (5,6)
 * Risoluzione: 8-bit (0-255)
 */

void pwm_basics() {
    // Configura come output
    pinMode(9, OUTPUT);
    
    // Scrivi valore PWM (0-255)
    analogWrite(9, 127);  // 50% duty cycle
    analogWrite(9, 255);  // 100% duty cycle (sempre HIGH)
    analogWrite(9, 0);    // 0% duty cycle (sempre LOW)
}

/*
 * ESEMPIO: FADE LED
 * Hardware: LED su pin 9 con resistenza 220Ω
 */

const int LED_PIN = 9;

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    // Fade in
    for (int brightness = 0; brightness <= 255; brightness++) {
        analogWrite(LED_PIN, brightness);
        delay(5);
    }
    
    // Fade out
    for (int brightness = 255; brightness >= 0; brightness--) {
        analogWrite(LED_PIN, brightness);
        delay(5);
    }
}
```

---

## 6. Temporizzazione: delay vs millis

### 6.1 Problema con delay()

```cpp
/*
 * PERCHÉ delay() È PROBLEMATICO
 */

// ❌ CODICE BLOCCANTE
void loop() {
    digitalWrite(LED1, HIGH);
    delay(1000);  // ⚠️ Arduino BLOCCATO per 1 secondo!
                  // Non può fare nient'altro:
                  // - Non legge sensori
                  // - Non risponde a pulsanti
                  // - Non comunica su seriale
    digitalWrite(LED1, LOW);
    delay(1000);
}

// Esempio scenario problematico:
void loop() {
    // Voglio:
    // - LED1 lampeggia ogni 1 secondo
    // - LED2 lampeggia ogni 500ms
    // - Leggere pulsante istantaneamente
    
    // Con delay(): IMPOSSIBILE!
    digitalWrite(LED1, HIGH);
    delay(1000);
    digitalWrite(LED1, LOW);
    // Durante questi 2 secondi, LED2 e pulsante ignorati!
}
```

### 6.2 Soluzione: millis()

```cpp
/*
 * millis() - NON BLOCCANTE
 * 
 * millis() ritorna millisecondi da avvio board
 * Tipo: unsigned long (32-bit)
 * Overflow dopo: ~49 giorni
 */

unsigned long currentMillis = millis();
// currentMillis = 1234567  (esempio)

// PATTERN BASE:
unsigned long previousMillis = 0;
const unsigned long INTERVAL = 1000;  // ms

void loop() {
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= INTERVAL) {
        previousMillis = currentMillis;
        
        // Azione periodica qui
        doSomething();
    }
    
    // Il resto del loop continua a girare!
    checkButton();
    readSensors();
}
```

### 6.3 Esempio: Blink Non-Bloccante

```cpp
/*
 * BLINK NON-BLOCCANTE
 */

const int LED_PIN = 13;
const unsigned long BLINK_INTERVAL = 1000;  // ms

unsigned long previousMillis = 0;
bool ledState = false;

void setup() {
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();
    
    // Check se è tempo di cambiare stato
    if (currentMillis - previousMillis >= BLINK_INTERVAL) {
        previousMillis = currentMillis;
        
        // Toggle LED
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }
    
    // Loop continua immediatamente!
    // Posso fare altre cose qui
}
```

### 6.4 Multi-Timer Pattern

```cpp
/*
 * GESTIONE MULTIPLI TIMER INDIPENDENTI
 */

const int LED1_PIN = 12;
const int LED2_PIN = 11;
const int LED3_PIN = 10;

// Timer indipendenti per ogni LED
unsigned long led1_previousMillis = 0;
unsigned long led2_previousMillis = 0;
unsigned long led3_previousMillis = 0;

// Intervalli diversi
const unsigned long LED1_INTERVAL = 1000;   // 1 secondo
const unsigned long LED2_INTERVAL = 500;    // 0.5 secondi
const unsigned long LED3_INTERVAL = 250;    // 0.25 secondi

bool led1_state = false;
bool led2_state = false;
bool led3_state = false;

void setup() {
    pinMode(LED1_PIN, OUTPUT);
    pinMode(LED2_PIN, OUTPUT);
    pinMode(LED3_PIN, OUTPUT);
}

void loop() {
    unsigned long currentMillis = millis();
    
    // Timer LED1
    if (currentMillis - led1_previousMillis >= LED1_INTERVAL) {
        led1_previousMillis = currentMillis;
        led1_state = !led1_state;
        digitalWrite(LED1_PIN, led1_state);
    }
    
    // Timer LED2
    if (currentMillis - led2_previousMillis >= LED2_INTERVAL) {
        led2_previousMillis = currentMillis;
        led2_state = !led2_state;
        digitalWrite(LED2_PIN, led2_state);
    }
    
    // Timer LED3
    if (currentMillis - led3_previousMillis >= LED3_INTERVAL) {
        led3_previousMillis = currentMillis;
        led3_state = !led3_state;
        digitalWrite(LED3_PIN, led3_state);
    }
    
    // Tutti e 3 i LED lampeggiano indipendentemente!
}
```

### 6.5 Gestione Overflow millis()

```cpp
/*
 * GESTIONE OVERFLOW DI millis()
 * 
 * millis() overflow dopo ~49 giorni (2^32 ms)
 * Il pattern (currentMillis - previousMillis) 
 * gestisce AUTOMATICAMENTE l'overflow!
 */

void loop() {
    unsigned long currentMillis = millis();
    
    // Questo funziona ANCHE con overflow!
    if (currentMillis - previousMillis >= INTERVAL) {
        // Esempio numerico overflow:
        // previousMillis = 4294967290 (quasi overflow)
        // currentMillis  = 10 (dopo overflow)
        // Differenza = 10 - 4294967290 = 
        //   (su unsigned) = 16 ms ✅ CORRETTO!
        
        previousMillis = currentMillis;
        // ...
    }
}

// ❌ SBAGLIATO (non gestisce overflow):
if (millis() >= previousMillis + INTERVAL) {
    // Questo FALLISCE dopo overflow!
}
```

---

## 7. Comunicazione Seriale

### 7.1 Serial Basics

```cpp
/*
 * COMUNICAZIONE SERIALE - DEBUGGING PRINCIPALE
 */

void setup() {
    // Inizializza seriale
    Serial.begin(9600);  // Baud rate: 9600 bps
    // Altri comuni: 115200, 57600, 38400, 19200
    
    // Attendi connessione (opzionale, utile per Leonardo/Micro)
    while (!Serial) {
        ; // Aspetta porta seriale
    }
    
    Serial.println(F("Sistema inizializzato!"));
}

void loop() {
    // === OUTPUT ===
    
    // Print senza newline
    Serial.print("Valore: ");
    Serial.print(123);
    
    // Print con newline
    Serial.println(" ms");
    
    // Print formattato
    int value = 42;
    Serial.print("Dec: "); Serial.println(value);      // Decimale
    Serial.print("Hex: "); Serial.println(value, HEX); // Esadecimale
    Serial.print("Bin: "); Serial.println(value, BIN); // Binario
    
    float pi = 3.14159;
    Serial.println(pi, 2);  // 2 decimali: 3.14
    
    // === INPUT ===
    
    // Check se dati disponibili
    if (Serial.available() > 0) {
        // Leggi singolo byte
        int inByte = Serial.read();
        
        // Echo back
        Serial.write(inByte);
        
        // Oppure leggi stringa completa
        String input = Serial.readString();
        Serial.print("Ricevuto: ");
        Serial.println(input);
    }
    
    delay(100);
}
```

### 7.2 Debugging Avanzato con Serial

```cpp
/*
 * TECNICHE DEBUGGING SERIALE
 */

// === MACRO DEBUG ===
#define DEBUG 1  // Imposta 0 per disabilitare debug

#if DEBUG
  #define DEBUG_PRINT(x) Serial.print(x)
  #define DEBUG_PRINTLN(x) Serial.println(x)
#else
  #define DEBUG_PRINT(x)
  #define DEBUG_PRINTLN(x)
#endif

void setup() {
    Serial.begin(115200);  // Baud rate alto per debug
}

void loop() {
    int sensor = analogRead(A0);
    
    // Debug condizionale
    DEBUG_PRINT("Sensor: ");
    DEBUG_PRINTLN(sensor);
    
    // Compilato solo se DEBUG=1, altrimenti rimosso!
}

// === SERIAL PLOTTER ===
// Arduino IDE: Tools → Serial Plotter
// Formato: valori separati da spazio o tab, newline alla fine

void loop_plotter() {
    int sensor1 = analogRead(A0);
    int sensor2 = analogRead(A1);
    
    // Formato per plotter
    Serial.print(sensor1);
    Serial.print(" ");
    Serial.println(sensor2);
    
    delay(50);  // ~20 campioni/sec
}

// === TIMESTAMPING ===
void logEvent(const char* message) {
    Serial.print("[");
    Serial.print(millis());
    Serial.print("ms] ");
    Serial.println(message);
}

// === FORMATO CSV PER LOG ===
void logData(int value1, float value2, bool state) {
    Serial.print(millis());
    Serial.print(",");
    Serial.print(value1);
    Serial.print(",");
    Serial.print(value2, 2);
    Serial.print(",");
    Serial.println(state);
}
```

### 7.3 Parsing Input Seriale

```cpp
/*
 * PARSING COMANDI SERIALI
 */

void processSerialCommand() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();  // Rimuovi whitespace
        
        if (command == "ON") {
            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED ON");
        } 
        else if (command == "OFF") {
            digitalWrite(LED_PIN, LOW);
            Serial.println("LED OFF");
        }
        else if (command.startsWith("SET ")) {
            // Comando: "SET 128"
            int value = command.substring(4).toInt();
            analogWrite(PWM_PIN, value);
            Serial.print("PWM set to: ");
            Serial.println(value);
        }
        else {
            Serial.println("Unknown command");
        }
    }
}

// === PARSING NUMERICO ===
void parseNumericInput() {
    if (Serial.available() > 0) {
        // parseInt() legge fino a carattere non-numerico
        int number = Serial.parseInt();
        
        // Consuma resto fino a newline
        Serial.read();  
        
        Serial.print("Ricevuto numero: ");
        Serial.println(number);
    }
}
```

---

## 8. Sensori Analogici

### 8.1 Sensore di Temperatura TMP36

```cpp
/*
 * SENSORE TEMPERATURA TMP36
 * 
 * Pinout TMP36:
 * [Flat side facing you]
 * Pin 1: Vcc (5V)
 * Pin 2: Vout (segnale)
 * Pin 3: GND
 * 
 * Formula: T(°C) = (Vout - 0.5) * 100
 * Range: -40°C a +125°C
 * Risoluzione: 10mV per °C
 */

const int TEMP_PIN = A0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    // Leggi ADC
    int rawValue = analogRead(TEMP_PIN);
    
    // Converti in tensione
    float voltage = rawValue * (5.0 / 1023.0);
    
    // Converti in temperatura
    float temperatureC = (voltage - 0.5) * 100.0;
    float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
    
    // Output
    Serial.print("Raw: "); Serial.print(rawValue);
    Serial.print(" | V: "); Serial.print(voltage, 3);
    Serial.print(" | Temp: "); Serial.print(temperatureC, 1);
    Serial.println(" C");
    
    delay(1000);
}
```

### 8.2 Fotoresistenza (LDR)

```cpp
/*
 * FOTORESISTENZA (Light Dependent Resistor)
 * 
 * Circuito: Voltage Divider
 *     5V
 *      |
 *    [LDR]
 *      |----→ A0
 *    [10kΩ]
 *      |
 *     GND
 * 
 * Luminoso: LDR ~1kΩ  → Tensione alta
 * Buio:     LDR ~100kΩ → Tensione bassa
 */

const int LDR_PIN = A0;
const int LED_PIN = 13;
const int THRESHOLD = 500;  // Soglia buio/luce

void setup() {
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    int lightLevel = analogRead(LDR_PIN);
    
    // Accendi LED se buio
    if (lightLevel < THRESHOLD) {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("BUIO - LED ON");
    } else {
        digitalWrite(LED_PIN, LOW);
        Serial.print("LUCE - ");
        Serial.println(lightLevel);
    }
    
    delay(200);
}
```

### 8.3 Filtraggio e Calibrazione

```cpp
/*
 * TECNICHE FILTRAGGIO SENSORI
 */

// === MEDIA MOBILE (Moving Average) ===
const int NUM_READINGS = 10;
int readings[NUM_READINGS];
int readIndex = 0;
int total = 0;

int readSensorFiltered(int pin) {
    // Rimuovi lettura vecchia
    total -= readings[readIndex];
    
    // Leggi nuovo valore
    readings[readIndex] = analogRead(pin);
    
    // Aggiungi al totale
    total += readings[readIndex];
    
    // Avanza indice (circular buffer)
    readIndex = (readIndex + 1) % NUM_READINGS;
    
    // Ritorna media
    return total / NUM_READINGS;
}

// === FILTRO ESPONENZIALE (EMA) ===
float filteredValue = 0;
const float ALPHA = 0.1;  // 0-1, più basso = più smooth

float readSensorEMA(int pin) {
    int rawValue = analogRead(pin);
    filteredValue = (ALPHA * rawValue) + ((1 - ALPHA) * filteredValue);
    return filteredValue;
}

// === CALIBRAZIONE AUTOMATICA ===
int sensorMin = 1023;
int sensorMax = 0;

void calibrateSensor(int pin, unsigned long duration) {
    Serial.println("Calibrazione in corso...");
    Serial.println("Varia il sensore per range completo!");
    
    unsigned long startTime = millis();
    
    while (millis() - startTime < duration) {
        int sensorValue = analogRead(pin);
        
        if (sensorValue > sensorMax) {
            sensorMax = sensorValue;
        }
        if (sensorValue < sensorMin) {
            sensorMin = sensorValue;
        }
        
        delay(10);
    }
    
    Serial.print("Min: "); Serial.println(sensorMin);
    Serial.print("Max: "); Serial.println(sensorMax);
}

int readSensorCalibrated(int pin) {
    int raw = analogRead(pin);
    
    // Map to 0-100%
    int mapped = map(raw, sensorMin, sensorMax, 0, 100);
    
    // Constrain
    return constrain(mapped, 0, 100);
}
```

---

## 9. Attuatori e PWM

### 9.1 Controllo LED RGB

```cpp
/*
 * LED RGB COMMON CATHODE
 * 
 * Pinout:
 * R → Pin 9  (PWM)
 * G → Pin 10 (PWM)
 * B → Pin 11 (PWM)
 * - → GND
 * 
 * Ogni pin con resistenza 220Ω
 */

const int RED_PIN = 9;
const int GREEN_PIN = 10;
const int BLUE_PIN = 11;

void setup() {
    pinMode(RED_PIN, OUTPUT);
    pinMode(GREEN_PIN, OUTPUT);
    pinMode(BLUE_PIN, OUTPUT);
}

void setColor(int red, int green, int blue) {
    analogWrite(RED_PIN, red);
    analogWrite(GREEN_PIN, green);
    analogWrite(BLUE_PIN, blue);
}

void loop() {
    // Rosso
    setColor(255, 0, 0);
    delay(1000);
    
    // Verde
    setColor(0, 255, 0);
    delay(1000);
    
    // Blu
    setColor(0, 0, 255);
    delay(1000);
    
    // Giallo (R+G)
    setColor(255, 255, 0);
    delay(1000);
    
    // Viola (R+B)
    setColor(255, 0, 255);
    delay(1000);
    
    // Ciano (G+B)
    setColor(0, 255, 255);
    delay(1000);
    
    // Bianco (R+G+B)
    setColor(255, 255, 255);
    delay(1000);
}

// Rainbow effect
void rainbow() {
    for (int hue = 0; hue < 360; hue++) {
        // Converti HSV a RGB
        int r, g, b;
        hsvToRgb(hue, 255, 255, &r, &g, &b);
        setColor(r, g, b);
        delay(10);
    }
}
```

### 9.2 Servo Motore

```cpp
/*
 * CONTROLLO SERVO MOTORE
 * Richiede libreria Servo.h
 */

#include <Servo.h>

Servo myServo;
const int SERVO_PIN = 9;

void setup() {
    myServo.attach(SERVO_PIN);
    myServo.write(90);  // Posizione centrale
}

void loop() {
    // Sweep 0-180°
    for (int angle = 0; angle <= 180; angle++) {
        myServo.write(angle);
        delay(15);
    }
    
    // Sweep 180-0°
    for (int angle = 180; angle >= 0; angle--) {
        myServo.write(angle);
        delay(15);
    }
}

// Controllo con potenziometro
void servoWithPot() {
    int potValue = analogRead(A0);
    int angle = map(potValue, 0, 1023, 0, 180);
    myServo.write(angle);
    delay(15);
}
```

### 9.3 Buzzer e Toni

```cpp
/*
 * BUZZER PIEZOELETTRICO
 * 
 * Connessione:
 * Buzzer+ → Pin 8
 * Buzzer- → GND
 */

const int BUZZER_PIN = 8;

void setup() {
    pinMode(BUZZER_PIN, OUTPUT);
}

// Tono semplice
void beep(int frequency, int duration) {
    tone(BUZZER_PIN, frequency, duration);
    delay(duration);
    noTone(BUZZER_PIN);
}

// Melodia
void playMelody() {
    // Note e durate
    int melody[] = {262, 294, 330, 349, 392, 440, 494, 523};  // C D E F G A B C
    int duration[] = {250, 250, 250, 250, 250, 250, 250, 500};
    
    for (int i = 0; i < 8; i++) {
        tone(BUZZER_PIN, melody[i], duration[i]);
        delay(duration[i] * 1.3);  // Pausa tra note
        noTone(BUZZER_PIN);
    }
}

// Allarme
void alarm() {
    for (int i = 0; i < 10; i++) {
        tone(BUZZER_PIN, 1000);
        delay(200);
        noTone(BUZZER_PIN);
        delay(200);
    }
}

void loop() {
    beep(440, 500);  // LA, 0.5 secondi
    delay(1000);
}
```

---

## 10. Prompt Tecnici per Arduino

### 10.1 Template Prompt Base

```markdown
# TEMPLATE PROMPT PER SKETCH ARDUINO

Scrivi uno sketch Arduino per board **Arduino Uno** che:

## Hardware Setup
- Board: Arduino Uno (ATmega328P, 5V, 16MHz)
- Componenti:
  * [Componente 1] su pin [X]
  * [Componente 2] su pin [Y]
- Alimentazione: [USB / Batteria / Alimentatore]

## Funzionalità Richieste
1. [Funzione principale]
2. [Funzione secondaria]
3. [Gestione errori/edge cases]

## Vincoli Tecnici
- Usa `millis()` per temporizzazione (NO delay() lunghi)
- Gestione non-bloccante
- Comunicazione seriale a 9600 baud per debug
- Commenti esplicativi
- Definisci pin con #define o const
- Gestisci debouncing se pulsanti

## Output Richiesto
1. Sketch completo (.ino)
2. Commenti che spiegano logica
3. Diagramma pin testuale
4. Istruzioni cablaggio

## Esempio Comportamento
[Descrivi scenario d'uso tipico]
```

### 10.2 Esempi Prompt Specifici

#### **Prompt 1: Sistema Controllo Temperatura**

```
Scrivi sketch Arduino Uno per controllo temperatura ambiente:

HARDWARE:
- Sensore TMP36 su A0
- LED verde su pin 12
- LED rosso su pin 13
- Buzzer su pin 8

LOGICA:
- Leggi temperatura ogni 2 secondi
- Se temp < 20°C: LED verde ON, rosso OFF
- Se 20°C ≤ temp ≤ 25°C: entrambi LED OFF
- Se temp > 25°C: LED rosso ON, verde OFF
- Se temp > 30°C: attiva allarme buzzer (beep 1 sec ogni 5 sec)
- Output seriale: timestamp + temperatura

VINCOLI:
- Usa millis() (no delay)
- Media mobile su 5 letture per stabilità
- Isteresi 0.5°C per evitare oscillazioni
- F() macro per stringhe seriali

OUTPUT:
- Sketch completo
- Schema collegamenti testuale
```

#### **Prompt 2: Sistema Anti-Intruso**

```
Sketch Arduino Uno per allarme anti-intruso:

HARDWARE:
- Sensore PIR (motion) su pin 2
- LED stato su pin 13
- Buzzer allarme su pin 9
- Pulsante disattivazione su pin 3 (pull-up interno)

COMPORTAMENTO:
- Sistema parte in modalità "attesa" (30 sec)
- LED lampeggia lentamente in attesa
- Dopo attesa, sistema "armato"
- LED lampeggia veloce quando armato
- Se PIR rileva movimento → allarme attivo
- Allarme: buzzer continuo + LED fisso
- Pulsante disattiva allarme e torna ad "attesa"
- Log eventi su seriale con timestamp

VINCOLI:
- Tutto non-bloccante con millis()
- Debouncing pulsante 50ms
- Gestione stato con enum o #define

OUTPUT:
- Sketch
- Diagramma stati
- Collegamenti hardware
```

### 10.3 Prompt per Debugging

```
DEBUGGING SKETCH ARDUINO

Ho questo sketch che non funziona come previsto:

```cpp
[CODICE CON PROBLEMA]
```

PROBLEMA OSSERVATO:
[Descrizione comportamento errato]

COMPORTAMENTO ATTESO:
[Cosa dovrebbe fare]

HARDWARE:
[Descrizione setup]

COMPITI:
1. Identifica possibili cause
2. Proponi fix
3. Aggiungi debug seriale appropriato
4. Spiega perché il problema si verificava

VINCOLI:
- Mantieni logica generale
- Migliora robustezza
```

---

## 11. Errori Comuni Generati da IA

### 11.1 Errore: Pin Non Esistenti o Sbagliati

```cpp
// ❌ IA potrebbe suggerire:
analogWrite(A0, 128);  // ERRORE! A0 non è pin PWM

// ✅ CORRETTO:
// Pin PWM su Uno: 3, 5, 6, 9, 10, 11
analogWrite(9, 128);

// ❌ IA potrebbe usare pin inesistenti:
pinMode(20, OUTPUT);  // Uno ha solo pin 0-13 digital!

// ✅ Verifica sempre pinout della board target
```

### 11.2 Errore: Librerie Non Standard

```cpp
// ❌ IA potrebbe suggerire librerie inesistenti:
#include <UltrasonicSensor.h>  // Non esiste!

// ✅ CORRETTO: libreria corretta o codice raw
#include <NewPing.h>  // Libreria reale per HC-SR04
// OPPURE implementazione diretta
```

### 11.3 Errore: Uso Scorretto di delay()

```cpp
// ❌ IA potrebbe generare:
void loop() {
    if (digitalRead(BUTTON_PIN) == LOW) {
        digitalWrite(LED_PIN, HIGH);
        delay(5000);  // 5 secondi bloccato!
        digitalWrite(LED_PIN, LOW);
    }
    checkSensor();  // Eseguito solo ogni 5+ secondi!
}

// ✅ CORRETTO: millis()
unsigned long ledOnTime = 0;
bool ledActive = false;
const unsigned long LED_DURATION = 5000;

void loop() {
    // Check pulsante
    if (digitalRead(BUTTON_PIN) == LOW && !ledActive) {
        digitalWrite(LED_PIN, HIGH);
        ledOnTime = millis();
        ledActive = true;
    }
    
    // Check timeout LED
    if (ledActive && (millis() - ledOnTime >= LED_DURATION)) {
        digitalWrite(LED_PIN, LOW);
        ledActive = false;
    }
    
    // Eseguito sempre!
    checkSensor();
}
```

### 11.4 Errore: Overflow Variabili

```cpp
// ❌ IA potrebbe usare int per millis():
int currentTime = millis();  // OVERFLOW dopo 32 secondi!

// ✅ CORRETTO:
unsigned long currentTime = millis();

// ❌ Calcoli errati:
int interval = 1000;
if (millis() - previousMillis > interval) {  // Confronto signed/unsigned!

// ✅ CORRETTO:
unsigned long interval = 1000;
if (millis() - previousMillis >= interval) {
```

### 11.5 Errore: Consumo Memoria Eccessivo

```cpp
// ❌ IA potrebbe generare:
String messages[100];  // Ogni String alloca dinamicamente!
                       // Memoria esaurita velocemente!

// ✅ CORRETTO per SRAM limitata:
char messages[10][50];  // Array statico, uso controllato

// ❌ Stringhe letterali in SRAM:
Serial.println("Questo è un messaggio lungo che occupa SRAM inutilmente");

// ✅ PROGMEM:
Serial.println(F("Messaggio in Flash, non in SRAM"));
```

### 11.6 Errore: Pull-up/Pull-down Ignorati

```cpp
// ❌ IA potrebbe dimenticare:
pinMode(BUTTON_PIN, INPUT);
// Pulsante fluttua, letture casuali!

// ✅ CORRETTO:
pinMode(BUTTON_PIN, INPUT_PULLUP);
// Oppure pull-down esterno se necessario
```

---

## 12. Debugging Arduino

### 12.1 Strategia Debugging Embedded

```
DEBUGGING ARDUINO - PROCESSO:

1. VERIFICA HARDWARE
   □ Alimentazione corretta (LED power ON?)
   □ USB connesso e riconosciuto
   □ Board selezionata correttamente
   □ Porta seriale corretta
   □ Componenti cablati secondo schema
   □ Polarità corrette (LED, condensatori, IC)
   □ Cortocircuiti assenti
   □ Connessioni salde

2. VERIFICA UPLOAD
   □ Sketch compila senza errori
   □ Upload completato con successo
   □ LED L lampeggia durante upload

3. DEBUG SOFTWARE
   □ Serial.begin() in setup()
   □ Print debug nei punti chiave
   □ Verifica valori variabili
   □ Usa LED onboard (pin 13) per feedback

4. ISOLAMENTO PROBLEMA
   □ Disabilita sezioni codice
   □ Testa un componente alla volta
   □ Semplifica sketch a minimo funzionante
```

### 12.2 Tecniche Debug Seriale

```cpp
/*
 * DEBUG PRINT AVANZATO
 */

// Macro utili
#define DEBUG_VAR(var) \
    Serial.print(#var " = "); Serial.println(var);

#define DEBUG_PIN(pin) \
    Serial.print("Pin " #pin " = "); \
    Serial.println(digitalRead(pin) ? "HIGH" : "LOW");

void setup() {
    Serial.begin(115200);
    
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop() {
    int sensor = analogRead(A0);
    bool button = digitalRead(2);
    
    // Debug variabili
    DEBUG_VAR(sensor);
    DEBUG_VAR(button);
    DEBUG_PIN(2);
    DEBUG_PIN(13);
    
    // Output: "sensor = 512"
    //         "button = 1"
    //         "Pin 2 = HIGH"
    //         etc.
    
    delay(500);
}

// Trace execution
void debugTrace(const char* func, int line) {
    Serial.print(F("["));
    Serial.print(millis());
    Serial.print(F("ms] "));
    Serial.print(func);
    Serial.print(F(":"));
    Serial.println(line);
}

#define TRACE() debugTrace(__func__, __LINE__)

void myFunction() {
    TRACE();  // Output: "[1234ms] myFunction:45"
    // ... codice ...
}
```

### 12.3 Debug con LED

```cpp
/*
 * DEBUG VISIVO CON LED (quando Serial non disponibile)
 */

const int DEBUG_LED = 13;

// Blink pattern per errori
void blinkError(int code) {
    for (int i = 0; i < code; i++) {
        digitalWrite(DEBUG_LED, HIGH);
        delay(200);
        digitalWrite(DEBUG_LED, LOW);
        delay(200);
    }
    delay(1000);
}

void loop() {
    int sensor = analogRead(A0);
    
    if (sensor < 100) {
        blinkError(1);  // 1 blink = sensore basso
    } else if (sensor > 900) {
        blinkError(2);  // 2 blink = sensore alto
    } else {
        blinkError(3);  // 3 blink = OK
    }
}

// Heartbeat: conferma loop() gira
void heartbeat() {
    static unsigned long lastBlink = 0;
    static bool state = false;
    
    if (millis() - lastBlink >= 500) {
        lastBlink = millis();
        state = !state;
        digitalWrite(DEBUG_LED, state);
    }
}
```

### 12.4 Watchdog e Reset

```cpp
/*
 * WATCHDOG TIMER (riavvio automatico se freeze)
 */

#include <avr/wdt.h>

void setup() {
    Serial.begin(9600);
    
    // Abilita watchdog 2 secondi
    wdt_enable(WDTO_2S);
    
    Serial.println(F("Watchdog attivo"));
}

void loop() {
    // Reset watchdog (dice "sono vivo!")
    wdt_reset();
    
    // Codice normale
    // Se loop() si blocca >2 sec → reset automatico
    
    delay(100);
}
```

---

## 13. Progetti Completi Guidati

### 13.1 Progetto: Stazione Meteo

```cpp
/*
 * STAZIONE METEO ARDUINO
 * 
 * HARDWARE:
 * - TMP36 (temperatura) su A0
 * - Fotoresistenza (luce) su A1
 * - LED stato su pin 13
 * - Buzzer allarme su pin 8
 * 
 * FUNZIONALITÀ:
 * - Lettura temperatura e luminosità ogni 5 secondi
 * - Media mobile su 10 campioni
 * - Allarme se temperatura > 30°C
 * - Log dati su seriale formato CSV
 * - LED heartbeat
 */

#include <EEPROM.h>

// === PIN ===
const int TEMP_PIN = A0;
const int LIGHT_PIN = A1;
const int LED_PIN = 13;
const int BUZZER_PIN = 8;

// === COSTANTI ===
const unsigned long READ_INTERVAL = 5000;  // 5 secondi
const unsigned long HEARTBEAT_INTERVAL = 500;
const float TEMP_ALARM_THRESHOLD = 30.0;  // °C
const int NUM_SAMPLES = 10;

// === VARIABILI GLOBALI ===
unsigned long lastReadTime = 0;
unsigned long lastHeartbeat = 0;
bool ledState = false;
bool alarmActive = false;

// Buffer per media mobile
float tempReadings[NUM_SAMPLES];
int lightReadings[NUM_SAMPLES];
int sampleIndex = 0;
bool bufferFull = false;

// Statistiche
float tempMin = 999.0;
float tempMax = -999.0;
unsigned long sampleCount = 0;

// === SETUP ===
void setup() {
    Serial.begin(9600);
    
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    
    // Inizializza buffer
    for (int i = 0; i < NUM_SAMPLES; i++) {
        tempReadings[i] = 0;
        lightReadings[i] = 0;
    }
    
    // Header CSV
    Serial.println(F("timestamp,temperature,light,alarm"));
    
    Serial.println(F("=== Stazione Meteo Avviata ==="));
}

// === LOOP ===
void loop() {
    unsigned long currentMillis = millis();
    
    // Heartbeat LED
    if (currentMillis - lastHeartbeat >= HEARTBEAT_INTERVAL) {
        lastHeartbeat = currentMillis;
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }
    
    // Lettura sensori
    if (currentMillis - lastReadTime >= READ_INTERVAL) {
        lastReadTime = currentMillis;
        
        readAndProcessSensors();
        logData();
        checkAlarms();
        
        sampleCount++;
    }
}

// === FUNZIONI ===

void readAndProcessSensors() {
    // Leggi temperatura
    int tempRaw = analogRead(TEMP_PIN);
    float tempVoltage = tempRaw * (5.0 / 1023.0);
    float tempC = (tempVoltage - 0.5) * 100.0;
    
    // Leggi luce
    int lightRaw = analogRead(LIGHT_PIN);
    
    // Aggiungi a buffer
    tempReadings[sampleIndex] = tempC;
    lightReadings[sampleIndex] = lightRaw;
    
    sampleIndex = (sampleIndex + 1) % NUM_SAMPLES;
    if (sampleIndex == 0) bufferFull = true;
    
    // Aggiorna min/max
    if (tempC < tempMin) tempMin = tempC;
    if (tempC > tempMax) tempMax = tempC;
}

float getAverageTemp() {
    int samples = bufferFull ? NUM_SAMPLES : sampleIndex;
    if (samples == 0) return 0;
    
    float sum = 0;
    for (int i = 0; i < samples; i++) {
        sum += tempReadings[i];
    }
    return sum / samples;
}

float getAverageLight() {
    int samples = bufferFull ? NUM_SAMPLES : sampleIndex;
    if (samples == 0) return 0;
    
    long sum = 0;
    for (int i = 0; i < samples; i++) {
        sum += lightReadings[i];
    }
    return (float)sum / samples;
}

void logData() {
    float avgTemp = getAverageTemp();
    float avgLight = getAverageLight();
    
    // Formato CSV: timestamp,temp,light,alarm
    Serial.print(millis());
    Serial.print(",");
    Serial.print(avgTemp, 2);
    Serial.print(",");
    Serial.print(avgLight, 0);
    Serial.print(",");
    Serial.println(alarmActive ? "1" : "0");
}

void checkAlarms() {
    float avgTemp = getAverageTemp();
    
    if (avgTemp > TEMP_ALARM_THRESHOLD && !alarmActive) {
        // Attiva allarme
        alarmActive = true;
        Serial.println(F("!!! ALLARME TEMPERATURA ALTA !!!"));
        soundAlarm();
    } else if (avgTemp <= TEMP_ALARM_THRESHOLD - 1.0 && alarmActive) {
        // Disattiva allarme (isteresi 1°C)
        alarmActive = false;
        Serial.println(F("Allarme disattivato"));
    }
}

void soundAlarm() {
    // Beep pattern
    for (int i = 0; i < 3; i++) {
        tone(BUZZER_PIN, 1000, 200);
        delay(300);
    }
    noTone(BUZZER_PIN);
}

void printStatistics() {
    Serial.println(F("\n=== STATISTICHE ==="));
    Serial.print(F("Campioni: ")); Serial.println(sampleCount);
    Serial.print(F("Temp min: ")); Serial.print(tempMin, 1); Serial.println(F(" C"));
    Serial.print(F("Temp max: ")); Serial.print(tempMax, 1); Serial.println(F(" C"));
    Serial.print(F("Temp media: ")); Serial.print(getAverageTemp(), 1); Serial.println(F(" C"));
    Serial.println();
}
```

### 13.2 Progetto: Sistema Irrigazione Automatico

```cpp
/*
 * SISTEMA IRRIGAZIONE AUTOMATICO
 * 
 * HARDWARE:
 * - Sensore umidità terreno (resistivo) su A0
 * - Relè pompa su pin 7
 * - LED stato su pin 13
 * - Pulsante manuale su pin 2
 * - Potenziometro soglia su A1
 * 
 * LOGICA:
 * - Leggi umidità ogni 10 secondi
 * - Se umidità < soglia → attiva pompa per 5 secondi
 * - Pulsante forza irrigazione manuale
 * - Potenziometro regola soglia
 */

const int MOISTURE_PIN = A0;
const int THRESHOLD_POT_PIN = A1;
const int PUMP_PIN = 7;
const int LED_PIN = 13;
const int BUTTON_PIN = 2;

const unsigned long CHECK_INTERVAL = 10000;  // 10 sec
const unsigned long PUMP_DURATION = 5000;    // 5 sec

unsigned long lastCheckTime = 0;
unsigned long pumpStartTime = 0;
bool pumpActive = false;
bool lastButtonState = HIGH;

void setup() {
    Serial.begin(9600);
    
    pinMode(PUMP_PIN, OUTPUT);
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    
    digitalWrite(PUMP_PIN, LOW);  // Pompa off
    
    Serial.println(F("=== Sistema Irrigazione ==="));
}

void loop() {
    unsigned long currentMillis = millis();
    
    // Check automatico umidità
    if (currentMillis - lastCheckTime >= CHECK_INTERVAL && !pumpActive) {
        lastCheckTime = currentMillis;
        checkMoisture();
    }
    
    // Check pulsante manuale
    checkButton();
    
    // Gestione timeout pompa
    if (pumpActive && (currentMillis - pumpStartTime >= PUMP_DURATION)) {
        stopPump();
    }
    
    // LED indica pompa attiva
    digitalWrite(LED_PIN, pumpActive);
}

void checkMoisture() {
    int moisture = analogRead(MOISTURE_PIN);
    int threshold = analogRead(THRESHOLD_POT_PIN);
    
    Serial.print(F("Umidità: ")); Serial.print(moisture);
    Serial.print(F(" | Soglia: ")); Serial.println(threshold);
    
    if (moisture < threshold) {
        Serial.println(F("Terreno secco → irrigazione"));
        startPump();
    } else {
        Serial.println(F("Umidità OK"));
    }
}

void checkButton() {
    bool reading = digitalRead(BUTTON_PIN);
    
    // Rileva fronte discesa (pressione)
    if (reading == LOW && lastButtonState == HIGH && !pumpActive) {
        Serial.println(F("Irrigazione manuale"));
        startPump();
        delay(50);  // Debounce semplice
    }
    
    lastButtonState = reading;
}

void startPump() {
    pumpActive = true;
    pumpStartTime = millis();
    digitalWrite(PUMP_PIN, HIGH);
    Serial.println(F(">>> Pompa ATTIVATA"));
}

void stopPump() {
    pumpActive = false;
    digitalWrite(PUMP_PIN, LOW);
    Serial.println(F("<<< Pompa DISATTIVATA"));
}
```

---

## 14. Librerie e Moduli

### 14.1 Librerie Arduino Essenziali

```cpp
/*
 * LIBRERIE COMUNI
 */

// === SERVO ===
#include <Servo.h>
Servo myservo;
myservo.attach(9);
myservo.write(90);

// === DHT (Temperatura/Umidità) ===
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
dht.begin();
float temp = dht.readTemperature();
float hum = dht.readHumidity();

// === LCD I2C ===
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Indirizzo, cols, rows
lcd.init();
lcd.backlight();
lcd.setCursor(0, 0);
lcd.print("Hello World!");

// === EEPROM (storage persistente) ===
#include <EEPROM.h>
EEPROM.write(0, 42);   // Scrivi byte
int val = EEPROM.read(0);  // Leggi byte

// === WIRE (I2C) ===
#include <Wire.h>
Wire.begin();  // Master
Wire.beginTransmission(address);
Wire.write(data);
Wire.endTransmission();

// === SPI ===
#include <SPI.h>
SPI.begin();
SPI.transfer(data);
```

### 14.2 Gestione Display LCD

```cpp
/*
 * DISPLAY LCD 16x2 I2C
 * Indirizzo tipico: 0x27 o 0x3F
 */

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();
    lcd.backlight();
    
    lcd.setCursor(0, 0);  // Colonna 0, Riga 0
    lcd.print("Arduino ITS");
    
    lcd.setCursor(0, 1);  // Riga 1
    lcd.print("Temp: ");
}

void updateDisplay(float temperature) {
    lcd.setCursor(6, 1);  // Dopo "Temp: "
    lcd.print(temperature, 1);  // 1 decimale
    lcd.print((char)223);  // Simbolo °
    lcd.print("C  ");  // Spazi per cancellare vecchi char
}

// Caratteri custom
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
    lcd.createChar(0, heart);  // Definisci carattere 0
    lcd.setCursor(0, 0);
    lcd.write(0);  // Stampa cuore
}
```

---

## 15. Best Practices Embedded

### 15.1 Ottimizzazione Memoria

```cpp
/*
 * TECNICHE RISPARMIO MEMORIA
 */

// ❌ SPRECO SRAM:
char message[] = "Questo messaggio lungo occupa SRAM";
Serial.println(message);  // 35 byte di SRAM sprecati!

// ✅ F() MACRO (Flash):
Serial.println(F("Messaggio in Flash, non in SRAM"));

// ❌ ARRAY GRANDI IN SRAM:
int bigArray[1000];  // 2000 byte di SRAM!

// ✅ PROGMEM (Flash):
const int bigArray[1000] PROGMEM = { /* dati */ };
int value = pgm_read_word(&bigArray[i]);  // Leggi da Flash

// === VERIFICA USO MEMORIA ===
void checkMemory() {
    extern int __heap_start, *__brkval;
    int v;
    int free = (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
    
    Serial.print(F("SRAM libera: "));
    Serial.print(free);
    Serial.println(F(" byte"));
}

// === RISPARMIO CON TIPI PICCOLI ===
// ❌ Spreco:
int ledState = 1;  // 2 byte per valore 0/1!

// ✅ Ottimizzato:
bool ledState = true;  // 1 byte

// ✅ Bitfield per flags multipli:
struct {
    uint8_t led1 : 1;
    uint8_t led2 : 1;
    uint8_t alarm : 1;
    uint8_t motor : 1;
    // 4 flag in 1 byte invece di 4!
} flags;
```

### 15.2 Gestione Energia

```cpp
/*
 * RISPARMIO ENERGETICO
 */

#include <avr/sleep.h>
#include <avr/power.h>

void enterSleep() {
    // Disabilita ADC
    ADCSRA &= ~(1 << ADEN);
    
    // Setup sleep mode
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    sleep_enable();
    
    // Sleep
    sleep_mode();
    
    // ↑ CPU si ferma qui
    // ↓ Riprende dopo interrupt (es. watchdog)
    
    sleep_disable();
    
    // Riabilita ADC
    ADCSRA |= (1 << ADEN);
}

// Wakeup con interrupt esterno
void setup() {
    pinMode(2, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(2), wakeUp, LOW);
}

void wakeUp() {
    // ISR vuota, serve solo per wakeup
}

void loop() {
    // Fai qualcosa
    doWork();
    
    // Dormi
    enterSleep();
}
```

### 15.3 Checklist Qualità Sketch

```
✅ STRUTTURA
[ ] Setup completo (pin, seriale, librerie)
[ ] Loop non-bloccante (millis, no delay lunghi)
[ ] Funzioni brevi e focused
[ ] Commenti significativi

✅ HARDWARE
[ ] Pin definiti con #define/const
[ ] Pull-up/down configurati
[ ] Correnti pin non superate (20mA max)
[ ] Alimentazione adeguata

✅ TEMPORIZZAZIONE
[ ] millis() per azioni periodiche
[ ] Unsigned long per timestamp
[ ] Gestione overflow considerata

✅ MEMORIA
[ ] F() macro per stringhe
[ ] PROGMEM per dati const grandi
[ ] Evitato uso eccessivo String
[ ] Verificato uso SRAM (< 75%)

✅ ROBUSTEZZA
[ ] Input validation (range sensori)
[ ] Debouncing pulsanti
[ ] Watchdog per freeze (opzionale)
[ ] Gestione errori sensori

✅ DEBUG
[ ] Seriale configurata per debug
[ ] LED heartbeat per conferma esecuzione
[ ] Log eventi significativi
[ ] Testato su hardware reale

✅ DOCUMENTAZIONE
[ ] Schema collegamenti chiaro
[ ] Lista componenti
[ ] Istruzioni upload
[ ] Comportamento atteso descritto
```

---

## ✅ Checklist Completamento Modulo 4

- [ ] Conosco architettura Arduino (pinout, memoria, limiti)
- [ ] So strutturare sketch (setup/loop)
- [ ] Gestisco pin digitali e analogici correttamente
- [ ] Uso millis() invece di delay() per logiche non-bloccanti
- [ ] Implemento multi-timer indipendenti
- [ ] Uso comunicazione seriale per debugging
- [ ] Interfaccio sensori analogici con filtraggio
- [ ] Controllo attuatori (LED RGB, servo, buzzer)
- [ ] Scrivo prompt efficaci per sketch Arduino
- [ ] Riconosco errori comuni generati da IA
- [ ] Debuggo efficacemente via seriale e LED
- [ ] Ho completato almeno 2 progetti completi
- [ ] Applico best practices embedded
- [ ] Mi sento pronto per il Modulo 5 (Verifica Finale)

---

**Fine Modulo 4**

*Prossimo passo: Modulo 5 - Verifica Finale del Corso*

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita

