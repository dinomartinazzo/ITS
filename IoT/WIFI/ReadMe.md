# Guida alle Funzionalità WiFi dell'ESP32

## Modalità WiFi Disponibili
L'ESP32 può operare in tre modalità WiFi principali:

1. **Modalità Station (STA)**
   - ESP32 si connette a una rete WiFi esistente
   - Funziona come client
   - La più comune per progetti IoT
   - Supporta reti WPA/WPA2

2. **Modalità Access Point (AP)**
   - ESP32 crea la propria rete WiFi
   - Altri dispositivi possono connettersi
   - Gestisce fino a 5 connessioni simultanee
   - Utile per portali di configurazione

3. **Modalità Station + Access Point (STA+AP)**
   - Combinazione di entrambe le modalità
   - Può connettersi a una rete mentre ne ospita una propria

## Caratteristiche WiFi Principali

### Funzionalità Modalità Station
- Riconnessione automatica
- Configurazione IP statico
- Supporto DNS
- Supporto WPS
- Supporto Smart Config
- Supporto WPA2 Enterprise

### Funzionalità Access Point
- SSID e password configurabili
- Selezione del canale
- Opzione rete nascosta
- Modalità di autenticazione:
  - OPEN
  - WPA-PSK
  - WPA2-PSK
  - WPA/WPA2-PSK

### Protocolli di Rete Supportati
- Stack TCP/IP integrato
- Capacità server HTTP/HTTPS
- Supporto WebSocket
- Supporto mDNS
- Capacità client MQTT
- Aggiornamenti OTA (Over The Air)

## Casi d'Uso Comuni

1. **Applicazioni Web Server**
   - Pagine di configurazione
   - Dashboard visualizzazione dati
   - Interfacce di controllo remoto

2. **Raccolta Dati IoT**
   - Invio dati sensori al cloud
   - Logging su server remoti
   - Pubblicazione/sottoscrizione MQTT

3. **Bridge di Rete**
   - Funzionamento come ripetitore WiFi
   - Gateway di traduzione protocolli
   - Nodo rete mesh

4. **Portale di Configurazione**
   - Setup iniziale dispositivo
   - Gestione credenziali di rete
   - Configurazione parametri dispositivo

## Librerie Principali
- `WiFi.h` - Funzionalità WiFi core
- `WebServer.h` - Capacità server HTTP
- `ESPAsyncWebServer` - Server web asincrono
- `WiFiManager` - Portale di configurazione
- `HTTPClient.h` - Operazioni client HTTP
- `AsyncMqttClient` - Comunicazioni MQTT

## Considerazioni Energetiche
- Modalità consumo WiFi:
  - WIFI_POWER_19_5dBm
  - WIFI_POWER_19dBm
  - WIFI_POWER_18_5dBm
  - WIFI_POWER_17dBm
  - WIFI_POWER_15dBm
  - WIFI_POWER_13dBm
  - WIFI_POWER_11dBm
  - WIFI_POWER_8_5dBm
  - WIFI_POWER_7dBm
  - WIFI_POWER_5dBm
  - WIFI_POWER_2dBm
  - WIFI_POWER_MINUS_1dBm

## Strumenti di Debug
- Output monitor seriale
- Monitoraggio potenza segnale WiFi
- Funzionalità scanner di rete
- Eventi stato connessione

## Esempi di Codice
Tutti gli esempi sono disponibili nella cartella `/Examples`:
