# Modulo 7: Puntatori e Gestione Memoria
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Capire cosa sono i puntatori e perché sono utili
- Dichiarare e usare puntatori semplici
- Passare parametri per riferimento alle funzioni
- Capire la relazione tra array e puntatori
- Gestire la memoria dinamica in modo base
- Evitare errori comuni con i puntatori

---

## 7.1 Che cosa sono i Puntatori?

Un **puntatore** è come un **indirizzo di casa**: invece di contenere un valore, contiene la **posizione** dove si trova quel valore in memoria.

### Analogia della Vita Reale:
```
Tu vuoi mandare una lettera a Mario.
Non metti Mario nella busta (impossibile!), 
ma scrivi il suo INDIRIZZO: "Via Roma 15, Milano"

Puntatore = Indirizzo
Variabile = Casa
Valore = Mario che abita nella casa
```

### Nel Codice:
```c
#include <stdio.h>

int main() {
    int numero = 42;        // Una variabile normale
    int *puntatore;         // Un puntatore a int
    
    puntatore = &numero;    // Il puntatore "punta" a numero
    
    printf("Valore di numero: %d\n", numero);
    printf("Indirizzo di numero: %p\n", (void*)&numero);
    printf("Valore del puntatore: %p\n", (void*)puntatore);
    printf("Valore puntato: %d\n", *puntatore);
    
    return 0;
}
```

