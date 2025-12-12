# MODULO 6 - VERIFICA FINALE E CERTIFICAZIONE
## Fondamenti di Intelligenza Artificiale per la Programmazione
### Corso ITS 2025 - Assessment Completo

---

## INDICE

1. [Struttura dell'Esame](#struttura-dellesame)
2. [Parte Teorica - 40 Punti](#parte-teorica)
3. [Parte Pratica - 60 Punti](#parte-pratica)
4. [Progetti d'Esame](#progetti-desame)
5. [Criteri di Valutazione](#criteri-di-valutazione)
6. [Materiali di Preparazione](#materiali-di-preparazione)
7. [Portfolio Professionale](#portfolio-professionale)
8. [Simulazioni d'Esame](#simulazioni-desame)
9. [Certificazione e Career Path](#certificazione-e-career-path)

---

## STRUTTURA DELL'ESAME

### Panoramica Generale

L'esame finale si articola in **due parti complementari** che valutano competenze teoriche e pratiche acquisite durante il corso.

#### Distribuzione dei Punti

```
┌─────────────────────────────────────────┐
│ PARTE TEORICA              40 punti     │
├─────────────────────────────────────────┤
│ - Quiz a risposta multipla  20 punti    │
│ - Domande aperte            10 punti    │
│ - Analisi critica           10 punti    │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ PARTE PRATICA              60 punti     │
├─────────────────────────────────────────┤
│ - Implementazione progetto  35 punti    │
│ - Documentazione tecnica    10 punti    │
│ - Presentazione orale       10 punti    │
│ - Uso AI e metodologia       5 punti    │
└─────────────────────────────────────────┘

TOTALE: 100 punti
Soglia minima: 60/100 (sufficienza)
```

### Tempistiche

- **Parte Teorica**: 90 minuti
- **Pausa**: 15 minuti
- **Parte Pratica**: 4 ore (sviluppo)
- **Presentazione**: 15 minuti per candidato

**Totale tempo d'esame**: circa 6 ore

---

## PARTE TEORICA - 40 PUNTI

### Sezione A: Quiz a Risposta Multipla (20 punti)

**20 domande, 1 punto ciascuna**

#### Blocco 1: Fondamenti di IA (Domande 1-5)

**Domanda 1**
Quale delle seguenti affermazioni descrive meglio un Large Language Model (LLM)?

a) Un sistema che traduce solo tra lingue diverse
b) Un modello di rete neurale addestrato su grandi quantità di testo per comprendere e generare linguaggio naturale
c) Un database di risposte pre-programmate
d) Un motore di ricerca avanzato

**Risposta corretta**: b)

---

**Domanda 2**
Cosa significa "temperatura" nei parametri di generazione di un LLM?

a) La velocità di elaborazione del modello
b) Il livello di randomness nelle risposte generate
c) La dimensione del modello in GB
d) Il numero di token processati al secondo

**Risposta corretta**: b)

---

**Domanda 3**
Qual è il principale vantaggio del "prompt engineering"?

a) Rendere il codice più veloce
b) Ridurre il consumo di memoria
c) Ottenere risposte più precise e rilevanti dall'IA senza modificare il modello
d) Compilare automaticamente il codice

**Risposta corretta**: c)

---

**Domanda 4**
Cosa rappresenta il "contesto" (context window) in un LLM?

a) La quantità di informazioni che il modello può considerare in una singola interazione
b) Il tempo di risposta del modello
c) La qualità delle risposte generate
d) Il numero di utenti simultanei supportati

**Risposta corretta**: a)

---

**Domanda 5**
Quale tecnica NON è consigliata per migliorare un prompt?

a) Fornire esempi concreti (few-shot learning)
b) Specificare il formato di output desiderato
c) Usare solo parole chiave senza contesto
d) Descrivere il ruolo o persona dell'IA

**Risposta corretta**: c)

---

#### Blocco 2: Programmazione C (Domande 6-10)

**Domanda 6**
Quale funzione standard C deve essere usata per allocare dinamicamente memoria?

a) `new()`
b) `malloc()`
c) `allocate()`
d) `create()`

**Risposta corretta**: b)

---

**Domanda 7**
Cosa succede se non si libera la memoria allocata dinamicamente con `free()`?

a) Il programma va in crash immediatamente
b) Si verifica un memory leak
c) La memoria viene liberata automaticamente
d) Il compilatore genera un errore

**Risposta corretta**: b)

---

**Domanda 8**
Qual è la differenza tra passaggio per valore e per riferimento (puntatore)?

a) Nessuna differenza in C
b) Per valore copia i dati, per riferimento passa l'indirizzo di memoria
c) Per valore è più veloce
d) Per riferimento funziona solo con interi

**Risposta corretta**: b)

---

**Domanda 9**
Quale header file contiene le definizioni per le operazioni su stringhe in C?

a) `<stdio.h>`
b) `<stdlib.h>`
c) `<string.h>`
d) `<ctype.h>`

**Risposta corretta**: c)

---

**Domanda 10**
Cosa fa l'operatore `sizeof()` in C?

a) Restituisce il valore di una variabile
b) Restituisce il numero di byte occupati da un tipo o variabile
c) Converte tipi di dati
d) Alloca memoria dinamicamente

**Risposta corretta**: b)

---

#### Blocco 3: Arduino e Embedded (Domande 11-15)

**Domanda 11**
Quale funzione Arduino legge un valore analogico da un pin?

a) `digitalRead()`
b) `analogRead()`
c) `readAnalog()`
d) `getAnalogValue()`

**Risposta corretta**: b)

---

**Domanda 12**
Qual è il range di valori restituiti da `analogRead()` su Arduino Uno?

a) 0-255
b) 0-1023
c) 0-4095
d) 0-65535

**Risposta corretta**: b)

---

**Domanda 13**
Quale protocollo di comunicazione usa solo 2 fili (SDA e SCL)?

