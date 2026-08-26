# 📘 MODULO 2
# Prompt Engineering e Programmazione Assistita
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 4 ore | Livello: Intermedio

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Cos'è la Programmazione Assistita](#2-cosè-la-programmazione-assistita)
3. [Teoria del Prompt Engineering](#3-teoria-del-prompt-engineering)
4. [Struttura del Prompt Perfetto](#4-struttura-del-prompt-perfetto)
5. [Applicazioni Pratiche](#5-applicazioni-pratiche)
6. [Metodologie Operative](#6-metodologie-operative)
7. [Analisi Critica del Codice Generato](#7-analisi-critica-del-codice-generato)
8. [Esempi Guidati Completi](#8-esempi-guidati-completi)
9. [Errori Comuni e Come Evitarli](#9-errori-comuni-e-come-evitarli)
10. [Esercizi Pratici](#10-esercizi-pratici)

---

## 1. Introduzione e Obiettivi

### 1.1 Benvenuti al Modulo 2

Dopo aver compreso i fondamenti dell'IA nel Modulo 1, è tempo di applicare queste conoscenze in modo pratico. Questo modulo vi insegnerà a **trasformare l'IA in uno strumento efficace** per lo sviluppo software.

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Formulare** prompt tecnici efficaci e completi
✅ **Valutare criticamente** la qualità del codice generato da IA
✅ **Integrare** l'IA nel flusso di sviluppo professionale
✅ **Riconoscere** errori, omissioni e limiti degli output IA
✅ **Applicare** metodologie iterative per migliorare i risultati
✅ **Documentare** e testare codice assistito da IA

### 1.3 Prerequisiti

- Completamento Modulo 1 (Fondamenti IA)
- Conoscenze base di programmazione
- Familiarità con un linguaggio (C, Python, o simili)
- Accesso a un LLM (ChatGPT, Claude, GitHub Copilot, ecc.)

---

## 2. Cos'è la Programmazione Assistita

### 2.1 Definizione

> **Programmazione Assistita**: metodologia di sviluppo in cui l'intelligenza artificiale affianca (ma non sostituisce) il programmatore nelle fasi di ideazione, scrittura, documentazione, test e refactoring del codice.

### 2.2 Il Ruolo dell'IA

```
┌─────────────────────────────────────────┐
│     IL PROGRAMMATORE RESTA AL CENTRO    │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────┐         ┌───────────┐   │
│  │           │         │           │   │
│  │   UMANO   │ ◄────► │    IA     │   │
│  │           │         │           │   │
│  │ Decisioni │         │ Supporto  │   │
│  │ Strategia │         │ Operativo │   │
│  │ Validazione│         │ Velocità  │   │
│  │           │         │           │   │
│  └───────────┘         └───────────┘   │
│                                         │
│  L'IA suggerisce, l'umano decide       │
└─────────────────────────────────────────┘
```

### 2.3 Benefici Misurabili

| Metrica | Miglioramento |
|---------|---------------|
| Velocità scrittura codice | +35-55% |
| Riduzione errori sintattici | +40% |
| Tempo documentazione | -60% |
| Produttività complessiva | +30% |

**Attenzione:** Questi benefici si ottengono SOLO con uso corretto!

### 2.4 Quando Usare la Programmazione Assistita

✅ **Usa IA per:**
- Funzioni utility standard
- Algoritmi ben noti (sort, search)
- Boilerplate code
- Conversioni di formato
- Test cases generazione
- Documentazione
- Spiegazione codice esistente

❌ **NON usare IA per:**
- Logica business critica complessa
- Algoritmi proprietari innovativi
- Codice safety-critical (medicale, avionico)
- Quando non puoi validare l'output

---

## 3. Teoria del Prompt Engineering

### 3.1 Cos'è un Prompt

> **Prompt**: L'istruzione in linguaggio naturale che fornisci all'IA per ottenere un output desiderato.

La **qualità del prompt** determina direttamente la **qualità dell'output**.

### 3.2 Anatomia di un Prompt

```
┌─────────────────────────────────────────┐
│         PROMPT EFFICACE                 │
├─────────────────────────────────────────┤
│                                         │
│  1. RUOLO (opzionale)                   │
│     "Sei un esperto programmatore C"    │
│                                         │
│  2. CONTESTO                            │
│     "Per un sistema embedded STM32"     │
│                                         │
│  3. COMPITO                             │
│     "Scrivi una funzione che..."        │
│                                         │
│  4. VINCOLI                             │
│     "Usa solo standard C99"             │
│     "Max 50 righe"                      │
│                                         │
│  5. FORMATO OUTPUT                      │
│     "Codice + commenti + esempio uso"   │
│                                         │
│  6. ESEMPI (opzionale)                  │
│     "Input: [1,2,3] → Output: 6"        │
│                                         │
└─────────────────────────────────────────┘
```

### 3.3 Principi Fondamentali

#### **Principio 1: Specificità**

❌ **Vago:**
```
"Scrivi una funzione di ordinamento"
```

✅ **Specifico:**
```
"Scrivi in C99 una funzione `void bubble_sort(int arr[], int n)`
che ordina in-place un array di interi in ordine crescente usando
l'algoritmo bubble sort"
```

#### **Principio 2: Contesto**

❌ **Senza contesto:**
```
"Ottimizza questa funzione"
```

✅ **Con contesto:**
```
"Ottimizza questa funzione per microcontrollore ARM Cortex-M4
a 168MHz con 192KB RAM, minimizzando uso memoria ma mantenendo
complessità O(n log n)"
```

#### **Principio 3: Iterazione**

```
Prompt 1 (base) → Output 1 → Analisi
    ↓
Prompt 2 (migliorato) → Output 2 → Analisi
    ↓
Prompt 3 (raffinato) → Output 3 → Validazione
```

Non aspettarti perfezione al primo tentativo!

### 3.4 Framework CLEAR

**C**ontext (Contesto)
**L**anguage/Library (Linguaggio/Librerie)
**E**xpectation (Aspettativa)
**A**ssumptions (Assunzioni)
**R**equirements (Requisiti)

#### **Esempio Applicato:**

```
[C] Sto sviluppando firmware per sensore IoT temperatura/umidità
[L] Usa C99 con SDK ESP32 (FreeRTOS)
[E] Voglio funzione che legge DHT22 e ritorna struct con valori
[A] DHT22 già configurato su GPIO4, timing già gestito da libreria
[R] Funzione deve:
    - Ritornare struct {float temp; float hum; bool valid;}
    - Gestire timeout lettura (max 2 secondi)
    - Validare checksum DHT22
    - Essere non-bloccante (non usare delay>10ms)
```

### 3.5 Template di Prompt Professionale

```markdown
# PROMPT TEMPLATE PER CODICE

## Contesto
[Sistema: embedded/desktop/web]
[Hardware: MCU/PC specs se rilevante]
[Obiettivo progetto]

## Task Tecnico
Scrivi in [LINGUAGGIO + STANDARD] una funzione/modulo che:
- [Funzionalità principale]
- [Funzionalità secondaria]

## Firma Funzione
[tipo_ritorno] nome_funzione([parametri])

## Vincoli
- [Vincolo 1: es. no librerie esterne]
- [Vincolo 2: es. complessità massima O(n)]
- [Vincolo 3: es. memoria massima]

## Input/Output
Input: [Descrizione + esempio]
Output: [Descrizione + esempio]
Errori: [Come gestirli]

## Requisiti Output
- Codice ben commentato
- [Gestione errori richiesta]
- [Test case inclusi / separati]
- [Documentazione funzione]

## Esempio Uso (opzionale)
```c
// Esempio di chiamata
int result = mia_funzione(input);
```
```

---

## 4. Struttura del Prompt Perfetto

### 4.1 Checklist del Prompt

Prima di inviare un prompt, verifica:

```
[ ] Ho specificato il linguaggio? (C, C99, C++, Python, ecc.)
[ ] Ho specificato lo standard? (C99, C11, Python 3.10)
[ ] Ho descritto chiaramente il task?
[ ] Ho elencato i vincoli?
[ ] Ho specificato cosa NON usare?
[ ] Ho indicato come gestire errori?
[ ] Ho richiesto esempi/test?
[ ] Ho specificato il formato output?
[ ] Ho fornito esempi se necessario?
[ ] Il prompt è <500 parole? (evita prolissità)
```

### 4.2 Livelli di Prompt

#### **Livello 1: Principiante (Insufficiente)**
```
"Scrivi codice per sommare array"
```
**Voto: 3/10**

#### **Livello 2: Intermedio (Accettabile)**
```
"Scrivi in C una funzione che somma gli elementi di un array di interi.
La funzione deve chiamarsi `somma_array` e prendere array e dimensione."
```
**Voto: 6/10**

#### **Livello 3: Avanzato (Buono)**
```
"Scrivi in standard C99 una funzione:

int somma_array(const int arr[], int n)

che:
- Somma tutti gli elementi dell'array
- Ritorna 0 se n <= 0
- Gestisce correttamente array vuoto
- Usa int per somma (overflow ignorato per semplicità)
- Nessuna libreria esterna necessaria

Includi 2 esempi di test."
```
**Voto: 9/10**

### 4.3 Pattern di Prompt Utili

#### **Pattern: "Explain Then Code"**
```
"Prima spiega l'algoritmo in pseudocodice o linguaggio naturale,
poi implementa in [linguaggio]"
```

#### **Pattern: "Test-Driven"**
```
"Genera prima 5 test cases (input/output attesi),
poi scrivi la funzione che li passa"
```

#### **Pattern: "Incremental"**
```
"Scrivi prima versione base senza gestione errori,
poi aggiungi gestione errori,
poi aggiungi validazione input,
poi ottimizza"
```

---

## 5. Applicazioni Pratiche

### 5.1 Generazione Codice

#### **Esempio: Funzione Utility**

**Prompt:**
```
Scrivi in C99 una funzione per invertire un array di interi in-place.

int arr[] = {1, 2, 3, 4, 5};
reverse_array(arr, 5);
// arr diventa {5, 4, 3, 2, 1}
```

**Output Atteso:**
```c
void reverse_array(int arr[], int n) {
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
}
```

### 5.2 Documentazione Automatica

**Prompt:**
```
"Genera documentazione stile Doxygen per questa funzione C: [codice]"
```

**Output:**
```c
/**
 * @brief Calcola il Massimo Comun Divisore (MCD) di due interi
 *
 * Implementazione dell'algoritmo di Euclide per calcolare il MCD.
 *
 * @param a Primo numero intero
 * @param b Secondo numero intero
 * @return Il MCD di a e b
 *
 * @note Complessità O(log(min(a,b)))
 *
 * @example
 * int risultato = gcd(48, 18); // risultato = 6
 */
```

### 5.3 Debugging Assistito

**Prompt:**
```
"Spiega questo errore e correggilo: [errore] [codice]"
```

**Output IA:**
```
PROBLEMA 1: arr dichiarato come int, non int[]
Correzione: int arr[] o int *arr

PROBLEMA 2: Loop condition i <= n causa accesso fuori range
Correzione: i < n

CODICE CORRETTO:
void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
}
```

### 5.4 Generazione Test

**Prompt:**
```
"Genera 5 test cases per la funzione:

int binary_search(int arr[], int n, int target)

che cerca target in array ordinato arr di dimensione n.
Ritorna indice se trovato, -1 altrimenti."
```

---

## 6. Metodologie Operative

### 6.1 Ciclo "Spec → Code → Test"

```
┌──────────────────────────────────────┐
│   METODOLOGIA RACCOMANDATA           │
├──────────────────────────────────────┤
│                                      │
│  FASE 1: SPECIFICA                   │
│  Scrivi prompt dettagliato           │
│  Definisci test cases aspettati      │
│         ↓                            │
│  FASE 2: GENERAZIONE                 │
│  IA genera codice                    │
│         ↓                            │
│  FASE 3: REVISIONE                   │
│  Leggi e comprendi codice            │
│  Identifica problemi potenziali      │
│         ↓                            │
│  FASE 4: TESTING                     │
│  Compila                             │
│  Esegui test                         │
│  Verifica edge cases                 │
│         ↓                            │
│  FASE 5: VALIDAZIONE                 │
│  ✅ OK → Integra nel progetto        │
│  ❌ Problemi → Torna a FASE 1/2      │
│                                      │
└──────────────────────────────────────┘
```

### 6.2 Iterazione Guidata

**Iterazione 1: Base**
```
Prompt: "Scrivi funzione per calcolare media array"
Output: Funzione base (ma forse senza gestione errori)
```

**Iterazione 2: Rafforzata**
```
Prompt: "Migliora gestendo n<=0 e possibile overflow"
Output: Funzione con controlli
```

**Iterazione 3: Ottimizzata**
```
Prompt: "Aggiungi versione per array molto grandi usando streaming"
Output: Implementazione ottimizzata
```

### 6.3 Validazione Multi-Livello

```
LIVELLO 1: Sintassi
[ ] Codice compila senza errori?
[ ] Nessun warning?

LIVELLO 2: Semantica
[ ] Logica corretta?
[ ] Edge cases gestiti?
[ ] No buffer overflow?

LIVELLO 3: Stile
[ ] Nomi variabili chiari?
[ ] Codice leggibile?
[ ] Commenti utili?

LIVELLO 4: Performance
[ ] Complessità accettabile?
[ ] Uso memoria ragionevole?
```

---

## 7. Analisi Critica del Codice Generato

### 7.1 Checklist di Analisi

#### **Controllo Immediato (2 minuti)**
```
[ ] Compila?
[ ] Firma funzione corretta?
[ ] Nomi variabili sensati?
[ ] Gestione base errori presente?
```

#### **Controllo Approfondito (10 minuti)**
```
[ ] Testato su casi normali?
[ ] Testato su edge cases?
[ ] Gestione memoria corretta?
[ ] No memory leak?
[ ] Comportamento su input invalidi?
```

### 7.2 Errori Tipici da Cercare

#### **Errore 1: Funzioni Non Standard**

```c
// IA potrebbe generare:
char *str = strdup(input); // ❌ strdup non è C standard!

// Soluzione corretta:
char *str = malloc(strlen(input) + 1);
if (str != NULL) {
    strcpy(str, input);
}
```

#### **Errore 2: Buffer Overflow**

```c
// IA potrebbe generare:
void copy_string(char *dest, char *src) {
    strcpy(dest, src); // ❌ Pericoloso! No size check
}

// Soluzione:
void copy_string(char *dest, char *src, size_t dest_size) {
    if (dest && src && dest_size > 0) {
        strncpy(dest, src, dest_size - 1);
        dest[dest_size - 1] = '\0';
    }
}
```

#### **Errore 3: Gestione Puntatori NULL**

```c
// IA potrebbe generare:
int sum(int *arr, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += arr[i]; // ❌ Crash se arr == NULL!
    }
    return s;
}

// Soluzione:
int sum(int *arr, int n) {
    if (arr == NULL || n <= 0) {
        return 0; // ✅ Gestione esplicita
    }
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += arr[i];
    }
    return s;
}
```

---

## 8. Esempi Guidati Completi

### 8.1 Esempio: Ricerca Binaria

**Prompt Professionale:**
```
"Scrivi in C99 una funzione di ricerca binaria:

int binary_search(const int arr[], int n, int target)

Requisiti:
- Array arr ordinato in ordine crescente
- Ritorna indice se trovato, -1 se non trovato
- Gestisce arr=NULL (ritorna -1)
- Gestisce n<=0 (ritorna -1)
- Implementazione iterativa (non ricorsiva)
- Complessità O(log n)
- Commenti che spiegano logica
- Includi 5 test cases"
```

**Output Validato:**
```c
/**
 * @brief Ricerca binaria in array ordinato
 *
 * @param arr Array ordinato crescente
 * @param n Dimensione array
 * @param target Valore da cercare
 * @return Indice se trovato, -1 altrimenti
 */
int binary_search(const int arr[], int n, int target) {
    if (arr == NULL || n <= 0) {
        return -1;
    }

    int left = 0;
    int right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}
```

---

## 9. Errori Comuni e Come Evitarli

### 9.1 Errore: Prompt Troppo Vago

❌ **Sbagliato:**
```
"Scrivi codice per ordinare"
```

✅ **Corretto:**
```
"Scrivi in C99 funzione `void selection_sort(int arr[], int n)`
che ordina in-place array di interi in ordine crescente usando
algoritmo selection sort. Gestisci n<=0 ritornando immediatamente."
```

### 9.2 Errore: Fidarsi Ciecamente

❌ **Comportamento Pericoloso:**
```
1. Chiedi codice a IA
2. Copia-incolla nel progetto
3. Compila
4. Deploy in produzione
```

✅ **Comportamento Corretto:**
```
1. Chiedi codice a IA
2. LEGGI e COMPRENDI il codice
3. TESTA su casi normali ed edge
4. VALIDA con tool (cppcheck, valgrind)
5. CODE REVIEW con collega
6. Integra gradualmente
```

### 9.3 Errore: Non Iterare

❌ **Singolo Tentativo:**
```
Prompt 1 → Output mediocre → "Vabbè, lo uso così"
```

✅ **Approccio Iterativo:**
```
Prompt 1 → Output base
   ↓
Analisi problemi
   ↓
Prompt 2 migliorato → Output migliore
   ↓
✅ Codice pronto
```

---

## 10. Esercizi Pratici

### Esercizio 1: Miglioramento Prompt

**Dato questo prompt mediocre:**
```
"Fai una funzione che trova il massimo"
```

**Compito:** Riscrivilo in versione professionale che includa:
- Linguaggio e standard
- Firma funzione
- Gestione errori
- Formato output
- Test richiesti

### Esercizio 2: Debugging Assistito

**Dato questo codice con bug:**
```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int sum = 0;

    for (int i = 0; i <= 5; i++) {
        sum += arr[i];
    }

    printf("Somma: %d\n", sum);
    return 0;
}
```

**Compiti:**
1. Identifica il bug
2. Scrivi un prompt per l'IA che chieda di spiegare e correggere
3. Valida la soluzione proposta

### Esercizio 3: Test Generation

**Data questa funzione:**
```c
// Verifica se una stringa è palindroma
bool is_palindrome(const char *str);
```

**Compito:** Scrivi un prompt che generi 8 test cases completi

---

## ✅ Checklist Completamento Modulo

- [ ] So formulare prompt tecnici completi
- [ ] Comprendo struttura CLEAR
- [ ] Conosco pattern di prompt utili
- [ ] So iterare su prompt per migliorare output
- [ ] So analizzare criticamente codice generato da IA
- [ ] Riconosco errori tipici (buffer overflow, NULL ptr, ecc.)
- [ ] Applico metodologia Spec → Code → Test
- [ ] Ho completato almeno 3 esercizi pratici
- [ ] Mi sento pronto per Modulo 3

---

**Fine Modulo 2**

*Prossimo: Modulo 3 - Programmazione C con IA*

---

**Versione:** 2.0 | **Aggiornamento:** Dicembre 2024 | **Corso ITS**
