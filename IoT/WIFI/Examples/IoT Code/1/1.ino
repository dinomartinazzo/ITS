#include <WiFi.h>

const char* ssid = "Mate10";
const char* password = "3661461500";

void setup() {
  Serial.begin(115200);
  
  // Configura modalità station
  WiFi.mode(WIFI_STA);
  
  // Imposta esplicitamente WPA2
  WiFi.begin(ssid, password);
  
  Serial.println("Connessione WPA2...");
  
  // Attendi connessione con timeout
  int timeout = 0;
  while (WiFi.status() != WL_CONNECTED && timeout < 20) {
    delay(500);
    Serial.print(".");
    timeout++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnesso al WiFi");
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());
    Serial.print("Indirizzo IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("Potenza segnale: ");
    Serial.print(WiFi.RSSI());
    Serial.println(" dBm");
  } else {
    Serial.println("\nConnessione fallita!");
  }
}

void loop() {
  if(WiFi.status() == WL_CONNECTED) {
    Serial.printf("Connesso a %s, potenza: %d dBm\n", 
      WiFi.SSID().c_str(), 
      WiFi.RSSI()
    );
  } else {
    Serial.println("Connessione persa, riprovo...");
    WiFi.reconnect();
  }
  delay(5000);
}