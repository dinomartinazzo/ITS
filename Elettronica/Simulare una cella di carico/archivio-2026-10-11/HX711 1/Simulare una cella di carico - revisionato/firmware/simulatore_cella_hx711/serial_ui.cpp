// serial_ui.cpp — parsing comandi e formattazione dell'output
#include "serial_ui.h"
#include <ctype.h>
#include <stdlib.h>

Command SerialUi::poll() {
  while (port_.available() > 0) {
    const char c = static_cast<char>(port_.read());
    if (c == '\n' || c == '\r') {
      if (len_ == 0) {
        continue;   // CR+LF: la seconda terminazione è vuota
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
  const double value = strtod(rest, &end);
  cmd.hasArg = (end != rest);
  cmd.arg = value;

  switch (key) {
    case 't': cmd.type = Command::Type::Tare; break;
    case 's': cmd.type = Command::Type::Stats; break;
    case 'c': cmd.type = cmd.hasArg ? Command::Type::Span : Command::Type::SpanReset; break;
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
  port_.println("# Simulatore cella di carico - HX711 + ESP32");
  help();
}

void SerialUi::help() {
  port_.println("# Comandi:");
  port_.println("#   t          tara (media su N campioni)");
  port_.println("#   s          statistiche su N campioni (media, dev. std, min, max)");
  port_.println("#   c <mV/V>   calibrazione span al valore di riferimento indicato");
  port_.println("#   c          azzera la calibrazione span (fattore 1)");
  port_.println("#   r          alterna uscita ingegneristica / grezza");
  port_.println("#   p          pausa / riprende lo streaming");
  port_.println("#   i          configurazione e stato calibrazione");
  port_.println("#   h          questo aiuto");
}

void SerialUi::sampleEng(double mvv, double load, const char *unit) {
  // formato etichetta:valore, compatibile con il Serial Plotter
  port_.printf("mVV:%.4f\t%s:%.3f\n", mvv, unit, load);
}

void SerialUi::sampleRaw(int32_t raw, double filtered) {
  port_.printf("raw:%ld\tfilt:%.1f\n", static_cast<long>(raw), filtered);
}

void SerialUi::stats(const StatsReport &r) {
  port_.printf("# n=%u  media=%.1f cnt  std=%.1f cnt  min=%ld  max=%ld\n",
               static_cast<unsigned>(r.n), r.meanCounts, r.stdCounts,
               static_cast<long>(r.minCounts), static_cast<long>(r.maxCounts));
  port_.printf("# media=%.4f mV/V  rumore=%.3f uV/V rms  p-p=%ld cnt\n",
               r.meanMvV, r.stdUvV, static_cast<long>(r.maxCounts - r.minCounts));
}

void SerialUi::message(const char *text) {
  port_.print("# ");
  port_.println(text);
}
