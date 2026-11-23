// hx711_driver.h — driver bit-bang per HX711 (lettura non bloccante)
#pragma once
#include <Arduino.h>

class Hx711Driver {
public:
  enum class Status : uint8_t { Ok, NotReady, Saturated };

  static constexpr int32_t RAW_MAX = 0x7FFFFF;   // +fondo scala ADC
  static constexpr int32_t RAW_MIN = -0x800000;  // -fondo scala ADC

  Hx711Driver(uint8_t pinDout, uint8_t pinSck, uint8_t extraPulses);

  void begin();
  bool isReady() const;                 // DOUT basso = conversione disponibile
  Status read(int32_t &value);          // ritorna subito se il dato non è pronto
  void powerDown();                     // SCK alto per più di 60 us
  void powerUp();

private:
  void pulse();

  uint8_t pinDout_;
  uint8_t pinSck_;
  uint8_t extraPulses_;
};
