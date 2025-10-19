# Modulo 3: Decisioni e Controllo del Flusso
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Usare `if` ed `else` per prendere decisioni
- Confrontare valori con operatori relazionali
- Combinare condizioni con operatori logici
- Usare `switch` per menu a scelta multipla
- Creare programmi che si comportano diversamente in base ai dati

---

## 3.1 Prendere Decisioni: if-else

Nella vita reale prendiamo decisioni continuamente:
```
SE piove ALLORA prendo l'ombrello
ALTRIMENTI porto gli occhiali da sole
```

In C facciamo la stessa cosa:

```c
#include <stdio.h>

int main() {
    int eta;
    
    printf("Quanti anni hai? ");
    scanf("%d", &eta);
    
    if (eta >= 18) {
        printf("Sei maggiorenne! Puoi guidare.\n");
    } else {
        printf("Sei minorenne. Non puoi ancora guidare.\n");
    }
    
    return 0;
}
```

### Spiegazione:
- `if (condizione)` = "se la condizione è vera"
- `else` = "altrimenti"
- Le `{}` racchiudono cosa fare in ogni caso

---

## 3.2 Operatori di Confronto

Per confrontare i valori usiamo questi simboli:

| Operatore | Significato | Esempio | Risultato |
|-----------|-------------|---------|-----------|
| `==` | Uguale a | `5 == 5` | Vero |
| `!=` | Diverso da | `5 != 3` | Vero |
| `>` | Maggiore di | `7 > 3` | Vero |
| `<` | Minore di | `3 < 7` | Vero |
| `>=` | Maggiore o uguale | `5 >= 5` | Vero |
| `<=` | Minore o uguale | `3 <= 5` | Vero |

### Esempio Pratico:
```c
#include <stdio.h>

int main() {
    int voto;
    
    printf("Che voto hai preso? ");
    scanf("%d", &voto);
    
    if (voto >= 6) {
        printf("Bravo! Sei promosso!\n");
    } else {
        printf("Devi studiare di più!\n");
    }
    
    return 0;
}
```

---

## 3.3 Condizioni Multiple: if-else if-else

Quando hai più di due possibilità:

```c
#include <stdio.h>

int main() {
    int voto;
    
    printf("Che voto hai preso (1-10)? ");
    scanf("%d", &voto);
    
    if (voto >= 9) {
        printf("Ottimo! Sei un genio!\n");
    } else if (voto >= 7) {
        printf("Bravo! Buon lavoro!\n");
    } else if (voto >= 6) {
        printf("Sufficiente, ma puoi fare meglio.\n");
    } else {
        printf("Devi impegnarti di più!\n");
    }
    
    return 0;
}
```

### Come funziona:
1. Controlla la **prima** condizione (`voto >= 9`)
2. Se è falsa, controlla la **seconda** (`voto >= 7`)
3. Se è falsa, controlla la **terza** (`voto >= 6`)  
4. Se tutte sono false, esegue l'`else`

---

## 3.4 Operatori Logici

Per combinare più condizioni:

| Operatore | Significato | Esempio | Quando è vero |
|-----------|-------------|---------|---------------|
| `&&` | AND (e) | `a > 0 && b > 0` | Entrambe vere |
| `\|\|` | OR (o) | `a > 0 \|\| b > 0` | Almeno una vera |
| `!` | NOT (non) | `!(a > 0)` | Condizione falsa |

### Esempio: Controllo Accesso
```c
#include <stdio.h>

int main() {
    int eta;
    char patente;
    
    printf("Quanti anni hai? ");
    scanf("%d", &eta);
    
    printf("Hai la patente? (s/n): ");
    scanf(" %c", &patente);  // Nota lo spazio prima di %c
    
    if (eta >= 18 && patente == 's') {
        printf("Puoi guidare!\n");
    } else if (eta < 18) {
        printf("Sei troppo giovane!\n");
    } else {
        printf("Devi prendere la patente!\n");
    }
    
    return 0;
}
```

