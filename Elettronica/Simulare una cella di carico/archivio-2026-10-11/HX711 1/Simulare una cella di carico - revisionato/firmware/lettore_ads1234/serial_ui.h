// serial_ui.h — comandi da seriale per il lettore multicanale
#pragma once
#include <Arduino.h>

struct Command {
  enum class Type : uint8_t { None, Tare, Stats, OffsetCal, Speed, Channels, ToggleRaw, Pause, Info, Help, Unknown };
  Type type = Type::None;
  double arg = 0.0;
  bool hasArg = false;
};

class SerialUi {
public:
  explicit SerialUi(Stream &port) : port_(port) {}

  Command poll();          // non bloccante
  void banner();
  void help();
  void message(const char *text);

private:
  Command parse(const char *line);

  Stream &port_;
  char buf_[32] = {};
  size_t len_ = 0;
};
