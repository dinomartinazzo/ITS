// Test della logica applicativa reale; ADC e seriale sono sostituiti da stub.
#include <cassert>
#include <cstdio>
#include <initializer_list>
#include "../firmware/lettore_ads131m04/app.cpp"
bool fakeReady = true;
uint32_t fakeNow = 10000;
unsigned printed = 0;
FakeSerial Serial;
static unsigned reads = 0;
static unsigned writes = 0;
static bool registersOk = true;
static uint16_t fakeId = 0x2400;
static Ads131m04Driver::Frame nextFrame{};
double Ads131m04Driver::begin(uint32_t hz, uint8_t) { id_ = fakeId; return hz; }
void Ads131m04Driver::sync() {}
bool Ads131m04Driver::writeRegister(uint8_t, uint16_t) { ++writes; return registersOk; }
void Ads131m04Driver::readFrame(Frame &f, uint16_t) { ++reads; f = nextFrame; }
Command SerialUi::poll() { return {}; }
void SerialUi::banner() {}
void SerialUi::help() {}
void SerialUi::message(const char *) {}

void resetCase() {
  task = Task::Idle;
  invalidateMeasurement();
  fakeReady = true;
  registersOk = true;
  configOk = true;
  fakeId = 0x2400;
  clkinHz = adc.begin(cfg::CLKIN_HZ, 0);
  discardLeft = 0;
  timeoutReported = false;
  lastFrameMs = fakeNow;
  lastPrintMs = 0;
  streaming = true;
  printed = reads = writes = 0;
  nextFrame = {};
  nextFrame.crcOk = true;
  nextFrame.ch[0] = 100000;
  nextFrame.ch[1] = -100000;
  nextFrame.ch[2] = 200000;
  nextFrame.ch[3] = 4369067; // circa 0,625 V -> eccitazione 2,5 V
  for (auto &v : tareMvV) v = 0.0;
}
void fill() { for (size_t i=0; i<cfg::FILTER_LEN; ++i) acquire(fakeNow); }
void assertInvalid() {
  assert(!filters[0].full());
  assert(task == Task::Idle);
  assert(acc[0].count() == 0);
  printed = 0;
  report(fakeNow);
  assert(printed == 0);
}
int main() {
  resetCase(); fill(); report(fakeNow); assert(printed > 0); // percorso normale
  resetCase(); configOk = false; startTask(Task::Tare); acquire(fakeNow);
  assert(reads == 0); assert(task == Task::Idle); // nessuna misura/config non valida
  for (int channel=0; channel<4; ++channel) {
    for (auto rail : {Ads131m04Driver::RAW_MAX, Ads131m04Driver::RAW_MIN}) {
      resetCase(); fill(); tareMvV[0] = 0.125; startTask(Task::Tare); acquire(fakeNow);
      nextFrame.ch[channel] = rail; acquire(fakeNow);
      assertInvalid(); assert(tareMvV[0] == 0.125);
    }
  }
  resetCase(); fill(); startTask(Task::Stats); acquire(fakeNow);
  nextFrame.crcOk=false; acquire(fakeNow); assertInvalid();
  nextFrame.crcOk=true; fill(); assert(filters[0].full()); // recupero dopo errore
  resetCase(); fill(); startTask(Task::Tare); nextFrame.ch[3]=0;
  acquire(fakeNow); assertInvalid();
  resetCase(); fill(); startTask(Task::Tare); fakeReady=false;
  acquire(fakeNow+cfg::DRDY_TIMEOUT_MS+1); assertInvalid();
  resetCase(); fill(); startTask(Task::Tare); registersOk=false;
  configOk=applyConfig(); assert(!configOk); assertInvalid();
  unsigned oldReads=reads; acquire(fakeNow); assert(reads==oldReads);
  resetCase(); fill(); startTask(Task::Stats); configOk=applyConfig();
  assert(configOk); assertInvalid(); // nuova configurazione annulla raccolta
  for (unsigned i=0;i<cfg::DISCARD_FRAMES;++i) acquire(fakeNow);
  assert(!filters[0].full()); fill(); assert(filters[0].full());
  resetCase(); clkinHz=0; configOk=applyConfig(); assert(!configOk); assert(writes==0);
  resetCase(); fakeId=0; adc.begin(cfg::CLKIN_HZ, 0);
  configOk=applyConfig(); assert(!configOk); assert(writes==0);
  resetCase(); startTask(Task::Tare);
  for(size_t i=0;i<cfg::STATS_SAMPLES;++i) acquire(fakeNow);
  assert(task==Task::Idle); assert(!filters[0].full());
  fill(); assert(filters[0].full()); assert(std::abs(filters[0].mean()) <= 1.0);
  std::puts("PASS: acquisizione, configurazione, saturazione 4 canali +/- , CRC, eccitazione, timeout, recupero e tara");
}
