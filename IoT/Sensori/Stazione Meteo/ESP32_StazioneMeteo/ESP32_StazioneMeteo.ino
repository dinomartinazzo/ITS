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


// HTML semplificato e dinamico
String buildPage(String city, String country, String desc, String icon,
                 float temp, float temp_min, float temp_max, int humidity, int pressure,
                 float wind, int wind_deg, String sunrise, String sunset, String last_update) {
  return "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Meteo</title></head><body>"
         "<h2>Meteo per " + city + ", " + country + "</h2>"
         "<p><img src='https://openweathermap.org/img/wn/" + icon + "@2x.png'></p>"
         "<p><strong>Condizione:</strong> " + desc + "</p>"
         "<p><strong>Temperatura:</strong> " + String(temp) + "°C (min: " + String(temp_min) + "°C, max: " + String(temp_max) + "°C)</p>"
         "<p><strong>Umidità:</strong> " + String(humidity) + "%</p>"
         "<p><strong>Pressione:</strong> " + String(pressure) + " hPa</p>"
         "<p><strong>Vento:</strong> " + String(wind) + " m/s (" + String(wind_deg) + "°)</p>"
         "<p><strong>Alba:</strong> " + sunrise + " - <strong>Tramonto:</strong> " + sunset + "</p>"
         "<p><strong>Ultimo aggiornamento:</strong> " + last_update + "</p><br>"
         "<form action='/setcity'><input name='q' placeholder='Es: Torino,it'><button>Aggiorna Città</button></form>"
         "<script>setTimeout(()=>location.reload(), 60000);</script>"
         "</body></html>";
}

// Conversione UNIX -> ora leggibile
String formatTime(time_t t) {
  char buf[20];
  strftime(buf, sizeof(buf), "%H:%M:%S", localtime(&t));
  return String(buf);
}

void handleRoot() {
  if (WiFi.status() != WL_CONNECTED) {
    server.send(503, "text/plain", "WiFi non connesso");
    return;
  }

  String url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apiKey + "&units=metric";
  HTTPClient http;
  http.begin(url);
  int httpCode = http.GET();

  if (httpCode <= 0) {
    server.send(500, "text/plain", "Errore HTTP");
    return;
  }

  String payload = http.getString();
  JsonDocument doc;
  DeserializationError error = deserializeJson(doc, payload);

  if (error) {
    server.send(500, "text/plain", "Errore parsing JSON");
    return;
  }

  // Estrazione dati principali
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

  String page = buildPage(
    city, country, desc, icon,
    temp, temp_min, temp_max, humidity, pressure,
    wind, wind_deg, formatTime(sunrise), formatTime(sunset), formatTime(dt)
  );

  server.send(200, "text/html", page);
}

void handleSetCity() {
  if (server.hasArg("q")) {
    location = server.arg("q");
    server.sendHeader("Location", "/", true);
    server.send(302, "text/plain", "Redirecting...");
  } else {
    server.send(400, "text/plain", "Parametro 'q' mancante");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Connessione a WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connesso. IP: " + WiFi.localIP().toString());

  configTime(7200, 0, "pool.ntp.org");  // fuso orario Italia

  server.on("/", handleRoot);
  server.on("/setcity", handleSetCity);
  server.begin();
  Serial.println("Web server avviato.");
}

void loop() {
  server.handleClient();
}