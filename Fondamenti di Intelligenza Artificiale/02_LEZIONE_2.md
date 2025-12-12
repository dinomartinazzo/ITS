# 📘 LEZIONE 2: PROMPT ENGINEERING E PROGRAMMAZIONE BASE
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Durata:** 2 ore
**Struttura:** 1 ora teoria + 1 ora pratica
**Livello:** Base-Intermedio
**Prerequisiti:** Lezione 1 completata, familiarità base con almeno 1 LLM

---

## 🎯 Obiettivi della Lezione

Al termine di questa lezione sarai in grado di:

✅ **Applicare** il framework CLEAR per scrivere prompt efficaci
✅ **Utilizzare** tecniche avanzate: Zero-shot, Few-shot, Chain-of-Thought
✅ **Generare** codice C completo e robusto con l'IA
✅ **Validare** criticamente l'output dell'IA
✅ **Creare** una libreria personale di prompt riutilizzabili
✅ **Debuggare** codice con assistenza IA
✅ **Riconoscere** pattern di prompt efficaci vs inefficaci
✅ **Iterare** e raffinare prompt per risultati ottimali

---

## 📋 Struttura della Lezione

### **PARTE 1: TEORIA (60 minuti)**

1. **Introduzione al Prompt Engineering** (10 min)
   - Cos'è il Prompt Engineering
   - Perché è una skill fondamentale
   - Anatomia di un prompt efficace

2. **Framework CLEAR** (15 min)
   - Context (Contesto)
   - Length (Lunghezza)
   - Examples (Esempi)
   - Action (Azione)
   - Role (Ruolo)

3. **Tecniche Avanzate** (20 min)
   - Zero-shot Prompting
   - Few-shot Learning
   - Chain-of-Thought (CoT)
   - Role Prompting
   - Template Prompting

4. **Validazione Critica dell'Output** (15 min)
   - Checklist di validazione
   - Red flags comuni
   - Testing metodico
   - Quando fidarsi vs quando dubitare

### **PARTE 2: PRATICA (60 minuti)**

5. **Workshop: Prompt per Codice C** (20 min)
   - Esercizi guidati progressivi
   - Da prompt basico a prompt avanzato
   - Analisi comparativa degli output

6. **Debug Assistito con IA** (15 min)
   - Tecniche di debugging collaborativo
   - Spiegare bug all'IA
   - Iterazione fino alla soluzione

7. **Creare Libreria di Prompt** (15 min)
   - Template riutilizzabili
   - Organizzazione e categorizzazione
   - Best practices

8. **Casi Studio e Analisi** (10 min)
   - Prompt falliti: cosa non fare
   - Prompt di successo: cosa funziona
   - Lezioni apprese

---

---

# PARTE 1: TEORIA (60 MINUTI)

---

## 1. INTRODUZIONE AL PROMPT ENGINEERING (10 minuti)

### 1.1 Cos'è il Prompt Engineering

**Definizione:**

> **Prompt Engineering** è l'arte e la scienza di formulare richieste (prompt) a sistemi di IA in modo da ottenere output di alta qualità, precisi e utili.

**Analogia:** Immagina l'IA come un dipendente molto capace ma letterale:

```
👨 Capo (tu): "Fammi un report"
🤖 Dipendente (IA): "Ecco un report generico di 2 righe"
👨 Capo: "No, intendevo report vendite Q1, con grafici, confronto anno scorso"
🤖 Dipendente: "Ah! Ecco report dettagliato e preciso"
```

**Il prompt engineering è imparare a comunicare in modo specifico ed efficace** con questo "dipendente".

### 1.2 Perché è una Skill Fondamentale

**Dati di produttività:**

Studi recenti (2024) mostrano che:

- 📊 **Sviluppatori esperti in prompting:** 55% più veloci
- 📊 **Sviluppatori senza skill di prompting:** Solo 20% più veloci
- 📊 **Differenza:** Il prompting **tripla** i benefici dell'IA

**Esempio concreto:**

**Prompt povero:**
```
Scrivi codice per lista
```

**Risultato:** Codice generico, probabilmente Python, non specificato, inutile.

**Prompt ottimizzato:**
```
Scrivi una implementazione completa di linked list in C99 con:
- Struttura nodo con void* per dati generici
- Funzioni: create, append, prepend, delete, free_all
- Gestione errori (malloc failures)
- Esempio d'uso con commenti
- Memory-safe (nessun leak)
```

**Risultato:** Codice production-ready, completo, testabile.

**Differenza:** 10 minuti vs 60 minuti di lavoro.

### 1.3 Anatomia di un Prompt Efficace

**Componenti chiave:**

```
┌──────────────────────────────────────────────┐
│  PROMPT EFFICACE                             │
├──────────────────────────────────────────────┤
│  1. CONTESTO                                 │
│     Chi sei, cosa stai facendo              │
│                                              │
│  2. TASK SPECIFICO                           │
│     Cosa vuoi esattamente                    │
│                                              │
│  3. VINCOLI E REQUISITI                      │
│     Limiti, standard, formati                │
│                                              │
│  4. FORMATO OUTPUT                           │
│     Come strutturare la risposta             │
│                                              │
│  5. ESEMPI (opzionale)                       │
│     Mostra cosa intendi                      │
└──────────────────────────────────────────────┘
```

**Esempio annotato:**

```
[CONTESTO]
Sono uno studente ITS che sta imparando C.

[TASK]
Scrivi una funzione che verifica se un numero è primo.

[VINCOLI]
- Linguaggio: C99
- Ottimizzata (controlla solo fino a √n)
- Gestisci edge cases (n < 2)

[OUTPUT]
- Codice commentato
- Spiegazione algoritmo
- Analisi complessità
- Test cases

[ESEMPI]
is_prime(7) → true
is_prime(10) → false
is_prime(1) → false
```

**Questo prompt genererà output di qualità MOLTO superiore** a "scrivi funzione per numeri primi".

---

## 2. FRAMEWORK CLEAR (15 minuti)

Il framework **CLEAR** è un metodo sistematico per costruire prompt efficaci. Ogni lettera rappresenta un elemento chiave.

### 2.1 C = Context (Contesto)

**Definizione:** Fornisci informazioni di background rilevanti.

**Perché è importante:**
- L'IA non conosce il tuo livello di competenza
- Non sa il tuo obiettivo finale
- Non conosce i vincoli del tuo progetto

**Esempi di contesto utile:**

**❌ Senza contesto:**
```
Come faccio ordinamento veloce?
```

**✅ Con contesto:**
```
Sono uno studente ITS al primo anno. Sto lavorando su un progetto
embedded (Arduino Due) dove devo ordinare array di sensori.
Ho limitazioni di memoria (96KB RAM).
```

**Effetto:** L'IA ora sa:
- Livello: principiante
- Dominio: embedded
- Vincoli: memoria limitata
- Linguaggio: probabilmente C

**Tipi di contesto da includere:**

1. **Ruolo/Livello:**
   - "Sono uno studente al primo anno"
   - "Sono un programmatore junior"
   - "Sto imparando C dopo Python"

