// load_model.cpp — modello ratiometrico HX711: ±0,5·Vex/gain corrisponde a ±2^23 conteggi
#include "load_model.h"
#include <math.h>

namespace {
constexpr double FULL_SCALE_COUNTS = 8388608.0;  // 2^23
constexpr double MIN_SPAN_COUNTS = 10000.0;      // segnale minimo per una calibrazione sensata
constexpr double SPAN_MIN = 0.5;
constexpr double SPAN_MAX = 2.0;
}

LoadModel::LoadModel(float gain, float sensMvV, float capacity)
    : mvvPerCount_(500.0 / (gain * FULL_SCALE_COUNTS)),  // [mV/V per conteggio]
      sens_(sensMvV),
      cap_(capacity) {}

double LoadModel::countsToMvV(double counts) const {
  return (counts - offset_) * mvvPerCount_ * span_;
}

double LoadModel::mvvToLoad(double mvv) const {
  return mvv / sens_ * cap_;
}

bool LoadModel::calibrateSpan(double meanCounts, double referenceMvV) {
  const double net = meanCounts - offset_;
  if (fabs(net) < MIN_SPAN_COUNTS || referenceMvV == 0.0) {
    return false;
  }
  const double factor = referenceMvV / (net * mvvPerCount_);
  if (factor < SPAN_MIN || factor > SPAN_MAX) {
    return false;   // valore incoerente: probabile errore di segno o di misura
  }
  span_ = factor;
  return true;
}
