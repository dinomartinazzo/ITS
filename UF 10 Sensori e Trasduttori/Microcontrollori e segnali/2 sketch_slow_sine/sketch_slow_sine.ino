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
// FUNZIONI DI UTILITÀ
// ============================================================================

// Aggiorna il periodo di campionamento Ts_us
// quando cambia la frequenza di campionamento Fs
void updateSamplingPeriod() {
  Ts_us = (uint32_t)(1000000.0f / sampleRate);
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
  Serial.println("Comandi:");
  Serial.println("  f <Hz>   -> frequenza segnale");
  Serial.println("  sr <Hz>  -> sample rate");
  Serial.println("  on/off   -> abilita/disabilita output");
  Serial.println("  h        -> help");
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
      // OUTPUT SERIALE
      // Una sola colonna -> perfetto per Serial Plotter
      // ----------------------------------------------------------------------
      Serial.println(y, 2);

      // Incrementa indice del campione
      sampleIndex++;
    }
  }
}
