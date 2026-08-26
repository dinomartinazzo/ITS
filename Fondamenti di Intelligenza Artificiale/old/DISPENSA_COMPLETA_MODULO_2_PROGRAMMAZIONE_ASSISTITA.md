# 📘 DISPENSA COMPLETA - MODULO 2
# Tecniche e Metodologie di Programmazione Assistita
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 2 ore | Livello: Intermedio

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
11. [Glossario Prompt Engineering](#11-glossario-prompt-engineering)

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

### 1.4 Strumenti Necessari

- Editor di testo / IDE
- Compilatore (gcc per C)
- Accesso a LLM
- Questa dispensa

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

### 2.3 Cosa FA la Programmazione Assistita

✅ **Accelera la scrittura di codice boilerplate**
```c
// Invece di scrivere manualmente:
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        matrix[i][j] = 0;
    }
}

// Chiedi: "funzione per azzerare matrice n×m"
```

✅ **Genera documentazione automaticamente**
```
Codice esistente → IA → README.md completo
```

✅ **Propone soluzioni alternative**
```
"Come posso ottimizzare questa ricerca?"
→ IA suggerisce: binary search, hash table, tree
```

✅ **Spiega codice complesso**
```
Regex incomprensibile → IA → Spiegazione chiara
```

✅ **Aiuta nel debugging**
```
Errore del compilatore → IA → Spiegazione + fix
```

### 2.4 Cosa NON FA la Programmazione Assistita

❌ **Non sostituisce la competenza tecnica**
```
IA può scrivere codice, ma serve esperto per validarlo
```

❌ **Non conosce il contesto specifico del progetto**
```
"Ottimizza per il mio hardware" → IA non sa quale hai
```

❌ **Non garantisce correttezza al 100%**
```
Codice può compilare ma avere bug logici
```

❌ **Non gestisce architettura complessa**
```
Microservizi con 50 componenti → Troppo per singolo prompt
```

### 2.5 Paradigma di Collaborazione

**Vecchio Paradigma:**
```
Programmatore → Scrive tutto manualmente → Codice
```

**Nuovo Paradigma:**
```
Programmatore → Descrive requisiti (prompt)
      ↓
      IA genera bozza
      ↓
Programmatore → Valida, corregge, ottimizza → Codice finale
```

**Analogia Utile:**
```
IA : Programmatore = Calcolatrice : Matematico

La calcolatrice accelera calcoli,
ma il matematico deve:
- Impostare il problema
- Interpretare risultati
- Validare sensatezza
```

### 2.6 Benefici Misurabili

Studi recenti mostrano:

| Metrica | Miglioramento |
|---------|---------------|
| Velocità scrittura codice | +35-55% |
| Riduzione errori sintattici | +40% |
| Tempo documentazione | -60% |
| Produttività complessiva | +30% |

**Attenzione:** Questi benefici si ottengono SOLO con uso corretto!

### 2.7 Quando Usare la Programmazione Assistita

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

#### **Principio 3: Vincoli Espliciti**

❌ **Senza vincoli:**
```
"Scrivi codice per leggere file CSV"
```

✅ **Con vincoli:**
```
"Scrivi in C99 standard codice per leggere file CSV che:
- Non usa librerie esterne
- Gestisce righe fino a 1024 char
- Ritorna NULL su errore
- Libera memoria allocata"
```

#### **Principio 4: Iterazione**

```
Prompt 1 (base) → Output 1 → Analisi
    ↓
Prompt 2 (migliorato) → Output 2 → Analisi
    ↓
Prompt 3 (raffinato) → Output 3 → Validazione
```

Non aspettarti perfezione al primo tentativo!

### 3.4 Framework CLEAR

Un metodo mnemonico per prompt efficaci:

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

### 3.5 Tipi di Prompt

#### **Prompt Zero-Shot**
```
"Scrivi funzione per invertire stringa in C"
```
Nessun esempio fornito, solo istruzione.

#### **Prompt One-Shot**
```
"Scrivi funzione per invertire stringa in C.

Esempio:
Input: "hello"
Output: "olleh"
```
Un esempio fornito.

#### **Prompt Few-Shot**
```
"Scrivi funzione per invertire stringa in C.

Esempi:
Input: "hello" → Output: "olleh"
Input: "a" → Output: "a"
Input: "" → Output: ""
```
Multipli esempi forniti. **Migliore per task complessi.**

#### **Prompt Chain-of-Thought**
```
"Scrivi funzione per invertire stringa in C.
Prima spiega l'algoritmo passo-passo, poi scrivi il codice."
```
Forza l'IA a "ragionare" esplicitamente.

### 3.6 Template di Prompt Professionale

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
**Problemi:**
- Linguaggio non specificato
- Tipo dati non chiaro
- Gestione errori assente
- Output formato sconosciuto

**Voto: 3/10**

---

#### **Livello 2: Intermedio (Accettabile)**
```
"Scrivi in C una funzione che somma gli elementi di un array di interi.
La funzione deve chiamarsi `somma_array` e prendere array e dimensione."
```
**Migliorato:**
- Linguaggio specificato
- Nome funzione chiaro
- Parametri identificati

**Ancora manca:**
- Standard C
- Gestione array vuoto
- Tipo di ritorno
- Overflow handling

**Voto: 6/10**

---

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
**Eccellente:**
- Standard specificato
- Firma funzione completa
- Edge cases gestiti
- Test richiesti

**Voto: 9/10**

---

#### **Livello 4: Professionale (Eccellente)**
```
"Progetta in standard C99 una funzione per sommare array di interi con gestione overflow.

FIRMA RICHIESTA:
typedef enum { SUM_OK, SUM_ERROR_NULL, SUM_ERROR_OVERFLOW } SumResult;
SumResult somma_array_safe(const int arr[], int n, long long *result);

SPECIFICHE:
- Usa long long per gestire overflow di int
- Parametri:
  - arr: array input (può essere NULL se n=0)
  - n: dimensione array (può essere 0, nega tivo = errore)
  - result: puntatore per output (non NULL)
- Ritorna:
  - SUM_OK: successo
  - SUM_ERROR_NULL: arr NULL con n>0, o result NULL
  - SUM_ERROR_OVERFLOW: somma non rappresentabile in long long
- Gestione edge cases:
  - n=0: result=0, ritorna SUM_OK
  - n<0: ritorna SUM_ERROR_NULL
  - arr=NULL con n>0: ritorna SUM_ERROR_NULL
  - Overflow: verifica prima di sommare

VINCOLI:
- Solo C99 standard, nessuna libreria esterna
- No VLA (Variable Length Arrays)
- Codice documentato con commenti
- Complessità O(n), spazio O(1)

OUTPUT RICHIESTO:
1. File header (.h) con dichiarazioni e documentazione
2. File implementation (.c)
3. 5 test cases che coprono:
   - Caso normale
   - Array vuoto (n=0)
   - Input NULL
   - Overflow positivo
   - Overflow negativo

ESEMPIO USO:
```c
int arr[] = {1, 2, 3, 4, 5};
long long sum;
SumResult res = somma_array_safe(arr, 5, &sum);
if (res == SUM_OK) {
    printf("Somma: %lld\n", sum);
}
```
```

**Questo è un prompt professionale!**

**Voto: 10/10**

### 4.3 Pattern di Prompt Utili

#### **Pattern: "Explain Then Code"**
```
"Prima spiega l'algoritmo in pseudocodice o linguaggio naturale,
poi implementa in [linguaggio]"
```
**Beneficio:** Forza l'IA a "ragionare", migliora qualità.

---

#### **Pattern: "Test-Driven"**
```
"Genera prima 5 test cases (input/output attesi),
poi scrivi la funzione che li passa"
```
**Beneficio:** Specifica comportamento, riduce ambiguità.

---

#### **Pattern: "Incremental"**
```
"Scrivi prima versione base senza gestione errori,
poi aggiungi gestione errori,
poi aggiungi validazione input,
poi ottimizza"
```
**Beneficio:** Costruzione graduale, più controllabile.

---

#### **Pattern: "Comparative"**
```
"Mostra 3 implementazioni diverse (ricorsiva, iterativa, pointer-based)
con pro/contro di ciascuna"
```
**Beneficio:** Educativo, permette scelta informata.

---

#### **Pattern: "Constraint-Heavy"**
```
"Scrivi rispettando:
- Max 30 righe
- Max nesting depth: 3
- No goto
- No magic numbers
- Nomi variabili descrittivi (min 4 caratteri)"
```
**Beneficio:** Forza buone pratiche, codice leggibile.

### 4.4 Cosa Evitare nei Prompt

❌ **Vaghezza**
```
"Fai qualcosa con questo array"
```

❌ **Contraddizioni**
```
"Scrivi in C++ ma usa solo C89 standard"
```

❌ **Richieste Impossibili**
```
"Scrivi codice che non usa memoria"
```

❌ **Troppe Richieste in Uno**
```
"Scrivi un intero sistema operativo con kernel,
driver, filesystem, shell, in un solo file"
```

❌ **Assunzioni Implicite**
```
"Ottimizza" (per cosa? velocità? memoria? leggibilità?)
```

❌ **Linguaggio Emotivo**
```
"Per favore ti prego scrivi questo codice perfetto" (inutile)
```

---

## 5. Applicazioni Pratiche

### 5.1 Generazione Codice

#### **Caso 1: Funzione Utility**

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

**Validazione:**
```c
// Test
int test[] = {1, 2, 3, 4, 5};
reverse_array(test, 5);
// Verifica: test == {5, 4, 3, 2, 1}
```

---

#### **Caso 2: Struttura Dati**

**Prompt:**
```
Crea in C99 una struttura per stack di interi con:
- Funzione push
- Funzione pop
- Funzione is_empty
- Capacità fissa (100 elementi)
- Gestione errori (stack pieno/vuoto)
```

**Output Validato Parziale:**
```c
#define STACK_SIZE 100

typedef struct {
    int data[STACK_SIZE];
    int top;
} Stack;

void stack_init(Stack *s) {
    s->top = -1;
}

bool stack_push(Stack *s, int value) {
    if (s->top >= STACK_SIZE - 1) {
        return false; // Stack full
    }
    s->data[++s->top] = value;
    return true;
}
// ... pop, is_empty ...
```

---

### 5.2 Documentazione Automatica

#### **Scenario:** Hai scritto codice, serve documentazione

**Codice Esistente:**
```c
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
```

**Prompt:**
```
"Genera documentazione stile Doxygen per questa funzione C: [codice sopra]"
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
 * @return Il MCD di a e b. Se b=0, ritorna |a|
 * 
 * @note Algoritmo iterativo, complessità O(log(min(a,b)))
 * 
 * @warning Non gestisce il caso a=b=0 (risultato indefinito)
 * 
 * @example
 * int risultato = gcd(48, 18); // risultato = 6
 */
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
```

---

### 5.3 Debugging Assistito

#### **Scenario:** Codice con errore del compilatore

**Codice Problematico:**
```c
void print_array(int arr, int n) {
    for (int i = 0; i <= n; i++) {
        printf("%d ", arr[i]);
    }
}
```

**Errore Compilatore:**
```
error: subscripted value is neither array nor pointer
```

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

---

### 5.4 Refactoring

#### **Codice Da Migliorare:**
```c
int f(int x) {
    int y = 0;
    for (int i = 0; i < x; i++) {
        y = y + i;
    }
    return y;
}
```

**Prompt:**
```
"Migliora leggibilità e aggiungi gestione errori: [codice]"
```

**Output:**
```c
/**
 * @brief Calcola la somma dei primi n numeri naturali (0 + 1 + ... + n-1)
 * @param n Il limite superiore (escluso)
 * @return La somma, oppure 0 se n <= 0
 */
int sum_first_n_numbers(int n) {
    if (n <= 0) {
        return 0; // Input invalido
    }
    
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += i;
    }
    
    return sum;
}

// ALTERNATIVA OTTIMIZZATA (O(1)):
int sum_first_n_numbers_optimized(int n) {
    if (n <= 0) {
        return 0;
    }
    // Formula: sum = n * (n-1) / 2
    return (n * (n - 1)) / 2;
}
```

---

### 5.5 Generazione Test

**Prompt:**
```
"Genera 5 test cases per la funzione:

int binary_search(int arr[], int n, int target)

che cerca target in array ordinato arr di dimensione n.
Ritorna indice se trovato, -1 altrimenti."
```

**Output:**
```c
// Test 1: Elemento presente al centro
int arr1[] = {1, 3, 5, 7, 9};
assert(binary_search(arr1, 5, 5) == 2);

// Test 2: Elemento presente all'inizio
int arr2[] = {10, 20, 30, 40};
assert(binary_search(arr2, 4, 10) == 0);

// Test 3: Elemento presente alla fine
int arr3[] = {2, 4, 6, 8, 10};
assert(binary_search(arr3, 5, 10) == 4);

// Test 4: Elemento non presente
int arr4[] = {1, 2, 3, 4, 5};
assert(binary_search(arr4, 5, 7) == -1);

// Test 5: Array vuoto
int arr5[] = {};
assert(binary_search(arr5, 0, 5) == -1);

// Test 6: Array singolo elemento (match)
int arr6[] = {42};
assert(binary_search(arr6, 1, 42) == 0);

// Test 7: Array singolo elemento (no match)
int arr7[] = {42};
assert(binary_search(arr7, 1, 10) == -1);
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

Non aspettarti perfezione al primo colpo!

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

### 6.3 Tecnica del "Rubber Duck" con IA

```
"Critica il tuo stesso codice. Identifica:
1. Possibili bug
2. Inefficienze
3. Problemi di sicurezza
4. Violazioni di best practices

Poi proponi fix."
```

Questo forza l'IA a fare review del proprio output!

### 6.4 Validazione Multi-Livello

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

LIVELLO 5: Portabilità
[ ] Funziona su target hardware?
[ ] Nessuna dipendenza non standard?
```

Valida TUTTI i livelli prima di usare codice in produzione!

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
[ ] Complessità dichiarata corretta?
```

#### **Controllo Produzione (30+ minuti)**
```
[ ] Code review con collega?
[ ] Test di integrazione?
[ ] Performance profiling?
[ ] Static analysis tools?
[ ] Fuzz testing?
[ ] Documentazione completa?
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
        dest[dest_size - 1] = '\0'; // Garantisci terminatore
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

#### **Errore 4: Off-by-One**

```c
// IA potrebbe generare:
for (int i = 0; i <= n; i++) { // ❌ Accede a arr[n]!
    sum += arr[i];
}

// Soluzione:
for (int i = 0; i < n; i++) { // ✅ Corretto
    sum += arr[i];
}
```

#### **Errore 5: Memory Leak**

```c
// IA potrebbe generare:
int* create_array(int n) {
    int *arr = malloc(n * sizeof(int));
    // ... init ...
    return arr;
}

void process() {
    int *arr = create_array(100);
    // ... usa arr ...
    // ❌ Manca free(arr)!
}

// Soluzione: Sempre liberare memoria allocata
void process() {
    int *arr = create_array(100);
    if (arr) {
        // ... usa arr ...
        free(arr); // ✅ Libera memoria
    }
}
```

### 7.3 Tool di Analisi Automatica

**Usa sempre tool automatici oltre a revisione manuale:**

```bash
# Static analysis
cppcheck mycode.c

# Memory checking
valgrind --leak-check=full ./myprogram

# Compiler warnings (massimo livello)
gcc -Wall -Wextra -Werror mycode.c
```

---

## 8. Esempi Guidati Completi

### 8.1 Esempio Completo: Contatore di Soglia

**Obiettivo:** Contare quanti elementi di un array superano una soglia.

#### **Step 1: Prompt Iniziale**
```
"Scrivi in C99 una funzione che conta quanti elementi di un array
di float superano una soglia data."
```

#### **Step 2: Output IA (Prima Iterazione)**
```c
int conta_sopra_soglia(float arr[], int n, float soglia) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > soglia) {
            count++;
        }
    }
    return count;
}
```

#### **Step 3: Analisi**
```
✅ Logica base corretta
❌ Non gestisce arr == NULL
❌ Non gestisce n <= 0
❌ Nessun commento
❌ Nessun test
```

#### **Step 4: Prompt Migliorato**
```
"Migliora la funzione precedente aggiungendo:
- Gestione arr NULL (ritorna -1)
- Gestione n <= 0 (ritorna 0)
- Commenti Doxygen
- 3 test cases"
```

#### **Step 5: Output Migliorato**
```c
/**
 * @brief Conta elementi di un array che superano una soglia
 * 
 * @param arr Array di float da analizzare
 * @param n Dimensione dell'array
 * @param soglia Valore di soglia per il confronto
 * @return Numero di elementi > soglia, -1 se errore input
 * 
 * @note Complessità: O(n) tempo, O(1) spazio
 */
int conta_sopra_soglia(const float arr[], int n, float soglia) {
    // Validazione input
    if (arr == NULL && n > 0) {
        return -1; // Errore: puntatore NULL con size positiva
    }
    
    if (n <= 0) {
        return 0; // Array vuoto, 0 elementi sopra soglia
    }
    
    // Conteggio
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > soglia) {
            count++;
        }
    }
    
    return count;
}

// --- Test Cases ---

void test_conta_sopra_soglia() {
    // Test 1: Caso normale
    float arr1[] = {1.5, 2.5, 3.5, 4.5};
    assert(conta_sopra_soglia(arr1, 4, 3.0) == 2); // 3.5 e 4.5
    
    // Test 2: Tutti sotto soglia
    float arr2[] = {1.0, 2.0, 3.0};
    assert(conta_sopra_soglia(arr2, 3, 10.0) == 0);
    
    // Test 3: Tutti sopra soglia
    float arr3[] = {5.0, 6.0, 7.0};
    assert(conta_sopra_soglia(arr3, 3, 1.0) == 3);
    
    // Test 4: Array vuoto
    assert(conta_sopra_soglia(NULL, 0, 5.0) == 0);
    
    // Test 5: Puntatore NULL con n>0 (errore)
    assert(conta_sopra_soglia(NULL, 5, 5.0) == -1);
    
    printf("Tutti i test passati!\n");
}
```

#### **Step 6: Validazione Finale**
```c
// Compila e testa
gcc -std=c99 -Wall -Wextra test.c -o test
./test
// Output: Tutti i test passati!

✅ CODICE APPROVATO PER USO PRODUZIONE
```

---

### 8.2 Esempio Completo: Ricerca Binaria

**Obiettivo:** Implementare ricerca binaria con gestione errori.

#### **Prompt Professionale**
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
- Includi 5 test cases

Fornisci anche una spiegazione dell'algoritmo."
```

#### **Output IA (Validato)**

```c
/**
 * @brief Ricerca binaria in array ordinato di interi
 * 
 * Cerca un valore target in un array ordinato usando l'algoritmo
 * di ricerca binaria. L'array DEVE essere ordinato in ordine crescente.
 * 
 * ALGORITMO:
 * 1. Inizia con left=0, right=n-1
 * 2. Calcola mid = left + (right-left)/2
 * 3. Se arr[mid] == target → trovato, ritorna mid
 * 4. Se arr[mid] < target → cerca in metà destra (left = mid+1)
 * 5. Se arr[mid] > target → cerca in metà sinistra (right = mid-1)
 * 6. Ripeti fino a trovare o left > right
 * 
 * @param arr Array ordinato di interi (ordine crescente)
 * @param n Dimensione dell'array
 * @param target Valore da cercare
 * @return Indice di target se trovato, -1 altrimenti o errore input
 * 
 * @pre arr deve essere ordinato in ordine crescente
 * @note Complessità: O(log n) tempo, O(1) spazio
 */
int binary_search(const int arr[], int n, int target) {
    // Validazione input
    if (arr == NULL || n <= 0) {
        return -1;
    }
    
    int left = 0;
    int right = n - 1;
    
    while (left <= right) {
        // Calcolo mid sicuro contro overflow
        // (left + right) / 2 potrebbe overflow con int grandi
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid; // Trovato!
        } else if (arr[mid] < target) {
            // Target è nella metà destra
            left = mid + 1;
        } else {
            // Target è nella metà sinistra
            right = mid - 1;
        }
    }
    
    // Non trovato
    return -1;
}

