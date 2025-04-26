#include <SPI.h>
#include <LoRa.h>

#define SS 5
#define RST 14
#define DIO0 26

int counter = 0;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  LoRa.setPins(SS, RST, DIO0);

  if (!LoRa.begin(433E6)) {
    Serial.println("LoRa init failed!");
    while (1);
  }
  Serial.println("LoRa Master Ready");
}

void loop() {
  // Simula una temperatura tra 20 e 30 °C
  float temperature = 20.0 + random(0, 1000) / 100.0;

  Serial.print("Sending packet: ");
  Serial.print(counter);
  Serial.print(" Temp: ");
  Serial.println(temperature);

  // Invio dati
  LoRa.beginPacket();
  LoRa.print(counter);
  LoRa.print(",");
  LoRa.print(temperature);
  LoRa.endPacket();

  // Attesa di una risposta
  unsigned long startTime = millis();
  while (millis() - startTime < 2000) { // 2 secondi di timeout
    int packetSize = LoRa.parsePacket();
    if (packetSize) {
      Serial.print("Received reply: ");
      while (LoRa.available()) {
        Serial.print((char)LoRa.read());
      }
      Serial.println();
      break;
    }
  }

  counter++;
  delay(2000); // Aspetta prima di inviare di nuovo
}
