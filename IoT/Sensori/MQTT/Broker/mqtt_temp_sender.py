import paho.mqtt.client as mqtt
import time
import random

BROKER = 'localhost'  # Cambia se necessario
PORT = 1883
TOPIC = 'sensori/temperatura'

temp = 22.0  # Valore iniziale realistico
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

try:
    while True:
        # Variazione lenta e realistica
        temp += random.uniform(-0.3, 0.3)
        temp = max(18.0, min(28.0, temp))
        temp_rounded = round(temp, 1)
        client.publish(TOPIC, temp_rounded)
        print(f"Inviata temperatura: {temp_rounded}°C")
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrotto dall'utente.")
finally:
    client.disconnect()
