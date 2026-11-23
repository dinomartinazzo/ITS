// serial_ui.h — interfaccia testuale su porta seriale (comandi in ingresso, report in uscita)
#pragma once
#include <Arduino.h>

struct Command {
  enum class Type : uint8_t { None, Tare, Stats, Span, SpanReset, ToggleRaw, Pause, Info, Help, Unknown };
  Type type = Type::None;
  double arg = 0.0;
  bool hasArg = false;
};

struct StatsReport {
  size_t n;
  double meanCounts;
  double stdCounts;
  int32_t minCounts;
  int32_t maxCounts;
  double meanMvV;
  double stdUvV;     // rumore in µV/V
};

class SerialUi {
public:
  explicit SerialUi(Stream &port) : port_(port) {}

  Command poll();   // non bloccante: restituisce un comando quando arriva una riga completa

  void banner();
  void help();
  void sampleEng(double mvv, double load, const char *unit);
  void sampleRaw(int32_t raw, double filtered);
  void stats(const StatsReport &r);
  void message(const char *text);

private:
  Command parse(const char *line);

  Stream &port_;
  char buf_[32] = {};
  size_t len_ = 0;
};