2. **Obiettivo finale:**
   - "Sto preparando un esame"
   - "Sto costruendo un progetto portfolio"
   - "Devo presentare questa soluzione al team"

3. **Vincoli tecnici:**
   - "Sistema embedded con 4KB RAM"
   - "Deve girare su C89 (non C99)"
   - "Non posso usare librerie esterne"

4. **Vincoli temporali:**
   - "Ho bisogno di soluzione rapida per prototipo"
   - "Questo andrà in produzione, priorità: robustezza"

### 2.2 L = Length (Lunghezza)

**Definizione:** Specifica quanto dettagliato deve essere l'output.

**Perché è importante:**
L'IA potrebbe dare:
- Risposta troppo breve (non utile)
- Risposta troppo verbosa (dispersiva)

**Esempi:**

**Per spiegazioni:**

```
❌ "Spiega i puntatori in C"
   → Potrebbe dare 10 righe o 10 pagine

✅ "Spiega i puntatori in C in 3 paragrafi brevi (max 200 parole),
    con 2 esempi di codice semplici."
```

**Per codice:**

```
❌ "Scrivi programma gestione studenti"
   → Potrebbe generare 1000 righe di codice complesso

✅ "Scrivi un programma C minimale (circa 50 righe) che gestisce
    un array di max 10 studenti con operazioni base: add, print."
```

**Indicatori di lunghezza utili:**

- "In 3 bullet points"
- "Spiegazione breve (max 100 parole)"
- "Tutorial dettagliato step-by-step (almeno 500 parole)"
- "Codice minimale (~50 righe)"
- "Implementazione completa production-ready"

### 2.3 E = Examples (Esempi)

**Definizione:** Mostra esempi concreti di input/output desiderato.

**Perché è importante:**
"Show, don't tell" → Esempi eliminano ambiguità.

**Tecnica Few-Shot (dettagli dopo):**

**Esempio per funzione:**

```
Scrivi una funzione C che converte stringhe secondo questo pattern:

Esempi:
- Input: "hello" → Output: "HELLO"
- Input: "Hello World" → Output: "HELLO WORLD"
- Input: "" → Output: ""
- Input: NULL → Output: NULL (con controllo errore)
```

**Ora l'IA sa esattamente:**
- Deve convertire a maiuscolo
- Deve gestire spazi
- Deve gestire stringa vuota
- Deve gestire NULL senza crashare

**Esempio per formato output:**

```
Genera documentazione per questa funzione nel seguente formato:

ESEMPIO:
/**
 * @brief Breve descrizione (1 riga)
 * @param nome_param Descrizione parametro
 * @return Descrizione ritorno
 * @note Note importanti (opzionale)
 */
```

### 2.4 A = Action (Azione)

**Definizione:** Usa verbi imperativi chiari che specificano esattamente cosa deve fare l'IA.

**Verbi efficaci:**

**Per codice:**
- ✅ "Scrivi una funzione C che..."
- ✅ "Implementa un algoritmo per..."
- ✅ "Genera codice completo per..."
- ✅ "Refactoring questo codice per..."

**Per debugging:**
- ✅ "Trova e correggi i bug in..."
- ✅ "Analizza questo codice e identifica problemi di..."
- ✅ "Debugga questo segmentation fault:"

**Per spiegazione:**
- ✅ "Spiega riga per riga come funziona..."
- ✅ "Descrivi l'algoritmo usato in..."
- ✅ "Confronta le differenze tra X e Y"

**Per revisione:**
- ✅ "Rivedi questo codice per memory leaks"
- ✅ "Valuta la sicurezza di questo codice"
- ✅ "Suggerisci ottimizzazioni per..."

**Verbi da evitare (troppo vaghi):**

- ❌ "Dimmi qualcosa su..."
- ❌ "Parlami di..."
- ❌ "Aiutami con..."
- ❌ "Fammi vedere..."

**Esempio comparativo:**

**❌ Vago:**
```
Aiutami con ordinamento array
```

**✅ Specifico:**
```
Implementa la funzione quicksort in C per ordinare array di interi,
includendo gestione edge cases e commenti esplicativi.
```

### 2.5 R = Role (Ruolo)

**Definizione:** Chiedi all'IA di assumere un ruolo specifico per modellare lo stile e il livello di dettaglio.

**Perché funziona:**
I LLM sono addestrati su testi dove persone con ruoli diversi scrivono in modi diversi. Specificare un ruolo attiva questi pattern.

**Ruoli utili per programmazione:**

**Ruolo: Insegnante paziente**
```
Agisci come un insegnante di programmazione paziente che spiega
concetti a studenti principianti. Usa analogie semplici e evita
jargon tecnico quando possibile.

[la tua domanda]
```

**Effetto:** Spiegazioni più chiare e pedagogiche.

**Ruolo: Senior developer esperto in C**
```
Agisci come un senior C developer con 15 anni di esperienza in
sistemi embedded e sicurezza. Rivedi questo codice con occhio
critico per vulnerabilità e anti-pattern.

[codice da rivedere]
```

**Effetto:** Analisi più profonda, focus su best practices.

**Ruolo: Code reviewer attento**
```
Agisci come un code reviewer meticoloso che deve approvare codice
per produzione. Identifica ogni potenziale bug, memory leak,
race condition, e problema di sicurezza.

[codice]
```

**Effetto:** Analisi rigorosa, nessun problema trascurato.

**Ruolo: Tutor Socratico**
```
Agisci come un tutor che usa il metodo socratico: invece di dare
la soluzione completa, guidami con domande e hint per arrivare
alla soluzione da solo.

Problema: [descrivi problema]
```

**Effetto:** Impari di più perché risolvi tu (con guida).

**Altri ruoli utili:**

- "Esperto di performance e ottimizzazione"
- "Security auditor"
- "Technical writer specializzato in documentazione chiara"
- "Debugging expert che ragiona sistematicamente"

### 2.6 Framework CLEAR: Template Completo

**Template da usare:**

```
[CONTEXT - Contesto]
Sono [ruolo/livello]. Sto lavorando su [progetto/task].
Ho [vincoli/limitazioni].

[LENGTH - Lunghezza]
Fornisci [tipo di output, livello di dettaglio].

[EXAMPLES - Esempi]
Esempi di input/output desiderato:
- [esempio 1]
- [esempio 2]

[ACTION - Azione]
[Verbo imperativo chiaro] [cosa fare esattamente].

[ROLE - Ruolo]
Agisci come [ruolo specifico].
```

**Esempio concreto applicato:**

```
[CONTEXT]
Sono uno studente ITS al primo anno. Sto imparando la gestione
memoria in C. Ho già visto malloc/free ma non puntatori complessi.

[LENGTH]
Fornisci spiegazione di 3-4 paragrafi con 2 esempi di codice
commentati (circa 30 righe totali).

[EXAMPLES]
Voglio capire scenari tipo:
- Allocare array dinamico di struct
- Liberare correttamente senza leak
- Cosa succede se dimentico free()

[ACTION]
Spiega come allocare e liberare correttamente un array dinamico
di struct in C, includendo best practices e errori comuni.

[ROLE]
Agisci come un insegnante di C paziente che usa analogie
semplici e evidenzia errori comuni dei principianti.
```

