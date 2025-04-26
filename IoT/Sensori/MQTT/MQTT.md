# Cos'è MQTT
MQTT (Message Queuing Telemetry Transport) è un protocollo di messaggistica leggero, basato su TCP/IP, progettato per la comunicazione tra dispositivi IoT. Utilizza un modello publish/subscribe, dove i client possono pubblicare messaggi su determinati "topic" o iscriversi per ricevere messaggi da questi topic tramite un broker centrale.

## Come si usa MQTT
- **Broker**: È il server centrale che gestisce la comunicazione tra i client (ad esempio Mosquitto).
- **Client**: Può essere un dispositivo, un'applicazione o un microcontrollore che invia (publish) o riceve (subscribe) messaggi.
- **Topic**: Canali logici su cui vengono inviati o ricevuti i messaggi.

### Flusso tipico
1. Il client si connette al broker MQTT.
2. Il client si iscrive a uno o più topic.
3. Altri client pubblicano messaggi su questi topic.
4. Il broker inoltra i messaggi ai client iscritti.

## Implementazione con ESP32 e Arduino IDE
Per utilizzare MQTT con ESP32 tramite Arduino IDE, segui questi passaggi:

### 1. Installazione delle librerie
- Installa la libreria `PubSubClient` tramite il Library Manager di Arduino IDE.
- Assicurati di avere la libreria WiFi per ESP32.

### 2. Esempio di codice
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TUO_SSID";
const char* password = "TUA_PASSWORD";
const char* mqtt_server = "indirizzo_broker";

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      client.subscribe("test/topic");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  client.publish("test/topic", "Hello from ESP32!");
  delay(2000);
}
```

### 3. Note
- Sostituisci `TUO_SSID`, `TUA_PASSWORD` e `indirizzo_broker` con i tuoi dati.
- Puoi modificare i topic e i messaggi secondo le tue esigenze.

## Risorse utili
- [MQTT.org](https://mqtt.org/)
- [PubSubClient GitHub](https://github.com/knolleary/pubsubclient)
- [Mosquitto Broker](https://mosquitto.org/)
