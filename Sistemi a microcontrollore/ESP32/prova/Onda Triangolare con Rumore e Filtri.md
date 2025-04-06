- This Arduino sketch is designed to generate and modify a triangular wave signal, incorporating both random noise and occasional spikes, before outputting the modified signal over a serial connection. Here's a breakdown of its key components and functionality: 
- **Global Parameters for the Triangular Wave** : The code defines constants for the minimum (`valoreMin`) and maximum (`valoreMax`) values of the triangular wave, as well as the step size (`passo`), which controls the speed of the signal's change. The `passo` value is the amount by which the signal increases or decreases with each update. 
- **Direction and Current Value Variables** : It uses a boolean variable (`incrementa`) to track the direction of the signal (increasing or decreasing). The current value of the signal is held in `valoreCorrente`, starting at the minimum value. 
- **Triangular Wave Update Function** : The `aggiornaSegnaleTriangolare()` function updates the triangular wave. If the wave is increasing and reaches the maximum value, it reverses direction; if it is decreasing and reaches the minimum value, it changes direction to increase again. 
- **Noise and Spike Addition Function** : The `aggiungiRumoreESpike(float segnale)` function takes the current signal value as input and adds random noise to it by using the `random(-150, 150)` function call. Additionally, it occasionally inserts a large spike into the signal, with a 5% chance (`random(0, 100) > 95`) of adding a random value between -1300 and 1300 to the signal. 
- ** Function** : This function initializes the serial communication at a baud rate of 115200 bits per second, which is used for sending the signal data to a connected computer. 
- ** Function** : The main program loop repeatedly updates the triangular wave, adds noise and spikes, and then sends the modified signal value over the serial connection. A `delay(10)` call at the end of the loop controls the frequency of the updates, pausing the loop for 10 milliseconds between each update.

This sketch is useful for simulating signals with varying degrees of randomness and for testing signal processing algorithms or monitoring tools that need to handle both gradual changes in signal strength and sudden, unpredictable spikes.

```cpp

  - #include <Arduino.h>

  // Parametri del segnale triangolare
  const float valoreMin = 0;
  const float valoreMax = 4096;  
  const float passo = 5; // Velocità di cambiamento del segnale

  // Variabile per la direzione del segnale (incremento o decremento)
  bool incrementa = true;

  // Variabile per il valore corrente del segnale
  float valoreCorrente = valoreMin;

  void aggiornaSegnaleTriangolare() {
    if (incrementa) {
      valoreCorrente += passo;
      if (valoreCorrente >= valoreMax) {
        incrementa = false;
      }
    } else {
      valoreCorrente -= passo;
      if (valoreCorrente <= valoreMin) {
        incrementa = true;
      }
    }
  }

  float aggiungiRumoreESpike(float segnale) {
    // Aggiungi rumore bianco
    float rumore = random(-150, 150);  
    segnale += rumore;

    // Aggiungi occasionalmente uno spike
    if (random(0, 100) > 95) { // Con una probabilità del 5%
      segnale += random(-1300, 1300); // Spike con ampie variazione
    }

    return segnale;
  }


  void setup() {
    Serial.begin(115200);
  }

  void loop() {
    // Aggiorna e genera il segnale triangolare
    aggiornaSegnaleTriangolare();

    // Aggiungi rumore e spike
    float segnaleConRumore = aggiungiRumoreESpike(valoreCorrente);

    // Stampa il segnale modificato sulla console seriale (per debug o visualizzazione)
    Serial.println(segnaleConRumore);
  
    delay(10); // Regola questo valore in base alla frequenza di aggiornamento desiderata
  }
  
```

  
Per sostituire `delay()` con l'uso di `millis()` nel tuo sketch Arduino, è necessario implementare una logica di temporizzazione non bloccante. Questo approccio consente al tuo programma di eseguire altre operazioni mentre aspetta che passi il tempo necessario per l'aggiornamento del segnale. Ecco come potresti modificare il tuo sketch:

```cpp
#include <Arduino.h>

// Parametri del segnale triangolare
const float valoreMin = 0;
const float valoreMax = 4096;  
const float passo = 5; // Velocità di cambiamento del segnale

// Variabile per la direzione del segnale (incremento o decremento)
bool incrementa = true;

// Variabile per il valore corrente del segnale
float valoreCorrente = valoreMin;

// Variabili per la gestione del tempo con millis()
unsigned long tempoPrecedente = 0; // Memorizza l'ultimo momento in cui il segnale è stato aggiornato
const long intervallo = 10; // Intervallo di tempo per gli aggiornamenti del segnale (in millisecondi)

void aggiornaSegnaleTriangolare() {
  if (incrementa) {
    valoreCorrente += passo;
    if (valoreCorrente >= valoreMax) {
      incrementa = false;
    }
  } else {
    valoreCorrente -= passo;
    if (valoreCorrente <= valoreMin) {
      incrementa = true;
    }
  }
}

float aggiungiRumoreESpike(float segnale) {
  // Aggiungi rumore bianco
  float rumore = random(-150, 150);  
  segnale += rumore;

  // Aggiungi occasionalmente uno spike
  if (random(0, 100) > 95) { // Con una probabilità del 5%
    segnale += random(-1300, 1300); // Spike con ampie variazione
  }

  return segnale;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  // Utilizza millis() per aggiornare il segnale in modo non bloccante
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    // Aggiorna e genera il segnale triangolare
    aggiornaSegnaleTriangolare();

    // Aggiungi rumore e spike
    float segnaleConRumore = aggiungiRumoreESpike(valoreCorrente);

    // Stampa il segnale modificato sulla console seriale
    Serial.println(segnaleConRumore);
  }

  // Qui puoi inserire altre operazioni che devono essere eseguite in modo continuativo
}
```

