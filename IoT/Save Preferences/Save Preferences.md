# Uso della libreria Preferences su ESP32 (Arduino IDE)

## 1. Introduzione
La libreria `Preferences` permette di salvare dati persistenti nella memoria NVS (Non-Volatile Storage) dell’ESP32. È ideale per memorizzare configurazioni, contatori, flag, strutture e piccole basi dati che devono sopravvivere a riavvii o spegnimenti.

**Prerequisiti:**
- ESP32 core installato su Arduino IDE 2.x
- Include: `#include <Preferences.h>`

---

## 2. Concetti Base
- **Namespace:** Ogni gruppo di dati è separato in uno spazio (max 15 caratteri).
- **Chiavi:** Ogni valore è associato a una chiave stringa.
- **Tipi supportati:** int, float, bool, String, byte array, ecc.

---

## 3. Esempio Base: Salvare e Leggere un Contatore
```cpp
#include <Preferences.h>
Preferences preferences;

void setup() {
  Serial.begin(115200);
  preferences.begin("mioSpazio", false); // false = lettura/scrittura
  int contatore = preferences.getInt("avvii", 0); // default 0
  Serial.print("Numero avvii precedenti: ");
  Serial.println(contatore);
  contatore++;
  preferences.putInt("avvii", contatore);
  Serial.print("Nuovo valore salvato: ");
  Serial.println(contatore);
  preferences.end();
}
void loop() {}
```
**Cosa fa:**
- Legge il numero di avvii precedenti
- Incrementa e salva il nuovo valore

---

## 3.1 Salvare e leggere una configurazione WiFi (SSID, password)

```cpp
#include <Preferences.h>
Preferences preferences;

struct WiFiConfig {
  char ssid[32];
  char password[64];
};

void salvaWiFiConfig(const WiFiConfig &cfg) {
  preferences.begin("wifi", false);
  preferences.putBytes("cfg", &cfg, sizeof(WiFiConfig));
  preferences.end();
}

bool leggiWiFiConfig(WiFiConfig &cfg) {
  preferences.begin("wifi", true);
  size_t size = preferences.getBytesLength("cfg");
  if (size != sizeof(WiFiConfig)) { preferences.end(); return false; }
  preferences.getBytes("cfg", &cfg, sizeof(WiFiConfig));
  preferences.end();
  return true;
}

void cancellaWiFiConfig() {
  preferences.begin("wifi", false);
  preferences.remove("cfg");
  preferences.end();
}

void setup() {
  Serial.begin(115200);
  WiFiConfig config = {"MioSSID", "MiaPassword"};
  salvaWiFiConfig(config);
  WiFiConfig letto;
  if (leggiWiFiConfig(letto)) {
    Serial.print("SSID letto: ");
    Serial.println(letto.ssid);
    Serial.print("Password letta: ");
    Serial.println(letto.password);
  }
}
void loop() {}
```
**Cosa fa:**
- Salva una struct con SSID e password
- Legge la configurazione salvata e la stampa su Serial
- Funzione per cancellare la configurazione

---

## 4. Cancellare Dati
### Cancellare una singola chiave
```cpp
preferences.begin("mioSpazio", false);
preferences.remove("avvii");
preferences.end();
```
### Cancellare tutto il namespace
```cpp
preferences.begin("mioSpazio", false);
preferences.clear();
preferences.end();
```

---

## 5. Reset Totale della NVS (Tutti i Namespace)
Per cancellare tutta la memoria NVS (tutti i namespace e chiavi):
```cpp
#include <Preferences.h>
#include "nvs_flash.h"
#include "esp_system.h"

void setup() {
  Serial.begin(115200);
  nvs_flash_erase(); // Cancella tutta la NVS
  nvs_flash_init();  // Re-inizializza
}
void loop() {}
```
**Nota:** Usare solo se serve un reset totale (es. factory reset).

---

## 6. Reset NVS tramite Pulsante (Sicurezza)
```cpp
#include <Preferences.h>
#include "nvs_flash.h"
#include "esp_system.h"
#define RESET_PIN 0

void setup() {
  Serial.begin(115200);
  pinMode(RESET_PIN, INPUT_PULLUP);
  delay(1000);
  if (digitalRead(RESET_PIN) == LOW) {
    nvs_flash_erase();
    nvs_flash_init();
    ESP.restart();
  }
}
void loop() {}
```

---