**Risultato atteso:** Output perfettamente calibrato per le tue esigenze.

---

## 3. TECNICHE AVANZATE (20 minuti)

### 3.1 Zero-Shot Prompting

**Definizione:**
Chiedi all'IA di completare un task **senza fornire esempi**.

**Quando usare:**
- Task comuni e ben definiti
- Quando non hai tempo di creare esempi
- Per spiegazioni generali

**Esempio:**

```
Scrivi una funzione C che calcola il fattoriale di un numero.
Include gestione errori per input negativi.
```

**Pro:**
- ✅ Veloce
- ✅ Funziona bene per task standard

**Contro:**
- ❌ Meno controllo su format output
- ❌ Può interpretare in modo inatteso

### 3.2 Few-Shot Learning (Tecnica Potente!)

**Definizione:**
Fornisci **2-5 esempi** di input/output desiderato prima del task reale.

**Quando usare:**
- Task con format specifico
- Stile di codice particolare
- Pattern non standard

**Struttura:**

```
[Introduzione task]

Esempi:

Esempio 1:
Input: [...]
Output: [...]

Esempio 2:
Input: [...]
Output: [...]

Esempio 3:
Input: [...]
Output: [...]

Ora, applica lo stesso pattern a:
Input: [il tuo input reale]
```

**Caso pratico: Generare commenti consistenti**

```
Voglio che tu generi commenti Doxygen per funzioni C seguendo
questo stile esatto:

Esempio 1:
Funzione: int add(int a, int b)

Commento generato:
/**
 * @brief Somma due numeri interi
 * @param a Primo operando
 * @param b Secondo operando
 * @return Somma di a e b
 */

Esempio 2:
Funzione: void print_array(int *arr, size_t size)

Commento generato:
/**
 * @brief Stampa gli elementi di un array
 * @param arr Puntatore all'array
 * @param size Numero di elementi
 * @return void
 */

Ora genera commento per:
Funzione: char* reverse_string(const char *str)
```

**Risultato:** L'IA seguirà esattamente il tuo stile.

**Magia dei few-shot:**

Funziona anche per pattern complessi che sarebbe difficile descrivere a parole.

**Esempio avanzato: Stile di naming custom**

```
Nel mio progetto uso questo naming convention:

int calculate_total_sum(int *values, size_t count);
bool is_valid_input(const char *input);
void free_memory_safely(void **ptr);

Ora genera 5 nomi di funzioni per:
1. Funzione che ordina array
2. Funzione che controlla parità
3. Funzione che alloca buffer
4. Funzione che legge configurazione
5. Funzione che valida puntatore
```

L'IA capirà il pattern (verbo_soggetto_dettaglio) e genererà nomi consistenti.

### 3.3 Chain-of-Thought (CoT) - Ragionamento Passo-Passo

**Definizione:**
Chiedi all'IA di **mostrare il ragionamento** step-by-step prima della risposta finale.

**Tecnica:**
Aggiungi al prompt: **"Ragiona passo per passo prima di rispondere"** o **"Let's think step by step"**

**Perché funziona:**
Forzare l'IA a "pensare ad alta voce" migliora la qualità del ragionamento.

**Esempio senza CoT:**

```
Questo codice ha un bug. Qual è?

int calculate_average(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i <= size; i++) {
        sum += arr[i];
    }
    return sum / size;
}
```

**Risposta tipica:** "Il bug è alla linea 3, condizione loop sbagliata"

**Esempio CON CoT:**

```
Questo codice ha un bug. Ragiona passo per passo:
1. Cosa fa il codice?
2. Quali sono gli input/output attesi?
3. Cosa succede con input edge case?
4. Dove potrebbe crashare o dare risultati sbagliati?

int calculate_average(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i <= size; i++) {
        sum += arr[i];
    }
    return sum / size;
}
```

**Risposta con CoT:**

```
Ragionamento passo per passo:

1. Cosa fa: calcola media di array di interi
2. Input: array e dimensione. Output: media (int)
3. Edge cases problematici:
   - size = 0 → divisione per zero!
   - i <= size → off-by-one! Accede arr[size] che è fuori bounds
4. Con arr di 5 elementi (indici 0-4) e size=5:
   - Loop va da i=0 a i=5 (6 iterazioni)
   - arr[5] è fuori bounds → segmentation fault

Bug identificati:
1. ⚠️ CRITICO: i <= size deve essere i < size (off-by-one)
2. ⚠️ CRITICO: Manca controllo size == 0 (divisione per zero)
3. ⚠️ Warning: integer division perde decimali (considerare float)

Codice corretto:
[...]
```

**Molto più dettagliato e utile!**

**Quando usare CoT:**
- Debugging complesso
- Analisi algoritmica
- Scelte di design (quale approccio usare?)
- Problemi con più soluzioni possibili

### 3.4 Role Prompting Avanzato

Abbiamo visto role nel framework CLEAR. Ecco tecniche avanzate:

**Tecnica: Persona dettagliata**

Invece di ruolo generico, crea una "persona" con caratteristiche specifiche:

```
Agisci come Linus Torvalds reviewando codice per il kernel Linux.
Sei estremamente critico su:
- Performance
- Memory management
- Race conditions
- Codice "clever" ma non chiaro

Usa tono diretto e senza fronzoli. Evidenzia ogni problema
senza sugarcoating.

[codice da revieware]
```

**Effetto:** Review MOLTO più rigorosa.

**Tecnica: Multi-role perspective**

Chiedi analisi da più punti di vista:

```
Analizza questo codice da 3 prospettive:

1. Come SECURITY EXPERT: identifica vulnerabilità
2. Come PERFORMANCE ENGINEER: trova bottleneck
3. Come MAINTAINABILITY EXPERT: valuta leggibilità

[codice]
```

**Effetto:** Analisi completa a 360°.

### 3.5 Template Prompting

**Definizione:**
Usa template riutilizzabili con placeholder da riempire.

**Esempio template per generazione funzione C:**

```
Scrivi una funzione C con queste specifiche:

**Firma:**
[RETURN_TYPE] [FUNCTION_NAME]([PARAMETERS])

**Comportamento:**
[DESCRIZIONE COSA FA]

**Input:**
- [PARAMETRO_1]: [descrizione e vincoli]
- [PARAMETRO_2]: [descrizione e vincoli]

**Output:**
- [descrizione return value e possibili valori speciali]

**Edge cases da gestire:**
- [edge case 1]
- [edge case 2]

**Vincoli:**
- Standard: [C89/C99/C11]
- [altri vincoli]

**Includi:**
- Commenti esplicativi
- Controllo errori
- Esempio d'uso
```

**Uso:**

Salva questo template. Ogni volta che serve una funzione, riempi i placeholder.

