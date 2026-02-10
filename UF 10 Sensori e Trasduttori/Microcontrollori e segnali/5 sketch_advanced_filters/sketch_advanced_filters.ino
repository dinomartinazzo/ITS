/*
===============================================================================
 STEP 0 - Generatore SINUSOIDALE didattico
 Ampiezza 0..4096 (simil DAC / ADC 12 bit)
 ESP32 / Arduino
===============================================================================

 OBIETTIVO:
 - Generare una sinusoide campionata
 - Frequenza del segnale impostabile (Hz)
 - Frequenza di campionamento impostabile (Hz)
 - Output seriale (una sola colonna)

 CARATTERISTICHE:
 - Nessun interrupt
 - Nessun FreeRTOS
 - Un solo loop()
 - Temporizzazione con micros()

 UTILIZZO TIPICO:
 - Serial Plotter per visualizzare il segnale
 - Introduzione a:
     * tempo discreto
     * campionamento
     * segnali reali (0..4096)

===============================================================================
*/

#include <Arduino.h>

// ============================================================================
// PARAMETRI DI BASE
// ============================================================================

// Velocità della comunicazione seriale
static const uint32_t SERIAL_BAUD = 115200;

// Ampiezza massima del segnale (tipica risoluzione 12 bit)
static const float SIGNAL_MAX = 4096.0f;

// ============================================================================
// PARAMETRI MODIFICABILI A RUNTIME
// ============================================================================

// Frequenza del segnale sinusoidale (Hz)
// Valore ottimizzato per visualizzazione lenta e chiara
float signalFreq = 0.1f;  // 1 ciclo ogni 10 secondi

// Frequenza di campionamento (Hz)
// Alta risoluzione per curva fluida
float sampleRate = 50.0f;  // 50 campioni/secondo

// ============================================================================
// VARIABILI DI SUPPORTO
// ============================================================================

// Periodo di campionamento in microsecondi
// Ts = 1 / Fs
uint32_t Ts_us = 10000;

// Flag che abilita/disabilita l'output
bool streaming = false;

// Contatore del campione discreto n
// rappresenta l'indice temporale
uint32_t sampleIndex = 0;

// Tempo dell'ultimo campione generato
uint32_t lastSampleTime_us = 0;

// Buffer per la riga di comando seriale
String cmdLine;

// ============================================================================
// DISTURBI E RUMORI
// ============================================================================

// Flag per abilitare/disabilitare i vari disturbi
bool noiseWhite = false;      // Rumore bianco gaussiano
bool noisePink = false;       // Rumore 1/f (pink noise)
bool noiseImpulse = false;    // Impulsi casuali (spikes)
bool noiseSinusoidal = false; // Interferenza sinusoidale
bool noiseDrift = false;      // Deriva lenta (DC drift)
bool noiseQuantization = false; // Rumore di quantizzazione
bool noiseScatter = false;    // Nuvola di punti (scatter)

// Parametri dei disturbi
float whiteNoiseAmplitude = 100.0f;    // Ampiezza rumore bianco
float pinkNoiseAmplitude = 300.0f;     // Ampiezza pink noise (aumentata)
float impulseAmplitude = 500.0f;       // Ampiezza impulsi
float impulseProbability = 0.01f;      // Probabilità impulso (1%)
float interferenceFreq = 2.0f;         // Freq interferenza sinusoidale (Hz)
float interferenceAmplitude = 200.0f;  // Ampiezza interferenza
float driftRate = 5.0f;                // Velocità deriva (aumentata)
uint16_t quantizationBits = 5;         // Bit di quantizzazione (ridotto per visibilità)
float scatterAmplitude = 600.0f;       // Ampiezza scatter (nuvola di punti)

// Variabili di stato per i disturbi
float pinkNoiseState = 0.0f;           // Stato per pink noise filter
float driftValue = 0.0f;               // Valore corrente della deriva

// ============================================================================
// FILTRI
// ============================================================================

// Flag per abilitare/disabilitare i vari filtri
bool filterSimpleAvg = false;          // Media aritmetica semplice
bool filterMovingAvg = false;          // Media mobile
bool filterExpMovingAvg = false;       // Media mobile esponenziale (EMA)
bool filterComplementary = false;      // Filtro complementare
bool filterMedian = false;             // Filtro mediano
bool filterKalman = false;             // Filtro di Kalman semplificato
bool filterLowPass = false;            // Filtro passa-basso RC
bool filterHighPass = false;           // Filtro passa-alto

// FILTRI AVANZATI
bool filterSavitzkyGolay = false;      // Savitzky-Golay
bool filterButterworth = false;        // Butterworth 2nd order
bool filterNotch = false;              // Notch filter (band-stop)
bool filterLMS = false;                // Adaptive LMS filter
bool filterWavelet = false;            // Wavelet denoising (semplificato)
bool filterParticle = false;           // Particle filter (semplificato)
bool filterAlphaBeta = false;          // Alpha-Beta tracker
bool filterWiener = false;             // Wiener filter (approssimato)

// Parametri dei filtri
uint8_t simpleAvgSamples = 10;         // Numero campioni per media semplice
uint8_t movingAvgWindow = 20;          // Finestra media mobile
float emaAlpha = 0.1f;                 // Coefficiente EMA (0-1, più basso = più liscio)
float complementaryAlpha = 0.98f;      // Peso filtro complementare
uint8_t medianWindow = 5;              // Finestra filtro mediano (dispari)
float kalmanQ = 0.01f;                 // Rumore processo Kalman
float kalmanR = 1.0f;                  // Rumore misura Kalman
float lowPassCutoff = 0.5f;            // Frequenza taglio passa-basso (Hz)
float highPassCutoff = 0.05f;          // Frequenza taglio passa-alto (Hz)

