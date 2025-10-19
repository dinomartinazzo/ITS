# Modulo 1: Fondamenti della Programmazione C
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Comprendere cos'è la programmazione
- Capire le caratteristiche del linguaggio C
- Installare e configurare l'ambiente di sviluppo
- Scrivere, compilare ed eseguire il tuo primo programma

---

## 1.1 Che cos'è la Programmazione?

Cosa è la **Programmazione**?
La programmazione è l'arte di dare istruzioni precise a un computer per risolvere problemi. Un programma è una sequenza di istruzioni che il computer può eseguire.
Perché il Linguaggio C?
Il linguaggio C, sviluppato da Dennis Ritchie nel 1972, è:

Fondamentale: Base per linguaggi come C++, Java, JavaScript
Efficiente: Controllo diretto dell'hardware
Portabile: Funziona su qualsiasi sistema
Procedurale: Approccio strutturato alla risoluzione dei problemi
Compilato: Il codice viene trasformato in linguaggio macchina

### Esempio della vita reale:
```
Ricetta per fare un panino:
1. Prendi 2 fette di pane
2. Spalma il burro sulla prima fetta
3. Metti il prosciutto sopra
4. Copri con la seconda fetta
```

### Lo stesso concetto in programmazione:
```c
1. Chiedi all'utente di inserire un numero
2. Moltiplica il numero per 2
3. Mostra il risultato
```

---

## 1.2 Perché il Linguaggio C?

Il **C** è come l'italiano della programmazione: se lo sai, ti è più facile imparare altre "lingue" (linguaggi).

### Vantaggi del C:
- ✅ **Semplice**: poche regole da ricordare
- ✅ **Veloce**: i programmi sono molto efficienti
- ✅ **Universale**: funziona su qualsiasi computer
- ✅ **Fondamentale**: base per C++, Java, JavaScript

### Dove si usa il C:
- Sistemi operativi (Windows, Linux)
- Videogiochi
- App per smartphone
- Programmi per banche
- Software per ospedali

---

## 1.3 Come Funziona un Programma C

```
Codice C (.c) → Compilatore → Programma Eseguibile
     ↑              ↑                    ↑
  Lo scrivi tu   Lo fa gcc         Lo esegui tu
```

### Analogia:
- **Codice C** = Ricetta scritta in italiano
- **Compilatore** = Traduttore che la trasforma in cinese
- **Programma** = Ricetta in cinese che il computer (cinese) può seguire

---

## 1.4 Installazione dell'Ambiente

### Su Windows:
1. Scarica **Dev-C++** (gratuito e semplice)
2. Installa seguendo le istruzioni
3. Apri il programma

### Su Linux/Mac:
```bash
# Installa il compilatore
sudo apt install gcc    # Ubuntu
brew install gcc        # Mac

# Editor consigliato
code nomefile.c         # Visual Studio Code
```

### Online (per iniziare subito):
- **Replit.com** 
- **OnlineGDB.com**
- **Programiz C Compiler**

---

## 1.5 Il Primo Programma: "Ciao Mondo!"

Ecco il programma più famoso del mondo:

```c
#include <stdio.h>

int main() {
    printf("Ciao Mondo!\n");
    return 0;
}
```

### Spiegazione riga per riga:

**Riga 1:** `#include <stdio.h>`
- Dice al computer: "Prendi la scatola degli attrezzi per scrivere e leggere"
- Come dire "Prendi la cassetta degli attrezzi" prima di riparare qualcosa

**Riga 3:** `int main() {`
- È il **punto di partenza** del programma
- Come dire "Inizia qui!"

**Riga 4:** `printf("Ciao Mondo!\n");`
- **printf** = "stampa sullo schermo"
- Le parole tra `""` sono quello che apparirà
- `\n` = vai a capo (nuova riga)
- `;` = fine dell'istruzione (come il punto in italiano)

**Riga 5:** `return 0;`
- Dice al computer "Ho finito, tutto è andato bene"
- Come dire "Arrivederci!" al computer

**Riga 6:** `}`
- Chiude il programma (come chiudere una parentesi)

---

## 1.6 Come Compilare ed Eseguire

