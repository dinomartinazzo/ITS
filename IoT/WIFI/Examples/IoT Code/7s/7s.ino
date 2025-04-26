#include <WiFi.h>

const char* ssid = "ESP32_Chat_AP";
const char* password = "12345678"; // Password minima di 8 caratteri

WiFiServer server(12345);
WiFiClient clients[5]; // Max 5 client
unsigned long lastConfigPrintTime = 0; // Variabile per tracciare il tempo

void setupAccessPoint() {
  WiFi.softAP(ssid, password);
  Serial.println("Access Point avviato");
  Serial.print("SSID: ");
  Serial.println(ssid);
  Serial.print("IP: ");
  Serial.println(WiFi.softAPIP());
}

void printConnectedClients() {
  Serial.println("Elenco client connessi:");
  for (int i = 0; i < 5; i++) {
    if (clients[i] && clients[i].connected()) {
      Serial.printf("Client ID %d: IP %s\n", i, clients[i].remoteIP().toString().c_str());
    }
  }
}

void handleNewClients() {
  if (server.hasClient()) {
    for (int i = 0; i < 5; i++) {
      if (!clients[i] || !clients[i].connected()) {
        if (clients[i]) clients[i].stop();
        clients[i] = server.available();
        if (clients[i]) {
          Serial.printf("Nuovo client connesso: ID %d, IP %s\n", i, clients[i].remoteIP().toString().c_str());
          clients[i].printf("ID:%d\n", i); // Invia ID al client
        }
        break;
      }
    }
  }
}

void handleClientMessages() {
  for (int i = 0; i < 5; i++) {
    if (clients[i] && clients[i].connected() && clients[i].available()) {
      String message = clients[i].readStringUntil('\n');
      Serial.printf("Client %d: %s\n", i, message.c_str());
      for (int j = 0; j < 5; j++) {
        if (j != i && clients[j] && clients[j].connected()) {
          clients[j].println(message);
        }
      }
    }
  }
}

void sendMessageToClient(int clientIndex, const String& message) {
  if (clients[clientIndex] && clients[clientIndex].connected()) {
    clients[clientIndex].println(message);
    Serial.printf("Messaggio inviato al client %d: %s\n", clientIndex, message.c_str());
  } else {
    Serial.printf("Client %d non connesso\n", clientIndex);
  }
}

void broadcastMessage(const String& message) {
  for (int i = 0; i < 5; i++) {
    if (clients[i] && clients[i].connected()) {
      clients[i].println(message);
    }
  }
  Serial.printf("Messaggio broadcast inviato: %s\n", message.c_str());
}

void handleServerInput() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    if (input.startsWith("send ")) {
      int clientIndex = input.substring(5, 6).toInt();
      String message = input.substring(7);
      sendMessageToClient(clientIndex, message);
    } else if (input.startsWith("broadcast ")) {
      String message = input.substring(10);
      broadcastMessage(message);
    } else {
      Serial.println("Comando non riconosciuto. Usa 'send <index> <message>' o 'broadcast <message>'");
    }
  }
}

void printConfigurationPeriodically() {
  unsigned long currentTime = millis();
  if (currentTime - lastConfigPrintTime >= 60000) { // 1 minuto = 60000 ms
    Serial.println("Configurazione attuale:");
    Serial.print("SSID: ");
    Serial.println(ssid);
    Serial.print("IP: ");
    Serial.println(WiFi.softAPIP());
    printConnectedClients(); // Mostra elenco client connessi
    lastConfigPrintTime = currentTime;
  }
}

void setup() {
  Serial.begin(115200);
  setupAccessPoint();
  server.begin();
  Serial.println("Server avviato");
}

void loop() {
  handleNewClients();
  handleClientMessages();
  handleServerInput();
  printConfigurationPeriodically();
}