// Parametri filtri avanzati
uint8_t savitzkyWindow = 7;            // Finestra Savitzky-Golay (dispari, >=5)
uint8_t savitzkyOrder = 2;             // Ordine polinomio (2 o 3)
float butterworthCutoff = 0.5f;        // Frequenza taglio Butterworth (Hz)
float notchFreq = 2.0f;                // Frequenza notch (Hz) - default 2Hz per test
float notchQ = 10.0f;                  // Q-factor notch (5-30)
float lmsMu = 0.01f;                   // Step size LMS (0.001-0.1)
uint8_t lmsOrder = 10;                 // Ordine filtro LMS
float waveletThreshold = 0.3f;         // Soglia wavelet (0.1-1.0)
uint8_t particleCount = 20;            // Numero particelle (10-50)
float alphaBetaAlpha = 0.2f;           // Coefficiente alpha (0.1-0.5)
float alphaBetaBeta = 0.1f;            // Coefficiente beta (0.01-0.2)
float wienerNoiseVar = 100.0f;         // Varianza rumore stimata

// Buffer e stati per i filtri
#define MAX_FILTER_BUFFER 50
float filterBuffer[MAX_FILTER_BUFFER]; // Buffer circolare per filtri
uint8_t filterBufferIndex = 0;
uint8_t filterBufferCount = 0;
float emaState = 0.0f;                 // Stato EMA
bool emaInitialized = false;
float complementaryState = 0.0f;       // Stato filtro complementare
float kalmanX = 0.0f;                  // Stima Kalman
float kalmanP = 1.0f;                  // Covarianza errore Kalman
float lowPassState = 0.0f;             // Stato passa-basso
float highPassState = 0.0f;            // Stato passa-alto
float highPassPrevInput = 0.0f;        // Input precedente passa-alto

// Valore filtrato finale (per visualizzazione)
float filteredValue = 0.0f;

// Stati per filtri avanzati
float butterworthX1 = 0.0f, butterworthX2 = 0.0f;  // Stati input Butterworth
float butterworthY1 = 0.0f, butterworthY2 = 0.0f;  // Stati output Butterworth
float notchX1 = 0.0f, notchX2 = 0.0f;              // Stati input Notch
float notchY1 = 0.0f, notchY2 = 0.0f;              // Stati output Notch
float lmsWeights[20];                               // Pesi LMS (max 20)
float lmsBuffer[20];                                // Buffer input LMS
uint8_t lmsBufferIdx = 0;
float waveletCoeffs[MAX_FILTER_BUFFER];             // Coefficienti wavelet
struct Particle {
  float x;      // Stato
  float weight; // Peso
};
Particle particles[50];                             // Array particelle (max 50)
float alphaBetaPosition = 0.0f;                     // Posizione stimata
float alphaBetaVelocity = 0.0f;                     // Velocità stimata
float wienerSignalVar = 1000.0f;                    // Varianza segnale stimata

// ============================================================================
// FUNZIONI DI UTILITÀ
// ============================================================================

// Aggiorna il periodo di campionamento Ts_us
// quando cambia la frequenza di campionamento Fs
void updateSamplingPeriod() {
  Ts_us = (uint32_t)(1000000.0f / sampleRate);
}

// ============================================================================
// GENERATORI DI DISTURBI
// ============================================================================

// Genera numero casuale gaussiano (approssimazione Box-Muller semplificata)
float randomGaussian() {
  float sum = 0.0f;
  for (int i = 0; i < 12; i++) {
    sum += random(0, 1000) / 1000.0f;
  }
  return sum - 6.0f;  // Media 0, deviazione std ~1
}

// Genera rumore bianco gaussiano
float generateWhiteNoise() {
  return randomGaussian() * whiteNoiseAmplitude;
}

// Genera pink noise (1/f) con filtro semplificato
float generatePinkNoise() {
  float white = randomGaussian();
  // Filtro più "colorato" per maggiore visibilità
  pinkNoiseState = 0.95f * pinkNoiseState + 0.05f * white;
  return pinkNoiseState * pinkNoiseAmplitude;
}

// Genera impulsi casuali (spikes)
float generateImpulse() {
  if (random(0, 10000) < impulseProbability * 10000) {
    return (random(0, 2) == 0 ? 1.0f : -1.0f) * impulseAmplitude;
  }
  return 0.0f;
}

// Genera interferenza sinusoidale
float generateSinusoidalNoise(float t) {
  return interferenceAmplitude * sinf(2.0f * PI * interferenceFreq * t);
}

// Genera deriva lenta (DC drift)
float generateDrift(float t) {
  driftValue = driftRate * t;
  return driftValue;
}

// Applica quantizzazione
float applyQuantization(float value) {
  float levels = pow(2.0f, quantizationBits);
  float step = SIGNAL_MAX / levels;
  return floor(value / step) * step;
}

// Genera scatter noise (nuvola di punti)
// Rumore molto forte che trasforma la sinusoide in una nuvola
float generateScatter() {
  return randomGaussian() * scatterAmplitude;
}

// Mostra stato dei disturbi
void printNoiseStatus() {
  Serial.println("=== DISTURBI ATTIVI ===");
  Serial.print("  white:  "); Serial.println(noiseWhite ? "ON" : "off");
  Serial.print("  pink:   "); Serial.println(noisePink ? "ON" : "off");
  Serial.print("  impulse:"); Serial.println(noiseImpulse ? "ON" : "off");
  Serial.print("  sine:   "); Serial.println(noiseSinusoidal ? "ON" : "off");
  Serial.print("  drift:  "); Serial.println(noiseDrift ? "ON" : "off");
  Serial.print("  quant:  "); Serial.println(noiseQuantization ? "ON" : "off");
  Serial.print("  scatter:"); Serial.println(noiseScatter ? "ON" : "off");
  Serial.println("=======================");
}

