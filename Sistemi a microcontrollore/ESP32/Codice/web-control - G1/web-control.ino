#include <WiFi.h>

const char* ssid = "ESP32";
const char* password = "123456"; // Lascia vuoto per rete aperta
bool usePassword = true;

WiFiServer server(80);
float temperature = 10.0; // Temperatura iniziale simulata
bool increasing = true; // Flag per determinare la direzione della variazione

// Definizione dei pin LED per la visualizzazione a colonna
const int ledPins[] = {21, 22, 19, 23, 18, 5, 2};
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, usePassword ? password : NULL);
  Serial.println("AP IP address: " + WiFi.softAPIP().toString());
  server.begin();

  // Imposta i pin dei LED come output
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
}

void loop() {
  // Simulazione della temperatura tra 10 e 35 gradi
  if (increasing) {
    temperature += 0.1;
    if (temperature >= 35.0) increasing = false;
  } else {
    temperature -= 0.1;
    if (temperature <= 10.0) increasing = true;
  }
  
  // Gestione dei LED per la visualizzazione a colonna
  int activeLeds = map(temperature, 10, 35, 0, numLeds); // Mappa la temperatura al numero di LED
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(ledPins[i], i < activeLeds ? HIGH : LOW);
  }

  WiFiClient client = server.available();
  if (client) {
    String request = "";
    while (client.available()) request += (char)client.read();
    
    if (request.indexOf("GET /temperature") >= 0) {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/plain");
      client.println("Connection: close");
      client.println();
      client.println(String(temperature, 1));
    } else {
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: text/html");
      client.println("Connection: close");
      client.println();
      client.println("<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>");
      client.println("<script>");
      client.println("let tempData = [];");
      client.println("function update(){ fetch('/temperature').then(r => r.text()).then(t => {");
      client.println("document.getElementById('temp').innerText = t + ' °C';");
      client.println("let tempValue = parseFloat(t);");
      client.println("let barWidth = ((tempValue - 10) / 25) * 100;");
      client.println("document.getElementById('bar').style.width = barWidth + '%';");
      client.println("tempData.push(tempValue);");
      client.println("if (tempData.length > 50) tempData.shift();");
      client.println("drawStrip(tempData);");
      client.println("}); }");
      client.println("setInterval(update, 500);");
      client.println("function drawStrip(data) {");
      client.println("let canvas = document.getElementById('stripChart');");
      client.println("let ctx = canvas.getContext('2d');");
      client.println("ctx.clearRect(0, 0, canvas.width, canvas.height);");
      client.println("ctx.beginPath();");
      client.println("ctx.moveTo(0, canvas.height - ((data[0] - 10) / 25) * canvas.height);");
      client.println("for (let i = 1; i < data.length; i++) {");
      client.println("let x = (i / 50) * canvas.width;");
      client.println("let y = canvas.height - ((data[i] - 10) / 25) * canvas.height;");
      client.println("ctx.lineTo(x, y);");
      client.println("}");
      client.println("ctx.strokeStyle = 'blue'; ctx.lineWidth = 2; ctx.stroke();");
      client.println("}");
      client.println("</script>");
      client.println("<style>");
      client.println(".bar-container { width: 100%; background-color: #ddd; height: 30px; border-radius: 5px; overflow: hidden; }");
      client.println(".bar { height: 100%; background-color: #4CAF50; width: 0%; transition: width 0.3s ease-in-out; }");
      client.println("</style>");
      client.println("</head>");
      client.println("<body><h5>ESP32 Web Server</h5>");
      client.println("<p>Temperatura attuale: <span id='temp'>-- °C</span></p>");
      client.println("<div class='bar-container'><div id='bar' class='bar'></div></div>");
      client.println("<canvas id='stripChart' width='400' height='100'></canvas>");
      client.println("</body></html>");
    }
    client.stop();
  }
}
