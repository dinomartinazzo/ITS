#define PI 3.14159265358979323846

const int sampleRate = 100;  // Numero di campioni al secondo
const float frequency = 1.0; // Frequenza della sinusoide in Hz
const int amplitude = 1000;  // Ampiezza del segnale (modificabile)

void setup() {
  Serial.begin(115200);  // Inizializza la comunicazione seriale
}

void loop() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= (1000 / sampleRate)) {
    previousMillis = currentMillis;

    // Calcola il tempo in secondi
    float time = currentMillis / 1000.0;

    // Genera il valore sinusoidale
    float sineValue = amplitude * sin(2 * PI * frequency * time);

    // Stampa il valore sulla seriale
    Serial.println(sineValue);
  }
}
