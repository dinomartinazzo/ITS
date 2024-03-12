// FiltroMM.cpp
#include "FiltroMM.h"

FiltroMM::FiltroMM(int lunghezzaFinestra) {
  this->lunghezzaFinestra = lunghezzaFinestra;
  valoriFinestra = new float[lunghezzaFinestra]; // Alloca memoria dinamicamente
  indiceValore = 0;
  sommaValori = 0;
  for (int i = 0; i < lunghezzaFinestra; i++) {
    valoriFinestra[i] = 0; // Inizializza l'array con 0
  }
}

FiltroMM::~FiltroMM() {
  delete[] valoriFinestra; // Libera la memoria allocata
}

float FiltroMM::calcola(float nuovoValore) {
  sommaValori -= valoriFinestra[indiceValore]; // Sottrai il valore più vecchio dalla somma
  valoriFinestra[indiceValore] = nuovoValore; // Inserisci il nuovo valore nell'array
  sommaValori += nuovoValore; // Aggiungi il nuovo valore alla somma
  indiceValore = (indiceValore + 1) % lunghezzaFinestra; // Aggiorna l'indice circolarmente
  return sommaValori / lunghezzaFinestra; // Restituisce la media mobile
}
