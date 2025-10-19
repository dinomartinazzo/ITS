# Modulo 6: Array e Stringhe
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Capire cosa sono gli array e come usarli
- Dichiarare e inizializzare array di diversi tipi
- Scorrere array con i cicli
- Lavorare con le stringhe come array di caratteri
- Implementare algoritmi di ricerca e ordinamento
- Creare programmi che gestiscono liste di dati

---

## 6.1 Che cosa sono gli Array?

Un **array** è come un **armadio con cassetti numerati** dove puoi mettere cose dello stesso tipo.

### Analogia della Vita Reale:
```
Armadio "voti":
┌─────┬─────┬─────┬─────┬─────┐
│  8  │ 7.5 │  9  │ 6.5 │ 8.5 │  ← I valori
└─────┴─────┴─────┴─────┴─────┘
   0     1     2     3     4     ← Gli indici (iniziano da 0!)
```

### Nel Codice:
```c
float voti[5] = {8.0, 7.5, 9.0, 6.5, 8.5};

printf("Primo voto: %.1f\n", voti[0]);    // 8.0
printf("Terzo voto: %.1f\n", voti[2]);    // 9.0
```

**Perché sono utili?**
- ✅ Gestire molti dati dello stesso tipo
- ✅ Organizzare informazioni in modo ordinato
- ✅ Fare operazioni su gruppi di dati
- ✅ Creare liste, tabelle, elenchi

---

## 6.2 Dichiarazione e Inizializzazione

### Metodo 1: Dichiarazione e Inizializzazione Separata
```c
#include <stdio.h>

int main() {
    int numeri[5];    // Dichiara array di 5 interi
    
    // Assegna valori uno per uno
    numeri[0] = 10;
    numeri[1] = 20;
    numeri[2] = 30;
    numeri[3] = 40;
    numeri[4] = 50;
    
    printf("Secondo numero: %d\n", numeri[1]);
    
    return 0;
}
```

### Metodo 2: Inizializzazione Diretta
```c
#include <stdio.h>

int main() {
    int numeri[5] = {10, 20, 30, 40, 50};    // Tutto insieme
    float prezzi[] = {19.99, 29.50, 45.00}; // Dimensione automatica
    
    printf("Primo numero: %d\n", numeri[0]);
    printf("Secondo prezzo: %.2f euro\n", prezzi[1]);
    
    return 0;
}
```

### Metodo 3: Inizializzazione Parziale
```c
#include <stdio.h>

int main() {
    int numeri[10] = {1, 2, 3};  // Solo i primi 3, gli altri sono 0
    
    for (int i = 0; i < 10; i++) {
        printf("numeri[%d] = %d\n", i, numeri[i]);
    }
    
    return 0;
}
```

---

## 6.3 Scorrere un Array

### Con il Ciclo FOR:
```c
#include <stdio.h>

int main() {
    int voti[] = {8, 7, 9, 6, 8, 7, 9};
    int dimensione = 7;
    
    printf("I tuoi voti:\n");
    for (int i = 0; i < dimensione; i++) {
        printf("Voto %d: %d\n", i + 1, voti[i]);
    }
    
    return 0;
}
```

### Calcolare la Media:
```c
#include <stdio.h>

int main() {
    float voti[] = {8.5, 7.2, 9.0, 6.8, 8.0};
    int dimensione = 5;
    float somma = 0;
    
    // Somma tutti i voti
    for (int i = 0; i < dimensione; i++) {
        somma += voti[i];
    }
    
    float media = somma / dimensione;
    
    printf("I tuoi voti: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%.1f ", voti[i]);
    }
    printf("\n");
    
    printf("Somma: %.2f\n", somma);
    printf("Media: %.2f\n", media);
    
    return 0;
}
```

---

## 6.4 Input in Array

### Riempire Array da Tastiera:
```c
#include <stdio.h>

int main() {
    int numeri[5];
    
    printf("Inserisci 5 numeri:\n");
    for (int i = 0; i < 5; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &numeri[i]);
    }
    
    printf("\nHai inserito: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    return 0;
}
```

### Trovare il Massimo:
```c
#include <stdio.h>

int main() {
    int numeri[5];
    int massimo;
    
    printf("Inserisci 5 numeri:\n");
    for (int i = 0; i < 5; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &numeri[i]);
    }
    
    // Il primo numero è il massimo iniziale
    massimo = numeri[0];
    
    // Confronta con gli altri
    for (int i = 1; i < 5; i++) {
        if (numeri[i] > massimo) {
            massimo = numeri[i];
        }
    }
    
    printf("Il numero più grande è: %d\n", massimo);
    
    return 0;
}
```

---

## 6.5 Le Stringhe (Array di Caratteri)