a) SPI
b) UART
c) I2C
d) CAN Bus

**Risposta corretta**: c)

---

**Domanda 14**
Perché è importante usare resistenze di pull-up in I2C?

a) Per limitare la corrente
b) Per garantire livelli logici definiti quando le linee non sono guidate
c) Per aumentare la velocità di comunicazione
d) Non sono necessarie in I2C

**Risposta corretta**: b)

---

**Domanda 15**
Cosa rappresenta il duty cycle in un segnale PWM?

a) La frequenza del segnale
b) La percentuale di tempo in cui il segnale è alto rispetto al periodo totale
c) L'ampiezza del segnale
d) Il numero di impulsi al secondo

**Risposta corretta**: b)

---

#### Blocco 4: IoT e Sistemi Avanzati (Domande 16-20)

**Domanda 16**
Quale protocollo è comunemente usato per la comunicazione IoT leggera e basata su publish/subscribe?

a) HTTP
b) FTP
c) MQTT
d) SMTP

**Risposta corretta**: c)

---

**Domanda 17**
Cosa significa QoS (Quality of Service) in MQTT?

a) La velocità di trasmissione dati
b) Il livello di garanzia di consegna dei messaggi (0, 1, o 2)
c) La qualità della connessione WiFi
d) Il numero di client connessi

**Risposta corretta**: b)

---

**Domanda 18**
In un controllo PID, quale componente reagisce all'errore attuale?

a) Integrale (I)
b) Derivativo (D)
c) Proporzionale (P)
d) Tutti e tre insieme

**Risposta corretta**: c)

---

**Domanda 19**
Quale piattaforma ESP32 supporta nativamente WiFi e Bluetooth?

a) Arduino Uno
b) Arduino Nano
c) ESP8266
d) ESP32

**Risposta corretta**: d)

---

**Domanda 20**
Cosa permette TensorFlow Lite Micro?

a) Eseguire modelli di machine learning su microcontrollori
b) Creare interfacce grafiche
c) Gestire database SQL
d) Compilare codice più velocemente

**Risposta corretta**: a)

---

### Sezione B: Domande Aperte (10 punti)

**5 domande, 2 punti ciascuna**

#### Domanda 1: Prompt Engineering
**Domanda**: Spiega la differenza tra un prompt "zero-shot" e "few-shot" fornendo un esempio pratico per ciascuno nel contesto della generazione di codice C.

**Risposta attesa** (criteri di valutazione):
- **Zero-shot** (1 punto): Definizione corretta - richiesta diretta senza esempi
  - Esempio: "Scrivi una funzione C che calcola il fattoriale"
- **Few-shot** (1 punto): Definizione corretta - fornisce esempi prima della richiesta
  - Esempio: "Ecco una funzione che somma due numeri: [codice]. Ecco una che moltiplica: [codice]. Ora scrivi una che calcola il fattoriale."
- **Bonus**: Menzione del vantaggio del few-shot per task complessi (+0.5)

---

#### Domanda 2: Gestione Memoria
**Domanda**: Descrivi il concetto di "stack" vs "heap" in C e quando è appropriato usare l'allocazione dinamica (heap) invece dell'allocazione automatica (stack).

**Risposta attesa**:
- **Stack** (0.5 punti): Memoria automatica, LIFO, veloce, dimensione limitata
- **Heap** (0.5 punti): Memoria dinamica, gestita manualmente, più grande, più lenta
- **Quando usare heap** (1 punto):
  - Dimensione dati non nota a compile-time
  - Dati che devono persistere oltre la funzione
  - Strutture dati grandi (array estesi, liste)
  - Esempio concreto

---

#### Domanda 3: Protocolli di Comunicazione
**Domanda**: Confronta I2C e SPI in termini di numero di fili, velocità, complessità e casi d'uso tipici per progetti Arduino.

**Risposta attesa**:
- **I2C** (1 punto):
  - 2 fili (SDA, SCL) + alimentazione
  - Velocità: 100kHz-400kHz (standard/fast mode)
  - Indirizzamento, multi-master possibile
  - Uso: sensori, display, RTC (molti dispositivi)
- **SPI** (1 punto):
  - 4+ fili (MISO, MOSI, SCK, CS per ogni slave)
  - Velocità: fino a diversi MHz
  - Full-duplex, comunicazione più veloce
  - Uso: SD card, display TFT, moduli radio

---

#### Domanda 4: Controllo PID
**Domanda**: Spiega cosa causa l'effetto "integral windup" in un controllore PID e come può essere mitigato nel codice.

**Risposta attesa**:
- **Causa** (1 punto):
  - Accumulo eccessivo del termine integrale quando l'attuatore è saturato
  - Sistema non può raggiungere setpoint, errore continua ad accumularsi
- **Mitigazione** (1 punto):
  - Clamping: limitare il valore dell'integrale
  - Back-calculation: ridurre integrale quando output è saturato
  - Conditional integration: non integrare quando output saturato
  - Esempio di codice con clamping

---

#### Domanda 5: IoT Security
**Domanda**: Elenca almeno tre misure di sicurezza essenziali da implementare in un dispositivo IoT che trasmette dati sensibili.

**Risposta attesa** (0.67 punti per misura, max 2 punti):
1. **Crittografia in transito**: TLS/SSL per MQTT o HTTPS
2. **Autenticazione**: Certificati client, token, credenziali sicure
3. **OTA sicuro**: Verifica firma firmware, rollback su errori
4. **Protezione credenziali**: Non hardcodare password, usare secure storage
5. **Principle of least privilege**: Permessi minimi necessari
6. **Aggiornamenti regolari**: Patch vulnerabilità note

---

### Sezione C: Analisi Critica (10 punti)

**2 casi, 5 punti ciascuno**

#### Caso 1: Debug di Codice Arduino con IA

**Scenario**:
Uno studente ha scritto il seguente codice per leggere un sensore di temperatura DHT22 e visualizzarlo su display LCD, ma riceve errori di compilazione e comportamenti anomali:

