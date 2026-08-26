# 📘 DISPENSA COMPLETA - MODULO 5
# Verifica Finale del Corso
## Intelligenza Artificiale e Programmazione Assistita
## Corso ITS - Valutazione Completa delle Competenze
### Durata: 2 ore | Livello: Valutazione Finale

---

## 📑 Indice del Modulo

1. [Introduzione alla Verifica](#1-introduzione-alla-verifica)
2. [Struttura della Verifica](#2-struttura-della-verifica)
3. [Sezione A: Fondamenti IA](#3-sezione-a-fondamenti-ia)
4. [Sezione B: Programmazione Assistita](#4-sezione-b-programmazione-assistita)
5. [Sezione C: Programmazione in C](#5-sezione-c-programmazione-in-c)
6. [Sezione D: Arduino e Embedded](#6-sezione-d-arduino-e-embedded)
7. [Sezione E: Progetto Integrato](#7-sezione-e-progetto-integrato)
8. [Criteri di Valutazione](#8-criteri-di-valutazione)
9. [Soluzioni e Spiegazioni](#9-soluzioni-e-spiegazioni)
10. [Preparazione alla Verifica](#10-preparazione-alla-verifica)

---

## 1. Introduzione alla Verifica

### 1.1 Obiettivo della Verifica Finale

La verifica finale ha l'obiettivo di valutare in modo completo e strutturato le competenze acquisite durante i quattro moduli del corso:

- **Modulo 1**: Fondamenti di Intelligenza Artificiale
- **Modulo 2**: Tecniche di Programmazione Assistita
- **Modulo 3**: Programmazione in C con Supporto IA
- **Modulo 4**: Programmazione Arduino con Supporto IA

La verifica non è solo un test di conoscenze teoriche, ma una **valutazione pratica** delle capacità di:
- Utilizzare l'IA come strumento professionale
- Analizzare criticamente codice generato
- Progettare soluzioni embedded complete
- Applicare best practices ingegneristiche

### 1.2 Modalità di Svolgimento

```
INFORMAZIONI GENERALI:
┌─────────────────────────────────────┐
│ Durata totale:    2 ore             │
│ Tipo:             Misto (teoria +   │
│                   pratica)          │
│ Strumenti:        Computer, Arduino,│
│                   LLM consentito    │
│ Consultazione:    Dispense SI,      │
│                   Internet NO       │
│ Punteggio totale: 100 punti         │
│ Sufficienza:      60/100            │
└─────────────────────────────────────┘
```

**Importante**: L'uso di IA è **CONSENTITO E INCORAGGIATO**, ma verrà valutata la capacità di:
- Formulare prompt efficaci
- Validare criticamente l'output
- Integrare correttamente il codice generato

### 1.3 Materiale Consentito

✅ **CONSENTITO:**
- Dispense del corso (Moduli 1-4)
- Editor/IDE (VSCode, Arduino IDE)
- Accesso a LLM (ChatGPT, Claude, ecc.)
- Appunti personali
- Arduino e componenti hardware

❌ **NON CONSENTITO:**
- Ricerche web generiche
- Comunicazione con altri studenti
- Codice pre-scritto non generato durante la verifica
- Soluzioni di esercizi precedenti (se non rielaborate)

### 1.4 Come Prepararsi

**Una settimana prima:**
- [ ] Ripassare tutte le dispense
- [ ] Rivedere esercizi svolti
- [ ] Testare hardware Arduino
- [ ] Verificare software installati

**Il giorno prima:**
- [ ] Dormire bene (8 ore)
- [ ] Preparare workspace organizzato
- [ ] Caricare eventuali librerie Arduino
- [ ] Rileggere checklist best practices

**Durante la verifica:**
- [ ] Leggere TUTTO prima di iniziare
- [ ] Gestire bene il tempo (massimo 30 min per sezione)
- [ ] Validare SEMPRE il codice generato da IA
- [ ] Documentare scelte progettuali

---

## 2. Struttura della Verifica

### 2.1 Distribuzione Punteggi

```
STRUTTURA COMPLETA:
┌──────────────────────────────────────────┐
│ SEZIONE A - Fondamenti IA                │
│   6 domande a scelta multipla            │
│   Punteggio: 18 punti (3 pt cad.)       │
│   Tempo consigliato: 15 minuti          │
├──────────────────────────────────────────┤
│ SEZIONE B - Programmazione Assistita    │
│   5 domande aperte brevi                 │
│   Punteggio: 15 punti (3 pt cad.)       │
│   Tempo consigliato: 20 minuti          │
├──────────────────────────────────────────┤
│ SEZIONE C - Programmazione C             │
│   3 esercizi pratici                     │
│   Punteggio: 27 punti (9 pt cad.)       │
│   Tempo consigliato: 35 minuti          │
├──────────────────────────────────────────┤
│ SEZIONE D - Arduino                      │
│   3 esercizi pratici                     │
│   Punteggio: 20 punti (variabili)       │
│   Tempo consigliato: 30 minuti          │
├──────────────────────────────────────────┤
│ SEZIONE E - Progetto Integrato           │
│   1 progetto completo                    │
│   Punteggio: 20 punti                    │
│   Tempo consigliato: 20 minuti          │
├──────────────────────────────────────────┤
│ TOTALE: 100 punti | 120 minuti          │
└──────────────────────────────────────────┘
```

### 2.2 Livelli di Difficoltà

Ogni sezione contiene esercizi di difficoltà crescente:

- **Base (40%)**: Conoscenze fondamentali, applicazione diretta
- **Intermedio (40%)**: Integrazione concetti, problem solving
- **Avanzato (20%)**: Pensiero critico, ottimizzazione, design

### 2.3 Criteri Generali

Ogni risposta/esercizio viene valutato su:

1. **Correttezza (50%)**: Funziona? È tecnicamente corretto?
2. **Qualità (30%)**: Codice leggibile, best practices, robustezza
3. **Completezza (20%)**: Gestione errori, edge cases, documentazione

---

## 3. Sezione A: Fondamenti IA

**Istruzioni**: Scegli la risposta corretta per ogni domanda. Una sola risposta è corretta.

**Punteggio**: 18 punti totali (3 punti per domanda)

**Tempo consigliato**: 15 minuti

---

### Domanda A1 (3 punti)

Quale delle seguenti affermazioni descrive correttamente il funzionamento di un Large Language Model (LLM)?

A) Un LLM ragiona logicamente come un essere umano, deducendo conclusioni da premesse  
B) Un LLM cerca nel suo database interno e copia frasi esistenti  
C) Un LLM predice il token successivo più probabile basandosi su pattern statistici appresi dai dati di training  
D) Un LLM esegue ricerche su internet in tempo reale per ogni risposta  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: C**

**Spiegazione:**
Gli LLM funzionano tramite predizione probabilistica token-per-token. Non "ragionano" nel senso logico (A è falsa), non hanno un database di frasi da copiare (B è falsa), e non accedono a internet a meno che non abbiano tool specifici (D è falsa nella maggior parte dei casi).

**Punti chiave:**
- Predizione statistica, non deduzione logica
- Apprendimento da pattern nei dati di training
- Generazione probabilistica, non deterministica

</details>

---

### Domanda A2 (3 punti)

Cos'è un'"allucinazione" nel contesto dei modelli di linguaggio?

A) Un errore di compilazione nel codice generato  
B) La generazione di informazioni plausibili ma inventate o errate  
C) Un malfunzionamento hardware del server che esegue il modello  
D) La tendenza del modello a ripetere la stessa risposta  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: B**

**Spiegazione:**
Un'allucinazione è quando l'LLM genera contenuti che sembrano plausibili e ben formulati, ma sono in realtà inventati o fattualmente errati. Questo accade perché il modello predice ciò che è statisticamente probabile, non ciò che è vero.

**Esempio:**
```
Prompt: "Chi ha vinto il Nobel per la Fisica nel 2087?"
Output (allucinazione): "Nel 2087, Maria Rossi ha vinto il Nobel 
per la scoperta della fusione fredda."

Problema: 2087 è nel futuro! Il modello ha inventato un nome 
e un'informazione plausibile.
```

</details>

---

### Domanda A3 (3 punti)

Quale tipo di machine learning è più appropriato per raggruppare clienti con comportamenti simili SENZA avere etichette predefinite?

A) Supervised Learning  
B) Unsupervised Learning (Clustering)  
C) Reinforcement Learning  
D) Transfer Learning  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: B**

**Spiegazione:**
L'unsupervised learning, in particolare il clustering, è progettato esattamente per questo: trovare pattern e raggruppamenti naturali nei dati senza etichette predefinite.

**Perché le altre sono sbagliate:**
- A (Supervised): Richiede etichette note a priori
- C (Reinforcement): Per apprendimento tramite trial-error con reward
- D (Transfer): Riuso di modello pre-addestrato, non una categoria base

</details>

---

### Domanda A4 (3 punti)

Quale dei seguenti è un LIMITE tecnico reale dei modelli di IA generativa attuali?

A) Non possono mai generare codice funzionante  
B) Possono generare output statisticamente plausibili ma fattualmente errati  
C) Non possono elaborare più di 100 parole alla volta  
D) Funzionano solo con testo in lingua inglese  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: B**

**Spiegazione:**
I modelli generativi possono e spesso generano codice funzionante (A falsa), gestiscono migliaia di token (C falsa), e supportano molte lingue (D falsa). Tuttavia, il limite fondamentale è che generano output basati su probabilità statistica, non su verità fattuale o comprensione reale.

**Implicazione pratica:**
Questo è il motivo per cui dobbiamo SEMPRE validare l'output dell'IA, specialmente per codice, dati fattuali e informazioni critiche.

</details>

---

### Domanda A5 (3 punti)

Quale applicazione rappresenta un uso reale di Deep Learning in ambito embedded/industriale?

A) Calcolatrice scientifica  
B) Sistema di controllo semafori basato su timer  
C) Riconoscimento difetti su linea produzione tramite computer vision  
D) Algoritmo di ordinamento quicksort  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: C**

**Spiegazione:**
Il riconoscimento visivo di difetti in produzione è un'applicazione reale di Deep Learning (tipicamente CNN - Convolutional Neural Networks) in ambito industriale.

**Perché le altre sono sbagliate:**
- A: Calcoli deterministici, no ML necessario
- B: Logica if/else classica
- D: Algoritmo deterministico classico

**Contesto ITS:**
Questo tipo di applicazione è sempre più richiesta in Industry 4.0 e automazione industriale.

</details>

---

### Domanda A6 (3 punti)

Quale affermazione sul bias nei modelli di IA è corretta?

A) Il bias è sempre intenzionale e inserito dai programmatori  
B) Il bias può derivare da dati di training non rappresentativi o sbilanciati  
C) I modelli di IA non possono avere bias perché sono matematici e oggettivi  
D) Il bias si corregge automaticamente con più dati di qualsiasi tipo  

<details>
<summary>Risposta e Spiegazione</summary>

**Risposta corretta: B**

**Spiegazione:**
Il bias nei modelli deriva principalmente dai dati di training. Se i dati sono sbilanciati, non rappresentativi, o contengono pregiudizi storici, il modello apprenderà e riprodurrà questi bias.

**Esempio:**
```
Dataset: 90% foto di medici uomini, 10% donne
Risultato: Modello associa "medico" principalmente a uomini
→ Bias di genere non intenzionale ma presente
```

**Perché le altre sono sbagliate:**
- A: Spesso non intenzionale
- C: La matematica opera sui dati forniti; se i dati sono biased, anche il modello lo sarà
- D: Più dati aiutano solo se sono rappresentativi e bilanciati

</details>

---

## 4. Sezione B: Programmazione Assistita

**Istruzioni**: Rispondi alle domande in modo conciso ma completo (3-5 righe per domanda).

**Punteggio**: 15 punti totali (3 punti per domanda)

**Tempo consigliato**: 20 minuti

---

### Domanda B1 (3 punti)

Descrivi la struttura essenziale di un prompt tecnico efficace per generare codice. Elenca almeno 4 elementi che dovrebbe contenere.

<details>
<summary>Risposta Attesa</summary>

**Elementi essenziali:**

1. **Contesto**: Linguaggio, standard (es. C99), ambiente (embedded, desktop)
2. **Obiettivo tecnico**: Descrizione chiara e misurabile di cosa deve fare
3. **Vincoli**: Limitazioni (memoria, performance, librerie da evitare)
4. **Formato output**: Tipo di output richiesto (funzione, modulo, test inclusi)
5. **Gestione errori**: Come gestire input invalidi ed edge cases (opzionale ma raccomandato)

**Esempio di buon prompt:**
```
"Scrivi in C99 standard una funzione `int somma(int arr[], int n)` 
che sommi elementi array, gestisca n<=0 ritornando 0, 
includa 3 test cases."
```

**Punteggio:**
- 3 punti: 4+ elementi corretti con esempi
- 2 punti: 3 elementi corretti
- 1 punto: 2 elementi corretti
- 0 punti: Meno di 2 elementi o errati

</details>

---

### Domanda B2 (3 punti)

Perché è necessario verificare sempre il codice generato dall'IA? Fornisci almeno DUE motivi tecnici specifici.

<details>
<summary>Risposta Attesa</summary>

**Motivi principali:**

1. **Possibili allucinazioni**: L'IA può generare funzioni o sintassi inesistenti (es. `strdup()` non è C standard, ma l'IA potrebbe usarlo)

2. **Errori logici sottili**: Il codice può compilare ma contenere bug (buffer overflow, off-by-one, memory leak, mancata gestione NULL)

3. **Mancanza di contesto**: L'IA non conosce il tuo hardware specifico, vincoli di memoria, o requisiti di performance

4. **Sicurezza**: Potrebbe generare codice vulnerabile (es. `strcpy` senza controllo dimensione)

**Esempio:**
```c
// IA potrebbe generare:
char *copy = strdup(str);  // ❌ Non standard C99!

// Corretto:
char *copy = malloc(strlen(str) + 1);
strcpy(copy, str);
```

