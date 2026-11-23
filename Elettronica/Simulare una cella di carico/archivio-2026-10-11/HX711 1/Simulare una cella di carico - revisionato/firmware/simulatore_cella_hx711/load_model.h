// load_model.h — conversione conteggi -> mV/V -> unità ingegneristiche, tara e span
#pragma once
#include <stdint.h>

class LoadModel {
public:
  LoadModel(float gain, float sensMvV, float capacity);

  void setOffset(double offsetCounts) { offset_ = offsetCounts; }
  double offset() const { return offset_; }

  // Corregge il guadagno: la media netta attuale deve valere referenceMvV
  bool calibrateSpan(double meanCounts, double referenceMvV);
  void resetSpan() { span_ = 1.0; }
  double spanFactor() const { return span_; }

  double countsToMvV(double counts) const;   // applica tara e span
  double mvvToLoad(double mvv) const;        // mV/V -> unità della cella
  double mvvPerCount() const { return mvvPerCount_; }

private:
  double mvvPerCount_;
  double sens_;
  double cap_;
  double offset_ = 0.0;
  double span_ = 1.0;
};
