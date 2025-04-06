#include "FiltroMM.h"

FiltroMM mm(20); // Crea un'istanza del filtro MM con una finestra di 20 campioni

void setup() {
  Serial.begin(115200);
}

void loop() {
  float segnale = analogRead(A0); // Leggi un valore dal pin analogico A0
  float segnaleFiltrato = mm.calcola(segnale); // Applica il filtro MM
  Serial.println(segnaleFiltrato); // Stampa il valore filtrato
  delay(100); // Ritardo tra le letture
}
