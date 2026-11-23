// serial_ui.cpp — parsing dei comandi e testi di aiuto
#include "serial_ui.h"
#include <ctype.h>
#include <stdlib.h>

Command SerialUi::poll() {
  while (port_.available() > 0) {
    const char c = static_cast<char>(port_.read());
    if (c == '\n' || c == '\r') {
      if (len_ == 0) {
        continue;
      }
      buf_[len_] = '\0';
      len_ = 0;
      return parse(buf_);
    }
    if (len_ < sizeof(buf_) - 1) {
      buf_[len_++] = c;
    }
  }
  return Command{};
}

Command SerialUi::parse(const char *line) {
  Command cmd;
  while (*line == ' ') {
    ++line;
  }
  const char key = static_cast<char>(tolower(*line));
  const char *rest = line + 1;
  char *end = nullptr;
  cmd.arg = strtod(rest, &end);
  cmd.hasArg = (end != rest);

  switch (key) {
    case 't': cmd.type = Command::Type::Tare; break;
    case 's': cmd.type = Command::Type::Stats; break;
    case 'o': cmd.type = Command::Type::Osr; break;
    case 'g': cmd.type = Command::Type::GlobalChop; break;
    case 'r': cmd.type = Command::Type::ToggleRaw; break;
    case 'p': cmd.type = Command::Type::Pause; break;
    case 'i': cmd.type = Command::Type::Info; break;
    case 'h':
    case '?': cmd.type = Command::Type::Help; break;
    default: cmd.type = Command::Type::Unknown; break;
  }
  return cmd;
}

void SerialUi::banner() {
  port_.println();
  port_.println("# Lettore simultaneo ADS131M04 + ESP32");
  help();
}

void SerialUi::help() {
  port_.println("# Comandi:");
  port_.println("#   t        tara delle tre celle");
  port_.println("#   s        statistiche per canale (media, rumore in uV/V e nV)");
  port_.println("#   o <0-7>  OSR: 0=128 ... 7=16384");
  port_.println("#   g        attiva / disattiva il global-chop");
  port_.println("#   r        alterna uscita ingegneristica / grezza");
  port_.println("#   p        pausa / riprende lo streaming");
  port_.println("#   i        configurazione, ID, contatori di errore");
  port_.println("#   h        questo aiuto");
}

void SerialUi::message(const char *text) {
  port_.print("# ");
  port_.println(text);
}
