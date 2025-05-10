# Apre la porta 1883 TCP per Mosquitto MQTT (IN e OUT) con un unico nome
New-NetFirewallRule -DisplayName "MQTT Broker 1883" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 1883
New-NetFirewallRule -DisplayName "MQTT Broker 1883" -Direction Outbound -Action Allow -Protocol TCP -LocalPort 1883
