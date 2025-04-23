# Chiamata API OpenWeatherMap: Day Summary

Questo file descrive come effettuare una chiamata all'endpoint `https://api.openweathermap.org/data/3.0/onecall/day_summary` per ottenere un riepilogo giornaliero delle condizioni meteo.

## Parametri della chiamata

- **`lat`**: Latitudine della posizione (es. `45.4642` per Milano).
- **`lon`**: Longitudine della posizione (es. `9.1900` per Milano).
- **`date`**: Data per la quale si desidera il riepilogo (formato `YYYY-MM-DD`).
- **`appid`**: La tua API key personale fornita da OpenWeatherMap.

## Esempio di chiamata

Ecco un esempio di chiamata HTTP GET:

```
https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=45.4642&lon=9.1900&date=2023-10-01&appid=YOUR_API_KEY
```

## Risposta JSON

La risposta JSON conterrà un riepilogo delle condizioni meteo per la data specificata. Esempio:

```json
{
  "date": "2023-10-01",
  "summary": {
    "temp_min": 15.2,
    "temp_max": 22.5,
    "humidity_avg": 65,
    "wind_speed_avg": 3.5,
    "precipitation": 0.0
  }
}
```

### Campi principali

- **`temp_min`**: Temperatura minima registrata (in gradi Celsius).
- **`temp_max`**: Temperatura massima registrata (in gradi Celsius).
- **`humidity_avg`**: Umidità media (in percentuale).
- **`wind_speed_avg`**: Velocità media del vento (in m/s).
- **`precipitation`**: Quantità di precipitazioni (in mm).

## Implementazione in C++

Ecco un esempio di codice per effettuare la chiamata e gestire la risposta:

```cpp
// filepath: z:\Documents MD\CoockBooks\Sviluppo 2025\IoT\Sensori\Stazione Meteo 001.cpp
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourWiFiPassword";
String apiKey = "YourAPIKey";
String lat = "45.4642"; // Milano
String lon = "9.1900"; // Milano
String date = "2023-10-01";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Connessione a WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connesso. IP: " + WiFi.localIP().toString());

  fetchDaySummary();
}

void fetchDaySummary() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi non connesso");
    return;
  }

  String url = "https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=" + lat + "&lon=" + lon + "&date=" + date + "&appid=" + apiKey;
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

    float temp_min = doc["summary"]["temp_min"];
    float temp_max = doc["summary"]["temp_max"];
    int humidity_avg = doc["summary"]["humidity_avg"];
    float wind_speed_avg = doc["summary"]["wind_speed_avg"];
    float precipitation = doc["summary"]["precipitation"];

    Serial.println("=== Riepilogo Meteo ===");
    Serial.println("Temperatura Minima: " + String(temp_min) + "°C");
    Serial.println("Temperatura Massima: " + String(temp_max) + "°C");
    Serial.println("Umidità Media: " + String(humidity_avg) + "%");
    Serial.println("Velocità Media del Vento: " + String(wind_speed_avg) + " m/s");
    Serial.println("Precipitazioni: " + String(precipitation) + " mm");
    Serial.println("=======================");
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
- La data deve essere fornita nel formato `YYYY-MM-DD`.
- Per una panoramica delle condizioni meteo attuali, consulta anche la chiamata API `overview` descritta nel file [Stazione Meteo 002.md](Stazione%20Meteo%20002.md).
- Consulta la documentazione ufficiale di OpenWeatherMap per ulteriori dettagli: [https://openweathermap.org/api](https://openweathermap.org/api).