// --- Test Cases ---

#include <assert.h>
#include <stdio.h>

void test_binary_search() {
    printf("Running binary search tests...\n");
    
    // Test 1: Elemento al centro
    int arr1[] = {1, 3, 5, 7, 9, 11, 13};
    assert(binary_search(arr1, 7, 7) == 3);
    printf("✓ Test 1 passed: elemento al centro\n");
    
    // Test 2: Elemento all'inizio
    int arr2[] = {10, 20, 30, 40, 50};
    assert(binary_search(arr2, 5, 10) == 0);
    printf("✓ Test 2 passed: elemento all'inizio\n");
    
    // Test 3: Elemento alla fine
    int arr3[] = {2, 4, 6, 8, 10};
    assert(binary_search(arr3, 5, 10) == 4);
    printf("✓ Test 3 passed: elemento alla fine\n");
    
    // Test 4: Elemento non presente
    int arr4[] = {1, 2, 3, 4, 5};
    assert(binary_search(arr4, 5, 99) == -1);
    printf("✓ Test 4 passed: elemento non presente\n");
    
    // Test 5: Array vuoto
    assert(binary_search(NULL, 0, 5) == -1);
    printf("✓ Test 5 passed: array vuoto\n");
    
    // Test 6: Array con un solo elemento (match)
    int arr6[] = {42};
    assert(binary_search(arr6, 1, 42) == 0);
    printf("✓ Test 6 passed: singolo elemento (match)\n");
    
    // Test 7: Array con un solo elemento (no match)
    int arr7[] = {42};
    assert(binary_search(arr7, 1, 100) == -1);
    printf("✓ Test 7 passed: singolo elemento (no match)\n");
    
    printf("\n✅ Tutti i test passati!\n");
}