### Metodo 1: Con Dev-C++
1. Scrivi il codice
2. Salva il file come `primo.c`
3. Premi **F9** (Compile & Run)
4. Vedi il risultato!

### Metodo 2: Da Terminale
```bash
# Compila il programma
gcc primo.c -o primo

# Esegui il programma
./primo        # Linux/Mac
primo.exe      # Windows
```

### Cosa vedrai:
```
Ciao Mondo!
```

---

## 1.7 Esercizi Pratici

### 🎯 Esercizio 1.1: Il Tuo Nome
Modifica il programma per stampare il tuo nome:

```c
#include <stdio.h>

int main() {
    printf("Ciao, io sono Mario!\n");
    return 0;
}
```

### 🎯 Esercizio 1.2: Più Righe
Scrivi un programma che stampi 3 righe:

```c
#include <stdio.h>

int main() {
    printf("Prima riga\n");
    printf("Seconda riga\n");
    printf("Terza riga\n");
    return 0;
}
```

**Risultato:**
```
Prima riga
Seconda riga
Terza riga
```

### 🎯 Esercizio 1.3: La Tua Presentazione
Crea un programma che stampi:
- Il tuo nome
- La tua età
- La tua città
- Il tuo hobby preferito

**Esempio:**
```c
#include <stdio.h>

int main() {
    printf("Mi chiamo Anna\n");
    printf("Ho 19 anni\n");
    printf("Vivo a Milano\n");
    printf("Mi piace suonare la chitarra\n");
    return 0;
}
```

---

## 1.8 Errori Comuni e Come Risolverli

### ❌ Errore: "stdio.h not found"
**Causa:** Hai dimenticato `#include <stdio.h>`
**Soluzione:** Aggiungi sempre questa riga all'inizio!

### ❌ Errore: "main not found"
**Causa:** Hai scritto `Main` invece di `main` (maiuscola/minuscola)
**Soluzione:** In C tutto è **case sensitive**!

### ❌ Errore: "expected ;"
**Causa:** Hai dimenticato il `;` alla fine di una riga
**Soluzione:** Ogni istruzione finisce con `;`

### ❌ Il programma non stampa niente
**Causa:** Hai dimenticato `\n` o hai errori di sintassi
**Soluzione:** Controlla le virgolette e i punti e virgola

---

## 1.9 Trucchi Utili

### 💡 Commenti
Usa i commenti per spiegare il tuo codice:

```c
#include <stdio.h>

int main() {
    // Questo è un commento: stampa un saluto
    printf("Ciao!\n");
    
    /* Questo è un commento
       su più righe */
    printf("Arrivederci!\n");
    
    return 0;
}
```

### 💡 Caratteri Speciali
- `\n` = nuova riga
- `\t` = tab (spazio grande)
- `\"` = virgolette nel testo

```c
printf("Ciao\tMondo\n");     // Ciao    Mondo
printf("Lui disse: \"Ciao!\"\n");  // Lui disse: "Ciao!"
```

---

## 1.10 Riepilogo

✅ **Cosa hai imparato:**
- Cos'è un programma
- Come funziona il linguaggio C  
- Come installare gli strumenti
- Come scrivere il primo programma
- Come compilare ed eseguire
- Come risolvere errori comuni

✅ **Cosa sai fare ora:**
- Scrivere programmi semplici che stampano testo
- Compilare ed eseguire codice C
- Aggiungere commenti al codice
- Correggere errori di base

---

## 🎯 Progetto del Modulo: "La Mia Carta d'Identità"

Scrivi un programma che stampi la tua carta d'identità digitale:

```c
#include <stdio.h>

int main() {
    printf("========================================\n");
    printf("         CARTA D'IDENTITA' DIGITALE\n");
    printf("========================================\n");
    printf("Nome: Mario\n");
    printf("Cognome: Rossi\n");
    printf("Eta': 19 anni\n");
    printf("Citta': Roma\n");
    printf("Corso: ITS Informatica\n");
    printf("Anno: 2024\n");
    printf("========================================\n");
    printf("Programmatore in erba dal: oggi!\n");
    return 0;
}
```

---

**Prossimo modulo:** Imparerai a usare le **variabili** per memorizzare dati e renderli modificabili!
