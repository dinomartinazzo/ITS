// hx711_driver.cpp — implementazione del protocollo seriale HX711
#include "hx711_driver.h"

// Sezione critica: un'interruzione durante la lettura allungherebbe SCK alto;
// oltre 60 us il chip entra in power-down e il dato va perso.
static portMUX_TYPE s_hxMux = portMUX_INITIALIZER_UNLOCKED;

Hx711Driver::Hx711Driver(uint8_t pinDout, uint8_t pinSck, uint8_t extraPulses)
    : pinDout_(pinDout), pinSck_(pinSck), extraPulses_(extraPulses) {}

void Hx711Driver::begin() {
  pinMode(pinSck_, OUTPUT);
  digitalWrite(pinSck_, LOW);   // SCK basso = chip attivo
  pinMode(pinDout_, INPUT);
}

bool Hx711Driver::isReady() const {
  return digitalRead(pinDout_) == LOW;
}

void Hx711Driver::pulse() {
  digitalWrite(pinSck_, HIGH);
  delayMicroseconds(1);         // T3 min 0,2 us
  digitalWrite(pinSck_, LOW);
  delayMicroseconds(1);         // T4 min 0,2 us
}

Hx711Driver::Status Hx711Driver::read(int32_t &value) {
  if (!isReady()) {
    return Status::NotReady;
  }

  uint32_t data = 0;
  portENTER_CRITICAL(&s_hxMux);
  for (uint8_t i = 0; i < 24; ++i) {          // 24 bit, MSB per primo
    digitalWrite(pinSck_, HIGH);
    delayMicroseconds(1);                     // dato valido 0,1 us dopo il fronte di salita
    data = (data << 1) | (digitalRead(pinDout_) == HIGH ? 1u : 0u);
    digitalWrite(pinSck_, LOW);
    delayMicroseconds(1);
  }
  for (uint8_t i = 0; i < extraPulses_; ++i) { // seleziona canale/guadagno della prossima conversione
    pulse();
  }
  portEXIT_CRITICAL(&s_hxMux);

  if (data & 0x800000u) {                     // estensione del segno: complemento a 2 su 24 bit
    data |= 0xFF000000u;
  }
  value = static_cast<int32_t>(data);

  if (value >= RAW_MAX || value <= RAW_MIN) {
    return Status::Saturated;
  }
  return Status::Ok;
}

void Hx711Driver::powerDown() {
  digitalWrite(pinSck_, LOW);
  digitalWrite(pinSck_, HIGH);
  delayMicroseconds(70);        // > 60 us: power-down
}

void Hx711Driver::powerUp() {
  digitalWrite(pinSck_, LOW);   // ripartenza su canale A, gain 128
}