int main() {
    test_binary_search();
    return 0;
}
```

**Validazione:**
```bash
$ gcc -std=c99 -Wall -Wextra binary_search.c -o bs
$ ./bs
Running binary search tests...
✓ Test 1 passed: elemento al centro
✓ Test 2 passed: elemento all'inizio
✓ Test 3 passed: elemento alla fine
✓ Test 4 passed: elemento non presente
✓ Test 5 passed: array vuoto
✓ Test 6 passed: singolo elemento (match)
✓ Test 7 passed: singolo elemento (no match)

✅ Tutti i test passati!
```

---

## 9. Errori Comuni e Come Evitarli

### 9.1 Errore: Prompt Troppo Vago

❌ **Sbagliato:**
```
"Scrivi codice per ordinare"
```

**Problemi:**
- Linguaggio?
- Algoritmo?
- In-place o nuovo array?
- Ordine crescente/decrescente?

✅ **Corretto:**
```
"Scrivi in C99 funzione `void selection_sort(int arr[], int n)` 
che ordina in-place array di interi in ordine crescente usando
algoritmo selection sort. Gestisci n<=0 ritornando immediatamente."
```

---

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
7. Monitora in produzione
```

---

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
Test rivelano edge case
   ↓
Prompt 3 con edge case → Output robusto
   ↓