**Spiegazione simboli:**
- `&` = "indirizzo di" (ottieni l'indirizzo)
- `*` = "contenuto di" (ottieni il valore)

---

## 7.2 Dichiarazione e Uso Base

### Esempio Semplice:
```c
#include <stdio.h>

int main() {
    int x = 10;       // Variabile normale
    int *ptr;         // Puntatore (dichiara)
    
    ptr = &x;         // Puntatore ora "punta" a x
    
    printf("x vale: %d\n", x);
    printf("*ptr vale: %d\n", *ptr);  // Stesso valore di x
    
    // Modifico attraverso il puntatore
    *ptr = 20;
    
    printf("Ora x vale: %d\n", x);   // x è cambiato!
    
    return 0;
}
```

### Esempio con Float:
```c
#include <stdio.h>

int main() {
    float prezzo = 19.99;
    float *p_prezzo = &prezzo;  // Dichiaro e assegno insieme
    
    printf("Prezzo originale: %.2f euro\n", prezzo);
    
    // Sconto del 20% attraverso puntatore
    *p_prezzo = *p_prezzo * 0.8;
    
    printf("Prezzo scontato: %.2f euro\n", prezzo);
    
    return 0;
}
```

---

## 7.3 Puntatori e Funzioni

I puntatori permettono alle funzioni di **modificare** le variabili originali.

### Senza Puntatori (Non Funziona):
```c
#include <stdio.h>

void raddoppia_sbagliato(int numero) {
    numero = numero * 2;  // Modifica solo la copia!
    printf("Dentro la funzione: %d\n", numero);
}

int main() {
    int x = 5;
    
    printf("Prima: x = %d\n", x);
    raddoppia_sbagliato(x);
    printf("Dopo: x = %d\n", x);  // x non è cambiato!
    
    return 0;
}
```

### Con Puntatori (Funziona!):
```c
#include <stdio.h>

void raddoppia_giusto(int *numero) {
    *numero = *numero * 2;  // Modifica l'originale!
    printf("Dentro la funzione: %d\n", *numero);
}

int main() {
    int x = 5;
    
    printf("Prima: x = %d\n", x);
    raddoppia_giusto(&x);   // Passo l'indirizzo
    printf("Dopo: x = %d\n", x);  // x è cambiato!
    
    return 0;
}
```

### Scambio di Due Variabili:
```c
#include <stdio.h>

void scambia(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    
    printf("Prima: x=%d, y=%d\n", x, y);
    scambia(&x, &y);
    printf("Dopo: x=%d, y=%d\n", x, y);
    
    return 0;
}
```

---

## 7.4 Funzioni che Restituiscono Più Valori

Con i puntatori, una funzione può "restituire" più valori:

```c
#include <stdio.h>

void calcola_rettangolo(float base, float altezza, 
                       float *area, float *perimetro) {
    *area = base * altezza;
    *perimetro = 2 * (base + altezza);
}

void dividi_con_resto(int dividendo, int divisore, 
                     int *quoziente, int *resto) {
    *quoziente = dividendo / divisore;
    *resto = dividendo % divisore;
}

int main() {
    // Test rettangolo
    float area, perimetro;
    calcola_rettangolo(5.0, 3.0, &area, &perimetro);
    
    printf("Rettangolo 5x3:\n");
    printf("Area: %.2f\n", area);
    printf("Perimetro: %.2f\n", perimetro);
    
    // Test divisione
    int quoziente, resto;
    dividi_con_resto(17, 5, &quoziente, &resto);
    
    printf("\n17 ÷ 5:\n");
    printf("Quoziente: %d\n", quoziente);
    printf("Resto: %d\n", resto);
    
    return 0;
}
```

---

## 7.5 Array e Puntatori

Il nome di un array **è già un puntatore** al primo elemento!

```c
#include <stdio.h>

int main() {
    int numeri[5] = {10, 20, 30, 40, 50};
    int *ptr = numeri;  // ptr punta al primo elemento
    
    // Tre modi per accedere agli elementi:
    printf("Primo elemento:\n");
    printf("numeri[0] = %d\n", numeri[0]);
    printf("*numeri = %d\n", *numeri);
    printf("*ptr = %d\n", *ptr);
    
    printf("\nSecondo elemento:\n");
    printf("numeri[1] = %d\n", numeri[1]);
    printf("*(numeri + 1) = %d\n", *(numeri + 1));
    printf("*(ptr + 1) = %d\n", *(ptr + 1));
    
    // Scorre array con puntatore
    printf("\nTutto l'array:\n");
    for (int i = 0; i < 5; i++) {
        printf("Elemento %d: %d\n", i, *(ptr + i));
    }
    
    return 0;
}
```

### Funzione che Somma Array:
```c
#include <stdio.h>

int somma_array(int *array, int dimensione) {
    int somma = 0;
    for (int i = 0; i < dimensione; i++) {
        somma += array[i];  // Oppure: somma += *(array + i);
    }
    return somma;
}

void stampa_array(int *array, int dimensione) {
    printf("Array: ");
    for (int i = 0; i < dimensione; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {
    int numeri[] = {5, 10, 15, 20, 25};
    int dim = 5;
    
    stampa_array(numeri, dim);
    printf("Somma: %d\n", somma_array(numeri, dim));
    
    return 0;
}
```

---

## 7.6 Allocazione Dinamica della Memoria

Fino ad ora hai creato array di **dimensione fissa**. Con i puntatori puoi creare array di **dimensione variabile**!

### malloc() - Alloca Memoria:
```c
#include <stdio.h>
#include <stdlib.h>  // Per malloc e free

int main() {
    int n;
    int *array;
    
    printf("Quanti numeri vuoi memorizzare? ");
    scanf("%d", &n);
    
    // Alloca memoria per n interi
    array = (int*)malloc(n * sizeof(int));
    
    if (array == NULL) {
        printf("Errore: memoria non disponibile!\n");
        return 1;
    }
    
    // Riempie l'array
    printf("Inserisci %d numeri:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &array[i]);
    }
    
    // Stampa l'array
    printf("Hai inserito: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    // IMPORTANTE: Libera la memoria!
    free(array);
    
    return 0;
}
```

### Esempio: Media di N Voti:
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int numero_voti;
    float *voti;
    float somma = 0, media;
    
    printf("Quanti voti hai? ");
    scanf("%d", &numero_voti);
    
    // Alloca memoria per i voti
    voti = (float*)malloc(numero_voti * sizeof(float));
    
    if (voti == NULL) {
        printf("Errore nell'allocazione memoria!\n");
        return 1;
    }
    
    // Inserimento voti
    for (int i = 0; i < numero_voti; i++) {
        do {
            printf("Voto %d (0-10): ", i + 1);
            scanf("%f", &voti[i]);
        } while (voti[i] < 0 || voti[i] > 10);
        
        somma += voti[i];
    }
    
    media = somma / numero_voti;
    
    // Risultati
    printf("\nI tuoi voti: ");
    for (int i = 0; i < numero_voti; i++) {
        printf("%.1f ", voti[i]);
    }
    printf("\n");
    
    printf("Media: %.2f\n", media);
    
    if (media >= 6.0) {
        printf("Promosso! 🎉\n");
    } else {
        printf("Devi studiare di più! 📚\n");
    }
    
    // Libera memoria
    free(voti);
    
    return 0;
}
```

---

## 7.7 Stringhe Dinamiche

Anche le stringhe possono essere dinamiche:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int lunghezza;
    char *nome;
    
    printf("Quanto è lungo il tuo nome? ");
    scanf("%d", &lunghezza);
    
    // Alloca memoria per la stringa (+ 1 per '\0')
    nome = (char*)malloc((lunghezza + 1) * sizeof(char));
    
    if (nome == NULL) {
        printf("Errore nell'allocazione memoria!\n");
        return 1;
    }
    
    printf("Inserisci il tuo nome: ");
    scanf("%s", nome);
    
    printf("Ciao %s!\n", nome);
    printf("Il tuo nome ha %lu caratteri\n", strlen(nome));
    
    // Libera memoria
    free(nome);
    
    return 0;
}
```

