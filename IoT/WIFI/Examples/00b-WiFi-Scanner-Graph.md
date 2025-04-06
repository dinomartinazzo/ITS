# Esempio 0b: Scanner WiFi con Grafico ASCII

```cpp
#include <WiFi.h>

// Funzione per convertire RSSI in barre ASCII
String signalToGraph(int32_t rssi) {
  String graph = "[";
  // RSSI tipicamente va da -100dBm (debole) a -30dBm (forte)
  int bars = map(rssi, -100, -30, 0, 10);
  bars = constrain(bars, 0, 10);
  
  for(int i = 0; i < 10; i++) {
    if(i < bars) {
      graph += "=";
    } else {
      graph += " ";
    }
  }
  graph += "]";
  return graph;
}

void setup() {
  Serial.begin(115200);
  
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("Scanner WiFi Grafico Avviato");
}

void loop() {
  Serial.println("\n\nScansione Reti WiFi...");
  int n = WiFi.scanNetworks();
  
  if (n == 0) {
    Serial.println("Nessuna rete trovata");
  } else {
    // Intestazione
    Serial.println("\nPotenza Segnale (-100dBm → -30dBm)");
    Serial.println("SSID                     Segnale    Grafico");
    Serial.println("------------------------ ---------- --------------------");
    
    for (int i = 0; i < n; ++i) {
      String ssid = WiFi.SSID(i);
      // Padding SSID a 24 caratteri
      ssid.reserve(24);
      while(ssid.length() < 24) ssid += " ";
      
      // Formatta RSSI
      String rssiStr = String(WiFi.RSSI(i));
      rssiStr.reserve(4);
      while(rssiStr.length() < 4) rssiStr = " " + rssiStr;
      
      // Stampa riga
      Serial.print(ssid);
      Serial.print(" ");
      Serial.print(rssiStr);
      Serial.print("dBm ");
      Serial.println(signalToGraph(WiFi.RSSI(i)));
    }
    
    Serial.println("\nLegenda:");
    Serial.println("=== Forte    (> -50dBm)");
    Serial.println("==  Medio    (-70dBm ~ -50dBm)");
    Serial.println("=   Debole   (< -70dBm)");
  }
  
  delay(5000);
}
```

Output di esempio:
```
Scansione Reti WiFi...

Potenza Segnale (-100dBm → -30dBm)
SSID                     Segnale    Grafico
------------------------ ---------- --------------------
MyWiFi                   -45dBm    [========  ]
Vodafone-WiFi            -67dBm    [=====    ]
AndroidAP                -89dBm    [==       ]
```