**Punteggio:**
- 3 punti: 2+ motivi tecnici corretti con esempi
- 2 punti: 2 motivi corretti senza esempi
- 1 punto: 1 motivo corretto
- 0 punti: Nessun motivo valido

</details>

---

### Domanda B3 (3 punti)

Spiega la differenza tra approccio "Zero-Shot" e "Few-Shot" nel prompt engineering. Quando è preferibile usare Few-Shot?

<details>
<summary>Risposta Attesa</summary>

**Definizioni:**

**Zero-Shot**: Fornire solo l'istruzione senza esempi
```
"Scrivi funzione per invertire stringa"
```

**Few-Shot**: Fornire istruzione + esempi di input/output
```
"Scrivi funzione per invertire stringa.
Esempi:
Input: "hello" → Output: "olleh"
Input: "a" → Output: "a"
Input: "" → Output: ""
```

**Quando usare Few-Shot:**
- Comportamento desiderato complesso o ambiguo
- Task specifico con edge cases da coprire
- Formato output particolare
- Ridurre ambiguità nell'interpretazione

**Vantaggio Few-Shot**: L'IA comprende meglio le aspettative vedendo esempi concreti.

**Punteggio:**
- 3 punti: Spiega entrambi + indica quando Few-Shot
- 2 punti: Spiega entrambi ma senza contesto d'uso
- 1 punto: Spiega solo uno dei due
- 0 punti: Risposta errata o assente

</details>

---

### Domanda B4 (3 punti)

Descrivi la metodologia "Spec → Code → Test" per lo sviluppo assistito da IA. Perché migliora l'affidabilità?

<details>
<summary>Risposta Attesa</summary>

**Metodologia in 3 fasi:**

**1. Spec (Specifica)**
- Definisci chiaramente COSA deve fare il codice
- Scrivi prompt dettagliato con requisiti
- Identifica edge cases e gestione errori

**2. Code (Generazione)**
- Chiedi all'IA di generare codice basato su spec
- Revisiona e comprendi il codice generato

**3. Test (Validazione)**
- Scrivi o chiedi test cases
- Compila e esegui
- Verifica edge cases
- Valida con tool (valgrind, cppcheck)

**Perché migliora affidabilità:**
- Forza pensiero chiaro PRIMA di generare codice
- Test validano comportamento, non solo sintassi
- Approccio iterativo permette correzioni graduali
- Riduce rischio di integrare codice non validato

**Punteggio:**
- 3 punti: Descrive tutte 3 fasi + spiega benefici
- 2 punti: Descrive 3 fasi senza benefici chiari
- 1 punto: Descrizione incompleta
- 0 punti: Non comprende la metodologia

</details>

---

### Domanda B5 (3 punti)

Qual è la differenza principale tra usare l'IA per "generare codice" vs "debuggare codice esistente"? Fornisci un esempio di prompt per ciascun caso.

<details>
<summary>Risposta Attesa</summary>

**Differenza principale:**

**Generazione**: Parti da zero, definisci cosa vuoi
- Focus su: requisiti, vincoli, comportamento desiderato

**Debugging**: Parti da codice con problema
- Focus su: sintomi, errori osservati, comportamento attuale vs atteso

**Esempi:**

**Generazione:**
```
"Scrivi in C99 funzione che calcola media array di float,
gestisce n<=0 ritornando 0.0, include 3 test."
```

**Debugging:**
```
"Questo codice causa segfault:
[codice]

Errore: Segmentation fault su riga 15
Input test: arr={1,2,3}, n=3
Atteso: somma 6
Ottenuto: crash

Analizza e correggi."
```

**Differenza chiave**: Il debugging richiede descrivere il problema osservato, non solo il comportamento desiderato.

**Punteggio:**
- 3 punti: Spiega differenza + 2 esempi corretti
- 2 punti: Spiega differenza + 1 esempio
- 1 punto: Solo differenza o solo esempi
- 0 punti: Risposta inadeguata

</details>

---

## 5. Sezione C: Programmazione in C

**Istruzioni**: Risolvi gli esercizi utilizzando IA se necessario, ma VALIDA sempre il codice. Consegna codice funzionante e commentato.

**Punteggio**: 27 punti totali

**Tempo consigliato**: 35 minuti

---

### Esercizio C1: Analisi e Correzione (9 punti)

Analizza il seguente codice C e identifica TUTTI gli errori (sintattici, logici, di sicurezza). Poi fornisci la versione corretta.

```c
#include <stdio.h>
#include <string.h>

// Copia stringa e ritorna lunghezza
int copy_string(char *dest, char *src) {
    strcpy(dest, src);
    return strlen(dest);
}

int main() {
    char buffer[10];
    char *input = "Questa stringa è molto lunga";
    
    int len = copy_string(buffer, input);
    printf("Copiato %d caratteri: %s\n", len, buffer);
    
    return 0;
}
```

**Compiti:**
1. Elenca tutti gli errori (minimo 3)
2. Spiega perché sono errori
3. Fornisci codice corretto e sicuro

<details>
<summary>Soluzione e Valutazione</summary>

**Errori identificati:**

1. **Buffer Overflow (CRITICO)**
   - `strcpy(dest, src)` non controlla dimensione
   - `input` ha 29 caratteri, `buffer` solo 10
   - Comportamento indefinito, possibile crash

2. **Mancanza parametro size**
   - Funzione non sa dimensione `dest`
   - Impossibile fare controllo sicuro

3. **Mancanza controllo NULL**
   - Se `dest` o `src` sono NULL → crash

4. **Tipo parametri**
   - Dovrebbero essere `const char *src` (non modifica sorgente)

**Codice corretto:**

```c
#include <stdio.h>
#include <string.h>

/**
 * Copia stringa in modo sicuro
 * @return Lunghezza copiata, -1 se errore
 */
int copy_string_safe(char *dest, size_t dest_size, const char *src) {
    // Validazione input
    if (dest == NULL || src == NULL || dest_size == 0) {
        return -1;
    }
    
    // Copia sicura
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // Garantisci terminatore
    
    return strlen(dest);
}

int main() {
    char buffer[10];
    const char *input = "Questa stringa è molto lunga";
    
    int len = copy_string_safe(buffer, sizeof(buffer), input);
    
    if (len >= 0) {
        printf("Copiato %d caratteri: %s\n", len, buffer);
    } else {
        printf("Errore nella copia\n");
    }
    
    return 0;
}

// Output: "Copiato 9 caratteri: Questa st"
```

**Valutazione:**
- 9 punti: Identifica 3+ errori, corregge tutto, codice funzionante
- 7 punti: Identifica 2-3 errori, correzione parziale
- 5 punti: Identifica 1-2 errori, correzione con bug
- 3 punti: Identifica 1 errore, correzione inadeguata
- 0 punti: Non identifica errori o codice errato

</details>

---

### Esercizio C2: Implementazione con IA (9 punti)

Usa l'IA per implementare una funzione di ricerca binaria in C99. Fornisci:

1. **Prompt** che useresti (strutturato e completo)
2. **Codice generato** dall'IA
3. **Analisi critica**: identifica potenziali problemi
4. **Test**: almeno 3 casi di test

