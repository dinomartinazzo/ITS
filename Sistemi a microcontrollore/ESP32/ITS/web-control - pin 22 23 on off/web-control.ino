#include <WiFi.h>

// Configurazione della rete Wi-Fi
const char* ssid = "ESP32";
const char* password = "123456"; // Lascia vuoto per rete aperta
bool usePassword = true; // Imposta a false per una rete aperta

// Imposta la potenza massima del Wi-Fi (valori tra 8 e 20 dBm)
const int wifiPower = 20; // 20 dBm = 100 mW

// Imposta il server sulla porta 80
WiFiServer server(80);

// Variabili per lo stato degli output
String output22State = "off";
String output23State = "off";

// Definizione dei pin GPIO
const int pin22 = 22;
const int pin23 = 23;

void setup() {
  Serial.begin(115200);
  
  // Imposta i pin GPIO come output e spegnili inizialmente
  pinMode(pin22, OUTPUT);
  pinMode(pin23, OUTPUT);
  digitalWrite(pin22, LOW);
  digitalWrite(pin23, LOW);
  
  // Imposta la potenza massima del Wi-Fi
  WiFi.setTxPower((wifi_power_t)wifiPower);
  
  Serial.print("Impostazione Access Point...");
  if (usePassword) {
    WiFi.softAP(ssid, password, 11, 0, 4); // Canale 11, nessun SSID nascosto, max 4 client
  } else {
    WiFi.softAP(ssid, NULL, 11, 0, 4); // NULL per creare una rete aperta
  }

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  Serial.print("SSID impostato: ");
  Serial.println(ssid);

  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Nuovo client connesso.");
    String header = "";
    String currentLine = "";
    
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        header += c;
        
        if (c == '\n') {
          if (currentLine.length() == 0) {
            // Invio dell'header HTTP
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            
            // Controllo dello stato dei GPIO
            if (header.indexOf("GET /22/on") >= 0) {
              Serial.println("GPIO 22 acceso");
              output22State = "on";
              digitalWrite(pin22, HIGH);
            } else if (header.indexOf("GET /22/off") >= 0) {
              Serial.println("GPIO 22 spento");
              output22State = "off";
              digitalWrite(pin22, LOW);
            } else if (header.indexOf("GET /23/on") >= 0) {
              Serial.println("GPIO 23 acceso");
              output23State = "on";
              digitalWrite(pin23, HIGH);
            } else if (header.indexOf("GET /23/off") >= 0) {
              Serial.println("GPIO 23 spento");
              output23State = "off";
              digitalWrite(pin23, LOW);
            }
            
            // Creazione della pagina HTML
            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<style>html { font-family: Helvetica; text-align: center;}");
            client.println(".button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px;");
            client.println("text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}");
            client.println(".button2 {background-color: #555555;}</style></head>");
            
            client.println("<body><h1>ESP32 Web Server</h1>");
            client.println("<p>GPIO 22 - Stato " + output22State + "</p>");
            client.println(output22State == "off" ? "<p><a href='/22/on'><button class='button'>ON</button></a></p>" : "<p><a href='/22/off'><button class='button button2'>OFF</button></a></p>");
            client.println("<p>GPIO 23 - Stato " + output23State + "</p>");
            client.println(output23State == "off" ? "<p><a href='/23/on'><button class='button'>ON</button></a></p>" : "<p><a href='/23/off'><button class='button button2'>OFF</button></a></p>");
            client.println("</body></html>");
            
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    header = ""; // Libera memoria
    client.stop();
    Serial.println("Client disconnesso.");
  }
}