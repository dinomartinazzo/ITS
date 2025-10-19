# Modulo 2: Variabili e Tipi di Dato
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Capire cosa sono le variabili
- Usare i tipi di dato fondamentali (int, float, char)
- Dichiarare e inizializzare variabili
- Fare operazioni matematiche semplici
- Leggere input dall'utente

---

## 2.1 Che cosa sono le Variabili?

Una **variabile** è come una **scatola con un'etichetta** dove puoi mettere un valore.

### Analogia della vita reale:
```
┌─────────────────┐
│     SCATOLA     │  ← Questa è la variabile "eta"
│       19        │  ← Questo è il valore dentro
└─────────────────┘
```

### Nel programma:
```c
int eta = 19;    // Creo una scatola chiamata "eta" e ci metto 19
```

**Perché sono utili?**
- Puoi cambiare il valore quando vuoi
- Puoi usare lo stesso valore più volte
- Rendi il programma più flessibile

---

## 2.2 I Tipi di Dato Principali

Come le scatole hanno dimensioni diverse, le variabili hanno **tipi** diversi:

### 🔢 `int` - Numeri Interi
```c
int eta = 19;
int studenti = 25;
int temperatura = -5;
```
- Contiene: numeri senza virgola (-100, 0, 42, 1000)
- Range: circa da -2 miliardi a +2 miliardi

### 💰 `float` - Numeri Decimali  
```c
float prezzo = 29.99;
float altezza = 1.75;
float media = 7.5;
```
- Contiene: numeri con la virgola (3.14, -2.5, 0.1)
- Precisione: circa 6-7 cifre decimali

### 📝 `char` - Caratteri
```c
char lettera = 'A';
char voto = 'B';
char risposta = 'S';
```
- Contiene: un singolo carattere
- Si scrive sempre tra apici singoli `' '`

---

## 2.3 Dichiarazione e Inizializzazione

### Metodo 1: Prima dichiari, poi assegni
```c
#include <stdio.h>

int main() {
    int numero;        // Dichiaro la variabile
    numero = 42;       // Assegno il valore
    
    printf("Il numero è: %d\n", numero);
    return 0;
}
```

### Metodo 2: Dichiari e assegni insieme
```c
#include <stdio.h>

int main() {
    int numero = 42;   // Tutto in una riga
    
    printf("Il numero è: %d\n", numero);
    return 0;
}
```

### Più variabili insieme:
```c
#include <stdio.h>

int main() {
    int a = 10, b = 20, c = 30;    // Tre variabili insieme
    
    printf("a=%d, b=%d, c=%d\n", a, b, c);
    return 0;
}
```

---

## 2.4 Come Stampare le Variabili

Ogni tipo ha il suo **codice speciale** per la stampa:

```c
#include <stdio.h>

int main() {
    int eta = 19;
    float altezza = 1.75;
    char iniziale = 'M';
    
    printf("Eta: %d anni\n", eta);           // %d per int
    printf("Altezza: %.2f metri\n", altezza); // %f per float
    printf("Iniziale: %c\n", iniziale);      // %c per char
    
    return 0;
}
```

**Risultato:**
```
Eta: 19 anni
Altezza: 1.75 metri
Iniziale: M
```

### 🎨 Trucchi di Formattazione:
- `%.1f` = 1 cifra dopo la virgola (3.1)
- `%.2f` = 2 cifre dopo la virgola (3.14)
- `%5d` = almeno 5 spazi per il numero (   42)

---

## 2.5 Operatori Matematici

### Operatori Base:
```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 3;
    
    printf("a + b = %d\n", a + b);    // Addizione: 13
    printf("a - b = %d\n", a - b);    // Sottrazione: 7
    printf("a * b = %d\n", a * b);    // Moltiplicazione: 30
    printf("a / b = %d\n", a / b);    // Divisione: 3 (parte intera)
    printf("a %% b = %d\n", a % b);    // Resto: 1
    
    return 0;
}
```

### 🚨 Attenzione alla Divisione!
```c
#include <stdio.h>

int main() {
    int risultato1 = 7 / 2;      // Risultato: 3 (perde la parte decimale)
    float risultato2 = 7.0 / 2;  // Risultato: 3.5 (mantiene i decimali)
    
    printf("7 / 2 (int) = %d\n", risultato1);
    printf("7.0 / 2 (float) = %.1f\n", risultato2);
    
    return 0;
}
```

---

## 2.6 Leggere Input dall'Utente

Usa `scanf()` per far inserire dati all'utente:

### Esempio Semplice:
```c
#include <stdio.h>

int main() {
    int eta;
    
    printf("Quanti anni hai? ");
    scanf("%d", &eta);              // Legge un numero intero
    
    printf("Hai %d anni!\n", eta);
    
    return 0;
}
```

### 🔍 Nota Importante:
- `scanf` usa `&` prima del nome della variabile
- `&eta` significa "metti il valore nella scatola chiamata eta"

