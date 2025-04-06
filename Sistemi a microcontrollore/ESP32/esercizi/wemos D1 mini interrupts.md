https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/

https://arduino-esp8266.readthedocs.io/en/latest/reference.html?highlight=attachinterrupt#digital-io

``` js
#define INTERRUPT_PIN D7 

 
void ICACHE_RAM_ATTR   dmpDataReady() { 
    mpuInterrupt = true;
}


digitalPinToInterrupt(INTERRUPT_PIN);
attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), dmpDataReady, RISING);



float deltat;
float told;
float spacex;
float spacey;
float spacez;

    float accx = aaReal.x;
    float accy = aaReal.y;
    float accz = aaReal.z;
    if (accx < 0)
    {
      accx = 0;
    }
    if (accx > 15)
    {
      spacex += ( 0.5 * accx * (millis() - told)) / 1000;
    }

    if (accy < 0)
    {
      accy = 0;
    }
    if (accy > 15)
    {
      spacey += ( 0.5 * accy * (millis() - told)) / 1000;
    }

    if (accz < 0)
    {
      accz = 0;
    }
    if (accz > 15)
    {
      spacez += ( 0.5 * accz * (millis() - told)) / 1000;
    }

    Serial.print((String)(spacex)  + "," + (String)(spacey ) + "," + (String)(spacez ) + "\r\n");


  told = millis();

```