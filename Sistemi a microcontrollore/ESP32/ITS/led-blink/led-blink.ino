#define LED_PIN 23  // Definiamo il pin del LED

void setup() {
  pinMode(LED_PIN, OUTPUT);  // Imposta GPIO32 come output
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // Accende il LED
  delay(1000);  // Aspetta 1 secondo
  digitalWrite(LED_PIN, LOW);  // Spegne il LED
  delay(1000);  // Aspetta 1 secondo
}
