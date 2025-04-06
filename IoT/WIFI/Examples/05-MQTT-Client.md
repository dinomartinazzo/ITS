# Esempio 5: Client MQTT

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TuaReteWiFi";
const char* password = "TuaPassword";
const char* mqtt_server = "broker.mqtt.com";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  client.setServer(mqtt_server, 1883);
  client.setCallback([](char* topic, byte* payload, unsigned int length) {
    Serial.print("Messaggio ricevuto [");
    Serial.print(topic);
    Serial.print("] ");
    for (int i = 0; i < length; i++) {
      Serial.print((char)payload[i]);
    }
    Serial.println();
  });
}

void loop() {
  if (!client.connected()) {
    if (client.connect("ESP32Client")) {
      client.subscribe("test/topic");
    }
  }
  client.loop();
}
```
