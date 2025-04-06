#define LED_PIN 23  // Pin del LED
unsigned long previousMillis = 0; // Memorizza il tempo precedente
const long interval = 1000; // Intervallo di lampeggio (1 secondo)
bool ledState = LOW; // Stato iniziale del LED

void setup() {
  pinMode(LED_PIN, OUTPUT); // Imposta GPIO32 come output
}

void loop() {
  unsigned long currentMillis = millis(); // Legge il tempo attuale

  // Controlla se è passato l'intervallo di tempo
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis; // Aggiorna il tempo precedente

    // Inverte lo stato del LED
    ledState = !ledState;
    digitalWrite(LED_PIN, ledState);
  }
}