// ============================================================================
// FILTRI
// ============================================================================

// Reset buffer filtri
void resetFilterBuffer() {
  filterBufferIndex = 0;
  filterBufferCount = 0;
  emaInitialized = false;
  emaState = 0.0f;
  complementaryState = 0.0f;
  kalmanX = 0.0f;
  kalmanP = 1.0f;
  lowPassState = 0.0f;
  highPassState = 0.0f;
  highPassPrevInput = 0.0f;
}

// Aggiungi campione al buffer circolare
void addToFilterBuffer(float value) {
  filterBuffer[filterBufferIndex] = value;
  filterBufferIndex = (filterBufferIndex + 1) % MAX_FILTER_BUFFER;
  if (filterBufferCount < MAX_FILTER_BUFFER) {
    filterBufferCount++;
  }
}

// Media aritmetica semplice (ultimi N campioni)
float applySimpleAvg() {
  if (filterBufferCount == 0) return filteredValue;
  
  uint8_t count = min(filterBufferCount, simpleAvgSamples);
  float sum = 0.0f;
  
  for (uint8_t i = 0; i < count; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    sum += filterBuffer[idx];
  }
  
  return sum / count;
}

// Media mobile (finestra scorrevole)
float applyMovingAvg() {
  if (filterBufferCount == 0) return filteredValue;
  
  uint8_t count = min(filterBufferCount, movingAvgWindow);
  float sum = 0.0f;
  
  for (uint8_t i = 0; i < count; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    sum += filterBuffer[idx];
  }
  
  return sum / count;
}

// Media mobile esponenziale (EMA)
float applyExpMovingAvg(float newValue) {
  if (!emaInitialized) {
    emaState = newValue;
    emaInitialized = true;
    return newValue;
  }
  
  emaState = emaAlpha * newValue + (1.0f - emaAlpha) * emaState;
  return emaState;
}

// Filtro complementare (combina alta e bassa frequenza)
float applyComplementary(float newValue, float previousValue) {
  // High-pass: differenza tra nuovo valore e stato
  float highFreq = newValue - complementaryState;
  
  // Aggiorna stato (low-pass)
  complementaryState = complementaryAlpha * complementaryState + 
                       (1.0f - complementaryAlpha) * newValue;
  
  return complementaryState;
}

// Filtro mediano (ordina finestra e prende valore centrale)
float applyMedian() {
  if (filterBufferCount == 0) return filteredValue;
  
  uint8_t count = min(filterBufferCount, medianWindow);
  float tempBuffer[MAX_FILTER_BUFFER];
  
  // Copia dati in buffer temporaneo
  for (uint8_t i = 0; i < count; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    tempBuffer[i] = filterBuffer[idx];
  }
  
  // Bubble sort semplice
  for (uint8_t i = 0; i < count - 1; i++) {
    for (uint8_t j = 0; j < count - i - 1; j++) {
      if (tempBuffer[j] > tempBuffer[j + 1]) {
        float temp = tempBuffer[j];
        tempBuffer[j] = tempBuffer[j + 1];
        tempBuffer[j + 1] = temp;
      }
    }
  }
  
  // Ritorna valore mediano
  return tempBuffer[count / 2];
}

// Filtro di Kalman semplificato (1D)
float applyKalman(float measurement) {
  // Prediction
  float xPrior = kalmanX;
  float pPrior = kalmanP + kalmanQ;
  
  // Update
  float kalmanGain = pPrior / (pPrior + kalmanR);
  kalmanX = xPrior + kalmanGain * (measurement - xPrior);
  kalmanP = (1.0f - kalmanGain) * pPrior;
  
  return kalmanX;
}

// Filtro passa-basso RC (IIR primo ordine)
float applyLowPass(float newValue) {
  // Calcola alpha dal cutoff frequency e sample rate
  float dt = 1.0f / sampleRate;
  float rc = 1.0f / (2.0f * PI * lowPassCutoff);
  float alpha = dt / (rc + dt);
  
  lowPassState = alpha * newValue + (1.0f - alpha) * lowPassState;
  return lowPassState;
}

// Filtro passa-alto (differenziatore + passa-basso)
float applyHighPass(float newValue) {
  // Calcola alpha dal cutoff frequency e sample rate
  float dt = 1.0f / sampleRate;
  float rc = 1.0f / (2.0f * PI * highPassCutoff);
  float alpha = rc / (rc + dt);
  
  highPassState = alpha * (highPassState + newValue - highPassPrevInput);
  highPassPrevInput = newValue;
  
  return highPassState;
}

// Applica cascata di filtri nell'ordine corretto
float applyFilters(float rawValue) {
  float result = rawValue;
  
  // Aggiungi al buffer per filtri che ne hanno bisogno
  addToFilterBuffer(result);
  
  // Applica filtri BASE in cascata
  if (filterSimpleAvg) {
    result = applySimpleAvg();
  }
  
  if (filterMovingAvg) {
    result = applyMovingAvg();
  }
  
  if (filterExpMovingAvg) {
    result = applyExpMovingAvg(result);
  }
  
  if (filterComplementary) {
    result = applyComplementary(result, rawValue);
  }
  
  if (filterMedian) {
    result = applyMedian();
  }
  
  if (filterKalman) {
    result = applyKalman(result);
  }
  
  if (filterLowPass) {
    result = applyLowPass(result);
  }
  
  if (filterHighPass) {
    result = applyHighPass(result);
  }
  
  // Applica filtri AVANZATI in cascata
  if (filterSavitzkyGolay) {
    result = applySavitzkyGolay();
  }
  
  if (filterButterworth) {
    result = applyButterworth(result);
  }
  
  if (filterNotch) {
    result = applyNotch(result);
  }
  
  if (filterLMS) {
    result = applyLMS(rawValue, result);
  }
  
  if (filterWavelet) {
    result = applyWavelet();
  }
  
  if (filterParticle) {
    result = applyParticle(result);
  }
  
  if (filterAlphaBeta) {
    result = applyAlphaBeta(result);
  }
  
  if (filterWiener) {
    result = applyWiener();
  }
  
  return result;
}

