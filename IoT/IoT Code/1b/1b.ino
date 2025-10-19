#include <WiFi.h>

// Credenziali per connettersi alla rete esistente (modalità Station)
const char* sta_ssid = "Mate10";
const char* sta_password = "3661461500";

// Credenziali per l'Access Point
const char* ap_ssid = "ESP32-Access-Point";
const char* ap_password = "123456789";

void setup() {
  Serial.begin(115200);
  
  // Configura modalità Station
  WiFi.begin(sta_ssid, sta_password);
  
  // Configura Access Point simultaneamente
  WiFi.softAP(ap_ssid, ap_password, 1);  // 1 indica il canale

  // Attendi connessione Station
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nModalità ibrida attiva");
  Serial.printf("Station IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("Access Point IP: %s\n", WiFi.softAPIP().toString().c_str());
}

void loop() {
  Serial.printf("Clients AP connessi: %d\n", WiFi.softAPgetStationNum());
  delay(5000);
}