# Guida Filtri Avanzati - Generatore Sinusoidale

## Panoramica

Questo progetto estende il sistema base con **8 filtri avanzati** utilizzati in applicazioni professionali di elaborazione del segnale. Ogni filtro è ottimizzato per scenari specifici e può essere combinato con gli altri in cascata.

## 🚀 Filtri Avanzati Implementati

### 1. **Savitzky-Golay Filter** (Fit Polinomiale)
**Comando**: `filter savitzky` / `nofilter savitzky`

**Teoria**:
Il filtro Savitzky-Golay esegue un fit polinomiale (least-squares) su una finestra mobile di dati. A differenza della media mobile che "appiattisce" tutto, questo filtro preserva meglio la forma del segnale, inclusi picchi e valli.

**Caratteristiche**:
- Fit polinomiale di ordine 2 (quadratico) su finestra mobile
- Parametri:
  - `savitzkyWindow = 7` (finestra, deve essere dispari, 5 o 7)
  - `savitzkyOrder = 2` (ordine polinomio, 2 o 3)
- Usa coefficienti precalcolati per efficienza

**Coefficienti Precalcolati**:
- Finestra 7, ordine 2: [-0.095, 0.143, 0.286, 0.333, 0.286, 0.143, -0.095]
- Finestra 5, ordine 2: [-0.086, 0.343, 0.486, 0.343, -0.086]

**Formula**:
```
y[n] = Σ(c[i] * x[n-i]) per i=0 to window-1
dove c[i] sono i coefficienti precalcolati
```

**Effetto**:
- Smoothing "intelligente" che preserva forma
- Mantiene picchi e transizioni meglio della media mobile
- Riduce rumore senza "arrotondare" troppo
- Perfetto per dati scientifici

**Uso tipico**:
- Spettroscopia e analisi chimica
- Dati scientifici con picchi importanti
- Smoothing di curve mantenendo dettagli
- Pre-processing per peak detection

**Vantaggi vs Moving Average**:
- ✅ Preserva meglio la forma del segnale
- ✅ Non "schiaccia" i picchi
- ✅ Migliore risposta in frequenza
- ❌ Leggermente più complesso computazionalmente

**Confronto visivo**:
```
add white
filter moving     # Osserva: curva molto liscia ma "appiattita"
nofilter moving
filter savitzky   # Osserva: liscia ma mantiene la forma sinusoidale
```

---

### 2. **Butterworth Filter** (2nd Order Low-Pass)
**Comando**: `filter butter` / `nofilter butter`

**Teoria**:
Il Butterworth è un filtro IIR (Infinite Impulse Response) di ordine superiore progettato per avere una risposta in frequenza massimamente piatta nella banda passante. È uno dei filtri più usati in elettronica e DSP.

**Caratteristiche**:
- Filtro passa-basso secondo ordine (biquad)
- Parametro: `butterworthCutoff = 0.5` Hz
- Implementazione: bilinear transform
- Roll-off: -40 dB/decade (vs -20 dB del 1st order)

**Formula (biquad)**:
```
y[n] = b0*x[n] + b1*x[n-1] + b2*x[n-2] - a1*y[n-1] - a2*y[n-2]

Coefficienti calcolati con bilinear transform:
k = tan(ωc * T / 2)
b0 = k² / (1 + √2·k + k²)
b1 = 2·b0
b2 = b0
a1 = 2·(k² - 1) / (1 + √2·k + k²)
a2 = (1 - √2·k + k²) / (1 + √2·k + k²)
```

**Effetto**:
- Risposta molto piatta fino al cutoff
- Transizione più netta rispetto a RC semplice
- Roll-off più ripido (2x più veloce del 1st order)
- Fase non lineare (introduce distorsione di fase)

**Uso tipico**:
- Anti-aliasing prima di ADC
- Audio processing (crossover, equalizzazione)
- Rimozione rumore alta frequenza
- Condizionamento segnali analogici

**Confronto con Low-Pass RC**:
```
add white
filter lowpass    # Roll-off graduale
nofilter lowpass
filter butter     # Roll-off più ripido, attenuazione migliore
```

**Parametri cutoff**:
- 0.1 Hz: molto selettivo
- **0.5 Hz**: bilanciato (default)
- 2.0 Hz: passa più dinamica
- 5.0 Hz: solo rumore velocissimo viene attenuato

