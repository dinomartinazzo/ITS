// FiltroMM.h
#ifndef FiltroMM_h
#define FiltroMM_h

#include "Arduino.h"

class FiltroMM {
  public:
    FiltroMM(int lunghezzaFinestra); // Costruttore modificato per accettare la lunghezza della finestra
    ~FiltroMM(); // Distruttore per liberare la memoria
    float calcola(float nuovoValore); // Metodo per aggiungere un nuovo valore e calcolare la media mobile
  private:
    int lunghezzaFinestra; // Dimensione della finestra di media mobile
    float *valoriFinestra; // Puntatore all'array per memorizzare gli ultimi valori
    int indiceValore; // Indice corrente nell'array
    float sommaValori; // Somma corrente dei valori nell'array
};

#endif