**Esempio riempito:**

```
Scrivi una funzione C con queste specifiche:

**Firma:**
char* string_duplicate(const char *src)

**Comportamento:**
Crea una copia dinamica della stringa src

**Input:**
- src: stringa sorgente (può essere NULL)

**Output:**
- Puntatore a nuova stringa allocata (NULL se errore)

**Edge cases da gestire:**
- src == NULL → ritorna NULL
- malloc fallisce → ritorna NULL
- stringa vuota → ritorna stringa vuota allocata

**Vincoli:**
- Standard: C99
- Usa malloc (non calloc o strdup)

**Includi:**
- Commenti esplicativi
- Controllo errori
- Esempio d'uso
```

**Vantaggio:** Consistenza + velocità.

### 3.6 Iterative Refinement (Raffinamento Iterativo)

**Tecnica:**
Non aspettarti perfezione al primo prompt. Raffina in multiple iterazioni.

**Pattern:**

```
Iterazione 1: Richiesta base
            ↓
         [Output V1]
            ↓
Iterazione 2: "Migliora X, aggiungi Y"
            ↓
         [Output V2]
            ↓
Iterazione 3: "Ottimizza per Z"
            ↓
         [Output V3 - Finale]
```

**Esempio pratico:**

**Iterazione 1:**
```
Scrivi funzione C che legge file
```

**Output:** Codice basico senza controlli.

**Iterazione 2:**
```
Migliora aggiungendo:
- Controllo errori (fopen, fread)
- Gestione file grandi (lettura a chunk)
- Ritorno codice errore
```

**Output:** Codice più robusto.

**Iterazione 3:**
```
Ottimizza per performance:
- Usa buffer size ottimale (4KB?)
- Minimizza system calls
```

**Output:** Codice production-ready.

**Quando usare:**
- Task complessi
- Quando non sei sicuro di tutti i requisiti
- Per apprendere (vedi evoluzione del codice)

---

## 4. VALIDAZIONE CRITICA DELL'OUTPUT (15 minuti)

### 4.1 Checklist di Validazione

**Prima di usare codice generato dall'IA, verifica SEMPRE:**

**✅ Checklist Compilazione:**

- [ ] **Compila senza errori**
  ```bash
  gcc -Wall -Wextra -Werror file.c
  ```

- [ ] **Compila con flag di sicurezza**
  ```bash
  gcc -Wall -Wextra -Wpedantic -Werror file.c
  ```

- [ ] **Nessun warning ignorato**
  Anche un warning può indicare bug sottile

**✅ Checklist Correttezza:**

- [ ] **Include tutti gli header necessari**
  - `<stdio.h>` per I/O
  - `<stdlib.h>` per malloc/free
  - `<string.h>` per string functions
  - Nessun header "inventato"

- [ ] **Funzioni standard esistono davvero**
  Verifica su cppreference.com

- [ ] **Logica corretta**
  Traccia mentalmente (o su carta) l'esecuzione

**✅ Checklist Sicurezza:**

- [ ] **Controllo puntatori NULL**
  ```c
  if (ptr == NULL) {
      // gestione errore
  }
  ```

- [ ] **Controllo malloc success**
  ```c
  int *arr = malloc(size * sizeof(int));
  if (arr == NULL) {
      return ERROR_CODE;
  }
  ```

- [ ] **Nessun buffer overflow**
  ```c
  // ❌ PERICOLOSO
  char buffer[10];
  scanf("%s", buffer); // può scrivere oltre buffer!

  // ✅ SICURO
  char buffer[10];
  scanf("%9s", buffer); // max 9 char + \0
  ```

- [ ] **Ogni malloc ha un free**
  Valgrind check:
  ```bash
  valgrind --leak-check=full ./program
  ```

- [ ] **No funzioni deprecate/pericolose**
  - ❌ `gets()` → usa `fgets()`
  - ❌ `strcpy()` → usa `strncpy()` o `strlcpy()`
  - ❌ `sprintf()` → usa `snprintf()`

**✅ Checklist Testing:**

- [ ] **Test con input normale**
- [ ] **Test con input edge case**
  - Array vuoto (size = 0)
  - Puntatori NULL
  - Numeri negativi
  - Stringhe vuote
- [ ] **Test con input invalido**
  - Cosa succede con input assurdo?

**✅ Checklist Documentazione:**

- [ ] **Commenti spiegano WHY, non WHAT**
  ```c
  // ❌ Male
  i++; // incrementa i

  // ✅ Bene
  i++; // Skip header row (data starts at index 1)
  ```

- [ ] **Nomi variabili significativi**
  - ❌ `int a, b, c;`
  - ✅ `int student_count, max_score, average;`

### 4.2 Red Flags Comuni

**🚩 Red Flag #1: Librerie "strane"**

```c
#include <fastmath.h>  // ← MAI SENTITA? VERIFICA!
#include <easyfile.h>  // ← PROBABILMENTE INVENTATA
```

**Verifica:** Cerca "libname C library" su Google.

**🚩 Red Flag #2: Funzioni con nomi "troppo perfetti"**

```c
// Troppo bello per essere vero?
secure_malloc();
safe_strcpy();
auto_free();
```

Se il nome descrive esattamente quello di cui hai bisogno ma non l'hai mai visto → probabilmente inventato.

**🚩 Red Flag #3: Codice che "sembra troppo semplice"**

```c
// L'IA suggerisce:
int *arr = malloc(size);  // ← Manca sizeof(int)!
free(arr);
arr = NULL;  // ← Inutile dopo free
```

Se qualcosa sembra "troppo facile" rispetto a quello che sai, verifica attentamente.

**🚩 Red Flag #4: Gestione errori assente**

```c
FILE *fp = fopen("file.txt", "r");
// ← Manca: if (fp == NULL) return error;

char *str = malloc(100);
// ← Manca: if (str == NULL) return error;
```

Codice senza controlli errori → da rivedere completamente.

**🚩 Red Flag #5: Commenti evasivi**

```c
// Questo fa qualcosa di complesso
complex_function();

// Magic happens here
magic_code();
```

Se l'IA usa commenti vaghi → probabilmente non "capisce" davvero cosa sta facendo.

### 4.3 Testing Metodico

**Strategia di testing in 4 livelli:**

**Livello 1: Smoke Test (Test di fumo)**

```c
// Compila?
gcc file.c

// Gira senza crashare?
./a.out

// Output sensato?
echo $?  // exit code
```

**Livello 2: Happy Path Test**

```c
// Test con input "normale" previsto
int result = my_function(valid_input);
assert(result == expected_output);
```

**Livello 3: Edge Case Test**

```c
// Test edge cases
assert(my_function(NULL) == ERROR);
assert(my_function("") == EMPTY_RESULT);
assert(my_function(MAX_INT) handles_correctly);
```

**Livello 4: Stress Test**

```c
// Input molto grandi
int huge_array[10000];
// Loop molte iterazioni
for (int i = 0; i < 1000000; i++) { ... }
// Valgrind memory check
valgrind ./program
```