✅ Codice pronto
```

---

### 9.4 Errore: Ignor are Warning

❌ **Compilazione con Warning:**
```bash
$ gcc code.c -o program
warning: unused variable 'x'
warning: format '%d' expects argument of type 'int', but...

# "Vabbè, compila, va bene così"
```

✅ **Zero Tolerance per Warning:**
```bash
$ gcc -Wall -Wextra -Werror code.c -o program
# -Werror: Tratta warning come errori
# Se compila, è REALMENTE pulito
```

---

### 9.5 Errore: Non Testare Edge Cases

❌ **Test Superficiale:**
```c
// Test solo caso normale
int arr[] = {3, 1, 4, 1, 5};
sort(arr, 5);
// "Funziona!" → Spedito
```

✅ **Test Completo:**
```c
// Caso normale
test_normal();

// Edge cases
test_empty_array();
test_single_element();
test_already_sorted();
test_reverse_sorted();
test_all_equal();
test_negative_numbers();
test_large_array();
test_null_pointer();
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

<details>
<summary>Soluzione Esempio</summary>

```
"Scrivi in standard C99 una funzione:

int find_max(const int arr[], int n, int *max_value)

che trova il valore massimo in un array di interi.

COMPORTAMENTO:
- Se array valido e n>0: salva massimo in *max_value, ritorna 0 (successo)
- Se arr==NULL o max_value==NULL: ritorna -1 (errore input)
- Se n<=0: ritorna -1 (errore size)

VINCOLI:
- Solo C99 standard
- Complessità O(n)
- Commenti Doxygen

OUTPUT RICHIESTO:
- Header file (.h)
- Implementation (.c)
- 5 test cases inclusi

TEST DA COPRIRE:
1. Array normale positivi
2. Array con negativi
3. Array singolo elemento
4. Array vuoto (n=0)
5. Puntatore NULL
"
```

