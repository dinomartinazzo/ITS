# Sistema di Chat con ESP32

Questo progetto implementa un sistema di chat utilizzando dispositivi ESP32 in una rete indipendente. Un ESP32 funge da server e Access Point (AP), mentre più ESP32 agiscono come client connessi direttamente all'AP.

## Funzionalità
- Il server funge da Access Point e gestisce più connessioni client.
- I client inviano e ricevono messaggi in tempo reale.
- La comunicazione avviene tramite socket TCP.
- Gestione delle riconnessioni e delle eccezioni in tempo reale.
- Il server può inviare messaggi a un singolo client o a tutti i client (broadcast).

---

## Codice del Server

Il server agisce come Access Point e inoltra i messaggi tra i client connessi.

### Requisiti
- Scheda ESP32
- Arduino IDE con supporto per schede ESP32 installato

### Codice
```cpp
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
```

---

## Codice del Client

Il client si connette direttamente all'Access Point del server.

### Requisiti
- Scheda ESP32
- Arduino IDE con supporto per schede ESP32 installato

### Codice
```cpp
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
```

---

## Istruzioni per l'Uso

1. Il server funge da Access Point con SSID `ESP32_Chat_AP` e password `12345678`.
2. Caricare il codice del server su un ESP32 e il codice del client su altri dispositivi ESP32.
3. I client si connettono direttamente all'Access Point del server.
4. Aprire il Monitor Seriale per ogni dispositivo per inviare e ricevere messaggi.
5. Sul server, utilizzare i comandi `send <index> <message>` per inviare un messaggio a un singolo client o `broadcast <message>` per inviare un messaggio a tutti i client.

---

## Note
- Il codice ora gestisce automaticamente le riconnessioni in caso di disconnessione.
- Le funzionalità principali sono modularizzate per migliorare la leggibilità e la manutenzione.
- L'indirizzo IP del server è `192.168.4.1` per impostazione predefinita.
- Il server supporta l'invio di messaggi a un singolo client o a tutti i client connessi.
- Il server ora mostra l'elenco dei client connessi e invia un ID univoco a ciascun client.
- Il client visualizza l'ID assegnato dal server.
