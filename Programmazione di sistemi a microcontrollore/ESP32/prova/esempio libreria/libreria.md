- Organizzare tutti i filtri come librerie richiede un approccio sistematico simile a quello utilizzato per il filtro EMA. Per ciascun filtro, creerai un file header (`.h`) e un file di implementazione (`.cpp`). Qui ti fornirò un esempio su come organizzare ciascuno dei filtri menzionati nel codice iniziale come librerie separate.
### Struttura della Cartella

```Copy code
ArduinoProject/
│
├── libraries/
│   ├── FiltroEMA/
│   │   ├── FiltroEMA.h
│   │   └── FiltroEMA.cpp
│   ├── FiltroMM/
│   │   ├── FiltroMM.h
│   │   └── FiltroMM.cpp
│   ├── FiltroMediano/
│   │   ├── FiltroMediano.h
│   │   └── FiltroMediano.cpp
│   ├── FiltroFIR/
│   │   ├── FiltroFIR.h
│   │   └── FiltroFIR.cpp
│   ├── FiltroButterworth/
│   │   ├── FiltroButterworth.h
│   │   └── FiltroButterworth.cpp
│   └── FiltroKalman/
│       ├── FiltroKalman.h
│       └── FiltroKalman.cpp
└── YourArduinoSketch.ino
```

### Esempio di File Header e Implementazione per Ogni Filtro

Ogni coppia di file `.h` e `.cpp` definirà una classe per il rispettivo filtro. Qui sotto trovi un esempio per il Filtro EMA, e dovrai seguire una struttura simile per gli altri filtri, adattando i membri e i metodi in base alle specifiche di ciascun filtro.

**FiltroEMA.h** 

```cpp
#ifndef FiltroEMA_h
#define FiltroEMA_h

class FiltroEMA {
public:
    FiltroEMA(float alpha);
    float calcola(float nuovoValore);
private:
    float emaSegnale;
    float alpha;
};

#endif
```



**FiltroEMA.cpp** 

```cpp
#include "FiltroEMA.h"

FiltroEMA::FiltroEMA(float alpha) : alpha(alpha), emaSegnale(0) {}

float FiltroEMA::calcola(float nuovoValore) {
    emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
    return emaSegnale;
}
```


### Istruzioni per l'Uso

Dopo aver creato le librerie per ciascun filtro, puoi utilizzarle nel tuo sketch principale includendo l'header corrispondente e creando un'istanza dell'oggetto filtro. Ad esempio:

```cpp
#include <FiltroEMA.h>
#include <FiltroMM.h>
// Includi gli altri filtri qui

FiltroEMA ema(0.1); // Crea un'istanza del filtro EMA con alpha = 0.1
FiltroMM mm; // Assumi che il costruttore di FiltroMM non richieda parametri

void setup() {
    // Inizializzazione (se necessaria)
}

void loop() {
    float segnale = analogRead(A0); // Sostituisci con la tua sorgente di segnale
    float segnaleFiltratoEMA = ema.calcola(segnale);
    float segnaleFiltratoMM = mm.calcola(segnale);
    // Applica gli altri filtri come necessario
}
```

- Per creare una libreria per il filtro di media mobile (Moving Average, MM), dovrai seguire passaggi simili a quelli descritti precedentemente per il filtro EMA. Creeremo un file header (`.h`) che dichiara la classe del filtro MM e un file di implementazione (`.cpp`) che definisce il comportamento del filtro.
### Passo 1: Creare il File Header (FiltroMM.h)

```cpp
// FiltroMM.h
#ifndef FiltroMM_h
#define FiltroMM_h

#include "Arduino.h"

class FiltroMM {
  public:
    FiltroMM(); // Costruttore
    float calcola(float nuovoValore); // Metodo per aggiungere un nuovo valore e calcolare la media mobile
  private:
    static const int lunghezzaFinestra = 10; // Dimensione della finestra di media mobile
    float valoriFinestra[lunghezzaFinestra]; // Array per memorizzare gli ultimi valori
    int indiceValore; // Indice corrente nell'array
    float sommaValori; // Somma corrente dei valori nell'array
};

#endif
```


### Passo 2: Creare il File di Implementazione (FiltroMM.cpp)

```cpp
// FiltroMM.cpp
#include "FiltroMM.h"

FiltroMM::FiltroMM() {
  indiceValore = 0;
  sommaValori = 0;
  for (int i = 0; i < lunghezzaFinestra; i++) {
    valoriFinestra[i] = 0; // Inizializza l'array con 0
  }
}

float FiltroMM::calcola(float nuovoValore) {
  sommaValori -= valoriFinestra[indiceValore]; // Sottrai il valore più vecchio dalla somma
  valoriFinestra[indiceValore] = nuovoValore; // Inserisci il nuovo valore nell'array
  sommaValori += nuovoValore; // Aggiungi il nuovo valore alla somma
  indiceValore = (indiceValore + 1) % lunghezzaFinestra; // Aggiorna l'indice circolarmente
  return sommaValori / lunghezzaFinestra; // Restituisce la media mobile
}
```


### Passo 3: Utilizzo della Libreria nel Tuo Sketch

Dopo aver creato i file `FiltroMM.h` e `FiltroMM.cpp`, assicurati di posizionarli nella directory corretta (come descritto nella struttura della cartella per le librerie Arduino) e poi includi la libreria nel tuo sketch principale per usarla.

```cpp
#include <FiltroMM.h>

FiltroMM mm; // Crea un'istanza del filtro MM

void setup() {
  Serial.begin(115200);
}

void loop() {
  float segnale = analogRead(A0); // Sostituisci con la tua fonte di segnale
  float segnaleFiltrato = mm.calcola(segnale);
  Serial.println(segnaleFiltrato); // Stampa il valore filtrato
  delay(100); // Aspetta un po' prima della prossima lettura
}
```
- Per rendere la lunghezza della finestra parametrizzabile in modo che l'utente possa specificarla al momento della creazione dell'istanza del filtro, dovrai apportare alcune modifiche alla classe `FiltroMM`. Queste modifiche richiedono l'utilizzo di memoria dinamica, poiché la dimensione dell'array che tiene traccia dei valori della finestra non può essere determinata a compile-time.
### Modifica del File Header (FiltroMM.h)

Aggiungi un parametro al costruttore per specificare la lunghezza della finestra e aggiungi il codice per gestire la memoria dinamica.

```cpp
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
```


### Modifica del File di Implementazione (FiltroMM.cpp)

Implementa la gestione della memoria dinamica nel costruttore e distruttore.

```cpp
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
```


### Esempio di Utilizzo nel Tuo Sketch

```cpp
#include <FiltroMM.h>

FiltroMM mm(10); // Crea un'istanza del filtro MM con una finestra di 10 campioni

void setup() {
  Serial.begin(115200);
}

void loop() {
  float segnale = analogRead(A0); // Leggi un valore dal pin analogico A0
  float segnaleFiltrato = mm.calcola(segnale); // Applica il filtro MM
  Serial.println(segnaleFiltrato); // Stampa il valore filtrato
  delay(100); // Ritardo tra le letture
}
```



Questa modifica rende il filtro di media mobile (`FiltroMM`) più flessibile, permettendo all'utente di specificare la dimensione della finestra di media al momento della creazione dell'oggetto. La gestione della memoria dinamica assicura che la quantità di memoria utilizzata sia adeguata alla dimensione della finestra specificata, ottimizzando l'uso delle risorse.