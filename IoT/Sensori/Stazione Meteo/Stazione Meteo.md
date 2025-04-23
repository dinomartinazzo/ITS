# Stazione Meteo con OpenWeatherMap

Questo progetto utilizza un microcontrollore (ad esempio ESP32) per connettersi al servizio OpenWeatherMap e ottenere dati meteo in tempo reale. I dati vengono visualizzati su una pagina web ospitata dal microcontrollore stesso.

## Come funziona

1. **Connessione WiFi**: Il microcontrollore si connette a una rete WiFi utilizzando le credenziali fornite nel codice (`ssid` e `password`).
2. **Richiesta API**: Viene effettuata una richiesta HTTP al servizio OpenWeatherMap utilizzando un'API key personale (`apiKey`) e il nome della città (`location`).
3. **Risposta JSON**: OpenWeatherMap restituisce i dati meteo in formato JSON.
4. **Parsing JSON**: Il microcontrollore analizza il JSON per estrarre informazioni come temperatura, umidità, velocità del vento, ecc.
5. **Visualizzazione Web**: I dati vengono formattati in HTML e resi disponibili su una pagina web accessibile tramite il browser.

## Dettagli del JSON di ritorno

Il JSON restituito da OpenWeatherMap contiene diverse informazioni. Ecco una spiegazione dei campi principali:

- **`coord`**: Coordinate geografiche della città (latitudine e longitudine).
- **`weather`**: Array contenente informazioni sulle condizioni meteo:
  - `id`: ID della condizione meteo.
  - `main`: Descrizione breve (es. "Clouds").
  - `description`: Descrizione dettagliata (es. "few clouds").
  - `icon`: Codice per l'icona meteo.
- **`main`**: Informazioni principali:
  - `temp`: Temperatura attuale (in gradi Celsius se specificato).
  - `feels_like`: Temperatura percepita.
  - `temp_min` e `temp_max`: Temperature minima e massima.
  - `pressure`: Pressione atmosferica (in hPa).
  - `humidity`: Umidità relativa (in percentuale).
- **`wind`**: Informazioni sul vento:
  - `speed`: Velocità del vento (in m/s).
  - `deg`: Direzione del vento (in gradi).
- **`sys`**: Informazioni aggiuntive:
  - `country`: Codice del paese.
  - `sunrise` e `sunset`: Orari di alba e tramonto (in formato UNIX).
- **`dt`**: Timestamp dell'ultimo aggiornamento (in formato UNIX).
- **`name`**: Nome della città.

## API Key

L'API key (`apiKey`) è una chiave univoca fornita da OpenWeatherMap al momento della registrazione. Serve per autenticare le richieste al servizio. È importante mantenerla privata per evitare utilizzi non autorizzati.

## Codice HTML generato

Il codice HTML generato dal microcontrollore include:
- Un titolo con il nome della città e del paese.
- Un'icona meteo basata sul codice `icon` fornito dal JSON.
- Informazioni dettagliate come temperatura, umidità, pressione, velocità del vento, orari di alba e tramonto.
- Un modulo per aggiornare la città visualizzata.

## Esempio di utilizzo

1. Modifica le credenziali WiFi e l'API key nel codice.
2. Carica il codice sul microcontrollore.
3. Accedi alla pagina web tramite l'indirizzo IP del dispositivo.
4. Visualizza i dati meteo e aggiorna la città tramite il modulo.

Per ulteriori dettagli, visita il sito ufficiale di OpenWeatherMap: [https://openweathermap.org/](https://openweathermap.org/)

```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "main": {
    "temp": 289.79,
    "feels_like": 288.89,
    "temp_min": 288.1,
    "temp_max": 290.67,
    "pressure": 1004,
    "humidity": 53
  },
  "wind": {
    "speed": 5.66,
    "deg": 230
  },
  "sys": {
    "country": "GB",
    "sunrise": 1744520922,
    "sunset": 1744570372
  },
  "name": "London"
}
```

```cpp
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

unsigned long lastPrintTime = 0;

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

void printWeatherDataToSerial() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi non connesso");
    return;
  }

  String url = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apiKey + "&units=metric";
  HTTPClient http;
  http.begin(url);
  int httpCode = http.GET();

  if (httpCode <= 0) {
    Serial.println("Errore HTTP");
    return;
  }

  String payload = http.getString();
  JsonDocument doc;
  DeserializationError error = deserializeJson(doc, payload);

  if (error) {
    Serial.println("Errore parsing JSON");
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

  // Stampa dati in seriale
  Serial.println("=== Meteo ===");
  Serial.println("IP: " + WiFi.localIP().toString());
  Serial.println("Città: " + city + ", " + country);
  Serial.println("Descrizione: " + desc);
  Serial.println("Icona: " + icon);
  Serial.println("Temperatura: " + String(temp) + "°C (min: " + String(temp_min) + "°C, max: " + String(temp_max) + "°C)");
  Serial.println("Umidità: " + String(humidity) + "%");
  Serial.println("Pressione: " + String(pressure) + " hPa");
  Serial.println("Vento: " + String(wind) + " m/s (" + String(wind_deg) + "°)");
  Serial.println("Alba: " + formatTime(sunrise));
  Serial.println("Tramonto: " + formatTime(sunset));
  Serial.println("Ultimo aggiornamento: " + formatTime(dt));
  Serial.println("================");
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
    String newLocation = server.arg("q");
    if (newLocation.length() > 0 && newLocation.indexOf(',') != -1) {
      location = newLocation;
      server.sendHeader("Location", "/", true);
      server.send(302, "text/plain", "Redirecting...");
    } else {
      server.send(400, "text/html", 
        "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Errore</title></head><body>"
        "<h2>Errore: Formato città non valido</h2>"
        "<p>Il formato corretto è: <strong>NomeCittà,Paese</strong> (es: Torino,it)</p>"
        "<a href='/'>Torna alla pagina principale</a>"
        "</body></html>");
    }
  } else {
    server.send(400, "text/html", 
      "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Errore</title></head><body>"
      "<h2>Errore: Parametro 'q' mancante</h2>"
      "<a href='/'>Torna alla pagina principale</a>"
      "</body></html>");
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

  // Stampa dati ogni 10 secondi
  if (millis() - lastPrintTime >= 10000) {
    lastPrintTime = millis();
    printWeatherDataToSerial();
  }
}
```
