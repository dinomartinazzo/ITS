#include <Arduino.h>

// Parametri della sinusoide
const int amplitude = 2047; // Ampiezza della sinusoide (4095/2)
const int offset = 2047;    // Offset per portare i valori tra 0 e 4095
const int frequency = 1;    // Frequenza della sinusoide in Hz
const int samples = 100;    // Numero di campioni per ciclo
const int noiseLevel = 204; // 10% dell'ampiezza massima
const int spikeInterval = 20; // Intervallo per generare spike
const int spikeAmplitude = 4095; // Ampiezza massima dello spike
const float alpha = 0.8;    // Parametro del filtro complementare (0.0 - 1.0)
const float beta = 0.01;     // Parametro per il secondo campione precedente
const float step = 0.01; // Passo del loop generatore

// Variabili per il filtro complementare di ordine 1
float filteredValue1 = 0;

// Variabili per il filtro complementare di ordine 2
float filteredValue2 = 0;
float prevFilteredValue1 = 0; // Primo campione precedente
float prevFilteredValue2 = 0; // Secondo campione precedente

// Variabili per il filtro mediano
const int medianWindowSize = 5; // Dimensione della finestra del filtro mediano
int medianWindow[medianWindowSize] = {0}; // Finestra circolare per il filtro mediano
int medianIndex = 0; // Indice corrente nella finestra

// Variabili per il filtro della media mobile
const int movingAverageWindowSize = 5; // Dimensione della finestra
float movingAverageWindow[movingAverageWindowSize] = {0};
int movingAverageIndex = 0;
float movingAverageSum = 0;

// Variabili per il filtro della media mobile pesata
const int weightedWindowSize = 5; // Dimensione della finestra
float weightedWindow[weightedWindowSize] = {0};
int weightedIndex = 0;
float weightedSum = 0;

// Coefficienti per il filtro FIR
const int firOrder = 5; // Ordine del filtro FIR
float firCoefficients[firOrder] = {0.1, 0.15, 0.5, 0.15, 0.1}; // Coefficienti FIR
float firBuffer[firOrder] = {0};
int firIndex = 0;

// Funzione per inizializzare la comunicazione seriale
void initializeSerial() {
  Serial.begin(115200); // Inizializza la comunicazione seriale a 115200 baud
}

// Funzione per generare un valore di sinusoide
float generateSinusoidValue(float i) {
  float angle = 2.0 * PI * i; // Calcola l'angolo in radianti
  return offset + amplitude * sin(angle); // Restituisce il valore della sinusoide
}

// Funzione per aggiungere rumore casuale al segnale
float addNoise(float value) {
  float noise = random(-noiseLevel, noiseLevel + 1); // Genera un rumore casuale
  return value + noise; // Aggiunge il rumore al valore originale
}

// Funzione per aggiungere spike al segnale
float addSpike(float value, int i) {
  if (i % spikeInterval == 0) { // Controlla se è il momento di generare uno spike
    float spike = random(0, 2) == 0 ? spikeAmplitude : -spikeAmplitude; // Genera uno spike positivo o negativo
    value += spike; // Aggiunge lo spike al valore
  }
  return constrain(value, 0.0f, 4095.0f); // Limita il valore tra 0 e 4095
}

// Funzione per applicare la media mobile
float applyMovingAverage(float value) {
  movingAverageSum -= movingAverageWindow[movingAverageIndex];
  movingAverageWindow[movingAverageIndex] = value;
  movingAverageSum += value;
  movingAverageIndex = (movingAverageIndex + 1) % movingAverageWindowSize;
  return movingAverageSum / movingAverageWindowSize;
}

// Funzione per applicare la media mobile pesata testa-coda corretta e allineata
float applyWeightedMovingAverage(float value) {
  weightedSum -= weightedWindow[weightedIndex] * (weightedIndex + 1); // Rimuove il peso precedente
  weightedWindow[weightedIndex] = value; // Aggiorna il valore nella finestra
  weightedSum += value * (weightedIndex + 1); // Aggiunge il nuovo peso
  weightedIndex = (weightedIndex + 1) % weightedWindowSize; // Aggiorna l'indice

  float weightSum = 0;
  for (int i = 0; i < weightedWindowSize; i++) {
    weightSum += (i + 1); // Calcola la somma dei pesi
  }
  return weightedSum / weightSum; // Restituisce la media pesata
}