---

### 3. **Notch Filter** (Band-Stop)
**Comando**: `filter notch` / `nofilter notch`

**Teoria**:
Il Notch filter è un filtro band-stop che elimina selettivamente una banda stretta di frequenze, lasciando passare tutto il resto. È l'opposto di un filtro passa-banda.

**Caratteristiche**:
- Elimina una singola frequenza specifica
- Parametri:
  - `notchFreq = 2.0` Hz (frequenza da eliminare)
  - `notchQ = 10.0` (Q-factor, 5-30: più alto = più selettivo)
- Implementazione: IIR biquad band-stop

**Formula**:
```
Coefficienti calcolati con:
ω0 = 2π·f_notch
α = sin(ω0·T/2) · sinh(BW·T/2)
dove BW = ω0/Q

b0 = 1
b1 = -2·cos(ω0·T)
b2 = 1
a0 = 1 + α
a1 = -2·cos(ω0·T)
a2 = 1 - α

Output: y[n] = b0*x[n] + b1*x[n-1] + b2*x[n-2] - a1*y[n-1] - a2*y[n-2]
```

**Effetto**:
- Attenua drasticamente la frequenza target
- Larghezza banda determinata da Q
- Fase minima (distorsione fase ridotta)
- Risposta simmetrica attorno alla frequenza notch

**Q-Factor**:
- Q = 5: banda larga (±0.4 Hz per f=2Hz)
- **Q = 10**: medio (±0.2 Hz) - default
- Q = 20: selettivo (±0.1 Hz)
- Q = 30: molto stretto (±0.067 Hz)

**Uso tipico**:
- **Eliminazione interferenza 50/60 Hz dalla rete elettrica**
- Rimozione toni specifici indesiderati
- Cancellazione hum audio
- Eliminazione risonanze meccaniche

**Esempio pratico**:
```cpp
// Per eliminare interferenza 50 Hz:
float notchFreq = 50.0f;
float notchQ = 15.0f;

// Per test con segnale 0.1 Hz + interferenza 2 Hz:
add sine              # Interferenza a 2 Hz
filter notch          # Elimina i 2 Hz, mantiene 0.1 Hz
```

**Test ottimale**:
```
> f 0.1               # Segnale principale a 0.1 Hz
> on
> add sine            # Interferenza a 2 Hz (default)
[vedi segnale modulato]
> filter notch        # Elimina i 2 Hz
[vedi solo segnale a 0.1 Hz pulito!]
```

---

### 4. **LMS Adaptive Filter** (Least Mean Squares)
**Comando**: `filter lms` / `nofilter lms`

**Teoria**:
L'LMS è un filtro adattivo che "impara" automaticamente le caratteristiche del rumore e lo sottrae dal segnale. È uno dei filtri adattivi più usati per la sua semplicità ed efficacia.

**Caratteristiche**:
- Algoritmo di apprendimento supervisionato
- Parametri:
  - `lmsMu = 0.01` (step size, 0.001-0.1)
  - `lmsOrder = 10` (numero coefficienti/pesi)
- Auto-adattivo: si sintonizza sul rumore

**Algoritmo**:
```
1. Output (predizione):
   y[n] = Σ(w[i] * x[n-i]) per i=0 to order-1

2. Errore:
   e[n] = desired[n] - y[n]

3. Aggiornamento pesi (gradient descent):
   w[i] = w[i] + 2·μ·e[n]·x[n-i]
```

**Parametro μ (step size)**:
- μ = 0.001: convergenza lenta ma stabile
- **μ = 0.01**: bilanciato (default)
- μ = 0.05: convergenza veloce ma possibile instabilità
- μ = 0.1: molto veloce ma rischio divergenza

**Effetto**:
- "Impara" il pattern del rumore
- Si adatta a cambiamenti nel rumore
- Convergenza progressiva (migliora nel tempo)
- Tracking di segnali non stazionari

**Uso tipico**:
- Cancellazione eco (telefonia, videoconferenza)
- Noise cancellation adattivo
- Equalizzazione canali
- Sistema identification
- Predizione di serie temporali

**Confronto con Kalman**:
- LMS: più semplice, si adatta a pattern
- Kalman: ottimo per rumore gaussiano fisso