// Mostra stato dei filtri
void printFilterStatus() {
  Serial.println("=== FILTRI ATTIVI ===");
  Serial.print("  simple:  "); Serial.println(filterSimpleAvg ? "ON" : "off");
  Serial.print("  moving:  "); Serial.println(filterMovingAvg ? "ON" : "off");
  Serial.print("  ema:     "); Serial.println(filterExpMovingAvg ? "ON" : "off");
  Serial.print("  compl:   "); Serial.println(filterComplementary ? "ON" : "off");
  Serial.print("  median:  "); Serial.println(filterMedian ? "ON" : "off");
  Serial.print("  kalman:  "); Serial.println(filterKalman ? "ON" : "off");
  Serial.print("  lowpass: "); Serial.println(filterLowPass ? "ON" : "off");
  Serial.print("  highpass:"); Serial.println(filterHighPass ? "ON" : "off");
  Serial.print("  savitzky:"); Serial.println(filterSavitzkyGolay ? "ON" : "off");
  Serial.print("  butter:  "); Serial.println(filterButterworth ? "ON" : "off");
  Serial.print("  notch:   "); Serial.println(filterNotch ? "ON" : "off");
  Serial.print("  lms:     "); Serial.println(filterLMS ? "ON" : "off");
  Serial.print("  wavelet: "); Serial.println(filterWavelet ? "ON" : "off");
  Serial.print("  particle:"); Serial.println(filterParticle ? "ON" : "off");
  Serial.print("  alphabeta:"); Serial.println(filterAlphaBeta ? "ON" : "off");
  Serial.print("  wiener:  "); Serial.println(filterWiener ? "ON" : "off");
  Serial.println("=====================");
}

// ============================================================================
// FILTRI AVANZATI
// ============================================================================

// Savitzky-Golay Filter (fit polinomiale)
// Usa coefficienti precalcolati per finestra 7, ordine 2
float applySavitzkyGolay() {
  if (filterBufferCount < savitzkyWindow) return filteredValue;
  
  // Coefficienti per finestra 7, ordine 2 (smoothing quadratico)
  const float coeffs7[7] = {-0.095, 0.143, 0.286, 0.333, 0.286, 0.143, -0.095};
  
  // Coefficienti per finestra 5, ordine 2
  const float coeffs5[5] = {-0.086, 0.343, 0.486, 0.343, -0.086};
  
  const float* coeffs;
  uint8_t window;
  
  if (savitzkyWindow >= 7) {
    coeffs = coeffs7;
    window = 7;
  } else {
    coeffs = coeffs5;
    window = 5;
  }
  
  float sum = 0.0f;
  for (uint8_t i = 0; i < window; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    sum += coeffs[i] * filterBuffer[idx];
  }
  
  return sum;
}

// Butterworth Low-Pass 2nd Order (biquad)
float applyButterworth(float input) {
  // Calcola coefficienti (bilinear transform)
  float dt = 1.0f / sampleRate;
  float wc = 2.0f * PI * butterworthCutoff;
  float k = tan(wc * dt / 2.0f);
  float k2 = k * k;
  float sqrt2 = 1.414213562f;
  float norm = 1.0f / (1.0f + sqrt2 * k + k2);
  
  // Coefficienti
  float b0 = k2 * norm;
  float b1 = 2.0f * b0;
  float b2 = b0;
  float a1 = 2.0f * (k2 - 1.0f) * norm;
  float a2 = (1.0f - sqrt2 * k + k2) * norm;
  
  // Equazione differenza
  float output = b0 * input + b1 * butterworthX1 + b2 * butterworthX2
                 - a1 * butterworthY1 - a2 * butterworthY2;
  
  // Aggiorna stati
  butterworthX2 = butterworthX1;
  butterworthX1 = input;
  butterworthY2 = butterworthY1;
  butterworthY1 = output;
  
  return output;
}

// Notch Filter (band-stop IIR)
float applyNotch(float input) {
  // Calcola coefficienti
  float dt = 1.0f / sampleRate;
  float w0 = 2.0f * PI * notchFreq;
  float bw = w0 / notchQ;
  
  float alpha = sin(w0 * dt / 2.0f) * sinh(bw * dt / 2.0f);
  float cosw0 = cos(w0 * dt);
  
  float b0 = 1.0f;
  float b1 = -2.0f * cosw0;
  float b2 = 1.0f;
  float a0 = 1.0f + alpha;
  float a1 = -2.0f * cosw0;
  float a2 = 1.0f - alpha;
  
  // Normalizza
  b0 /= a0;
  b1 /= a0;
  b2 /= a0;
  a1 /= a0;
  a2 /= a0;
  
  // Equazione differenza
  float output = b0 * input + b1 * notchX1 + b2 * notchX2
                 - a1 * notchY1 - a2 * notchY2;
  
  // Aggiorna stati
  notchX2 = notchX1;
  notchX1 = input;
  notchY2 = notchY1;
  notchY1 = output;
  
  return output;
}

