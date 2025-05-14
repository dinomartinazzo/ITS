#include <WiFi.h>
#include <PubSubClient.h>

// ===== CONFIGURAZIONE =====
//const char* ssid = "Mate10";
const char* ssid = "FRITZ!Box 7530 NH";
const char* password = "3661461500";
 
const char* mqtt_server = "10.0.0.23"; // IP del broker MQTT, adatta se usi localhost

WiFiClient espClient;
PubSubClient client(espClient);

float temperature = 22.0;

void setup_wifi() {
  delay(100);
  Serial.println();
  Serial.print("Connessione a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connesso");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connessione al broker MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("connesso!");
    } else {
      Serial.print("fallito, rc=");
      Serial.print(client.state());
      Serial.println(" ritento tra 5 secondi");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float delta = random(-30, 31) / 100.0;  // -0.3 a +0.3
  temperature += delta;
  if (temperature < 18.0) temperature = 18.0;
  if (temperature > 28.0) temperature = 28.0;

  char msg[10];
  dtostrf(temperature, 4, 1, msg);

  Serial.print("Invio temperatura: ");
  Serial.println(msg);
  client.publish("sensori/temperatura", msg);
  //client.publish("sensori/temperatura2", msg);

  delay(1000);
}