</details>

---

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

<details>
<summary>Soluzione</summary>

**Bug Identificato:**
```
i <= 5 causa accesso a arr[5] che è fuori range (array è [0..4])
```

**Prompt:**
```
"Analizza questo codice C e identifica eventuali bug.
Spiega il problema e fornisci versione corretta:

[codice]
"
```

**Correzione:**
```c
for (int i = 0; i < 5; i++) { // Cambiato <= in <
    sum += arr[i];
}
```

</details>

---

### Esercizio 3: Test Generation

**Data questa funzione:**
```c
// Verifica se una stringa è palindroma
bool is_palindrome(const char *str);
```

**Compito:** Scrivi un prompt che generi 8 test cases completi che coprano:
- Palindromi validi
- Non-palindromi
- Edge cases (stringa vuota, singolo carattere)
- Input NULL

<details>
<summary>Soluzione</summary>

**Prompt:**
```
"Genera 8 test cases completi in C per la funzione:

bool is_palindrome(const char *str)

che verifica se una stringa è palindroma (ignora case).

Test da includere:
1. Palindromo semplice lowercase
2. Palindromo con case misto
3. Non-palindromo
4. Stringa vuota ""
5. Singolo carattere
6. Palindromo lungo
7. Puntatore NULL
8. Stringa con spazi (decidere se ignorarli)

Ogni test deve avere:
- Input chiaro
- Output atteso
- Commento esplicativo
"
```