```cpp
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  dht.begin();
  lcd.init();
  lcd.backlight();
}

void loop() {
  float temp = dht.readTemperature();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temp);
  lcd.print(" C");
  delay(100);
}
```

Lo studente chiede all'IA: *"Il mio codice non funziona, sistemalo"*

**Domande**:
1. Identifica almeno 3 problemi nel codice (1.5 punti)
2. Critica il prompt usato dallo studente (1 punto)
3. Scrivi un prompt migliore per ottenere aiuto dall'IA (1.5 punti)
4. Proponi il codice corretto (1 punto)

**Risposta attesa**:

**1. Problemi nel codice** (0.5 punti ciascuno):
- Delay troppo breve (100ms): DHT22 necessita almeno 2 secondi tra letture
- Nessun controllo su `isnan()`: temperatura potrebbe essere NaN se lettura fallisce
- LCD non viene pulito: testo si sovrappone, specialmente se lunghezza varia
- Nessuna gestione errori: se sensore non risponde, stampa valori invalidi

**2. Critica del prompt** (1 punto):
- Troppo generico: "non funziona" non descrive il problema
- Nessun contesto: tipo di errore (compilazione/runtime)
- Nessuna informazione hardware: collegamenti, alimentazione
- Non specifica comportamento atteso vs osservato

**3. Prompt migliorato** (1.5 punti):
```
Ho un Arduino Uno con sensore DHT22 su pin 2 e LCD I2C all'indirizzo 0x27.
Il codice compila senza errori, ma sul display vedo valori "nan" che si
sovrappongono.

Ecco il mio codice:
[codice]

Voglio:
1. Visualizzare la temperatura in formato "Temp: XX.X C"
2. Gestire errori di lettura sensore
3. Aggiornare il display ogni 2 secondi senza sovrascritture

Analizza il codice e suggerisci correzioni con spiegazioni.
```

**4. Codice corretto** (1 punto):
```cpp
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("DHT22 Ready");
  delay(2000);
}

void loop() {
  float temp = dht.readTemperature();

  lcd.clear();  // Pulisce display

  if (isnan(temp)) {
    lcd.setCursor(0, 0);
    lcd.print("Errore sensore!");
    Serial.println("Lettura fallita");
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(temp, 1);  // 1 decimale
    lcd.print(" C");
    Serial.print("Temperatura: ");
    Serial.println(temp);
  }

  delay(2000);  // DHT22 richiede 2 sec tra letture
}
```

---

#### Caso 2: Scelta Architetturale IoT

**Scenario**:
Un'azienda agricola vuole monitorare 50 serre distribuite su 10 ettari. Ogni serra necessita di:
- Temperatura, umidità aria, umidità suolo (3 sensori)
- Controllo irrigazione automatica
- Allarmi in caso di anomalie
- Storico dati per analisi mensili
- Budget limitato: 100€ per serra

Due proposte:

**Proposta A**:
- ESP32 per ogni serra (WiFi)
- Invio dati ogni minuto a server cloud (ThingSpeak gratuito)
- Controllo attuatori tramite cloud
- App mobile per monitoraggio

**Proposta B**:
- Arduino Nano + modulo LoRa per ogni serra
- Gateway centrale LoRa + Raspberry Pi
- Database locale (InfluxDB)
- Controllo attuatori locale
- Dashboard web (Grafana)

**Domande**:
1. Analizza vantaggi e svantaggi di ciascuna proposta (2 punti)
2. Quali sono i rischi principali per ciascuna soluzione? (1.5 punti)
3. Quale proporresti e perché? (1 punto)
4. Come useresti l'IA per sviluppare la soluzione scelta? (0.5 punti)

**Risposta attesa**:

**1. Vantaggi e Svantaggi** (0.5 punti per voce, max 2 punti):

*Proposta A (ESP32 + Cloud)*:
- ✅ Vantaggi:
  - Accesso remoto da ovunque
  - Scalabilità facile
  - Manutenzione software remota (OTA)
  - Interfaccia pronta (ThingSpeak)
- ❌ Svantaggi:
  - Dipendenza da connessione internet
  - Costi dati se si supera piano gratuito
  - Latenza nel controllo (cloud round-trip)
  - Privacy: dati su server terzi
  - Consumo energetico WiFi elevato

*Proposta B (LoRa + Locale)*:
- ✅ Vantaggi:
  - Autonomia: funziona senza internet
  - Basso consumo energetico
  - Controllo in tempo reale (locale)
  - Privacy: dati proprietari
  - Costi operativi bassi
- ❌ Svantaggi:
  - Accesso remoto complesso (VPN, DDNS)
  - Manutenzione hardware centrale
  - Scalabilità limitata da gateway
  - Setup iniziale più complesso

**2. Rischi principali** (0.5 punti per rischio):

*Proposta A*:
- Interruzione connettività → sistema non funziona
- Limite rate ThingSpeak gratuito (15 sec tra update)
- Costo energetico: ESP32 WiFi consuma molto (batterie non durano)

*Proposta B*:
- Single point of failure: se gateway si guasta, tutte le serre offline
- Range LoRa: 10 ettari potrebbero richiedere più gateway
- Complessità manutentiva: server locale da gestire

**3. Raccomandazione** (1 punto - valutare giustificazione):

**Soluzione ibrida consigliata**:
- Base: Proposta B (LoRa + locale) per:
  - Autonomia operativa
  - Controllo real-time irrigazione
  - Basso consumo (batterie solari)
- Aggiunta: Connessione internet gateway per:
  - Backup cloud dati (1 volta/giorno)
  - Notifiche allarmi via Telegram
  - Accesso remoto occasionale

