### Installare Mosquitto MQTT broker in locale su Windows 


### 1. Scaricare Mosquitto 


- Vai al sito ufficiale: [https://mosquitto.org/download]()
 
- Nella sezione Windows, scarica l’installer `.exe` (es: `mosquitto-2.x.x-install-windows-x64.exe`)


### 2. Installare Mosquitto 


- Esegui l’installer come amministratore
 
- Durante l’installazione:


  - Seleziona l’opzione per installare anche il servizio
 
  - Consenti l’installazione dei componenti opzionali come OpenSSL se richiesto


### 3. Configurare il file di configurazione 


- Il file `mosquitto.conf` si trova nella directory di installazione, ad esempio:


```makefile
C:\Program Files\mosquitto\mosquitto.conf
```
 
- Per iniziare, puoi usare una configurazione minima. Crea un file di testo con:


```yaml
listener 1883
allow_anonymous true
```

Salvalo come `mosquitto.conf` e posizionalo nella stessa directory dell’eseguibile se vuoi avviarlo manualmente.

---

# Esempi di configurazione Mosquitto

## Configurazione semplice (senza autenticazione)

Crea un file `mosquitto.conf` con il seguente contenuto:

```conf
listener 1883
allow_anonymous true
```

---

## Configurazione completa (con autenticazione)

1. Crea un file `mosquitto.conf` con il seguente contenuto:

```conf
listener 1883
allow_anonymous false
password_file C:/Program Files/mosquitto/passwd.txt
```

2. Genera il file delle password:

Apri il prompt dei comandi nella cartella di Mosquitto e digita:

```bash
mosquitto_passwd -c "C:/Program Files/mosquitto/passwd.txt" nomeutente
```

Sostituisci `nomeutente` con il nome utente desiderato. Ti verrà chiesta la password.

3. Avvia Mosquitto normalmente.

---

Per connetterti ora sarà necessario specificare username e password nei client MQTT.

---

## Aprire la porta 1883 nel firewall di Windows

Per permettere le connessioni al broker Mosquitto, è necessario aprire la porta 1883 (TCP) nel firewall di Windows sia in ingresso (IN) che in uscita (OUT). Puoi usare una sola regola con lo stesso nome per entrambe le direzioni.

### Script batch (cmd)

Esegui come amministratore:

```bat
netsh advfirewall firewall add rule name="MQTT Broker 1883" dir=in action=allow protocol=TCP localport=1883
netsh advfirewall firewall add rule name="MQTT Broker 1883" dir=out action=allow protocol=TCP localport=1883
```

### Script PowerShell

Esegui come amministratore:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

```powershell
New-NetFirewallRule -DisplayName "MQTT Broker 1883" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 1883
New-NetFirewallRule -DisplayName "MQTT Broker 1883" -Direction Outbound -Action Allow -Protocol TCP -LocalPort 1883
```

---

### 4. Avviare Mosquitto 


#### Come servizio (se installato come tale): 


- Premi `Win + R`, digita `services.msc`
 
- Cerca “Mosquitto Broker” e avvialo


#### Manualmente da terminale: 


- Apri il prompt dei comandi
 
- Naviga nella cartella di installazione:


```bash
cd "C:\Program Files\mosquitto"
```
 
- Avvia il broker:


```r
mosquitto -v -c mosquitto.conf
```


### 5. Test locale 


- Apri un nuovo prompt dei comandi
 
- Pubblica un messaggio:


```bash
mosquitto_pub -t test/topic -m "ciao"
```
 
- In un altro terminale, sottoscrivi:


```bash
mosquitto_sub -t test/topic
```

---

## Gestione della history e persistenza dei messaggi nel broker MQTT

### Retained message
- Ogni topic può avere solo un messaggio "retained" (conservato) alla volta. Non esiste una vera "history" multipla per topic, ma solo l’ultimo messaggio marcato come retained viene mantenuto e inviato ai nuovi client che si connettono.

### Persistenza dei messaggi
- Mosquitto può essere configurato per salvare i messaggi QoS 1/2 non ancora consegnati ai client offline (persistent session).
- La dimensione massima della persistenza dipende dallo spazio disco e dai parametri di configurazione.

### Parametri di configurazione principali in `mosquitto.conf`

```
persistence true
persistence_location C:/Program Files/mosquitto/data/
max_queued_messages 1000
max_queued_bytes 10485760
message_size_limit 1048576
```

- `persistence true/false`: abilita la persistenza su disco.
- `persistence_location`: cartella dove vengono salvati i dati.
- `max_queued_messages`: massimo numero di messaggi in coda per client offline (default: 100).
- `max_queued_bytes`: massimo numero di byte in coda per client offline.
- `message_size_limit`: dimensione massima di un singolo messaggio.

> **Nota:** Mosquitto non mantiene una vera “history” per topic, ma puoi configurare la coda per client offline e la persistenza dei messaggi. La dimensione massima dipende dai parametri sopra e dallo spazio disco.

---

## Salvare e visualizzare i dati MQTT in Excel

Per visualizzare i dati ricevuti dal broker MQTT in Excel, puoi usare lo script Python `mqtt_to_csv.py` che salva i messaggi in un file CSV.

### 1. Requisiti
- Python 3 installato
- Modulo paho-mqtt: installa con `pip install paho-mqtt`

### 2. Configura lo script
Modifica le variabili BROKER, PORT e TOPIC all'inizio dello script secondo la tua configurazione.

### 3. Avvia lo script
Apri un terminale nella cartella dello script e lancia:

```
python mqtt_to_csv.py
```

I messaggi ricevuti saranno salvati in `mqtt_data.csv` nella stessa cartella.

### 4. Importa in Excel
- Apri Excel
- Vai su Dati > Da testo/CSV
- Seleziona `mqtt_data.csv`
- Segui la procedura guidata per importare i dati

In questo modo puoi visualizzare e aggiornare facilmente i dati MQTT in Excel.

---

### Esempio di codice Python per salvare dati MQTT in CSV

```python
import paho.mqtt.client as mqtt
import csv
from datetime import datetime

BROKER = 'localhost'  # Cambia con l'indirizzo del tuo broker
PORT = 1883
TOPIC = 'test/topic'  # Cambia con il tuo topic
CSV_FILE = 'mqtt_data.csv'

# Callback quando si riceve un messaggio
def on_message(client, userdata, msg):
    data = [datetime.now().isoformat(), msg.topic, msg.payload.decode()]
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print(f"Salvato: {data}")

# Scrivi intestazione se il file non esiste
try:
    with open(CSV_FILE, 'x', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'topic', 'payload'])
except FileExistsError:
    pass

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
print(f"In ascolto su {TOPIC}... (Ctrl+C per uscire)")
client.loop_forever()
```

---

## Esempi di comando per inviare e leggere una temperatura randomica

### Inviare una temperatura randomica realistica (18°C - 28°C) al broker (PowerShell)

Se `mosquitto_pub` non è nel PATH, usa il percorso completo (tutto su una riga):

```powershell
powershell -Command "$temp = Get-Random -Minimum 18 -Maximum 28; & 'C:\Program Files\mosquitto\mosquitto_pub.exe' -h localhost -t sensori/temperatura -m $temp"
```

Oppure, se sei già in PowerShell:

```powershell
$temp = Get-Random -Minimum 18 -Maximum 28
& 'C:\Program Files\mosquitto\mosquitto_pub.exe' -h localhost -t sensori/temperatura -m $temp
```

```powershell
$temp = 22.0  # Valore iniziale realistico
while ($true) {
    $delta = (Get-Random -Minimum -0.3 -Maximum 0.3)
    $temp += $delta
    if ($temp -lt 18) { $temp = 18 }
    if ($temp -gt 28) { $temp = 28 }
    $temp_rounded = [math]::Round($temp, 1)
    & 'C:\Program Files\mosquitto\mosquitto_pub.exe' -h localhost -t sensori/temperatura -m $temp_rounded
    Write-Host "Inviata temperatura: $temp_rounded°C"
    Start-Sleep -Seconds 1
}
```



### Leggere la temperatura dal broker a linea di comando

Esegui nel prompt dei comandi:

```bash
mosquitto_sub -h localhost -t sensori/temperatura
```

---

## Esempio di programma INO per ESP32 (Arduino IDE 2 / IDF 5.4)

Questo sketch connette l'ESP32 a una rete WiFi, si collega a un broker MQTT, si sottoscrive a un topic e invia una temperatura simulata ogni secondo.

### Librerie richieste
- WiFi.h
- PubSubClient.h

### Codice di esempio

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "TUO_SSID";
const char* password = "TUA_PASSWORD";
const char* mqtt_server = "192.168.1.100"; // IP del broker MQTT
const int mqtt_port = 1883;
const char* topic_pub = "sensori/temperatura";
const char* topic_sub = "sensori/temperatura";

WiFiClient espClient;
PubSubClient client(espClient);

float temp = 22.0; // Valore iniziale realistico

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Messaggio ricevuto su topic: ");
  Serial.println(topic);
  Serial.print("Payload: ");
  for (unsigned int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connessione a MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("connesso");
      client.subscribe(topic_sub);
    } else {
      Serial.print("fallito, rc=");
      Serial.print(client.state());
      Serial.println(" riprovo tra 5 secondi");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(100);
  WiFi.begin(ssid, password);
  Serial.print("Connessione a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connesso!");
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Simula temperatura realistica
  temp += random(-3, 4) * 0.1; // Variazione tra -0.3 e +0.3
  if (temp < 18.0) temp = 18.0;
  if (temp > 28.0) temp = 28.0;

  char tempStr[8];
  dtostrf(temp, 4, 1, tempStr);
  client.publish(topic_pub, tempStr);
  Serial.print("Temperatura inviata: ");
  Serial.println(tempStr);
  delay(1000);
}
```

### Istruzioni
1. Sostituisci `TUO_SSID` e `TUA_PASSWORD` con i dati della tua rete WiFi.
2. Imposta l'indirizzo IP del broker MQTT (`mqtt_server`).
3. Carica lo sketch su ESP32 tramite Arduino IDE 2 o IDF 5.4.
4. Apri il monitor seriale per vedere i messaggi inviati e ricevuti.




Per raccogliere, estrarre e memorizzare i valori dei sensori da un broker MQTT per analisi successive, puoi seguire una delle seguenti architetture, a seconda delle tue esigenze e risorse disponibili.



---



## 1. Architettura Base: Python + SQLite 

**Ideale per piccoli progetti o prototipi locali.** 

### Componenti: 

 
- **Broker MQTT** : ad esempio Mosquitto.
 
- **Client MQTT** : utilizzando `paho-mqtt` in Python.
 
- **Database** : SQLite.[ioscape.io
+4
Test and Measurement Solutions
+4
AWS Documentation
+4](https://dewesoft.com/it/prodotti/historian?utm_source=chatgpt.com) [Reddit](https://www.reddit.com/r/flask/comments/fmmu00/write_sensor_data_to_db_using_mqtt_flask/?utm_source=chatgpt.com) [Reddit
+9
Arduino Docs
+9
Steve's Internet Guide
+9](https://docs.arduino.cc/tutorials/portenta-x8/datalogging-iot?utm_source=chatgpt.com)


### Passaggi: 

 
2. **Installazione delle librerie necessarie** :


```bash
pip install paho-mqtt sqlite3
```
 
4. **Script Python per sottoscrizione e salvataggio dati** :


```python
import sqlite3
import json
from paho.mqtt.client import Client

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    conn = sqlite3.connect("sensori.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO misurazioni (temperatura, umidita, timestamp) VALUES (?, ?, ?)",
                   (data["temperatura"], data["umidita"], data["timestamp"]))
    conn.commit()
    conn.close()

client = Client()
client.connect("localhost", 1883)
client.subscribe("sensori/dati")
client.on_message = on_message
client.loop_forever()
```
 
6. **Creazione del database SQLite** :


```sql
CREATE TABLE misurazioni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL,
    umidita REAL,
    timestamp TEXT
);
```

Questo approccio è semplice e funziona bene per progetti di piccole dimensioni. Per maggiori dettagli, puoi consultare la guida di EMQX su come memorizzare dati MQTT in SQLite. [www.emqx.com
+1
www.emqx.com
+1](https://www.emqx.com/en/blog/mqtt-to-sqlite?utm_source=chatgpt.com) 


---



## 2. Architettura Scalabile: Node-RED + InfluxDB + Grafana 

**Adatta per progetti più complessi con esigenze di visualizzazione e analisi avanzate.** 

### Componenti: 

 
- **Broker MQTT** : ad esempio Mosquitto.
 
- **Node-RED** : per l'elaborazione dei dati.
 
- **InfluxDB** : database per serie temporali.
 
- **Grafana** : per la visualizzazione dei dati.[AWS Documentation
+2
Test and Measurement Solutions
+2
Home Assistant Community
+2](https://dewesoft.com/it/prodotti/historian?utm_source=chatgpt.com) [www.emqx.com](https://www.emqx.com/en/blog/database-for-mqtt-data-storage?utm_source=chatgpt.com)


### Passaggi: 

 
2. **Installazione dei componenti** :
 
  - Installa Mosquitto, Node-RED, InfluxDB e Grafana sul tuo sistema.
 
4. **Configurazione di Node-RED** :
 
  - Utilizza un nodo MQTT per sottoscrivere i dati dei sensori.
 
  - Elabora i dati se necessario.
 
  - Utilizza un nodo InfluxDB per salvare i dati nel database.
 
6. **Visualizzazione con Grafana** :
 
  - Configura Grafana per leggere i dati da InfluxDB e crea dashboard personalizzate.[Arduino Docs
+1
Test and Measurement Solutions
+1](https://docs.arduino.cc/tutorials/portenta-x8/datalogging-iot?utm_source=chatgpt.com)

Questo setup è stato utilizzato, ad esempio, in un progetto con Arduino Portenta X8. [Arduino Docs](https://docs.arduino.cc/tutorials/portenta-x8/datalogging-iot?utm_source=chatgpt.com) 


---



## 3. Architettura Cloud: AWS IoT Core + DynamoDB 

**Per progetti che richiedono scalabilità e accesso remoto.** 

### Componenti: 

 
- **AWS IoT Core** : per la gestione dei dispositivi e dei messaggi MQTT.
 
- **AWS Lambda** : per l'elaborazione dei messaggi.
 
- **DynamoDB** : database NoSQL di AWS.[AWS Documentation](https://docs.aws.amazon.com/it_it/iot/latest/developerguide/iot-ddb-rule.html?utm_source=chatgpt.com) [Repost
+3
Medium
+3
www.emqx.com
+3](https://medium.com/%40maheshwar.ramkrushna/step-by-step-guide-inserting-mqtt-data-into-a-database-using-aws-iot-core-and-lambda-ba0ec0d25b3e?utm_source=chatgpt.com)


### Passaggi: 

 
2. **Configurazione di AWS IoT Core** :
 
  - Crea una regola che instradi i messaggi MQTT a una funzione Lambda.
 
4. **Creazione della funzione Lambda** :
 
  - Scrivi una funzione che elabori i messaggi e li salvi in DynamoDB.
 
6. **Configurazione di DynamoDB** :
 
  - Crea una tabella con gli attributi necessari per memorizzare i dati dei sensori.[AWS Documentation](https://docs.aws.amazon.com/it_it/iot/latest/developerguide/iot-ddb-rule.html?utm_source=chatgpt.com)

Per un esempio dettagliato, puoi consultare la guida su come inserire dati MQTT in un database utilizzando AWS IoT Core e Lambda. [Medium](https://medium.com/%40maheshwar.ramkrushna/step-by-step-guide-inserting-mqtt-data-into-a-database-using-aws-iot-core-and-lambda-ba0ec0d25b3e?utm_source=chatgpt.com) 


---



## Considerazioni Finali 

 
- **Formato dei dati** : È consigliabile utilizzare JSON per il payload dei messaggi MQTT, includendo sempre un timestamp.
 
- **Sicurezza** : Utilizza connessioni TLS/SSL e autenticazione per proteggere i dati.
 
- **Backup** : Implementa strategie di backup regolari per il tuo database.[www.emqx.com
+2
AWS Documentation
+2
Medium
+2](https://docs.aws.amazon.com/it_it/iot/latest/developerguide/iot-ddb-rule.html?utm_source=chatgpt.com)

 