In C, una **stringa** è un array di caratteri che finisce con `'\0'` (carattere nullo).

### Dichiarazione Stringhe:
```c
#include <stdio.h>
#include <string.h>  // Per le funzioni delle stringhe

int main() {
    char nome1[20] = "Mario";           // Metodo 1
    char nome2[] = "Luigi";             // Metodo 2 (dimensione automatica)
    char nome3[20];                     // Metodo 3 (riempire dopo)
    
    strcpy(nome3, "Anna");              // Copia "Anna" in nome3
    
    printf("Nome 1: %s\n", nome1);
    printf("Nome 2: %s\n", nome2);
    printf("Nome 3: %s\n", nome3);
    
    return 0;
}
```

### Input Stringhe:
```c
#include <stdio.h>

int main() {
    char nome[50];
    char cognome[50];
    
    printf("Inserisci il tuo nome: ");
    scanf("%49s", nome);  // Massimo 49 caratteri + '\0'
    
    printf("Inserisci il tuo cognome: ");
    scanf("%49s", cognome);
    
    printf("Ciao %s %s!\n", nome, cognome);
    
    return 0;
}
```

### Funzioni per Stringhe:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char nome[50] = "Mario";
    char cognome[50] = "Rossi";
    char nome_completo[100];
    
    // Lunghezza stringa
    printf("Il nome %s ha %lu caratteri\n", nome, strlen(nome));
    
    // Copia stringa
    strcpy(nome_completo, nome);
    
    // Concatena stringhe
    strcat(nome_completo, " ");
    strcat(nome_completo, cognome);
    
    printf("Nome completo: %s\n", nome_completo);
    
    // Confronta stringhe
    if (strcmp(nome, "Mario") == 0) {
        printf("Il nome è Mario!\n");
    }
    
    return 0;
}
```

---

## 6.6 Array Bidimensionali (Matrici)

Un array bidimensionale è come una **tabella** con righe e colonne.

### Esempio: Tabella di Moltiplicazione:
```c
#include <stdio.h>