**Giustificazione**:
L'agricoltura richiede affidabilità anche senza internet. Il controllo irrigazione deve essere real-time e locale. Il budget di 100€/serra è compatibile con Arduino Nano (3€) + LoRa (8€) + sensori (20€) + relay (5€) + pannello solare (15€) = ~50€, lasciando margine.

**4. Uso IA nello sviluppo** (0.5 punti):
- Generazione codice LoRa per Arduino
- Configurazione InfluxDB e Grafana dashboard
- Algoritmi di ottimizzazione irrigazione
- Script Python per analisi dati storici
- Debugging problemi comunicazione
- Documentazione tecnica automatica

---

## PARTE PRATICA - 60 PUNTI

### Modalità di Svolgimento

La parte pratica consiste nello sviluppo completo di un progetto embedded/IoT scelto tra le opzioni proposte. Il candidato dovrà:

1. **Analizzare i requisiti** (15 min)
2. **Progettare la soluzione** con aiuto IA (30 min)
3. **Implementare il codice** (2 ore)
4. **Testare e debuggare** (1 ora)
5. **Documentare** (30 min)
6. **Preparare presentazione** (15 min)

### Strumenti Consentiti

- ✅ Accesso a LLM (ChatGPT, Claude, ecc.)
- ✅ Documentazione ufficiale (Arduino, datasheets)
- ✅ IDE Arduino / PlatformIO
- ✅ Materiali del corso
- ❌ Comunicazione con altri candidati
- ❌ Codice pre-scritto personale (librerie pubbliche OK)

### Hardware Fornito

Per tutti i progetti:
- Arduino Uno / Nano o ESP32 (a scelta)
- Breadboard, cavi jumper
- Alimentatore USB
- Computer con IDE preinstallato

Componenti specifici per progetto (vedi sezione progetti)

---

## PROGETTI D'ESAME

### Progetto 1: Sistema di Monitoraggio Ambientale

#### Descrizione
Realizzare un sistema che monitora temperatura, umidità e qualità dell'aria, visualizza i dati su display LCD e invia allarmi quando valori superano soglie configurabili.

#### Requisiti Funzionali

**RF1 - Acquisizione Dati** (10 punti)
- Leggere temperatura e umidità da sensore DHT22 ogni 2 secondi
- Leggere qualità aria da sensore MQ-135 ogni 5 secondi
- Validare letture (gestire errori sensore)
- Calcolare media mobile su 5 campioni per stabilizzare letture

**RF2 - Visualizzazione** (8 punti)
- Display LCD I2C 16x2 mostra:
  - Riga 1: `T:XX.XC H:XX%`
  - Riga 2: `Air:XXX [OK/WARN]`
- Aggiornamento display ogni secondo
- Backlight lampeggia in caso di allarme

**RF3 - Sistema Allarmi** (10 punti)
- LED verde: tutto OK
- LED giallo: warning (un parametro fuori soglia)
- LED rosso + buzzer: allarme critico (più parametri fuori soglia)
- Soglie configurabili via costanti:
  ```cpp
  const float TEMP_MIN = 18.0;
  const float TEMP_MAX = 28.0;
  const float HUM_MIN = 30.0;
  const float HUM_MAX = 60.0;
  const int AIR_QUALITY_MAX = 400;
  ```

**RF4 - Logging** (7 punti)
- Salvare dati su SD card ogni 10 secondi in formato CSV
- Formato: `timestamp,temp,hum,air_quality,alarm_status`
- Gestire errori SD card (LED dedicato)
- File naming: `LOG_GGMMAA.CSV`

#### Requisiti Non Funzionali

- Codice modulare con funzioni chiare
- Commenti esplicativi
- Gestione robusta degli errori
- Consumo memoria < 70% SRAM disponibile

#### Hardware Fornito

- Arduino Uno / ESP32
- Sensore DHT22
- Sensore MQ-135 (gas/qualità aria)
- Display LCD 16x2 I2C
- Modulo SD card
- 3x LED (verde, giallo, rosso)
- Buzzer passivo
- Resistenze, cavi

#### Schema di Massima

```
Arduino Uno:
- DHT22 → Pin 2 (digitale)
- MQ-135 → Pin A0 (analogico)
- LCD I2C → SDA (A4), SCL (A5)
- SD Card → SPI (MISO 12, MOSI 11, SCK 13, CS 10)
- LED Verde → Pin 5 + resistenza 220Ω
- LED Giallo → Pin 6 + resistenza 220Ω
- LED Rosso → Pin 7 + resistenza 220Ω
- Buzzer → Pin 8
```

#### Criteri di Valutazione

| Criterio | Punti | Descrizione |
|----------|-------|-------------|
| **Funzionalità** | 35 | |
| - Lettura sensori corretta | 10 | Valori accurati, gestione errori |
| - Display funzionante | 8 | Formattazione corretta, aggiornamenti |
| - Sistema allarmi | 10 | Logica corretta, LED e buzzer |
| - Logging SD card | 7 | File CSV valido, timestamp |
| **Documentazione** | 10 | |
| - Schema circuito | 3 | Fritzing o disegno chiaro |
| - Commenti codice | 3 | Funzioni documentate |
| - README | 4 | Installazione, uso, troubleshooting |
| **Presentazione** | 10 | |
| - Demo funzionante | 4 | Mostra tutte le funzionalità |
| - Spiegazione tecnica | 4 | Scelte progettuali, difficoltà |
| - Risposte domande | 2 | Chiarezza e correttezza |
| **Uso IA** | 5 | |
| - Prompt efficaci | 2 | Documentati in file PROMPTS.md |
| - Integrazione codice | 2 | IA usata per parti complesse |
| - Personalizzazione | 1 | Non solo copia-incolla |

---

### Progetto 2: Data Logger Industriale

#### Descrizione
Sistema di acquisizione dati ad alta frequenza per simulare un ambiente industriale, con campionamento di segnali analogici, calcolo statistico e trasmissione seriale.

#### Requisiti Funzionali

