# Esempio 1c: Informazioni Complete di Rete

```cpp
#include <WiFi.h>
#include <esp_wifi.h>
#include <esp_wifi_types.h>

const char* ssid = "TuaReteWiFi";
const char* password = "TuaPassword";

void printNetworkInfo() {
  Serial.println("\n=== Informazioni di Rete ===");
  
  // Info WiFi
  Serial.println("\nInfo WiFi:");
  Serial.printf("SSID: %s\n", WiFi.SSID().c_str());
  Serial.printf("Potenza segnale: %d dBm\n", WiFi.RSSI());
  Serial.printf("MAC Address: %s\n", WiFi.macAddress().c_str());
  Serial.printf("Modalità WiFi: %s\n", 
    WiFi.getMode() == WIFI_MODE_STA ? "Station" :
    WiFi.getMode() == WIFI_MODE_AP ? "Access Point" :
    WiFi.getMode() == WIFI_MODE_APSTA ? "AP+Station" : "Unknown"
  );

  // Info Rete
  Serial.println("\nInfo Rete:");
  Serial.printf("Indirizzo IP: %s\n", WiFi.localIP().toString().c_str());
  Serial.printf("Subnet Mask: %s\n", WiFi.subnetMask().toString().c_str());
  Serial.printf("Gateway: %s\n", WiFi.gatewayIP().toString().c_str());
  Serial.printf("Broadcast: %s\n", WiFi.broadcastIP().toString().c_str());
  
  // Info DNS
  Serial.println("\nServer DNS:");
  for(int i=0; i<2; i++) {
    IPAddress dns = WiFi.dnsIP(i);
    if(dns != INADDR_NONE) {
      Serial.printf("DNS %d: %s\n", i+1, dns.toString().c_str());
    }
  }

  // Info Connessione
  Serial.println("\nStato Connessione:");
  Serial.printf("Canale: %d\n", WiFi.channel());
  Serial.printf("TX Power: %d\n", WiFi.getTxPower());
  Serial.printf("Auto Connect: %s\n", WiFi.getAutoReconnect() ? "Si" : "No");
  Serial.printf("Sleep Mode: %s\n", 
    WiFi.getSleep() ? "Modem Sleep" : "No Sleep"
  );

  // Statistiche
  Serial.println("\nStatistiche:");
  Serial.printf("Uptime: %lu s\n", millis()/1000);
  Serial.printf("WiFi Status: %d\n", WiFi.status());
  Serial.printf("Actual TX Power: %d\n", WiFi.getTxPower());
  Serial.printf("Connection Quality: %d%%\n", 
    constrain(map(WiFi.RSSI(), -100, -50, 0, 100), 0, 100));
}

void printExtendedNetworkInfo() {
  printNetworkInfo();
  
  // Aggiungo informazioni extra
  Serial.println("\nInfo Avanzate:");
  Serial.printf("BSSID: %s\n", WiFi.BSSIDstr().c_str());
  Serial.printf("Hostname: %s\n", WiFi.getHostname());
  
  // Info sicurezza
  Serial.println("\nSicurezza:");
  wifi_ap_record_t wifidata;
  if(esp_wifi_sta_get_ap_info(&wifidata) == ESP_OK) {
    Serial.printf("Tipo Autenticazione: %s\n", 
      wifidata.authmode == WIFI_AUTH_OPEN ? "Open" :
      wifidata.authmode == WIFI_AUTH_WEP ? "WEP" :
      wifidata.authmode == WIFI_AUTH_WPA_PSK ? "WPA PSK" :
      wifidata.authmode == WIFI_AUTH_WPA2_PSK ? "WPA2 PSK" :
      wifidata.authmode == WIFI_AUTH_WPA_WPA2_PSK ? "WPA/WPA2 PSK" :
      "Unknown"
    );
  }

  // Performance
  Serial.println("\nPerformance:");
  wifi_ap_record_t wifidata_perf;
  if(esp_wifi_sta_get_ap_info(&wifidata_perf) == ESP_OK) {
    // Estimate max PHY speed based on capabilities
    int speed;
    if(wifidata_perf.phy_11n) {
      speed = 72; // Basic 802.11n speed
    } else if(wifidata_perf.phy_11g) {
      speed = 54; // 802.11g
    } else {
      speed = 11; // 802.11b
    }
    
    Serial.printf("Velocità PHY: %d Mbps\n", speed);
    Serial.printf("Potenza AP: %d dBm\n", wifidata_perf.rssi);
    Serial.printf("Qualità segnale: %d%%\n", 
      constrain(map(WiFi.RSSI(), -100, -50, 0, 100), 0, 100));
  }
}

void setup() {
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  Serial.print("Connessione");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnesso!");
  
  printExtendedNetworkInfo();
}

void loop() {
  if(WiFi.status() == WL_CONNECTED) {
    static unsigned long lastCheck = 0;
    if(millis() - lastCheck > 10000) {  // Ogni 10 secondi
      printExtendedNetworkInfo();
      lastCheck = millis();
    }
  }
  delay(100);
}
```