### Esempio: Sconto Cinema
```c
#include <stdio.h>

int main() {
    int eta;
    float prezzo = 8.0;  // Prezzo normale
    
    printf("Quanti anni hai? ");
    scanf("%d", &eta);
    
    // Sconto per bambini (< 12) o anziani (> 65)
    if (eta < 12 || eta > 65) {
        prezzo = prezzo / 2;  // 50% di sconto
        printf("Hai diritto allo sconto!\n");
    }
    
    printf("Il biglietto costa: %.2f euro\n", prezzo);
    
    return 0;
}
```

---

## 3.5 Il Costrutto Switch

Quando hai molte opzioni da scegliere, `switch` è più pulito di tanti `if`:

```c
#include <stdio.h>

int main() {
    int giorno;
    
    printf("Inserisci il numero del giorno (1-7): ");
    scanf("%d", &giorno);
    
    switch (giorno) {
        case 1:
            printf("Lunedì - Si torna a scuola!\n");
            break;
        case 2:
            printf("Martedì - Andiamo avanti!\n");
            break;
        case 3:
            printf("Mercoledì - Siamo a metà settimana!\n");
            break;
        case 4:
            printf("Giovedì - Quasi weekend!\n");
            break;
        case 5:
            printf("Venerdì - Evviva!\n");
            break;
        case 6:
            printf("Sabato - Weekend!\n");
            break;
        case 7:
            printf("Domenica - Relax!\n");
            break;
        default:
            printf("Numero non valido!\n");
            break;
    }
    
    return 0;
}
```

### 🚨 Importante: Il `break`
- Senza `break`, il programma continua ai casi successivi!
- `default` è come l'`else` - si esegue se nessun caso corrisponde

---

## 3.6 Menu Interattivo

Esempio di menu per una calcolatrice:

```c
#include <stdio.h>

int main() {
    int scelta;
    float num1, num2, risultato;
    
    printf("=== CALCOLATRICE ===\n");
    printf("1. Addizione\n");
    printf("2. Sottrazione\n");
    printf("3. Moltiplicazione\n");
    printf("4. Divisione\n");
    printf("Scegli l'operazione (1-4): ");
    
    scanf("%d", &scelta);
    
    printf("Inserisci primo numero: ");
    scanf("%f", &num1);
    printf("Inserisci secondo numero: ");
    scanf("%f", &num2);
    
    switch (scelta) {
        case 1:
            risultato = num1 + num2;
            printf("%.2f + %.2f = %.2f\n", num1, num2, risultato);
            break;
        case 2:
            risultato = num1 - num2;
            printf("%.2f - %.2f = %.2f\n", num1, num2, risultato);
            break;
        case 3:
            risultato = num1 * num2;
            printf("%.2f × %.2f = %.2f\n", num1, num2, risultato);
            break;
        case 4:
            if (num2 != 0) {
                risultato = num1 / num2;
                printf("%.2f ÷ %.2f = %.2f\n", num1, num2, risultato);
            } else {
                printf("Errore: non si può dividere per zero!\n");
            }
            break;
        default:
            printf("Scelta non valida!\n");
            break;
    }
    
    return 0;
}
```

---

## 3.7 Esercizi Pratici

### 🎯 Esercizio 3.1: Maggiore di Tre
```c
#include <stdio.h>

int main() {
    int a, b, c;
    
    printf("Inserisci tre numeri: ");
    scanf("%d %d %d", &a, &b, &c);
    
    if (a >= b && a >= c) {
        printf("Il maggiore è: %d\n", a);
    } else if (b >= a && b >= c) {
        printf("Il maggiore è: %d\n", b);
    } else {
        printf("Il maggiore è: %d\n", c);
    }
    
    return 0;
}
```

### 🎯 Esercizio 3.2: Pari o Dispari
```c
#include <stdio.h>

int main() {
    int numero;
    
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    if (numero % 2 == 0) {
        printf("%d è pari\n", numero);
    } else {
        printf("%d è dispari\n", numero);
    }
    
    return 0;
}
```