</details>

---

### Esercizio 4: Refactoring Challenge

**Codice Da Migliorare:**
```c
int f(int *a, int n) {
    int x = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) {
            x++;
        }
    }
    return x;
}
```

**Compito:** 
1. Scrivi prompt per migliorare nomi variabili e aggiungere documentazione
2. Aggiungi gestione errori
3. Aggiungi test

<details>
<summary>Soluzione</summary>

```c
/**
 * @brief Conta numeri pari in un array
 * 
 * @param arr Array di interi da analizzare
 * @param n Dimensione array
 * @return Numero di elementi pari, -1 se errore
 */
int count_even_numbers(const int arr[], int n) {
    // Validazione input
    if (arr == NULL && n > 0) {
        return -1;
    }
    
    if (n <= 0) {
        return 0;
    }
    
    // Conteggio
    int even_count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            even_count++;
        }
    }
    
    return even_count;
}

// Test cases
void test_count_even_numbers() {
    // Test 1: Mix pari/dispari
    int arr1[] = {1, 2, 3, 4, 5, 6};
    assert(count_even_numbers(arr1, 6) == 3); // 2, 4, 6
    
    // Test 2: Tutti pari
    int arr2[] = {2, 4, 6, 8};
    assert(count_even_numbers(arr2, 4) == 4);
    
    // Test 3: Tutti dispari
    int arr3[] = {1, 3, 5, 7};
    assert(count_even_numbers(arr3, 4) == 0);
    
    // Test 4: Array vuoto
    assert(count_even_numbers(NULL, 0) == 0);
    
    // Test 5: Puntatore NULL con n>0
    assert(count_even_numbers(NULL, 5) == -1);
}
```

