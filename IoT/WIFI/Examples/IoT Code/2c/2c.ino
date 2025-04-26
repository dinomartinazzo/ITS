#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";
WebServer server(80);

String getHTML() {
  String html = "<!DOCTYPE html><html><head>";
  html += "<meta http-equiv='refresh' content='5'/>";
  html += "<title>ESP32 AP Statistics</title>";
  html += "<style>body{font-family:Arial;margin:20px;}";
  html += "table{border-collapse:collapse;width:100%;}";
  html += "td,th{border:1px solid #ddd;padding:8px;}</style></head>";
  html += "<body><h1>ESP32 Network Statistics</h1>";
  html += "<table><tr><th>Parameter</th><th>Value</th></tr>";
  
  // Add network statistics
  html += "<tr><td>Connected Devices</td><td>" + String(WiFi.softAPgetStationNum()) + "</td></tr>";
  html += "<tr><td>Network SSID</td><td>" + String(WiFi.softAPSSID()) + "</td></tr>";
  html += "<tr><td>AP IP Address</td><td>" + WiFi.softAPIP().toString() + "</td></tr>";
  html += "<tr><td>AP MAC Address</td><td>" + WiFi.softAPmacAddress() + "</td></tr>";
  html += "<tr><td>Channel</td><td>" + String(WiFi.channel()) + "</td></tr>";
  html += "<tr><td>TX Power</td><td>" + String(WiFi.getTxPower()) + " dBm</td></tr>";
  html += "<tr><td>Free Memory</td><td>" + String(ESP.getFreeHeap()) + " bytes</td></tr>";
  
  html += "</table><p><small>Page auto-refreshes every 5 seconds</small></p></body></html>";
  return html;
}

void handleRoot() {
  server.send(200, "text/html", getHTML());
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  
  server.on("/", handleRoot);
  server.begin();
  
  Serial.println("Access Point e WebServer Avviati");
  Serial.printf("Connettiti a %s e visita http://%s\n", ssid, WiFi.softAPIP().toString().c_str());
}

void loop() {
  server.handleClient();
  delay(10);
}