# Guida ai Filtri - Generatore Sinusoidale

## Panoramica

Il sistema ora include **8 tipi di filtri** digitali che possono essere applicati singolarmente o in cascata al segnale (pulito o con disturbi). I filtri sono visualizzati in tempo reale sul Serial Plotter insieme al segnale originale.

## Visualizzazione

Quando **almeno un filtro è attivo**, il Serial Plotter mostra **due tracce**:
- **Prima traccia (blu)**: Segnale RAW (con eventuali disturbi)
- **Seconda traccia (rossa)**: Segnale FILTRATO

Questo permette di confrontare visivamente l'efficacia del filtro in tempo reale!

---

## Filtri Disponibili

### 1. **Simple Average** (Media Aritmetica Semplice)
**Comando**: `filter simple` / `nofilter simple`

**Caratteristiche**:
- Media degli ultimi N campioni
- Parametro: `simpleAvgSamples = 10` (modificabile nel codice)
- Filtro non ricorsivo (FIR)

**Formula**:
```
y[n] = (x[n] + x[n-1] + ... + x[n-N+1]) / N
```

**Effetto**:
- Riduce rumore bianco efficacemente
- Ritardo di N/2 campioni
- Transizione graduale

**Uso tipico**:
- Smoothing generale
- Riduzione rumore ad alta frequenza
- Applicazioni in tempo non critico

**Parametri ottimali**:
- Rumore basso: N = 5-10
- Rumore medio: N = 10-20
- Rumore alto: N = 20-30

---

### 2. **Moving Average** (Media Mobile)
**Comando**: `filter moving` / `nofilter moving`

**Caratteristiche**:
- Media scorrevole su finestra fissa
- Parametro: `movingAvgWindow = 20` (modificabile nel codice)
- Equivalente a Simple Average ma con finestra più ampia

**Formula**:
```
y[n] = (1/W) * Σ(x[n-i]) per i=0 to W-1
```
Dove W = dimensione finestra

**Effetto**:
- Smoothing molto efficace
- Elimina picchi e rumore
- Ritardo proporzionale a W

**Uso tipico**:
- Trend analysis
- Rimozione oscillazioni rapide
- Smoothing robusto

**Confronto con Simple Average**:
- Moving Average: finestra più ampia (default 20)
- Simple Average: finestra più stretta (default 10)
- Usa entrambi per smoothing progressivo!

---

### 3. **Exponential Moving Average (EMA)** (Media Mobile Esponenziale)
**Comando**: `filter ema` / `nofilter ema`

**Caratteristiche**:
- Peso esponenziale decrescente ai campioni vecchi
- Parametro: `emaAlpha = 0.1` (0-1, più basso = più liscio)
- Filtro ricorsivo (IIR) molto efficiente
- Memoria infinita ma decadimento esponenziale

**Formula**:
```
y[n] = α * x[n] + (1-α) * y[n-1]
```
Dove α = emaAlpha

**Effetto**:
- Smoothing reattivo
- Risposta più veloce di moving average
- Ritardo minimo
- Peso maggiore ai campioni recenti

**Uso tipico**:
- Trading e finanza
- Inseguimento di segnali variabili
- Applicazioni real-time

**Parametri α**:
- α = 0.01: molto liscio, lento
- α = 0.1: bilanciato (default)
- α = 0.3: reattivo, veloce
- α = 0.5: molto reattivo

**Relazione con time constant**:
```
α = 2 / (N + 1)
Dove N = numero campioni equivalente
```

---

### 4. **Complementary Filter** (Filtro Complementare)
**Comando**: `filter compl` / `nofilter compl`

**Caratteristiche**:
- Combina alta e bassa frequenza con pesi complementari
- Parametro: `complementaryAlpha = 0.98` (tipicamente 0.95-0.99)
- Usato in sensor fusion (IMU, gyro+accel)

**Formula**:
```
y_low[n] = α * y_low[n-1] + (1-α) * x[n]
y_high[n] = x[n] - y_low[n]
y[n] = y_low[n]  (output passa-basso)
```