**RF1 - Acquisizione Multi-Canale** (12 punti)
- Leggere 4 canali analogici (A0-A3) a 100 Hz
- Buffer circolare per 1000 campioni per canale
- Timestamp campioni con precisione millisecondo
- Interrupt-driven per garantire frequenza stabile

**RF2 - Elaborazione Dati** (10 punti)
- Calcolare ogni secondo per ogni canale:
  - Valore medio
  - Valore minimo e massimo
  - Deviazione standard
- Rilevare anomalie: valori fuori da ±2σ dalla media
- Contatore anomalie per canale

**RF3 - Interfaccia Seriale** (8 punti)
- Comunicazione UART a 115200 baud
- Comandi testuali:
  - `START` - inizia acquisizione
  - `STOP` - ferma acquisizione
  - `STATUS` - mostra statistiche
  - `RESET` - azzera contatori
  - `DUMP` - scarica buffer ultimi 100 campioni
- Protocollo: comando + `\n`, risposta + checksum

**RF4 - Visualizzazione** (5 punti)
- LED per ogni canale: lampeggia a ogni anomalia
- Display OLED SSD1306 mostra:
  ```
  CH1: 512 [OK]
  CH2: 487 [!]
  CH3: 501 [OK]
  CH4: 523 [OK]
  Rate: 100 Hz
  ```

#### Criteri di Valutazione

| Criterio | Punti |
|----------|-------|
| **Funzionalità** | 35 |
| - Acquisizione 100 Hz stabile | 12 |
| - Calcoli statistici corretti | 10 |
| - Protocollo seriale completo | 8 |
| - Visualizzazione OLED | 5 |
| **Documentazione** | 10 |
| **Presentazione** | 10 |
| **Uso IA** | 5 |

---

### Progetto 3: Controllore PID per Temperatura

#### Descrizione
Implementare un sistema di controllo PID per mantenere una temperatura target, utilizzando un elemento riscaldante (simulato con LED PWM) e un sensore di temperatura.

#### Requisiti Funzionali

**RF1 - Controllo PID** (15 punti)
- Implementare controllore PID completo:
  ```cpp
  output = Kp * error + Ki * integral + Kd * derivative
  ```
- Parametri regolabili:
  - Kp (proporzionale): 2.0 - 10.0
  - Ki (integrale): 0.1 - 2.0
  - Kd (derivativo): 0.1 - 5.0
- Anti-windup per termine integrale
- Derivata filtrata (media mobile) per ridurre rumore
- Output limitato 0-255 (PWM)

**RF2 - Interfaccia Utente** (10 punti)
- Display LCD 20x4 mostra:
  ```
  Setpoint: 25.0 C
  Current:  24.3 C
  Output:   142 (55%)
  Kp:2.5 Ki:0.5 Kd:1.2
  ```
- 3 pulsanti per regolare:
  - Btn 1: Setpoint ±0.5°C
  - Btn 2: Kp ±0.1
  - Btn 3: Ki ±0.05
  - Btn 4: Kd ±0.1
- Rotary encoder per navigazione menu

**RF3 - Tuning Assistito** (5 punti)
- Modalità auto-tuning (metodo Ziegler-Nichols):
  1. Aumenta Kp fino a oscillazione sostenuta
  2. Misura periodo oscillazione (Pu)
  3. Calcola: Kp=0.6Ku, Ki=1.2Ku/Pu, Kd=0.075KuPu
- Salva parametri ottimali in EEPROM
- Possibilità ripristino valori salvati

---

## CRITERI DI VALUTAZIONE DETTAGLIATI

### Griglia di Valutazione Parte Pratica

#### 1. Funzionalità (35 punti)

**Eccellente (32-35 punti)**:
- Tutti i requisiti funzionali implementati
- Codice robusto con gestione errori completa
- Performance ottimali (timing, memoria)
- Funzionalità aggiuntive pertinenti

**Buono (28-31 punti)**:
- Requisiti principali implementati
- Gestione errori presente ma non esaustiva
- Performance accettabili
- Alcune funzionalità mancanti non critiche

**Sufficiente (21-27 punti)**:
- Funzionalità di base implementate
- Gestione errori minima
- Performance limite
- Requisiti secondari mancanti

**Insufficiente (<21 punti)**:
- Funzionalità incomplete
- Errori frequenti
- Performance inadeguate

#### 2. Documentazione (10 punti)

**Componenti richiesti**:

**Schema Circuito (3 punti)**:
- 3 punti: Schema Fritzing o disegno chiaro con tutti i componenti, valori resistenze, collegamenti etichettati
- 2 punti: Schema completo ma poco chiaro o senza valori
- 1 punto: Schema parziale o confuso
- 0 punti: Schema assente

**Commenti Codice (3 punti)**:
- 3 punti: Tutte le funzioni documentate con scopo, parametri, return. Sezioni complesse spiegate
- 2 punti: Funzioni principali documentate, commenti presenti
- 1 punto: Commenti sporadici
- 0 punti: Codice senza commenti

**README.md (4 punti)**:
Deve contenere:
```markdown
# Nome Progetto

## Descrizione
Breve descrizione del progetto e obiettivi

## Hardware Richiesto
- Lista componenti con quantità
- Collegamenti (riferimento a schema)

## Software
- Librerie necessarie (con versioni)
- Istruzioni installazione

## Utilizzo
- Procedura di avvio
- Comandi/interfaccia disponibili
- Esempi di output

## Troubleshooting
- Problemi comuni e soluzioni

## Note di Sviluppo
- Difficoltà incontrate
- Come l'IA ha aiutato (riferimento a PROMPTS.md)
```

#### 3. Presentazione (10 punti)

**Demo Funzionante (4 punti)**:
- 4: Demo completa di tutte le funzionalità, fluida, senza errori
- 3: Demo funziona ma con qualche imperfezione
- 2: Demo parziale, funzionalità limitate
- 1: Demo problematica, molti errori
- 0: Demo non funzionante