In questo codice, `tempoPrecedente` tiene traccia dell'ultimo momento in cui il segnale è stato aggiornato, e `intervallo` specifica ogni quanti millisecondi il segnale deve essere aggiornato. Il controllo `if (tempoAttuale - tempoPrecedente >= intervallo)` determina se è il momento di aggiornare il segnale.

Usando `millis()` invece di `delay()`, il tuo sketch diventa non bloccante, permettendoti di eseguire altre operazioni nel loop principale senza dover attendere il completamento della pausa.


   


Per implementare un filtro passa-basso Exponential Moving Average (EMA) e sovrapporre il segnale filtrato al segnale con rumore e spike, puoi aggiungere una nuova funzione per calcolare l'EMA e poi utilizzarla per filtrare il segnale prima di stamparlo sulla console seriale. L'EMA è un tipo di media mobile ponderata che dà più peso ai dati più recenti, rendendola ideale per filtrare il rumore dai dati in tempo reale.

Ecco come potresti modificare ed estendere il tuo sketch:

```cpp
#include <Arduino.h>

// Parametri del segnale triangolare
const float valoreMin = 0;
const float valoreMax = 4096;  
const float passo = 5; // Velocità di cambiamento del segnale

// Variabile per la direzione del segnale (incremento o decremento)
bool incrementa = true;

// Variabile per il valore corrente del segnale
float valoreCorrente = valoreMin;

// Variabili per la gestione del tempo con millis()
unsigned long tempoPrecedente = 0;
const long intervallo = 10;

// Parametri per il filtro EMA
float emaSegnale = 0; // Valore iniziale dell'EMA
const float alpha = 0.1; // Fattore di smoothing (tra 0 e 1)

void aggiornaSegnaleTriangolare() {
  if (incrementa) {
    valoreCorrente += passo;
    if (valoreCorrente >= valoreMax) {
      incrementa = false;
    }
  } else {
    valoreCorrente -= passo;
    if (valoreCorrente <= valoreMin) {
      incrementa = true;
    }
  }
}

float aggiungiRumoreESpike(float segnale) {
  float rumore = random(-150, 150);
  segnale += rumore;

  if (random(0, 100) > 95) {
    segnale += random(-1300, 1300);
  }

  return segnale;
}

// Calcola l'EMA del segnale
float calcolaEMA(float nuovoValore) {
  emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
  return emaSegnale;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    aggiornaSegnaleTriangolare();

    float segnaleConRumore = aggiungiRumoreESpike(valoreCorrente);
    
    // Applica il filtro EMA al segnale con rumore
    float segnaleFiltrato = calcolaEMA(segnaleConRumore);

    // Stampa sia il segnale con rumore che quello filtrato
    Serial.print("Segnale con rumore: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | Segnale filtrato (EMA): ");
    Serial.println(segnaleFiltrato);
  }

  // Altre operazioni...
}
```



In questo aggiornamento, abbiamo introdotto: 
- **Parametri per il filtro EMA** : `emaSegnale` mantiene l'ultimo valore calcolato dell'EMA, mentre `alpha` è il fattore di smoothing che determina il peso dei nuovi valori nel calcolo dell'EMA. Un valore di `alpha` più alto dà più peso ai valori più recenti, rendendo il filtro più sensibile ai cambiamenti del segnale. 
- **calcolaEMA** : questa funzione aggiorna il valore dell'EMA basandosi sul nuovo valore del segnale. Utilizza il valore corrente dell'EMA e il nuovo valore del segnale per calcolare un nuovo EMA.

Il loop principale ora calcola sia il segnale con rumore e spike che il segnale filtrato attraverso l'EMA, e poi stampa entrambi i valori sulla console seriale. Questo ti permette di vedere sia l'effetto del rumore e degli spike sul segnale originale sia come il filtro EMA riesce a smussare tali effetti, offrendo una versione più pulita del segnale.


 Per aggiungere un filtro di media mobile (Moving Average Filter) al tuo sketch Arduino e sovrapporre il segnale in uscita filtrato con il segnale originale, devi prima definire una finestra di valori sui quali calcolare la media. Questo filtro calcola la media di un insieme di valori di ingresso per produrre ciascun valore di uscita, riducendo così il rumore casuale.

Di seguito, mostro come potresti estendere ulteriormente il tuo sketch per includere un filtro di media mobile, oltre al filtro EMA già implementato:

```cpp
#include <Arduino.h>

// Parametri del segnale triangolare
const float valoreMin = 0;
const float valoreMax = 4096;  
const float passo = 5; // Velocità di cambiamento del segnale

// Variabile per la direzione del segnale (incremento o decremento)
bool incrementa = true;

// Variabile per il valore corrente del segnale
float valoreCorrente = valoreMin;

// Variabili per la gestione del tempo con millis()
unsigned long tempoPrecedente = 0;
const long intervallo = 10;

// Parametri per il filtro EMA
float emaSegnale = 0;
const float alpha = 0.1;

// Parametri per il filtro di Media Mobile
const int lunghezzaFinestra = 10; // Lunghezza della finestra di valori per la media mobile
float valoriFinestra[10]; // Array per memorizzare i valori della finestra
int indiceValore = 0; // Indice per l'inserimento dei valori nell'array
float sommaValori = 0; // Somma dei valori nella finestra per calcolare la media

void aggiornaSegnaleTriangolare() {
  if (incrementa) {
    valoreCorrente += passo;
    if (valoreCorrente >= valoreMax) {
      incrementa = false;
    }
  } else {
    valoreCorrente -= passo;
    if (valoreCorrente <= valoreMin) {
      incrementa = true;
    }
  }
}

float aggiungiRumoreESpike(float segnale) {
  float rumore = random(-150, 150);
  segnale += rumore;

  if (random(0, 100) > 95) {
    segnale += random(-1300, 1300);
  }

  return segnale;
}

float calcolaEMA(float nuovoValore) {
  emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
  return emaSegnale;
}

float calcolaMediaMobile(float nuovoValore) {
  // Sottrai il valore più vecchio dalla somma totale e aggiungilo con il nuovo valore
  sommaValori -= valoriFinestra[indiceValore];
  sommaValori += nuovoValore;
  
  // Aggiorna l'array con il nuovo valore
  valoriFinestra[indiceValore] = nuovoValore;
  indiceValore = (indiceValore + 1) % lunghezzaFinestra;
  
  // Calcola la media mobile
  return sommaValori / lunghezzaFinestra;
}

void setup() {
  Serial.begin(115200);
  // Inizializza l'array dei valori della finestra
  for (int i = 0; i < lunghezzaFinestra; i++) {
    valoriFinestra[i] = 0;
  }
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    aggiornaSegnaleTriangolare();
    float segnaleConRumore = aggiungiRumoreESpike(valoreCorrente);
    
    // Applica il filtro EMA
    float segnaleFiltratoEMA = calcolaEMA(segnaleConRumore);
    
    // Applica il filtro di Media Mobile
    float segnaleFiltratoMM = calcolaMediaMobile(segnaleConRumore);

    // Stampa i segnali: originale, filtrato con EMA e filtrato con Media Mobile
    Serial.print("Segnale con rumore: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | Filtrato EMA: ");
    Serial.print(segnaleFiltratoEMA);
    Serial.print(" | Filtrato Media Mobile: ");
    Serial.println(segnaleFiltratoMM);
  }
}
```



In questo aggiornamento, abbiamo introdotto: 
- **Finestra di valori per la Media Mobile** : Un array `valoriFinestra` che memorizza gli ultimi `lunghezzaFinestra` valori del segnale. La `lunghezzaFinestra` determina il numero di valori inclusi nella media. 
- **calcolaMediaMobile** : Questa funzione aggiorna la somma dei valori nella finestra con il nuovo valore del segnale, calcola la nuova media mobile e restituisce il segnale filtrato.

Questo sketch calcola e stampa sia il segnale filtrato con l'EMA che quello filtrato con la media mobile, permettendoti di confrontare l'efficacia di ciascun metodo di filtraggio in tempo reale.


Per aggiungere un filtro mediano (Median Filter) al tuo sketch Arduino e sovrapporre il segnale filtrato con il segnale originale, dovrai implementare una logica per ordinare i valori all'interno di una finestra di dati e selezionare il valore mediano. Il filtro mediano è particolarmente efficace per rimuovere gli spike o i disturbi di breve durata dal segnale, mantenendo al contempo le variazioni rapide del segnale stesso.

Ecco come potresti estendere ulteriormente il tuo sketch per includere un filtro mediano, oltre ai filtri EMA e di media mobile già implementati:

```cpp
#include <Arduino.h>

// Parametri del segnale triangolare
const float valoreMin = 0;
const float valoreMax = 4096;  
const float passo = 5; // Velocità di cambiamento del segnale

// Variabile per la direzione del segnale (incremento o decremento)
bool incrementa = true;

// Variabile per il valore corrente del segnale
float valoreCorrente = valoreMin;

// Variabili per la gestione del tempo con millis()
unsigned long tempoPrecedente = 0;
const long intervallo = 10;

// Parametri per il filtro EMA
float emaSegnale = 0;
const float alpha = 0.1;

// Parametri per il filtro di Media Mobile
const int lunghezzaFinestraMM = 10; // Lunghezza della finestra di valori per la media mobile
float valoriFinestraMM[10]; // Array per memorizzare i valori della finestra
int indiceValoreMM = 0; // Indice per l'inserimento dei valori nell'array
float sommaValoriMM = 0; // Somma dei valori nella finestra per calcolare la media

// Parametri per il filtro mediano
const int lunghezzaFinestraMed = 5; // Lunghezza della finestra di valori per il filtro mediano
float valoriFinestraMed[5]; // Array per memorizzare i valori della finestra per il filtro mediano

void aggiornaSegnaleTriangolare() {
  if (incrementa) {
    valoreCorrente += passo;
    if (valoreCorrente >= valoreMax) {
      incrementa = false;
    }
  } else {
    valoreCorrente -= passo;
    if (valoreCorrente <= valoreMin) {
      incrementa = true;
    }
  }
}

float aggiungiRumoreESpike(float segnale) {
  float rumore = random(-150, 150);
  segnale += rumore;

  if (random(0, 100) > 95) {
    segnale += random(-1300, 1300);
  }

  return segnale;
}

float calcolaEMA(float nuovoValore) {
  emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
  return emaSegnale;
}

float calcolaMediaMobile(float nuovoValore) {
  sommaValoriMM -= valoriFinestraMM[indiceValoreMM];
  sommaValoriMM += nuovoValore;
  valoriFinestraMM[indiceValoreMM] = nuovoValore;
  indiceValoreMM = (indiceValoreMM + 1) % lunghezzaFinestraMM;
  return sommaValoriMM / lunghezzaFinestraMM;
}

// Funzione di supporto per ordinare l'array (implementazione semplice)
void ordinaArray(float arr[], int lunghezza) {
  for (int i = 0; i < lunghezza - 1; i++) {
    for (int j = 0; j < lunghezza - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        float temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

// Calcola il filtro mediano
float calcolaMediano(float nuovoValore) {
  // Inserisci il nuovo valore nell'array, sovrascrivendo il più vecchio se necessario
  static int indiceValoreMed = 0;
  valoriFinestraMed[indiceValoreMed] = nuovoValore;
  indiceValoreMed = (indiceValoreMed + 1) % lunghezzaFinestraMed;

  // Crea una copia dell'array per l'ordinamento
  float copiaArray[lunghezzaFinestraMed];
  for (int i = 0; i < lunghezzaFinestraMed; i++) {
    copiaArray[i] = valoriFinestraMed[i];
  }

  // Ordina l'array
  ordinaArray(copiaArray, lunghezzaFinestraMed);

  // Restituisce il valore mediano
  return copiaArray[lunghezzaFinestraMed / 2];
}

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < lunghezzaFinestraMM; i++) {
    valoriFinestraMM[i] = 0;
  }
  for (int i = 0; i < lunghezzaFinestraMed; i++) {
    valoriFinestraMed[i] = 0;
  }
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    aggiornaSegnaleTriangolare();
    float segnaleConRumore = aggiungiRumoreESpike(valoreCorrente);
    
    float segnaleFiltratoEMA = calcolaEMA(segnaleConRumore);
    float segnaleFiltratoMM = calcolaMediaMobile(segnaleConRumore);
    float segnaleFiltratoMediano = calcolaMediano(segnaleConRumore);

    // Stampa i segnali: con rumore, filtrato con EMA, filtrato con Media Mobile, e filtrato con Mediano
    Serial.print("Rumore: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | EMA: ");
    Serial.print(segnaleFiltratoEMA);
    Serial.print(" | MM: ");
    Serial.print(segnaleFiltratoMM);
    Serial.print(" | Mediano: ");
    Serial.println(segnaleFiltratoMediano);
  }
}
```