</details>

---

### Progetto Finale: Sistema Completo

**Obiettivo:** Creare un sistema di gestione studenti con IA assistita.

**Requisiti:**
```
Sistema deve:
1. Struttura Student con: nome, matricola, voti (array)
2. Funzione add_student()
3. Funzione calculate_average()
4. Funzione find_top_student()
5. Gestione errori completa
6. Test suite completo
7. Documentazione
```

**Deliverable:**
- Codice C99 modulare (header + impl)
- Makefile
- README con istruzioni
- Test suite che passa
- Documentazione completa

**Usa IA per:** Generare scheletro, suggerire strutture dati, creare test  
**Fai Tu:** Validazione, integrazione, decisioni architetturali

---

## 11. Glossario Prompt Engineering

### Termini Chiave

**Boilerplate Code**
Codice ripetitivo e standardizzato (es. getter/setter, init functions).

**Chain-of-Thought**
Tecnica di prompt che chiede all'IA di "ragionare" esplicitamente.

**Context Window**
Quantità massima di testo che l'LLM può elaborare (input + output).

**Edge Case**
Caso limite o anomalo che potrebbe causare errori (es. array vuoto).

**Few-Shot Learning**
Fornire esempi nel prompt per guidare l'output.

**Hallucination**
Output plausibile ma inventato dall'IA (vedi Modulo 1).

