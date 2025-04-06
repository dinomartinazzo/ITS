# Esempio 2: Access Point Mode

```cpp
#include <WiFi.h>

const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";

void setup() {
  Serial.begin(115200);
  
  WiFi.softAP(ssid, password);

  Serial.println("Access Point Avviato");
  Serial.print("SSID: ");
  Serial.println(ssid);
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());
}

void loop() {
  Serial.printf("Dispositivi connessi: %d\n", WiFi.softAPgetStationNum());
  delay(5000);
}
```