**Requisiti funzione:**
```c
int binary_search(const int arr[], int n, int target);
// Ritorna: indice se trovato, -1 altrimenti
// Array deve essere ordinato crescente
```

<details>
<summary>Soluzione Attesa</summary>

**1. Prompt Professionale:**
```
Scrivi in standard C99 una funzione di ricerca binaria:

int binary_search(const int arr[], int n, int target)

SPECIFICHE:
- Array `arr` ordinato in ordine crescente
- Ritorna indice di `target` se trovato, -1 altrimenti
- Gestisci arr==NULL (ritorna -1)
- Gestisci n<=0 (ritorna -1)
- Implementazione iterativa (non ricorsiva)
- Complessità O(log n)
- Commenti che spiegano logica

OUTPUT:
- Codice completo
- 5 test cases:
  * Elemento al centro
  * Elemento all'inizio
  * Elemento alla fine
  * Elemento non presente
  * Array vuoto
```

**2. Codice Generato (esempio):**
```c
/**
 * Ricerca binaria in array ordinato
 */
int binary_search(const int arr[], int n, int target) {
    if (arr == NULL || n <= 0) {
        return -1;
    }
    
    int left = 0;
    int right = n - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // Evita overflow
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;  // Non trovato
}
```

**3. Analisi Critica:**
```
✅ PUNTI POSITIVI:
- Gestione NULL e n<=0
- Calcolo mid sicuro contro overflow
- Logica corretta
- Complessità O(log n)

⚠️ POTENZIALI MIGLIORAMENTI:
- Potrebbe aggiungere assert per debug
- Documentazione Doxygen più completa
- Test di edge case più estesi

✅ CONCLUSIONE: Codice corretto e utilizzabile
```

**4. Test Cases:**
```c
#include <assert.h>

void test_binary_search() {
    // Test 1: Elemento al centro
    int arr1[] = {1, 3, 5, 7, 9};
    assert(binary_search(arr1, 5, 5) == 2);
    
    // Test 2: Elemento all'inizio
    int arr2[] = {10, 20, 30};
    assert(binary_search(arr2, 3, 10) == 0);
    
    // Test 3: Elemento alla fine
    int arr3[] = {2, 4, 6};
    assert(binary_search(arr3, 3, 6) == 2);
    
    // Test 4: Non presente
    int arr4[] = {1, 2, 3};
    assert(binary_search(arr4, 3, 99) == -1);
    
    // Test 5: Array vuoto
    assert(binary_search(NULL, 0, 5) == -1);
    
    printf("Tutti i test passati!\n");
}
```

**Valutazione:**
- 9 punti: Prompt completo, codice corretto, analisi critica, test funzionanti
- 7 punti: Prompt buono, codice funzionante, test presenti
- 5 punti: Prompt base, codice con piccoli bug, test incompleti
- 3 punti: Prompt vago, codice errato, pochi test
- 0 punti: Non completa l'esercizio

</details>

---

### Esercizio C3: Refactoring (9 punti)

Refactora questo codice migliorando leggibilità, gestione errori e robustezza. Usa l'IA se necessario ma valida il risultato.

```c
#include <stdio.h>

int f(int *a, int n) {
    int x = a[0];
    for(int i=1;i<n;i++) {
        if(a[i]>x) x=a[i];
    }
    return x;
}

int main() {
    int v[] = {3,7,2,9,1};
    printf("%d\n", f(v, 5));
    return 0;
}
```

**Compiti:**
1. Rinomina variabili con nomi descrittivi
2. Aggiungi gestione errori
3. Aggiungi documentazione
4. Scrivi test

<details>
<summary>Soluzione Attesa</summary>

**Codice Refactorato:**

```c
#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

/**
 * @brief Trova il valore massimo in un array di interi
 * 
 * @param array Array di interi da analizzare
 * @param size Dimensione dell'array
 * @param max_value Puntatore dove salvare il massimo (output)
 * @return true se successo, false se errore
 * 
 * @note Complessità: O(n) tempo, O(1) spazio
 */
bool find_max(const int *array, int size, int *max_value) {
    // Validazione input
    if (array == NULL || max_value == NULL) {
        return false;  // Puntatori NULL
    }
    
    if (size <= 0) {
        return false;  // Array vuoto o dimensione invalida
    }
    
    // Inizializza massimo con primo elemento
    int current_max = array[0];
    
    // Cerca massimo
    for (int i = 1; i < size; i++) {
        if (array[i] > current_max) {
            current_max = array[i];
        }
    }
    
    // Salva risultato
    *max_value = current_max;
    return true;
}

/**
 * Test cases per find_max
 */
void test_find_max() {
    printf("=== Test find_max ===\n");
    
    // Test 1: Array normale
    {
        int arr[] = {3, 7, 2, 9, 1};
        int max;
        if (find_max(arr, 5, &max)) {
            printf("Test 1: max = %d ", max);
            printf(max == 9 ? "✓ PASS\n" : "✗ FAIL\n");
        }
    }
    
    // Test 2: Array con negativi
    {
        int arr[] = {-5, -2, -10, -1};
        int max;
        if (find_max(arr, 4, &max)) {
            printf("Test 2: max = %d ", max);
            printf(max == -1 ? "✓ PASS\n" : "✗ FAIL\n");
        }
    }
    
    // Test 3: Array singolo elemento
    {
        int arr[] = {42};
        int max;
        if (find_max(arr, 1, &max)) {
            printf("Test 3: max = %d ", max);
            printf(max == 42 ? "✓ PASS\n" : "✗ FAIL\n");
        }
    }
    
    // Test 4: Gestione NULL
    {
        int max;
        bool result = find_max(NULL, 5, &max);
        printf("Test 4 (NULL): ");
        printf(!result ? "✓ PASS\n" : "✗ FAIL\n");
    }
    
    // Test 5: Size invalido
    {
        int arr[] = {1, 2, 3};
        int max;
        bool result = find_max(arr, 0, &max);
        printf("Test 5 (size=0): ");
        printf(!result ? "✓ PASS\n" : "✗ FAIL\n");
    }
}

int main() {
    // Test suite
    test_find_max();
    
    // Uso normale
    printf("\n=== Uso Normale ===\n");
    int values[] = {3, 7, 2, 9, 1};
    int maximum;
    
    if (find_max(values, 5, &maximum)) {
        printf("Massimo trovato: %d\n", maximum);
    } else {
        printf("Errore nella ricerca del massimo\n");
    }
    
    return 0;
}
```

**Miglioramenti Applicati:**

1. **Nomi Descrittivi:**
   - `f` → `find_max`
   - `a` → `array`
   - `n` → `size`
   - `x` → `current_max`

2. **Gestione Errori:**
   - Controllo puntatori NULL
   - Controllo size <= 0
   - Return bool per indicare successo/fallimento
   - Output tramite parametro puntatore

3. **Documentazione:**
   - Commenti Doxygen
   - Spiegazione parametri e return
   - Nota sulla complessità

4. **Test Completi:**
   - Caso normale
   - Negativi
   - Singolo elemento
   - Edge cases (NULL, size=0)

