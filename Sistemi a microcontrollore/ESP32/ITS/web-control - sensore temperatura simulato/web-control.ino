#include <WiFi.h>

const char* ssid = "ESP32";
const char* password = "123456"; // Lascia vuoto per rete aperta
bool usePassword = true;

WiFiServer server(80);
float temperature = 22.5; // Temperatura iniziale simulata

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, usePassword ? password : NULL);
  Serial.println("AP IP address: " + WiFi.softAPIP().toString());
  server.begin();
}

void loop() {
  // Simulazione variazione temperatura tra 10 e 35 gradi con precisione 0.1
  float variation = ((random(-5, 6)) / 10.0); // Variazione casuale tra -0.5 e +0.5
  temperature += variation;
  if (temperature < 10.0) temperature = 10.0;
  if (temperature > 35.0) temperature = 35.0;
  
  WiFiClient client = server.available();
  if (client) {
    String request = "";
    while (client.available()) request += (char)client.read();
    
    if (request.indexOf("GET /temperature") >= 0) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/plain");
      client.println("Connection: close");
      client.println();
      client.println(String(temperature, 1) + " °C"); // Precisione 0.1
    } else {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/html");
      client.println("Connection: close");
      client.println();
      client.println("<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>");
      client.println("<script>");
      client.println("function update(){ fetch('/temperature').then(r => r.text()).then(t => document.getElementById('temp').innerText = t); }");
      client.println("setInterval(update, 300);");
      client.println("</script></head>");
      client.println("<body><h5>ESP32 Web Server</h5>");
      client.println("<p></h3>Temperatura attuale: <span id='temp'>-- °C</span></h3></p>");
      client.println("</body></html>");
    }
    client.stop();
  }
}