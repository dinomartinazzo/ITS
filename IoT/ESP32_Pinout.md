# ESP32 - Mappa dei Pin e Considerazioni

## Mappa dei Pin Generale

### Pin Speciali e Limitazioni
- **GPIO 0**: Pin di Boot
  - Usato per il flashing
  - Pull-up interno
  - Evitare uso come input
  
- **GPIO 1 e GPIO 3**: Pin UART0
  - Usati per comunicazione seriale/programmazione
  - Evitare uso in progetti finali

- **GPIO 6-11**: 
  - Collegati alla flash SPI
  - Non disponibili per uso generale

- **GPIO 34-39**: 
  - Solo input
  - No pull-up/pull-down interno
  - Non supportano PWM

### Pin ADC
- **ADC1**: GPIO 32-39
  - Utilizzabili in modalità deep-sleep
  - 12-bit risoluzione

- **ADC2**: GPIO 0, 2, 4, 12-15, 25-27
  - Non utilizzabili con WiFi attivo
  - 12-bit risoluzione

### Pin Touch
- **Touch0**: GPIO 4
- **Touch1**: GPIO 0
- **Touch2**: GPIO 2
- **Touch3**: GPIO 15
- **Touch4**: GPIO 13
- **Touch5**: GPIO 12
- **Touch6**: GPIO 14
- **Touch7**: GPIO 27
- **Touch8**: GPIO 33
- **Touch9**: GPIO 32

## Problematiche di Overlapping

### Conflitti Comuni
1. **WiFi e ADC2**
   - ADC2 non utilizzabile quando WiFi è attivo
   - Usare ADC1 per misurazioni continue

2. **Flash e GPIO 6-11**
   - Pin riservati per memoria flash
   - Non utilizzabili per altri scopi

3. **Strapping Pins**
   - GPIO 0, 2, 5, 12, 15
   - Stati durante il boot influenzano il comportamento
   - Evitare collegamenti esterni che potrebbero interferire

### Pin Consigliati per Uso Generale
- **Input/Output Digitale**: GPIO 13, 14, 16-18, 21, 22, 23, 25, 26, 27, 32, 33
- **Input Analogico**: GPIO 32-39 (ADC1)
- **Output PWM**: GPIO 13, 14, 16-18, 21, 22, 23, 25, 26, 27
- **Comunicazione I2C**: 
  - SDA: GPIO 21
  - SCL: GPIO 22

## Best Practices
1. **Boot Mode**
   - Mantenere GPIO 0 libero per programmazione
   - Non collegare carichi capacitivi sui pin di strapping

2. **Analog Input**
   - Preferire ADC1 per progetti con WiFi
   - Usare divisori di tensione per input >3.3V

3. **Interrupt**
   - Evitare interrupt su pin di strapping
   - Usare pin dedicati per interrupt critici

4. **Pull-up/Pull-down**
   - Ricordare che GPIO 34-39 non hanno resistenze interne
   - Aggiungere resistenze esterne quando necessario

## Schema Riassuntivo Collegamenti Sicuri

### Sensori Analogici
- Temperatura: GPIO 32, 33, 34, 35
- Umidità: GPIO 36, 37, 38, 39

### Comunicazione
- UART0 (DEBUG): GPIO 1 (TX), GPIO 3 (RX)
- UART1: GPIO 16 (RX), GPIO 17 (TX)
- UART2: GPIO 14 (RX), GPIO 27 (TX)
- I2C: GPIO 21 (SDA), GPIO 22 (SCL)
- SPI: 
  - MOSI: GPIO 23
  - MISO: GPIO 19
  - CLK: GPIO 18
  - CS: GPIO 5

### Output Digitali
- LED: GPIO 13, 14, 16-18, 21-23, 25-27
- Relè: GPIO 13, 14, 16-18, 21-23, 25-27