**Spiegazione Tecnica (4 punti)**:
Valuta:
- Chiarezza nell'esporre architettura software
- Giustificazione scelte progettuali
- Spiegazione parti complesse (PID, interrupt, protocolli)
- Discussione difficoltà e soluzioni

**Risposte Domande (2 punti)**:
La commissione farà 3-5 domande su:
- Dettagli implementazione
- Alternative progettuali
- Modifiche future
- Concetti teorici applicati

#### 4. Uso IA e Metodologia (5 punti)

**PROMPTS.md richiesto**:
Il candidato deve documentare i prompt usati:

```markdown
# Prompt Utilizzati

## Fase 1: Analisi Requisiti
**Prompt**: "Analizza questi requisiti per un sistema di [...]
          Suggerisci architettura software modulare e componenti hardware"
**Risultato**: [sintesi risposta IA]
**Utilizzato**: [cosa hai preso dalla risposta]

## Fase 2: Implementazione Buffer Circolare
**Prompt**: "Implementa una classe C++ per buffer circolare thread-safe
          per Arduino, con 1000 elementi per 4 canali. Deve supportare [...]"
**Risultato**: [...]
**Modifiche**: Ho modificato [...] perché [...]

## Fase 3: Debug Errore I2C
**Problema**: Display OLED non inizializza
**Prompt**: "Display OLED SSD1306 su Arduino Uno non risponde.
          Indirizzo I2C 0x3C, libreria Adafruit_SSD1306. Codice: [...]
          Scanner I2C non trova dispositivo. Come debuggare?"
**Soluzione**: [...]
```

**Valutazione**:
- 5 punti: Prompt ben strutturati, IA usata strategicamente, codice personalizzato
- 3-4: Prompt discreti, integrazione buona, alcune modifiche
- 1-2: Prompt generici, copia-incolla con modifiche minime
- 0: Nessuna documentazione uso IA o non utilizzata

---

## MATERIALI DI PREPARAZIONE

### Checklist Pre-Esame

**1 Settimana Prima**:
- [ ] Ripassare teoria LLM e prompt engineering
- [ ] Rivedere tutti i progetti del corso
- [ ] Testare hardware su tutti i progetti proposti
- [ ] Installare librerie necessarie
- [ ] Preparare template documentazione

**3 Giorni Prima**:
- [ ] Simulazione parte teorica (quiz completo)
- [ ] Implementare un progetto simile da zero in 4 ore
- [ ] Esercitarsi su presentazioni (timing 15 min)

**1 Giorno Prima**:
- [ ] Verificare IDE funzionante e aggiornato
- [ ] Account LLM attivo e funzionante
- [ ] Ripassare formule (PID, conversioni ADC, ecc.)
- [ ] Dormire bene!

### Quiz di Auto-Valutazione

#### Set Aggiuntivo Domande Multiple (per esercitazione)

**21.** Quale funzione C permette di allocare memoria inizializzata a zero?
- a) `malloc()`
- b) `calloc()`
- c) `realloc()`
- d) `alloc()`

**Risposta**: b) `calloc()`

---

**22.** In Arduino, quale funzione configura un pin come output?
- a) `setOutput(pin)`
- b) `pinMode(pin, OUTPUT)`
- c) `configPin(pin, OUT)`
- d) `pinOutput(pin)`

**Risposta**: b)

---

**23.** Qual è la tensione di riferimento predefinita per l'ADC di Arduino Uno?
- a) 3.3V
- b) 5V
- c) 1.1V
- d) 2.5V

**Risposta**: b) 5V (può essere cambiata con `analogReference()`)

---

**24.** Quale libreria Arduino supporta il protocollo I2C?
- a) `SPI.h`
- b) `Wire.h`
- c) `Serial.h`
- d) `I2C.h`

**Risposta**: b) `Wire.h`

---

**25.** In un controllo PID, il termine derivativo serve a:
- a) Correggere errori accumulati nel tempo
- b) Anticipare variazioni future basandosi sulla velocità di cambiamento
- c) Reagire all'errore attuale
- d) Filtrare il rumore

**Risposta**: b)

---

### Esercizi Pratici di Preparazione

#### Esercizio 1: Debouncing Pulsante

**Obiettivo**: Implementare debouncing software per pulsante senza usare `delay()`.

**Requisiti**:
- Pulsante su pin 2 con pull-up interno
- LED su pin 13 che togola a ogni pressione
- Debounce time: 50 ms
- Usare tecnica con timestamp `millis()`

**Soluzione**:
```cpp
const int buttonPin = 2;
const int ledPin = 13;

bool ledState = LOW;
bool lastButtonState = HIGH;
bool currentButtonState = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, ledState);
}

void loop() {
  // Leggi stato pulsante
  bool reading = digitalRead(buttonPin);

  // Se lo stato è cambiato, resetta timer debounce
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  // Se è passato abbastanza tempo, considera il nuovo stato
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Se lo stato è davvero cambiato
    if (reading != currentButtonState) {
      currentButtonState = reading;

      // Solo sul fronte di discesa (pressione)
      if (currentButtonState == LOW) {
        ledState = !ledState;
        digitalWrite(ledPin, ledState);
      }
    }
  }

  lastButtonState = reading;
}
```

---

#### Esercizio 2: Media Mobile

**Obiettivo**: Filtrare lettura sensore analogico con media mobile.

**Requisiti**:
- Potenziometro su A0
- Calcolare media su 10 campioni
- Stampare valore raw e filtrato su Serial
- Update 10 volte al secondo