**Test progressivo**:
```
add white
filter lms
# Osserva: all'inizio rumoroso, poi progressivamente più pulito
# I pesi "imparano" le caratteristiche del rumore
```

**Note implementative**:
- Necessita di un segnale "desired" (riferimento)
- In questa implementazione usa il raw value come desired
- I pesi partono da zero e convergono gradualmente

---

### 5. **Wavelet Denoising** (Haar Wavelet)
**Comando**: `filter wavelet` / `nofilter wavelet`

**Teoria**:
Il wavelet denoising decompone il segnale in componenti multi-risoluzione (approssimazione + dettagli), applica thresholding sui dettagli (che contengono il rumore), e ricostruisce il segnale pulito.

**Caratteristiche**:
- Trasformata Haar (wavelet più semplice)
- Parametro: `waveletThreshold = 0.3` (0.1-1.0)
- 1 livello di decomposizione
- Soft thresholding sui coefficienti di dettaglio

**Algoritmo**:
```
1. DECOMPOSIZIONE (Haar):
   Approssimazione: a[i] = (x[2i] + x[2i+1]) / √2
   Dettaglio:      d[i] = (x[2i] - x[2i+1]) / √2

2. THRESHOLDING (soft):
   Se |d[i]| < threshold: d[i] = 0
   Se d[i] > threshold:   d[i] = d[i] - threshold
   Se d[i] < -threshold:  d[i] = d[i] + threshold

3. RICOSTRUZIONE:
   x[2i]   = (a[i] + d[i]) / √2
   x[2i+1] = (a[i] - d[i]) / √2
```

**Threshold**:
- 0.1: conservativo, mantiene più dettagli
- **0.3**: bilanciato (default)
- 0.5: aggressivo, smoothing maggiore
- 1.0: molto aggressivo, quasi solo approssimazione

**Effetto**:
- Rimozione rumore multi-scala
- Preserva transizioni e discontinuità
- Non introduce blur come filtri lineari
- Ottimo per burst noise

**Uso tipico**:
- Compressione immagini (JPEG2000)
- Denoising segnali biomedici (ECG, EEG)
- Analisi vibrazioni
- Rimozione artefatti localizzati

**Vantaggi**:
- ✅ Preserva bordi e transizioni
- ✅ Efficace su rumore non gaussiano
- ✅ Analisi multi-risoluzione
- ❌ Richiede potenza di 2 campioni

**Wavelet vs Fourier**:
- Wavelet: localizzazione tempo-frequenza
- Fourier: solo frequenza, perde informazione temporale

---

### 6. **Particle Filter** (Sequential Monte Carlo)
**Comando**: `filter particle` / `nofilter particle`

**Teoria**:
Il Particle Filter è un metodo Monte Carlo che rappresenta la distribuzione di probabilità dello stato con un insieme di "particelle" (campioni). Ogni particella è una possibile stima dello stato, con un peso che rappresenta la sua probabilità.

**Caratteristiche**:
- N particelle che "inseguono" il segnale
- Parametro: `particleCount = 20` (10-50 particelle)
- Non lineare, non gaussiano
- Resampling periodico per evitare degenerazione

**Algoritmo**:
```
1. INIZIALIZZAZIONE:
   Genera N particelle attorno alla prima misura
   Assegna peso uniforme: w[i] = 1/N

2. PREDICTION:
   Per ogni particella:
     x[i] = x[i] + rumore_processo

3. UPDATE (likelihood):
   Per ogni particella:
     w[i] = exp(-0.5 · (misura - x[i])² / σ²)
   Normalizza: w[i] = w[i] / Σ(w)

4. STIMA:
   x_stima = Σ(w[i] · x[i])

5. RESAMPLING (periodico):
   Crea nuove particelle basate sui pesi
   Particelle con peso alto → duplicate
   Particelle con peso basso → eliminate
```

**Effetto**:
- Tracking robusto anche con rumore estremo
- Gestisce multi-modalità (più picchi di probabilità)
- Converge anche da stime iniziali lontane
- Computazionalmente più costoso di Kalman

**Uso tipico**:
- Tracking oggetti con occlusioni
- Localizzazione robot (SLAM)
- Tracking in visione artificiale
- Sistemi fortemente non lineari

