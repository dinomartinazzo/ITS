# Modulo 5: Funzioni
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Capire cosa sono le funzioni e perché sono utili
- Creare funzioni semplici che restituiscono valori
- Creare funzioni che ricevono parametri
- Organizzare il codice in moduli riutilizzabili
- Capire il concetto di scope delle variabili

---

## 5.1 Che cosa sono le Funzioni?

Una **funzione** è come una "scatola magica" che:
- Riceve degli **ingredienti** (parametri)
- Fa qualcosa con questi ingredienti
- Restituisce un **risultato**

### Analogia della Cucina:
```
Funzione: "Fai Toast"
Ingredienti: pane, burro, marmellata
Processo: spalma burro, aggiungi marmellata, tosta
Risultato: toast pronto
```

### Nel Codice:
```c
int somma(int a, int b) {    // Riceve due numeri
    int risultato = a + b;   // Li somma
    return risultato;        // Restituisce il risultato
}
```

**Vantaggi delle funzioni:**
- ✅ **Riutilizzo**: scrivi una volta, usa molte volte
- ✅ **Organizzazione**: codice più pulito e leggibile
- ✅ **Testing**: più facile trovare e correggere errori
- ✅ **Collaborazione**: diverse persone lavorano su funzioni diverse

---

## 5.2 La Prima Funzione

### Funzione Senza Parametri:
```c
#include <stdio.h>

void saluta() {
    printf("Ciao! Benvenuto nel programma!\n");
    printf("Spero ti diverta!\n");
}

int main() {
    saluta();  // Chiama la funzione
    
    printf("Iniziamo...\n");
    
    saluta();  // La chiama di nuovo!
    
    return 0;
}
```

**Spiegazione:**
- `void` = la funzione non restituisce nulla
- `saluta()` = nome della funzione + parentesi vuote
- Per usarla: scrivi `saluta();`

---

## 5.3 Funzioni che Restituiscono Valori

### Funzione Semplice:
```c
#include <stdio.h>

int quadrato(int numero) {
    int risultato = numero * numero;
    return risultato;
}

int main() {
    int x = 5;
    int y = quadrato(x);
    
    printf("Il quadrato di %d è %d\n", x, y);
    
    // Posso usarla direttamente:
    printf("Il quadrato di 7 è %d\n", quadrato(7));
    
    return 0;
}
```

### Calcolatrice con Funzioni:
```c
#include <stdio.h>

int addizione(int a, int b) {
    return a + b;
}

int sottrazione(int a, int b) {
    return a - b;
}

int moltiplicazione(int a, int b) {
    return a * b;
}

float divisione(int a, int b) {
    if (b != 0) {
        return (float)a / b;
    } else {
        printf("Errore: divisione per zero!\n");
        return 0;
    }
}

int main() {
    int num1 = 10, num2 = 3;
    
    printf("%d + %d = %d\n", num1, num2, addizione(num1, num2));
    printf("%d - %d = %d\n", num1, num2, sottrazione(num1, num2));
    printf("%d × %d = %d\n", num1, num2, moltiplicazione(num1, num2));
    printf("%d ÷ %d = %.2f\n", num1, num2, divisione(num1, num2));
    
    return 0;
}
```

---

## 5.4 Tipi di Funzioni

### Funzioni che Non Restituiscono Nulla (void):
```c
void stampa_linea() {
    printf("======================\n");
}

void stampa_messaggio(char messaggio[]) {
    printf("*** %s ***\n", messaggio);
}
```

### Funzioni che Restituiscono Diversi Tipi:
```c
#include <stdio.h>

int massimo(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

float media(float a, float b) {
    return (a + b) / 2.0;
}

char voto_lettera(int voto) {
    if (voto >= 90) return 'A';
    else if (voto >= 80) return 'B';
    else if (voto >= 70) return 'C';
    else if (voto >= 60) return 'D';
    else return 'F';
}

int main() {
    printf("Massimo tra 15 e 23: %d\n", massimo(15, 23));
    printf("Media di 8.5 e 7.2: %.2f\n", media(8.5, 7.2));
    printf("Voto 85 corrisponde a: %c\n", voto_lettera(85));
    
    return 0;
}
```

---

## 5.5 Funzioni con Più Parametri

