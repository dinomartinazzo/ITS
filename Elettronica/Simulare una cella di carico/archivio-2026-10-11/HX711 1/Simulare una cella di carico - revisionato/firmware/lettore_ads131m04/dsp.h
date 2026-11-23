// dsp.h — filtri e statistiche su campioni interi (header-only)
#pragma once
#include <stddef.h>
#include <stdint.h>
#include <math.h>
#include <limits>

// Media mobile su N campioni; somma a 64 bit, nessun overflow con dati a 24 bit
template <size_t N>
class MovingAverage {
public:
  void reset() {
    idx_ = 0;
    count_ = 0;
    sum_ = 0;
  }

  void push(int32_t x) {
    if (count_ == N) {
      sum_ -= buf_[idx_];
    } else {
      ++count_;
    }
    buf_[idx_] = x;
    sum_ += x;
    idx_ = (idx_ + 1) % N;
  }

  bool full() const { return count_ == N; }
  double mean() const { return count_ ? static_cast<double>(sum_) / count_ : 0.0; }

private:
  int32_t buf_[N] = {};
  size_t idx_ = 0;
  size_t count_ = 0;
  int64_t sum_ = 0;
};

// Statistiche incrementali (algoritmo di Welford): media e deviazione standard senza buffer
class RunningStats {
public:
  void reset() {
    n_ = 0;
    mean_ = 0.0;
    m2_ = 0.0;
    min_ = std::numeric_limits<int32_t>::max();
    max_ = std::numeric_limits<int32_t>::min();
  }

  void push(int32_t x) {
    ++n_;
    const double d = x - mean_;
    mean_ += d / n_;
    m2_ += d * (x - mean_);
    if (x < min_) {
      min_ = x;
    }
    if (x > max_) {
      max_ = x;
    }
  }

  size_t count() const { return n_; }
  double mean() const { return mean_; }
  double stddev() const { return n_ > 1 ? sqrt(m2_ / (n_ - 1)) : 0.0; }
  int32_t min() const { return min_; }
  int32_t max() const { return max_; }

private:
  size_t n_ = 0;
  double mean_ = 0.0;
  double m2_ = 0.0;
  int32_t min_ = std::numeric_limits<int32_t>::max();
  int32_t max_ = std::numeric_limits<int32_t>::min();
};