**Valutazione:**
- 9 punti: Tutti i miglioramenti + test completi
- 7 punti: Maggior parte miglioramenti + alcuni test
- 5 punti: Nomi migliorati + gestione errori base
- 3 punti: Solo renaming o documentazione
- 0 punti: Non migliora significativamente

</details>

---

## 6. Sezione D: Arduino e Embedded

**Istruzioni**: Risolvi gli esercizi. Puoi usare hardware fisico o simulazione. Codice deve essere testabile.

**Punteggio**: 20 punti totali

**Tempo consigliato**: 30 minuti

---

### Esercizio D1: Sketch Non-Bloccante (8 punti)

Scrivi sketch Arduino che:
- LED1 su pin 12: lampeggia ogni 1000ms
- LED2 su pin 11: lampeggia ogni 500ms
- Pulsante su pin 2: quando premuto, inverte stato LED3 su pin 10
- Tutto NON-BLOCCANTE (usa `millis()`)

**Fornisci:**
1. Sketch completo
2. Diagramma collegamenti (testuale)

<details>
<summary>Soluzione</summary>

**Sketch:**
```cpp
/*
 * SKETCH NON-BLOCCANTE - 3 LED + PULSANTE
 */

// === PIN ===
const int LED1_PIN = 12;
const int LED2_PIN = 11;
const int LED3_PIN = 10;
const int BUTTON_PIN = 2;

// === TIMING ===
const unsigned long LED1_INTERVAL = 1000;  // 1 secondo
const unsigned long LED2_INTERVAL = 500;   // 0.5 secondi
const unsigned long DEBOUNCE_DELAY = 50;   // 50ms debounce

// === STATI ===
unsigned long led1_previousMillis = 0;
unsigned long led2_previousMillis = 0;
unsigned long lastDebounceTime = 0;

bool led1_state = false;
bool led2_state = false;
bool led3_state = false;
bool lastButtonState = HIGH;

void setup() {
    // Configura pin
    pinMode(LED1_PIN, OUTPUT);
    pinMode(LED2_PIN, OUTPUT);
    pinMode(LED3_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    
    // Inizializza output
    digitalWrite(LED1_PIN, LOW);
    digitalWrite(LED2_PIN, LOW);
    digitalWrite(LED3_PIN, LOW);
    
    // Debug seriale (opzionale)
    Serial.begin(9600);
    Serial.println(F("Sistema avviato"));
}

void loop() {
    unsigned long currentMillis = millis();
    
    // === GESTIONE LED1 (1000ms) ===
    if (currentMillis - led1_previousMillis >= LED1_INTERVAL) {
        led1_previousMillis = currentMillis;
        led1_state = !led1_state;
        digitalWrite(LED1_PIN, led1_state);
    }
    
    // === GESTIONE LED2 (500ms) ===
    if (currentMillis - led2_previousMillis >= LED2_INTERVAL) {
        led2_previousMillis = currentMillis;
        led2_state = !led2_state;
        digitalWrite(LED2_PIN, led2_state);
    }
    
    // === GESTIONE PULSANTE CON DEBOUNCING ===
    bool reading = digitalRead(BUTTON_PIN);
    
    // Se stato è cambiato, resetta timer debounce
    if (reading != lastButtonState) {
        lastDebounceTime = currentMillis;
    }
    
    // Controlla se stato è stabile per DEBOUNCE_DELAY
    if ((currentMillis - lastDebounceTime) > DEBOUNCE_DELAY) {
        // Stato stabile: se è cambiato, agisci
        static bool buttonState = HIGH;
        
        if (reading != buttonState) {
            buttonState = reading;
            
            // Rileva fronte di discesa (pressione)
            if (buttonState == LOW) {
                // Toggle LED3
                led3_state = !led3_state;
                digitalWrite(LED3_PIN, led3_state);
                
                Serial.print(F("LED3: "));
                Serial.println(led3_state ? "ON" : "OFF");
            }
        }
    }
    
    lastButtonState = reading;
}
```

**Diagramma Collegamenti:**
```
ARDUINO UNO
┌─────────────────────────────────┐
│                                 │
│  LED1 (pin 12) ──[220Ω]── GND  │
│  LED2 (pin 11) ──[220Ω]── GND  │
│  LED3 (pin 10) ──[220Ω]── GND  │
│                                 │
│  BUTTON (pin 2)                 │
│    └── Pulsante a GND           │
│    (usa INPUT_PULLUP interno)   │
│                                 │
└─────────────────────────────────┘

NOTE:
- LED: Anodo (+) al pin, Catodo (-) a GND via resistenza
- Pulsante: Un lato a pin 2, altro lato a GND
- Pull-up interno attivo: HIGH quando non premuto
```

**Valutazione:**
- 8 punti: Tutto funzionante, non-bloccante, debouncing
- 6 punti: Funziona ma senza debouncing o con piccoli bug
- 4 punti: Logica base corretta ma usa delay()
- 2 punti: Sketch incompleto o con errori maggiori
- 0 punti: Non funziona

</details>

---

### Esercizio D2: Sensore Analogico (6 punti)

Scrivi funzione Arduino che:
- Legge sensore analogico su pin A0
- Applica media mobile su 5 campioni
- Ritorna valore normalizzato 0.0-1.0 (float)

```cpp
float read_sensor_normalized(void);
```

Fornisci implementazione completa e esempio d'uso nel loop().

<details>
<summary>Soluzione</summary>

```cpp
/*
 * LETTURA SENSORE CON MEDIA MOBILE E NORMALIZZAZIONE
 */

const int SENSOR_PIN = A0;
const int NUM_SAMPLES = 5;

// Buffer per media mobile
int readings[NUM_SAMPLES];
int readIndex = 0;
int total = 0;
bool bufferFull = false;

/**
 * Legge sensore analogico con media mobile e normalizzazione
 * @return Valore normalizzato 0.0-1.0
 */
float read_sensor_normalized(void) {
    // Rimuovi lettura vecchia dal totale
    total = total - readings[readIndex];
    
    // Leggi nuovo valore
    readings[readIndex] = analogRead(SENSOR_PIN);
    
    // Aggiungi nuovo valore al totale
    total = total + readings[readIndex];
    
    // Avanza indice (circular buffer)
    readIndex = (readIndex + 1) % NUM_SAMPLES;
    
    // Marca buffer come pieno dopo primo ciclo completo
    if (readIndex == 0) {
        bufferFull = true;
    }
    
    // Calcola media
    int samples = bufferFull ? NUM_SAMPLES : readIndex;
    if (samples == 0) samples = 1;  // Evita divisione per zero
    
    int average = total / samples;
    
    // Normalizza 0-1023 → 0.0-1.0
    float normalized = average / 1023.0;
    
    return normalized;
}

/**
 * Inizializza buffer media mobile
 */
void init_sensor(void) {
    for (int i = 0; i < NUM_SAMPLES; i++) {
        readings[i] = 0;
    }
    total = 0;
    readIndex = 0;
    bufferFull = false;
}

void setup() {
    Serial.begin(9600);
    init_sensor();
    
    // Pre-riempi buffer con letture iniziali
    for (int i = 0; i < NUM_SAMPLES; i++) {
        read_sensor_normalized();
        delay(10);
    }
    
    Serial.println(F("Sensore inizializzato"));
}

void loop() {
    // Leggi sensore normalizzato
    float value = read_sensor_normalized();
    
    // Converti in percentuale per display
    int percent = (int)(value * 100);
    
    // Output
    Serial.print(F("Valore: "));
    Serial.print(value, 3);  // 3 decimali
    Serial.print(F(" ("));
    Serial.print(percent);
    Serial.println(F("%)"));
    
    // Esempio uso: controllo LED basato su soglia
    if (value > 0.5) {
        digitalWrite(LED_BUILTIN, HIGH);
    } else {
        digitalWrite(LED_BUILTIN, LOW);
    }
    
    delay(200);  // Leggi ogni 200ms
}
```

