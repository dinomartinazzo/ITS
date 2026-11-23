# Verifica della revisione

Dalla cartella principale estratta:

```bash
g++ -std=c++11 -Wall -Wextra -Werror -I tests/stubs tests/test_ads131m04.cpp -o /tmp/test_cella_ads131m04
/tmp/test_cella_ads131m04
```

Il test include il vero `app.cpp` ADS131M04 e sostituisce solo driver hardware, seriale e temporizzazione con stub. Verifica acquisizione normale, blocco su configurazione errata, clock assente, ID inatteso, saturazione positiva/negativa di ogni canale, CRC errato, eccitazione insufficiente, timeout, annullamento delle raccolte al cambio configurazione, recupero e tara.

Non verifica SPI, LEDC, temporizzazioni reali, compatibilità del core ESP32 o comportamento elettrico. Per questa revisione non è stata eseguita la compilazione ESP32: arduino-cli non disponibile nell'ambiente. Il condensatore è stato valutato mediante analisi circuitale, non mediante misure al banco.
