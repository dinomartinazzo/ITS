# Script PowerShell per inviare temperatura randomica al broker MQTT ogni secondo

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