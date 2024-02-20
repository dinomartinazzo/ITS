 Per organizzare i filtri come librerie in modo da poterli riutilizzare facilmente in altri progetti Arduino, dovrai seguire alcuni passaggi. Creerò un esempio per il filtro EMA (Exponential Moving Average) per mostrarti come procedere. Gli stessi passaggi possono essere applicati agli altri filtri modificando i dettagli specifici di ciascuno.
### 1. Creare i File della Libreria

Per ogni filtro, avrai bisogno di due file: un file header (`.h`) che dichiara la classe e le sue funzioni, e un file di implementazione (`.cpp`) che definisce le funzioni dichiarate nel file header.
#### Esempio per il Filtro EMA

**FiltroEMA.h** 

```cpp
#ifndef FiltroEMA_h
#define FiltroEMA_h

#include "Arduino.h"

class FiltroEMA {
  public:
    FiltroEMA(float alpha); // Costruttore che accetta il coefficiente alpha
    float calcola(float nuovoValore); // Metodo per calcolare il nuovo valore filtrato
  private:
    float _emaSegnale;
    float _alpha;
};

#endif
```



**FiltroEMA.cpp** 

```cpp
#include "FiltroEMA.h"

FiltroEMA::FiltroEMA(float alpha) {
  _alpha = alpha;
  _emaSegnale = 0;
}

float FiltroEMA::calcola(float nuovoValore) {
  _emaSegnale = _alpha * nuovoValore + (1 - _alpha) * _emaSegnale;
  return _emaSegnale;
}
```


### 2. Utilizzare la Libreria nel Tuo Sketch

Dopo aver creato i file della libreria, puoi includerli nel tuo sketch Arduino per utilizzare il filtro.

**Esempio di Utilizzo** 

```cpp
#include <Arduino.h>
#include "FiltroEMA.h"

FiltroEMA ema(0.1); // Crea un'istanza del filtro EMA con alpha = 0.1

void setup() {
  Serial.begin(115200);
}

void loop() {
  float segnale = analogRead(A0); // Legge un valore dal pin analogico A0
  float segnaleFiltrato = ema.calcola(segnale); // Applica il filtro EMA
  Serial.println(segnaleFiltrato); // Stampa il valore filtrato
  delay(100); // Aspetta un po' prima della prossima lettura
}
```


### 3. Organizzare le Librerie

Quando crei più filtri, organizza ciascun paio di file (`.h` e `.cpp`) nella propria cartella sotto la directory `libraries` della tua installazione Arduino o nella directory del tuo progetto. Questo ti permette di mantenere il codice ordinato e facilmente riutilizzabile.
### 4. Rinominare e Riutilizzare

Rinomina i file e le classi per gli altri filtri seguendo lo schema sopra, ad esempio, `FiltroMM.h` e `FiltroMM.cpp` per il filtro di media mobile, assicurandoti di aggiustare i contenuti dei file per riflettere la logica specifica di ciascun filtro.