---

## 7.8 Esercizi Pratici

### 🎯 Esercizio 7.1: Scambio in Funzione
```c
#include <stdio.h>

void scambia_float(float *a, float *b) {
    float temp = *a;
    *a = *b;
    *b = temp;
}

void ordina_tre_numeri(float *a, float *b, float *c) {
    // Ordina tre numeri in ordine crescente
    if (*a > *b) scambia_float(a, b);
    if (*b > *c) scambia_float(b, c);
    if (*a > *b) scambia_float(a, b);
}

int main() {
    float x, y, z;
    
    printf("Inserisci tre numeri: ");
    scanf("%f %f %f", &x, &y, &z);
    
    printf("Prima: %.1f, %.1f, %.1f\n", x, y, z);
    
    ordina_tre_numeri(&x, &y, &z);
    
    printf("Dopo: %.1f, %.1f, %.1f\n", x, y, z);
    
    return 0;
}
```

### 🎯 Esercizio 7.2: Statistiche Array Dinamico
```c
#include <stdio.h>
#include <stdlib.h>

void calcola_statistiche(int *array, int n, 
                        int *minimo, int *massimo, float *media) {
    *minimo = *massimo = array[0];
    int somma = 0;
    
    for (int i = 0; i < n; i++) {
        if (array[i] < *minimo) *minimo = array[i];
        if (array[i] > *massimo) *massimo = array[i];
        somma += array[i];
    }
    
    *media = (float)somma / n;
}

int main() {
    int n;
    int *numeri;
    int minimo, massimo;
    float media;
    
    printf("Quanti numeri? ");
    scanf("%d", &n);
    
    numeri = (int*)malloc(n * sizeof(int));
    if (numeri == NULL) {
        printf("Errore memoria!\n");
        return 1;
    }
    
    for (int i = 0; i < n; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &numeri[i]);
    }
    
    calcola_statistiche(numeri, n, &minimo, &massimo, &media);
    
    printf("\n--- STATISTICHE ---\n");
    printf("Minimo: %d\n", minimo);
    printf("Massimo: %d\n", massimo);
    printf("Media: %.2f\n", media);
    
    free(numeri);
    return 0;
}
```

---

## 7.9 Errori Comuni con i Puntatori

### ❌ Puntatore Non Inizializzato:
```c
// SBAGLIATO:
int *ptr;           // Non punta a niente!
*ptr = 42;          // CRASH! ☠️

// GIUSTO:
int numero;
int *ptr = &numero; // Ora punta a qualcosa
*ptr = 42;          // OK!
```

### ❌ Dimenticare free():
```c
// SBAGLIATO:
int *array = (int*)malloc(100 * sizeof(int));
// Uso array...
// return 0;  // Memory leak! 💸

// GIUSTO:
int *array = (int*)malloc(100 * sizeof(int));
// Uso array...
free(array);  // Libero la memoria
return 0;
```

### ❌ Usare free() Due Volte:
```c
// SBAGLIATO:
int *ptr = (int*)malloc(sizeof(int));
free(ptr);
free(ptr);  // CRASH! ☠️

// GIUSTO:
int *ptr = (int*)malloc(sizeof(int));
free(ptr);
ptr = NULL;  // Buona pratica
// free(ptr);  // Ora è sicuro (non fa nulla)
```

---

## 🎯 Progetto del Modulo: "Gestione Lista Spesa Dinamica"

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOME 30

// Struttura per un prodotto
typedef struct {
    char nome[MAX_NOME];
    float prezzo;
    int quantita;
} Prodotto;

// Funzioni
void stampa_menu(void);
Prodotto* aggiungi_prodotto(Prodotto *lista, int *dimensione);
void stampa_lista(Prodotto *lista, int dimensione);
void calcola_totale(Prodotto *lista, int dimensione);
void modifica_quantita(Prodotto *lista, int dimensione);