// Funzione per applicare il filtro FIR
float applyFIR(float value) {
  firBuffer[firIndex] = value;
  float firOutput = 0;
  for (int i = 0; i < firOrder; i++) {
    int index = (firIndex - i + firOrder) % firOrder;
    firOutput += firCoefficients[i] * firBuffer[index];
  }
  firIndex = (firIndex + 1) % firOrder;
  return firOutput;
}

// Funzione per applicare i filtri al segnale
void applyFilters(float value, float &medianValue, float &movingAvg, float &weightedAvg, float &firValue) {
  // Filtro complementare di ordine 1
  filteredValue1 = alpha * filteredValue1 + (1 - alpha) * value;

  // Filtro complementare di ordine 2
  float newFilteredValue2 = alpha * filteredValue2 + (1 - alpha) * value + beta * prevFilteredValue2;
  prevFilteredValue2 = prevFilteredValue1;
  prevFilteredValue1 = filteredValue2;
  filteredValue2 = newFilteredValue2;

  // Filtro mediano
  medianWindow[medianIndex] = (int)value; // Aggiunge il valore corrente alla finestra
  medianIndex = (medianIndex + 1) % medianWindowSize; // Aggiorna l'indice della finestra

  // Ordina la finestra per calcolare la mediana
  int sortedWindow[medianWindowSize];
  memcpy(sortedWindow, medianWindow, sizeof(medianWindow));
  for (int j = 0; j < medianWindowSize - 1; j++) {
    for (int k = j + 1; k < medianWindowSize; k++) {
      if (sortedWindow[j] > sortedWindow[k]) {
        int temp = sortedWindow[j];
        sortedWindow[j] = sortedWindow[k];
        sortedWindow[k] = temp;
      }
    }
  }
  medianValue = sortedWindow[medianWindowSize / 2]; // Calcola la mediana

  // Media mobile
  movingAvg = applyMovingAverage(value);

  // Media mobile pesata
  weightedAvg = applyWeightedMovingAverage(value);

  // Filtro FIR
  firValue = applyFIR(value);
}

// Funzione per inviare i dati via seriale
void sendData(float value, float medianValue, float movingAvg, float weightedAvg, float firValue) {
  Serial.print(value);       // Segnale originale
  Serial.print(",");         // Separatore CSV
  Serial.print(filteredValue1); // Filtro di ordine 1
  Serial.print(",");         // Separatore CSV
  Serial.print(filteredValue2); // Filtro di ordine 2
  Serial.print(",");         // Separatore CSV
  Serial.print(medianValue); // Filtro mediano
  Serial.print(",");         // Separatore CSV
  Serial.print(movingAvg);   // Media mobile
  Serial.print(",");         // Separatore CSV
  Serial.print(weightedAvg); // Media mobile pesata
  Serial.print(",");         // Separatore CSV
  Serial.println(firValue);  // Filtro FIR
}

// Funzione per processare un campione
void processSample(float i) {
  float value = generateSinusoidValue(i); // Genera il valore della sinusoide
  value = addNoise(value); // Aggiunge rumore
  value = addSpike(value, (int)(i * samples)); // Aggiunge spike

  float medianValue, movingAvg, weightedAvg, firValue;
  applyFilters(value, medianValue, movingAvg, weightedAvg, firValue); // Applica i filtri

  sendData(value, medianValue, movingAvg, weightedAvg, firValue); // Invia i dati
}

// Funzione di setup
void setup() {
  initializeSerial(); // Inizializza la comunicazione seriale
}

// Funzione di loop
void loop() {
  for (float i = 0; i < 1.0; i += step) { // Loop con passo 0.01
    processSample(i); // Processa il campione
    delay(100); // Ritardo 
  }
}