**Effetto**:
- Separa componenti lente e veloci
- Configurazione attuale: output passa-basso
- Ottimo per deriva + rumore

**Uso tipico**:
- Fusione sensori (gyro drift + accel noise)
- Rimozione deriva mantenendo dinamica
- Sistemi di navigazione inerziale

**Nota**: α alto (0.98) = più passa-basso, α basso (0.90) = più passa-alto

---

### 5. **Median Filter** (Filtro Mediano)
**Comando**: `filter median` / `nofilter median`

**Caratteristiche**:
- Ordina campioni e prende valore centrale
- Parametro: `medianWindow = 5` (dispari, tipicamente 3-7)
- Filtro non lineare

**Algoritmo**:
1. Preleva ultimi N campioni
2. Ordina in ordine crescente
3. Restituisce valore centrale

**Effetto**:
- **ECCELLENTE per impulsi**: elimina spike completamente
- Preserva bordi e transizioni
- Non introduce blur come media
- Immune a outlier

**Uso tipico**:
- Rimozione impulsi e spike
- Elaborazione immagini (salt & pepper noise)
- Dati con outlier occasionali
- Segnali con transizioni nette

**Dimensione finestra**:
- 3: veloce, rimozione spike singoli
- 5: bilanciato (default)
- 7: robusto contro burst di impulsi

**Confronto con Moving Average**:
- Median: elimina impulsi senza smoothing eccessivo
- Moving: smussa tutto ma diffonde gli impulsi

---

### 6. **Kalman Filter** (Filtro di Kalman)
**Comando**: `filter kalman` / `nofilter kalman`

**Caratteristiche**:
- Filtro ottimo per sistemi lineari con rumore gaussiano
- Stima lo stato "vero" da misure rumorose
- Parametri:
  - `kalmanQ = 0.01` (rumore processo)
  - `kalmanR = 1.0` (rumore misura)
- Versione semplificata 1D

**Algoritmo**:
```
PREDICTION:
x_prior = x_prev
P_prior = P_prev + Q

UPDATE:
K = P_prior / (P_prior + R)  (Kalman Gain)
x = x_prior + K * (measurement - x_prior)
P = (1 - K) * P_prior
```

**Effetto**:
- Smoothing ottimale statisticamente
- Bilancia predizione e misura
- Adattivo al rumore
- Convergenza rapida

**Uso tipico**:
- Tracking di oggetti
- GPS e navigazione
- Fusione dati multi-sensore
- Sistemi di controllo

**Tuning parametri**:
- **Q basso** (0.001): sistema molto stabile, cambia lentamente
- **Q medio** (0.01): bilanciato (default)
- **Q alto** (0.1): sistema dinamico, segue misure rapidamente

- **R basso** (0.1): misure affidabili, segue il segnale
- **R medio** (1.0): bilanciato (default)
- **R alto** (10.0): misure rumorose, più smoothing

**Rapporto Q/R**:
- Q/R << 1: filtro conservativo (smoothing pesante)
- Q/R ≈ 1: bilanciato
- Q/R >> 1: filtro reattivo (segue misure)

---

### 7. **Low-Pass Filter** (Filtro Passa-Basso RC)
**Comando**: `filter lowpass` / `nofilter lowpass`

**Caratteristiche**:
- Filtro IIR primo ordine (RC analogico digitalizzato)
- Parametro: `lowPassCutoff = 0.5` Hz (frequenza di taglio)
- Attenua frequenze sopra il cutoff

**Formula**:
```
α = Δt / (RC + Δt)
dove RC = 1 / (2π * f_cutoff)

y[n] = α * x[n] + (1-α) * y[n-1]
```

**Effetto**:
- Rimuove alte frequenze (rumore rapido)
- Preserva basse frequenze (trend, segnale lento)
- Roll-off graduale: -20 dB/decade

**Uso tipico**:
- Anti-aliasing
- Rimozione rumore ad alta frequenza
- Smoothing audio
- Condizionamento sensori

**Frequenza di taglio**:
- 0.1 Hz: molto selettivo, solo trend lentissimi
- **0.5 Hz**: bilanciato per sinusoide 0.1 Hz (default)
- 2.0 Hz: permette più dinamica
- 5.0 Hz: taglio alto, rimuove solo rumore veloce