**Spiegazione Tecnica:**

1. **Buffer Circolare**: Array di 5 elementi con indice che "gira"
2. **Media Mobile**: Somma degli ultimi N valori / N
3. **Normalizzazione**: Divide per 1023.0 per ottenere 0.0-1.0
4. **Gestione Startup**: Buffer inizialmente non pieno

**Valutazione:**
- 6 punti: Implementazione corretta, media mobile, normalizzazione
- 4 punti: Funziona ma senza media mobile O normalizzazione errata
- 2 punti: Logica base presente ma con errori
- 0 punti: Non implementato o completamente errato

</details>

---

### Esercizio D3: Debugging (6 punti)

Questo sketch dovrebbe accendere LED quando pulsante premuto, ma non funziona. Identifica e correggi TUTTI i bug.

```cpp
const int LED = 13;
const int BUTTON = 2;

void setup() {
    pinMode(LED, INPUT);      // Bug?
    pinMode(BUTTON, OUTPUT);  // Bug?
}

void loop() {
    int stato = digitalRead(BUTTON);
    if (stato = HIGH) {       // Bug?
        digitalWrite(LED, LOW);
    }
}
```

**Compiti:**
1. Elenca tutti i bug (almeno 4)
2. Fornisci codice corretto
3. Spiega brevemente ogni correzione

<details>
<summary>Soluzione</summary>

**Bug Identificati:**

1. **Pin LED configurato come INPUT invece di OUTPUT**
   ```cpp
   pinMode(LED, INPUT);  // ❌ SBAGLIATO
   pinMode(LED, OUTPUT); // ✅ CORRETTO
   ```

2. **Pin BUTTON configurato come OUTPUT invece di INPUT**
   ```cpp
   pinMode(BUTTON, OUTPUT);       // ❌ SBAGLIATO
   pinMode(BUTTON, INPUT_PULLUP); // ✅ CORRETTO (con pull-up)
   ```

3. **Operatore assegnamento (=) invece di confronto (==)**
   ```cpp
   if (stato = HIGH) {  // ❌ Assegna HIGH a stato, sempre true!
   if (stato == HIGH) { // ✅ Confronta stato con HIGH
   ```

4. **LED acceso con LOW invece di HIGH**
   ```cpp
   digitalWrite(LED, LOW);  // ❌ Spegne LED
   digitalWrite(LED, HIGH); // ✅ Accende LED
   ```

5. **Manca gestione stato OFF** (bug logico)
   - LED dovrebbe spegnersi quando pulsante rilasciato

**Codice Corretto Completo:**

```cpp
/*
 * LED CONTROLLATO DA PULSANTE - VERSIONE CORRETTA
 */

const int LED_PIN = 13;
const int BUTTON_PIN = 2;

void setup() {
    // ✅ LED configurato come OUTPUT
    pinMode(LED_PIN, OUTPUT);
    
    // ✅ Pulsante configurato come INPUT con pull-up interno
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    
    // Inizializza LED spento
    digitalWrite(LED_PIN, LOW);
    
    // Debug (opzionale)
    Serial.begin(9600);
    Serial.println(F("Sistema pronto"));
}

void loop() {
    // Leggi stato pulsante
    int buttonState = digitalRead(BUTTON_PIN);
    
    // ✅ Confronto con == (non assegnamento con =)
    // Nota: con INPUT_PULLUP, LOW = premuto, HIGH = rilasciato
    if (buttonState == LOW) {
        // Pulsante premuto → accendi LED
        digitalWrite(LED_PIN, HIGH);
        Serial.println(F("LED ON"));
    } else {
        // Pulsante rilasciato → spegni LED
        digitalWrite(LED_PIN, LOW);
        Serial.println(F("LED OFF"));
    }
    
    delay(50);  // Piccolo delay per stabilità
}
```

**Spiegazioni:**

1. **pinMode corretto**: LED output, pulsante input
2. **INPUT_PULLUP**: Resistenza pull-up interna (20kΩ), stato HIGH quando non premuto
3. **Confronto ==**: Verifica uguaglianza senza modificare variabile
4. **digitalWrite HIGH**: Accende LED (5V sul pin)
5. **Logica completa**: Gestisce sia accensione che spegnimento

**Valutazione:**
- 6 punti: Identifica 4+ bug, corregge tutto, spiega
- 4 punti: Identifica 3 bug, correzione funzionante
- 2 punti: Identifica 1-2 bug, correzione parziale
- 0 punti: Non identifica bug o correzione errata

</details>

---

## 7. Sezione E: Progetto Integrato

**Istruzioni**: Progetta sistema completo che integra C e Arduino. Puoi usare IA per assistenza.

**Punteggio**: 20 punti

**Tempo consigliato**: 20 minuti

---

### Progetto: Sistema di Monitoraggio Temperatura

**Obiettivo**: Creare sistema che monitora temperatura e attiva allarme se supera soglia.

**Requisiti:**

**Hardware:**
- Arduino Uno
- Sensore temperatura TMP36 su A0
- LED verde su pin 12 (temperatura OK)
- LED rosso su pin 13 (temperatura alta)
- Buzzer su pin 8 (allarme)

**Software:**
1. Funzione C per filtraggio media mobile (10 campioni)
2. Sketch Arduino che usa la funzione
3. Logica:
   - Temperatura < 25°C: LED verde ON, rosso OFF
   - Temperatura 25-30°C: entrambi OFF
   - Temperatura > 30°C: LED rosso ON, verde OFF, allarme
4. Output seriale ogni 2 secondi con timestamp
5. Tutto non-bloccante

**Consegna:**
1. Codice C completo (funzioni + sketch)
2. Diagramma collegamenti
3. Breve spiegazione logica (5 righe)

<details>
<summary>Soluzione Completa</summary>

**Codice:**

