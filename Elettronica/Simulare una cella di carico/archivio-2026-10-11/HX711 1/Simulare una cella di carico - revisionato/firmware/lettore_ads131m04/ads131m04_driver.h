// ads131m04_driver.h — driver SPI per ADS131M04 (TI): trame a 6 parole da 24 bit
#pragma once
#include <Arduino.h>
#include <SPI.h>

class Ads131m04Driver {
public:
  struct Pins {
    uint8_t sclk;
    uint8_t miso;
    uint8_t mosi;
    uint8_t cs;
    uint8_t drdy;
    uint8_t sync;
    uint8_t clkin;
  };
  struct Frame {
    uint16_t response;   // risposta al comando della trama precedente
    int32_t ch[4];       // dati dei quattro canali, complemento a 2 su 24 bit
    uint16_t crc;
    bool crcOk;
  };

  static constexpr uint16_t CMD_NULL  = 0x0000;
  static constexpr uint16_t CMD_RESET = 0x0011;
  static constexpr uint8_t REG_ID     = 0x00;
  static constexpr uint8_t REG_STATUS = 0x01;
  static constexpr uint8_t REG_MODE   = 0x02;
  static constexpr uint8_t REG_CLOCK  = 0x03;
  static constexpr uint8_t REG_GAIN   = 0x04;
  static constexpr uint8_t REG_CFG    = 0x06;
  static constexpr int32_t RAW_MAX = 0x7FFFFF;
  static constexpr int32_t RAW_MIN = -0x800000;

  Ads131m04Driver(const Pins &pins, uint32_t spiHz) : p_(pins), spi_(spiHz, MSBFIRST, SPI_MODE1) {}

  // Avvia il clock su CLKIN, esegue il reset hardware e verifica l'ID. Ritorna la frequenza effettiva.
  double begin(uint32_t clkinHz, uint8_t ledcChannel);
  bool isReady() const { return digitalRead(p_.drdy) == LOW; }
  void readFrame(Frame &frame, uint16_t command = CMD_NULL);
  bool readRegister(uint8_t addr, uint16_t &value);
  bool writeRegister(uint8_t addr, uint16_t value);   // scrive e rilegge per conferma
  void hardReset();                                    // SYNC/RESET basso >= 2048 periodi di CLKIN
  void sync();                                         // impulso breve: riallinea i filtri e svuota le FIFO
  uint16_t id() const { return id_; }

  static uint16_t crc16Ccitt(const uint8_t *data, size_t len);

private:
  void transfer(uint16_t command, const uint16_t *data, uint8_t nData, Frame *out);

  Pins p_;
  SPISettings spi_;
  uint16_t id_ = 0;
};