int main() {
    int tabella[5][5];  // 5 righe, 5 colonne
    
    // Riempie la tabella
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            tabella[i][j] = (i + 1) * (j + 1);
        }
    }
    
    // Stampa la tabella
    printf("Tabella di moltiplicazione:\n");
    printf("   ");
    for (int j = 1; j <= 5; j++) {
        printf("%4d", j);
    }
    printf("\n");
    
    for (int i = 0; i < 5; i++) {
        printf("%2d ", i + 1);
        for (int j = 0; j < 5; j++) {
            printf("%4d", tabella[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```

### Esempio: Griglia Tris:
```c
#include <stdio.h>

int main() {
    char griglia[3][3] = {
        {'X', 'O', 'X'},
        {'O', 'X', 'O'},
        {'X', 'X', 'O'}
    };
    
    printf("Griglia Tris:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf(" %c ", griglia[i][j]);
            if (j < 2) printf("|");
        }
        printf("\n");
        if (i < 2) printf("-----------\n");
    }
    
    return 0;
}
```

---

## 6.7 Algoritmi con Array

### Ricerca in Array:
```c
#include <stdio.h>

int main() {
    int numeri[] = {5, 12, 8, 3, 15, 7, 20};
    int dimensione = 7;
    int da_cercare, trovato = 0, posizione = -1;
    
    printf("Array: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    printf("Che numero vuoi cercare? ");
    scanf("%d", &da_cercare);
    
    // Ricerca lineare
    for (int i = 0; i < dimensione; i++) {
        if (numeri[i] == da_cercare) {
            trovato = 1;
            posizione = i;
            break;  // Esce dal ciclo quando trova
        }
    }
    
    if (trovato) {
        printf("Numero %d trovato alla posizione %d\n", da_cercare, posizione);
    } else {
        printf("Numero %d non trovato\n", da_cercare);
    }
    
    return 0;
}
```

### Ordinamento Semplice (Bubble Sort):
```c
#include <stdio.h>

int main() {
    int numeri[] = {64, 34, 25, 12, 22, 11, 90};
    int dimensione = 7;
    
    printf("Array originale: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    // Bubble Sort
    for (int i = 0; i < dimensione - 1; i++) {
        for (int j = 0; j < dimensione - i - 1; j++) {
            if (numeri[j] > numeri[j + 1]) {
                // Scambia i due elementi
                int temp = numeri[j];
                numeri[j] = numeri[j + 1];
                numeri[j + 1] = temp;
            }
        }
    }
    
    printf("Array ordinato: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", numeri[i]);
    }
    printf("\n");
    
    return 0;
}
```

---

## 6.8 Esercizi Pratici

### 🎯 Esercizio 6.1: Registro Presenze
```c
#include <stdio.h>
#include <string.h>

int main() {
    char studenti[5][30] = {"Mario", "Luigi", "Anna", "Paolo", "Sara"};
    int presenze[5] = {0, 0, 0, 0, 0};  // 0 = assente, 1 = presente
    int numero_studenti = 5;
    
    printf("=== REGISTRO PRESENZE ===\n");
    
    for (int i = 0; i < numero_studenti; i++) {
        printf("%s è presente? (1=sì, 0=no): ", studenti[i]);
        scanf("%d", &presenze[i]);
    }
    
    printf("\n--- RISULTATO ---\n");
    int presenti = 0;
    
    for (int i = 0; i < numero_studenti; i++) {
        printf("%s: %s\n", studenti[i], 
               presenze[i] ? "Presente" : "Assente");
        if (presenze[i]) presenti++;
    }
    
    printf("\nPresenti: %d/%d\n", presenti, numero_studenti);
    
    return 0;
}
```

### 🎯 Esercizio 6.2: Analisi Testo
```c
#include <stdio.h>
#include <ctype.h>  // Per tolower()

int main() {
    char frase[100];
    int vocali = 0, consonanti = 0, spazi = 0;
    
    printf("Inserisci una frase: ");
    fgets(frase, sizeof(frase), stdin);  // Legge anche gli spazi
    
    for (int i = 0; frase[i] != '\0'; i++) {
        char c = tolower(frase[i]);  // Converte in minuscolo
        
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vocali++;
        } else if (c >= 'a' && c <= 'z') {
            consonanti++;
        } else if (c == ' ') {
            spazi++;
        }
    }
    
    printf("\n--- ANALISI ---\n");
    printf("Vocali: %d\n", vocali);
    printf("Consonanti: %d\n", consonanti);
    printf("Spazi: %d\n", spazi);
    printf("Caratteri totali: %d\n", vocali + consonanti);
    
    return 0;
}
```

---

## 6.9 Array e Funzioni

### Passare Array a Funzioni:
```c
#include <stdio.h>

void stampa_array(int array[], int dimensione) {
    printf("Array: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int somma_array(int array[], int dimensione) {
    int somma = 0;
    for (int i = 0; i < dimensione; i++) {
        somma += array[i];
    }
    return somma;
}

void raddoppia_array(int array[], int dimensione) {
    for (int i = 0; i < dimensione; i++) {
        array[i] *= 2;  // Modifica l'array originale!
    }
}

int main() {
    int numeri[] = {1, 2, 3, 4, 5};
    int dim = 5;
    
    stampa_array(numeri, dim);
    
    printf("Somma: %d\n", somma_array(numeri, dim));
    
    raddoppia_array(numeri, dim);
    printf("Dopo raddoppio: ");
    stampa_array(numeri, dim);
    
    return 0;
}
```

---

## 🎯 Progetto del Modulo: "Sistema di Voti della Classe"

```c
#include <stdio.h>
#include <string.h>

#define MAX_STUDENTI 20
#define MAX_NOME 30

// Funzioni
void stampa_menu(void);
void aggiungi_studente(char nomi[][MAX_NOME], float voti[], int *numero);
void stampa_tutti(char nomi[][MAX_NOME], float voti[], int numero);
void cerca_studente(char nomi[][MAX_NOME], float voti[], int numero);
float calcola_media_classe(float voti[], int numero);
void stampa_statistiche(char nomi[][MAX_NOME], float voti[], int numero);

int main() {
    char nomi[MAX_STUDENTI][MAX_NOME];
    float voti[MAX_STUDENTI];
    int numero_studenti = 0;
    int scelta;
    
    printf("=== SISTEMA VOTI DELLA CLASSE ===\n");
    
    do {
        stampa_menu();
        printf("Scegli (1-6): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                if (numero_studenti < MAX_STUDENTI) {
                    aggiungi_studente(nomi, voti, &numero_studenti);
                } else {
                    printf("Classe piena! (Max %d studenti)\n", MAX_STUDENTI);
                }
                break;
            case 2:
                stampa_tutti(nomi, voti, numero_studenti);
                break;
            case 3:
                cerca_studente(nomi, voti, numero_studenti);
                break;
            case 4:
                if (numero_studenti > 0) {
                    float media = calcola_media_classe(voti, numero_studenti);
                    printf("Media della classe: %.2f\n", media);
                } else {
                    printf("Nessuno studente inserito!\n");
                }
                break;
            case 5:
                stampa_statistiche(nomi, voti, numero_studenti);
                break;
            case 6:
                printf("Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 6);
    
    return 0;
}

void stampa_menu(void) {
    printf("\n--- MENU ---\n");
    printf("1. Aggiungi studente\n");
    printf("2. Mostra tutti gli studenti\n");
    printf("3. Cerca studente\n");
    printf("4. Media della classe\n");
    printf("5. Statistiche\n");
    printf("6. Esci\n");
}

void aggiungi_studente(char nomi[][MAX_NOME], float voti[], int *numero) {
    printf("Nome studente: ");
    scanf("%29s", nomi[*numero]);  // Max 29 caratteri + '\0'
    
    do {
        printf("Voto (0.0-10.0): ");
        scanf("%f", &voti[*numero]);
        
        if (voti[*numero] < 0.0 || voti[*numero] > 10.0) {
            printf("Voto non valido!\n");
        }
    } while (voti[*numero] < 0.0 || voti[*numero] > 10.0);
    
    (*numero)++;
    printf("Studente aggiunto!\n");
}

void stampa_tutti(char nomi[][MAX_NOME], float voti[], int numero) {
    if (numero == 0) {
        printf("Nessuno studente inserito!\n");
        return;
    }
    
    printf("\n=== ELENCO STUDENTI ===\n");
    printf("%-20s | Voto\n", "Nome");
    printf("---------------------------\n");
    
    for (int i = 0; i < numero; i++) {
        char giudizio;
        if (voti[i] >= 8.0) giudizio = 'A';
        else if (voti[i] >= 7.0) giudizio = 'B';
        else if (voti[i] >= 6.0) giudizio = 'C';
        else giudizio = 'F';
        
        printf("%-20s | %.1f (%c)\n", nomi[i], voti[i], giudizio);
    }
}

void cerca_studente(char nomi[][MAX_NOME], float voti[], int numero) {
    if (numero == 0) {
        printf("Nessuno studente inserito!\n");
        return;
    }
    
    char nome_cerca[MAX_NOME];
    printf("Nome da cercare: ");
    scanf("%29s", nome_cerca);
    
    for (int i = 0; i < numero; i++) {
        if (strcmp(nomi[i], nome_cerca) == 0) {
            printf("Studente trovato: %s - Voto: %.1f\n", nomi[i], voti[i]);
            return;
        }
    }
    
    printf("Studente '%s' non trovato!\n", nome_cerca);
}

float calcola_media_classe(float voti[], int numero) {
    float somma = 0;
    for (int i = 0; i < numero; i++) {
        somma += voti[i];
    }
    return somma / numero;
}

void stampa_statistiche(char nomi[][MAX_NOME], float voti[], int numero) {
    if (numero == 0) {
        printf("Nessuno studente inserito!\n");
        return;
    }
    
    printf("\n=== STATISTICHE CLASSE ===\n");
    printf("Numero studenti: %d\n", numero);
    
    float media = calcola_media_classe(voti, numero);
    printf("Media classe: %.2f\n", media);
    
    // Trova voto minimo e massimo
    float minimo = voti[0], massimo = voti[0];
    int pos_min = 0, pos_max = 0;
    
    for (int i = 1; i < numero; i++) {
        if (voti[i] < minimo) {
            minimo = voti[i];
            pos_min = i;
        }
        if (voti[i] > massimo) {
            massimo = voti[i];
            pos_max = i;
        }
    }
    
    printf("Voto più alto: %.1f (%s)\n", massimo, nomi[pos_max]);
    printf("Voto più basso: %.1f (%s)\n", minimo, nomi[pos_min]);
    
    // Conta promozioni/bocciature
    int promossi = 0, bocciati = 0;
    for (int i = 0; i < numero; i++) {
        if (voti[i] >= 6.0) {
            promossi++;
        } else {
            bocciati++;
        }
    }
    
    printf("Promossi: %d (%.1f%%)\n", promossi, (float)promossi / numero * 100);
    printf("Bocciati: %d (%.1f%%)\n", bocciati, (float)bocciati / numero * 100);
    printf("========================\n");
}
```

---

## 6.10 Riepilogo

✅ **Cosa hai imparato:**
- Array per gestire collezioni di dati dello stesso tipo
- Indici che iniziano da 0
- Cicli per scorrere gli array
- Stringhe come array di caratteri
- Array bidimensionali (matrici)
- Algoritmi di ricerca e ordinamento
- Passaggio di array alle funzioni

✅ **Cosa sai fare ora:**
- Gestire liste di studenti, voti, prodotti
- Implementare algoritmi di ricerca e ordinamento
- Lavorare con stringhe e testo
- Creare griglie e tabelle
- Sviluppare sistemi di gestione dati semplici

---

**Prossimo modulo:** Imparerai i **puntatori** per gestire la memoria in modo avanzato!
