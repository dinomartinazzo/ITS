# Comunicazione bidirezionale ESP32 + LoRa (SX1278)

Questa guida mostra come realizzare una comunicazione bidirezionale tra due ESP32 dotati di modulo LoRa SX1278, usando Arduino. 

**Obiettivo:**
- Inviare da un nodo (A) un contatore e una temperatura simulata realistica (20–30 °C).
- Ricevere questi dati su un secondo nodo (B), che risponde con un messaggio di conferma (ACK).
- Il nodo A riceve la risposta e la stampa su seriale.

## Schema generale
- **Nodo A (Master/Sender):**
  - Invia un pacchetto con contatore e temperatura simulata.
  - Attende una risposta dal nodo B.
- **Nodo B (Slave/Responder):**
  - Riceve il pacchetto, stampa i dati ricevuti.
  - Risponde con un messaggio di ACK che include i dati ricevuti.

## Collegamenti ESP32 ↔ SX1278
- **SS:** GPIO 5
- **RST:** GPIO 14
- **DIO0:** GPIO 26

## Sketch Arduino

### Nodo A (Master/Sender)
```cpp
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
  delay(5000); // Aspetta prima di inviare di nuovo
}
```

### Nodo B (Slave/Responder)
```cpp
#include <SPI.h>
#include <LoRa.h>

#define SS 5
#define RST 14
#define DIO0 26

void setup() {
  Serial.begin(115200);
  while (!Serial);

  LoRa.setPins(SS, RST, DIO0);

  if (!LoRa.begin(433E6)) {
    Serial.println("LoRa init failed!");
    while (1);
  }
  Serial.println("LoRa Responder Ready");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    String incoming = "";

    while (LoRa.available()) {
      incoming += (char)LoRa.read();
    }

    Serial.print("Received: ");
    Serial.println(incoming);

    // Risponde confermando
    LoRa.beginPacket();
    LoRa.print("ACK: ");
    LoRa.print(incoming);
    LoRa.endPacket();

    Serial.println("Sent ACK!");
  }
}
```

## Come funziona
1. **Nodo A** invia: `0,24.5` (contatore 0, temperatura 24.5 °C)
2. **Nodo B** riceve e risponde: `ACK: 0,24.5`
3. **Nodo A** riceve la risposta e la stampa.
 