// LMS Adaptive Filter
float applyLMS(float desired, float input) {
  // Aggiungi input al buffer
  lmsBuffer[lmsBufferIdx] = input;
  lmsBufferIdx = (lmsBufferIdx + 1) % lmsOrder;
  
  // Calcola output (predizione)
  float output = 0.0f;
  for (uint8_t i = 0; i < lmsOrder; i++) {
    uint8_t idx = (lmsBufferIdx - 1 - i + lmsOrder) % lmsOrder;
    output += lmsWeights[i] * lmsBuffer[idx];
  }
  
  // Calcola errore
  float error = desired - output;
  
  // Aggiorna pesi (LMS algorithm)
  for (uint8_t i = 0; i < lmsOrder; i++) {
    uint8_t idx = (lmsBufferIdx - 1 - i + lmsOrder) % lmsOrder;
    lmsWeights[i] += 2.0f * lmsMu * error * lmsBuffer[idx];
  }
  
  return output;
}

// Wavelet Denoising (Haar wavelet semplificato)
float applyWavelet() {
  if (filterBufferCount < 8) return filteredValue;
  
  // Trasformata Haar diretta (1 livello)
  uint8_t n = min(filterBufferCount, (uint8_t)32);
  n = (n / 2) * 2; // Rendi pari
  
  // Copia dati
  for (uint8_t i = 0; i < n; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    waveletCoeffs[i] = filterBuffer[idx];
  }
  
  // Decomposizione (media e differenza)
  float temp[MAX_FILTER_BUFFER];
  for (uint8_t i = 0; i < n/2; i++) {
    temp[i] = (waveletCoeffs[2*i] + waveletCoeffs[2*i+1]) / 1.414f;        // Approssimazione
    temp[n/2 + i] = (waveletCoeffs[2*i] - waveletCoeffs[2*i+1]) / 1.414f; // Dettaglio
  }
  
  // Soft thresholding sui dettagli
  for (uint8_t i = n/2; i < n; i++) {
    if (abs(temp[i]) < waveletThreshold) {
      temp[i] = 0.0f;
    } else if (temp[i] > 0) {
      temp[i] -= waveletThreshold;
    } else {
      temp[i] += waveletThreshold;
    }
  }
  
  // Ricostruzione
  for (uint8_t i = 0; i < n/2; i++) {
    waveletCoeffs[2*i] = (temp[i] + temp[n/2 + i]) / 1.414f;
    waveletCoeffs[2*i+1] = (temp[i] - temp[n/2 + i]) / 1.414f;
  }
  
  // Ritorna valore più recente ricostruito
  return waveletCoeffs[0];
}

// Particle Filter (versione semplificata)
float applyParticle(float measurement) {
  static bool initialized = false;
  
  // Inizializzazione
  if (!initialized) {
    for (uint8_t i = 0; i < particleCount; i++) {
      particles[i].x = measurement + randomGaussian() * 100.0f;
      particles[i].weight = 1.0f / particleCount;
    }
    initialized = true;
  }
  
  // Prediction: aggiungi rumore processo
  for (uint8_t i = 0; i < particleCount; i++) {
    particles[i].x += randomGaussian() * 10.0f;
  }
  
  // Update: calcola pesi basati su likelihood
  float sumWeights = 0.0f;
  for (uint8_t i = 0; i < particleCount; i++) {
    float diff = measurement - particles[i].x;
    particles[i].weight = exp(-0.5f * diff * diff / 10000.0f); // Likelihood gaussiana
    sumWeights += particles[i].weight;
  }
  
  // Normalizza pesi
  for (uint8_t i = 0; i < particleCount; i++) {
    particles[i].weight /= sumWeights;
  }
  
  // Stima (media pesata)
  float estimate = 0.0f;
  for (uint8_t i = 0; i < particleCount; i++) {
    estimate += particles[i].x * particles[i].weight;
  }
  
  // Resampling semplificato (ogni 10 iterazioni)
  static uint8_t resampleCounter = 0;
  if (++resampleCounter >= 10) {
    resampleCounter = 0;
    // Resampling sistematico semplificato
    Particle newParticles[50];
    for (uint8_t i = 0; i < particleCount; i++) {
      // Trova particella con peso più alto e duplicala
      uint8_t maxIdx = 0;
      float maxWeight = 0.0f;
      for (uint8_t j = 0; j < particleCount; j++) {
        if (particles[j].weight > maxWeight) {
          maxWeight = particles[j].weight;
          maxIdx = j;
        }
      }
      newParticles[i] = particles[maxIdx];
      particles[maxIdx].weight = 0.0f; // Evita duplicati multipli
    }
    // Copia back
    for (uint8_t i = 0; i < particleCount; i++) {
      particles[i] = newParticles[i];
      particles[i].weight = 1.0f / particleCount;
    }
  }
  
  return estimate;
}

// Alpha-Beta Filter (tracker)
float applyAlphaBeta(float measurement) {
  static bool initialized = false;
  static float dt = 0.02f; // Tempo campionamento
  
  if (!initialized) {
    alphaBetaPosition = measurement;
    alphaBetaVelocity = 0.0f;
    initialized = true;
    dt = 1.0f / sampleRate;
    return measurement;
  }
  
  // Prediction
  float predictedPosition = alphaBetaPosition + alphaBetaVelocity * dt;
  
  // Residual
  float residual = measurement - predictedPosition;
  
  // Update
  alphaBetaPosition = predictedPosition + alphaBetaAlpha * residual;
  alphaBetaVelocity = alphaBetaVelocity + (alphaBetaBeta * residual) / dt;
  
  return alphaBetaPosition;
}

