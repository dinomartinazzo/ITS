# Manuale Introduttivo alla Programmazione in C

## Introduzione
Questo libretto è pensato per studenti alle prime armi con la programmazione. Non è richiesta alcuna conoscenza precedente. Il linguaggio che utilizzeremo è **C**, uno dei linguaggi più diffusi e fondamentali, base di molti altri linguaggi moderni.

Il linguaggio C è:
- **Procedurale**: il programma è una sequenza di istruzioni.
- **Compilato**: il codice sorgente deve essere tradotto in linguaggio macchina da un compilatore (es. `gcc`).
- **Efficiente e vicino all’hardware**: permette di capire bene come funziona un calcolatore.

---

## Struttura del manuale
1. **Introduzione al linguaggio C**
2. **Primo programma: Hello World**
3. **Tipi di dato e variabili**
4. **Operatori**
5. **Input e Output**
6. **Strutture di controllo** (if, else, switch)
7. **Cicli** (for, while, do-while)
8. **Funzioni**
9. **Array**
10. **Esercizi di riepilogo con soluzioni guidate**
11. **Progetti pratici finali**

---

## Primo Programma in C
```c
#include <stdio.h>   // libreria per input e output

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

---

## Tipi di Dato e Variabili
| Tipo     | Descrizione                     | Esempio          |
|----------|---------------------------------|------------------|
| `int`    | Numeri interi                   | `int a = 5;`     |
| `float`  | Numeri decimali a precisione    | `float b = 3.14;`|
| `double` | Numeri decimali più precisi     | `double c = 2.71;`|
| `char`   | Carattere singolo               | `char d = 'A';`  |

```c
int eta = 18;
float pi = 3.14;
char iniziale = 'D';
```

---

## Operatori
- Aritmetici: `+`, `-`, `*`, `/`, `%`
- Relazionali: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logici: `&&`, `||`, `!`

```c
int a = 5, b = 2;
int somma = a + b;       // 7
int resto = a % b;       // 1
int confronto = (a > b); // vero (1)
```

---

## Input e Output
```c
#include <stdio.h>

int main() {
    int numero;
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    printf("Hai inserito: %d\n", numero);
    return 0;
}
```

---

## Strutture di Controllo
```c
if (x > 0) {
    printf("Positivo\n");
} else if (x < 0) {
    printf("Negativo\n");
} else {
    printf("Zero\n");
}
```

```c
switch (giorno) {
    case 1: printf("Lunedì\n"); break;
    case 2: printf("Martedì\n"); break;
    default: printf("Altro giorno\n");
}
```

---

## Cicli
```c
int i = 0;
while (i < 5) {
    printf("i = %d\n", i);
    i++;
}
```

```c
for (int i = 0; i < 5; i++) {
    printf("i = %d\n", i);
}
```

```c
int i = 0;
do {
    printf("i = %d\n", i);
    i++;
} while (i < 5);
```

---

## Funzioni
```c
int somma(int a, int b) {
    return a + b;
}

int main() {
    int risultato = somma(3, 4);
    printf("Somma = %d\n", risultato);
    return 0;
}
```

---

## Array
```c
int numeri[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
    printf("%d ", numeri[i]);
}
```

---

## Esercizi di Riepilogo con Soluzioni Guidate

### Capitolo 1 – Hello World
**Esercizio:** Scrivi un programma che stampi il tuo nome e cognome.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    printf("Mi chiamo Mario Rossi\n");
    return 0;
}
```

### Capitolo 2 – Variabili
**Esercizio:** Dichiarare una variabile `int` con la tua età e stamparla.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    int eta = 20;
    printf("Età = %d\n", eta);
    return 0;
}
```

### Capitolo 3 – Operatori
**Esercizio:** Calcolare somma, differenza e prodotto di due numeri interi.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    int a = 7, b = 3;
    printf("Somma = %d\n", a + b);
    printf("Differenza = %d\n", a - b);
    printf("Prodotto = %d\n", a * b);
    return 0;
}
```

### Capitolo 4 – Condizioni
**Esercizio:** Verificare se un numero è positivo, negativo o zero.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    int n;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
    if (n > 0)
        printf("Positivo\n");
    else if (n < 0)
        printf("Negativo\n");
    else
        printf("Zero\n");
    return 0;
}
```

### Capitolo 5 – Cicli
**Esercizio:** Stampare i numeri da 1 a 10 con un ciclo for.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    for (int i = 1; i <= 10; i++) {
        printf("%d ", i);
    }
    return 0;
}
```

### Capitolo 6 – Funzioni
**Esercizio:** Scrivere una funzione che calcola il quadrato di un numero.  
**Soluzione:**
```c
#include <stdio.h>
int quadrato(int x) { return x * x; }
int main() {
    printf("Quadrato di 5 = %d\n", quadrato(5));
    return 0;
}
```

### Capitolo 7 – Array
**Esercizio:** Calcolare la media di 5 numeri.  
**Soluzione:**
```c
#include <stdio.h>
int main() {
    int numeri[5] = {10, 20, 30, 40, 50};
    int somma = 0;
    for (int i = 0; i < 5; i++) somma += numeri[i];
    float media = somma / 5.0;
    printf("Media = %.2f\n", media);
    return 0;
}
```

---

## Progetti Pratici Finali
### Calcolatrice
*(già presente nella versione precedente con soluzione guidata)*

### Tabellina
*(già presente con soluzione guidata)*

### Media di una Lista di Numeri
*(già presente con soluzione guidata)*

### Indovina il Numero
*(già presente con soluzione guidata)*

---

## Conclusioni
Abbiamo introdotto:
- Concetti base del linguaggio C
- Tipi di dato e variabili
- Operatori
- Input/Output
- Strutture di controllo
- Cicli
- Funzioni
- Array
- Esercizi pratici con soluzioni guidate
- Progetti finali integrativi