Output di esempio:
```
=== Informazioni di Rete ===

Info WiFi:
SSID: TuaReteWiFi
Potenza segnale: -65 dBm
MAC Address: A4:CF:12:DF:6E:9C
Modalità WiFi: Station

Info Rete:
Indirizzo IP: 192.168.1.100
Subnet Mask: 255.255.255.0
Gateway: 192.168.1.1
Broadcast: 192.168.1.255

Server DNS:
DNS 1: 8.8.8.8
DNS 2: 8.8.4.4

Stato Connessione:
Canale: 6
TX Power: 78
Auto Connect: Si
Sleep Mode: Modem Sleep

Statistiche:
Uptime: 1234 s
WiFi Status: 3
Actual TX Power: 78
Connection Quality: 85%

Info Avanzate:
BSSID: A4:CF:12:DF:6E:9C
Hostname: esp32-device

Sicurezza:
Tipo Autenticazione: WPA2 PSK

Performance:
Velocità PHY: 72 Mbps
Potenza AP: -65 dBm
Qualità segnale: 85%
```

## Note sui Codici di Stato WiFi

Il campo `WiFi Status` nelle statistiche mostra lo stato corrente della connessione WiFi. I possibili valori sono:

- `WL_IDLE_STATUS (0)`: Stato temporaneo durante il cambio di modalità
- `WL_NO_SSID_AVAIL (1)`: SSID configurato non trovato
- `WL_SCAN_COMPLETED (2)`: Scansione delle reti WiFi completata
- `WL_CONNECTED (3)`: Connesso con successo alla rete WiFi
- `WL_CONNECT_FAILED (4)`: Connessione fallita (es. password errata)
- `WL_CONNECTION_LOST (5)`: Connessione persa
- `WL_DISCONNECTED (6)`: Disconnesso dalla rete

Nell'esempio sopra, il valore `3` indica che il dispositivo è correttamente connesso alla rete WiFi specificata.

## Note sulle Metriche di Performance

La sezione Performance mostra le caratteristiche tecniche della connessione WiFi:

- `Velocità PHY`: Indica la velocità massima teorica del collegamento fisico:
  - 11 Mbps: Standard 802.11b
  - 54 Mbps: Standard 802.11g
  - 72 Mbps: Standard base 802.11n (può arrivare a 150 Mbps con canale da 40MHz)

- `Potenza AP`: Potenza del segnale ricevuto dall'Access Point in dBm:
  - Eccellente: > -50 dBm
  - Buono: -50 a -60 dBm
  - Medio: -60 a -70 dBm
  - Debole: < -70 dBm

- `Qualità segnale`: Percentuale calcolata dalla potenza del segnale:
  - 100%: Segnale ottimo (-50 dBm o migliore)
  - 85%: Segnale buono (circa -65 dBm)
  - 50%: Segnale medio (circa -75 dBm)
  - 0%: Segnale minimo (-100 dBm o peggiore)
