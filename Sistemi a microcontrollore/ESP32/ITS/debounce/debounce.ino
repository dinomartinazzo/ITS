#define BUTTON_PIN 18  // Sostituisci con il pin del tuo pulsante
#define LED_PIN 23     // LED collegato a GPIO23

const int debounceDelay = 50; // Ritardo debounce in millisecondi
bool buttonState = LOW;
bool lastButtonState = LOW;
unsigned long lastDebounceTime = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Attiva la resistenza di pull-up interna
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int reading = digitalRead(BUTTON_PIN);

  // Controllo del debounce
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Se lo stato è cambiato, aggiorna lo stato effettivo
    if (reading != buttonState) {
      buttonState = reading;

      // Se il pulsante è stato premuto, cambia lo stato del LED
      if (buttonState == LOW) {  // LOW perché usiamo INPUT_PULLUP
        digitalWrite(LED_PIN, !digitalRead(LED_PIN)); // Toggle LED
        Serial.println("Pulsante premuto! LED cambiato.");
      }
    }
  }

  lastButtonState = reading;
}