**Esempio completo di test:**

```c
// Funzione da testare (generata da IA)
int find_max(int *arr, int size);

// Test suite
void test_find_max() {
    // Test 1: Happy path
    int arr1[] = {1, 5, 3, 9, 2};
    assert(find_max(arr1, 5) == 9);

    // Test 2: Array singolo elemento
    int arr2[] = {42};
    assert(find_max(arr2, 1) == 42);

    // Test 3: Tutti elementi uguali
    int arr3[] = {7, 7, 7};
    assert(find_max(arr3, 3) == 7);

    // Test 4: Numeri negativi
    int arr4[] = {-5, -2, -8};
    assert(find_max(arr4, 3) == -2);

    // Test 5: Edge case - NULL
    assert(find_max(NULL, 5) == ERROR_CODE);

    // Test 6: Edge case - size zero
    assert(find_max(arr1, 0) == ERROR_CODE);

    printf("✅ Tutti test passed!\n");
}
```

### 4.4 Quando Fidarsi vs Quando Dubitare

**🟢 Alta confidenza (ma verifica comunque):**

- Task molto comune (es: "scrivi hello world in C")
- Codice breve e semplice (<50 righe)
- Spiegazioni di concetti standard
- Algoritmi classici (sort, search, ecc.)

**🟡 Media confidenza (verifica attentamente):**

- Gestione memoria complessa
- Multi-threading
- Parsing di formati
- Interazione con OS (file, processi)

**🔴 Bassa confidenza (verifica MOLTO attentamente):**

- Codice di sicurezza (crittografia, auth)
- Driver o codice kernel
- Codice embedded con vincoli strict
- Ottimizzazioni avanzate
- Uso di librerie non mainstream

**Regola d'oro:**

> **"La tua responsabilità non diminuisce perché l'IA ha scritto il codice. Se va in produzione con il tuo nome, tu sei responsabile."**

### 4.5 Strumenti di Validazione

**Static Analysis:**

```bash
# Cppcheck - trova bug senza eseguire codice
cppcheck --enable=all file.c

# Clang Static Analyzer
clang --analyze file.c

# GCC con max warning
gcc -Wall -Wextra -Wpedantic -Werror file.c
```

**Dynamic Analysis:**

```bash
# Valgrind - memory leaks e invalid access
valgrind --leak-check=full ./program

# AddressSanitizer - memory errors (più veloce di valgrind)
gcc -fsanitize=address file.c
./a.out
```

**Fuzzing (avanzato):**

```bash
# AFL - trova input che crashano il programma
afl-fuzz -i input_dir -o output_dir ./program @@
```

---

---

# PARTE 2: PRATICA (60 MINUTI)

---

## 5. WORKSHOP: PROMPT PER CODICE C (20 minuti)

### 5.1 Esercizio Guidato #1: Evoluzione di un Prompt

**Obiettivo:** Vedere come prompt progressivamente migliori generano output migliori.

**Scenario:** Vuoi una funzione che conta le vocali in una stringa.

---

**TENTATIVO 1: Prompt Minimo**

```
scrivi funzione conta vocali
```

**Analizza l'output ricevuto:**

Probabilmente hai ricevuto:
- Linguaggio: forse Python, forse C (non specificato)
- Gestione errori: probabilmente assente
- Commenti: scarsi o assenti
- Test: nessuno

**Valutazione: 3/10** ⭐⭐⭐

---

**TENTATIVO 2: Prompt con Linguaggio Specificato**

```
Scrivi una funzione C che conta le vocali in una stringa
```

**Miglioramenti:**
- ✅ Linguaggio specificato: C
- ❌ Ancora mancante: case sensitivity? NULL handling?

**Valutazione: 5/10** ⭐⭐⭐⭐⭐

---

**TENTATIVO 3: Prompt con Requisiti**

```
Scrivi una funzione C che conta le vocali (a,e,i,o,u) in una stringa.

Requisiti:
- Case insensitive ('A' e 'a' entrambe contano)
- Gestisci stringa NULL (ritorna -1)
- Gestisci stringa vuota (ritorna 0)
```

**Miglioramenti:**
- ✅ Comportamento chiaro
- ✅ Edge cases specificati
- ❌ Manca: firma funzione, commenti

**Valutazione: 7/10** ⭐⭐⭐⭐⭐⭐⭐

---

**TENTATIVO 4: Prompt Ottimale (Framework CLEAR)**

```
[CONTEXT]
Sono uno studente ITS. Sto creando una libreria di utility
per manipolazione stringhe in C99.

[ACTION]
Scrivi una funzione C che conta le vocali in una stringa.

[SPECIFICHE]
- Nome: count_vowels
- Firma: int count_vowels(const char *str)
- Comportamento: conta a,e,i,o,u (case insensitive)
- Ritorna: numero vocali, oppure -1 se str è NULL

[EXAMPLES]
- count_vowels("Hello") → 2 (e,o)
- count_vowels("AEIOU") → 5
- count_vowels("xyz") → 0
- count_vowels("") → 0
- count_vowels(NULL) → -1

[OUTPUT]
Includi:
- Codice completo
- Commenti Doxygen
- Unit test con assert
```

**Risultato atteso:**

```c
#include <stdio.h>
#include <ctype.h>
#include <assert.h>

/**
 * @brief Conta il numero di vocali in una stringa
 * @param str Stringa da analizzare (può essere NULL)
 * @return Numero di vocali (a,e,i,o,u, case insensitive),
 *         -1 se str è NULL
 */
int count_vowels(const char *str) {
    if (str == NULL) {
        return -1;
    }

    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        char c = tolower(str[i]);
        if (c == 'a' || c == 'e' || c == 'i' ||
            c == 'o' || c == 'u') {
            count++;
        }
    }
    return count;
}

// Unit tests
void test_count_vowels() {
    assert(count_vowels("Hello") == 2);
    assert(count_vowels("AEIOU") == 5);
    assert(count_vowels("xyz") == 0);
    assert(count_vowels("") == 0);
    assert(count_vowels(NULL) == -1);
    printf("✅ All tests passed!\n");
}

int main() {
    test_count_vowels();
    return 0;
}
```

**Valutazione: 10/10** ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

**Codice production-ready, testato, documentato!**

---

**🎯 Esercizio per te:**

Applica la stessa progressione a questa richiesta:

**Task:** Funzione che inverte una stringa

**Step:**
1. Scrivi prompt minimo
2. Scrivi prompt con linguaggio
3. Scrivi prompt con requisiti
4. Scrivi prompt ottimale (CLEAR)

Confronta gli output!

---

### 5.2 Esercizio Guidato #2: Few-Shot per Stile Codice

**Obiettivo:** Insegnare all'IA il TUO stile di codice.

**Scenario:** Hai uno stile di error handling specifico che vuoi mantenere consistente.

**Il tuo stile:**

