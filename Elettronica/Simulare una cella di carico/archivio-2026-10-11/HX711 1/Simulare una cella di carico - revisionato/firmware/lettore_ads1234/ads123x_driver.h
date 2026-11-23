// ads123x_driver.h — driver per ADS1232/ADS1234 (TI): interfaccia a due fili, controllo a pin
#pragma once
#include <Arduino.h>

class Ads123xDriver {
public:
  struct Pins {
    uint8_t dout;
    uint8_t sclk;
    uint8_t a0;
    uint8_t a1;
    uint8_t pdwn;
    uint8_t speed;
  };
  enum class Status : uint8_t { Ok, NotReady, Saturated };

  static constexpr int32_t RAW_MAX = 0x7FFFFF;
  static constexpr int32_t RAW_MIN = -0x800000;

  explicit Ads123xDriver(const Pins &pins) : p_(pins) {}

  void begin(bool fast);                 // configura i pin ed esegue la sequenza di accensione
  void setSpeed(bool fast);              // cambia SPEED e riavvia il convertitore
  void selectChannel(uint8_t channel);   // 0..3; DRDY resta alto fino a dato assestato
  bool isReady() const;
  // Legge 24 bit. Con calibrate = true invia 26 impulsi e avvia la calibrazione dell'offset.
  Status read(int32_t &value, bool calibrate = false);

  uint8_t channel() const { return channel_; }
  bool fast() const { return fast_; }

private:
  void pulse();
  void restart();

  Pins p_;
  uint8_t channel_ = 0;
  bool fast_ = false;
};
