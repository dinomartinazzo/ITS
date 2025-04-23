#include <WiFi.h>
#include <PubSubClient.h>

// Credenziali WiFi
const char* ssid = "FRITZ!Box 7530 NH";
const char* password = "3661461500";

// Broker MQTT
const char* mqtt_server = "test.mosquitto.org";

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connessione a ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  wl_status_t lastStatus = WL_IDLE_STATUS;
  while (WiFi.status() != WL_CONNECTED) {
    wl_status_t currentStatus = WiFi.status();
    if (currentStatus != lastStatus) {
      lastStatus = currentStatus;
      Serial.print("Stato WiFi cambiato: ");
      Serial.println(currentStatus);
    }
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connesso");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Messaggio ricevuto [");
  Serial.print(topic);
  Serial.print("] ");
  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  static bool wasConnected = false;
  while (!client.connected()) {
    if (!wasConnected) {
      Serial.print("Tentativo di connessione MQTT...");
    }
    if (client.connect("ESP32Client")) {
      if (!wasConnected) {
        Serial.println("connesso");
      }
      client.subscribe("test/esp32");
      wasConnected = true;
    } else {
      if (wasConnected) {
        Serial.print("fallito, rc=");
        Serial.print(client.state());
        Serial.println(" riprovo tra 5 secondi");
      }
      wasConnected = false;
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Pubblica ogni 5 secondi
  static unsigned long lastMsg = 0;
  unsigned long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;
    String msg = "Ciao da ESP32";
    client.publish("test/esp32", msg.c_str());
    Serial.println("Messaggio pubblicato: " + msg);

    float temperatura = random(200, 300) / 10.0;  // 20.0 - 30.0 °C
    msg = String(temperatura, 1);  // esempio: "25.3"
    client.publish("test/esp32/temperature", msg.c_str());
    Serial.println("Temperatura inviata: " + msg + " °C");

  }
}
