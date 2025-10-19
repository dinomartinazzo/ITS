# Modulo 4: Cicli e Ripetizioni
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Usare il ciclo `for` per ripetere operazioni un numero fisso di volte
- Usare `while` per cicli con condizioni
- Usare `do-while` quando serve almeno un'esecuzione
- Controllare i cicli con `break` e `continue`
- Creare programmi che automatizzano compiti ripetitivi

---

## 4.1 Perché i Cicli?

Immagina di dover stampare i numeri da 1 a 100. Senza cicli:

```c
printf("1\n");
printf("2\n");
printf("3\n");
// ... 97 righe in più!
printf("100\n");
```

Con i cicli:
```c
for (int i = 1; i <= 100; i++) {
    printf("%d\n", i);
}
```

**I cicli ti permettono di:**
- Evitare codice ripetitivo
- Automatizzare compiti lunghi
- Rendere il codice più flessibile

---

## 4.2 Il Ciclo FOR

Il ciclo `for` è perfetto quando sai **quante volte** ripetere qualcosa.

### Struttura Base:
```c
for (inizializzazione; condizione; incremento) {
    // Codice da ripetere
}
```

### Esempio Semplice:
```c
#include <stdio.h>

int main() {
    // Conta da 1 a 10
    for (int i = 1; i <= 10; i++) {
        printf("Numero: %d\n", i);
    }
    
    return 0;
}
```

### Come Funziona:
1. **Inizializzazione** (`int i = 1`): Crea la variabile contatore
2. **Condizione** (`i <= 10`): Controlla se continuare
3. **Corpo del ciclo**: Esegue il codice dentro `{}`
4. **Incremento** (`i++`): Aumenta il contatore
5. Ripete dal punto 2

---

## 4.3 Varianti del Ciclo FOR

### Contare all'Indietro:
```c
#include <stdio.h>

int main() {
    printf("Countdown:\n");
    for (int i = 10; i >= 1; i--) {
        printf("%d\n", i);
    }
    printf("Via!\n");
    
    return 0;
}
```

### Saltare Numeri:
```c
#include <stdio.h>

int main() {
    printf("Numeri pari da 0 a 20:\n");
    for (int i = 0; i <= 20; i += 2) {  // i += 2 significa i = i + 2
        printf("%d ", i);
    }
    printf("\n");
    
    return 0;
}
```

### Tabellina:
```c
#include <stdio.h>

int main() {
    int numero;
    
    printf("Quale tabellina vuoi? ");
    scanf("%d", &numero);
    
    printf("\nTabellina del %d:\n", numero);
    for (int i = 1; i <= 10; i++) {
        printf("%d × %d = %d\n", numero, i, numero * i);
    }
    
    return 0;
}
```

---

## 4.4 Il Ciclo WHILE

Il ciclo `while` è perfetto quando **non sai quante volte** ripetere, ma sai **quando fermarti**.

### Struttura:
```c
while (condizione) {
    // Codice da ripetere
}
```

### Esempio: Input Valido
```c
#include <stdio.h>

int main() {
    int numero;
    
    printf("Inserisci un numero da 1 a 10: ");
    scanf("%d", &numero);
    
    // Continua a chiedere finché non è valido
    while (numero < 1 || numero > 10) {
        printf("Numero non valido! Riprova (1-10): ");
        scanf("%d", &numero);
    }
    
    printf("Bravo! Hai inserito %d\n", numero);
    
    return 0;
}
```

### Esempio: Somma Numeri
```c
#include <stdio.h>

int main() {
    int numero, somma = 0;
    
    printf("Inserisci numeri positivi (0 per finire):\n");
    
    scanf("%d", &numero);
    while (numero != 0) {
        if (numero > 0) {
            somma += numero;
        }
        scanf("%d", &numero);
    }
    
    printf("La somma è: %d\n", somma);
    
    return 0;
}
```

---

## 4.5 Il Ciclo DO-WHILE

Simile a `while`, ma esegue il codice **almeno una volta** prima di controllare la condizione.

### Struttura:
```c
do {
    // Codice da ripetere
} while (condizione);
```