int main() {
    Prodotto *lista_spesa = NULL;
    int num_prodotti = 0;
    int scelta;
    
    printf("=== LISTA SPESA DINAMICA ===\n");
    
    do {
        stampa_menu();
        printf("Scegli (1-5): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                lista_spesa = aggiungi_prodotto(lista_spesa, &num_prodotti);
                break;
            case 2:
                stampa_lista(lista_spesa, num_prodotti);
                break;
            case 3:
                calcola_totale(lista_spesa, num_prodotti);
                break;
            case 4:
                modifica_quantita(lista_spesa, num_prodotti);
                break;
            case 5:
                printf("Buona spesa! 🛒\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 5);
    
    // Libera memoria
    if (lista_spesa != NULL) {
        free(lista_spesa);
    }
    
    return 0;
}

void stampa_menu(void) {
    printf("\n--- MENU ---\n");
    printf("1. Aggiungi prodotto\n");
    printf("2. Mostra lista\n");
    printf("3. Calcola totale\n");
    printf("4. Modifica quantità\n");
    printf("5. Esci\n");
}

Prodotto* aggiungi_prodotto(Prodotto *lista, int *dimensione) {
    // Ridimensiona array (aggiunge spazio per un prodotto)
    lista = (Prodotto*)realloc(lista, (*dimensione + 1) * sizeof(Prodotto));
    
    if (lista == NULL) {
        printf("Errore nell'allocazione memoria!\n");
        return NULL;
    }
    
    Prodotto *nuovo = &lista[*dimensione];
    
    printf("Nome prodotto: ");
    scanf("%29s", nuovo->nome);
    
    do {
        printf("Prezzo (€): ");
        scanf("%f", &nuovo->prezzo);
        if (nuovo->prezzo < 0) printf("Il prezzo non può essere negativo!\n");
    } while (nuovo->prezzo < 0);
    
    do {
        printf("Quantità: ");
        scanf("%d", &nuovo->quantita);
        if (nuovo->quantita <= 0) printf("La quantità deve essere positiva!\n");
    } while (nuovo->quantita <= 0);
    
    (*dimensione)++;
    printf("Prodotto '%s' aggiunto alla lista!\n", nuovo->nome);
    
    return lista;
}

void stampa_lista(Prodotto *lista, int dimensione) {
    if (dimensione == 0) {
        printf("Lista spesa vuota!\n");
        return;
    }
    
    printf("\n=== LISTA SPESA ===\n");
    printf("%-20s | Prezzo | Qnt | Subtotale\n", "Prodotto");
    printf("------------------------------------------------\n");
    
    for (int i = 0; i < dimensione; i++) {
        float subtotale = lista[i].prezzo * lista[i].quantita;
        printf("%-20s | €%5.2f | %3d | €%8.2f\n",
               lista[i].nome, lista[i].prezzo, 
               lista[i].quantita, subtotale);
    }
}

void calcola_totale(Prodotto *lista, int dimensione) {
    if (dimensione == 0) {
        printf("Lista spesa vuota!\n");
        return;
    }
    
    float totale = 0;
    int pezzi_totali = 0;
    
    for (int i = 0; i < dimensione; i++) {
        totale += lista[i].prezzo * lista[i].quantita;
        pezzi_totali += lista[i].quantita;
    }
    
    printf("\n--- RIEPILOGO ---\n");
    printf("Prodotti diversi: %d\n", dimensione);
    printf("Pezzi totali: %d\n", pezzi_totali);
    printf("TOTALE SPESA: €%.2f\n", totale);
    printf("----------------\n");
}

void modifica_quantita(Prodotto *lista, int dimensione) {
    if (dimensione == 0) {
        printf("Lista spesa vuota!\n");
        return;
    }
    
    char nome_cerca[MAX_NOME];
    printf("Quale prodotto vuoi modificare? ");
    scanf("%29s", nome_cerca);
    
    for (int i = 0; i < dimensione; i++) {
        if (strcmp(lista[i].nome, nome_cerca) == 0) {
            printf("Quantità attuale di '%s': %d\n", 
                   lista[i].nome, lista[i].quantita);
            
            int nuova_quantita;
            do {
                printf("Nuova quantità: ");
                scanf("%d", &nuova_quantita);
                if (nuova_quantita <= 0) {
                    printf("La quantità deve essere positiva!\n");
                }
            } while (nuova_quantita <= 0);
            
            lista[i].quantita = nuova_quantita;
            printf("Quantità aggiornata!\n");
            return;
        }
    }
    
    printf("Prodotto '%s' non trovato nella lista!\n", nome_cerca);
}
```

---

## 7.10 Riepilogo

✅ **Cosa hai imparato:**
- I puntatori contengono indirizzi di memoria
- `&` per ottenere l'indirizzo, `*` per accedere al valore
- Passaggio per riferimento alle funzioni
- Array e puntatori sono strettamente collegati
- Allocazione dinamica con `malloc()` e `free()`
- Come evitare errori comuni con i puntatori

✅ **Cosa sai fare ora:**
- Modificare variabili attraverso funzioni
- Creare array di dimensione variabile
- Gestire memoria dinamicamente
- Implementare strutture dati flessibili
- Passare array efficientemente alle funzioni

---

**Prossimo modulo:** Imparerai a lavorare con i **file** per salvare e caricare dati!
