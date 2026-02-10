# Analisi del Generatore Sinusoidale Arduino

## Panoramica

Questo è un generatore di segnali sinusoidali didattico per ESP32/Arduino che simula un convertitore digitale-analogico (DAC) a 12 bit con uscita nell'intervallo 0-4096.

## Scopo del Programma

Il programma genera una sinusoide campionata con parametri configurabili dinamicamente via porta seriale. È progettato specificamente per scopi didattici nell'insegnamento di:

- Elaborazione digitale dei segnali (DSP)
- Concetti di tempo discreto
- Teoria del campionamento
- Conversione analogico-digitale

## Architettura Software

### Caratteristiche Principali

- **Nessun interrupt hardware**: tutta la logica è gestita nel loop principale
- **Nessun FreeRTOS**: implementazione single-threaded pura
- **Temporizzazione basata su `micros()`**: precisione al microsecondo
- **Gestione non bloccante**: la lettura seriale non blocca la generazione del segnale

### Struttura del Codice

Il programma è organizzato in sezioni logiche:

1. **Parametri di base** (righe 32-40): costanti di sistema
2. **Parametri runtime** (righe 42-50): variabili configurabili
3. **Variabili di supporto** (righe 52-71): stato interno
4. **Funzioni di utilità** (righe 73-81): helper functions
5. **Setup e Loop** (righe 83-199): logica principale

## Parametri Configurabili

### Costanti di Sistema

- `SERIAL_BAUD`: 115200 baud (velocità comunicazione seriale)
- `SIGNAL_MAX`: 4096.0 (ampiezza massima, risoluzione 12 bit)

### Parametri Runtime

- `signalFreq`: frequenza del segnale sinusoidale in Hz (default: 1.0 Hz)
- `sampleRate`: frequenza di campionamento in Hz (default: 100.0 Hz)
- `Ts_us`: periodo di campionamento in microsecondi (calcolato come 1/sampleRate)

### Variabili di Stato

- `streaming`: flag booleano per abilitare/disabilitare l'output
- `sampleIndex`: contatore dei campioni generati (indice temporale discreto n)
- `lastSampleTime_us`: timestamp dell'ultimo campione generato

## Interfaccia Utente (Comandi Seriali)

Il programma accetta i seguenti comandi via porta seriale:

| Comando | Descrizione | Esempio |
|---------|-------------|---------|
| `f <Hz>` | Imposta la frequenza del segnale | `f 50` |
| `sr <Hz>` | Imposta la frequenza di campionamento | `sr 1000` |
| `on` | Abilita lo streaming dei dati | `on` |
| `off` | Disabilita lo streaming dei dati | `off` |
| `h` | Mostra l'help con i comandi disponibili | `h` |

## Algoritmo di Generazione

### 1. Gestione Comandi Seriali (righe 113-157)

```cpp
while (Serial.available()) {
    char c = Serial.read();
    
    if (c == '\n' || c == '\r') {
        // Processa comando completo
        cmdLine.trim();
        
        if (cmdLine == "on") {
            streaming = true;
        }
        // ... altri comandi
        
        cmdLine = "";
    } else {
        cmdLine += c;
    }
}
```

**Caratteristiche**:
- Parser non bloccante che accumula caratteri
- Riconosce `\n` e `\r` come terminatori di comando
- Usa `String.startsWith()` per comandi con parametri

### 2. Temporizzazione (righe 162-168)

```cpp
uint32_t now_us = micros();

if (now_us - lastSampleTime_us >= Ts_us) {
    lastSampleTime_us += Ts_us;  // Accumula invece di resettare
    
    if (streaming) {
        // Genera campione
    }
}
```

**Strategia temporale**:
- Usa `micros()` per ottenere timestamp ad alta risoluzione
- **Accumula il periodo** invece di resettare: `lastSampleTime_us += Ts_us`
- Questa tecnica previene la deriva temporale (drift) nel lungo periodo

### 3. Calcolo Tempo Discreto (riga 176)

```cpp
float t = (float)sampleIndex / sampleRate;
```

**Formula**: t = n / Fs

Dove:
- `n` = sampleIndex (indice del campione)
- `Fs` = sampleRate (frequenza di campionamento)
- `t` = tempo continuo equivalente

### 4. Generazione Sinusoide (righe 181-187)

```cpp
// Sinusoide normalizzata [-1 .. +1]
float s = sinf(2.0f * PI * signalFreq * t);

// Trasformazione in [0 .. 4096]
float y = SIGNAL_MAX * (s + 1.0f) * 0.5f;
```