**Soluzione**:
```cpp
const int sensorPin = A0;
const int numReadings = 10;

int readings[numReadings];
int readIndex = 0;
int total = 0;
int average = 0;

void setup() {
  Serial.begin(9600);

  // Inizializza array a 0
  for (int i = 0; i < numReadings; i++) {
    readings[i] = 0;
  }
}

void loop() {
  // Sottrai lettura vecchia
  total = total - readings[readIndex];

  // Leggi nuovo valore
  readings[readIndex] = analogRead(sensorPin);

  // Aggiungi nuova lettura
  total = total + readings[readIndex];

  // Avanza indice circolare
  readIndex = (readIndex + 1) % numReadings;

  // Calcola media
  average = total / numReadings;

  // Stampa risultati
  Serial.print("Raw: ");
  Serial.print(readings[(readIndex - 1 + numReadings) % numReadings]);
  Serial.print(" | Filtered: ");
  Serial.println(average);

  delay(100);  // 10 Hz
}
```

---

## PORTFOLIO PROFESSIONALE

### Struttura Portfolio

Il portfolio è un elemento fondamentale per presentarsi nel mondo del lavoro. Deve mostrare competenze concrete attraverso progetti realizzati.

#### Repository GitHub

**Organizzazione consigliata**:
```
github.com/tuousername/
├── embedded-environmental-monitor/
│   ├── README.md
│   ├── hardware/
│   │   ├── schematic.png
│   │   ├── fritzing_diagram.fzz
│   │   └── BOM.csv
│   ├── firmware/
│   │   ├── src/
│   │   ├── lib/
│   │   └── platformio.ini
│   ├── docs/
│   │   ├── user_manual.pdf
│   │   └── technical_report.md
│   └── media/
│       ├── demo_video.mp4
│       └── photos/
├── industrial-data-logger/
│   └── ...
└── pid-temperature-controller/
    └── ...
```

---

## SIMULAZIONI D'ESAME

### Simulazione Completa 1

**Tempo: 6 ore**

#### Parte Teorica (90 minuti)

**Quiz**: Usa il set di 30 domande fornito, seleziona casualmente 20

**Domande Aperte** (scegli 3 su 5):
1. Spiega cosa sono i token in un LLM e perché limitano la lunghezza delle interazioni
2. Descrivi il ciclo di vita della memoria in C: stack, heap, memoria statica
3. Confronta UART, I2C e SPI: velocità, complessità, applicazioni
4. Cos'è un watchdog timer e perché è importante in sistemi embedded?
5. Descrivi l'architettura di un sistema IoT completo (device → cloud → app)

**Analisi Critica**:
Caso: Debug di un sistema con ESP32 che perde pacchetti WiFi quando legge da sensore I2C.

#### Parte Pratica (4 ore)

**Progetto**: Realizza un sistema di allarme con:
- Sensore movimento PIR
- Sensore porta (reed switch)
- Tastierino 4x4 per codice accesso
- Sirena (buzzer)
- Display LCD con stato sistema
- LED RGB per indicazione stato (verde=disarmato, giallo=armato, rosso=allarme)

**Funzionalità**:
1. Sistema si arma/disarma con codice 4 cifre
2. Se rileva movimento o porta aperta quando armato → allarme
3. Delay 30 secondi per inserire codice prima dell'allarme
4. Storico ultimi 10 eventi su SD card
5. Cambio codice via menu su tastierino

**Documenta**:
- Schema Fritzing
- Codice commentato
- README con istruzioni
- PROMPTS.md con interazioni IA

---

## CERTIFICAZIONE E CAREER PATH

### Certificato ITS

Al superamento dell'esame (≥60/100) viene rilasciato:

**Certificato di Competenza**:
```
ISTITUTO TECNICO SUPERIORE [Nome]

Certifica che

[Nome Cognome]

ha completato con successo il corso

FONDAMENTI DI INTELLIGENZA ARTIFICIALE
PER LA PROGRAMMAZIONE

Durata: 80 ore
Anno: 2025
Votazione: XX/100

Competenze acquisite:
✓ Prompt Engineering e uso strategico di Large Language Models
✓ Programmazione C (standard C99, gestione memoria, puntatori)
✓ Sviluppo firmware Arduino (Uno, Mega, Nano)
✓ Sistemi Embedded e IoT (ESP32, protocolli I2C/SPI/UART)
✓ Integrazione sensori e attuatori
✓ Controllo PID e automazione
✓ Cloud connectivity (MQTT, HTTP)
✓ Data logging e visualizzazione
✓ Debugging e testing sistemi real-time

[Data]                                    [Firma Direttore]
```

### Livelli di Merito

- **100/100**: Eccellenza - con lode
- **90-99**: Ottimo - menzione speciale
- **75-89**: Buono
- **60-74**: Sufficiente

### Sbocchi Professionali

**Ruoli Entry-Level**:
1. **Junior Embedded Developer**
   - Sviluppo firmware per dispositivi IoT
   - Testing e debugging
   - RAL: 22.000-28.000€

2. **IoT Technician**
   - Installazione e configurazione sistemi
   - Manutenzione dispositivi
   - RAL: 20.000-26.000€

3. **Technical Support Specialist (Embedded)**
   - Assistenza clienti su prodotti embedded
   - Troubleshooting remoto
   - RAL: 20.000-25.000€

4. **Automation Technician**
   - Programmazione PLC e microcontrollori
   - Integrazione sistemi industriali
   - RAL: 24.000-30.000€

**Aziende Tipiche**:
- Produttori dispositivi IoT
- System integrator automazione industriale
- Startup hardware/IoT
- Aziende domotica
- Automotive (sistemi embedded)

### Percorsi di Crescita

**Dopo 2-3 anni esperienza**:
- **Embedded Software Engineer** (RAL 30.000-45.000€)
- **IoT Solution Architect** (RAL 35.000-50.000€)
- **R&D Engineer** (RAL 32.000-48.000€)

**Certificazioni aggiuntive consigliate**:
- Arduino Certification (ufficiale)
- Certified LoRaWAN Professional
- AWS IoT Specialty
- Microsoft Azure IoT Developer

### Continuazione Studi

**Università (Laurea Triennale)**:
- Ingegneria Elettronica
- Ingegneria Informatica
- Computer Engineering

