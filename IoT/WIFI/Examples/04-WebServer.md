# Esempio 4: Web Server Basilare

```cpp
#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "TuaReteWiFi";
const char* password = "TuaPassword";

WebServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  server.on("/", HTTP_GET, []() {
    server.send(200, "text/html",
      "<html><body>"
      "<h1>ESP32 Web Server</h1>"
      "<p>Benvenuto nel web server ESP32!</p>"
      "</body></html>");
  });

  server.begin();
  Serial.println("\nWeb server attivo");
  Serial.println(WiFi.localIP());
}

void loop() {
  server.handleClient();
}
```