Questa versione dell'sketch introduce: 
- **Array e logica per il filtro mediano** : Viene creato un array `valoriFinestraMed` per memorizzare i valori utilizzati per calcolare il mediano. La funzione `calcolaMediano` aggiunge nuovi valori a questo array, ordina una copia dell'array e seleziona il valore mediano. 
- **ordinaArray** : Questa funzione è utilizzata per ordinare l'array dei valori prima di selezionare il valore mediano. L'ordinamento è necessario perché il filtro mediano funziona selezionando il valore centrale di un insieme di valori ordinati.

Ora il tuo sketch calcola e stampa i segnali filtrati usando tre metodi diversi (EMA, media mobile e mediano), permettendoti di confrontare l'efficacia di ciascun filtro nel ridurre il rumore mantenendo le caratteristiche del segnale originale.



Per organizzare meglio il codice e aggiungere un filtro FIR (Finite Impulse Response), possiamo raggruppare i parametri e le funzioni relative a ciascun tipo di filtro in strutture o classi separate. Questo approccio migliora la leggibilità e la manutenibilità del codice.

Inoltre, implementeremo un semplice filtro FIR. I filtri FIR utilizzano un set fisso di coefficienti (pesi) per filtrare il segnale. Questi coefficienti determinano le caratteristiche del filtro, come la banda di frequenza che permettono di passare.

Ecco un esempio di come potresti modificare il tuo sketch per includere un filtro FIR, oltre a organizzare meglio il codice:

```cpp
#include <Arduino.h>

// Struttura per gestire il segnale triangolare
struct SegnaleTriangolare {
  float valoreMin = 0;
  float valoreMax = 4096;
  float passo = 5;
  bool incrementa = true;
  float valoreCorrente = 0;
} segnaleTriangolare;

// Struttura per gestire il filtro EMA
struct FiltroEMA {
  float emaSegnale = 0;
  const float alpha = 0.1;
} filtroEMA;

// Struttura per gestire il filtro di Media Mobile
struct FiltroMediaMobile {
  static const int lunghezzaFinestra = 10;
  float valoriFinestra[lunghezzaFinestra] = {0};
  int indiceValore = 0;
  float sommaValori = 0;
} filtroMM;

// Struttura per gestire il filtro Mediano
struct FiltroMediano {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
} filtroMediano;

// Struttura per gestire il filtro FIR
struct FiltroFIR {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
  float coefficienti[lunghezzaFinestra] = {0.2, 0.2, 0.2, 0.2, 0.2}; // Esempio di coefficienti per un FIR passa-basso semplice
  int indiceValore = 0;
} filtroFIR;

// Prototipi delle funzioni
void aggiornaSegnaleTriangolare();
float aggiungiRumoreESpike(float segnale);
float calcolaEMA(float nuovoValore);
float calcolaMediaMobile(float nuovoValore);
float calcolaMediano(float nuovoValore);
float calcolaFIR(float nuovoValore);
void ordinaArray(float arr[], int lunghezza);

unsigned long tempoPrecedente = 0;
const long intervallo = 10;

void setup() {
  Serial.begin(115200);
  segnaleTriangolare.valoreCorrente = segnaleTriangolare.valoreMin;
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    aggiornaSegnaleTriangolare();
    float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
    
    float segnaleFiltratoEMA = calcolaEMA(segnaleConRumore);
    float segnaleFiltratoMM = calcolaMediaMobile(segnaleConRumore);
    float segnaleFiltratoMediano = calcolaMediano(segnaleConRumore);
    float segnaleFiltratoFIR = calcolaFIR(segnaleConRumore);

    Serial.print("Rumore: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | EMA: ");
    Serial.print(segnaleFiltratoEMA);
    Serial.print(" | MM: ");
    Serial.print(segnaleFiltratoMM);
    Serial.print(" | Mediano: ");
    Serial.print(segnaleFiltratoMediano);
    Serial.print(" | FIR: ");
    Serial.println(segnaleFiltratoFIR);
  }
}

// Qui dovresti implementare le funzioni aggiornaSegnaleTriangolare(), aggiungiRumoreESpike(), calcolaEMA(), calcolaMediaMobile(), calcolaMediano(), ordinaArray(), e la nuova funzione calcolaFIR()
// La funzione calcolaFIR() applica il filtro FIR al segnale.
```

