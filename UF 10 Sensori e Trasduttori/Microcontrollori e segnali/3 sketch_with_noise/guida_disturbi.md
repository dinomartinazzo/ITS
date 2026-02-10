# Guida ai Disturbi - Generatore Sinusoidale

## Panoramica

Lo sketch ora include 6 tipi di disturbi che possono essere aggiunti e rimossi singolarmente in tempo reale via porta seriale.

## Tipi di Disturbi Disponibili

### 1. **White Noise** (Rumore Bianco Gaussiano)
**Comando**: `add white` / `remove white`

**Caratteristiche**:
- Rumore con distribuzione gaussiana
- Tutte le frequenze hanno la stessa potenza
- Parametro: `whiteNoiseAmplitude = 100.0` (modificabile nel codice)

**Effetto visivo**: Oscillazioni rapide e casuali attorno alla sinusoide

**Uso tipico**: 
- Simulare rumore termico nei circuiti
- Testare algoritmi di filtraggio
- Simulare rumore nei sensori

---

### 2. **Pink Noise** (Rumore 1/f)
**Comando**: `add pink` / `remove pink`

**Caratteristiche**:
- Potenza inversamente proporzionale alla frequenza
- Più "morbido" del rumore bianco
- Filtro passa-basso con coefficiente 0.95
- Parametro: `pinkNoiseAmplitude = 300.0` (aumentata per visibilità)

**Effetto visivo**: Variazioni lente e ondulate, ben visibili sul segnale

**Uso tipico**:
- Simulare rumore flicker nei componenti elettronici
- Rumori ambientali naturali
- Variazioni biologiche

---

### 3. **Impulse Noise** (Impulsi Casuali - Spikes)
**Comando**: `add impulse` / `remove impulse`

**Caratteristiche**:
- Picchi casuali positivi o negativi
- Probabilità di impulso: 1% (default)
- Parametri:
  - `impulseAmplitude = 500.0`
  - `impulseProbability = 0.01` (1%)

**Effetto visivo**: Picchi sporadici che "bucano" il segnale

**Uso tipico**:
- Simulare interferenze elettromagnetiche
- Click nei sistemi audio
- Errori di trasmissione dati
- Artefatti nei sensori

---

### 4. **Sinusoidal Interference** (Interferenza Sinusoidale)
**Comando**: `add sine` / `remove sine`

**Caratteristiche**:
- Sinusoide aggiuntiva sovrapposta
- Frequenza di default: 2.0 Hz
- Parametri:
  - `interferenceFreq = 2.0` Hz
  - `interferenceAmplitude = 200.0`

**Effetto visivo**: Modulazione periodica del segnale originale

**Uso tipico**:
- Simulare interferenza 50/60 Hz dalla rete elettrica
- Crosstalk tra canali
- Interferenze radio
- Battimenti tra frequenze

---

### 5. **DC Drift** (Deriva Lenta)
**Comando**: `add drift` / `remove drift`

**Caratteristiche**:
- Spostamento lineare del livello DC
- Cresce linearmente nel tempo
- Parametro: `driftRate = 5.0` (unità/secondo) - velocità aumentata

**Effetto visivo**: Il segnale si sposta progressivamente verso l'alto in modo ben visibile

**Effetto pratico**: In circa 10-15 secondi il segnale inizierà a saturare verso il limite superiore (4096)

**Uso tipico**:
- Simulare deriva termica nei sensori
- Invecchiamento dei componenti
- Variazioni di offset negli amplificatori
- Batteria che si scarica

---

### 6. **Quantization Noise** (Rumore di Quantizzazione)
**Comando**: `add quant` / `remove quant`

**Caratteristiche**:
- Riduce la risoluzione del segnale
- Default: 5 bit (32 livelli invece di 4096) - ridotto per massima visibilità
- Parametro: `quantizationBits = 5` (range 2-12)

**Effetto visivo**: "Scalini" molto evidenti e ben visibili invece di una curva liscia

**Formula**: 
```
levels = 2^bits = 2^5 = 32 livelli
step = 4096 / 32 = 128 unità per scalino
quantized_value = floor(value / step) * step
```

**Confronto**:
- 12 bit (originale): 4096 livelli → curva liscia
- 8 bit: 256 livelli → scalini poco visibili
- **5 bit: 32 livelli → scalini MOLTO evidenti** ✓
- 4 bit: 16 livelli → scalini enormi

**Uso tipico**:
- Simulare ADC/DAC a bassa risoluzione
- Compressione del segnale
- Artefatti di digitalizzazione

---

### 7. **Scatter Noise** (Nuvola di Punti)
**Comando**: `add scatter` / `remove scatter`

**Caratteristiche**:
- Rumore gaussiano con ampiezza molto elevata
- Trasforma la sinusoide in una "nuvola" di punti sparsi
- Parametro: `scatterAmplitude = 600.0` (6x più forte del white noise)

**Effetto visivo**: La sinusoide scompare completamente e diventa una nuvola di punti distribuiti casualmente