```c
// Tutte le funzioni ritornano int (0 = success, -1 = errore)
// Output tramite parametri puntatore

int my_function(input_type input, output_type *output) {
    // Validazione input
    if (input == NULL || output == NULL) {
        fprintf(stderr, "Error: NULL parameter\n");
        return -1;
    }

    // Logica
    // ...

    // Success
    *output = result;
    return 0;
}
```

**Few-Shot Prompt:**

```
Voglio che tu generi funzioni C seguendo questo pattern esatto:

═══════════════════════════════════════════════════
ESEMPIO 1:

Task: Funzione che raddoppia un numero

Codice generato:
/**
 * @brief Raddoppia un numero intero
 * @param input Numero da raddoppiare
 * @param output Puntatore al risultato
 * @return 0 se successo, -1 se errore
 */
int double_number(int input, int *output) {
    if (output == NULL) {
        fprintf(stderr, "Error: NULL output pointer\n");
        return -1;
    }

    *output = input * 2;
    return 0;
}
═══════════════════════════════════════════════════

═══════════════════════════════════════════════════
ESEMPIO 2:

Task: Funzione che calcola lunghezza stringa

Codice generato:
/**
 * @brief Calcola la lunghezza di una stringa
 * @param input Stringa da misurare
 * @param output Puntatore alla lunghezza
 * @return 0 se successo, -1 se errore
 */
int string_length(const char *input, size_t *output) {
    if (input == NULL || output == NULL) {
        fprintf(stderr, "Error: NULL parameter\n");
        return -1;
    }

    *output = strlen(input);
    return 0;
}
═══════════════════════════════════════════════════

Ora genera una funzione seguendo LO STESSO IDENTICO PATTERN per:

Task: Funzione che verifica se numero è pari
```

**Risultato atteso:**

L'IA genererà codice che segue esattamente il tuo stile!

```c
/**
 * @brief Verifica se un numero è pari
 * @param input Numero da verificare
 * @param output Puntatore al risultato (1 se pari, 0 se dispari)
 * @return 0 se successo, -1 se errore
 */
int is_even(int input, int *output) {
    if (output == NULL) {
        fprintf(stderr, "Error: NULL output pointer\n");
        return -1;
    }

    *output = (input % 2 == 0) ? 1 : 0;
    return 0;
}
```

**🎯 Esercizio per te:**

Crea il tuo stile personale:
1. Decidi il tuo pattern preferito (return value? errno? struct per errori?)
2. Crea 2 esempi
3. Chiedi all'IA di generare 3 nuove funzioni nel tuo stile

---

### 5.3 Esercizio Guidato #3: Chain-of-Thought per Debugging

**Scenario:** Hai questo codice con bug nascosto.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concatenate(const char *str1, const char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    char *result = malloc(len1 + len2);

    strcpy(result, str1);
    strcat(result, str2);

    return result;
}

int main() {
    char *s = concatenate("Hello", " World");
    printf("%s\n", s);
    free(s);
    return 0;
}
```

**Prompt SENZA Chain-of-Thought:**

```
Questo codice ha un bug. Quale?

[codice]
```

**Risposta tipica:** "Manca +1 per null terminator alla linea 8"

**Prompt CON Chain-of-Thought:**

```
Questo codice ha un bug. Analizzalo usando Chain-of-Thought:

1. Cosa dovrebbe fare il codice?
2. Traccia l'esecuzione con esempio: str1="Hello", str2=" World"
3. Calcola memoria necessaria step-by-step
4. Identifica dove la memoria allocata non basta
5. Spiega le conseguenze del bug
6. Fornisci fix

[codice]
```

**Risposta con CoT:**

```
Analisi Chain-of-Thought:

1. OBIETTIVO: Concatenare due stringhe dinamicamente

2. TRACE CON ESEMPIO:
   - str1 = "Hello" → len1 = 5
   - str2 = " World" → len2 = 6
   - Totale caratteri: 5 + 6 = 11

3. MEMORIA NECESSARIA:
   - Caratteri: 11
   - Null terminator: 1
   - TOTALE: 12 byte

4. MEMORIA ALLOCATA:
   - malloc(len1 + len2) = malloc(5 + 6) = malloc(11)
   - ALLOCATO: 11 byte
   - NECESSARIO: 12 byte
   - ⚠️ MANCA 1 BYTE per \0!

5. CONSEGUENZE:
   - strcat() scrive \0 oltre il buffer allocato
   - Buffer overflow!
   - Undefined behavior: può crashare o corrompere heap

6. FIX:
   char *result = malloc(len1 + len2 + 1); // +1 per \0
   if (result == NULL) {
       return NULL; // Gestione malloc failure
   }
```

**Molto più educativo e completo!**

---

## 6. DEBUG ASSISTITO CON IA (15 minuti)

### 6.1 Tecnica: Rubber Duck Debugging con IA

**Cos'è:** Spiega il codice all'IA come se fosse un "rubber duck" (paperella di gomma).

**Perché funziona:** Spiegare ad alta voce (o per iscritto) ti forza a pensare sistematicamente.

**Prompt template:**

```
Ho questo bug: [descrivi sintomo]

Lasciami spiegare il codice riga per riga cosa DOVREBBE fare:
[spiega la tua intenzione]

Ecco il codice:
[codice]

Aiutami a trovare dove l'implementazione non corrisponde all'intenzione.
```

**Esempio:**

```
Ho questo bug: il programma stampa sempre -1 invece del massimo.

Lasciami spiegare cosa DOVREBBE fare:
1. Prendere array di interi
2. Trovare il valore massimo
3. Stampare quel valore

Ecco il codice:
```c
int find_max(int *arr, int size) {
    int max = 0;  // inizializzo max a 0
    for (int i = 0; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

int main() {
    int numbers[] = {-5, -2, -8, -1};
    printf("Max: %d\n", find_max(numbers, 4));
}
```

**L'IA risponderà:**

```
Il bug è alla riga 2: max inizializzato a 0.

Problema:
- Con array di tutti numeri negativi (es: -5,-2,-8,-1)
- Nessun numero è > 0
- max rimane 0
- Ma 0 non è nell'array!

Fix: Inizializza max al primo elemento:
int max = arr[0];
// oppure
int max = INT_MIN; // da <limits.h>
```

### 6.2 Tecnica: Debugging Incrementale

**Step 1: Isola il problema**

```
Ho un programma di 200 righe che crasha. Come posso isolare
dove avviene il crash?

[codice o descrizione]
```

**Step 2: Aggiungi logging**

```
Aiutami ad aggiungere printf di debug strategici in questo codice
per capire dove fallisce:

[codice]
```

**Step 3: Analizza output**

```
Ho aggiunto debug prints e questo è l'output:

[output]

Cosa mi dice questo sul bug?
```

**Step 4: Fix**

```
Ora che sappiamo il problema è [X], come posso fixarlo?
```

### 6.3 Esercizio: Debug Challenge

**Ti do codice con bug. Trova e correggi usando IA:**