Di seguito, troverai il codice completo con l'aggiunta del filtro FIR e l'organizzazione del codice per utilizzare strutture per ogni tipo di filtro, seguendo l'esempio introdotto precedentemente.

```cpp
#include <Arduino.h>

// Struttura per gestire il segnale triangolare
struct SegnaleTriangolare {
  float valoreMin = 0;
  float valoreMax = 4096;
  float passo = 5;
  bool incrementa = true;
  float valoreCorrente = valoreMin;

  void aggiorna() {
    if (incrementa) {
      valoreCorrente += passo;
      if (valoreCorrente >= valoreMax) {
        incrementa = false;
      }
    } else {
      valoreCorrente -= passo;
      if (valoreCorrente <= valoreMin) {
        incrementa = true;
      }
    }
  }
} segnaleTriangolare;

// Struttura per gestire il filtro EMA
struct FiltroEMA {
  float emaSegnale = 0;
  const float alpha = 0.1;

  float calcola(float nuovoValore) {
    emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
    return emaSegnale;
  }
} filtroEMA;

// Struttura per gestire il filtro di Media Mobile
struct FiltroMediaMobile {
  static const int lunghezzaFinestra = 10;
  float valoriFinestra[lunghezzaFinestra] = {0};
  int indiceValore = 0;
  float sommaValori = 0;

  float calcola(float nuovoValore) {
    sommaValori -= valoriFinestra[indiceValore];
    sommaValori += nuovoValore;
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    return sommaValori / lunghezzaFinestra;
  }
} filtroMM;

// Struttura per gestire il filtro Mediano
struct FiltroMediano {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
  int indiceValore = 0;

  float calcola(float nuovoValore) {
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    float valoriOrdinati[lunghezzaFinestra];
    memcpy(valoriOrdinati, valoriFinestra, sizeof(valoriOrdinati));
    ordinaArray(valoriOrdinati, lunghezzaFinestra);
    return valoriOrdinati[lunghezzaFinestra / 2];
  }

  static void ordinaArray(float arr[], int lunghezza) {
    for (int i = 0; i < lunghezza - 1; i++) {
      for (int j = 0; j < lunghezza - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          float temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }
} filtroMediano;

// Struttura per gestire il filtro FIR
struct FiltroFIR {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
  float coefficienti[lunghezzaFinestra] = {0.2, 0.2, 0.2, 0.2, 0.2}; // Esempio semplice di coefficienti per un FIR passa-basso
  int indiceValore = 0;

  float calcola(float nuovoValore) {
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    float risultato = 0;
    for (int i = 0; i < lunghezzaFinestra; i++) {
      risultato += valoriFinestra[(indiceValore + i) % lunghezzaFinestra] * coefficienti[i];
    }
    return risultato;
  }
} filtroFIR;

unsigned long tempoPrecedente = 0;
const long intervallo = 10;

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    segnaleTriangolare.aggiorna();
    float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
    
    float segnaleFiltratoEMA = filtroEMA.calcola(segnaleConRumore);
    float segnaleFiltratoMM = filtroMM.calcola(segnaleConRumore);
    float segnaleFiltratoMediano = filtroMediano.calcola(segnaleConRumore);
    float segnaleFiltratoFIR = filtroFIR.calcola(segnaleConRumore);

    Serial.print("Rumore: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | EMA: ");
    Serial.print(segnaleFiltratoEMA);
    Serial.print(" | MM: ");
    Serial.print(segnaleFiltratoMM);
    Serial.print(" | Mediano: ");
    Serial.print(segnaleFiltratoMediano);
    Serial.print(" | FIR: ");
    Serial.println(segnaleFiltratoFIR);
  }
}

float aggiungiRumoreESpike(float segnale) {
  float rumore = random(-150, 150);
  segnale += rumore;
  if (random(0, 100) > 95) {
    segnale += random(-1300, 1300);
  }
  return segnale;
}
```



Questo codice organizza ogni filtro e la logica di generazione del segnale in strutture separate, migliorando la modularità e la chiarezza. Ogni struttura ha i suoi parametri e metodi per elaborare i dati, rendendo il codice più organizzato e facilmente estensibile.

Il filtro FIR è implementato nella struttura `FiltroFIR` con un semplice set di coefficienti che rappresentano un filtro passa-basso. Puoi modificare i coefficienti del filtro FIR per adattarlo alle tue specifiche esigenze di filtraggio.


L'aggiunta di un filtro passa-basso di Butterworth nel contesto di un programma Arduino richiede un approccio un po' diverso rispetto ai filtri digitali semplici come media mobile, mediana o FIR, principalmente perché il filtro di Butterworth è tipicamente definito in termini di funzione di trasferimento analogica. Tuttavia, possiamo approssimare il comportamento di un filtro di Butterworth utilizzando un approccio digitale.

Uno dei modi per implementare un filtro di Butterworth digitale in un ambiente come Arduino è utilizzare la trasformazione bilineare per convertire la funzione di trasferimento analogica in una digitale. Questo processo può essere complesso e al di fuori delle capacità di calcolo di alcuni microcontroller, soprattutto se si desidera un filtro di ordine elevato.