**Distribuzione**: 
- I punti si concentrano comunque attorno alla forma sinusoidale
- Maggiore densità nel centro della sinusoide
- Minore densità agli estremi

**Uso tipico**:
- Simulare misure con errore di lettura molto alto
- Sensori estremamente rumorosi o malfunzionanti
- Test estremi di algoritmi di filtraggio
- Visualizzazione statistica di dati molto dispersi
- Esempio didattico di SNR (Signal-to-Noise Ratio) molto basso

**SNR approssimativo**: ~-15 dB (rumore molto più forte del segnale)

---

## Comandi Seriali

### Comandi Base
```
f <Hz>      → Imposta frequenza del segnale
sr <Hz>     → Imposta sample rate
on          → Avvia lo streaming
off         → Ferma lo streaming
h           → Mostra help
```

### Gestione Disturbi
```
add white       → Aggiungi rumore bianco
add pink        → Aggiungi pink noise
add impulse     → Aggiungi impulsi casuali
add sine        → Aggiungi interferenza sinusoidale
add drift       → Aggiungi deriva DC
add quant       → Aggiungi quantizzazione
add scatter     → Aggiungi nuvola di punti

remove white    → Rimuovi rumore bianco
remove pink     → Rimuovi pink noise
remove impulse  → Rimuovi impulsi
remove sine     → Rimuovi interferenza
remove drift    → Rimuovi deriva
remove quant    → Rimuovi quantizzazione
remove scatter  → Rimuovi nuvola di punti

status          → Mostra quali disturbi sono attivi
```

---

## Esempi di Utilizzo

### Esempio 1: Test Rumore Bianco
```
> on
> add white
Rumore bianco: ON
```
**Risultato**: Sinusoide pulita con piccole oscillazioni casuali

---

### Esempio 2: Combinazione di Disturbi
```
> on
> add white
> add sine
> status
=== DISTURBI ATTIVI ===
  white:  ON
  pink:   off
  impulse:off
  sine:   ON
  drift:  off
  quant:  off
=======================
```
**Risultato**: Sinusoide con rumore bianco + interferenza a 2 Hz

---

### Esempio 3: Effetto Quantizzazione
```
> on
> add quant
Quantizzazione: ON
```
**Risultato**: Sinusoide con "gradini" MOLTO evidenti (32 livelli invece di 4096)
Ogni scalino è alto circa 128 unità, ben visibile sul plotter!

---

### Esempio 4: Simulare Sensore Degradato
```
> on
> add white
> add drift
> add impulse
```
**Risultato**: 
- Rumore di fondo costante (white)
- Deriva progressiva dell'offset (drift)
- Picchi sporadici di interferenza (impulse)

---

### Esempio 5: Test Pink Noise vs White Noise
```
> on
> add pink
[osserva per 20 secondi]
> remove pink
> add white
[confronta visivamente]
```
**Differenza visibile**: Pink noise ha variazioni più lente e "morbide"

---

### Esempio 6: Effetto Scatter (Nuvola di Punti)
```
> on
> add scatter
Scatter (nuvola punti): ON
```
**Risultato**: La sinusoide si trasforma in una nuvola di punti sparsi. I punti sono concentrati statisticamente attorno alla forma sinusoidale ma con dispersione enorme.

**Test interessante**: Rimuovi scatter e aggiungi white noise per confrontare:
```
> remove scatter
> add white
```
Noterai che white noise mantiene visibile la sinusoide, mentre scatter la nasconde completamente.

---

## Combinazioni Interessanti

### Sensore Industriale Realistico
```
add white       // Rumore termico
add sine        // Interferenza 50Hz dalla rete
add impulse     // Click da relè/motori
```

### ADC a Bassa Risoluzione
```
add quant       // Risoluzione limitata
add white       // Rumore LSB
```

### Sensore con Problemi
```
add drift       // Deriva termica
add impulse     // Contatti intermittenti
add pink        // Rumore flicker
```

### Sensore Completamente Guasto
```
add scatter     // Letture totalmente casuali
add impulse     // Picchi sporadici
add drift       // Sistema che si degrada
```

### Test Filtri Passa-Basso
```
add white       // Aggiungi rumore ad alta frequenza
// Poi implementa un filtro e confronta
```

### Studio SNR (Signal-to-Noise Ratio)
```
// Confronta diversi livelli di rumore
add white       // SNR moderato (~20 dB)
remove white
add scatter     // SNR bassissimo (~-15 dB)
```

---

## Parametri Modificabili nel Codice

Se vuoi personalizzare l'intensità dei disturbi, modifica queste variabili nel codice:

```cpp
// Ampiezza disturbi
float whiteNoiseAmplitude = 100.0f;     // Default: 100
float pinkNoiseAmplitude = 300.0f;      // Default: 300 (aumentato)
float impulseAmplitude = 500.0f;        // Default: 500
float interferenceAmplitude = 200.0f;   // Default: 200

// Frequenza interferenza
float interferenceFreq = 2.0f;          // Default: 2 Hz

// Probabilità impulsi (0.01 = 1%)
float impulseProbability = 0.01f;       // Default: 1%

// Velocità deriva
float driftRate = 5.0f;                 // Default: 5.0 unità/sec (aumentato)

// Risoluzione quantizzazione
uint16_t quantizationBits = 5;          // Default: 5 bit (32 livelli - MOLTO visibile!)

// Ampiezza scatter (nuvola di punti)
float scatterAmplitude = 600.0f;        // Default: 600 (molto forte!)
```

### Esempio: Aumentare il Rumore Bianco
```cpp
float whiteNoiseAmplitude = 200.0f;  // Raddoppia l'ampiezza
```

### Esempio: Interferenza a 50 Hz (Rete Elettrica)
```cpp
float interferenceFreq = 50.0f;      // 50 Hz (Europa)
// oppure
float interferenceFreq = 60.0f;      // 60 Hz (USA)
```

---

## Note Tecniche

### Ordine di Applicazione
I disturbi vengono applicati in questo ordine:

1. Generazione sinusoide pulita
2. + Rumore bianco
3. + Pink noise
4. + Impulsi
5. + Interferenza sinusoidale
6. + Deriva DC
7. + Scatter (nuvola di punti)
8. Quantizzazione (sempre per ultima)
9. Clipping a [0, 4096]

### Clipping
Il segnale finale viene limitato al range [0, 4096]:
```cpp
if (y < 0.0f) y = 0.0f;
if (y > SIGNAL_MAX) y = SIGNAL_MAX;
```

Questo significa che disturbi molto forti possono saturare il segnale.

### Generazione Numeri Casuali
- `randomGaussian()`: Approssimazione Box-Muller con 12 campioni uniformi
- Media: 0
- Deviazione standard: ~1
- Range tipico: [-3, +3]

### Pink Noise Filter
Filtro IIR del primo ordine:
```cpp
y[n] = 0.95 * y[n-1] + 0.05 * white_noise[n]
```
Coefficiente 0.95 determina quanto è "colorato" il rumore (più basso = più visibile).

---

## Troubleshooting

### Il segnale scompare dopo un po'
**Problema**: Deriva DC attiva
**Soluzione**: 
```
> remove drift
```
La deriva fa uscire il segnale dal range visualizzabile.

### Gli impulsi sono troppo frequenti/rari
**Problema**: Probabilità impulsi non ottimale
**Soluzione**: Modifica `impulseProbability` nel codice
- Più frequenti: `0.05` (5%)
- Più rari: `0.001` (0.1%)

### La quantizzazione non si vede
**Problema**: Risoluzione ancora troppo alta
**Soluzione**: Con 5 bit dovresti vedere 32 scalini evidenti. Se ancora non si vedono:
- Verifica che il Serial Plotter abbia autoscale attivo
- Prova con 4 bit per scalini ancora più grandi:
```cpp
uint16_t quantizationBits = 4;  // 16 livelli (scalini enormi!)
```
- Con 4 bit ogni scalino è alto 256 unità (4096/16)

### Troppo rumore, non si vede la sinusoide
**Problema**: Ampiezze disturbi troppo alte
**Soluzione**: Riduci le ampiezze nel codice o rimuovi alcuni disturbi:
```
> remove white
> remove pink
```

---

## Progetti Didattici Suggeriti

### 1. Confronto Rumore Bianco vs Pink
Attiva alternativamente i due rumori e osserva le differenze nel dominio del tempo.

### 2. Simulatore ADC
Usa `add quant` con diversi valori di bit per vedere l'effetto della risoluzione:
- **5 bit (default)**: 32 livelli - scalini molto evidenti
- **4 bit**: 16 livelli - scalini enormi
- **6 bit**: 64 livelli - scalini moderati
- **8 bit**: 256 livelli - scalini piccoli ma visibili
- **10 bit**: 1024 livelli - quasi liscio

### 3. Filtro Passa-Basso
Aggiungi rumore bianco e poi implementa un filtro software per eliminarlo.

### 4. SNR (Signal-to-Noise Ratio)
Misura il rapporto segnale/rumore con diversi livelli di white noise.

### 5. Rilevamento Impulsi
Aggiungi impulsi e scrivi codice per rilevarli e contarli.

### 6. Analisi SNR con Scatter
Confronta il rapporto segnale/rumore tra white noise e scatter noise. Calcola la deviazione standard dei campioni per quantificare la differenza.

---

## Conclusioni

Questo sistema di disturbi permette di:

- **Testare** algoritmi di filtraggio e noise reduction
- **Simulare** condizioni reali di sensori e sistemi di acquisizione
- **Studiare** l'effetto di diversi tipi di rumore
- **Insegnare** concetti di elaborazione del segnale

La possibilità di aggiungere e rimuovere disturbi singolarmente in tempo reale rende il sistema molto flessibile per esperimenti didattici e test.