**Relazione con segnale**:
- Se f_signal = 0.1 Hz e f_cutoff = 0.5 Hz → passa segnale, attenua rumore
- Se f_cutoff < f_signal → attenua anche il segnale!

---

### 8. **High-Pass Filter** (Filtro Passa-Alto)
**Comando**: `filter highpass` / `nofilter highpass`

**Caratteristiche**:
- Filtro IIR primo ordine (differenziatore + passa-basso)
- Parametro: `highPassCutoff = 0.05` Hz (frequenza di taglio)
- Attenua frequenze sotto il cutoff

**Formula**:
```
α = RC / (RC + Δt)
dove RC = 1 / (2π * f_cutoff)

y[n] = α * (y[n-1] + x[n] - x[n-1])
```

**Effetto**:
- Rimuove basse frequenze (deriva DC, offset)
- Preserva alte frequenze (variazioni rapide)
- Blocca componente continua

**Uso tipico**:
- Rimozione deriva DC
- Eliminazione offset
- Accoppiamento AC
- Rilevamento transizioni

**Frequenza di taglio**:
- **0.05 Hz**: blocca deriva lenta (default, buono per drift)
- 0.01 Hz: blocca anche variazioni molto lente
- 0.1 Hz: più aggressivo

**Attenzione**: 
- Se f_cutoff troppo alto → attenua anche il segnale utile!
- Per sinusoide 0.1 Hz, usa f_cutoff << 0.1 Hz

---

## Comandi Seriali

### Attivare Filtri
```
filter simple      → Attiva media semplice
filter moving      → Attiva media mobile
filter ema         → Attiva EMA
filter compl       → Attiva complementare
filter median      → Attiva mediano
filter kalman      → Attiva Kalman
filter lowpass     → Attiva passa-basso
filter highpass    → Attiva passa-alto
```

### Disattivare Filtri
```
nofilter simple    → Disattiva media semplice
nofilter moving    → Disattiva media mobile
nofilter ema       → Disattiva EMA
nofilter compl     → Disattiva complementare
nofilter median    → Disattiva mediano
nofilter kalman    → Disattiva Kalman
nofilter lowpass   → Disattiva passa-basso
nofilter highpass  → Disattiva passa-alto
```

### Status
```
filters            → Mostra filtri attivi
```

---

## Esempi di Utilizzo

### Esempio 1: Rimozione Rumore Bianco
```
> on
> add white
[osserva rumore]
> filter moving
Filtro media mobile: ON
```
**Risultato**: Traccia blu rumorosa, traccia rossa liscia

---

### Esempio 2: Eliminazione Impulsi
```
> on
> add impulse
[vedi spike casuali]
> filter median
Filtro mediano: ON
```
**Risultato**: Gli impulsi spariscono completamente dalla traccia rossa!

---

### Esempio 3: Rimozione Deriva DC
```
> on
> add drift
[vedi segnale che sale]
> filter highpass
Filtro passa-alto: ON
```
**Risultato**: Traccia rossa centrata, deriva eliminata

---

### Esempio 4: Filtri in Cascata
```
> on
> add white
> add impulse
> filter median      # Prima elimina impulsi
> filter moving      # Poi smussa rumore bianco
> filters
=== FILTRI ATTIVI ===
  median:  ON
  moving:  ON
=====================
```
**Risultato**: Segnale super pulito! Median rimuove spike, Moving smussa rumore.

---

### Esempio 5: Confronto EMA vs Moving Average
```
> on
> add white
> filter ema
[osserva per 10 secondi]
> nofilter ema
> filter moving
[confronta]
```
**Differenza**: EMA più reattivo, Moving più liscio

---

### Esempio 6: Kalman su Scatter Noise
```
> on
> add scatter
[nuvola di punti]
> filter kalman
Filtro Kalman: ON
```
**Risultato**: Il Kalman "trova" la sinusoide nella nuvola di punti!

---

