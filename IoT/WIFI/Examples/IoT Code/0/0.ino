#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  
  // Imposta WiFi in modalità station
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  Serial.println("Scanner WiFi Avviato");
}

void loop() {
  Serial.println("\nInizio Scansione Reti...");
  int n = WiFi.scanNetworks();
  
  if (n == 0) {
    Serial.println("Nessuna rete trovata");
  } else {
    Serial.print(n);
    Serial.println(" Reti Trovate");
    
    for (int i = 0; i < n; ++i) {
      // Stampa SSID e RSSI per ogni rete trovata
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print("dBm) ");
      
      // Stampa il tipo di crittografia
      switch(WiFi.encryptionType(i)) {
        case WIFI_AUTH_OPEN:
          Serial.println("[OPEN]");
          break;
        case WIFI_AUTH_WEP:
          Serial.println("[WEP]");
          break;
        case WIFI_AUTH_WPA_PSK:
          Serial.println("[WPA_PSK]");
          break;
        case WIFI_AUTH_WPA2_PSK:
          Serial.println("[WPA2_PSK]");
          break;
        case WIFI_AUTH_WPA_WPA2_PSK:
          Serial.println("[WPA-WPA2_PSK]");
          break;
        default:
          Serial.println("[UNKNOWN]");
      }
      delay(10);
    }
  }
  
  // Attendi 5 secondi prima della prossima scansione
  delay(5000);
}