Il certificato ITS può dare crediti formativi (CFU) riconosciuti da alcuni atenei.

**Corsi Specializzazione**:
- Master in IoT e Industry 4.0
- Corso avanzato Machine Learning su Edge
- Specializzazione RTOS (Real-Time Operating Systems)

---

## RISORSE AGGIUNTIVE

### Siti Web Consigliati

**Documentazione Tecnica**:
- [Arduino Reference](https://www.arduino.cc/reference/) - Reference ufficiale funzioni
- [ESP32 Docs](https://docs.espressif.com/) - Documentazione Espressif
- [AVR Libc](https://www.nongnu.org/avr-libc/) - Libreria C per AVR

**Community e Forum**:
- [Arduino Forum](https://forum.arduino.cc/)
- [ESP32 Forum](https://www.esp32.com/)
- [Reddit r/arduino](https://www.reddit.com/r/arduino/)
- [Stack Overflow - Arduino tag](https://stackoverflow.com/questions/tagged/arduino)

**Tutorial e Progetti**:
- [Adafruit Learn](https://learn.adafruit.com/)
- [SparkFun Tutorials](https://learn.sparkfun.com/)
- [Hackster.io](https://www.hackster.io/)
- [Instructables - Arduino](https://www.instructables.com/circuits/arduino/)

---

## NOTE FINALI PER I CANDIDATI

### Consigli per l'Esame

**Gestione del Tempo**:
- Leggi TUTTI i requisiti prima di iniziare
- Pianifica: 30 min design, 2h coding core, 1h testing, 30 min docs
- Non perfezionare troppo una funzionalità a scapito di altre

**Uso dell'IA**:
- ✅ Usa IA per generare codice boilerplate
- ✅ Usa IA per debugging errori specifici
- ✅ Usa IA per capire datasheets e protocolli
- ❌ Non copiare codice senza capirlo
- ❌ Non dipendere 100% dall'IA per la logica

**Debugging**:
- Usa Serial.print() generosamente durante sviluppo
- Testa una funzionalità alla volta
- Se bloccato su un bug >20 min, documenta il problema e vai avanti

**Documentazione**:
- Scrivi README man mano che sviluppi, non alla fine
- Fai screenshot/foto del sistema funzionante
- Salva versioni intermedie del codice (git commit frequenti)

### Mindset Giusto

Questo esame non valuta solo competenze tecniche, ma anche:
- **Problem solving**: Affrontare problemi nuovi con metodo
- **Resourcefulness**: Usare strumenti disponibili (IA, docs, forum)
- **Comunicazione**: Spiegare scelte tecniche chiaramente
- **Pragmatismo**: Soluzioni funzionanti > soluzioni "perfette"

**Ricorda**: L'obiettivo è dimostrare che sai sviluppare sistemi embedded reali, usando l'IA come strumento professionale, non come stampella.

### Cosa Fare se Non Passi

- Revisiona correzioni con docente
- Identifica aree deboli (teoria vs pratica)
- Esercitati su progetti simili
- Seconda opportunità disponibile dopo 1 mese

---

## APPENDICE: FORMULE E REFERENCE RAPIDO

### Conversioni ADC

**Arduino Uno (10-bit ADC, 5V reference)**:
```cpp
float voltage = analogRead(pin) * (5.0 / 1023.0);
```

**ESP32 (12-bit ADC, 3.3V reference)**:
```cpp
float voltage = analogRead(pin) * (3.3 / 4095.0);
```

### Voltage Divider

```
Vout = Vin * (R2 / (R1 + R2))
```

Calcolare R2 per Vout desiderato:
```cpp
// Esempio: Vin=5V, vogliamo Vout=3.3V per ESP32, R1=1kΩ
float R2 = R1 * (Vout / (Vin - Vout));
// R2 = 1000 * (3.3 / (5.0 - 3.3)) = 1941Ω (usa 2kΩ standard)
```

### Resistenza LED

```
R = (Vsupply - Vled) / Iled

Esempio LED rosso (Vled=2V, Iled=20mA, Vsupply=5V):
R = (5 - 2) / 0.02 = 150Ω (usa 220Ω per sicurezza)
```

### PWM Duty Cycle

```
DutyCycle% = (Ton / Tperiod) * 100

Arduino:
analogWrite(pin, value);  // value: 0-255
DutyCycle% = (value / 255) * 100
```

### PID Formule

**Formula completa**:
```
output(t) = Kp * e(t) + Ki * ∫e(τ)dτ + Kd * (de(t)/dt)
```

**Implementazione discreta**:
```cpp
error = setpoint - measurement;
P = Kp * error;
integral += error * dt;
I = Ki * integral;
derivative = (error - previous_error) / dt;
D = Kd * derivative;
output = P + I + D;
```

**Ziegler-Nichols (metodo oscillazione)**:
```
Ku = Kp critico (punto di oscillazione sostenuta)
Tu = Periodo oscillazione

Kp = 0.6 * Ku
Ki = 1.2 * Ku / Tu
Kd = 0.075 * Ku * Tu
```

---

## CONCLUSIONE

Questo esame rappresenta la culminazione del percorso formativo **"Fondamenti di Intelligenza Artificiale per la Programmazione"**. Non è solo una verifica di conoscenze, ma un'opportunità per dimostrare la capacità di affrontare problemi reali utilizzando le tecnologie moderne, inclusa l'IA, come strumenti professionali.

Le competenze acquisite - dal prompt engineering alla programmazione embedded, dal controllo PID all'IoT - sono direttamente spendibili nel mercato del lavoro e costituiscono una solida base per ulteriori specializzazioni.

**In bocca al lupo a tutti i candidati!**

---

*Documento redatto: Dicembre 2025*
*Versione: 2.0*
*ITS [Nome Istituto] - Corso Fondamenti IA 2025*

---

**FINE MODULO 6 - FINE CORSO**
