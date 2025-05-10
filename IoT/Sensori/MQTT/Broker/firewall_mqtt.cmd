@echo off
REM Apre la porta 1883 TCP per Mosquitto MQTT (IN e OUT) con un unico nome
netsh advfirewall firewall add rule name="MQTT Broker 1883" dir=in action=allow protocol=TCP localport=1883
netsh advfirewall firewall add rule name="MQTT Broker 1883" dir=out action=allow protocol=TCP localport=1883