Per mantenere le cose semplici e pratiche, mostrerò come aggiungere un semplice filtro di Butterworth passa-basso del primo ordine utilizzando un approccio approssimativo che può essere eseguito su Arduino senza eccessivo carico computazionale.

Aggiungeremo una nuova struttura per il filtro di Butterworth nel codice esistente:

```cpp
struct FiltroButterworth {
    float y1 = 0; // Output precedente
    float x1 = 0; // Input precedente
    float a = 0.1; // Coefficiente di smoothing, dipende dalla frequenza di taglio desiderata

    float calcola(float x0) {
        // Implementazione di un filtro passa-basso del primo ordine
        float y0 = y1 + a * (x0 - x1);
        x1 = x0;
        y1 = y0;
        return y0;
    }
} filtroButterworth;
```



In questo esempio, il coefficiente `a` determina l'effetto del filtro, influenzando direttamente la frequenza di taglio. Questo valore dovrebbe essere scelto in base alla frequenza di campionamento del tuo segnale e alla frequenza di taglio desiderata. Un valore più basso di `a` porta a una maggiore attenuazione delle alte frequenze.

Per includere il filtro di Butterworth nel loop principale e applicarlo al segnale:

```cpp
void loop() {
    unsigned long tempoAttuale = millis();
    if (tempoAttuale - tempoPrecedente >= intervallo) {
        tempoPrecedente = tempoAttuale;

        segnaleTriangolare.aggiorna();
        float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
        
        float segnaleFiltratoEMA = filtroEMA.calcola(segnaleConRumore);
        float segnaleFiltratoMM = filtroMM.calcola(segnaleConRumore);
        float segnaleFiltratoMediano = filtroMediano.calcola(segnaleConRumore);
        float segnaleFiltratoFIR = filtroFIR.calcola(segnaleConRumore);
        float segnaleFiltratoButterworth = filtroButterworth.calcola(segnaleConRumore);

        Serial.print("Rumore: ");
        Serial.print(segnaleConRumore);
        Serial.print(" | EMA: ");
        Serial.print(segnaleFiltratoEMA);
        Serial.print(" | MM: ");
        Serial.print(segnaleFiltratoMM);
        Serial.print(" | Mediano: ");
        Serial.print(segnaleFiltratoMediano);
        Serial.print(" | FIR: ");
        Serial.print(segnaleFiltratoFIR);
        Serial.print(" | Butterworth: ");
        Serial.println(segnaleFiltratoButterworth);
    }
}
```



Questo approccio al filtro di Butterworth è piuttosto semplificato e serve principalmente per fornire un'introduzione all'idea di filtraggio passa-basso senza addentrarsi nelle complessità della progettazione dei filtri digitali. Per applicazioni più critiche o per filtri di ordine superiore, si consiglia di utilizzare librerie specifiche che possono gestire la trasformazione e l'implementazione in modo più accurato.


L'aggiunta di un filtro di Kalman a un progetto Arduino può migliorare significativamente la stima dello stato di un sistema dinamico soggetto a rumore. Il filtro di Kalman è un algoritmo ricorsivo che stima lo stato di un sistema lineare dinamico dall'insieme di misurazioni rumorose. È molto utilizzato in applicazioni di navigazione, tracciamento di oggetti e controllo. La sua implementazione richiede la conoscenza del modello del sistema, comprese le matrici che descrivono la dinamica del sistema, la covarianza del rumore di processo e la covarianza del rumore di misurazione.

Per semplicità, qui viene mostrata un'implementazione di base del filtro di Kalman per un singolo stato. Questo esempio può essere adattato e ampliato in base alle specifiche esigenze del tuo progetto.

Prima di tutto, definiamo una struttura per il filtro di Kalman:

```cpp
struct FiltroKalman {
    float q; // Process noise covariance
    float r; // Measurement noise covariance
    float x; // Valore stimato
    float p; // Covarianza dell'errore di stima
    float k; // Guadagno di Kalman

    FiltroKalman(float process_noise, float measurement_noise, float estimated_error, float initial_value) {
        q = process_noise;
        r = measurement_noise;
        p = estimated_error;
        x = initial_value; // Il valore iniziale può essere una stima o una misurazione diretta
    }

    float update(float measurement) {
        // Predizione
        p = p + q;

        // Aggiornamento
        k = p / (p + r);
        x = x + k * (measurement - x);
        p = (1 - k) * p;

        return x;
    }
};
```



In questo esempio, `q` rappresenta la varianza del rumore di processo (quanto ci si aspetta che il vero stato vari nel tempo), mentre `r` rappresenta la varianza del rumore di misurazione (quanto sono affidabili le misurazioni). `x` è lo stato stimato attuale del sistema, `p` è la stima dell'errore (covarianza), e `k` è il guadagno di Kalman.

Per utilizzare il filtro di Kalman nel loop principale e applicarlo a un segnale:

```cpp
// Inizializza il filtro di Kalman con valori esemplificativi
FiltroKalman filtroKalman(0.01, 0.1, 1, 0);

void loop() {
    unsigned long tempoAttuale = millis();
    if (tempoAttuale - tempoPrecedente >= intervallo) {
        tempoPrecedente = tempoAttuale;

        segnaleTriangolare.aggiorna();
        float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
        
        float segnaleFiltratoEMA = filtroEMA.calcola(segnaleConRumore);
        float segnaleFiltratoMM = filtroMM.calcola(segnaleConRumore);
        float segnaleFiltratoMediano = filtroMediano.calcola(segnaleConRumore);
        float segnaleFiltratoFIR = filtroFIR.calcola(segnaleConRumore);
        float segnaleFiltratoButterworth = filtroButterworth.calcola(segnaleConRumore);
        float segnaleFiltratoKalman = filtroKalman.update(segnaleConRumore);

        Serial.print("Rumore: ");
        Serial.print(segnaleConRumore);
        Serial.print(" | EMA: ");
        Serial.print(segnaleFiltratoEMA);
        Serial.print(" | MM: ");
        Serial.print(segnaleFiltratoMM);
        Serial.print(" | Mediano: ");
        Serial.print(segnaleFiltratoMediano);
        Serial.print(" | FIR: ");
        Serial.print(segnaleFiltratoFIR);
        Serial.print(" | Butterworth: ");
        Serial.print(segnaleFiltratoButterworth);
        Serial.print(" | Kalman: ");
        Serial.println(segnaleFiltratoKalman);
    }
}
```



Ricorda che i valori iniziali e i parametri `q` e `r` del filtro di Kalman dovrebbero essere scelti con cura in base alla natura specifica del tuo sistema e del rumore che intendi filtr


Per permettere la selezione di un filtro desiderato o una combinazione di filtri, possiamo introdurre una serie di flag (o una variabile di configurazione) che consentano all'utente di specificare quali filtri applicare. Questo può essere fatto impostando delle variabili booleane per ogni filtro, che possono essere attivate o disattivate in base alle esigenze.

Ecco un esempio di come potresti strutturare il tuo codice per permettere questa selezione:

```cpp
#include <Arduino.h>

// Definisci qui tutte le strutture dei filtri come mostrato in precedenza
// ...

// Flag per l'attivazione dei filtri
bool usaEMA = true;
bool usaMM = true;
bool usaMediano = false;
bool usaFIR = false;
bool usaButterworth = false;
bool usaKalman = false;

// Inizializza i filtri come mostrato in precedenza
// ...

void setup() {
  Serial.begin(115200);
  // Configura qui i filtri in base alle esigenze iniziali
}

void loop() {
    unsigned long tempoAttuale = millis();
    if (tempoAttuale - tempoPrecedente >= intervallo) {
        tempoPrecedente = tempoAttuale;

        segnaleTriangolare.aggiorna();
        float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
        float segnaleFiltrato = segnaleConRumore; // Inizia con il segnale originale

        // Applica i filtri selezionati
        if (usaEMA) {
            segnaleFiltrato = filtroEMA.calcola(segnaleFiltrato);
        }
        if (usaMM) {
            segnaleFiltrato = filtroMM.calcola(segnaleFiltrato);
        }
        if (usaMediano) {
            segnaleFiltrato = filtroMediano.calcola(segnaleFiltrato);
        }
        if (usaFIR) {
            segnaleFiltrato = filtroFIR.calcola(segnaleFiltrato);
        }
        if (usaButterworth) {
            segnaleFiltrato = filtroButterworth.calcola(segnaleFiltrato);
        }
        if (usaKalman) {
            segnaleFiltrato = filtroKalman.update(segnaleFiltrato);
        }

        // Stampa il segnale originale e il segnale filtrato
        Serial.print("Originale: ");
        Serial.print(segnaleConRumore);
        Serial.print(" | Filtrato: ");
        Serial.println(segnaleFiltrato);
    }
}
```



Questo approccio consente di attivare o disattivare facilmente i vari filtri modificando i valori delle variabili booleane. Potresti anche aggiungere un'interfaccia utente semplice tramite la console seriale o pulsanti fisici sull'hardware Arduino per modificare queste impostazioni in tempo reale.

Ricorda di inizializzare tutti i filtri nel `setup()` e di aggiornare le variabili di controllo (`tempoPrecedente`, ecc.) come necessario per il tuo specifico caso d'uso. Questo esempio assume che ogni filtro sia indipendente e che l'output di un filtro possa essere l'input del successivo, ma potresti dover adattare la logica di processing in base alle caratteristiche specifiche dei segnali che stai lavorando e agli effetti combinati dei filtri che scegli di utilizzare.