### Esempio: Menu che Si Ripete
```c
#include <stdio.h>

int main() {
    int scelta;
    
    do {
        printf("\n=== MENU ===\n");
        printf("1. Saluta\n");
        printf("2. Mostra data\n");
        printf("3. Esci\n");
        printf("Scegli (1-3): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                printf("Ciao! Come va?\n");
                break;
            case 2:
                printf("Oggi è lunedì!\n");
                break;
            case 3:
                printf("Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 3);
    
    return 0;
}
```

### Differenza con WHILE:
```c
// WHILE: potrebbe non eseguirsi mai
int x = 5;
while (x < 5) {
    printf("Non verrà mai stampato\n");
}

// DO-WHILE: si esegue sempre almeno una volta
int y = 5;
do {
    printf("Verrà stampato una volta\n");
} while (y < 5);
```

---

## 4.6 Controllo dei Cicli: break e continue

### BREAK - Esce dal Ciclo:
```c
#include <stdio.h>

int main() {
    printf("Trova il primo numero divisibile per 7:\n");
    
    for (int i = 50; i <= 100; i++) {
        if (i % 7 == 0) {
            printf("Trovato! %d è divisibile per 7\n", i);
            break;  // Esce dal ciclo
        }
        printf("Controllando %d...\n", i);
    }
    
    return 0;
}
```

### CONTINUE - Salta all'Iterazione Successiva:
```c
#include <stdio.h>

int main() {
    printf("Numeri da 1 a 10, saltando i multipli di 3:\n");
    
    for (int i = 1; i <= 10; i++) {
        if (i % 3 == 0) {
            continue;  // Salta il resto e va alla prossima iterazione
        }
        printf("%d ", i);
    }
    printf("\n");
    
    return 0;
}
```

---

## 4.7 Cicli Annidati

Puoi mettere un ciclo **dentro** un altro ciclo:

### Tabella di Moltiplicazione:
```c
#include <stdio.h>

int main() {
    printf("Tabella di moltiplicazione (1-5):\n\n");
    
    // Stampa intestazione
    printf("   ");
    for (int j = 1; j <= 5; j++) {
        printf("%4d", j);
    }
    printf("\n");
    
    // Stampa righe
    for (int i = 1; i <= 5; i++) {
        printf("%2d ", i);
        for (int j = 1; j <= 5; j++) {
            printf("%4d", i * j);
        }
        printf("\n");
    }
    
    return 0;
}
```

### Disegno con Asterischi:
```c
#include <stdio.h>

int main() {
    int righe;
    
    printf("Quante righe per il triangolo? ");
    scanf("%d", &righe);
    
    for (int i = 1; i <= righe; i++) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    
    return 0;
}
```

**Risultato con 5 righe:**
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

---

## 4.8 Esercizi Pratici

### 🎯 Esercizio 4.1: Calcolatrice del Fattoriale
```c
#include <stdio.h>

int main() {
    int numero, fattoriale = 1;
    
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    printf("%d! = ", numero);
    
    for (int i = 1; i <= numero; i++) {
        fattoriale *= i;  // fattoriale = fattoriale * i
        printf("%d", i);
        if (i < numero) printf(" × ");
    }
    
    printf(" = %d\n", fattoriale);
    
    return 0;
}
```

### 🎯 Esercizio 4.2: Numeri Primi
```c
#include <stdio.h>

int main() {
    int numero, primo = 1;
    
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    if (numero <= 1) {
        primo = 0;
    } else {
        for (int i = 2; i < numero; i++) {
            if (numero % i == 0) {
                primo = 0;
                break;
            }
        }
    }
    
    if (primo) {
        printf("%d è un numero primo\n", numero);
    } else {
        printf("%d non è un numero primo\n", numero);
    }
    
    return 0;
}
```

### 🎯 Esercizio 4.3: Media di N Numeri
```c
#include <stdio.h>

int main() {
    int quantita, numero;
    float somma = 0, media;
    
    printf("Quanti numeri vuoi inserire? ");
    scanf("%d", &quantita);
    
    for (int i = 1; i <= quantita; i++) {
        printf("Inserisci il numero %d: ", i);
        scanf("%d", &numero);
        somma += numero;
    }
    
    media = somma / quantita;
    
    printf("\nSomma: %.0f\n", somma);
    printf("Media: %.2f\n", media);
    
    return 0;
}
```

---

## 4.9 Pattern e Algoritmi Comuni

