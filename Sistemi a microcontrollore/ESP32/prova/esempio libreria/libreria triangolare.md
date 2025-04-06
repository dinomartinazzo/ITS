Per creare una libreria che genera un segnale triangolare, seguiremo un approccio simile a quello usato per i filtri. Questa libreria permetterà di specificare i parametri del segnale, come il valore minimo e massimo, e il passo di incremento/decremento, rendendola flessibile per diversi usi.
### Passo 1: Creare il File Header (GeneratoreSegnaleTriangolare.h)

```cpp
// GeneratoreSegnaleTriangolare.h
#ifndef GeneratoreSegnaleTriangolare_h
#define GeneratoreSegnaleTriangolare_h

class GeneratoreSegnaleTriangolare {
  public:
    GeneratoreSegnaleTriangolare(float valoreMin, float valoreMax, float passo);
    float genera(); // Metodo per generare il prossimo valore del segnale
  private:
    float valoreMin;
    float valoreMax;
    float passo;
    float valoreCorrente;
    bool incrementa;
};

#endif
```


### Passo 2: Creare il File di Implementazione (GeneratoreSegnaleTriangolare.cpp)

```cpp
// GeneratoreSegnaleTriangolare.cpp
#include "GeneratoreSegnaleTriangolare.h"

GeneratoreSegnaleTriangolare::GeneratoreSegnaleTriangolare(float valoreMin, float valoreMax, float passo) {
  this->valoreMin = valoreMin;
  this->valoreMax = valoreMax;
  this->passo = passo;
  valoreCorrente = valoreMin;
  incrementa = true;
}

float GeneratoreSegnaleTriangolare::genera() {
  if (incrementa) {
    valoreCorrente += passo;
    if (valoreCorrente >= valoreMax) {
      incrementa = false;
      valoreCorrente = valoreMax; // Assicura che il valore non superi il massimo
    }
  } else {
    valoreCorrente -= passo;
    if (valoreCorrente <= valoreMin) {
      incrementa = true;
      valoreCorrente = valoreMin; // Assicura che il valore non scenda sotto il minimo
    }
  }
  return valoreCorrente;
}
```


### Esempio di Utilizzo nel Tuo Sketch

```cpp
#include <GeneratoreSegnaleTriangolare.h>

// Crea un'istanza del generatore con valore minimo 0, massimo 4096 e passo 5
GeneratoreSegnaleTriangolare generatore(0, 4096, 5);

void setup() {
  Serial.begin(115200);
}

void loop() {
  float valoreSegnale = generatore.genera(); // Genera il prossimo valore del segnale
  Serial.println(valoreSegnale); // Stampa il valore generato
  delay(10); // Aspetta un po' prima di generare il prossimo valore
}
```


### Istruzioni per l'Uso 
- Posiziona i file `GeneratoreSegnaleTriangolare.h` e `GeneratoreSegnaleTriangolare.cpp` nella directory delle librerie del tuo ambiente Arduino, seguendo la struttura della cartella proposta nelle risposte precedenti. 
- Includi la libreria nel tuo sketch Arduino usando `#include <GeneratoreSegnaleTriangolare.h>`.
- Crea un'istanza del generatore specificando i parametri desiderati. 
- Chiama il metodo `genera()` per ottenere il prossimo valore del segnale triangolare.

Questa libreria fornisce un modo semplice e flessibile per generare segnali triangolari in progetti Arduino, utile per testare filtri o per altre applicazioni che richiedono un segnale di questo tipo.


Per creare una libreria che genera un segnale sinusoidale, seguiremo un approccio simile a quello adottato per il segnale triangolare, ma con le modifiche necessarie per produrre un'onda sinusoidale. Questa libreria permetterà di specificare i parametri del segnale come la frequenza, l'ampiezza e la fase, rendendola versatile per diversi usi.
### Passo 1: Creare il File Header (GeneratoreSegnaleSinusoidale.h)

```cpp
// GeneratoreSegnaleSinusoidale.h
#ifndef GeneratoreSegnaleSinusoidale_h
#define GeneratoreSegnaleSinusoidale_h

#include "Arduino.h"

class GeneratoreSegnaleSinusoidale {
  public:
    GeneratoreSegnaleSinusoidale(float ampiezza, float frequenza, float fase, unsigned long intervalloCampione);
    float genera();
  private:
    float ampiezza;
    float frequenza;
    float fase;
    unsigned long intervalloCampione; // Intervallo di tempo tra i campioni in millisecondi
    unsigned long ultimoTempo; // Ultimo momento in cui è stato generato un valore
    float angolo; // Angolo corrente per la generazione del segnale
};

#endif
```


### Passo 2: Creare il File di Implementazione (GeneratoreSegnaleSinusoidale.cpp)

```cpp
// GeneratoreSegnaleSinusoidale.cpp
#include "GeneratoreSegnaleSinusoidale.h"

GeneratoreSegnaleSinusoidale::GeneratoreSegnaleSinusoidale(float ampiezza, float frequenza, float fase, unsigned long intervalloCampione) {
  this->ampiezza = ampiezza;
  this->frequenza = frequenza;
  this->fase = fase;
  this->intervalloCampione = intervalloCampione;
  ultimoTempo = 0;
  angolo = 0.0;
}

float GeneratoreSegnaleSinusoidale::genera() {
  unsigned long tempoCorrente = millis();
  if (tempoCorrente - ultimoTempo >= intervalloCampione) {
    ultimoTempo = tempoCorrente;
    // Calcola il nuovo valore del segnale sinusoidale
    float valore = ampiezza * sin(2 * PI * frequenza * (tempoCorrente / 1000.0) + fase);
    return valore;
  }
  return ampiezza * sin(angolo); // Restituisce il valore corrente se non è ancora tempo per il nuovo campione
}
```


### Esempio di Utilizzo nel Tuo Sketch

```cpp
#include <GeneratoreSegnaleSinusoidale.h>

// Crea un'istanza del generatore con ampiezza 1.0, frequenza 1Hz, fase 0 e intervallo campione 100ms
GeneratoreSegnaleSinusoidale generatore(1.0, 1.0, 0.0, 100);

void setup() {
  Serial.begin(115200);
}

void loop() {
  float valoreSegnale = generatore.genera(); // Genera il prossimo valore del segnale
  Serial.println(valoreSegnale); // Stampa il valore generato
  delay(100); // Aspetta un po' prima di generare il prossimo valore
}
```


### Istruzioni per l'Uso 
- Posiziona i file `GeneratoreSegnaleSinusoidale.h` e `GeneratoreSegnaleSinusoidale.cpp` nella directory delle librerie del tuo ambiente Arduino. 
- Includi la libreria nel tuo sketch Arduino usando `#include <GeneratoreSegnaleSinusoidale.h>`.
- Crea un'istanza del generatore specificando i parametri desiderati come ampiezza, frequenza, fase e intervallo tra i campioni. 
- Chiama il metodo `genera()` per ottenere il prossimo valore del segnale sinusoidale.

Questa libreria offre un modo semplice e flessibile per generare segnali sinusoidali in progetti Arduino, utile per simulazioni, test di filtri, o qualsiasi applicazione che richieda un segnale periodico di questo tipo.