--------
--------
```cpp


#include <Arduino.h>

// Struttura per gestire il segnale triangolare
struct SegnaleTriangolare {
  float valoreMin = 0;
  float valoreMax = 4096;
  float passo = 5;
  bool incrementa = true;
  float valoreCorrente = valoreMin;

  void aggiorna() {
    if (incrementa) {
      valoreCorrente += passo;
      if (valoreCorrente >= valoreMax) {
        incrementa = false;
      }
    } else {
      valoreCorrente -= passo;
      if (valoreCorrente <= valoreMin) {
        incrementa = true;
      }
    }
  }
} segnaleTriangolare;

float aggiungiRumoreESpike(float segnale) {
  float rumore = random(-150, 150);
  segnale += rumore;
  if (random(0, 100) > 95) {
    segnale += random(-1300, 1300);
  }
  return segnale;
}


// Struttura per gestire il filtro EMA
struct FiltroEMA {
  float emaSegnale = 0;
  const float alpha = 0.1;

  float calcola(float nuovoValore) {
    emaSegnale = alpha * nuovoValore + (1 - alpha) * emaSegnale;
    return emaSegnale;
  }
} filtroEMA;

// Struttura per gestire il filtro di Media Mobile
struct FiltroMediaMobile {
  static const int lunghezzaFinestra = 10;
  float valoriFinestra[lunghezzaFinestra] = {0};
  int indiceValore = 0;
  float sommaValori = 0;

  float calcola(float nuovoValore) {
    sommaValori -= valoriFinestra[indiceValore];
    sommaValori += nuovoValore;
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    return sommaValori / lunghezzaFinestra;
  }
} filtroMM;

// Struttura per gestire il filtro Mediano
struct FiltroMediano {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
  int indiceValore = 0;

  float calcola(float nuovoValore) {
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    float valoriOrdinati[lunghezzaFinestra];
    memcpy(valoriOrdinati, valoriFinestra, sizeof(valoriOrdinati));
    ordinaArray(valoriOrdinati, lunghezzaFinestra);
    return valoriOrdinati[lunghezzaFinestra / 2];
  }

  static void ordinaArray(float arr[], int lunghezza) {
    for (int i = 0; i < lunghezza - 1; i++) {
      for (int j = 0; j < lunghezza - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          float temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }
} filtroMediano;

// Struttura per gestire il filtro FIR
struct FiltroFIR {
  static const int lunghezzaFinestra = 5;
  float valoriFinestra[lunghezzaFinestra] = {0};
  float coefficienti[lunghezzaFinestra] = {0.2, 0.2, 0.2, 0.2, 0.2}; // Esempio semplice di coefficienti per un FIR passa-basso
  int indiceValore = 0;

  float calcola(float nuovoValore) {
    valoriFinestra[indiceValore] = nuovoValore;
    indiceValore = (indiceValore + 1) % lunghezzaFinestra;
    float risultato = 0;
    for (int i = 0; i < lunghezzaFinestra; i++) {
      risultato += valoriFinestra[(indiceValore + i) % lunghezzaFinestra] * coefficienti[i];
    }
    return risultato;
  }
} filtroFIR;


struct FiltroButterworth {
  float y1 = 0; // Output precedente
  float x1 = 0; // Input precedente
  float a = 0.1; // Coefficiente di smoothing, dipende dalla frequenza di taglio desiderata

  float calcola(float x0) {
    // Implementazione di un filtro passa-basso del primo ordine
    float y0 = y1 + a * (x0 - x1);
    x1 = x0;
    y1 = y0;
    return y0;
  }
} filtroButterworth;


struct FiltroKalman {
  float q; // Process noise covariance
  float r; // Measurement noise covariance
  float x; // Valore stimato
  float p; // Covarianza dell'errore di stima
  float k; // Guadagno di Kalman

  FiltroKalman(float process_noise, float measurement_noise, float estimated_error, float initial_value) {
    q = process_noise;
    r = measurement_noise;
    p = estimated_error;
    x = initial_value; // Il valore iniziale può essere una stima o una misurazione diretta
  }

  float update(float measurement) {
    // Predizione
    p = p + q;

    // Aggiornamento
    k = p / (p + r);
    x = x + k * (measurement - x);
    p = (1 - k) * p;

    return x;
  }
};
// Inizializza il filtro di Kalman con valori esemplificativi
FiltroKalman filtroKalman(0.01, 0.1, 1, 0);



// Flag per l'attivazione dei filtri
bool usaEMA = false;
bool usaMM = false;
bool usaMediano = false;
bool usaFIR = false;
bool usaButterworth = false;
bool usaKalman = true;


unsigned long tempoPrecedente = 0;
const long intervallo = 10;

void setup() {
  Serial.begin(115200);
}

void loop() {
  unsigned long tempoAttuale = millis();
  if (tempoAttuale - tempoPrecedente >= intervallo) {
    tempoPrecedente = tempoAttuale;

    segnaleTriangolare.aggiorna();
    float segnaleConRumore = aggiungiRumoreESpike(segnaleTriangolare.valoreCorrente);
    /*
        float segnaleFiltratoEMA = filtroEMA.calcola(segnaleConRumore);
        float segnaleFiltratoMM = filtroMM.calcola(segnaleConRumore);
        float segnaleFiltratoMediano = filtroMediano.calcola(segnaleConRumore);
        float segnaleFiltratoFIR = filtroFIR.calcola(segnaleConRumore);
        float segnaleFiltratoButterworth = filtroButterworth.calcola(segnaleConRumore);
        float segnaleFiltratoKalman = filtroKalman.update(segnaleConRumore);

        Serial.print("Rumore: ");
        Serial.print(segnaleConRumore);
        Serial.print(" | EMA: ");
        Serial.print(segnaleFiltratoEMA);
        Serial.print(" | MM: ");
        Serial.print(segnaleFiltratoMM);
        Serial.print(" | Mediano: ");
        Serial.print(segnaleFiltratoMediano);
        Serial.print(" | FIR: ");
        Serial.print(segnaleFiltratoFIR);
        Serial.print(" | Butterworth: ");
        Serial.print(segnaleFiltratoButterworth);
        Serial.print(" | Kalman: ");
        Serial.println(segnaleFiltratoKalman);

    */

    float segnaleFiltrato = segnaleConRumore; // Inizia con il segnale originale

    // Applica i filtri selezionati
    if (usaEMA) {
      segnaleFiltrato = filtroEMA.calcola(segnaleFiltrato);
    }
    if (usaMM) {
      segnaleFiltrato = filtroMM.calcola(segnaleFiltrato);
    }
    if (usaMediano) {
      segnaleFiltrato = filtroMediano.calcola(segnaleFiltrato);
    }
    if (usaFIR) {
      segnaleFiltrato = filtroFIR.calcola(segnaleFiltrato);
    }
    if (usaButterworth) {
      segnaleFiltrato = filtroButterworth.calcola(segnaleFiltrato);
    }
    if (usaKalman) {
      segnaleFiltrato = filtroKalman.update(segnaleFiltrato);
    }

    // Stampa il segnale originale e il segnale filtrato
    Serial.print("Originale: ");
    Serial.print(segnaleConRumore);
    Serial.print(" | Filtrato: ");
    Serial.println(segnaleFiltrato);

  }
}
```
--------
--------
