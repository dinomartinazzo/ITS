# Esempio 6: Aggiornamenti OTA

```cpp
#include <WiFi.h>
#include <ESPmDNS.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

const char* ssid = "TuaReteWiFi";
const char* password = "TuaPassword";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  ArduinoOTA.setHostname("esp32-ota");
  ArduinoOTA.setPassword("admin");
  
  ArduinoOTA.onStart([]() {
    Serial.println("Avvio OTA");
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nCompletato");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progresso: %u%%\r", (progress / (total / 100)));
  });

  ArduinoOTA.begin();
  Serial.println("OTA Pronto");
  Serial.println(WiFi.localIP());
}

void loop() {
  ArduinoOTA.handle();
}
```