```cpp
/*
 * SISTEMA MONITORAGGIO TEMPERATURA
 * 
 * Hardware:
 * - TMP36 su A0
 * - LED verde su 12
 * - LED rosso su 13
 * - Buzzer su 8
 */

// === PIN ===
const int TEMP_PIN = A0;
const int LED_GREEN = 12;
const int LED_RED = 13;
const int BUZZER_PIN = 8;

// === COSTANTI ===
const int NUM_SAMPLES = 10;
const unsigned long READ_INTERVAL = 2000;  // 2 secondi
const float TEMP_LOW = 25.0;   // °C
const float TEMP_HIGH = 30.0;  // °C

// === BUFFER MEDIA MOBILE ===
float tempReadings[NUM_SAMPLES];
int readIndex = 0;
bool bufferFull = false;

// === TIMING ===
unsigned long lastReadTime = 0;

// === FUNZIONI C ===

/**
 * @brief Aggiunge campione a buffer e calcola media mobile
 * @param value Nuovo valore da aggiungere
 * @return Media mobile degli ultimi N campioni
 */
float moving_average_filter(float value) {
    // Aggiungi nuovo valore
    tempReadings[readIndex] = value;
    
    // Avanza indice circolare
    readIndex = (readIndex + 1) % NUM_SAMPLES;
    
    // Marca buffer pieno dopo primo ciclo
    if (readIndex == 0) {
        bufferFull = true;
    }
    
    // Calcola media
    float sum = 0.0;
    int count = bufferFull ? NUM_SAMPLES : readIndex;
    if (count == 0) count = 1;
    
    for (int i = 0; i < count; i++) {
        sum += tempReadings[i];
    }
    
    return sum / count;
}

/**
 * @brief Legge TMP36 e converte in °C
 * @return Temperatura in gradi Celsius
 */
float read_tmp36_temperature(void) {
    // Leggi ADC
    int rawValue = analogRead(TEMP_PIN);
    
    // Converti in tensione (0-1023 → 0-5V)
    float voltage = rawValue * (5.0 / 1023.0);
    
    // Converti in temperatura (TMP36: 10mV/°C, offset 500mV)
    float temperatureC = (voltage - 0.5) * 100.0;
    
    return temperatureC;
}

/**
 * @brief Gestisce LED e allarme basato su temperatura
 * @param temperature Temperatura in °C
 */
void control_outputs(float temperature) {
    if (temperature < TEMP_LOW) {
        // Temperatura OK
        digitalWrite(LED_GREEN, HIGH);
        digitalWrite(LED_RED, LOW);
        noTone(BUZZER_PIN);
        
    } else if (temperature >= TEMP_LOW && temperature <= TEMP_HIGH) {
        // Temperatura intermedia
        digitalWrite(LED_GREEN, LOW);
        digitalWrite(LED_RED, LOW);
        noTone(BUZZER_PIN);
        
    } else {
        // Temperatura alta - ALLARME
        digitalWrite(LED_GREEN, LOW);
        digitalWrite(LED_RED, HIGH);
        
        // Beep pattern
        static unsigned long lastBeep = 0;
        if (millis() - lastBeep >= 500) {
            lastBeep = millis();
            tone(BUZZER_PIN, 1000, 200);  // 1kHz, 200ms
        }
    }
}

/**
 * @brief Log dati su seriale
 * @param rawTemp Temperatura istantanea
 * @param filteredTemp Temperatura filtrata
 */
void log_data(float rawTemp, float filteredTemp) {
    Serial.print(F("["));
    Serial.print(millis());
    Serial.print(F("ms] Temp raw: "));
    Serial.print(rawTemp, 1);
    Serial.print(F("°C | Filtered: "));
    Serial.print(filteredTemp, 1);
    Serial.print(F("°C | Status: "));
    
    if (filteredTemp < TEMP_LOW) {
        Serial.println(F("OK"));
    } else if (filteredTemp <= TEMP_HIGH) {
        Serial.println(F("WARN"));
    } else {
        Serial.println(F("ALARM"));
    }
}

// === SETUP ===
void setup() {
    // Inizializza seriale
    Serial.begin(9600);
    Serial.println(F("=== Sistema Monitoraggio Temperatura ==="));
    
    // Configura pin
    pinMode(LED_GREEN, OUTPUT);
    pinMode(LED_RED, OUTPUT);
    pinMode(BUZZER_PIN, OUTPUT);
    
    // Inizializza output
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_RED, LOW);
    noTone(BUZZER_PIN);
    
    // Inizializza buffer
    for (int i = 0; i < NUM_SAMPLES; i++) {
        tempReadings[i] = 0.0;
    }
    
    // Pre-riempi buffer con letture iniziali
    Serial.println(F("Calibrazione sensore..."));
    for (int i = 0; i < NUM_SAMPLES; i++) {
        float temp = read_tmp36_temperature();
        moving_average_filter(temp);
        delay(100);
    }
    
    Serial.println(F("Sistema pronto!\n"));
}

// === LOOP ===
void loop() {
    unsigned long currentMillis = millis();
    
    // Lettura periodica ogni READ_INTERVAL
    if (currentMillis - lastReadTime >= READ_INTERVAL) {
        lastReadTime = currentMillis;
        
        // Leggi temperatura
        float rawTemp = read_tmp36_temperature();
        
        // Applica filtro media mobile
        float filteredTemp = moving_average_filter(rawTemp);
        
        // Controlla e attiva output
        control_outputs(filteredTemp);
        
        // Log dati
        log_data(rawTemp, filteredTemp);
    }
    
    // Loop continua immediatamente (non-bloccante)
}
```

**Diagramma Collegamenti:**

```
ARDUINO UNO
┌─────────────────────────────────────┐
│                                     │
│  TMP36 (sensore temperatura):      │
│    Pin 1 (left)  → 5V               │
│    Pin 2 (center)→ A0               │
│    Pin 3 (right) → GND              │
│                                     │
│  LED Verde (pin 12):                │
│    Anodo (+) → Pin 12               │
│    Catodo (-) → [220Ω] → GND       │
│                                     │
│  LED Rosso (pin 13):                │
│    Anodo (+) → Pin 13               │
│    Catodo (-) → [220Ω] → GND       │
│                                     │
│  Buzzer Piezo (pin 8):              │
│    Pin + → Pin 8                    │
│    Pin - → GND                      │
│                                     │
└─────────────────────────────────────┘

NOTE:
- TMP36 richiede orientamento corretto (flat side)
- Resistenze LED: 220Ω-330Ω
- Buzzer: Piezo passivo o attivo
```

**Spiegazione Logica:**

Il sistema legge periodicamente (ogni 2s) la temperatura dal TMP36, applica un filtro media mobile su 10 campioni per ridurre rumore, e controlla LED/buzzer basandosi su soglie definite. La logica è completamente non-bloccante usando `millis()`, permettendo al buzzer di emettere beep mentre il loop continua. Tutte le letture sono loggate su seriale con timestamp per analisi post-elaborazione.

**Valutazione:**
- 20 punti: Progetto completo, funzionante, ben documentato
- 16 punti: Funziona con piccole mancanze (es. no log o filtro semplificato)
- 12 punti: Logica base corretta ma con bug o incompletezza
- 8 punti: Struttura presente ma non funzionante
- 4 punti: Tentativo parziale
- 0 punti: Non consegnato

</details>

---

## 8. Criteri di Valutazione

### 8.1 Rubrica Generale