### Esempio 7: Passa-Basso per Rumore Veloce
```
> on
> add white
> add sine          # Interferenza 2 Hz
> filter lowpass
# Con lowPassCutoff = 0.5 Hz:
# - Segnale 0.1 Hz: PASSA
# - Rumore bianco: ATTENUATO
# - Interferenza 2 Hz: ATTENUATA
```

---

## Filtri in Cascata

I filtri vengono applicati **nell'ordine seguente**:

1. Simple Average
2. Moving Average
3. EMA
4. Complementary
5. Median
6. Kalman
7. Low-Pass
8. High-Pass

### Strategie Efficaci

#### Anti-Impulse + Smoothing
```
filter median      # Primo: elimina spike
filter moving      # Secondo: smussa residuo
```

#### Anti-Drift + Anti-Noise
```
filter highpass    # Primo: elimina deriva
filter lowpass     # Secondo: elimina rumore veloce
```

#### Optimal Filtering
```
filter median      # Elimina outlier
filter kalman      # Stima ottima
```

### ⚠️ Attenzione all'Ordine!

L'ordine è importante:
- ✅ `median` → `moving` = spike rimossi poi smoothing
- ❌ `moving` → `median` = spike diffusi poi mediano meno efficace

---

## Parametri Modificabili nel Codice

### Simple Average
```cpp
uint8_t simpleAvgSamples = 10;  // 5-30 campioni
```

### Moving Average
```cpp
uint8_t movingAvgWindow = 20;   // 10-50 campioni
```

### EMA
```cpp
float emaAlpha = 0.1f;          // 0.01-0.5
// α = 0.01 → molto liscio
// α = 0.1  → bilanciato
// α = 0.3  → reattivo
```

### Complementary
```cpp
float complementaryAlpha = 0.98f;  // 0.90-0.99
// 0.98 → favorisce passa-basso
// 0.95 → più bilanciato
```

### Median
```cpp
uint8_t medianWindow = 5;       // 3, 5, 7 (dispari)
```

### Kalman
```cpp
float kalmanQ = 0.01f;          // Rumore processo (0.001-0.1)
float kalmanR = 1.0f;           // Rumore misura (0.1-10.0)
// Q/R basso → più smoothing
// Q/R alto → più reattivo
```

### Low-Pass
```cpp
float lowPassCutoff = 0.5f;     // Frequenza taglio (Hz)
// 0.1 Hz  → molto selettivo
// 0.5 Hz  → bilanciato
// 2.0 Hz  → permette dinamica
```

### High-Pass
```cpp
float highPassCutoff = 0.05f;   // Frequenza taglio (Hz)
// 0.01 Hz → blocca deriva molto lenta
// 0.05 Hz → bilanciato
// 0.1 Hz  → più aggressivo
```

---

## Progetti Didattici

### 1. Confronto Filtri Anti-Rumore
```
add white
filter simple    # Test 1
nofilter simple
filter moving    # Test 2
nofilter moving
filter ema       # Test 3
```
Quale smussa meglio? Quale ha meno ritardo?

### 2. Median Filter Challenge
```
add impulse
filter simple    # Gli impulsi si "spalmano"
nofilter simple
filter median    # Gli impulsi spariscono!
```

### 3. Kalman vs EMA
```
add scatter
filter ema       # Prova EMA
nofilter ema
filter kalman    # Prova Kalman
```
Il Kalman converge meglio su rumore estremo!

### 4. Complementary Filter Demo
```
add drift        # Deriva lenta
add white        # Rumore veloce
filter compl     # Rimuove deriva, mantiene dinamica
```

### 5. Cascata Ottimale
```
add white
add impulse
add drift
filter highpass  # Elimina drift
filter median    # Elimina impulsi
filter lowpass   # Smussa rumore
```

### 6. Cutoff Frequency Test
Modifica nel codice:
```cpp
float lowPassCutoff = 0.1f;   // Test 1
float lowPassCutoff = 1.0f;   // Test 2
float lowPassCutoff = 5.0f;   // Test 3
```
Osserva come cambia l'effetto del filtro!

---

## Tabella Comparativa Filtri