// Wiener Filter (approssimazione con stima varianze)
float applyWiener() {
  if (filterBufferCount < 10) return filteredValue;
  
  // Calcola media locale
  float mean = 0.0f;
  uint8_t n = min(filterBufferCount, (uint8_t)20);
  for (uint8_t i = 0; i < n; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    mean += filterBuffer[idx];
  }
  mean /= n;
  
  // Calcola varianza locale
  float variance = 0.0f;
  for (uint8_t i = 0; i < n; i++) {
    uint8_t idx = (filterBufferIndex - 1 - i + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
    float diff = filterBuffer[idx] - mean;
    variance += diff * diff;
  }
  variance /= n;
  
  // Calcola gain Wiener
  float signalVar = max(variance - wienerNoiseVar, 0.0f);
  float wienerGain = signalVar / (signalVar + wienerNoiseVar);
  
  // Applica filtro
  uint8_t idx = (filterBufferIndex - 1 + MAX_FILTER_BUFFER) % MAX_FILTER_BUFFER;
  return mean + wienerGain * (filterBuffer[idx] - mean);
}

// ============================================================================
// SETUP
// ============================================================================

void setup() {
  Serial.begin(SERIAL_BAUD);
  while (!Serial) {
    // attesa apertura seriale (utile su alcune board)
  }

  updateSamplingPeriod();

  Serial.println("STEP 0 - Generatore sinusoidale didattico");
  Serial.println("Ampiezza: 0 .. 4096");
  Serial.println("");
  Serial.println("CONFIGURAZIONE ATTUALE:");
  Serial.println("  Freq segnale: 0.1 Hz (1 ciclo ogni 10 sec)");
  Serial.println("  Sample rate: 50 Hz (curva fluida)");
  Serial.println("  -> Ottimale per visualizzazione e test rumore");
  Serial.println("");
  Serial.println("Comandi base:");
  Serial.println("  f <Hz>   -> frequenza segnale");
  Serial.println("  sr <Hz>  -> sample rate");
  Serial.println("  on/off   -> abilita/disabilita output");
  Serial.println("");
  Serial.println("Gestione disturbi:");
  Serial.println("  add white    -> aggiungi rumore bianco");
  Serial.println("  add pink     -> aggiungi pink noise (1/f)");
  Serial.println("  add impulse  -> aggiungi impulsi casuali");
  Serial.println("  add sine     -> aggiungi interferenza sinusoidale");
  Serial.println("  add drift    -> aggiungi deriva DC");
  Serial.println("  add quant    -> aggiungi quantizzazione");
  Serial.println("  add scatter  -> aggiungi nuvola di punti");
  Serial.println("  remove <tipo> -> rimuovi disturbo");
  Serial.println("  status       -> mostra disturbi attivi");
  Serial.println("");
  Serial.println("Gestione filtri:");
  Serial.println("  filter simple/moving/ema/compl/median/kalman/lowpass/highpass");
  Serial.println("  filter savitzky/butter/notch/lms/wavelet/particle/alphabeta/wiener");
  Serial.println("  nofilter <tipo>  -> rimuovi filtro");
  Serial.println("  filters          -> mostra filtri attivi");
  Serial.println("  h            -> help");
}

// ============================================================================
// LOOP PRINCIPALE
// ============================================================================

void loop() {

  // --------------------------------------------------------------------------
  // 1) GESTIONE COMANDI SERIALI (non bloccante)
  // --------------------------------------------------------------------------
  while (Serial.available()) {
    char c = Serial.read();

    // Fine riga: comando completo
    if (c == '\n' || c == '\r') {
      cmdLine.trim();

      if (cmdLine == "h") {
        Serial.println("Comandi disponibili:");
        Serial.println("  f <Hz>   -> frequenza segnale");
        Serial.println("  sr <Hz>  -> sample rate");
        Serial.println("  on/off   -> abilita/disabilita output");
        Serial.println("");
        Serial.println("Disturbi:");
        Serial.println("  add white/pink/impulse/sine/drift/quant/scatter");
        Serial.println("  remove white/pink/impulse/sine/drift/quant/scatter");
        Serial.println("  status   -> mostra disturbi attivi");
        Serial.println("");
        Serial.println("Filtri:");
        Serial.println("  filter simple/moving/ema/compl/median/kalman/lowpass/highpass");
        Serial.println("  filter savitzky/butter/notch/lms/wavelet/particle/alphabeta/wiener");
        Serial.println("  nofilter <tipo>");
        Serial.println("  filters  -> mostra filtri attivi");
        Serial.println("");
        Serial.println("Configurazione corrente:");
        Serial.print("  Freq: ");
        Serial.print(signalFreq);
        Serial.println(" Hz");
        Serial.print("  SR: ");
        Serial.print(sampleRate);
        Serial.println(" Hz");
      }
      else if (cmdLine == "on") {
        streaming = true;
        Serial.println("streaming ON");
      }
      else if (cmdLine == "off") {
        streaming = false;
        Serial.println("streaming OFF");
      }
      else if (cmdLine.startsWith("f ")) {
        // Imposta frequenza del segnale
        signalFreq = cmdLine.substring(2).toFloat();
        Serial.print("freq = ");
        Serial.print(signalFreq);
        Serial.println(" Hz");
      }
      else if (cmdLine.startsWith("sr ")) {
        // Imposta frequenza di campionamento
        sampleRate = cmdLine.substring(3).toFloat();
        updateSamplingPeriod();
        Serial.print("sample rate = ");
        Serial.print(sampleRate);
        Serial.println(" Hz");
      }
      else if (cmdLine == "status") {
        printNoiseStatus();
      }
      // ---- COMANDI ADD ----
      else if (cmdLine == "add white") {
        noiseWhite = true;
        Serial.println("Rumore bianco: ON");
      }
      else if (cmdLine == "add pink") {
        noisePink = true;
        Serial.println("Pink noise: ON");
      }
      else if (cmdLine == "add impulse") {
        noiseImpulse = true;
        Serial.println("Impulsi: ON");
      }
      else if (cmdLine == "add sine") {
        noiseSinusoidal = true;
        Serial.println("Interferenza sinusoidale: ON");
      }
      else if (cmdLine == "add drift") {
        noiseDrift = true;
        driftValue = 0.0f;  // Reset drift
        Serial.println("Deriva DC: ON");
      }
      else if (cmdLine == "add quant") {
        noiseQuantization = true;
        Serial.println("Quantizzazione: ON");
      }
      else if (cmdLine == "add scatter") {
        noiseScatter = true;
        Serial.println("Scatter (nuvola punti): ON");
      }
      // ---- COMANDI REMOVE ----
      else if (cmdLine == "remove white") {
        noiseWhite = false;
        Serial.println("Rumore bianco: OFF");
      }
      else if (cmdLine == "remove pink") {
        noisePink = false;
        pinkNoiseState = 0.0f;  // Reset stato
        Serial.println("Pink noise: OFF");
      }
      else if (cmdLine == "remove impulse") {
        noiseImpulse = false;
        Serial.println("Impulsi: OFF");
      }
      else if (cmdLine == "remove sine") {
        noiseSinusoidal = false;
        Serial.println("Interferenza sinusoidale: OFF");
      }
      else if (cmdLine == "remove drift") {
        noiseDrift = false;
        driftValue = 0.0f;
        Serial.println("Deriva DC: OFF");
      }
      else if (cmdLine == "remove quant") {
        noiseQuantization = false;
        Serial.println("Quantizzazione: OFF");
      }
      else if (cmdLine == "remove scatter") {
        noiseScatter = false;
        Serial.println("Scatter (nuvola punti): OFF");
      }
      // ---- COMANDI FILTER ----
      else if (cmdLine == "filter simple") {
        filterSimpleAvg = true;
        Serial.println("Filtro media semplice: ON");
      }
      else if (cmdLine == "filter moving") {
        filterMovingAvg = true;
        Serial.println("Filtro media mobile: ON");
      }
      else if (cmdLine == "filter ema") {
        filterExpMovingAvg = true;
        Serial.println("Filtro EMA: ON");
      }
      else if (cmdLine == "filter compl") {
        filterComplementary = true;
        Serial.println("Filtro complementare: ON");
      }
      else if (cmdLine == "filter median") {
        filterMedian = true;
        Serial.println("Filtro mediano: ON");
      }
      else if (cmdLine == "filter kalman") {
        filterKalman = true;
        Serial.println("Filtro Kalman: ON");
      }
      else if (cmdLine == "filter lowpass") {
        filterLowPass = true;
        Serial.println("Filtro passa-basso: ON");
      }
      else if (cmdLine == "filter highpass") {
        filterHighPass = true;
        Serial.println("Filtro passa-alto: ON");
      }
      // ---- COMANDI NOFILTER ----
      else if (cmdLine == "nofilter simple") {
        filterSimpleAvg = false;
        Serial.println("Filtro media semplice: OFF");
      }
      else if (cmdLine == "nofilter moving") {
        filterMovingAvg = false;
        Serial.println("Filtro media mobile: OFF");
      }
      else if (cmdLine == "nofilter ema") {
        filterExpMovingAvg = false;
        emaInitialized = false;
        Serial.println("Filtro EMA: OFF");
      }
      else if (cmdLine == "nofilter compl") {
        filterComplementary = false;
        complementaryState = 0.0f;
        Serial.println("Filtro complementare: OFF");
      }
      else if (cmdLine == "nofilter median") {
        filterMedian = false;
        Serial.println("Filtro mediano: OFF");
      }
      else if (cmdLine == "nofilter kalman") {
        filterKalman = false;
        kalmanX = 0.0f;
        kalmanP = 1.0f;
        Serial.println("Filtro Kalman: OFF");
      }
      else if (cmdLine == "nofilter lowpass") {
        filterLowPass = false;
        lowPassState = 0.0f;
        Serial.println("Filtro passa-basso: OFF");
      }
      else if (cmdLine == "nofilter highpass") {
        filterHighPass = false;
        highPassState = 0.0f;
        highPassPrevInput = 0.0f;
        Serial.println("Filtro passa-alto: OFF");
      }
      // ---- COMANDI FILTER AVANZATI ----
      else if (cmdLine == "filter savitzky") {
        filterSavitzkyGolay = true;
        Serial.println("Filtro Savitzky-Golay: ON");
      }
      else if (cmdLine == "filter butter") {
        filterButterworth = true;
        Serial.println("Filtro Butterworth: ON");
      }
      else if (cmdLine == "filter notch") {
        filterNotch = true;
        Serial.println("Filtro Notch: ON");
      }
      else if (cmdLine == "filter lms") {
        filterLMS = true;
        // Inizializza pesi a zero
        for (uint8_t i = 0; i < lmsOrder; i++) {
          lmsWeights[i] = 0.0f;
          lmsBuffer[i] = 0.0f;
        }
        Serial.println("Filtro LMS: ON");
      }
      else if (cmdLine == "filter wavelet") {
        filterWavelet = true;
        Serial.println("Filtro Wavelet: ON");
      }
      else if (cmdLine == "filter particle") {
        filterParticle = true;
        Serial.println("Filtro Particle: ON");
      }
      else if (cmdLine == "filter alphabeta") {
        filterAlphaBeta = true;
        Serial.println("Filtro Alpha-Beta: ON");
      }
      else if (cmdLine == "filter wiener") {
        filterWiener = true;
        Serial.println("Filtro Wiener: ON");
      }
      // ---- COMANDI NOFILTER AVANZATI ----
      else if (cmdLine == "nofilter savitzky") {
        filterSavitzkyGolay = false;
        Serial.println("Filtro Savitzky-Golay: OFF");
      }
      else if (cmdLine == "nofilter butter") {
        filterButterworth = false;
        butterworthX1 = butterworthX2 = butterworthY1 = butterworthY2 = 0.0f;
        Serial.println("Filtro Butterworth: OFF");
      }
      else if (cmdLine == "nofilter notch") {
        filterNotch = false;
        notchX1 = notchX2 = notchY1 = notchY2 = 0.0f;
        Serial.println("Filtro Notch: OFF");
      }
      else if (cmdLine == "nofilter lms") {
        filterLMS = false;
        Serial.println("Filtro LMS: OFF");
      }
      else if (cmdLine == "nofilter wavelet") {
        filterWavelet = false;
        Serial.println("Filtro Wavelet: OFF");
      }
      else if (cmdLine == "nofilter particle") {
        filterParticle = false;
        Serial.println("Filtro Particle: OFF");
      }
      else if (cmdLine == "nofilter alphabeta") {
        filterAlphaBeta = false;
        alphaBetaPosition = alphaBetaVelocity = 0.0f;
        Serial.println("Filtro Alpha-Beta: OFF");
      }
      else if (cmdLine == "nofilter wiener") {
        filterWiener = false;
        Serial.println("Filtro Wiener: OFF");
      }
      else if (cmdLine == "filters") {
        printFilterStatus();
      }

      // Reset buffer comando
      cmdLine = "";
    }
    else {
      // Accumula caratteri del comando
      cmdLine += c;
    }
  }

  // --------------------------------------------------------------------------
  // 2) GENERAZIONE DEL CAMPIONE (controllo temporale)
  // --------------------------------------------------------------------------
  uint32_t now_us = micros();

  // Verifica se è passato il tempo di campionamento Ts
  if (now_us - lastSampleTime_us >= Ts_us) {

    // Aggiorna il riferimento temporale
    lastSampleTime_us += Ts_us;

    if (streaming) {

      // ----------------------------------------------------------------------
      // TEMPO DISCRETO
      // t = n / Fs
      // ----------------------------------------------------------------------
      float t = (float)sampleIndex / sampleRate;

      // ----------------------------------------------------------------------
      // SINUSOIDE NORMALIZZATA [-1 .. +1]
      // ----------------------------------------------------------------------
      float s = sinf(2.0f * PI * signalFreq * t);

      // ----------------------------------------------------------------------
      // TRASFORMAZIONE IN [0 .. 4096]
      // (s + 1) / 2 -> [0 .. 1]
      // ----------------------------------------------------------------------
      float y = SIGNAL_MAX * (s + 1.0f) * 0.5f;

      // ----------------------------------------------------------------------
      // APPLICAZIONE DISTURBI
      // ----------------------------------------------------------------------
      
      // Rumore bianco gaussiano
      if (noiseWhite) {
        y += generateWhiteNoise();
      }
      
      // Pink noise (1/f)
      if (noisePink) {
        y += generatePinkNoise();
      }
      
      // Impulsi casuali
      if (noiseImpulse) {
        y += generateImpulse();
      }
      
      // Interferenza sinusoidale
      if (noiseSinusoidal) {
        y += generateSinusoidalNoise(t);
      }
      
      // Deriva DC
      if (noiseDrift) {
        y += generateDrift(t);
      }
      
      // Scatter - nuvola di punti (rumore molto forte)
      if (noiseScatter) {
        y += generateScatter();
      }
      
      // Quantizzazione (applicata per ultima)
      if (noiseQuantization) {
        y = applyQuantization(y);
      }
      
      // Clipping al range valido [0..4096]
      if (y < 0.0f) y = 0.0f;
      if (y > SIGNAL_MAX) y = SIGNAL_MAX;

      // ----------------------------------------------------------------------
      // APPLICAZIONE FILTRI
      // ----------------------------------------------------------------------
      filteredValue = applyFilters(y);
      
      // Clipping valore filtrato
      if (filteredValue < 0.0f) filteredValue = 0.0f;
      if (filteredValue > SIGNAL_MAX) filteredValue = SIGNAL_MAX;

      // ----------------------------------------------------------------------
      // OUTPUT SERIALE
      // Due colonne: segnale raw (con disturbi) e segnale filtrato
      // ----------------------------------------------------------------------
      
      // Controlla se almeno un filtro è attivo
      bool anyFilterActive = filterSimpleAvg || filterMovingAvg || 
                             filterExpMovingAvg || filterComplementary ||
                             filterMedian || filterKalman || 
                             filterLowPass || filterHighPass ||
                             filterSavitzkyGolay || filterButterworth ||
                             filterNotch || filterLMS || filterWavelet ||
                             filterParticle || filterAlphaBeta || filterWiener;
      
      if (anyFilterActive) {
        // Output a due colonne: raw,filtered
        Serial.print(y, 2);
        Serial.print(",");
        Serial.println(filteredValue, 2);
      } else {
        // Output singola colonna (solo raw)
        Serial.println(y, 2);
      }

      // Incrementa indice del campione
      sampleIndex++;
    }
  }
}
