# LoRa: Caratteristiche Tecniche e Funzionamento

## Cos'è LoRa

**LoRa** (Long Range) è una tecnologia di modulazione radio sviluppata per comunicazioni wireless a lunga distanza e basso consumo energetico. È utilizzata principalmente in applicazioni IoT (Internet of Things) dove è necessario trasmettere piccoli pacchetti di dati su distanze elevate, mantenendo una lunga durata delle batterie dei dispositivi.

## Principio di Funzionamento

LoRa utilizza una modulazione chiamata **Chirp Spread Spectrum (CSS)**, che consente di trasmettere dati su lunghe distanze anche in presenza di interferenze e rumore. I dispositivi LoRa comunicano tipicamente con gateway che inoltrano i dati verso server centrali tramite Internet.

## Architettura

- **End Device (Nodo):** Sensori o attuatori che raccolgono dati e li trasmettono via LoRa.
- **Gateway:** Riceve i segnali LoRa dai nodi e li inoltra tramite IP (Ethernet, Wi-Fi, 4G) a un server di rete.
- **Network Server:** Gestisce la sicurezza, l'autenticazione e l'instradamento dei dati.
- **Application Server:** Elabora i dati ricevuti per l'applicazione finale.

## Caratteristiche Tecniche

| Caratteristica         | Descrizione                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Frequenze              | 433 MHz, 868 MHz (Europa), 915 MHz (USA), ISM band                          |
| Distanza               | Fino a 15 km in campo aperto, 2-5 km in ambiente urbano                     |
| Velocità di trasmissione| 0.3 kbps – 50 kbps                                                          |
| Consumo energetico     | Molto basso, adatto a dispositivi alimentati a batteria                     |
| Sicurezza              | Crittografia AES a 128 bit                                                  |
| Topologia              | Stella (tramite gateway)                                                    |
| Capacità di penetrazione| Elevata, grazie alla modulazione CSS                                        |
| Bidirezionalità        | Supportata (uplink e downlink)                                              |
| Supporto mobilità      | Limitato, ottimizzato per dispositivi statici                               |
| Payload massimo        | 243 byte per pacchetto                                                       |

## Vantaggi

- Lunga distanza di trasmissione
- Basso consumo energetico
- Buona resistenza alle interferenze
- Scalabilità per reti con molti dispositivi

## Limiti

- Bassa velocità di trasmissione dati
- Non adatto a comunicazioni in tempo reale o ad alta banda
- Limitazioni normative sulle frequenze e potenza di trasmissione

## Applicazioni Tipiche

- Smart metering (contatori intelligenti)
- Monitoraggio ambientale
- Agricoltura di precisione
- Smart city (illuminazione, parcheggi, ecc.)
- Tracciamento asset e logistica

## Standard e Ecosistema

LoRa è la tecnologia fisica di trasmissione, mentre **LoRaWAN** è il protocollo di rete che definisce la comunicazione tra dispositivi, gateway e server. Lo standard LoRaWAN è gestito dalla LoRa Alliance.

## Esempio base con Arduino: LoRa.begin(433E6)

Per utilizzare un modulo LoRa con Arduino, si usa la libreria [LoRa](https://github.com/sandeepmistry/arduino-LoRa). Il metodo `LoRa.begin(frequenza)` inizializza il modulo sulla frequenza desiderata (ad esempio 433 MHz: `433E6`).

```cpp
#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("LoRa Sender");

  if (!LoRa.begin(433E6)) { // Inizializza a 433 MHz
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  // Configurazioni opzionali:
  // LoRa.setSpreadingFactor(7);      // 6-12, default 7
  // LoRa.setSignalBandwidth(125E3);  // 7.8E3-500E3 Hz, default 125E3
  // LoRa.setCodingRate4(5);          // 5-8, default 5 (4/5)
  // LoRa.setTxPower(14);             // 2-20 dBm, default 17
  // LoRa.enableCrc();                // Abilita CRC
}

void loop() {
  LoRa.beginPacket();
  LoRa.print("hello");
  LoRa.endPacket();
  delay(1000);
}
```

### Principali configurazioni LoRa (libreria Arduino)

| Metodo                        | Descrizione                                                      |
|-------------------------------|------------------------------------------------------------------|
| LoRa.begin(frequenza)         | Inizializza il modulo sulla frequenza (es: 433E6, 868E6, 915E6)   |
| LoRa.setSpreadingFactor(sf)   | Fattore di spreading 6-12: aumenta portata, riduce velocità       |
| LoRa.setSignalBandwidth(bw)   | Larghezza di banda: 7.8E3-500E3 Hz, default 125E3                 |
| LoRa.setCodingRate4(cr)       | Codifica FEC: 5-8 (4/5 - 4/8), default 5                         |
| LoRa.setTxPower(dbm)          | Potenza di trasmissione: 2-20 dBm                                |
| LoRa.enableCrc()              | Abilita il controllo di errore CRC                               |
| LoRa.disableCrc()             | Disabilita il CRC                                                |
| LoRa.idle()                   | Mette il modulo in idle                                          |
| LoRa.sleep()                  | Mette il modulo in sleep                                         |

Queste configurazioni permettono di adattare la comunicazione alle esigenze di portata, consumo e robustezza.