| Filtro | Tipo | Ritardo | Anti-Rumore | Anti-Impulse | Anti-Drift | Complessità |
|--------|------|---------|-------------|--------------|------------|-------------|
| Simple | FIR | Medio | ⭐⭐⭐ | ⭐⭐ | ❌ | Bassa |
| Moving | FIR | Alto | ⭐⭐⭐⭐ | ⭐⭐ | ❌ | Bassa |
| EMA | IIR | Basso | ⭐⭐⭐ | ⭐ | ❌ | Molto Bassa |
| Complementary | IIR | Basso | ⭐⭐ | ⭐ | ⭐⭐⭐⭐ | Media |
| Median | Non-lin | Medio | ⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | Media |
| Kalman | Adattivo | Basso | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Alta |
| Low-Pass | IIR | Basso | ⭐⭐⭐⭐ | ⭐⭐ | ❌ | Bassa |
| High-Pass | IIR | Basso | ⭐ | ⭐ | ⭐⭐⭐⭐⭐ | Bassa |

### Legenda
- Ritardo: quanto il filtro rallenta la risposta
- Anti-Rumore: efficacia su rumore bianco/gaussiano
- Anti-Impulse: efficacia su spike/impulsi
- Anti-Drift: efficacia su deriva DC
- Complessità: costo computazionale

---

## Consigli Pratici

### Per Rumore Bianco
**Best**: Low-Pass, Moving Average, Kalman
```
filter lowpass
```

### Per Impulsi/Spike
**Best**: Median
```
filter median
```

### Per Deriva DC
**Best**: High-Pass, Complementary
```
filter highpass
```

### Per Scatter (rumore estremo)
**Best**: Kalman
```
filter kalman
```

### Per Applicazioni Real-Time
**Best**: EMA, Low-Pass (ritardo minimo)
```
filter ema
```

### Per Massima Pulizia (no vincoli tempo)
**Best**: Cascata multi-filtro
```
filter median
filter kalman
filter lowpass
```

---

## Suggerimenti per Altri Filtri

### Filtri da Aggiungere

#### 1. **Savitzky-Golay Filter**
- Fit polinomiale su finestra mobile
- Preserva forma del segnale meglio di moving average
- Ottimo per smoothing mantenendo picchi

#### 2. **Butterworth Filter**
- Filtro IIR di ordine superiore
- Risposta in frequenza molto piatta in banda passante
- Configurabile: passa-basso, passa-alto, passa-banda

#### 3. **Notch Filter** (Band-Stop)
- Elimina una specifica frequenza
- Perfetto per rimuovere interferenza 50/60 Hz
- Parametri: frequenza centrale e Q-factor

#### 4. **Adaptive Filter** (LMS - Least Mean Squares)
- Si adatta automaticamente al rumore
- Insegue caratteristiche variabili nel tempo
- Usato in cancellazione eco

#### 5. **Wavelet Denoising**
- Decomposizione multi-risoluzione
- Threshold su coefficienti wavelet
- Ottimo per segnali non stazionari

#### 6. **Particle Filter**
- Filtro Monte Carlo per sistemi non lineari
- Più robusto di Kalman per non-linearità
- Computazionalmente intensivo

#### 7. **Alpha-Beta Filter**
- Semplificazione di Kalman
- Due soli parametri (α, β)
- Tracking di posizione e velocità

#### 8. **Wiener Filter**
- Filtro ottimo nel senso dei minimi quadrati
- Richiede stima della PSD del rumore
- Ottimo per deconvoluzione

---

## Conclusioni

Il sistema di filtri implementato offre:

✅ **8 filtri diversi** per ogni tipo di disturbo
✅ **Visualizzazione comparativa** real-time (raw vs filtered)
✅ **Cascata configurabile** per filtraggio multi-stage
✅ **Parametrizzazione** via codice per tuning fine
✅ **Didattica completa** su DSP e filtraggio digitale

La possibilità di combinare disturbi e filtri rende questo sistema ideale per:
- Insegnamento DSP
- Test algoritmi
- Prototipazione rapida
- Confronto filtri

Sperimenta con diverse combinazioni per capire pregi e limiti di ogni approccio!