**Confronto con Kalman**:
| Aspetto | Kalman | Particle |
|---------|--------|----------|
| Linearità | Solo lineare | Qualsiasi |
| Rumore | Solo gaussiano | Qualsiasi |
| Multi-modale | No | Sì |
| Computazione | Bassa | Alta |
| Convergenza | Veloce | Media |

**Test estremo**:
```
add scatter           # Rumore estremo (nuvola punti)
filter particle       # Le particelle "trovano" il segnale
# Osserva convergenza progressiva
```

**Numero particelle**:
- 10: veloce ma meno preciso
- **20**: bilanciato (default)
- 30: più robusto
- 50: molto preciso ma lento

---

### 7. **Alpha-Beta Filter** (α-β Tracker)
**Comando**: `filter alphabeta` / `nofilter alphabeta`

**Teoria**:
L'Alpha-Beta filter è un tracker predittivo semplificato che stima posizione E velocità di un oggetto in movimento. È una versione semplificata del Kalman filter con solo 2 parametri invece di matrici di covarianza.

**Caratteristiche**:
- Stima congiunta di posizione e velocità
- Parametri:
  - `alphaBetaAlpha = 0.2` (peso posizione, 0.1-0.5)
  - `alphaBetaBeta = 0.1` (peso velocità, 0.01-0.2)
- Computazionalmente molto efficiente

**Algoritmo**:
```
1. PREDICTION:
   pos_pred = pos + vel · Δt

2. RESIDUAL:
   residual = misura - pos_pred

3. UPDATE:
   pos = pos_pred + α · residual
   vel = vel + (β · residual) / Δt
```

**Parametri α e β**:
```
α = 0.1, β = 0.01: molto liscio, lento
α = 0.2, β = 0.1:  bilanciato (default)
α = 0.4, β = 0.2:  reattivo, veloce
α = 0.5, β = 0.3:  molto reattivo
```

**Relazione tra α e β**:
```
β tipicamente = α² / 2
Questo bilancia smoothing posizione/velocità
```

**Effetto**:
- Predice movimento futuro
- Riduce jitter nei tracking
- Smoothing velocità oltre che posizione
- Ottimo per oggetti in movimento costante

**Uso tipico**:
- Tracking radar/sonar
- Smoothing GPS
- Inseguimento mouse/touch
- Tracking lineare con poca accelerazione

**Confronto tracking filters**:
| Filtro | Parametri | Stima | Costo CPU | Accuratezza |
|--------|-----------|-------|-----------|-------------|
| Alpha-Beta | 2 (α,β) | Pos+Vel | Basso | Buona |
| Kalman | Matrici Q,R | Pos+Vel+Cov | Medio | Ottima |
| Particle | N particelle | PDF completa | Alto | Ottima |

**Test movimento**:
```
f 0.2                 # Frequenza più alta
on
add white
filter alphabeta      # Tracker insegue movimento
# Osserva: predizione smooth anche con rumore
```

---

### 8. **Wiener Filter** (MMSE Optimal)
**Comando**: `filter wiener` / `nofilter wiener`

**Teoria**:
Il filtro di Wiener è il filtro lineare ottimo nel senso dei minimi quadrati medi (MMSE - Minimum Mean Square Error). Bilancia tra riduzione rumore e preservazione del segnale basandosi sulle statistiche locali.

**Caratteristiche**:
- Filtro ottimo statisticamente (MSE minimo)
- Parametro: `wienerNoiseVar = 100.0` (varianza rumore stimata)
- Calcola varianza locale del segnale
- Gain adattivo basato su SNR locale

**Formula (versione semplificata)**:
```
1. Media locale:
   μ = (1/N) · Σ(x[i])

2. Varianza locale:
   σ²_local = (1/N) · Σ((x[i] - μ)²)

3. Varianza segnale:
   σ²_signal = max(σ²_local - σ²_noise, 0)

4. Wiener Gain:
   G = σ²_signal / (σ²_signal + σ²_noise)

5. Output:
   y = μ + G · (x - μ)
```

**Gain Wiener**:
- Se σ²_signal >> σ²_noise → G ≈ 1 (passa segnale)
- Se σ²_signal ≈ σ²_noise → G ≈ 0.5 (bilancia)
- Se σ²_signal << σ²_noise → G ≈ 0 (blocca tutto)

