// ads131m04_driver.cpp — temporizzazioni e formati dal datasheet TI SBAS890D (ADS131M04)
#include "ads131m04_driver.h"

namespace {
constexpr uint8_t WORD_BYTES  = 3;   // parole da 24 bit (WLENGTH = 01b, valore di reset)
constexpr uint8_t FRAME_WORDS = 6;   // risposta + 4 canali + CRC
constexpr uint8_t FRAME_BYTES = WORD_BYTES * FRAME_WORDS;

uint16_t cmdRreg(uint8_t addr) { return static_cast<uint16_t>(0xA000 | ((addr & 0x3F) << 7)); }  // 101a aaaa a000 0000
uint16_t cmdWreg(uint8_t addr) { return static_cast<uint16_t>(0x6000 | ((addr & 0x3F) << 7)); }  // 011a aaaa a000 0000
uint16_t ackWreg(uint8_t addr) { return static_cast<uint16_t>(0x4000 | ((addr & 0x3F) << 7)); }  // 010a aaaa a000 0000
}  // namespace

uint16_t Ads131m04Driver::crc16Ccitt(const uint8_t *data, size_t len) {
  uint16_t crc = 0xFFFF;                       // seme FFFFh, polinomio x^16 + x^12 + x^5 + 1
  for (size_t i = 0; i < len; ++i) {
    crc ^= static_cast<uint16_t>(data[i]) << 8;
    for (uint8_t b = 0; b < 8; ++b) {
      crc = (crc & 0x8000) ? static_cast<uint16_t>((crc << 1) ^ 0x1021) : static_cast<uint16_t>(crc << 1);
    }
  }
  return crc;
}

double Ads131m04Driver::begin(uint32_t clkinHz, uint8_t ledcChannel) {
  pinMode(p_.cs, OUTPUT);
  digitalWrite(p_.cs, HIGH);
  pinMode(p_.drdy, INPUT_PULLUP);
  pinMode(p_.sync, OUTPUT);
  digitalWrite(p_.sync, HIGH);

  // Clock master su CLKIN: 1 bit di risoluzione = onda quadra al 50%
  double freq = 0.0;
#if defined(ESP_ARDUINO_VERSION_MAJOR) && ESP_ARDUINO_VERSION_MAJOR >= 3
  (void)ledcChannel;
  if (ledcAttach(p_.clkin, clkinHz, 1)) {
    ledcWrite(p_.clkin, 1);
    freq = ledcReadFreq(p_.clkin);
  }
#else
  freq = ledcSetup(ledcChannel, clkinHz, 1);
  ledcAttachPin(p_.clkin, ledcChannel);
  ledcWrite(ledcChannel, 1);
#endif

  SPI.begin(p_.sclk, p_.miso, p_.mosi, -1);   // CS gestito via GPIO: deve restare basso per tutta la trama
  hardReset();

  uint16_t value = 0;
  id_ = readRegister(REG_ID, value) ? value : 0;
  return freq;
}

void Ads131m04Driver::hardReset() {
  digitalWrite(p_.sync, LOW);
  delay(1);                     // >= 2048 periodi di CLKIN (256 us a 8 MHz): reset
  digitalWrite(p_.sync, HIGH);
  delay(1);                     // tREGACQ = 5 us; margine per l'avvio dei filtri
}

void Ads131m04Driver::sync() {
  digitalWrite(p_.sync, LOW);
  delayMicroseconds(10);        // 1..2047 periodi di CLKIN: sincronizzazione senza reset
  digitalWrite(p_.sync, HIGH);
}

void Ads131m04Driver::transfer(uint16_t command, const uint16_t *data, uint8_t nData, Frame *out) {
  uint8_t tx[FRAME_BYTES] = {};
  uint8_t rx[FRAME_BYTES] = {};
  tx[0] = static_cast<uint8_t>(command >> 8);  // parole allineate a sinistra, ultimi 8 bit a zero
  tx[1] = static_cast<uint8_t>(command & 0xFF);
  for (uint8_t i = 0; i < nData && i < FRAME_WORDS - 1; ++i) {
    tx[WORD_BYTES * (i + 1)] = static_cast<uint8_t>(data[i] >> 8);
    tx[WORD_BYTES * (i + 1) + 1] = static_cast<uint8_t>(data[i] & 0xFF);
  }

  SPI.beginTransaction(spi_);
  digitalWrite(p_.cs, LOW);
  SPI.transferBytes(tx, rx, FRAME_BYTES);
  digitalWrite(p_.cs, HIGH);
  SPI.endTransaction();

  if (out == nullptr) {
    return;
  }
  out->response = static_cast<uint16_t>((rx[0] << 8) | rx[1]);
  for (uint8_t k = 0; k < 4; ++k) {
    const uint8_t *b = &rx[WORD_BYTES * (k + 1)];
    uint32_t v = (static_cast<uint32_t>(b[0]) << 16) | (static_cast<uint32_t>(b[1]) << 8) | b[2];
    if (v & 0x800000u) {
      v |= 0xFF000000u;          // estensione del segno
    }
    out->ch[k] = static_cast<int32_t>(v);
  }
  out->crc = static_cast<uint16_t>((rx[15] << 8) | rx[16]);
  out->crcOk = (crc16Ccitt(rx, 15) == out->crc);   // CRC su risposta + 4 canali, riempimento compreso
}

void Ads131m04Driver::readFrame(Frame &frame, uint16_t command) {
  transfer(command, nullptr, 0, &frame);
}

bool Ads131m04Driver::readRegister(uint8_t addr, uint16_t &value) {
  Frame f;
  transfer(cmdRreg(addr), nullptr, 0, nullptr);   // comando
  transfer(CMD_NULL, nullptr, 0, &f);             // la risposta arriva nella trama successiva
  value = f.response;
  return f.crcOk;
}

bool Ads131m04Driver::writeRegister(uint8_t addr, uint16_t value) {
  Frame f;
  transfer(cmdWreg(addr), &value, 1, nullptr);
  transfer(CMD_NULL, nullptr, 0, &f);
  if (f.response != ackWreg(addr)) {              // 010a aaaa ammm mmmm, m = registri scritti - 1
    return false;
  }
  uint16_t check = 0;
  return readRegister(addr, check) && check == value;
}
