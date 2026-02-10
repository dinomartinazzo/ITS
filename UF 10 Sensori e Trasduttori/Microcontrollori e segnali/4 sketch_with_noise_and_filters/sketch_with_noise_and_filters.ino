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
  
  // Applica filtri in cascata
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
  Serial.println("=====================");
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
  Serial.println("  filter simple    -> media aritmetica");
  Serial.println("  filter moving    -> media mobile");
  Serial.println("  filter ema       -> media mobile esponenziale");
  Serial.println("  filter compl     -> filtro complementare");
  Serial.println("  filter median    -> filtro mediano");
  Serial.println("  filter kalman    -> filtro di Kalman");
  Serial.println("  filter lowpass   -> filtro passa-basso");
  Serial.println("  filter highpass  -> filtro passa-alto");
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
        Serial.println("  nofilter simple/moving/ema/compl/median/kalman/lowpass/highpass");
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
                             filterLowPass || filterHighPass;
      
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