**Effetto**:
- Smoothing adattivo basato su SNR locale
- Preserva zone con segnale forte
- Smussa pesantemente zone con solo rumore
- Ottimizza trade-off smoothing vs dettagli

**Uso tipico**:
- Restauro immagini
- Audio denoising
- Deconvoluzione
- Enhancing segnali deboli

**Stima rumore**:
- Manual: imposta `wienerNoiseVar` basandosi su conoscenza a priori
- Adaptive: stima da regioni "solo rumore"

**Varianza rumore**:
```cpp
// Rumore basso:
float wienerNoiseVar = 50.0f;   // Smoothing leggero

// Rumore medio (default):
float wienerNoiseVar = 100.0f;

// Rumore alto:
float wienerNoiseVar = 300.0f;  // Smoothing aggressivo
```

**Test adattivo**:
```
add white
filter wiener
# Osserva: smoothing si adatta automaticamente
# Zone con segnale forte → meno smoothing
# Zone piatte → più smoothing
```

---

## 🎯 Comandi Completi

### Attivare Filtri Avanzati
```
filter savitzky    → Savitzky-Golay
filter butter      → Butterworth 2nd order
filter notch       → Notch (band-stop)
filter lms         → LMS adattivo
filter wavelet     → Wavelet denoising
filter particle    → Particle filter
filter alphabeta   → Alpha-Beta tracker
filter wiener      → Wiener optimal
```

### Disattivare Filtri
```
nofilter savitzky
nofilter butter
nofilter notch
nofilter lms
nofilter wavelet
nofilter particle
nofilter alphabeta
nofilter wiener
```

### Status
```
filters            → Mostra tutti i filtri attivi (base + avanzati)
```

---

## 📊 Tabella Comparativa Completa

| Filtro | Tipo | Preserva Forma | Anti-Rumore | Computazione | Adattivo | Best Use Case |
|--------|------|----------------|-------------|--------------|----------|---------------|
| **Savitzky-Golay** | FIR | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Media | No | Dati scientifici con picchi |
| **Butterworth** | IIR | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Bassa | No | Anti-aliasing, audio |
| **Notch** | IIR | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐* | Bassa | No | Eliminazione 50/60Hz |
| **LMS** | Adattivo | ⭐⭐⭐ | ⭐⭐⭐⭐ | Media | Sì | Cancellazione eco |
| **Wavelet** | Multi-risoluzione | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Alta | No | Immagini, biomedico |
| **Particle** | Monte Carlo | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Molto Alta | Sì | Tracking non lineare |
| **Alpha-Beta** | Tracker | ⭐⭐⭐⭐ | ⭐⭐⭐ | Molto Bassa | No | Tracking GPS, radar |
| **Wiener** | Ottimo MMSE | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Media | Sì** | Restauro immagini |

\* Solo per frequenza specifica
\** Adattivo a SNR locale

---

## 🔬 Esempi Pratici

### Esempio 1: Eliminare Interferenza 50Hz
```
# Configura nel codice:
float notchFreq = 50.0f;
float notchQ = 15.0f;

# Poi:
> on
> filter notch
```
**Uso reale**: Elimina hum dalla rete elettrica in circuiti audio

---

### Esempio 2: Smoothing Scientifico
```
> on
> add white
> filter savitzky
Filtro Savitzky-Golay: ON
```
**Confronto**:
```
> nofilter savitzky
> filter moving
# Savitzky preserva meglio la forma sinusoidale
```

---

### Esempio 3: Tracking Robusto
```
> on
> add scatter          # Rumore estremo
> filter particle
# Le particelle convergono sul segnale vero
```

---

### Esempio 4: Cancellazione Adattiva
```
> on
> add white
> filter lms
# Osserva miglioramento progressivo nel tempo
# I pesi "imparano" il pattern del rumore
```

---

### Esempio 5: Cascata Avanzata
```
> on
> add white
> add impulse
> filter median        # Elimina impulsi
> filter wavelet       # Denoising multi-scala
> filter butter        # Smoothing finale
```

---

### Esempio 6: Confronto Butter vs LowPass
```
> on
> add white
> filter lowpass       # 1st order: -20dB/dec
> nofilter lowpass
> filter butter        # 2nd order: -40dB/dec
# Butterworth attenua meglio alte frequenze
```

---

## ⚙️ Parametrizzazione Avanzata

