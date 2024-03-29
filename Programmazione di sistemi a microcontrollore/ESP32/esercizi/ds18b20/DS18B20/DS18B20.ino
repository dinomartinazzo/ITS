//https://randomnerdtutorials.com/esp32-ds18b20-temperature-arduino-ide/

//onewire
//https://www.pjrc.com/teensy/td_libs_OneWire.html

//Dallas
//https://github.com/milesburton/Arduino-Temperature-Control-Library

#include <OneWire.h>
#include <DallasTemperature.h>

// GPIO where the DS18B20 is connected to
const int oneWireBus = 4;

// Setup a oneWire instance to communicate with any OneWire devices
OneWire oneWire(oneWireBus);

// Pass our oneWire reference to Dallas Temperature sensor
DallasTemperature sensors(&oneWire);

void setup()
{
  // Start the Serial Monitor
  Serial.begin(115200);
  // Start the DS18B20 sensor
  sensors.begin();
}

void loop()
{
  sensors.requestTemperatures();
  float temperatureC = sensors.getTempCByIndex(0);
  float temperatureF = sensors.getTempFByIndex(0);
  Serial.print(temperatureC);
  Serial.println(" ,ºC");
  //Serial.print(temperatureF);
  //Serial.println(" ,ºF");
  delay(500);
}