### 🎯 Esercizio 3.3: Calcolatore Tasse
```c
#include <stdio.h>

int main() {
    float stipendio, tasse;
    
    printf("Inserisci il tuo stipendio annuo: ");
    scanf("%f", &stipendio);
    
    if (stipendio <= 15000) {
        tasse = 0;  // Nessuna tassa
    } else if (stipendio <= 30000) {
        tasse = stipendio * 0.20;  // 20%
    } else {
        tasse = stipendio * 0.30;  // 30%
    }
    
    printf("Stipendio: %.2f euro\n", stipendio);
    printf("Tasse da pagare: %.2f euro\n", tasse);
    printf("Stipendio netto: %.2f euro\n", stipendio - tasse);
    
    return 0;
}
```

---

## 3.8 Operatore Ternario (Avanzato)

Una scorciatoia per `if-else` semplici:

```c
#include <stdio.h>

int main() {
    int numero;
    
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    // Invece di if-else:
    // if (numero >= 0) {
    //     printf("Positivo");
    // } else {
    //     printf("Negativo");
    // }
    
    // Puoi scrivere:
    printf("Il numero è: %s\n", (numero >= 0) ? "Positivo" : "Negativo");
    
    return 0;
}
```

**Sintassi:** `condizione ? valore_se_vero : valore_se_falso`

---

## 3.9 Errori Comuni

### ❌ Usare = invece di ==
```c
// SBAGLIATO:
if (x = 5) {  // Assegna 5 a x!
    
// GIUSTO:
if (x == 5) {  // Controlla se x è uguale a 5
```

### ❌ Dimenticare le graffe
```c
// RISCHIO:
if (condizione)
    printf("Prima riga\n");
    printf("Seconda riga\n");  // Questa si esegue sempre!

// SICURO:
if (condizione) {
    printf("Prima riga\n");
    printf("Seconda riga\n");  // Entrambe dentro l'if
}
```

### ❌ Dimenticare break in switch
```c
// SBAGLIATO:
switch (scelta) {
    case 1:
        printf("Uno\n");  // Senza break, continua al caso 2!
    case 2:
        printf("Due\n");
        break;
}

// GIUSTO:
switch (scelta) {
    case 1:
        printf("Uno\n");
        break;  // Esce dallo switch
    case 2:
        printf("Due\n");
        break;
}
```

---

## 🎯 Progetto del Modulo: "Indovina il Numero"

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int numero_segreto, tentativo, tentativi_rimasti;
    
    // Inizializza il generatore casuale
    srand(time(NULL));
    numero_segreto = rand() % 100 + 1;  // Numero da 1 a 100
    
    tentativi_rimasti = 7;
    
    printf("=== INDOVINA IL NUMERO ===\n");
    printf("Ho pensato a un numero da 1 a 100.\n");
    printf("Hai %d tentativi per indovinarlo!\n\n", tentativi_rimasti);
    
    while (tentativi_rimasti > 0) {
        printf("Tentativo %d - Inserisci il tuo numero: ", 8 - tentativi_rimasti);
        scanf("%d", &tentativo);
        
        if (tentativo == numero_segreto) {
            printf("🎉 BRAVO! Hai indovinato!\n");
            printf("Il numero era proprio %d!\n", numero_segreto);
            return 0;  // Esce dal programma
        } else if (tentativo < numero_segreto) {
            printf("📈 Troppo basso!\n");
        } else {
            printf("📉 Troppo alto!\n");
        }
        
        tentativi_rimasti--;
        
        if (tentativi_rimasti > 0) {
            printf("Ti restano %d tentativi.\n\n", tentativi_rimasti);
        }
    }
    
    printf("😞 Hai finito i tentativi!\n");
    printf("Il numero era %d. Ritenta!\n", numero_segreto);
    
    return 0;
}
```

---

## 3.10 Riepilogo

✅ **Cosa hai imparato:**
- Come prendere decisioni con `if`, `else`, `else if`
- Operatori di confronto (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Operatori logici (`&&`, `||`, `!`)
- Menu a scelta multipla con `switch`
- Come creare programmi interattivi

✅ **Cosa sai fare ora:**
- Creare programmi che si comportano diversamente in base ai dati
- Validare l'input degli utenti
- Creare menu e calcolatrici
- Combinare condizioni complesse

---

**Prossimo modulo:** Imparerai i **cicli** per ripetere operazioni automaticamente!
