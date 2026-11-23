// ads123x_driver.cpp — temporizzazioni dal datasheet TI SBAS350H (ADS123x)
#include "ads123x_driver.h"

void Ads123xDriver::begin(bool fast) {
  pinMode(p_.sclk, OUTPUT);
  digitalWrite(p_.sclk, LOW);          // SCLK alto a lungo = standby
  pinMode(p_.dout, INPUT);
  pinMode(p_.a0, OUTPUT);
  pinMode(p_.a1, OUTPUT);
  pinMode(p_.speed, OUTPUT);
  pinMode(p_.pdwn, OUTPUT);

  digitalWrite(p_.pdwn, LOW);          // convertitore in reset durante la configurazione
  selectChannel(0);
  fast_ = fast;
  digitalWrite(p_.speed, fast ? HIGH : LOW);
  delay(1);                            // t15 >= 10 us con alimentazioni stabili

  // Sequenza di accensione (fig. 7-15): PDWN alto >= 26 us, basso >= 26 us, poi alto
  digitalWrite(p_.pdwn, HIGH);
  delayMicroseconds(50);
  restart();
}

void Ads123xDriver::restart() {
  digitalWrite(p_.pdwn, LOW);
  delayMicroseconds(50);               // t14 >= 26 us
  digitalWrite(p_.pdwn, HIGH);         // primo dato valido dopo 401,8 ms (10 SPS) o 52,5 ms (80 SPS)
}

void Ads123xDriver::setSpeed(bool fast) {
  fast_ = fast;
  digitalWrite(p_.speed, fast ? HIGH : LOW);
  restart();                           // riparte con il filtro digitale azzerato
}

void Ads123xDriver::selectChannel(uint8_t channel) {
  channel_ = channel & 0x03;
  digitalWrite(p_.a0, (channel_ & 0x01) ? HIGH : LOW);
  digitalWrite(p_.a1, (channel_ & 0x02) ? HIGH : LOW);
  delayMicroseconds(60);               // tS max 50 us: entro questo tempo DRDY va alto
}

bool Ads123xDriver::isReady() const {
  return digitalRead(p_.dout) == LOW;
}

void Ads123xDriver::pulse() {
  digitalWrite(p_.sclk, HIGH);
  delayMicroseconds(1);                // t3 >= 100 ns
  digitalWrite(p_.sclk, LOW);
  delayMicroseconds(1);
}

Ads123xDriver::Status Ads123xDriver::read(int32_t &value, bool calibrate) {
  if (!isReady()) {
    return Status::NotReady;
  }

  // Nessuna sezione critica: lo standby richiede SCLK alto per circa 12 ms (80 SPS),
  // molto più di qualsiasi interruzione del sistema.
  uint32_t data = 0;
  for (uint8_t i = 0; i < 24; ++i) {   // MSB per primo, bit valido 50 ns dopo il fronte di salita
    digitalWrite(p_.sclk, HIGH);
    delayMicroseconds(1);
    data = (data << 1) | (digitalRead(p_.dout) == HIGH ? 1u : 0u);
    digitalWrite(p_.sclk, LOW);
    delayMicroseconds(1);
  }
  pulse();                             // 25° impulso: DOUT forzato alto fino al prossimo dato
  if (calibrate) {
    pulse();                           // 26° impulso: il fronte di discesa avvia la calibrazione
  }

  if (data & 0x800000u) {
    data |= 0xFF000000u;
  }
  value = static_cast<int32_t>(data);

  if (value >= RAW_MAX || value <= RAW_MIN) {
    return Status::Saturated;
  }
  return Status::Ok;
}
