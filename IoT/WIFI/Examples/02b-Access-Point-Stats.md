# Esempio 2B: Access Point con Statistiche

```cpp
#include <WiFi.h>

const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";

void printNetworkInfo() {
  Serial.printf("\n--- Statistiche Access Point ---\n");
  Serial.printf("Dispositivi connessi: %d\n", WiFi.softAPgetStationNum());
  Serial.printf("Canale corrente: %d\n", WiFi.channel());
  Serial.printf("Potenza trasmissione: %d dBm\n", WiFi.getTxPower());
  Serial.printf("Memoria libera: %d bytes\n", ESP.getFreeHeap());
  Serial.printf("SSID: %s\n", WiFi.softAPSSID());
  Serial.printf("IP AP: %s\n", WiFi.softAPIP().toString().c_str());
  Serial.printf("MAC AP: %s\n", WiFi.softAPmacAddress().c_str());
}

void setup() {
  Serial.begin(115200);
  
  WiFi.softAP(ssid, password);
  
  Serial.println("Access Point Avviato");
  Serial.printf("SSID: %s\n", ssid);
  Serial.printf("IP Address: %s\n", WiFi.softAPIP().toString().c_str());
  Serial.printf("Canale: %d\n", WiFi.channel());
  Serial.printf("MAC Address AP: %s\n", WiFi.softAPmacAddress().c_str());
}

void loop() {
  printNetworkInfo();
  delay(10000);
}
```
