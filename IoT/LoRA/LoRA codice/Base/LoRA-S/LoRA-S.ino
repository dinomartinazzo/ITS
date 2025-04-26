#include <SPI.h>
#include <LoRa.h>

#define SS 5
#define RST 14
#define DIO0 26

void setup() {
  Serial.begin(115200);
  while (!Serial);

  LoRa.setPins(SS, RST, DIO0);

  if (!LoRa.begin(433E6)) { // 433 MHz for SX1278
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  Serial.println("LoRa Sender");
}

void loop() {
  Serial.println("Sending packet...");
  LoRa.beginPacket();
  LoRa.print("Hello World");
  LoRa.endPacket();
  delay(1000);
}