```c
#include <stdio.h>
#include <string.h>

void reverse_words(char *str) {
    int len = strlen(str);
    int start = 0;

    for (int i = 0; i <= len; i++) {
        if (str[i] == ' ' || str[i] == '\0') {
            // Inverti parola da start a i-1
            int left = start;
            int right = i - 1;

            while (left < right) {
                char temp = str[left];
                str[left] = str[right];
                str[right] = temp;
                left++;
                right--;
            }

            start = i + 1;
        }
    }
}

int main() {
    char str[] = "Hello World";
    reverse_words(str);
    printf("%s\n", str); // Dovrebbe stampare: "olleH dlroW"
    return 0;
}
```

**Prompt per debugging:**

```
Questo codice dovrebbe invertire ogni parola singolarmente
(ma non l'ordine delle parole).

Input: "Hello World"
Output atteso: "olleH dlroW"
Output attuale: [prova tu!]

Usa Chain-of-Thought:
1. Traccia esecuzione passo per passo
2. Identifica eventuali bug
3. Fornisci fix se necessario
```

**🎯 Prova tu!** Usa l'IA per debuggare.

---

## 7. CREARE LIBRERIA DI PROMPT (15 minuti)

### 7.1 Concetto: Il Tuo "Prompt Toolkit"

**Idea:** Crea una collezione di prompt testati e riutilizzabili per task comuni.

**Struttura consigliata:**

```
my_prompts/
├── code_generation/
│   ├── c_function.md
│   ├── data_structure.md
│   └── algorithm.md
├── debugging/
│   ├── find_bug.md
│   ├── memory_leak.md
│   └── segfault.md
├── documentation/
│   ├── function_doc.md
│   ├── readme.md
│   └── comments.md
└── learning/
    ├── explain_concept.md
    └── compare_approaches.md
```

### 7.2 Template: Generazione Funzione C

**File: `c_function.md`**

```markdown
# Template: Genera Funzione C

Scrivi una funzione C con queste specifiche:

**Firma:**
[RETURN_TYPE] [FUNCTION_NAME]([PARAMETERS])

**Comportamento:**
[DESCRIZIONE DETTAGLIATA]

**Parametri:**
- [PARAM_1]: [descrizione e vincoli]
- [PARAM_2]: [descrizione e vincoli]

**Valore di ritorno:**
[Descrizione del return value]

**Edge cases:**
- [Caso 1]: [comportamento atteso]
- [Caso 2]: [comportamento atteso]

**Vincoli:**
- Standard: C99
- Nessuna libreria esterna
- Memory-safe

**Output richiesto:**
- [x] Codice completo
- [x] Commenti Doxygen
- [x] Gestione errori
- [x] Esempio d'uso
- [x] Unit test (opzionale)

---

## Esempio d'uso del template:

[RETURN_TYPE] = int
[FUNCTION_NAME] = is_palindrome
[PARAMETERS] = const char *str
[DESCRIZIONE] = Verifica se una stringa è palindroma
[Edge cases]:
  - NULL → ritorna -1 (errore)
  - Stringa vuota → ritorna 1 (true)
  - Singolo carattere → ritorna 1 (true)
```

### 7.3 Template: Debug Memory Leak

**File: `memory_leak.md`**

```markdown
# Template: Debug Memory Leak

Ho un memory leak in questo codice. Aiutami a trovarlo.

**Contesto:**
[Descrivi cosa fa il programma]

**Sintomi:**
- Valgrind output: [incolla output]
- Comportamento osservato: [descrivi]

**Codice:**
```c
[incolla codice]
```

**Analisi richiesta:**
1. Identifica ogni malloc/calloc/realloc
2. Verifica che ognuno abbia corrispondente free
3. Controlla percorsi di errore (early return senza free?)
4. Verifica ownership (chi è responsabile di free?)
5. Suggerisci fix con codice corretto

**Tool usati:**
- Valgrind: [versione]
- Compiler: gcc [versione]
```

### 7.4 Template: Confronto Approcci

**File: `compare_approaches.md`**

```markdown
# Template: Confronta Approcci

Ho bisogno di [OBIETTIVO]. Confronta questi approcci:

**Approccio A:** [Descrizione]
**Approccio B:** [Descrizione]
**Approccio C:** [Descrizione] (opzionale)

**Criteri di confronto:**
1. **Performance:** Big-O time e space complexity
2. **Memoria:** Uso memoria (heap vs stack)
3. **Semplicità:** Facilità implementazione/manutenzione
4. **Robustezza:** Gestione errori ed edge cases
5. **Portabilità:** Dipendenze e compatibilità

**Formato output:**
| Criterio | Approccio A | Approccio B | Approccio C |
|----------|-------------|-------------|-------------|
| ...      | ...         | ...         | ...         |

**Raccomandazione finale:** [Quale approccio è meglio e perché]

---

Esempio:
OBIETTIVO = Ordinare array di struct
Approccio A = qsort() standard library
Approccio B = Implementare quicksort custom
Approccio C = Insertion sort per array piccoli
```

### 7.5 Esercizio: Crea i Tuoi Template

**Task:** Crea 3 template per task che fai spesso.

**Suggerimenti:**
1. Pensa agli ultimi 5 task di programmazione che hai fatto
2. Quali erano ripetitivi?
3. Crea template riutilizzabile per quelli

**Esempio aree:**
- Generazione struct
- Parsing file (CSV, JSON, config)
- Error handling pattern
- Test unit creation
- Performance optimization

**Salva in:** `my_prompt_library/`

---

## 8. CASI STUDIO E ANALISI (10 minuti)

### 8.1 Caso Studio #1: Prompt Fallito

**❌ Prompt Inefficace:**

```
fai codice che prende file e fa cose
```

**Problemi:**
1. "fai codice" → linguaggio non specificato
2. "prende file" → legge? scrive? modifica?
3. "fa cose" → quali cose?!
4. Zero contesto

**Risultato:** Output inutile e vago.

---

**✅ Prompt Migliorato:**

```
Scrivi un programma C che legge un file CSV riga per riga
e calcola la media della seconda colonna (numeri interi).

File di esempio (input.csv):
```
nome,voto
Alice,85
Bob,92
Carol,78
```

Output atteso: "Media: 85"

Requisiti:
- Gestisci file non trovato
- Gestisci linee malformate
- Include makefile per compilare
```

**Risultato:** Codice completo e funzionante.

### 8.2 Caso Studio #2: Iterazione Efficace

**Iterazione 1:**
```
Scrivi funzione per cercare in array
```

**Output:** Codice generico.

**Iterazione 2:**
```
Migliora:
- Aggiungi binary search (assumo array ordinato)
- Ritorna indice (non bool)
- Gestisci array vuoto
```

**Output:** Codice migliorato ma manca gestione NULL.

**Iterazione 3:**
```
Perfetto! Ultima cosa: aggiungi test che verifichino:
- Array NULL
- Elemento non trovato
- Elemento primo/ultimo/medio
```

**Output:** Codice production-ready con test completi.

**Lezione:** L'iterazione è potente e normale.

### 8.3 Caso Studio #3: Few-Shot Magico

