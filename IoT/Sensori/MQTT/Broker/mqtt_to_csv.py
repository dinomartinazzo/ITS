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
