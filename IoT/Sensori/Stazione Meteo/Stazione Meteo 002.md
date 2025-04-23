# Chiamata API OpenWeatherMap: Overview

Questo file descrive come effettuare una chiamata all'endpoint `https://api.openweathermap.org/data/3.0/onecall` per ottenere una panoramica delle condizioni meteo attuali.

## Parametri della chiamata

- **`lat`**: Latitudine della posizione (es. `45.4642` per Milano).
- **`lon`**: Longitudine della posizione (es. `9.1900` per Milano).
- **`lang`**: Lingua della risposta (es. `it_it` per italiano).
- **`appid`**: La tua API key personale fornita da OpenWeatherMap.

## Esempio di chiamata

Ecco un esempio di chiamata HTTP GET:

```
https://api.openweathermap.org/data/3.0/onecall?lat=45.4642&lon=9.1900&lang=it_it&appid=YOUR_API_KEY

https://openweathermap.org/api/one-call-3#multi
```

## Risposta JSON

La risposta JSON conterrà una panoramica delle condizioni meteo attuali. Esempio:

```json
{
  "current": {
    "temp": 20.5,
    "humidity": 60,
    "pressure": 1012,
    "wind_speed": 4.2,
    "weather": {
      "description": "clear sky",
      "icon": "01d"
    }
  }
}
```

### Campi principali

- **`temp`**: Temperatura attuale (in gradi Celsius).
- **`humidity`**: Umidità relativa (in percentuale).
- **`pressure`**: Pressione atmosferica (in hPa).
- **`wind_speed`**: Velocità del vento (in m/s).
- **`weather.description`**: Descrizione delle condizioni meteo.
- **`weather.icon`**: Codice per l'icona meteo.

## Implementazione in C++

Ecco un esempio di codice per effettuare la chiamata e gestire la risposta:

```cpp
// filepath: z:\Documents MD\CoockBooks\Sviluppo 2025\IoT\Sensori\Stazione Meteo 002.cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
String apiKey = "YourAPIKey";
String lat = "45.4642"; // Milano
String lon = "9.1900"; // Milano
String lang = "it_it"; // Italiano

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Connessione a WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connesso. IP: " + WiFi.localIP().toString());

  fetchOverview();
}

void fetchOverview() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi non connesso");
    return;
  }

  String url = "https://api.openweathermap.org/data/3.0/onecall?lat=" + lat + "&lon=" + lon + "&lang=" + lang + "&appid=" + apiKey;
  HTTPClient http;
  http.begin(url);
  int httpCode = http.GET();

  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println("Risposta ricevuta: " + payload);

    // Parsing JSON
    StaticJsonDocument<512> doc;
    DeserializationError error = deserializeJson(doc, payload);

    if (error) {
      Serial.println("Errore parsing JSON");
      return;
    }

    float temp = doc["current"]["temp"];
    int humidity = doc["current"]["humidity"];
    int pressure = doc["current"]["pressure"];
    float wind_speed = doc["current"]["wind_speed"];
    String description = doc["current"]["weather"]["description"];
    String icon = doc["current"]["weather"]["icon"];

    Serial.println("=== Panoramica Meteo ===");
    Serial.println("Temperatura: " + String(temp) + "°C");
    Serial.println("Umidità: " + String(humidity) + "%");
    Serial.println("Pressione: " + String(pressure) + " hPa");
    Serial.println("Velocità del Vento: " + String(wind_speed) + " m/s");
    Serial.println("Descrizione: " + description);
    Serial.println("Icona: " + icon);
    Serial.println("========================");
  } else {
    Serial.println("Errore HTTP: " + String(httpCode));
  }

  http.end();
}

void loop() {
  // Nessuna operazione nel loop
}
```

## Note

- Assicurati di sostituire `YourWiFiSSID`, `YourWiFiPassword` e `YourAPIKey` con i tuoi valori reali.
- Per ottenere un riepilogo giornaliero delle condizioni meteo, consulta anche la chiamata API `day_summary` descritta nel file [Stazione Meteo 001.md](Stazione%20Meteo%20001.md).
- Consulta la documentazione ufficiale di OpenWeatherMap per ulteriori dettagli: [https://openweathermap.org/api](https://openweathermap.org/api).