## 7. Salvare una Struttura (struct) – CRUD Completo
### Definizione struttura
```cpp
struct Anagrafica {
  char nome[32];
  char cognome[32];
  int eta;
};
```
### Funzioni CRUD
```cpp
#include <Preferences.h>
Preferences prefs;

void salvaAnagrafica(const Anagrafica &a) {
  prefs.begin("datiAnag", false);
  prefs.putBytes("anagrafica", &a, sizeof(Anagrafica));
  prefs.end();
}

bool leggiAnagrafica(Anagrafica &a) {
  prefs.begin("datiAnag", true);
  size_t size = prefs.getBytesLength("anagrafica");
  if (size != sizeof(Anagrafica)) { prefs.end(); return false; }
  prefs.getBytes("anagrafica", &a, sizeof(Anagrafica));
  prefs.end();
  return true;
}

void cancellaAnagrafica() {
  prefs.begin("datiAnag", false);
  prefs.remove("anagrafica");
  prefs.end();
}
```
### Esempio d’uso
```cpp
void setup() {
  Serial.begin(115200);
  Anagrafica a1 = {"Mario", "Rossi", 45};
  salvaAnagrafica(a1);
  Anagrafica a2;
  if (leggiAnagrafica(a2)) {
    // stampa dati
  }
  cancellaAnagrafica();
}
void loop() {}
```

---

## 8. Coda Circolare (Circular Queue) di Struct Persistente
### Strategia
- 10 slot: `slot_0` ... `slot_9`
- Indici: `head` (prossima scrittura), `count` (elementi presenti)

### Codice essenziale
```cpp
#define MAX_RECORDS 10
struct Anagrafica { char nome[32]; char cognome[32]; int eta; };
Preferences prefs;

void salvaRecordInCoda(const Anagrafica &a) {
  prefs.begin("anagQueue", false);
  int head = prefs.getInt("head", 0);
  int count = prefs.getInt("count", 0);
  char key[16]; sprintf(key, "slot_%02d", head);
  prefs.putBytes(key, &a, sizeof(Anagrafica));
  head = (head + 1) % MAX_RECORDS;
  if (count < MAX_RECORDS) count++;
  prefs.putInt("head", head);
  prefs.putInt("count", count);
  prefs.end();
}

bool leggiRecord(int index, Anagrafica &a) {
  prefs.begin("anagQueue", true);
  int head = prefs.getInt("head", 0);
  int count = prefs.getInt("count", 0);
  if (index >= count) { prefs.end(); return false; }
  int pos = (head - count + index + MAX_RECORDS) % MAX_RECORDS;
  char key[16]; sprintf(key, "slot_%02d", pos);
  if (prefs.getBytesLength(key) != sizeof(Anagrafica)) { prefs.end(); return false; }
  prefs.getBytes(key, &a, sizeof(Anagrafica));
  prefs.end();
  return true;
}
```

---

## 9. Uso Avanzato: Queue FreeRTOS + Preferences
### Vantaggi
- Gestione RAM veloce (queue)
- Backup persistente su NVS

### Codice essenziale
```cpp
#include <Preferences.h>
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#define MAX_RECORDS 10
struct Anagrafica { char nome[32]; char cognome[32]; int eta; };
QueueHandle_t anagraficaQueue;
Preferences prefs;

void salvaCodaSuNVS() {
  prefs.begin("anagMem", false);
  int count = uxQueueMessagesWaiting(anagraficaQueue);
  prefs.putInt("count", count);
  Anagrafica temp;
  for (int i = 0; i < count; i++) {
    xQueuePeek(anagraficaQueue, &temp, 0);
    char key[16]; sprintf(key, "slot_%02d", i);
    prefs.putBytes(key, &temp, sizeof(Anagrafica));
    xQueueReceive(anagraficaQueue, &temp, 0);
    xQueueSend(anagraficaQueue, &temp, 0);
  }
  prefs.end();
}

void caricaCodaDaNVS() {
  prefs.begin("anagMem", true);
  int count = prefs.getInt("count", 0);
  for (int i = 0; i < count; i++) {
    char key[16]; sprintf(key, "slot_%02d", i);
    Anagrafica a;
    if (prefs.getBytesLength(key) == sizeof(Anagrafica)) {
      prefs.getBytes(key, &a, sizeof(Anagrafica));
      xQueueSend(anagraficaQueue, &a, 0);
    }
  }
  prefs.end();
}
```

---

## 10. Best Practice e Note  
- **Chiudere sempre** Preferences con `.end()` dopo l’uso.
- **Namespace separati** per gruppi di dati diversi.
- **Gestire errori**: controllare sempre la lunghezza dei dati letti.
- **Non abusare**: NVS ha un numero limitato di cicli di scrittura.
- **Per strutture complesse**: serializzare/deserializzare (binario, JSON, base64).
- **Per multi-utente**: usare chiavi dinamiche (es. `user_01`, `user_02`...)

---

## 11. Esercizi Proposti
1. Implementare una lista di log eventi (max 5 eventi)
2. Realizzare un reset selettivo di un solo gruppo di dati
3. Espandere la struct con timestamp e flag di validità

---

## 12. Risorse Utili
- [Documentazione ufficiale Preferences](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/preferences.html)
- [ESP-IDF NVS API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/storage/nvs_flash.html)
- [Esempi Arduino ESP32](https://github.com/espressif/arduino-esp32/tree/master/libraries/Preferences/examples)

---