### Modifica Parametri nel Codice

#### Savitzky-Golay
```cpp
uint8_t savitzkyWindow = 7;    // 5 o 7 (dispari)
uint8_t savitzkyOrder = 2;     // 2 o 3

// Finestra 5 → più reattivo
// Finestra 7 → più smooth (default)
```

#### Butterworth
```cpp
float butterworthCutoff = 0.5f;   // Hz

// 0.1 Hz → molto selettivo
// 1.0 Hz → permette dinamica
// 5.0 Hz → solo rumore veloce attenuato
```

#### Notch
```cpp
float notchFreq = 50.0f;       // Frequenza da eliminare
float notchQ = 15.0f;          // Selettività

// Q = 5:  banda larga
// Q = 15: selettivo (default per 50Hz)
// Q = 30: molto stretto
```

#### LMS
```cpp
float lmsMu = 0.01f;           // Step size
uint8_t lmsOrder = 10;         // Numero pesi

// μ = 0.001: lento ma stabile
// μ = 0.01:  bilanciato (default)
// μ = 0.1:   veloce ma instabile

// Order 5:  semplice
// Order 10: bilanciato (default)
// Order 20: complesso, tracking migliore
```

#### Wavelet
```cpp
float waveletThreshold = 0.3f;    // 0.1-1.0

// 0.1: conservativo
// 0.3: bilanciato (default)
// 0.5: aggressivo
// 1.0: molto aggressivo
```

#### Particle
```cpp
uint8_t particleCount = 20;       // 10-50

// 10:  veloce ma meno preciso
// 20:  bilanciato (default)
// 30:  robusto
// 50:  molto preciso ma lento
```

#### Alpha-Beta
```cpp
float alphaBetaAlpha = 0.2f;      // 0.1-0.5
float alphaBetaBeta = 0.1f;       // 0.01-0.2

// Regola empirica: β ≈ α²/2

// α=0.1, β=0.01: liscio, lento
// α=0.2, β=0.1:  bilanciato (default)
// α=0.4, β=0.2:  reattivo, veloce
```

#### Wiener
```cpp
float wienerNoiseVar = 100.0f;    // Varianza rumore

// 50:  rumore basso, smoothing leggero
// 100: medio (default)
// 300: alto, smoothing aggressivo
```

---

## 🎓 Progetti Didattici Avanzati

### 1. Confronto Filtri Ordine Superiore
```
add white
filter lowpass     # 1st order
nofilter lowpass
filter butter      # 2nd order
```
**Osservazione**: Butterworth ha roll-off 2x più ripido

---

### 2. Notch per Interferenza
```
# Nel codice imposta:
float notchFreq = 2.0f;   // Match con interferenza

add sine           # Interferenza 2Hz
filter notch       # Elimina SOLO i 2Hz
```
**Risultato**: Sinusoide 0.1Hz pulita!

---

### 3. Wavelet vs Moving Average
```
add impulse
filter moving      # Gli impulsi si "spalmano"
nofilter moving
filter wavelet     # Gli impulsi spariscono senza blur
```

---

### 4. Adaptive Learning (LMS)
```
add white
filter lms
# Lascia girare 30 secondi
# Osserva convergenza progressiva dei pesi
```

---

### 5. Particle Filter Challenge
```
add scatter        # Rumore estremo
filter kalman      # Prova Kalman
nofilter kalman
filter particle    # Prova Particle
```
**Quale converge meglio su rumore estremo?**

---

### 6. Tracker Comparison
```
add white
filter alphabeta   # Alpha-Beta tracker
nofilter alphabeta
filter kalman      # Kalman tracker
```
**Quale ha meno ritardo? Quale è più liscio?**

---

### 7. Wiener Adaptive Smoothing
```
add white
add impulse
filter wiener
# Osserva: smoothing si adatta automaticamente
# Spike → meno smoothing
# Zone piatte → più smoothing
```

---

## 🚀 Cascate Ottimali

### Per Rumore Bianco Forte
```
filter butter      # Attenua alte frequenze
filter wiener      # Smoothing adattivo
```

### Per Impulsi + Rumore
```
filter median      # Elimina impulsi
filter wavelet     # Denoising multi-scala
filter savitzky    # Smoothing che preserva forma
```

