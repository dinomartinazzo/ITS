#include <WiFi.h>
#include <esp_wifi.h>
#include <esp_wifi_types.h>

const char* ssid = "Mate10";
const char* password = "3661461500";

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