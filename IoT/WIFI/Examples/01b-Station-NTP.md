# Esempio 1b: WiFi Station con NTP Time

```cpp
#include <WiFi.h>
#include "time.h"

const char* ssid = "TuaReteWiFi";
const char* password = "TuaPassword";

// Server NTP Italia
const char* ntpServer1 = "it.pool.ntp.org";
const char* ntpServer2 = "pool.ntp.org";
const char* timezone = "CET-1CEST,M3.5.0,M10.5.0/3";  // Timezone Italia

void printLocalTime() {
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Errore ricezione tempo");
    return;
  }
  
  Serial.println("\n=== Info Tempo ===");
  Serial.printf("Data: %02d/%02d/%04d\n", 
    timeinfo.tm_mday, 
    timeinfo.tm_mon + 1, 
    1900 + timeinfo.tm_year);
  
  Serial.printf("Ora: %02d:%02d:%02d\n", 
    timeinfo.tm_hour, 
    timeinfo.tm_min, 
    timeinfo.tm_sec);
  
  Serial.printf("Giorno della settimana: %d\n", timeinfo.tm_wday);
  Serial.printf("Giorno dell'anno: %d\n", timeinfo.tm_yday);
  Serial.printf("Settimana dell'anno: %d\n", (timeinfo.tm_yday + 7) / 7);
  
  if(timeinfo.tm_isdst)
    Serial.println("Ora legale attiva");
  else
    Serial.println("Ora solare attiva");
}

void setup() {
  Serial.begin(115200);
  
  // Connessione WiFi
  Serial.printf("Connessione a %s", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" CONNESSO");

  // Configurazione NTP
  configTime(0, 0, ntpServer1, ntpServer2);  // UTC
  setenv("TZ", timezone, 1);                 // Timezone Italia
  tzset();

  Serial.println("Sincronizzazione NTP...");
  delay(2000);
  printLocalTime();
  
  // Info di rete
  Serial.println("\n=== Info Rete ===");
  Serial.print("Indirizzo IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("Subnet Mask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  Serial.print("DNS primario: ");
  Serial.println(WiFi.dnsIP(0));
  Serial.print("DNS secondario: ");
  Serial.println(WiFi.dnsIP(1));
  Serial.print("Indirizzo MAC: ");
  Serial.println(WiFi.macAddress());
}

void loop() {
  printLocalTime();
  delay(5000);
}
```

Output di esempio:
```
=== Info Tempo ===
Data: 15/02/2024
Ora: 14:30:45
Giorno della settimana: 4
Giorno dell'anno: 46
Settimana dell'anno: 7
Ora legale attiva

=== Info Rete ===
Indirizzo IP: 192.168.1.100
Subnet Mask: 255.255.255.0
Gateway: 192.168.1.1
DNS primario: 8.8.8.8
DNS secondario: 8.8.4.4
Indirizzo MAC: A4:CF:12:DF:6E:9C
```
