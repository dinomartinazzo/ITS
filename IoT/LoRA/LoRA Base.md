# Collegamento e Programmazione LoRa SX1278 con ESP32

## 1. Collegamento Hardware (Wiring)

Il modulo SX1278 utilizza l'interfaccia SPI per comunicare con l'ESP32. Ecco come collegare i pin:

| Pin SX1278 | Pin ESP32 |
|-----------|-----------|
| VCC       | 3.3V      |
| GND       | GND       |
| SCK       | 18        |
| MISO      | 19        |
| MOSI      | 23        |
| NSS (CS)  | 5         |
| RESET     | 14        |
| DIO0      | 26        |

> **Nota:** Puoi modificare i pin secondo le tue esigenze, ma ricordati di aggiornarli anche nel codice.

## 2. Librerie Arduino Necessarie

Installa queste librerie tramite il Library Manager di Arduino IDE:

- **LoRa by Sandeep Mistry** (libreria principale per LoRa)
- *(Opzionale)* **RadioHead** se vuoi un controllo più avanzato (per iniziare non è necessario)

## 3. Esempi di Codice

### ✅ Trasmettitore (Sender) ESP32 + SX1278

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

  if (!LoRa.begin(433E6)) { // 433 MHz per SX1278
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
```

### ✅ Ricevitore (Receiver) ESP32 + SX1278

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
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  Serial.println("LoRa Receiver");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Received packet: ");
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    Serial.println();
  }
}
```

## 4. Note Importanti

- **Antenna:** Assicurati che i moduli SX1278 abbiano sempre collegata l'antenna corretta, altrimenti rischi di danneggiarli.
- **Frequenza:** Sia trasmettitore che ricevitore devono usare la stessa frequenza (433 MHz per SX1278).
- **Alimentazione:** Alimenta correttamente ESP32 e SX1278; il modulo LoRa può assorbire picchi di corrente.
- **Pin SPI:** Se usi una scheda ESP32 particolare, potresti dover modificare i pin SPI nel codice.
 