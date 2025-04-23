#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <time.h>

//const char* ssid = "Mate10";
const char* ssid = "FRITZ!Box 7530 NH";
const char* password = "3661461500";
String apiKey = "e2263c853668df51ff7b3ed521ec5f9d";
String location = "Milano,it";

WebServer server(80);

// 🕒 FORMATO ORARIO
String formatTime(time_t t) {
  char buf[20];
  strftime(buf, sizeof(buf), "%H:%M:%S", localtime(&t));
  return String(buf);
}

// 🧱 PAGINA ERRORE
String buildErrorPage(String msg) {
  return "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Errore</title></head><body>"
         "<h2>⚠️ Errore nel recupero dati meteo</h2>"
         "<p>" + msg + "</p><br>"
         "<a href='/'>🔙 Torna indietro</a></body></html>";
}

// 🌐 PAGINA METEO
String buildPage(String city, String country, String desc, String icon,
                 float temp, float temp_min, float temp_max, int humidity, int pressure,
                 float wind, int wind_deg, String sunrise, String sunset, String last_update) {
  return "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Meteo</title>"
         "<style>body{font-family:sans-serif;padding:20px;}label,input{margin:5px;}button{margin-left:5px;}"
         "table{border-collapse:collapse;}td,th{padding:6px 10px;border:1px solid #ccc;}</style></head><body>"
         "<h2>📍 Meteo per <strong>" + city + ", " + country + "</strong></h2>"
         "<p><img src='https://openweathermap.org/img/wn/" + icon + "@2x.png' alt='Icona meteo'></p>"
         "<table><tr><td><strong>Condizione:</strong></td><td>" + desc + "</td></tr>"
         "<tr><td><strong>Temperatura:</strong></td><td>" + String(temp) + "°C (min " + String(temp_min) + "°, max " + String(temp_max) + "°)</td></tr>"
         "<tr><td><strong>Umidità:</strong></td><td>" + String(humidity) + "%</td></tr>"
         "<tr><td><strong>Pressione:</strong></td><td>" + String(pressure) + " hPa</td></tr>"
         "<tr><td><strong>Vento:</strong></td><td>" + String(wind) + " m/s (" + String(wind_deg) + "°)</td></tr>"
         "<tr><td><strong>Alba:</strong></td><td>" + sunrise + "</td></tr>"
         "<tr><td><strong>Tramonto:</strong></td><td>" + sunset + "</td></tr>"
         "<tr><td><strong>Aggiornato alle:</strong></td><td>" + last_update + "</td></tr></table><br>"
         "<form onsubmit='return checkInput();' action='/setcity'>"
         "<label for='q'>🌐 Cambia città (es: Torino,it):</label>"
         "<input type='text' id='q' name='q' placeholder='Roma,it'>"
         "<button>🔄 Aggiorna</button></form>"
         "<script>"
         "function checkInput(){"
         "  const val = document.getElementById('q').value;"
         "  if(val.trim()===''){alert('Inserisci una città valida!');return false;}"
         "  return true;"
         "}"
         "setTimeout(()=>location.reload(), 60000);"
         "</script></body></html>";
}

// 🌐 GESTIONE PAGINA PRINCIPALE
void handleRoot() {
  if (WiFi.status() != WL_CONNECTED) {
    server.send(503, "text/plain", "WiFi non connesso");
    return;
  }

  String url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apiKey + "&units=metric";
  HTTPClient http;
  http.begin(url);
  int httpCode = http.GET();

  if (httpCode != 200) {
    server.send(200, "text/html", buildErrorPage("Codice HTTP: " + String(httpCode)));
    return;
  }

  String payload = http.getString();
  JsonDocument doc;
  DeserializationError error = deserializeJson(doc, payload);
  if (error) {
    server.send(200, "text/html", buildErrorPage("Errore parsing JSON"));
    return;
  }

  if (!doc["main"] || !doc["weather"]) {
    server.send(200, "text/html", buildErrorPage("Città non trovata o dati incompleti"));
    return;
  }

  // 🔎 Estrazione dati
  String city = doc["name"];
  String country = doc["sys"]["country"];
  String desc = doc["weather"][0]["description"];
  String icon = doc["weather"][0]["icon"];
  float temp = doc["main"]["temp"];
  float temp_min = doc["main"]["temp_min"];
  float temp_max = doc["main"]["temp_max"];
  int humidity = doc["main"]["humidity"];
  int pressure = doc["main"]["pressure"];
  float wind = doc["wind"]["speed"];
  int wind_deg = doc["wind"]["deg"];
  time_t sunrise = doc["sys"]["sunrise"];
  time_t sunset = doc["sys"]["sunset"];
  time_t dt = doc["dt"];

  // 🖨️ STAMPA SERIALE
  Serial.println("📡 METEO " + city + ", " + country);
  Serial.println("Descrizione: " + desc);
  Serial.println("Temp: " + String(temp) + "°C (min: " + String(temp_min) + "°C, max: " + String(temp_max) + "°C)");
  Serial.println("Umidità: " + String(humidity) + "%");
  Serial.println("Pressione: " + String(pressure) + " hPa");
  Serial.println("Vento: " + String(wind) + " m/s (" + String(wind_deg) + "°)");
  Serial.println("Alba: " + formatTime(sunrise) + " | Tramonto: " + formatTime(sunset));
  Serial.println("Ultimo aggiornamento: " + formatTime(dt));
  Serial.println("-------------------------------");

  server.send(200, "text/html", buildPage(
    city, country, desc, icon,
    temp, temp_min, temp_max, humidity, pressure,
    wind, wind_deg, formatTime(sunrise), formatTime(sunset), formatTime(dt)
  ));
}

// 🌐 GESTIONE CAMBIO CITTÀ
void handleSetCity() {
  if (server.hasArg("q")) {
    location = server.arg("q");
    server.sendHeader("Location", "/", true);
    server.send(302, "text/plain", "Redirect...");
  } else {
    server.send(400, "text/plain", "Parametro mancante");
  }
}

// ⚙️ SETUP
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("🔌 Connessione a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ WiFi connesso. IP: " + WiFi.localIP().toString());

  configTime(7200, 0, "pool.ntp.org"); // ora Italia (GMT+2)
  server.on("/", handleRoot);
  server.on("/setcity", handleSetCity);
  server.begin();
  Serial.println("🌐 Web server avviato");
}

// 🔁 LOOP
void loop() {
  server.handleClient();
}