```c
#include <stdio.h>

float area_rettangolo(float lunghezza, float larghezza) {
    return lunghezza * larghezza;
}

float volume_scatola(float lunghezza, float larghezza, float altezza) {
    return lunghezza * larghezza * altezza;
}

void stampa_info_studente(char nome[], int eta, float media) {
    printf("=== STUDENTE ===\n");
    printf("Nome: %s\n", nome);
    printf("Età: %d anni\n", eta);
    printf("Media: %.2f\n", media);
    printf("================\n");
}

int main() {
    // Test area rettangolo
    float area = area_rettangolo(5.0, 3.0);
    printf("Area del rettangolo: %.2f m²\n", area);
    
    // Test volume scatola
    float volume = volume_scatola(2.0, 3.0, 4.0);
    printf("Volume della scatola: %.2f m³\n", volume);
    
    // Test info studente
    stampa_info_studente("Mario", 19, 8.7);
    
    return 0;
}
```

---

## 5.6 Scope delle Variabili

### Variabili Locali:
```c
#include <stdio.h>

int raddoppia(int numero) {
    int risultato = numero * 2;  // Variabile locale alla funzione
    return risultato;
}

int main() {
    int x = 5;
    int y = raddoppia(x);
    
    printf("x = %d, y = %d\n", x, y);
    
    // printf("%d", risultato);  // ERRORE! risultato non esiste qui
    
    return 0;
}
```

### Variabili Globali:
```c
#include <stdio.h>

int contatore = 0;  // Variabile globale

void incrementa() {
    contatore++;    // Può accedere alla variabile globale
    printf("Contatore: %d\n", contatore);
}

int main() {
    printf("Inizio: %d\n", contatore);
    
    incrementa();
    incrementa();
    incrementa();
    
    printf("Fine: %d\n", contatore);
    
    return 0;
}
```

---

## 5.7 Esercizi Pratici

### 🎯 Esercizio 5.1: Funzioni Matematiche
```c
#include <stdio.h>

int potenza(int base, int esponente) {
    int risultato = 1;
    for (int i = 0; i < esponente; i++) {
        risultato *= base;
    }
    return risultato;
}

int fattoriale(int n) {
    int risultato = 1;
    for (int i = 1; i <= n; i++) {
        risultato *= i;
    }
    return risultato;
}

int pari(int numero) {
    return (numero % 2 == 0);  // Restituisce 1 se pari, 0 se dispari
}

int main() {
    printf("2^5 = %d\n", potenza(2, 5));
    printf("5! = %d\n", fattoriale(5));
    printf("10 è pari? %s\n", pari(10) ? "Sì" : "No");
    printf("7 è pari? %s\n", pari(7) ? "Sì" : "No");
    
    return 0;
}
```

### 🎯 Esercizio 5.2: Validazione Input
```c
#include <stdio.h>

int leggi_numero_valido(int min, int max) {
    int numero;
    
    do {
        printf("Inserisci un numero tra %d e %d: ", min, max);
        scanf("%d", &numero);
        
        if (numero < min || numero > max) {
            printf("Numero non valido! Riprova.\n");
        }
    } while (numero < min || numero > max);
    
    return numero;
}

void stampa_menu() {
    printf("\n=== MENU ===\n");
    printf("1. Saluta\n");
    printf("2. Calcola quadrato\n");
    printf("3. Esci\n");
}

int main() {
    int scelta;
    
    do {
        stampa_menu();
        scelta = leggi_numero_valido(1, 3);
        
        switch (scelta) {
            case 1:
                printf("Ciao! Come va?\n");
                break;
            case 2: {
                int numero = leggi_numero_valido(1, 100);
                printf("Il quadrato di %d è %d\n", numero, numero * numero);
                break;
            }
            case 3:
                printf("Arrivederci!\n");
                break;
        }
    } while (scelta != 3);
    
    return 0;
}
```

---

## 5.8 Funzioni Ricorsive (Avanzato)

Una funzione può chiamare **se stessa**! Questo si chiama ricorsione.

### Esempio: Conto alla Rovescia
```c
#include <stdio.h>

void countdown(int numero) {
    if (numero > 0) {
        printf("%d\n", numero);
        countdown(numero - 1);  // Chiama se stessa con numero - 1
    } else {
        printf("Via!\n");
    }
}

int main() {
    countdown(5);
    return 0;
}
```

### Esempio: Fattoriale Ricorsivo
```c
#include <stdio.h>

int fattoriale_ricorsivo(int n) {
    if (n <= 1) {
        return 1;  // Caso base
    } else {
        return n * fattoriale_ricorsivo(n - 1);  // Chiamata ricorsiva
    }
}

int main() {
    int numero = 5;
    printf("%d! = %d\n", numero, fattoriale_ricorsivo(numero));
    return 0;
}
```

---

## 5.9 Prototipo delle Funzioni

A volte devi "annunciare" una funzione prima di usarla:

```c
#include <stdio.h>

// Prototipi (dichiarazioni)
int somma(int a, int b);
void saluta(void);

int main() {
    saluta();
    printf("5 + 3 = %d\n", somma(5, 3));
    return 0;
}

// Definizioni (implementazioni)
int somma(int a, int b) {
    return a + b;
}

void saluta(void) {
    printf("Ciao!\n");
}
```

**Perché i prototipi?**
- Il compilatore sa che le funzioni esistono
- Puoi mettere `main()` all'inizio
- Codice più organizzato

---

## 🎯 Progetto del Modulo: "Sistema di Gestione Voti"

```c
#include <stdio.h>

// Prototipi
void stampa_menu(void);
float calcola_media(float voti[], int numero_voti);
char voto_letterale(float media);
void stampa_statistiche(float voti[], int numero_voti);
float leggi_voto(void);

int main() {
    float voti[10];  // Massimo 10 voti
    int numero_voti = 0;
    int scelta;
    
    printf("=== SISTEMA GESTIONE VOTI ===\n");
    
    do {
        stampa_menu();
        printf("Scegli (1-5): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1: {
                if (numero_voti < 10) {
                    voti[numero_voti] = leggi_voto();
                    numero_voti++;
                    printf("Voto aggiunto!\n");
                } else {
                    printf("Massimo 10 voti raggiunto!\n");
                }
                break;
            }
            case 2: {
                if (numero_voti > 0) {
                    float media = calcola_media(voti, numero_voti);
                    printf("La tua media è: %.2f (%c)\n", media, voto_letterale(media));
                } else {
                    printf("Nessun voto inserito!\n");
                }
                break;
            }
            case 3:
                stampa_statistiche(voti, numero_voti);
                break;
            case 4:
                numero_voti = 0;
                printf("Tutti i voti cancellati!\n");
                break;
            case 5:
                printf("Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 5);
    
    return 0;
}

void stampa_menu(void) {
    printf("\n--- MENU ---\n");
    printf("1. Aggiungi voto\n");
    printf("2. Mostra media\n");
    printf("3. Statistiche\n");
    printf("4. Cancella tutto\n");
    printf("5. Esci\n");
}

float leggi_voto(void) {
    float voto;
    
    do {
        printf("Inserisci voto (0.0-10.0): ");
        scanf("%f", &voto);
        
        if (voto < 0.0 || voto > 10.0) {
            printf("Voto non valido!\n");
        }
    } while (voto < 0.0 || voto > 10.0);
    
    return voto;
}

float calcola_media(float voti[], int numero_voti) {
    float somma = 0;
    
    for (int i = 0; i < numero_voti; i++) {
        somma += voti[i];
    }
    
    return somma / numero_voti;
}

char voto_letterale(float media) {
    if (media >= 9.0) return 'A';
    else if (media >= 8.0) return 'B';
    else if (media >= 7.0) return 'C';
    else if (media >= 6.0) return 'D';
    else return 'F';
}

void stampa_statistiche(float voti[], int numero_voti) {
    if (numero_voti == 0) {
        printf("Nessun voto da mostrare!\n");
        return;
    }
    
    printf("\n=== STATISTICHE ===\n");
    printf("Numero voti: %d\n", numero_voti);
    
    // Tutti i voti
    printf("Voti: ");
    for (int i = 0; i < numero_voti; i++) {
        printf("%.1f ", voti[i]);
    }
    printf("\n");
    
    // Media
    float media = calcola_media(voti, numero_voti);
    printf("Media: %.2f (%c)\n", media, voto_letterale(media));
    
    // Voto più alto e più basso
    float minimo = voti[0], massimo = voti[0];
    for (int i = 1; i < numero_voti; i++) {
        if (voti[i] < minimo) minimo = voti[i];
        if (voti[i] > massimo) massimo = voti[i];
    }
    
    printf("Voto minimo: %.1f\n", minimo);
    printf("Voto massimo: %.1f\n", massimo);
    printf("==================\n");
}
```

---

## 5.10 Riepilogo

✅ **Cosa hai imparato:**
- Le funzioni organizzano il codice in blocchi riutilizzabili
- Tipi di funzioni: void, int, float, char
- Parametri per passare dati alle funzioni
- Return per restituire risultati
- Scope locale vs globale
- Prototipi per organizzare il codice

✅ **Cosa sai fare ora:**
- Scomporre problemi complessi in funzioni semplici
- Creare codice modulare e riutilizzabile
- Validare input con funzioni dedicate
- Organizzare programmi grandi e complessi
- Implementare algoritmi con approccio modulare

---

**Prossimo modulo:** Imparerai gli **array** per gestire collezioni di dati!