**Iteration**
Processo di raffinamento successivo di prompt e output.

**One-Shot Learning**
Fornire un singolo esempio nel prompt.

**Prompt**
Istruzione fornita all'IA per generare output.

**Prompt Engineering**
Arte e scienza di formulare prompt efficaci.

**Refactoring**
Miglioramento strutturale del codice senza cambiarne comportamento.

**Temperature**
Parametro che controlla casualità/creatività dell'output IA.

**Token**
Unità base di testo elaborata dall'LLM.

**Zero-Shot Learning**
Nessun esempio fornito, solo istruzione diretta.

---

## 📚 Risorse Supplementari

### Documentazione Ufficiale
- **C Standard Library**: https://en.cppreference.com/
- **GCC Documentation**: https://gcc.gnu.org/onlinedocs/
- **Valgrind Manual**: https://valgrind.org/docs/manual/

### Tool Utili
- **Compiler Explorer**: https://godbolt.org/ (vedi assembly generato)
- **OnlineGDB**: https://www.onlinegdb.com/ (IDE online)
- **Replit**: https://replit.com/ (coding collaborativo)

### Best Practices
- **CERT C Coding Standard**: Linee guida sicurezza
- **Google C++ Style Guide**: (molti principi applicabili a C)
- **Linux Kernel Coding Style**: Style robusto e professionale

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
- [ ] Mi sento pronto per Modulo 3 (Programmazione C Assistita)

---

**Fine Modulo 2**

*Prossimo passo: Modulo 3 - Programmazione C Approfondita con IA*

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita

