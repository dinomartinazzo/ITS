# Esempio 2D: Access Point Configurabile

Questo esempio mostra come configurare un Access Point ESP32 con impostazioni avanzate:
- Configurazione IP statico
- Selezione del canale WiFi
- Configurazione potenza di trasmissione
- Impostazioni PHY mode
- Interfaccia web per la gestione

```cpp
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include <esp_wifi.h>  // Add this include

// Configurazioni di default
const char* ap_ssid = "ESP32-Config-AP";
const char* ap_password = "123456789";
IPAddress ap_IP(192, 168, 4, 1);
IPAddress ap_gateway(192, 168, 4, 1);
IPAddress ap_subnet(255, 255, 255, 0);
int channel = 1;
wifi_phy_mode_t phyMode = WIFI_PHY_MODE_11G; // Fixed constant
int power = 20; // Range: 2-20 dBm

// Add current PHY mode tracking
uint8_t currentPhyMode = 2; // Default to 11G

// Add channel information structure
struct ChannelInfo {
  int channel;
  int frequency;
  const char* recommendation;
};

const ChannelInfo channelList[] = {
  {1, 2412, "Recommended"},
  {2, 2417, "Overlaps with 1"},
  {3, 2422, "Overlaps with 1,2"},
  {4, 2427, "Overlaps with 1,2,3"},
  {5, 2432, "Overlaps with 2,3,4"},
  {6, 2437, "Recommended"},
  {7, 2442, "Overlaps with 6"},
  {8, 2447, "Overlaps with 6,7"},
  {9, 2452, "Overlaps with 6,7,8"},
  {10, 2457, "Overlaps with 7,8,9"},
  {11, 2462, "Recommended"},
  {12, 2467, "Limited use"},
  {13, 2472, "Limited use"}
};

WebServer server(80);
String lastError = ""; // Add at top with other globals

void printWiFiStatus() {
  Serial.println("\n=== WiFi Status ===");
  Serial.printf("SSID: %s\n", WiFi.softAPSSID().c_str());
  Serial.printf("Channel: %d (%d MHz)\n", WiFi.channel(), 2407 + (WiFi.channel() * 5));
  Serial.printf("TX Power: %d dBm\n", WiFi.getTxPower());
  Serial.printf("IP Address: %s\n", WiFi.softAPIP().toString().c_str());
  Serial.printf("MAC Address: %s\n", WiFi.softAPmacAddress().c_str());
  Serial.printf("Connected devices: %d\n", WiFi.softAPgetStationNum());
  Serial.printf("Approx. range: %d meters\n", calculateRange(WiFi.getTxPower()));
  Serial.println("=================\n");
}

String getHTML() {
  String html = "<!DOCTYPE html><html><head>";
  html += "<title>ESP32 AP Configuration</title>";
  html += "<style>body{font-family:Arial;margin:20px;} ";
  html += ".form-group{margin:10px 0;} ";
  html += "input,select{width:200px;padding:5px;}</style></head>";
  html += "<body><h1>ESP32 AP Configuration</h1>";

  // Add status message at top of form
  if (lastError != "") {
    html += "<div style='background:#ffe6e6;padding:10px;margin:10px 0;border:1px solid #ff9999'>";
    html += lastError + "</div>";
  }

  html += "<form action='/update' method='POST'>";
  
  // IP Configuration
  html += "<div class='form-group'>";
  html += "<label>IP Address: </label>";
  html += "<input type='text' name='ip' value='" + WiFi.softAPIP().toString() + "'>";
  html += "</div>";
  
  // Enhanced Channel Selection
  html += "<div class='form-group'>";
  html += "<label>WiFi Channel (2.4GHz): </label>";
  html += "<style>.channel-info{color:#666;font-size:0.8em;}</style>";
  html += "<select name='channel' style='margin-bottom:5px'>";
  
  for(const auto& ch : channelList) {
    html += "<option value='" + String(ch.channel) + "'";
    html += (WiFi.channel()==ch.channel?" selected":"");
    html += ">" + String(ch.channel) + " (" + String(ch.frequency) + " MHz)";
    if(strcmp(ch.recommendation, "Recommended") == 0) {
      html += " ★";
    }
    html += "</option>";
  }
  html += "</select>";
  html += "<div class='channel-info'>";
  html += "★ Recommended channels: 1, 6, 11 (minimal interference)<br>";
  html += "Current channel: " + String(WiFi.channel()) + " (" + 
          String(2407 + (WiFi.channel() * 5)) + " MHz)";
  html += "</div></div>";
  
  // TX Power
  html += "<div class='form-group'>";
  html += "<label>TX Power (2-20 dBm): </label>";
  html += "<input type='number' name='power' min='2' max='20' value='" + String(WiFi.getTxPower()) + "'>";
  html += "</div>";
  
  // PHY Mode Selection
  html += "<div class='form-group'>";
  html += "<label>PHY Mode: </label>";
  html += "<select name='phymode'>";
  html += "<option value='1'" + String(currentPhyMode==1?" selected":"") + ">11B</option>";
  html += "<option value='2'" + String(currentPhyMode==2?" selected":"") + ">11G</option>";
  html += "<option value='3'" + String(currentPhyMode==3?" selected":"") + ">LR</option>";
  html += "</select></div>";
  
  // Current Status
  html += "<h2>Current Status</h2>";
  html += "<p>Connected Devices: " + String(WiFi.softAPgetStationNum()) + "</p>";
  html += "<p>MAC Address: " + WiFi.softAPmacAddress() + "</p>";
  html += "<p>Signal Range: ~" + String(calculateRange(WiFi.getTxPower())) + " meters</p>";
  
  html += "<input type='submit' value='Update Configuration'>";
  html += "</form></body></html>";
  return html;
}

int calculateRange(int txPower) {
  // Rough estimation of range based on TX power
  // This is a very simplified calculation
  return (txPower * 5); // Approx meters
}

void handleRoot() {
  server.send(200, "text/html", getHTML());
}

void handleUpdate() {
  Serial.println("\n--- Configuration Update Request ---");
  bool needsRestart = false;
  lastError = "";
  String status = "";

  if (server.hasArg("ip")) {
    IPAddress newIP;
    if (newIP.fromString(server.arg("ip"))) {
      Serial.printf("Changing IP to: %s\n", server.arg("ip").c_str());
      if (!WiFi.softAPConfig(newIP, newIP, ap_subnet)) {
        lastError += "Failed to set IP. ";
      } else {
        status += "IP updated. ";
        needsRestart = true;
      }
    }
  }
  
  if (server.hasArg("channel")) {
    int newChannel = server.arg("channel").toInt();
    Serial.printf("Changing channel to: %d\n", newChannel);
    if (newChannel >= 1 && newChannel <= 13) {
      // Store new channel and restart AP
      channel = newChannel;
      WiFi.softAPdisconnect(true);
      delay(500);
      if (WiFi.softAP(ap_ssid, ap_password, channel, 0, 4)) {
        status += "Channel updated. ";
        Serial.println("AP restarted with new channel");
      } else {
        lastError += "Failed to set channel. ";
        Serial.println("Failed to restart AP with new channel");
      }
      needsRestart = true;
    }
  }
  
  if (server.hasArg("power")) {
    int newPower = server.arg("power").toInt();
    Serial.printf("Changing TX power to: %d dBm\n", newPower);
    if (newPower >= 2 && newPower <= 20) {
      if (!WiFi.setTxPower((wifi_power_t)newPower)) {
        lastError += "Failed to set power. ";
      } else {
        status += "Power updated. ";
      }
    }
  }
  
  if (server.hasArg("phymode")) {
    int mode = server.arg("phymode").toInt();
    Serial.printf("Changing PHY mode to: %d\n", mode);
    uint8_t protocol;
    switch(mode) {
      case 1: protocol = WIFI_PROTOCOL_11B; break;
      case 2: protocol = WIFI_PROTOCOL_11B | WIFI_PROTOCOL_11G; break;
      case 3: protocol = WIFI_PROTOCOL_LR; break;
      default: protocol = WIFI_PROTOCOL_11B | WIFI_PROTOCOL_11G;
    }
    
    if (esp_wifi_set_protocol(WIFI_IF_AP, protocol) != ESP_OK) {
      lastError += "Failed to set PHY mode. ";
    } else {
      currentPhyMode = mode;
      status += "PHY mode updated. ";
      needsRestart = true;
    }
  }

  if (lastError == "" && status != "") {
    Serial.println("Update successful!");
    Serial.println(status);
    if (needsRestart) {
      Serial.println("Note: Some changes require reconnecting to AP");
    }
    printWiFiStatus();
    // Send success page with auto-refresh
    String response = "<html><head>";
    response += "<meta http-equiv='refresh' content='3;url=/'>";
    response += "</head><body>";
    response += "<h2>Configuration Updated</h2>";
    response += "<p>" + status + "</p>";
    if (needsRestart) {
      response += "<p>Some changes may require reconnecting to the AP.</p>";
    }
    response += "<p>Returning to main page in 3 seconds...</p>";
    response += "</body></html>";
    server.send(200, "text/html", response);
  } else if (lastError != "") {
    Serial.println("Update failed!");
    Serial.println(lastError);
    // Return to main page with error message
    server.sendHeader("Location", "/");
    server.send(302, "text/plain", "");
  }
  Serial.println("--------------------------------\n");
}

void setup() {
  Serial.begin(115200);
  Serial.println("\nESP32 Access Point Configuration");
  Serial.println("Initializing...");
  
  // Configurazione iniziale AP
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ap_IP, ap_gateway, ap_subnet);
  if (!WiFi.softAP(ap_ssid, ap_password, channel, 0, 4)) {
    Serial.println("Failed to initialize AP!");
  }
  WiFi.setTxPower((wifi_power_t)power);
  
  // Set initial protocol mode
  esp_wifi_set_protocol(WIFI_IF_AP, WIFI_PROTOCOL_11B | WIFI_PROTOCOL_11G);
  currentPhyMode = 2;
  
  server.on("/", handleRoot);
  server.on("/update", HTTP_POST, handleUpdate);
  server.begin();
  
  lastError = ""; // Initialize error string
  
  Serial.println("\nAccess Point Configuration Complete!");
  printWiFiStatus();
  Serial.println("Web interface available at http://" + WiFi.softAPIP().toString());
}

void loop() {
  static unsigned long lastStatusUpdate = 0;
  const unsigned long STATUS_INTERVAL = 30000; // Print status every 30 seconds
  
  server.handleClient();
  
  // Periodic status update
  if (millis() - lastStatusUpdate > STATUS_INTERVAL) {
    printWiFiStatus();
    lastStatusUpdate = millis();
  }
  
  delay(10);
}
```

Questo esempio permette di:
1. Impostare un IP statico per l'Access Point
2. Selezionare il canale WiFi (1-13)
3. Regolare la potenza di trasmissione (2-20 dBm)
4. Selezionare il PHY mode (11B, 11G, LR)
5. Visualizzare il numero di dispositivi connessi
6. Stimare approssimativamente la portata del segnale
7. Configurare i parametri tramite interfaccia web

Per utilizzare:
1. Caricare il codice su ESP32
2. Connettersi alla rete "ESP32-Config-AP" (password: 12345678)
3. Visitare http://192.168.4.1
4. Modificare le impostazioni tramite l'interfaccia web

## Documentazione Configurazioni WiFi ESP32

### Canali WiFi 2.4GHz
| Canale | Frequenza (MHz) | Note |
|--------|----------------|------|
| 1 | 2412 | Raccomandato, non sovrapposto |
| 6 | 2437 | Raccomandato, non sovrapposto |
| 11 | 2462 | Raccomandato, non sovrapposto |
| 2-5 | 2417-2432 | Sovrapposti con canale 1 |
| 7-10 | 2442-2457 | Sovrapposti con canale 6 |
| 12-13 | 2467-2472 | Uso limitato in alcuni paesi |

### Modalità PHY
| Modalità | Descrizione | Velocità Max | Uso Consigliato |
|----------|-------------|--------------|-----------------|
| 11B | Legacy mode | 11 Mbps | Maggiore compatibilità, minore velocità |
| 11G | Extended mode | 54 Mbps | Bilanciamento tra velocità e compatibilità |
| LR | Long Range mode | 1 Mbps | Massima portata, minima velocità |

### Potenza di Trasmissione (TX Power)
| Livello (dBm) | Portata Approx. | Consumo | Note |
|---------------|-----------------|---------|------|
| 2-5 | 10-25m | Molto Basso | Ambienti piccoli, risparmio energetico |
| 6-10 | 30-50m | Basso | Uso domestico tipico |
| 11-15 | 55-75m | Medio | Copertura estesa |
| 16-20 | 80-100m | Alto | Massima copertura, alto consumo |

### Limitazioni e Note Importanti

1. **Selezione Canale**
   - I canali 1, 6, e 11 sono raccomandati per evitare interferenze
   - La sovrapposizione dei canali può causare interferenze
   - Alcuni paesi hanno restrizioni sui canali 12 e 13

2. **Potenza di Trasmissione**
   - Range: 2dBm - 20dBm
   - Maggiore potenza = maggiore consumo energetico
   - La portata effettiva dipende dall'ambiente
   - Ostacoli riducono significativamente la portata

3. **Modalità PHY**
   - 11B: Compatibile con tutti i dispositivi
   - 11G: Miglior compromesso velocità/compatibilità
   - LR (Long Range): 
     * Solo per comunicazioni punto-punto
     * Richiede dispositivi compatibili
     * Velocità molto limitata

4. **Considerazioni per Access Point**
   - Max 4 client simultanei consigliati
   - La banda è condivisa tra tutti i client
   - L'IP di default è 192.168.4.1
   - DHCP assegna IP nel range 192.168.4.2 - 192.168.4.100

### Best Practices

1. **Ottimizzazione Prestazioni**
   - Usare canali non sovrapposti (1, 6, 11)
   - Bilanciare potenza TX in base all'area da coprire
   - Modalità 11G per uso generale
   - Posizionare l'ESP32 in punto elevato e centrale

2. **Risparmio Energetico**
   - Ridurre TX Power al minimo necessario
   - Usare modalità 11B se la velocità non è critica
   - Limitare il numero di client connessi

3. **Sicurezza**
   - Usare password WPA2 di almeno 8 caratteri
   - Cambiare le credenziali di default
   - Monitorare i dispositivi connessi
   - Evitare Access Point aperti

### Troubleshooting

1. **Problemi di Connessione**
   - Verificare la potenza del segnale
   - Controllare interferenze sul canale
   - Testare diverse modalità PHY
   - Verificare la compatibilità dei client

2. **Prestazioni Scarse**
   - Controllare il numero di client connessi
   - Verificare interferenze da altri network
   - Testare canali alternativi
   - Aumentare la potenza TX se necessario