### Trovare il Massimo:
```c
#include <stdio.h>

int main() {
    int numeri, numero, massimo;
    
    printf("Quanti numeri? ");
    scanf("%d", &numeri);
    
    printf("Inserisci numero 1: ");
    scanf("%d", &numero);
    massimo = numero;  // Il primo è il massimo iniziale
    
    for (int i = 2; i <= numeri; i++) {
        printf("Inserisci numero %d: ", i);
        scanf("%d", &numero);
        
        if (numero > massimo) {
            massimo = numero;
        }
    }
    
    printf("Il numero più grande è: %d\n", massimo);
    
    return 0;
}
```

### Contare le Cifre:
```c
#include <stdio.h>

int main() {
    int numero, cifre = 0;
    
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    if (numero == 0) {
        cifre = 1;
    } else {
        while (numero > 0) {
            numero /= 10;  // numero = numero / 10
            cifre++;
        }
    }
    
    printf("Il numero ha %d cifre\n", cifre);
    
    return 0;
}
```

---

## 4.10 Errori Comuni

### ❌ Ciclo Infinito:
```c
// SBAGLIATO: i non cambia mai!
int i = 1;
while (i <= 10) {
    printf("%d\n", i);
    // Dimenticato: i++;
}

// GIUSTO:
int i = 1;
while (i <= 10) {
    printf("%d\n", i);
    i++;
}
```

### ❌ Condizione Sbagliata:
```c
// SBAGLIATO: usa = invece di ==
for (int i = 1; i = 10; i++) {  // Assegna sempre 10 a i!

// GIUSTO:
for (int i = 1; i <= 10; i++) {  // Confronta i con 10
```

### ❌ Variabile Non Inizializzata:
```c
// SBAGLIATO:
int somma;  // Valore casuale!
for (int i = 1; i <= 10; i++) {
    somma += i;
}

// GIUSTO:
int somma = 0;  // Inizializza a 0!
for (int i = 1; i <= 10; i++) {
    somma += i;
}
```

---

## 🎯 Progetto del Modulo: "Gioco della Moltiplicazione"

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int punti = 0, domande = 5;
    int num1, num2, risposta, risposta_corretta;
    
    srand(time(NULL));  // Inizializza numeri casuali
    
    printf("=== GIOCO DELLA MOLTIPLICAZIONE ===\n");
    printf("Rispondi alle moltiplicazioni!\n");
    printf("Hai %d domande.\n\n", domande);
    
    for (int i = 1; i <= domande; i++) {
        // Genera numeri casuali da 1 a 10
        num1 = rand() % 10 + 1;
        num2 = rand() % 10 + 1;
        risposta_corretta = num1 * num2;
        
        printf("Domanda %d: %d × %d = ? ", i, num1, num2);
        scanf("%d", &risposta);
        
        if (risposta == risposta_corretta) {
            printf("✓ Corretto!\n");
            punti++;
        } else {
            printf("✗ Sbagliato! La risposta era %d\n", risposta_corretta);
        }
        printf("\n");
    }
    
    printf("=== RISULTATO FINALE ===\n");
    printf("Hai risposto correttamente a %d domande su %d\n", punti, domande);
    
    if (punti == domande) {
        printf("🏆 Perfetto! Sei un genio!\n");
    } else if (punti >= domande * 0.8) {
        printf("🎉 Bravo! Ottimo punteggio!\n");
    } else if (punti >= domande * 0.6) {
        printf("👍 Bene! Puoi fare ancora meglio!\n");
    } else {
        printf("📚 Devi esercitarti di più!\n");
    }
    
    return 0;
}
```

---

## 4.11 Riepilogo

✅ **Cosa hai imparato:**
- Ciclo `for` per ripetizioni con contatore
- Ciclo `while` per ripetizioni con condizione
- Ciclo `do-while` per almeno un'esecuzione
- Controllo con `break` e `continue`
- Cicli annidati per pattern complessi

✅ **Cosa sai fare ora:**
- Automatizzare compiti ripetitivi
- Creare tabelle e pattern
- Validare input degli utenti
- Implementare algoritmi matematici
- Creare giochi e quiz interattivi

---

**Prossimo modulo:** Imparerai le **funzioni** per organizzare il tuo codice in blocchi riutilizzabili!