**Processo**:

1. **Generazione**: s(t) = sin(2π · f · t)
   - Risultato: valore nell'intervallo [-1, +1]

2. **Offset**: (s + 1) / 2
   - Sposta l'intervallo a [0, 1]

3. **Scaling**: SIGNAL_MAX × risultato
   - Scala a [0, 4096] (risoluzione 12 bit)

### 5. Output Seriale (riga 193)

```cpp
Serial.println(y, 2);
```

- Stampa il valore con 2 cifre decimali
- **Una sola colonna**: ottimizzato per Arduino Serial Plotter
- Incrementa `sampleIndex` dopo ogni campione

## Analisi Matematica

### Teorema di Nyquist

Per evitare aliasing, deve valere:

**Fs ≥ 2 × f_max**

Dove:
- `Fs` = frequenza di campionamento (sampleRate)
- `f_max` = frequenza massima del segnale (signalFreq)

**Esempio**:
- Se `signalFreq = 50 Hz`, serve `sampleRate ≥ 100 Hz`
- Il programma non verifica questa condizione automaticamente

### Risoluzione Temporale

Il periodo di campionamento minimo dipende da:

1. **Velocità del processore**: ESP32 può gestire campionamenti molto rapidi
2. **Overhead di Serial.println()**: limita la frequenza massima pratica
3. **Calcoli in virgola mobile**: `sinf()` richiede alcuni cicli CPU

**Stima pratica**:
- Con `Serial.println()`: Fs_max ≈ 10-20 kHz
- Senza output seriale: Fs_max > 100 kHz

## Punti di Forza

### 1. Codice Didattico Eccellente
- Commenti dettagliati in italiano
- Struttura chiara e modulare
- Uso di costanti simboliche

### 2. Gestione Temporale Accurata
```cpp
lastSampleTime_us += Ts_us;  // Non: lastSampleTime_us = now_us
```
Accumulando il periodo invece di resettare il timestamp, si previene la deriva cumulativa.

### 3. Interfaccia Flessibile
- Configurazione runtime senza ricompilare
- Feedback immediato sui comandi
- Output ottimizzato per visualizzazione

### 4. Implementazione Semplice
- Nessuna dipendenza esterna (oltre Arduino.h)
- Nessun interrupt o task concorrenti
- Facile da comprendere e modificare

## Limitazioni e Possibili Miglioramenti

### 1. Validazione Input Assente

**Problema**:
```cpp
signalFreq = cmdLine.substring(2).toFloat();
```

Nessun controllo su:
- Valori negativi (`f -10`)
- Zero (`sr 0`)
- Valori eccessivi (`sr 1000000`)

**Soluzione suggerita**:
```cpp
float newFreq = cmdLine.substring(2).toFloat();
if (newFreq > 0 && newFreq < MAX_SIGNAL_FREQ) {
    signalFreq = newFreq;
    Serial.print("freq = ");
    Serial.println(signalFreq);
} else {
    Serial.println("ERRORE: frequenza non valida");
}
```

### 2. Aliasing Non Gestito

**Problema**: Se `signalFreq >= sampleRate / 2`, il segnale campionato non rappresenta correttamente l'originale (violazione teorema di Nyquist).

**Soluzione suggerita**:
```cpp
if (signalFreq >= sampleRate / 2.0f) {
    Serial.println("WARNING: Aliasing! Freq >= Nyquist limit");
}
```

### 3. Overflow di sampleIndex

**Problema**: `uint32_t sampleIndex` va in overflow dopo:
- 4.294.967.296 campioni
- A 100 Hz: dopo ~497 giorni
- A 10 kHz: dopo ~5 giorni

**Soluzione** (se necessario):
```cpp
if (sampleIndex == 0xFFFFFFFF) {
    sampleIndex = 0;
}
```

### 4. Precisione in Virgola Mobile

**Problema**: Per sessioni molto lunghe, l'accumulo di errori di arrotondamento in:
```cpp
float t = (float)sampleIndex / sampleRate;
```

può causare imprecisioni nella fase.

**Soluzione** (per applicazioni critiche):
- Usare `double` invece di `float`
- Implementare reset periodico della fase

### 5. Gestione Overflow micros()

**Problema**: `micros()` va in overflow ogni ~71.6 minuti.