### Input Multipli:
```c
#include <stdio.h>

int main() {
    int giorno, mese, anno;
    
    printf("Inserisci la tua data di nascita (gg mm aaaa): ");
    scanf("%d %d %d", &giorno, &mese, &anno);
    
    printf("Sei nato il %d/%d/%d\n", giorno, mese, anno);
    
    return 0;
}
```

---

## 2.7 Esercizi Pratici

### 🎯 Esercizio 2.1: Calcolatore dell'Età
```c
#include <stdio.h>

int main() {
    int anno_nascita, anno_corrente, eta;
    
    printf("In che anno sei nato? ");
    scanf("%d", &anno_nascita);
    
    printf("In che anno siamo? ");
    scanf("%d", &anno_corrente);
    
    eta = anno_corrente - anno_nascita;
    
    printf("Hai circa %d anni!\n", eta);
    
    return 0;
}
```

### 🎯 Esercizio 2.2: Calcolatrice Semplice
```c
#include <stdio.h>

int main() {
    float numero1, numero2, somma;
    
    printf("Inserisci primo numero: ");
    scanf("%f", &numero1);
    
    printf("Inserisci secondo numero: ");
    scanf("%f", &numero2);
    
    somma = numero1 + numero2;
    
    printf("%.1f + %.1f = %.1f\n", numero1, numero2, somma);
    
    return 0;
}
```

### 🎯 Esercizio 2.3: Convertitore Euro-Dollari
```c
#include <stdio.h>

int main() {
    float euro, dollari;
    float cambio = 1.1;  // 1 euro = 1.1 dollari (esempio)
    
    printf("Inserisci l'importo in euro: ");
    scanf("%f", &euro);
    
    dollari = euro * cambio;
    
    printf("%.2f euro = %.2f dollari\n", euro, dollari);
    
    return 0;
}
```

---

## 2.8 Errori Comuni e Soluzioni

### ❌ Errore: Variabile non dichiarata
```c
// SBAGLIATO:
printf("%d", numero);  // numero non esiste!

// GIUSTO:
int numero = 42;
printf("%d", numero);
```

### ❌ Errore: Tipo sbagliato in printf
```c
// SBAGLIATO:
int numero = 42;
printf("%f", numero);  // Usa %f per int!

// GIUSTO:
int numero = 42;
printf("%d", numero);  // Usa %d per int
```

### ❌ Errore: Dimenticare & in scanf
```c
// SBAGLIATO:
scanf("%d", numero);

// GIUSTO:
scanf("%d", &numero);
```

---

## 2.9 Nomi delle Variabili

### ✅ Nomi Validi:
```c
int eta;
int numeroStudenti;
int numero_telefono;
int x, y, z;
int counter1, counter2;
```

### ❌ Nomi Non Validi:
```c
int 2nome;        // Non può iniziare con numero
int numero-casa;  // Non può contenere -
int int;          // Non può essere una parola riservata
```

### 💡 Consigli per Nomi:
- Usa nomi **significativi**: `eta` invece di `x`
- Usa **camelCase**: `numeroStudenti`
- O usa **underscore**: `numero_studenti`
- Sii **coerente** nel tuo stile

---

## 2.10 Costanti

Per valori che **non cambiano mai**, usa le costanti:

```c
#include <stdio.h>

#define PI 3.14159
#define MAX_STUDENTI 30

int main() {
    float raggio = 5.0;
    float area = PI * raggio * raggio;
    
    printf("L'area del cerchio è: %.2f\n", area);
    printf("La classe può avere massimo %d studenti\n", MAX_STUDENTI);
    
    return 0;
}
```

---

## 🎯 Progetto del Modulo: "Calcolatore BMI"

Crea un programma che calcoli il BMI (Body Mass Index):

```c
#include <stdio.h>

int main() {
    float peso, altezza, bmi;
    
    printf("=== CALCOLATORE BMI ===\n");
    
    printf("Inserisci il tuo peso (kg): ");
    scanf("%f", &peso);
    
    printf("Inserisci la tua altezza (metri): ");
    scanf("%f", &altezza);
    
    bmi = peso / (altezza * altezza);
    
    printf("\n--- RISULTATO ---\n");
    printf("Peso: %.1f kg\n", peso);
    printf("Altezza: %.2f m\n", altezza);
    printf("BMI: %.1f\n", bmi);
    
    printf("\n--- INTERPRETAZIONE ---\n");
    if (bmi < 18.5) {
        printf("Sottopeso\n");
    } else if (bmi < 25) {
        printf("Peso normale\n");
    } else {
        printf("Sovrappeso\n");
    }
    
    return 0;
}
```

---

## 2.11 Riepilogo

✅ **Cosa hai imparato:**
- Le variabili sono "scatole" per contenere dati
- Tipi base: `int`, `float`, `char`
- Come dichiarare e inizializzare variabili
- Operatori matematici di base
- Come leggere input con `scanf()`
- Come formattare l'output con `printf()`

✅ **Cosa sai fare ora:**
- Creare programmi interattivi
- Fare calcoli matematici
- Memorizzare e utilizzare dati
- Gestire diversi tipi di informazioni

---

**Prossimo modulo:** Imparerai a prendere **decisioni** nei tuoi programmi con `if` ed `else`!