### Per Interferenza + Rumore
```
filter notch       # Elimina interferenza specifica
filter butter      # Rimuove rumore residuo
```

### Per Tracking con Rumore
```
filter median      # Pre-processing impulsi
filter alphabeta   # Tracking con predizione
```

### Setup Professionale
```
filter notch       # Elimina 50/60Hz
filter wavelet     # Multi-scale denoising
filter wiener      # Optimal smoothing
```

---

## 📈 Benchmark Performance

### Complessità Computazionale (cicli CPU relativi)

| Filtro | Cicli | Note |
|--------|-------|------|
| Moving Average | 10 | ⚡ Molto veloce |
| EMA | 5 | ⚡⚡ Velocissimo |
| Median | 30 | Sorting |
| Kalman | 20 | Matrici 1D |
| Savitzky-Golay | 15 | Convoluzione |
| Butterworth | 12 | Biquad |
| Notch | 12 | Biquad |
| LMS | 40 | Loop pesi |
| Wavelet | 80 | Trasformata + threshold |
| Particle | 200 | Monte Carlo |
| Alpha-Beta | 8 | ⚡⚡ Velocissimo |
| Wiener | 50 | Statistiche locali |

---

## 🎯 Raccomandazioni Finali

### Scegli il Filtro Giusto

**Per Smoothing Generale**:
→ Butterworth o Savitzky-Golay

**Per Eliminare Frequenza Specifica**:
→ Notch Filter

**Per Rumore che Cambia**:
→ LMS o Wiener

**Per Preservare Dettagli**:
→ Savitzky-Golay o Wavelet

**Per Tracking**:
→ Alpha-Beta o Kalman

**Per Rumore Estremo**:
→ Particle Filter

**Per Tempo Reale Veloce**:
→ Alpha-Beta o EMA

**Per Qualità Massima**:
→ Cascata: Notch + Wavelet + Wiener

---

## 💡 Consigli Pratici

1. **Inizia semplice**: Prova prima i filtri base, poi avanzati
2. **Visualizza sempre**: Le due tracce (raw vs filtered) mostrano l'efficacia
3. **Testa cascate**: Combinare filtri può dare risultati migliori
4. **Sintonizza parametri**: I default sono generici, ottimizza per il tuo caso
5. **Benchmark**: Su ESP32, Particle Filter può essere lento con 50 particelle
6. **Convergenza**: LMS e Particle richiedono tempo per convergere
7. **Memoria**: Wavelet e Particle usano più RAM

---

## 🔧 Troubleshooting

### Il filtro non fa niente
**Problema**: Parametri non ottimizzati per il caso specifico
**Soluzione**: Regola cutoff, threshold, o parametri nel codice

### LMS diverge
**Problema**: μ troppo alto
**Soluzione**: Riduci `lmsMu` a 0.001

### Particle Filter lento
**Problema**: Troppe particelle
**Soluzione**: Riduci `particleCount` a 10-15

### Notch non elimina interferenza
**Problema**: Frequenza non centrata
**Soluzione**: Verifica `notchFreq` corrisponda a interferenza

### Wavelet introduce artefatti
**Problema**: Threshold troppo alto
**Soluzione**: Riduci `waveletThreshold` a 0.1-0.2

---

## 📚 Riferimenti Teorici

- **Savitzky-Golay**: Smoothing and Differentiation by Simplified Least Squares
- **Butterworth**: Maximally Flat Frequency Response
- **Notch**: Band-Stop IIR Filter Design
- **LMS**: Least Mean Squares Adaptive Filtering (Widrow-Hoff)
- **Wavelet**: Multiresolution Analysis and Denoising (Donoho)
- **Particle**: Sequential Monte Carlo Methods (Gordon et al.)
- **Alpha-Beta**: Tracking and Kalman Filtering (Kalata)
- **Wiener**: Optimal Linear MMSE Filtering

---

## 🎉 Conclusioni

Hai ora a disposizione **16 filtri totali** (8 base + 8 avanzati) per ogni scenario di filtraggio immaginabile!

Questo sistema è perfetto per:
✅ Insegnamento DSP avanzato
✅ Prototipazione algoritmi
✅ Confronto filtri real-time
✅ Test robustezza
✅ Applicazioni professionali

Sperimenta, combina, e trova la configurazione ottimale per il tuo caso d'uso! 🚀