**Nota**: Il codice gestisce correttamente questo caso grazie all'aritmetica modulare degli unsigned:
```cpp
if (now_us - lastSampleTime_us >= Ts_us)
```
Funziona anche dopo overflow.

## Esempi di Utilizzo

### Esempio 1: Segnale Audio (440 Hz - La centrale)

```
> sr 8000          // Sample rate 8 kHz (buono per audio)
sample rate = 8000.00 Hz

> f 440            // La centrale (A4)
freq = 440.00 Hz

> on               // Avvia generazione
streaming ON
```

**Verifica Nyquist**: 440 Hz < 4000 Hz (Fs/2) ✓

### Esempio 2: Segnale Lento (Sensore)

```
> sr 10            // 10 campioni/secondo
sample rate = 10.00 Hz

> f 0.5            // Oscillazione ogni 2 secondi
freq = 0.50 Hz

> on
streaming ON
```

### Esempio 3: Test Aliasing (didattico)

```
> sr 100           // 100 Hz
> f 60             // 60 Hz (vicino a Nyquist limit di 50 Hz)
> on
```

**Risultato atteso**: segnale distorto per effetto aliasing.

## Visualizzazione

### Serial Plotter (Arduino IDE)

1. Carica lo sketch su ESP32/Arduino
2. Apri **Tools → Serial Plotter**
3. Imposta baud rate a **115200**
4. Invia comandi via Serial Monitor
5. Visualizza la sinusoide in tempo reale

### Processing / Python

È possibile catturare i dati seriali per analisi più avanzate:

```python
import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 115200)
samples = []

for i in range(1000):
    line = ser.readline().decode('utf-8').strip()
    samples.append(float(line))

plt.plot(samples)
plt.show()
```

## Estensioni Possibili

### 1. Forme d'Onda Multiple

Aggiungere triangolare, quadra, sawtooth:

```cpp
enum WaveType { SINE, SQUARE, TRIANGLE, SAWTOOTH };
WaveType waveType = SINE;

// Nel loop:
switch(waveType) {
    case SINE:
        s = sinf(2.0f * PI * signalFreq * t);
        break;
    case SQUARE:
        s = (sinf(2.0f * PI * signalFreq * t) > 0) ? 1.0f : -1.0f;
        break;
    // ...
}
```

### 2. Output DAC Reale

ESP32 ha DAC hardware su GPIO25 e GPIO26:

```cpp
#include <driver/dac.h>

void setup() {
    dac_output_enable(DAC_CHANNEL_1);  // GPIO25
}

void loop() {
    // ...
    uint8_t dacValue = (uint8_t)(y / 16.0f);  // 0-4096 -> 0-255
    dac_output_voltage(DAC_CHANNEL_1, dacValue);
}
```

### 3. Sweep di Frequenza

```cpp
float startFreq = 20.0f;
float endFreq = 20000.0f;
float sweepDuration = 10.0f;  // secondi

void loop() {
    float t = (float)sampleIndex / sampleRate;
    float currentFreq = startFreq + (endFreq - startFreq) * (t / sweepDuration);
    // ...
}
```

### 4. Modulazione (AM/FM)

```cpp
// AM (Amplitude Modulation)
float carrier = 1000.0f;     // 1 kHz
float modulator = 10.0f;     // 10 Hz
float s = sinf(2.0f * PI * carrier * t) * 
          (0.5f + 0.5f * sinf(2.0f * PI * modulator * t));
```

## Conclusioni

Questo generatore sinusoidale rappresenta un eccellente esempio di codice didattico per l'insegnamento dell'elaborazione digitale dei segnali. La sua semplicità architettonica lo rende ideale per studenti e maker che vogliono comprendere:

- Il concetto di tempo discreto
- La teoria del campionamento
- L'implementazione pratica di DSP su microcontrollori

I principali pregi sono la chiarezza del codice, la gestione temporale accurata e la flessibilità d'uso. Le limitazioni evidenziate (validazione input, controllo aliasing) sono facilmente risolvibili e rappresentano ottimi esercizi per estendere il progetto.

## Riferimenti Teorici

- **Teorema di Nyquist-Shannon**: Fs ≥ 2 × f_max
- **Frequenza di Nyquist**: f_Nyquist = Fs / 2
- **Aliasing**: fenomeno di distorsione quando f_signal > f_Nyquist
- **Tempo discreto**: t[n] = n / Fs

## Licenza e Uso

Il codice è chiaramente orientato all'uso didattico e può essere liberamente modificato per scopi educativi e di prototipazione.
