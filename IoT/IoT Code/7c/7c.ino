#include <WiFi.h>

const char* ssid = "ESP32_Chat_AP";
const char* password = "12345678";
const char* serverIP = "192.168.4.1"; // IP predefinito dell'AP ESP32
const int serverPort = 12345;

WiFiClient client;

void connectToAccessPoint() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connessione all'Access Point...");
  }
  Serial.println("Connesso all'Access Point");
}

void connectToServer() {
  while (!client.connect(serverIP, serverPort)) {
    delay(1000);
    Serial.println("Connessione al server...");
  }
  Serial.println("Connesso al server");
}

void handleServerCommunication() {
  // Invia messaggi
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n');
    if (client.connected()) {
      client.println(message);
    } else {
      Serial.println("Connessione al server persa. Riconnessione...");
      connectToServer();
    }
  }

  // Riceve messaggi
  if (client.available()) {
    String message = client.readStringUntil('\n');
    if (message.startsWith("ID:")) {
      Serial.printf("Il tuo ID assegnato è: %s\n", message.substring(3).c_str());
    } else {
      Serial.printf("Ricevuto: %s\n", message.c_str());
    }
  }
}

void setup() {
  Serial.begin(115200);
  connectToAccessPoint();
  connectToServer();
}

void loop() {
  handleServerCommunication();
}