```
SCALA VALUTAZIONE:
┌──────────────────────────────────────┐
│ 90-100: ECCELLENTE                   │
│   - Tutte sezioni completate         │
│   - Codice pulito e professionale    │
│   - Pensiero critico evidente        │
│   - Uso esperto di IA                │
├──────────────────────────────────────┤
│ 75-89: BUONO                         │
│   - Maggior parte sezioni complete   │
│   - Codice funzionante               │
│   - Buona comprensione concetti      │
│   - Uso efficace di IA               │
├──────────────────────────────────────┤
│ 60-74: SUFFICIENTE                   │
│   - Sezioni base completate          │
│   - Codice funziona con bug minori   │
│   - Comprensione accettabile         │
│   - Uso basilare di IA               │
├──────────────────────────────────────┤
│ <60: INSUFFICIENTE                   │
│   - Sezioni incomplete               │
│   - Codice non funzionante           │
│   - Gap comprensione                 │
│   - IA usata in modo scorretto       │
└──────────────────────────────────────┘
```

### 8.2 Valutazione Uso IA

L'uso di IA viene valutato su:

**✅ Uso Positivo (max +5 punti bonus):**
- Prompt ben strutturati e specifici
- Validazione critica dell'output
- Iterazioni migliorative
- Integrazione corretta nel codice
- Documentazione di scelte progettuali

**❌ Uso Negativo (penalizzazioni):**
- Codice copiato senza comprensione (-5 punti)
- Errori evidenti non corretti (-3 punti)
- Prompt vaghi che generano output inutile (-2 punti)
- Nessuna validazione dell'output IA (-3 punti)

### 8.3 Qualità Codice

**Criteri specifici:**

```c
CHECKLIST QUALITÀ (per esercizi C e Arduino):
[ ] Compila senza errori (OBBLIGATORIO per punteggio)
[ ] Compila senza warning (-1 punto per ogni warning)
[ ] Nomi variabili descrittivi (+2 punti)
[ ] Gestione errori presente (+2 punti)
[ ] Commenti utili presenti (+1 punto)
[ ] Best practices seguite (+2 punti)
[ ] Test inclusi e funzionanti (+3 punti)
```

---

## 9. Soluzioni e Spiegazioni

### 9.1 Note sulle Soluzioni

Le soluzioni fornite in questo documento sono **esempi di riferimento**. Durante la verifica reale:

- **Non esiste una sola soluzione corretta**
- Approcci diversi possono essere ugualmente validi
- La valutazione considera correttezza, qualità e completezza
- L'uso di IA è incoraggiato ma deve essere validato

### 9.2 Analisi Errori Comuni

**Errore 1: Prompt Troppo Vago**
```
❌ "Scrivi codice per Arduino con LED"
✅ "Scrivi sketch Arduino Uno che lampeggi LED su pin 13 
    ogni 500ms usando millis() (non delay)"
```

**Errore 2: Non Validare Output IA**
```cpp
// ❌ Accetta senza controllo:
char *str = strdup(input);  // strdup non è C standard!

// ✅ Verifica e corregge:
char *str = malloc(strlen(input) + 1);
strcpy(str, input);
```

**Errore 3: Ignorare Edge Cases**
```cpp
// ❌ Non gestisce array vuoto:
int max = arr[0];

// ✅ Gestisce edge case:
if (n <= 0) return error_code;
int max = arr[0];
```

---

## 10. Preparazione alla Verifica

### 10.1 Checklist Pre-Verifica

**Una settimana prima:**
- [ ] Ripassare Modulo 1: Fondamenti IA
  - [ ] Categorie IA
  - [ ] LLM e allucinazioni
  - [ ] Limiti e bias
- [ ] Ripassare Modulo 2: Prompt Engineering
  - [ ] Struttura prompt efficace
  - [ ] Pattern (Zero-shot, Few-shot)
  - [ ] Metodologia Spec→Code→Test
- [ ] Ripassare Modulo 3: Programmazione C
  - [ ] Gestione memoria (malloc/free)
  - [ ] Puntatori e array
  - [ ] Funzioni stringhe sicure
- [ ] Ripassare Modulo 4: Arduino
  - [ ] Pinout e configurazione
  - [ ] millis() vs delay()
  - [ ] Sensori analogici
  - [ ] Comunicazione seriale

**Il giorno prima:**
- [ ] Testare setup hardware Arduino
- [ ] Verificare librerie installate
- [ ] Preparare workspace pulito
- [ ] Dormire almeno 8 ore

**Il giorno della verifica:**
- [ ] Arrivare 10 minuti prima
- [ ] Computer carico
- [ ] Dispense stampate/digitali pronte
- [ ] Cavi USB funzionanti

### 10.2 Strategia Durante la Verifica

**Tempo Management:**
```
0-5 min:    Lettura completa di tutte le sezioni
5-20 min:   Sezione A (IA) - scelta multipla
20-40 min:  Sezione B (Prompt) - domande aperte
40-75 min:  Sezione C (C) - esercizi pratici
75-105 min: Sezione D (Arduino) - sketch
105-120 min: Sezione E (Progetto) - integrato
```

**Priorità:**
1. Completa TUTTO a livello base (60% del punteggio)
2. Migliora qualità dove hai tempo (30% del punteggio)
3. Aggiungi extra/ottimizzazioni (10% del punteggio)

**Se sei in ritardo:**
- Salta documentazione avanzata
- Test minimali ma presenti
- Commenta cosa faresti con più tempo

### 10.3 Simulazione Verifica

**Esercizio consigliato**: Prova a completare questa dispensa in 2 ore simulando condizioni reali.

**Autovalutazione:**
1. Calcola il tuo punteggio usando le rubriche
2. Identifica aree deboli
3. Rivedi quelle sezioni
4. Riprova dopo 2-3 giorni

---

## ✅ Checklist Finale

**Prima di consegnare la verifica:**

- [ ] Tutti i file nominati correttamente
- [ ] Codice compila senza errori
- [ ] Test eseguiti e funzionanti
- [ ] Documentazione presente
- [ ] Diagrammi completi
- [ ] Nome e cognome su tutti i file
- [ ] Tempo utilizzato: ___/120 minuti

**Autovalutazione stimata:**
- Sezione A: ___/18 punti
- Sezione B: ___/15 punti
- Sezione C: ___/27 punti
- Sezione D: ___/20 punti
- Sezione E: ___/20 punti
- **Totale stimato: ___/100 punti**

---

## 📚 Conclusione del Corso

Questa verifica conclude il percorso formativo su **Intelligenza Artificiale e Programmazione Assistita**. 

Le competenze acquisite rappresentano una base solida per:
- Sviluppo software professionale assistito da IA
- Programmazione embedded e IoT
- Progettazione sistemi industriali
- Continuo apprendimento tecnologico

**Ricorda:**
> L'IA è uno strumento potente, ma il pensiero critico, 
> la capacità di validazione e la competenza tecnica 
> rimangono fondamentali per l'ingegnere moderno.

**Buona verifica e... in bocca al lupo! 🍀**

---

**Fine Modulo 5 - Verifica Finale**

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita  
**Docente:** [Nome Docente]  
**Anno Accademico:** 2024/2025

