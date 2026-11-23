#pragma once
#include <cstddef>
#include <cstdint>
#include <cstdarg>
#define LOW 0
#define HIGH 1
extern bool fakeReady;
extern uint32_t fakeNow;
extern unsigned printed;
inline int digitalRead(uint8_t) { return fakeReady ? LOW : HIGH; }
inline uint32_t millis() { return fakeNow; }
inline void delay(unsigned) {}
struct Stream {};
struct FakeSerial : Stream {
  void begin(uint32_t) {}
  void printf(const char *, ...) { ++printed; }
};
extern FakeSerial Serial;