**Scenario:** Vuoi generare codice che segue standard aziendale specifico.

**Prompt:**

```
Nel nostro team usiamo questo pattern per logging:

Esempio 1:
LOG_INFO("Server started on port %d", port_number);

Esempio 2:
LOG_ERROR("Failed to allocate memory: %s", strerror(errno));

Esempio 3:
LOG_DEBUG("Processing request %d/%d", current, total);

Genera 5 chiamate di log appropriate per questa funzione:
[funzione che connette a database]
```

**Risultato:** Log consistente con lo stile del team!

---

## 🎯 RIEPILOGO LEZIONE 2

### Cosa Abbiamo Imparato

**Teoria:**
- ✅ Framework CLEAR (Context, Length, Examples, Action, Role)
- ✅ Tecniche avanzate: Zero-shot, Few-shot, Chain-of-Thought
- ✅ Validazione critica dell'output IA
- ✅ Red flags comuni e come riconoscerli
- ✅ Testing metodico a 4 livelli

**Pratica:**
- ✅ Evoluzione di prompt da basilare a ottimale
- ✅ Few-shot per insegnare stile personale
- ✅ Chain-of-Thought per debugging complesso
- ✅ Creazione di libreria personale di template
- ✅ Analisi casi studio reali

### Key Takeaways

**💡 Insight fondamentali:**

1. **Prompt Engineering è una skill**
   - Non basta "chiedere all'IA"
   - Prompt strutturati → output 10x migliori

2. **Framework CLEAR funziona**
   - Context, Length, Examples, Action, Role
   - Usa sempre quando serve qualità alta

3. **Few-shot è magia**
   - 2-3 esempi insegnano stile meglio di 1000 parole

4. **Chain-of-Thought per ragionamento**
   - "Ragiona passo per passo" migliora qualità drammaticamente

5. **Iterazione è normale**
   - Prompt V1 → Output mediocre
   - Raffina 2-3 volte → Output eccellente

6. **Validazione è CRITICA**
   - Compila sempre
   - Testa edge cases
   - Verifica con Valgrind

### Checklist Competenze Acquisite

**Verifica di aver padroneggiato:**

- [ ] Sai applicare framework CLEAR a un task
- [ ] Sai usare few-shot per insegnare il tuo stile
- [ ] Sai quando usare Chain-of-Thought
- [ ] Sai riconoscere red flags nel codice generato
- [ ] Hai creato almeno 2 template riutilizzabili
- [ ] Sai debuggare con IA usando rubber duck debugging
- [ ] Sai iterare e raffinare prompt

---

## 📚 COMPITI PER CASA

### Esercizio 1: Libreria di 10 Prompt

**Crea una raccolta personale di 10 prompt template per:**

1. Generazione funzione C
2. Debug memory leak
3. Ottimizzazione performance
4. Generazione test unitari
5. Documentazione Doxygen
6. Refactoring codice
7. Spiegazione algoritmo
8. Confronto approcci
9. Code review
10. [Tuo caso d'uso preferito]

Salva in formato Markdown.

### Esercizio 2: A/B Testing di Prompt

**Prendi 3 task e prova 2 approcci:**

**Task 1:** [es: implementa stack]
- Approccio A: Prompt semplice
- Approccio B: Prompt CLEAR

**Documenta:**
- Tempo impiegato
- Qualità output (1-10)
- Numero di iterazioni necessarie

**Obiettivo:** Quantificare benefici di prompt strutturati.

### Esercizio 3: Debug Challenge

**Trova e fixa 5 bug usando Chain-of-Thought:**

Cerca su Internet "common C bugs" o usa questi:
1. Off-by-one in loop
2. Memory leak
3. Buffer overflow
4. Use after free
5. Null pointer dereference

Per ognuno:
1. Trova codice buggy (o scrivi tu)
2. Usa CoT prompt per analizzare
3. Compara analisi IA con tua analisi
4. Documenta cosa hai imparato

---

## 🔗 RISORSE EXTRA

### Prompt Engineering Guides

- **Prompt Engineering Guide** - https://www.promptingguide.ai/
- **OpenAI Best Practices** - https://platform.openai.com/docs/guides/prompt-engineering
- **Anthropic Prompt Library** - https://docs.anthropic.com/claude/prompt-library

### Esempi di Prompt

- **Awesome ChatGPT Prompts** - https://github.com/f/awesome-chatgpt-prompts
- **Prompt Base** - Comunità di condivisione prompt

### Tool di Validazione

- **Cppcheck** - http://cppcheck.sourceforge.net/
- **Valgrind** - https://valgrind.org/
- **AddressSanitizer** - Documentazione GCC/Clang

---

## ❓ FAQ

**Q: Devo sempre usare il framework CLEAR?**
A: Per task complessi: sì. Per domande semplici: no. Usa giudizio.

**Q: Quanti esempi servono per few-shot?**
A: Di solito 2-3. Più di 5 raramente aiuta di più.

**Q: Chain-of-Thought rallenta l'IA?**
A: Sì, genera più token. Ma vale la pena per task complessi.

**Q: Posso combinare tecniche?**
A: Assolutamente! Few-shot + CoT + CLEAR = super potente.

**Q: Come salvo i miei prompt template?**
A: Usa file Markdown in cartella organizzata. Considera Git per versioning.

---

## 👨‍🏫 NOTE PER IL DOCENTE

### Timing Suggerito

**Teoria (60 min):**
- Intro + Anatomia prompt: 10 min
- Framework CLEAR: 15 min
- Tecniche avanzate: 20 min
- Validazione: 15 min

**Pratica (60 min):**
- Workshop prompt evolution: 20 min (hands-on importante!)
- Debug assistito: 15 min
- Libreria prompt: 15 min
- Casi studio: 10 min

### Punti Critici

1. **CLEAR framework**: Esercitalo dal vivo con classe
2. **Few-shot**: Dimostra con esempio reale quanto è potente
3. **Validazione**: Enfatizza che è SEMPRE necessaria

### Adattamenti

**Se hai più tempo (150 min):**
- Aggiungi competizione: chi scrive il prompt migliore?
- Live debugging session con codice portato dagli studenti

---

## 🎓 PROSSIMA LEZIONE

**LEZIONE 3: Programmazione C Sicura con IA**

**Anteprima:**
- Problemi ricorrenti del codice generato da IA
- Buffer overflow, memory leak, puntatori pericolosi
- Gestione memoria robusta
- Valgrind e strumenti professionali
- Progetto: sistema di gestione dati sicuro

**Preparazione:**
- Installa Valgrind (Linux/Mac) o Dr. Memory (Windows)
- Ripassa puntatori e memoria dinamica
- Porta domande da Lezione 2

---

**Fine Lezione 2**

---

**🚀 Ora sai scrivere prompt professionali che ottengono risultati eccellenti!**

**Ricorda:**
> "Un prompt ben fatto è la differenza tra codice mediocre e codice eccellente."

**Ottimo lavoro! Pratica i template e ci vediamo alla prossima lezione! 💻✨**