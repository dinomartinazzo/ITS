# 📚 BIBLIOTECA PROMPT - RACCOLTA COMPLETA
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Versione:** 1.0
**Data:** Gennaio 2025
**Autore:** Materiale didattico ITS

---

## 📖 INTRODUZIONE

Questa biblioteca contiene **prompt template pronti all'uso** per tutte le situazioni di programmazione che affronterai durante il corso e nella tua carriera.

### Come Usare Questa Biblioteca

1. **Trova il template** che corrisponde al tuo task
2. **Sostituisci i placeholder** (scritti in MAIUSCOLO tra parentesi quadre)
3. **Customizza** secondo le tue esigenze specifiche
4. **Copia e incolla** nel tuo LLM preferito (ChatGPT, Claude, Gemini)
5. **Itera** se necessario, raffinando il prompt

### Convenzioni

**Placeholder:**
- `[PLACEHOLDER]` → sostituisci con il tuo contenuto
- `[OPZIONALE: descrizione]` → includi solo se necessario
- `// commento` → note esplicative, non copiare

**Simboli:**
- 🟢 **BASE** - Per principianti
- 🟡 **INTERMEDIO** - Richiede esperienza
- 🔴 **AVANZATO** - Per utenti esperti

---

## 📑 INDICE CATEGORIE

1. **[Generazione Codice C](#1-generazione-codice-c)**
   - Funzioni Base
   - Strutture Dati
   - Algoritmi
   - File I/O
   - Memory Management

2. **[Debugging](#2-debugging)**
   - Trova Bug
   - Memory Leak
   - Segmentation Fault
   - Logic Errors
   - Performance Issues

3. **[Documentazione](#3-documentazione)**
   - README.md
   - Commenti Doxygen
   - User Guide
   - API Documentation
   - Architecture Documents

4. **[Testing](#4-testing)**
   - Unit Tests
   - Integration Tests
   - Edge Cases
   - Test Automation

5. **[Ottimizzazione](#5-ottimizzazione)**
   - Performance
   - Memoria
   - Algoritmi
   - Code Size

6. **[Code Review e Refactoring](#6-code-review-e-refactoring)**
   - Security Review
   - Best Practices
   - Refactoring
   - Code Quality

7. **[Git e Workflow](#7-git-e-workflow)**
   - Commit Messages
   - Branching
   - Merge Conflicts
   - Pull Requests

8. **[Apprendimento](#8-apprendimento)**
   - Spiegazione Concetti
   - Tutorial Step-by-Step
   - Confronto Approcci
   - Problem Solving

9. **[Casi Speciali](#9-casi-speciali)**
   - Arduino/Embedded
   - Multi-threading
   - Networking
   - Parsing

10. **[Prompt Compositi](#10-prompt-compositi)**
    - Multi-step Tasks
    - Progetti Completi
    - Iterazioni

---

---

# 1. GENERAZIONE CODICE C

---

## 1.1 Template: Funzione Base 🟢

### Descrizione
Genera una singola funzione C con specifiche dettagliate.

### Template

```
Scrivi una funzione C con queste specifiche:

**CONTEXT**
Sono uno studente ITS che sta [DESCRIVERE CONTESTO DEL PROGETTO].

**FIRMA FUNZIONE**
[TIPO_RETURN] [NOME_FUNZIONE]([PARAMETRI])

**COMPORTAMENTO**
[DESCRIZIONE DETTAGLIATA DI COSA DEVE FARE]

**PARAMETRI**
- [PARAM_1]: [tipo] - [descrizione e vincoli]
- [PARAM_2]: [tipo] - [descrizione e vincoli]
[aggiungere altri parametri se necessario]

**VALORE DI RITORNO**
[Descrizione del return value e significato]
- [VALORE_1]: [significato]
- [VALORE_2]: [significato]

**EDGE CASES DA GESTIRE**
- [CASO_1]: [comportamento atteso]
- [CASO_2]: [comportamento atteso]
- NULL pointer: [comportamento]
- Input invalido: [comportamento]

**VINCOLI**
- Standard: C99
- Nessuna libreria esterna (solo stdlib)
- Memory-safe (nessun leak)
- Performance: O([COMPLESSITÀ])

**INCLUDI NEL OUTPUT**
- [x] Codice completo funzionante
- [x] Commenti Doxygen
- [x] Controllo errori completo
- [x] Esempio d'uso nel main()
- [x] Test con assert (almeno 3 casi)

**ESEMPI INPUT/OUTPUT**
Input: [esempio 1] → Output: [risultato 1]
Input: [esempio 2] → Output: [risultato 2]
Input: [esempio edge case] → Output: [gestione errore]
```

### Esempio Riempito

```
Scrivi una funzione C con queste specifiche:

**CONTEXT**
Sono uno studente ITS che sta creando una libreria di utility per stringhe.

**FIRMA FUNZIONE**
int count_words(const char *text)

**COMPORTAMENTO**
Conta il numero di parole in una stringa. Le parole sono separate da spazi,
tab, o newline. Parole multiple separate da più spazi contano come distinte
solo se separate da almeno uno spazio.

**PARAMETRI**
- text: const char* - Stringa da analizzare (può essere NULL)

**VALORE DI RITORNO**
Numero di parole nella stringa
- >= 0: numero valido di parole
- -1: errore (text è NULL)

**EDGE CASES DA GESTIRE**
- text == NULL: ritorna -1
- Stringa vuota "": ritorna 0
- Solo spazi "   ": ritorna 0
- Spazi multipli "hello  world": ritorna 2
- Leading/trailing spaces "  hello  ": ritorna 1

**VINCOLI**
- Standard: C99
- Nessuna libreria esterna (solo stdlib)
- Memory-safe (nessun leak)
- Performance: O(n) dove n è lunghezza stringa

**INCLUDI NEL OUTPUT**
- [x] Codice completo funzionante
- [x] Commenti Doxygen
- [x] Controllo errori completo
- [x] Esempio d'uso nel main()
- [x] Test con assert (almeno 5 casi)

**ESEMPI INPUT/OUTPUT**
Input: "Hello World" → Output: 2
Input: "  spaces  " → Output: 1
Input: "" → Output: 0
Input: NULL → Output: -1
Input: "one" → Output: 1
```

---

## 1.2 Template: Struttura Dati Completa 🟡

### Descrizione
Genera una struttura dati con tutte le operazioni CRUD.

### Template

```
Implementa una struttura dati completa in C per [TIPO_STRUTTURA].

**CONTEXT**
[DESCRIZIONE PROGETTO E OBIETTIVO]

**STRUTTURA DATI**
```c
typedef struct {
    [CAMPO_1] [nome_campo_1];
    [CAMPO_2] [nome_campo_2];
    // altri campi...
} [NOME_STRUCT];

typedef struct {
    [NOME_STRUCT] *items;
    size_t count;          // elementi correnti
    size_t capacity;       // capacità allocata
} [NOME_CONTAINER];
```

**OPERAZIONI RICHIESTE**
1. **Create**: Inizializza struttura vuota
   - Firma: `[NOME_CONTAINER]* [nome]_create(size_t initial_capacity)`
   - Ritorna: puntatore a nuova struttura o NULL se errore

2. **Add**: Aggiunge elemento
   - Firma: `int [nome]_add([NOME_CONTAINER] *container, [NOME_STRUCT] item)`
   - Ritorna: 0 successo, -1 errore
   - Auto-resize se necessario

3. **Get**: Recupera elemento per indice
   - Firma: `[NOME_STRUCT]* [nome]_get([NOME_CONTAINER] *container, size_t index)`
   - Ritorna: puntatore a elemento o NULL se errore

4. **Remove**: Rimuove elemento
   - Firma: `int [nome]_remove([NOME_CONTAINER] *container, size_t index)`
   - Ritorna: 0 successo, -1 errore

5. **Find**: Cerca elemento
   - Firma: `int [nome]_find([NOME_CONTAINER] *container, [CRITERIO])`
   - Ritorna: indice elemento o -1 se non trovato

6. **Free**: Libera tutta la memoria
   - Firma: `void [nome]_free([NOME_CONTAINER] *container)`

**REQUISITI**
- Dynamic array che si espande automaticamente (raddoppia capacità)
- Controllo NULL su tutti i parametri
- Controllo malloc/realloc failures
- Memory-safe (Valgrind clean)
- Commenti Doxygen su tutte le funzioni pubbliche

**INCLUDI**
- File header (.h) con dichiarazioni
- File implementation (.c) con definizioni
- Esempio d'uso completo con tutte le operazioni
- Unit test per ogni operazione
```

### Esempio Riempito

```
Implementa una struttura dati completa in C per gestione studenti.

**CONTEXT**
Sto creando un sistema di gestione per una scuola. Ho bisogno di
memorizzare studenti con nome, matricola ed email, e poter aggiungere,
cercare e rimuovere studenti dinamicamente.

**STRUTTURA DATI**
```c
typedef struct {
    int id;
    char name[100];
    char email[100];
    int enrollment_year;
} Student;

typedef struct {
    Student *items;
    size_t count;
    size_t capacity;
} StudentDB;
```

**OPERAZIONI RICHIESTE**
1. **Create**: Inizializza database vuoto
   - Firma: `StudentDB* student_db_create(size_t initial_capacity)`
   - Ritorna: puntatore a nuovo DB o NULL se errore

2. **Add**: Aggiunge studente
   - Firma: `int student_db_add(StudentDB *db, Student student)`
   - Ritorna: 0 successo, -1 errore
   - Auto-resize se necessario (raddoppia capacità)

3. **Get**: Recupera studente per indice
   - Firma: `Student* student_db_get(StudentDB *db, size_t index)`
   - Ritorna: puntatore a studente o NULL

4. **Remove**: Rimuove studente per indice
   - Firma: `int student_db_remove(StudentDB *db, size_t index)`
   - Ritorna: 0 successo, -1 errore
   - Compatta array (shift elementi successivi)

5. **Find**: Cerca studente per ID
   - Firma: `int student_db_find_by_id(StudentDB *db, int id)`
   - Ritorna: indice studente o -1

6. **Free**: Libera memoria
   - Firma: `void student_db_free(StudentDB *db)`

**REQUISITI**
- Dynamic array iniziale 10 elementi, raddoppia quando pieno
- Controllo NULL su tutti i parametri
- Controllo malloc/realloc failures
- Memory-safe (Valgrind clean)
- Commenti Doxygen su tutte le funzioni

**INCLUDI**
- student_db.h con dichiarazioni
- student_db.c con implementazioni
- main.c con esempio d'uso completo
- Test almeno 3 studenti, test find, test remove, test resize
```

---

## 1.3 Template: Algoritmo con Requisiti Performance 🟡

### Descrizione
Implementa algoritmo con vincoli di performance specifici.

### Template

```
Implementa l'algoritmo [NOME_ALGORITMO] in C.

**CONTEXT**
[DESCRIZIONE PROBLEMA DA RISOLVERE]

**REQUISITI ALGORITMO**
- Input: [descrizione input]
- Output: [descrizione output]
- Complessità temporale richiesta: O([COMPLESSITÀ])
- Complessità spaziale richiesta: O([COMPLESSITÀ])
- Caso migliore: O([COMPLESSITÀ])
- Caso peggiore: O([COMPLESSITÀ])

**VINCOLI**
- Dimensione input: fino a [N] elementi
- Tipo dati: [tipo]
- Memoria disponibile: [limite se applicabile]
- Deve essere [stable/in-place/iterativo/ricorsivo]

**SPECIFICHE IMPLEMENTAZIONE**
```c
// Firma funzione
[TIPO_RETURN] [nome_funzione]([PARAMETRI]);

// Eventuali funzioni ausiliarie
[se necessario, elenca]
```

**EDGE CASES**
- Input vuoto: [comportamento]
- Input singolo elemento: [comportamento]
- Input già ordinato/processato: [comportamento]
- Input worst-case: [comportamento]

**OUTPUT RICHIESTO**
- [x] Implementazione completa
- [x] Spiegazione algoritmo (commenti)
- [x] Analisi complessità (nel commento header)
- [x] Test con vari input size
- [x] Confronto con algoritmo alternativo [se applicabile]
```

### Esempio Riempito

```
Implementa l'algoritmo QuickSort in C.

**CONTEXT**
Ho bisogno di ordinare array di interi in modo efficiente per un progetto
di analisi dati. L'array può contenere fino a 100,000 elementi.

**REQUISITI ALGORITMO**
- Input: array di int, dimensione array
- Output: array ordinato in-place
- Complessità temporale richiesta: O(n log n) caso medio
- Complessità spaziale richiesta: O(log n) per stack ricorsione
- Caso migliore: O(n log n)
- Caso peggiore: O(n²) ma mitigato con pivot mediano

**VINCOLI**
- Dimensione input: fino a 100,000 elementi
- Tipo dati: int
- Deve essere in-place (no array ausiliario grande)
- Preferibilmente iterativo o ricorsivo ottimizzato

**SPECIFICHE IMPLEMENTAZIONE**
```c
// Firma funzione principale
void quicksort(int *arr, int size);

// Funzioni ausiliarie
static int partition(int *arr, int low, int high);
static void swap(int *a, int *b);
```

**EDGE CASES**
- Input vuoto (size=0): nessuna operazione
- Input singolo elemento: già ordinato
- Input già ordinato: O(n log n) con pivot mediano
- Input tutti elementi uguali: gestire senza stack overflow

**OUTPUT RICHIESTO**
- [x] Implementazione completa quicksort
- [x] Spiegazione algoritmo passo-passo nei commenti
- [x] Analisi complessità Big-O nel header
- [x] Test con array [10, 100, 1000, 10000] elementi
- [x] Confronto tempo esecuzione vs bubble sort
```

---

## 1.4 Template: File I/O con Parsing 🟡

### Descrizione
Lettura/scrittura file con parsing di formati specifici.

### Template

```
Implementa modulo per lettura/scrittura file [FORMATO].

**CONTEXT**
[DESCRIZIONE PROGETTO]

**FORMATO FILE**
```
[ESEMPIO FORMATO FILE CON ANNOTAZIONI]
```

**FUNZIONI RICHIESTE**

1. **Read/Parse**
```c
int [nome]_read(const char *filename, [STRUCT] **output, size_t *count);
```
- Legge file e parsa contenuto
- Alloca dinamicamente struttura output
- Ritorna: 0 successo, codice errore altrimenti

2. **Write/Serialize**
```c
int [nome]_write(const char *filename, [STRUCT] *data, size_t count);
```
- Scrive struttura su file nel formato specificato
- Ritorna: 0 successo, codice errore altrimenti

3. **Validate**
```c
int [nome]_validate(const char *filename);
```
- Valida formato file senza caricare tutto
- Ritorna: 0 valido, -1 invalido

**GESTIONE ERRORI**
- File non trovato → errno, messaggio stderr
- Formato invalido → skip riga + warning, continua
- Malloc failure → cleanup parziale, ritorna errore
- Permessi insufficienti → errno, messaggio chiaro

**REQUISITI**
- Parsing robusto (gestisce spazi extra, linee vuote)
- Supporto commenti [se applicabile]
- Validazione campi (range, formato)
- Memory-safe (chiude file sempre, free su errore)
- Buffer overflow protection

**INCLUDI**
- Header file con API
- Implementation file
- Esempio file di test (valido e invalido)
- Main di esempio che legge, processa, scrive
```

### Esempio Riempito

```
Implementa modulo per lettura/scrittura file CSV studenti.

**CONTEXT**
Sistema gestione studenti che salva dati su CSV. Devo poter
leggere file esistenti, aggiungere studenti, e salvare.

**FORMATO FILE**
```
# Studenti Database - Formato: id,nome,email,anno
# Righe che iniziano con # sono commenti
1,Mario Rossi,mario@example.com,2023
2,Laura Bianchi,laura@example.com,2024
# formato: int,string(max 100),string(max 100),int
```

**FUNZIONI RICHIESTE**

1. **Read/Parse**
```c
int students_csv_read(const char *filename, Student **output, size_t *count);
```
- Legge file CSV e parsa righe
- Alloca array dinamico di Student
- Ritorna: 0 successo, -1 file not found, -2 parse error

2. **Write/Serialize**
```c
int students_csv_write(const char *filename, Student *data, size_t count);
```
- Scrive array di studenti su CSV
- Include header con commento formato
- Ritorna: 0 successo, -1 errore

3. **Validate**
```c
int students_csv_validate(const char *filename);
```
- Valida formato senza caricare
- Controlla: 4 campi per riga, tipi corretti
- Ritorna: 0 valido, -1 invalido

**GESTIONE ERRORI**
- File non trovato → fprintf(stderr, "Error: file not found") + return -1
- Riga malformata → skip + warning "Line X skipped (invalid format)"
- Malloc failure → free parziale + return -2
- Email troppo lunga → tronca + warning

**REQUISITI**
- Parsing robusto (trim spazi, gestisce ",")
- Supporta commenti # e righe vuote
- Validazione: id > 0, anno tra 2000-2100, email con @
- Chiude sempre file (anche su errore)
- Protetto da buffer overflow (usa strncpy, snprintf)

**INCLUDI**
- students_csv.h con API
- students_csv.c con implementazioni
- test_valid.csv e test_invalid.csv
- main.c: read → stampa → modifica → write
```

---

## 1.5 Template: Memory Management Complesso 🔴

### Descrizione
Gestione memoria avanzata con allocazioni multiple e ownership.

### Template

```
Implementa gestione memoria per [DESCRIZIONE STRUTTURA COMPLESSA].

**CONTEXT**
[SCENARIO COMPLESSO]

**ARCHITETTURA MEMORIA**
```
[DIAGRAMMA ASCII DELLA STRUTTURA MEMORIA]
Parent
  ├─> Child1 (owned)
  ├─> Child2 (owned)
  └─> Shared (reference)
```

**OWNERSHIP MODEL**
- [STRUCT_A] owns [STRUCT_B]: deve fare free
- [STRUCT_C] references [STRUCT_D]: NON deve fare free
- [RISORSA] ha lifetime [DESCRIZIONE]

**FUNZIONI RICHIESTE**

1. **Allocazione Completa**
```c
[MAIN_STRUCT]* [nome]_create([PARAMS]);
```
- Alloca struttura principale + tutte le sottostrutture owned
- Inizializza references a NULL
- Ritorna: puntatore o NULL

2. **Deep Copy**
```c
[MAIN_STRUCT]* [nome]_clone(const [MAIN_STRUCT] *source);
```
- Copia profonda (duplica owned, copia references)
- Ritorna: nuova struttura indipendente

3. **Free Completo**
```c
void [nome]_free([MAIN_STRUCT] *obj);
```
- Libera SOLO owned resources
- Non tocca references
- NULL-safe (accetta NULL)
- Setta puntatore a NULL alla fine

4. **Transfer Ownership**
```c
void [nome]_transfer_[RESOURCE]([MAIN_STRUCT] *from, [MAIN_STRUCT] *to);
```
- Trasferisce ownership di risorsa
- from perde ownership, to acquista

**VALIDAZIONE VALGRIND**
Il codice DEVE passare:
```bash
valgrind --leak-check=full --show-leak-kinds=all ./program
# Output atteso: "All heap blocks were freed -- no leaks are possible"
```

**EDGE CASES**
- Allocazione parziale fallisce → cleanup parziale + return NULL
- Free su struttura parzialmente inizializzata → safe
- Double free protection → NULL check
- Free su reference → non deve crashare

**INCLUDI**
- Implementazione completa
- Test che crea/clona/free 100 istanze
- Valgrind output showing 0 leaks
- Diagramma ownership commentato nel codice
```

---

---

# 2. DEBUGGING

---

## 2.1 Template: Trova Bug Generico 🟢

### Descrizione
Analisi sistematica di codice con bug.

### Template

```
Ho un bug in questo codice. Aiutami a trovarlo usando Chain-of-Thought.

**SINTOMI**
[DESCRIZIONE COMPORTAMENTO OSSERVATO]
- Input: [esempio]
- Output atteso: [cosa dovrebbe succedere]
- Output effettivo: [cosa succede invece]
- Messaggio errore: [se presente]

**CODICE**
```c
[INCOLLA CODICE COMPLETO]
```

**ANALISI RICHIESTA**
Usa Chain-of-Thought, rispondi step-by-step:

1. **Cosa dovrebbe fare il codice?**
   - Analizza l'obiettivo generale

2. **Traccia esecuzione con input di esempio**
   - Simula esecuzione riga per riga
   - Traccia valori variabili chiave

3. **Identifica discrepanza**
   - Dove l'esecuzione effettiva diverge da quella attesa?

4. **Analizza causa root**
   - Perché succede questa discrepanza?
   - È bug logico, off-by-one, tipo sbagliato, altro?

5. **Verifica edge cases**
   - Il bug si manifesta solo con certi input?
   - Testa mentalmente: NULL, empty, boundary values

6. **Proponi fix**
   - Codice corretto
   - Spiegazione fix
   - Test che verifica fix funziona

**FORMATO OUTPUT**
```
🐛 BUG IDENTIFICATO: [descrizione 1 riga]

📍 LOCATION: [file:linea o descrizione precisa]

🔍 ANALISI:
[spiegazione dettagliata causa]

✅ FIX:
```c
[codice corretto]
```

🧪 TEST:
[test case che verifica fix]
```
```

### Esempio d'Uso

```
Ho un bug in questo codice. Aiutami a trovarlo usando Chain-of-Thought.

**SINTOMI**
Funzione che dovrebbe calcolare media array, ma ritorna sempre 0.
- Input: arr={10, 20, 30}, size=3
- Output atteso: 20
- Output effettivo: 0
- Messaggio errore: nessuno

**CODICE**
```c
int average(int *arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    int avg = sum / size;
    return avg;
}

int main() {
    int numbers[] = {10, 20, 30};
    printf("Average: %d\n", average(numbers, 3));
}
```

**ANALISI RICHIESTA**
[segui i 6 step sopra]
```

---

## 2.2 Template: Memory Leak Debug 🟡

### Descrizione
Debugging sistematico di memory leak con Valgrind.

### Template

```
Ho un memory leak. Aiutami a trovarlo e fixarlo.

**VALGRIND OUTPUT**
```
[INCOLLA OUTPUT COMPLETO DI VALGRIND]
```

**CODICE SOSPETTO**
```c
[INCOLLA FUNZIONI COINVOLTE]
```

**ANALISI RICHIESTA**

1. **Interpreta Valgrind output**
   - Quanti byte persi?
   - Dove allocati (file:linea)?
   - "Definitely lost" vs "still reachable"?

2. **Identifica tutti i malloc/calloc/realloc**
   - Elenca ogni allocazione nel codice
   - Per ognuna, c'è corrispondente free?

3. **Verifica percorsi di errore**
   - Se funzione fa return early, fa free prima?
   - In caso di errore, cleanup parziale corretto?

4. **Ownership analysis**
   - Chi è responsabile di free per ogni allocazione?
   - Trasferimenti di ownership corretti?

5. **Fix dettagliato**
   - Codice corretto con free mancanti
   - Eventuali goto cleanup pattern se necessario

6. **Valgrind verification**
   - Comando per verificare fix
   - Output atteso (0 leaks)

**OUTPUT FORMAT**
```
🔴 LEAK SUMMARY:
- Bytes lost: [numero]
- Allocations: [numero]
- Locations: [lista]

🔍 ROOT CAUSES:
1. [causa 1]
2. [causa 2]

✅ FIX:
```c
[codice corretto]
```

✓ VERIFICATION:
```bash
valgrind --leak-check=full ./program_fixed
# Expected: 0 bytes leaked
```
```
```

---

## 2.3 Template: Segmentation Fault Debug 🟡

### Descrizione
Debug crash con segfault usando GDB e analisi.

### Template

```
Il mio programma crasha con segmentation fault. Aiutami a debuggare.

**GDB BACKTRACE**
```
[INCOLLA OUTPUT DI gdb backtrace]
```

**SINTOMI**
- Crash consistente: [sì/no]
- Crash solo con certi input: [quali]
- Core dump disponibile: [sì/no]

**CODICE**
```c
[FUNZIONE CHE CRASHA + CHIAMANTI]
```

**ANALISI RICHIESTA**

1. **Interpreta backtrace**
   - Quale funzione crasha esattamente?
   - Stack trace: sequenza chiamate che porta al crash

2. **Identifica NULL dereference**
   - Quali puntatori sono dereferenziati?
   - Quali potrebbero essere NULL?

3. **Buffer overflow check**
   - Ci sono accessi array arr[i]?
   - Bounds corretti (i < size, non i <= size)?

4. **Use-after-free check**
   - Puntatori usati dopo free?
   - Puntatori non inizializzati (garbage value)?

5. **Stack corruption check**
   - Buffer overflow su array locali?
   - Ritorno puntatore a variabile locale?

6. **Fix + defensive programming**
   - Codice corretto
   - Aggiungi assert/check per prevenire

**DEBUG COMMANDS**
Fornisci comandi GDB per isolare:
```bash
gdb ./program
(gdb) run
(gdb) backtrace
(gdb) frame [N]
(gdb) print [VARIABLE]
(gdb) info locals
```
```

---

## 2.4 Template: Logic Error (Bug Sottile) 🟢

### Descrizione
Bug che non crasha ma produce risultati sbagliati.

### Template

```
Il codice compila e gira senza crashare, ma il risultato è sbagliato.

**SCENARIO**
[DESCRIZIONE DETTAGLIATA PROBLEMA]

**TEST CASES**
| Input | Output Atteso | Output Effettivo | Differenza |
|-------|---------------|------------------|------------|
| [1]   | [att_1]       | [eff_1]          | [diff_1]   |
| [2]   | [att_2]       | [eff_2]          | [diff_2]   |

**CODICE**
```c
[CODICE COMPLETO]
```

**DEBUGGING APPROACH**

Usa tecnica "Rubber Duck Debugging":

1. **Spiega a voce alta (o per iscritto) cosa il codice DOVREBBE fare**
   - Linea per linea, in pseudocodice

2. **Confronta con cosa il codice EFFETTIVAMENTE fa**
   - Leggi codice reale
   - Dove diverge dall'intenzione?

3. **Aggiungi print debug strategici**
   - Suggerisci dove inserire printf
   - Quali variabili ispezionare

4. **Ipotizza cause possibili**
   - Almeno 3 ipotesi
   - Per ognuna: test per confermare/escludere

5. **Fix**
   - Codice corretto
   - Spiegazione perché ora funziona
```

---

## 2.5 Template: Performance Bottleneck 🔴

### Descrizione
Identifica e risolvi problemi di performance.

### Template

```
Il codice funziona ma è troppo lento. Aiutami ad ottimizzare.

**PERFORMANCE ISSUE**
- Input size: [dimensione]
- Tempo attuale: [secondi/ms]
- Tempo target: [obiettivo]
- Risorsa limitante: [CPU / Memoria / I/O]

**PROFILING DATA** (se disponibile)
```
[OUTPUT gprof o perf o time]
```

**CODICE**
```c
[FUNZIONE/I LENTE]
```

**ANALISI RICHIESTA**

1. **Complessità attuale**
   - Analisi Big-O tempo e spazio
   - Caso peggiore identificato

2. **Hotspot identification**
   - Quale riga/funzione consuma più tempo?
   - Loop annidati? Chiamate ridondanti?

3. **Algoritmo alternatives**
   - Esiste algoritmo con complessità migliore?
   - Trade-off tempo vs spazio

4. **Micro-optimizations**
   - Riduci allocazioni
   - Cache locality
   - Evita copia inutili

5. **Fix proposto**
   - Codice ottimizzato
   - Spiegazione miglioramenti
   - Stima nuovo Big-O
   - Benchmark comparativo

**PROFILING COMMANDS**
```bash
# Compila con profiling
gcc -pg program.c -o program

# Run + genera gprof data
./program
gprof program gmon.out

# Oppure con perf (Linux)
perf record ./program
perf report
```
```

---

---

# 3. DOCUMENTAZIONE

---

## 3.1 Template: README.md Completo 🟢

### Descrizione
Genera README professionale per progetto GitHub.

### Template

```
Genera un README.md professionale per questo progetto:

**INFORMAZIONI PROGETTO**
- Nome: [NOME_PROGETTO]
- Tagline: [breve descrizione 1 frase]
- Linguaggio: [C / Python / etc]
- Target utente: [chi userà questo]
- Repository: https://github.com/[USER]/[REPO]

**FEATURES PRINCIPALI**
- [Feature 1]: [descrizione breve]
- [Feature 2]: [descrizione breve]
- [Feature 3]: [descrizione breve]

**TECNOLOGIE/DIPENDENZE**
- [Tool 1]: [versione]
- [Library 1]: [versione]

**INSTALLAZIONE**
[Descrivere step per compilare/installare]

**USO BASE**
[Descrivere comandi principali con esempi]

**SEZIONI DA INCLUDERE**
- [ ] Header con title + badges (build status, license, versione)
- [ ] Overview (2-3 paragrafi con problema risolto)
- [ ] Features list (con emoji)
- [ ] Installation (step-by-step)
- [ ] Quick Start (esempio minimo funzionante)
- [ ] Usage (esempi dettagliati con output)
- [ ] Documentation (link a doc dettagliata se esiste)
- [ ] Project Structure (tree files principali)
- [ ] Testing (come eseguire test)
- [ ] Contributing (guidelines se open source)
- [ ] License
- [ ] Authors/Credits
- [ ] Changelog (opzionale)

**STILE**
- Usa emoji appropriati (non esagerare)
- Includi code blocks con syntax highlighting
- Aggiungi screenshot ASCII o link a immagini (se applicabile)
- Tono: professionale ma friendly
- Massimo 500 righe (README conciso)

**BADGES** (genera codice per)
- Build status (se applicabile)
- License badge
- Version badge
```

### Esempio Riempito

```
Genera un README.md professionale per questo progetto:

**INFORMAZIONI PROGETTO**
- Nome: TaskMaster CLI
- Tagline: Gestisci le tue TODO list direttamente dal terminale
- Linguaggio: C99
- Target utente: Sviluppatori e power user che vivono in terminale
- Repository: https://github.com/mariorossi/taskmaster

**FEATURES PRINCIPALI**
- CRUD completo: Create, Read, Update, Delete tasks
- Priorità: Gestione task con 3 livelli di priorità
- Filtering: Filtra per status, priorità, categoria
- Persistenza: Salvataggio automatico su CSV
- Stats: Statistiche produttività (completati/giorno)

**TECNOLOGIE/DIPENDENZE**
- GCC: 9.0+
- Make: build system
- Valgrind: memory testing (dev only)

**INSTALLAZIONE**
```bash
git clone https://github.com/mariorossi/taskmaster.git
cd taskmaster
make
```

**USO BASE**
```bash
# Aggiungi task
./taskmaster add "Studiare per esame" --priority high

# Lista tasks
./taskmaster list

# Completa task
./taskmaster complete 1
```

**SEZIONI DA INCLUDERE**
[tutte quelle elencate sopra]

**STILE**
✅ Emoji con moderazione
📝 Code examples abbondanti
🎯 Focus su quick start
```

---

## 3.2 Template: Commenti Doxygen 🟢

### Descrizione
Genera commenti Doxygen per funzioni esistenti.

### Template

```
Genera commenti Doxygen completi per queste funzioni:

**STILE DOXYGEN RICHIESTO**
```c
/**
 * @brief [descrizione breve 1 riga]
 *
 * [Descrizione dettagliata opzionale, 2-3 righe se funzione complessa]
 *
 * @param [nome_param] [descrizione parametro + vincoli]
 * @param [nome_param2] [descrizione + range valori / NULL handling]
 * @return [descrizione return value + significato valori speciali]
 *
 * @note [informazioni importanti] (opzionale)
 * @warning [avvertimenti] (opzionale)
 *
 * @code
 * // Esempio d'uso
 * [codice esempio]
 * @endcode
 */
```

**FUNZIONI DA DOCUMENTARE**
```c
[INCOLLA FIRMA FUNZIONI O CODICE COMPLETO]
```

**REQUISITI**
- @brief obbligatorio per tutte
- @param per OGNI parametro con vincoli (es: "must be non-NULL", "must be > 0")
- @return che spiega TUTTI i possibili valori di ritorno
- @code esempio solo per funzioni pubbliche API
- @note per side effects (es: "modifica array in-place", "alloca memoria")
- @warning per pericoli (es: "caller must free", "not thread-safe")

**GENERA**
Solo commenti, non modificare codice funzioni.
```

---

## 3.3 Template: User Guide 🟡

### Descrizione
Guida utente per applicazioni end-user.

### Template

```
Scrivi una User Guide completa per [NOME_APPLICAZIONE].

**TARGET AUDIENCE**
[Descrizione utenti: tecnici? non-tecnici? livello esperienza?]

**APPLICAZIONE**
[Breve descrizione cosa fa]

**STRUTTURA GUIDA**

1. **Getting Started** (10 minuti dall'installazione al primo uso)
   - Cosa serve (prerequisiti)
   - Installazione step-by-step
   - Prima esecuzione
   - Tour interfaccia (se applicabile)

2. **Basic Operations** (operazioni giornaliere)
   - Operazione 1: [nome]
     - Quando usarla
     - Come eseguirla (step-by-step con screenshot se necessario)
     - Cosa aspettarsi
   - Operazione 2: [nome]
   - ...

3. **Common Workflows** (use case reali)
   - Workflow 1: [scenario tipico]
     - Step 1: [azione]
     - Step 2: [azione]
     - Risultato atteso
   - Workflow 2: [scenario]
   - ...

4. **Advanced Features** (opzionale)
   - Feature avanzata 1
   - Quando usarla
   - Esempi

5. **Troubleshooting** (problemi comuni)
   - Problema 1: [sintomo]
     - Causa: [spiegazione]
     - Soluzione: [step]
   - Problema 2
   - ...

6. **FAQ**
   - Domanda 1?
     - Risposta chiara e concisa
   - Domanda 2?
   - ...

7. **Reference** (quick reference)
   - Tutti i comandi disponibili
   - Tutti i parametri
   - Shortcuts

**STILE SCRITTURA**
- Linguaggio semplice (livello scuola media)
- Evita jargon tecnico o spiegalo
- Usa analogie quando utili
- Tono friendly e incoraggiante
- Step numerati chiaramente
- Evidenzia warning/note importanti

**FORMATO**
Markdown con:
- Headers chiari
- Code blocks per comandi
- Callout boxes (con > quote) per note/warning
- Tabelle per reference rapide
```

---

## 3.4 Template: API Documentation 🟡

### Descrizione
Documentazione API completa per librerie.

### Template

```
Genera API documentation completa per [NOME_LIBRERIA].

**OVERVIEW**
- Libreria: [nome]
- Versione: [x.y.z]
- Linguaggio: C
- Scopo: [cosa fa la libreria]

**STRUTTURA DOCUMENTAZIONE**

# [NOME_LIBRERIA] API Reference

## Installation

```bash
[comandi per installare/linkare libreria]
```

## Quick Start

```c
// Esempio minimale
#include "[libreria.h]"

int main() {
    // [codice minimo funzionante]
}
```

## Core Concepts

[Spiega 2-3 concetti chiave necessari per capire l'API]

## API Reference

### Data Types

#### `[struct/typedef nome]`

**Description:** [cosa rappresenta]

**Fields:**
- `[tipo] [nome]`: [descrizione]
- ...

**Example:**
```c
[esempio creazione e uso]
```

---

### Functions

#### `[nome_funzione]()`

```c
[firma completa]
```

**Description:** [cosa fa]

**Parameters:**
- `[nome]`: [tipo] - [descrizione dettagliata + vincoli]

**Returns:**
- [valore]: [significato]
- [valore errore]: [quando succede]

**Example:**
```c
[esempio uso]
```

**See Also:** [link ad altre funzioni correlate]

**Since:** [versione in cui è stata introdotta]

---

[Ripeti per ogni funzione pubblica]

## Error Handling

[Spiega filosofia error handling della libreria]

## Thread Safety

[Specifica se thread-safe, quali funzioni, quali no]

## Examples

### Example 1: [Scenario]
```c
[codice completo esempio]
```

### Example 2: [Scenario]
...

## Changelog

### v[X.Y.Z] - [Data]
- Added: [feature]
- Fixed: [bug]
- Changed: [breaking change]

**FORMATO OUTPUT**
Markdown che può essere convertito in HTML con Doxygen o simili.
```

---

## 3.5 Template: Architecture Document 🔴

### Descrizione
Documentazione architettura per sistemi complessi.

### Template

```
Scrivi Architecture Document per [NOME_SISTEMA].

**SISTEMA**
[Descrizione alto livello]

**AUDIENCE**
[Chi leggerà: developer nuovi, team lead, stakeholder?]

**STRUTTURA DOCUMENTO**

# [NOME] Architecture

## 1. Executive Summary (1 pagina)

Riassunto per manager non-tecnici:
- Cosa fa il sistema
- Perché è progettato così
- Componenti chiave
- Decisioni architetturali principali

## 2. System Overview

### 2.1 Context Diagram
```
[Diagramma ASCII showing sistema e interazioni esterne]

User → [Sistema] → Database
          ↓
     External API
```

### 2.2 High-Level Architecture
```
[Diagramma layer/moduli principali]
```

### 2.3 Technology Stack
- Language: [C99]
- Build: [Make]
- Dependencies: [list]
- Platform: [Linux/Windows/embedded]

## 3. Detailed Design

### 3.1 Module Breakdown

#### Module: [Nome]
**Responsibility:** [cosa fa]
**Files:** [lista file.c/.h]
**Dependencies:** [altri moduli]
**Interfaces:**
```c
[prototipi funzioni pubbliche chiave]
```

[Ripeti per ogni modulo]

### 3.2 Data Flow

```
[Diagramma ASCII mostrando flusso dati tra moduli]

Input → Module A → Module B → Output
                      ↓
                  Storage
```

### 3.3 Data Model

```c
// Core data structures
[struct principali con commenti]
```

## 4. Key Design Decisions

### Decision 1: [Titolo]
**Context:** [problema da risolvere]
**Options Considered:**
- Option A: [pro/contro]
- Option B: [pro/contro]
**Decision:** [scelta fatta]
**Rationale:** [perché]

[Ripeti per decisioni importanti]

## 5. Cross-Cutting Concerns

### 5.1 Error Handling
[Strategy utilizzata nel sistema]

### 5.2 Logging
[Dove, come, livelli]

### 5.3 Memory Management
[Ownership model, allocation strategy]

### 5.4 Thread Safety
[Se applicabile]

### 5.5 Security
[Considerazioni sicurezza]

## 6. Deployment

### 6.1 Build Process
```bash
[comandi build]
```

### 6.2 Configuration
[File config, parametri, environment]

### 6.3 Dependencies
[Runtime dependencies, versioni]

## 7. Performance Considerations

- Expected load: [descrizione]
- Bottlenecks identified: [lista]
- Optimizations: [cosa è stato ottimizzato]
- Scalability: [limiti]

## 8. Testing Strategy

- Unit tests: [copertura, framework]
- Integration tests: [approccio]
- Performance tests: [benchmark]

## 9. Future Enhancements

[Roadmap, feature pianificate, debt tecnico]

## 10. References

- [Link a doc esterne]
- [Papers/articoli rilevanti]
- [Standard seguiti]

**FORMATO**
Markdown con diagrammi ASCII (o PlantUML se richiesto).
Lunghezza: 15-30 pagine.
```

---

---

# 4. TESTING

---

## 4.1 Template: Unit Test Suite 🟢

### Descrizione
Genera suite di unit test completa per funzioni.

### Template

```
Genera unit test completi per questa funzione:

**FUNZIONE DA TESTARE**
```c
[CODICE FUNZIONE]
```

**FRAMEWORK TEST**
- [assert.h manuale / CUnit / Unity / altro]

**TEST RICHIESTI**

1. **Happy Path Tests** (comportamento normale)
   - Almeno 3 test con input validi tipici
   - Verifica output corretto

2. **Edge Case Tests** (casi limite)
   - Input minimo (es: 0, empty string, array vuoto)
   - Input massimo (es: INT_MAX, buffer pieno)
   - Boundary values (es: size-1, size, size+1)

3. **Error Handling Tests** (gestione errori)
   - Input NULL (se applicabile)
   - Input invalidi (es: negativi quando non permessi)
   - Verifica codici errore corretti

4. **State Tests** (se funzione cambia stato)
   - Verifica side effects
   - Verifica idempotenza (se applicabile)

**STRUTTURA OUTPUT**

```c
#include <assert.h>
#include <stdio.h>
#include "[header_funzione]"

// Test 1: [Descrizione]
void test_[nome_funzione]_[scenario]() {
    // Arrange (setup)
    [preparazione input]

    // Act (esecuzione)
    [tipo] result = [funzione](input);

    // Assert (verifica)
    assert(result == [expected]);

    printf("✅ Test [nome]: PASSED\\n");
}

// ... altri test ...

// Test runner
int main() {
    printf("Running [funzione] tests...\\n\\n");

    test_[nome]_happy_path_1();
    test_[nome]_happy_path_2();
    test_[nome]_edge_case_null();
    test_[nome]_edge_case_empty();
    test_[nome]_error_invalid_input();
    // ... tutti i test ...

    printf("\\n🎉 All tests passed!\\n");
    return 0;
}
```

**COPERTURA MINIMA**
- Tutte le branch (if/else) coperte
- Ogni return statement testato
- Ogni error path testato

**INCLUDI ANCHE**
- Istruzioni compilazione
- Istruzioni esecuzione
- Expected output quando tutti test passano
```

---

## 4.2 Template: Integration Test 🟡

### Descrizione
Test integrazione tra moduli multipli.

### Template

```
Genera integration tests per [SCENARIO_INTEGRAZIONE].

**MODULI COINVOLTI**
1. [Modulo A]: [responsabilità]
2. [Modulo B]: [responsabilità]
3. [Modulo C]: [responsabilità]

**INTERFACCE DA TESTARE**
- Modulo A → Modulo B: [funzione chiamata]
- Modulo B → Modulo C: [funzione chiamata]

**SCENARIO DA TESTARE**
[Descrizione workflow completo end-to-end]

**TEST STRUCTURE**

```c
// Test 1: End-to-end happy path
void test_integration_[scenario]_happy_path() {
    printf("Test: [scenario] - Happy Path\\n");

    // Setup (inizializza tutti i moduli)
    [ModuloA]* mod_a = [modulo_a_init]();
    [ModuloB]* mod_b = [modulo_b_init]();
    assert(mod_a != NULL && mod_b != NULL);

    // Step 1: [Azione]
    int result = [modulo_a_operazione](mod_a, input);
    assert(result == SUCCESS);

    // Step 2: [Passa dati a modulo B]
    [Tipo]* data = [modulo_a_get_data](mod_a);
    result = [modulo_b_process](mod_b, data);
    assert(result == SUCCESS);

    // Step 3: [Verifica risultato finale]
    [Tipo] final_result = [modulo_b_get_result](mod_b);
    assert(final_result == [EXPECTED]);

    // Cleanup
    [modulo_a_free](mod_a);
    [modulo_b_free](mod_b);

    printf("  ✅ PASSED\\n");
}

// Test 2: Error propagation
void test_integration_[scenario]_error_handling() {
    // Testa che errore in modulo A si propaga correttamente a B
    [similar structure]
}

// Test 3: Data consistency
void test_integration_[scenario]_data_consistency() {
    // Verifica che dati passati tra moduli rimangono consistenti
    [similar structure]
}
```

**SCENARI DA COPRIRE**
- [ ] Happy path completo
- [ ] Errore in modulo A → propagazione corretta
- [ ] Errore in modulo B → cleanup modulo A
- [ ] Dati consistenti tra passaggi
- [ ] Concorrenza (se applicabile)

**INCLUDI**
- Setup/teardown per ambiente test
- Fixtures (dati test riutilizzabili)
- Istruzioni esecuzione
```

---

## 4.3 Template: Valgrind Test Automation 🟡

### Descrizione
Automatizza testing memoria con Valgrind.

### Template

```
Crea test automation per verificare zero memory leaks con Valgrind.

**PROGRAMMI DA TESTARE**
- [programma1]: [descrizione]
- [programma2]: [descrizione]

**SCRIPT BASH RICHIESTO**

```bash
#!/bin/bash
# valgrind_test.sh - Automated memory leak testing

set -e  # Exit on error

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
NC='\\033[0m' # No Color

# Test counter
TESTS_RUN=0
TESTS_PASSED=0

# Function: run valgrind on program
test_program() {
    local program=$1
    local test_name=$2
    local args="$3"

    echo "Testing: $test_name"
    TESTS_RUN=$((TESTS_RUN+1))

    # Run valgrind
    valgrind --leak-check=full \\
             --show-leak-kinds=all \\
             --track-origins=yes \\
             --error-exitcode=1 \\
             --log-file=valgrind_$test_name.log \\
             ./$program $args > /dev/null 2>&1

    # Check result
    if [ $? -eq 0 ]; then
        # Check for "no leaks are possible"
        if grep -q "no leaks are possible" valgrind_$test_name.log; then
            echo "${GREEN}✅ PASSED${NC}: No leaks detected"
            TESTS_PASSED=$((TESTS_PASSED+1))
            rm valgrind_$test_name.log
        else
            echo "${RED}❌ FAILED${NC}: Leaks detected"
            echo "See valgrind_$test_name.log for details"
        fi
    else
        echo "${RED}❌ FAILED${NC}: Errors detected"
        echo "See valgrind_$test_name.log for details"
    fi
    echo ""
}

# Main test suite
echo "======================================"
echo "Memory Leak Test Suite (Valgrind)"
echo "======================================"
echo ""

# Test 1: [descrizione]
test_program "[program]" "[test_name]" "[args]"

# Test 2: ...
test_program "[program]" "[test_name]" "[args]"

# Summary
echo "======================================"
echo "Test Summary"
echo "======================================"
echo "Tests run: $TESTS_RUN"
echo "Tests passed: $TESTS_PASSED"
echo "Tests failed: $((TESTS_RUN - TESTS_PASSED))"

if [ $TESTS_PASSED -eq $TESTS_RUN ]; then
    echo "${GREEN}✅ All tests PASSED${NC}"
    exit 0
else
    echo "${RED}❌ Some tests FAILED${NC}"
    exit 1
fi
```

**TEST CASES DA INCLUDERE**
- [Test 1]: [scenario]
- [Test 2]: [scenario]
- ...

**MAKEFILE INTEGRATION**

```makefile
# Add to Makefile

.PHONY: valgrind-test
valgrind-test: [programs]
\t./valgrind_test.sh
```

**USAGE**
```bash
# Make executable
chmod +x valgrind_test.sh

# Run tests
make valgrind-test

# Or directly
./valgrind_test.sh
```
```

---

## 4.4 Template: Stress Testing 🔴

### Descrizione
Test con input grandi, molte iterazioni, edge of limits.

### Template

```
Genera stress test per [COMPONENTE].

**OBIETTIVO STRESS TEST**
- Verificare stabilità sotto carico
- Trovare limiti pratici
- Identificare memory leaks in long run
- Verificare performance degrada gracefully

**STRESS SCENARIOS**

1. **Large Input Test**
```c
void stress_test_large_input() {
    printf("Stress test: Large input (10,000 items)\\n");

    [STRUCT]* container = [create]();

    // Add 10,000 items
    for (int i = 0; i < 10000; i++) {
        [ITEM] item = [generate_item](i);
        int result = [add](container, item);
        assert(result == SUCCESS);

        // Print progress every 1000
        if (i % 1000 == 0) {
            printf("  Added %d items...\\n", i);
        }
    }

    // Verify all items present
    assert([get_count](container) == 10000);

    // Cleanup
    [free](container);

    printf("  ✅ Large input test PASSED\\n");
}
```

2. **Repeated Operations Test**
```c
void stress_test_repeated_operations() {
    printf("Stress test: Repeated add/remove (100,000 ops)\\n");

    [STRUCT]* container = [create]();

    for (int i = 0; i < 100000; i++) {
        // Add item
        [add](container, [item]);

        // Remove item
        [remove](container, 0);

        // Verify empty
        assert([get_count](container) == 0);

        if (i % 10000 == 0) {
            printf("  Completed %d operations...\\n", i);
        }
    }

    [free](container);

    printf("  ✅ Repeated operations test PASSED\\n");
}
```

3. **Memory Limit Test**
```c
void stress_test_memory_limit() {
    printf("Stress test: Approach memory limit\\n");

    // Allocate until failure
    int count = 0;
    while (count < 1000000) { // Safety limit
        [STRUCT]* item = [allocate]();
        if (item == NULL) {
            printf("  Allocation failed at %d items (expected)\\n", count);
            break;
        }
        count++;

        if (count % 100000 == 0) {
            printf("  Allocated %d items...\\n", count);
        }
    }

    // Cleanup all allocations
    // [free all items]

    printf("  ✅ Memory limit test PASSED\\n");
}
```

4. **Time-Based Test**
```c
void stress_test_long_running() {
    printf("Stress test: Run for 60 seconds\\n");

    [STRUCT]* container = [create]();

    time_t start = time(NULL);
    int operations = 0;

    while (difftime(time(NULL), start) < 60.0) {
        // Perform random operations
        int op = rand() % 3;

        switch(op) {
            case 0: [add](container, [item]); break;
            case 1: if ([count](container) > 0) [remove](container, 0); break;
            case 2: [search](container, [key]); break;
        }

        operations++;

        if (operations % 10000 == 0) {
            printf("  %d operations (%.0f sec elapsed)\\n",
                   operations, difftime(time(NULL), start));
        }
    }

    printf("  Completed %d operations in 60 seconds\\n", operations);

    [free](container);

    printf("  ✅ Long running test PASSED\\n");
}
```

**METRICHE DA TRACCIARE**
- Tempo esecuzione per ciascun test
- Memoria usata (peak RSS)
- Operazioni al secondo
- Eventuali failures

**AUTOMATION**
Includi script che:
- Compila con optimization (-O2)
- Esegue tutti stress test
- Monitora con time e /usr/bin/time -v
- Verifica Valgrind dopo (no leaks anche su test lunghi)
```

---

## 4.5 Template: Test-Driven Development (TDD) 🟡

### Descrizione
Genera test PRIMA di implementare funzione.

### Template

```
Usa approccio TDD per implementare [FUNZIONALITÀ].

**TDD WORKFLOW**

Seguimi in 3 cicli Red-Green-Refactor:

**CYCLE 1: Simplest Test**

1. **RED - Write failing test**

```c
// test_[function].c

void test_[function]_simplest_case() {
    // Test più semplice possibile
    [TYPE] result = [function]([simplest_input]);
    assert(result == [expected]);
}

int main() {
    test_[function]_simplest_case();
    return 0;
}
```

Compila e verifica che FALLISCE (funzione non esiste ancora).

2. **GREEN - Write minimal code to pass**

```c
// [function].c

[TYPE] [function]([PARAMS]) {
    // Implementazione MINIMA che fa passare test
    return [hardcoded_value];
}
```

Compila e verifica test PASSA.

3. **REFACTOR - Improve if needed**

[In questo caso probabilmente non serve refactor]

---

**CYCLE 2: Add more test cases**

1. **RED - Add new test**

```c
void test_[function]_case_2() {
    [TYPE] result = [function]([input_2]);
    assert(result == [expected_2]);
}
```

Verifica FALLISCE (hardcoded value non funziona più).

2. **GREEN - Implement real logic**

```c
[TYPE] [function]([PARAMS]) {
    // Ora implementa logica vera
    [algoritmo reale]
    return result;
}
```

Verifica ENTRAMBI i test passano.

3. **REFACTOR - Clean up**

[Rifattorizza se codice duplicato o poco chiaro]

---

**CYCLE 3: Edge cases**

1. **RED - Edge case test**

```c
void test_[function]_edge_null() {
    [TYPE] result = [function](NULL);
    assert(result == [error_value]);
}

void test_[function]_edge_empty() {
    [TYPE] result = [function]([empty_input]);
    assert(result == [expected_for_empty]);
}
```

Verifica FALLISCONO (no gestione edge cases).

2. **GREEN - Add edge case handling**

```c
[TYPE] [function]([PARAMS]) {
    // Validate input
    if ([param] == NULL) return [error];
    if ([empty_condition]) return [empty_result];

    // Existing logic
    [...]
}
```

Verifica TUTTI i test passano.

3. **REFACTOR - Final cleanup**

[Rifattorizza per chiarezza, rimuovi duplicazione]

---

**FINAL TEST SUITE**

```c
// All tests together
int main() {
    test_[function]_simplest_case();
    test_[function]_case_2();
    test_[function]_edge_null();
    test_[function]_edge_empty();

    printf("✅ All tests PASSED\\n");
    return 0;
}
```

**BEST PRACTICES TDD**
- Test SEMPRE prima del codice
- Test più semplice possibile per primo
- Codice minimo per far passare test
- Refactor solo quando test passano
- Commit ad ogni green phase
```

---

---

# 5. OTTIMIZZAZIONE

---

## 5.1 Template: Ottimizzazione Performance 🟡

### Descrizione
Analizza e ottimizza codice lento.

### Template

```
Ottimizza questo codice per migliori performance.

**CODICE ATTUALE**
```c
[CODICE DA OTTIMIZZARE]
```

**PROFILING DATA**
```
[Output gprof/perf se disponibile]
```

**PERFORMANCE ISSUE**
- Tempo attuale: [X secondi] per input size [N]
- Tempo target: [Y secondi]
- Risorsa limitante: [CPU / Memory / I/O]

**ANALISI RICHIESTA**

1. **Complessità Attuale**
   - Big-O analisi (tempo e spazio)
   - Identificazione bottleneck (quale riga/funzione)

2. **Ottimizzazioni Algoritmiche**
   - Esiste algoritmo con complessità migliore?
   - Tabelle/memo per evitare ricalcoli?
   - Struttura dati migliore?

3. **Ottimizzazioni Implementazione**
   - Riduci allocazioni (riusa buffer?)
   - Migliora cache locality (dati contigui?)
   - Elimina copia inutili (usa puntatori?)
   - Loop optimization (unrolling se sensato?)

4. **Compiler Optimizations**
   - Suggerisci flag (-O2, -O3, -march=native)
   - Annotazioni (inline, restrict, const)

**OUTPUT**

```c
// Codice ottimizzato
[CODICE MIGLIORATO]
```

**Spiegazione ottimizzazioni:**
1. [Ottimizzazione 1]: [descrizione + impatto stimato]
2. [Ottimizzazione 2]: [descrizione + impatto]

**Complessità nuova:** O([NUOVA_COMPLESSITÀ])

**Benchmark comparativo:**
```c
// Test performance (usare clock() o simile)
[codice benchmark che confronta vecchio vs nuovo]
```

**Expected speedup:** [stima miglioramento]
```

---

## 5.2 Template: Ottimizzazione Memoria 🟡

### Descrizione
Riduci uso memoria di programma.

### Template

```
Ottimizza uso memoria di questo codice.

**CODICE ATTUALE**
```c
[CODICE]
```

**MEMORY PROFILE**
- Memoria usata: [X MB/KB]
- Target: [Y MB/KB]
- Picco allocazione: [quando]

**ANALISI RICHIESTA**

1. **Memory Audit**
   - Struct size analysis (usa sizeof, padding?)
   - Array size (sovradimensionati?)
   - Stack vs heap (troppo su stack?)

2. **Optimization Strategies**

   a) **Struct packing**
   ```c
   // Before
   struct {
       char a;   // 1 byte + 3 padding
       int b;    // 4 bytes
       char c;   // 1 byte + 3 padding
   };  // Total: 12 bytes

   // After
   struct {
       int b;    // 4 bytes
       char a;   // 1 byte
       char c;   // 1 byte + 2 padding
   };  // Total: 8 bytes
   ```

   b) **Bit fields** (se molti bool)
   ```c
   // Before
   struct {
       int flag1;  // 4 bytes
       int flag2;  // 4 bytes
       int flag3;  // 4 bytes
   };  // 12 bytes

   // After
   struct {
       unsigned int flag1 : 1;
       unsigned int flag2 : 1;
       unsigned int flag3 : 1;
   };  // 4 bytes (or less)
   ```

   c) **Pool allocation** (riusa memoria)
   ```c
   // Before: alloca/free per ogni elemento

   // After: pre-alloca pool, riusa slot
   ```

   d) **Lazy loading** (carica solo quando serve)

   e) **Compression** (se dati ripetitivi)

3. **Trade-offs**
   - Memoria vs velocità
   - Complessità codice vs beneficio

**OUTPUT**

```c
// Codice ottimizzato memoria
[CODICE MIGLIORATO]
```

**Risparmio stimato:** [X% o Y KB]

**Benchmark:**
```bash
# Misura con valgrind massif
valgrind --tool=massif ./program_original
valgrind --tool=massif ./program_optimized
ms_print massif.out.*
```
```

---

## 5.3 Template: Ottimizzazione Algoritmo 🔴

### Descrizione
Sostituisci algoritmo con uno più efficiente.

### Template

```
Sostituisci algoritmo inefficiente con alternativa migliore.

**PROBLEMA**
[Descrizione task algoritmo deve risolvere]

**ALGORITMO ATTUALE**
```c
[CODICE ALGORITMO CORRENTE]
```

**COMPLESSITÀ ATTUALE**
- Tempo: O([CURRENT_TIME])
- Spazio: O([CURRENT_SPACE])
- Problema con input size: [descrizione issue]

**ANALISI ALTERNATIVE**

Confronta almeno 3 algoritmi alternativi:

| Algoritmo | Time Complexity | Space Complexity | Pro | Contro |
|-----------|----------------|------------------|-----|--------|
| Attuale   | O([...])       | O([...])         | [pro] | [contro] |
| Alt. 1    | O([...])       | O([...])         | [pro] | [contro] |
| Alt. 2    | O([...])       | O([...])         | [pro] | [contro] |
| Alt. 3    | O([...])       | O([...])         | [pro] | [contro] |

**RACCOMANDAZIONE**

Algoritmo scelto: [NOME]
Motivo: [giustificazione basata su use case]

**IMPLEMENTAZIONE**

```c
// Nuovo algoritmo implementato
[CODICE COMPLETO]
```

**Spiegazione algoritmo:**
[Descrizione step-by-step come funziona]

**Complessità analysis:**
- Caso migliore: O([BEST])
- Caso medio: O([AVG])
- Caso peggiore: O([WORST])

**Benchmark:**

```c
// Confronto performance
#include <time.h>

void benchmark_algorithms() {
    clock_t start, end;

    // Test old algorithm
    start = clock();
    [old_algorithm]([input]);
    end = clock();
    double time_old = ((double)(end - start)) / CLOCKS_PER_SEC;

    // Test new algorithm
    start = clock();
    [new_algorithm]([input]);
    end = clock();
    double time_new = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Old: %.6f sec\\n", time_old);
    printf("New: %.6f sec\\n", time_new);
    printf("Speedup: %.2fx\\n", time_old / time_new);
}
```

**Expected improvement:** [stima]
```

---

---

# 6. CODE REVIEW E REFACTORING

---

## 6.1 Template: Security Review 🔴

### Descrizione
Analisi sicurezza codice, vulnerabilità comuni.

### Template

```
Esegui security audit completo di questo codice.

**CONTEXT**
- Tipo applicazione: [CLI tool / server / library / embedded]
- Dati gestiti: [sensibili? user input? file esterni?]
- Ambiente: [trusted / untrusted input?]

**CODICE DA REVIEWARE**
```c
[CODICE COMPLETO]
```

**SECURITY CHECKLIST**

Analizza per queste vulnerabilità:

### 1. Buffer Overflow (CWE-120)
- [ ] Tutti i buffer hanno size check?
- [ ] `strcpy` sostituito con `strncpy` o `strlcpy`?
- [ ] `scanf("%s")` sostituito con `scanf("%99s")`?
- [ ] `gets()` mai usato (è deprecato)?

### 2. Integer Overflow (CWE-190)
- [ ] Moltiplicazioni controllate prima di malloc?
- [ ] Addizioni che potrebbero overflow?
- [ ] Cast impliciti pericolosi?

### 3. Format String (CWE-134)
- [ ] `printf(user_input)` vs `printf("%s", user_input)`?
- [ ] Format string da source untrusted?

### 4. Memory Issues
- [ ] Ogni malloc ha check NULL?
- [ ] Use-after-free possibile?
- [ ] Double-free possibile?
- [ ] Uninitialized memory read?

### 5. Path Traversal (CWE-22)
- [ ] Filenames validati (no "../../../etc/passwd")?
- [ ] Path resolution sicura?

### 6. Command Injection (CWE-78)
- [ ] `system()` chiamato con user input?
- [ ] Input sanitizzato prima di shell commands?

### 7. Race Conditions (CWE-362)
- [ ] TOCTOU bugs? (Time-Of-Check-Time-Of-Use)
- [ ] File operations non-atomic?

### 8. Access Control
- [ ] Privilegi minimi (drop root dopo init)?
- [ ] File permissions corretti?

**OUTPUT FORMAT**

```markdown
# Security Audit Report

## Executive Summary
[Breve riassunto: quante vulnerabilità, severità]

## Vulnerabilities Found

### 🔴 CRITICAL - [Nome Vulnerabilità]
**Location:** [file.c:linea]
**CWE:** [CWE-XXX]
**Description:** [cosa è sbagliato]
**Exploit Scenario:** [come potrebbe essere sfruttato]
**Impact:** [conseguenze]
**Fix:**
```c
[codice corretto]
```

### 🟠 HIGH - [Nome]
[...stesso formato...]

### 🟡 MEDIUM - [Nome]
[...stesso formato...]

### 🟢 LOW - [Nome]
[...stesso formato...]

## Recommendations
1. [Raccomandazione prioritaria]
2. [Altra raccomandazione]

## Secure Coding Guidelines
[Link a linee guida rilevanti: CERT C, CWE Top 25]
```

**TOOLS SUGGERITI**
```bash
# Static analysis
cppcheck --enable=all file.c
clang --analyze file.c

# Fuzzing
afl-fuzz -i input_dir -o output_dir ./program @@
```
```

---

## 6.2 Template: Code Quality Review 🟡

### Descrizione
Review generale qualità codice, best practices.

### Template

```
Esegui code review completo focalizzato su qualità e manutenibilità.

**CODICE**
```c
[CODICE DA REVIEWARE]
```

**REVIEW DIMENSIONS**

### 1. Readability (1-10): __/10

**Issues found:**
- [ ] Naming inconsistente (camelCase vs snake_case mix?)
- [ ] Magic numbers (use #define o const)
- [ ] Funzioni troppo lunghe (>50 righe?)
- [ ] Nesting profondo (>3 livelli?)
- [ ] Commenti obsoleti/fuorvianti

**Suggerimenti:**
[Lista miglioramenti specifici]

---

### 2. Maintainability (1-10): __/10

**Issues found:**
- [ ] Duplicazione codice (DRY principle violato?)
- [ ] Tight coupling (moduli troppo dipendenti?)
- [ ] God functions (fanno troppe cose?)
- [ ] Hardcoded values (no configurabilità?)

**Suggerimenti:**
[Refactoring proposti]

---

### 3. Correctness (1-10): __/10

**Issues found:**
- [ ] Edge cases non gestiti
- [ ] Error handling incompleto
- [ ] Assunzioni non documentate
- [ ] Off-by-one errors
- [ ] Type mismatch issues

**Bugs trovati:**
[Lista bug con fix]

---

### 4. Performance (1-10): __/10

**Issues found:**
- [ ] Inefficienze algoritmiche evidenti
- [ ] Allocazioni inutili
- [ ] Copia inutili di dati
- [ ] I/O non buffered

**Ottimizzazioni quick-win:**
[Ottimizzazioni facili con alto impatto]

---

### 5. Safety (1-10): __/10

**Issues found:**
- [ ] Memory leaks (run Valgrind)
- [ ] Buffer overflow risks
- [ ] Null pointer dereferences
- [ ] Undefined behavior

**Fix critici:**
[Lista fix necessari]

---

## OVERALL SCORE: __/50

## Priority Fixes

### HIGH PRIORITY (fix prima di merge)
1. [Issue critico 1]
2. [Issue critico 2]

### MEDIUM PRIORITY (fix prossima iterazione)
1. [Issue importante 1]
2. [Issue importante 2]

### LOW PRIORITY (nice-to-have)
1. [Miglioramento 1]
2. [Miglioramento 2]

## Refactoring Suggestions

```c
// Before
[esempio codice problematico]

// After
[esempio refactored]

// Why: [spiegazione benefici]
```

## Positive Aspects
[Cosa è fatto bene - feedback positivo!]

## Conclusion
[Riassunto generale + raccomandazione: approve / approve with changes / reject]
```

---

## 6.3 Template: Refactoring Plan 🟡

### Descrizione
Piano dettagliato per refactoring sicuro.

### Template

```
Crea piano di refactoring per [COMPONENTE/MODULO].

**PROBLEMA ATTUALE**
[Descrizione debt tecnico o problemi design]

**OBIETTIVO REFACTORING**
[Cosa vogliamo ottenere]

**VINCOLI**
- Non deve rompere API pubblica: [sì/no]
- Backward compatibility richiesta: [sì/no]
- Deve rimanere testabile: [sì]
- Tempo disponibile: [stima]

**REFACTORING PLAN**

### Step 1: Setup Safety Net

**Prima di qualsiasi modifica:**

1. **Add comprehensive tests** (se mancanti)
```c
// Scrivi test che coverano comportamento attuale
[test suite che fissa comportamento corrente]
```

2. **Baseline performance benchmark**
```c
// Misura performance before refactoring
[benchmark code]
```

3. **Git branch**
```bash
git checkout -b refactor/[nome]
git commit -am "Pre-refactor baseline + tests"
```

---

### Step 2: Extract Functions

**Identifica pezzi da estrarre:**

```c
// Before: God function
void do_everything() {
    // Part 1: validation (20 lines)
    [...]

    // Part 2: processing (50 lines)
    [...]

    // Part 3: output (15 lines)
    [...]
}

// After: Split in funzioni smaller
static int validate_input(...) {
    [extracted validation]
}

static int process_data(...) {
    [extracted processing]
}

static int generate_output(...) {
    [extracted output]
}

void do_everything() {
    if (validate_input(...) != 0) return -1;
    if (process_data(...) != 0) return -2;
    if (generate_output(...) != 0) return -3;
}
```

**Verifica:** Run tests, must still pass.
**Commit:** `git commit -am "refactor: Extract helper functions"`

---

### Step 3: Rename for Clarity

**Migliora naming:**

```c
// Before
int proc(Data* d) { ... }

// After
int process_customer_order(CustomerOrder* order) { ... }
```

**Verifica:** Compile + test.
**Commit:** `git commit -am "refactor: Improve naming"`

---

### Step 4: Remove Duplication

**DRY principle:**

```c
// Before: duplicazione
void func_a() {
    [common code]
    [specific A]
}

void func_b() {
    [common code]  // DUPLICATED!
    [specific B]
}

// After: extract common
static void common_logic() {
    [common code]
}

void func_a() {
    common_logic();
    [specific A]
}

void func_b() {
    common_logic();
    [specific B]
}
```

**Verifica:** Test pass.
**Commit:** `git commit -am "refactor: Remove duplication"`

---

### Step 5: Improve Error Handling

**Consistenza gestione errori:**

```c
// Before: mix di stili
int func1() { return -1; }  // Error code
int func2() { errno = EINVAL; return 0; }  // errno
void func3() { exit(1); }  // Termina!

// After: stile consistente (scegli uno)
int func1() { return ERROR_INVALID_INPUT; }
int func2() { return ERROR_FILE_NOT_FOUND; }
int func3() { return ERROR_OUT_OF_MEMORY; }
```

**Verifica:** Test pass.
**Commit:** `git commit -am "refactor: Standardize error handling"`

---

### Step 6: Performance Check

**Benchmark after refactoring:**

```c
// Run same benchmark di Step 1
[benchmark code]

// Compare results
printf("Before: %.6f sec\\n", time_before);
printf("After:  %.6f sec\\n", time_after);

// Acceptable if within 5% (refactoring potrebbe slightly slow)
```

---

### Step 7: Final Review

**Checklist:**
- [ ] All tests pass
- [ ] No new warnings (compile with -Wall -Wextra)
- [ ] Valgrind clean (no new leaks)
- [ ] Performance not degraded >5%
- [ ] Code more readable than before
- [ ] Documentation updated

**Merge:**
```bash
git checkout main
git merge refactor/[nome]
git tag refactor-[nome]-complete
```

---

## ROLLBACK PLAN

Se qualcosa va male durante refactoring:

```bash
# Torna a commit pre-refactor
git reset --hard [baseline_commit_hash]

# Oppure crea patch per salvare lavoro parziale
git diff > refactor_wip.patch
git reset --hard [baseline]
# Poi applica patch quando sei pronto
git apply refactor_wip.patch
```

## RISKS & MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Break API | Low | High | Test suite completo |
| Performance regress | Medium | Medium | Benchmark before/after |
| Introduce bugs | Medium | High | Incremental refactor + test |

```

---

---

# 7. GIT E WORKFLOW

---

## 7.1 Template: Commit Message 🟢

### Descrizione
Genera commit message seguendo conventional commits.

### Template

```
Genera commit message per queste modifiche.

**MODIFICHE FATTE**
[Descrizione breve cosa è stato modificato]

**FILE MODIFICATI**
- [file1.c]: [modifica]
- [file2.h]: [modifica]

**CONVENTIONAL COMMITS FORMAT**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**TYPES:**
- feat: Nuova feature
- fix: Bug fix
- docs: Solo documentazione
- style: Formattazione (no logic change)
- refactor: Né feat né fix
- perf: Performance improvement
- test: Aggiunta test
- chore: Build, tools, dependencies

**EXAMPLES:**

```
feat(parser): Add support for CSV comments

Implemented parsing logic to skip lines starting with '#'.
This allows CSV files to include metadata comments at the top.

- Added is_comment_line() helper function
- Updated parse_csv() to skip comment lines
- Added tests for comment handling

Closes #42
```

```
fix(memory): Prevent leak in student_db_free()

student_db_free() was not freeing the individual student name strings
before freeing the array, causing memory leak detected by Valgrind.

- Added loop to free each student->name
- Valgrind now reports 0 leaks

Fixes #38
```

**REGOLE:**
- Subject max 50 caratteri
- Subject imperativo ("Add" not "Added")
- Body wrapped at 72 caratteri
- Spiega WHY, non WHAT (il diff mostra WHAT)
- Reference issue/PR se applicabile

**GENERA COMMIT MESSAGE PER:**
[descrivi modifiche specifiche]
```

---

## 7.2 Template: Branch Strategy 🟡

### Descrizione
Setup branching strategy per progetto.

### Template

```
Definisci Git branching strategy per [PROGETTO].

**CONTEXT**
- Tipo progetto: [solo / team di X persone]
- Release frequency: [continuous / versioned releases]
- Environment: [dev, staging, production?]

**BRANCHING MODELS** (scegli uno)

### Option A: GitHub Flow (semplice, per continuous deployment)

```
main (sempre deployable)
  │
  ├─ feature/user-auth
  ├─ feature/csv-export
  └─ bugfix/memory-leak
```

**Rules:**
1. `main` è sempre stable
2. Crea branch per ogni feature: `feature/[nome]`
3. Pull Request per merge in main
4. Deploy da main after merge

**Commands:**
```bash
# Start feature
git checkout -b feature/user-auth

# Work + commit
git add ...
git commit -m "..."

# Push
git push -u origin feature/user-auth

# Create PR su GitHub

# After merge, delete branch
git branch -d feature/user-auth
```

---

### Option B: Git Flow (per release versionate)

```
main (production)
  │
develop (integration)
  ├─ feature/X
  ├─ feature/Y
  └─ release/v1.2.0
       └─ hotfix/critical-bug
```

**Branches:**
- `main`: production, tagged releases (v1.0.0, v1.1.0)
- `develop`: integration branch
- `feature/*`: features (branch from develop)
- `release/*`: release preparation (branch from develop)
- `hotfix/*`: urgent prod fixes (branch from main)

**Workflow:**
```bash
# Feature
git checkout develop
git checkout -b feature/user-auth
[lavoro]
git checkout develop
git merge feature/user-auth

# Release
git checkout -b release/v1.2.0 develop
[bug fix, version bump]
git checkout main
git merge release/v1.2.0
git tag v1.2.0
git checkout develop
git merge release/v1.2.0

# Hotfix
git checkout -b hotfix/critical-bug main
[fix]
git checkout main
git merge hotfix/critical-bug
git tag v1.2.1
git checkout develop
git merge hotfix/critical-bug
```

---

### Option C: Trunk-Based (per team grandi, CI/CD)

```
main (trunk)
  ├─ short-lived branches (max 1-2 days)
```

**Rules:**
1. Tutti committano spesso su main
2. Branch di vita breve (<2 giorni)
3. Feature flags per features incomplete
4. CI esegue test ad ogni commit

---

## RECOMMENDED FOR [PROGETTO]

**Strategy:** [A/B/C]
**Rationale:** [perché questa scelta]

**BRANCH NAMING CONVENTION**

```
feature/[short-description]
bugfix/[issue-number]-[description]
hotfix/[critical-issue]
release/v[X.Y.Z]
```

**PROTECTION RULES** (GitHub settings)

main branch:
- [ ] Require pull request reviews (almeno 1)
- [ ] Require status checks (CI green)
- [ ] No direct push

**WORKFLOW DIAGRAM**

[ASCII diagram del flow scelto]
```

---

## 7.3 Template: Pull Request 🟡

### Descrizione
Template per Pull Request complete.

### Template

```
Crea Pull Request description per [FEATURE/FIX].

**GITHUB PR TEMPLATE**

## Summary

[Breve descrizione 2-3 frasi di cosa fa questa PR]

## Type of Change

- [ ] 🐛 Bug fix (non-breaking change che risolve issue)
- [ ] ✨ New feature (non-breaking change che aggiunge funzionalità)
- [ ] 💥 Breaking change (fix o feature che causa breaking di esistente)
- [ ] 📝 Documentation update
- [ ] ♻️ Code refactoring
- [ ] ⚡ Performance improvement

## Motivation and Context

**Problem:**
[Descrivi problema che questa PR risolve]

**Solution:**
[Descrivi come questa PR risolve il problema]

**Alternatives considered:**
[Eventuali approcci alternativi considerati e perché scartati]

## Related Issues

Closes #[issue_number]
Related to #[issue_number]

## Changes Made

### Added
- [Cosa è stato aggiunto]

### Changed
- [Cosa è stato modificato]

### Removed
- [Cosa è stato rimosso]

### Fixed
- [Bug fixati]

## Testing

### Test Checklist
- [ ] Unit tests aggiunti/updated
- [ ] Integration tests passed
- [ ] Manual testing eseguito
- [ ] Valgrind clean (no memory leaks)
- [ ] No new compiler warnings

### Test Instructions

```bash
# Come testare questa PR
git checkout [branch-name]
make test
./program [example usage]
```

### Test Results

```
[Incolla output test se rilevante]
```

## Performance Impact

- [ ] No performance impact
- [ ] Performance improvement: [describe]
- [ ] Potential performance regression: [explain + justify]

**Benchmark results** (se applicabile):
```
Before: X ms
After:  Y ms
Change: +/-Z%
```

## Breaking Changes

- [ ] No breaking changes
- [ ] Breaking changes (describe below)

**Migration guide** (se breaking):
```
// Before
[old usage]

// After
[new usage]
```

## Documentation

- [ ] Code comments updated
- [ ] README updated
- [ ] API documentation updated
- [ ] User guide updated (if applicable)

## Screenshots / Examples

[Se applicabile, screenshot o esempi output]

```
$ ./program
[example output]
```

## Deployment Notes

[Eventuali note per deployment: migration scripts, config changes, etc.]

## Checklist Before Merge

- [ ] Code compiles without errors/warnings
- [ ] All tests pass locally
- [ ] CI/CD pipeline green
- [ ] Code reviewed by at least 1 person
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Branch up to date with main

## Reviewer Notes

@reviewer-username: Please pay special attention to:
- [Area specifica da revieware]
- [Parte complicata che richiede attenzione]

---

**[Your Name]**
[Date]
```

---

---

# 8. APPRENDIMENTO

---

## 8.1 Template: Spiegazione Concetto 🟢

### Descrizione
Chiedi spiegazione chiara di concetto complesso.

### Template

```
Spiega il concetto di [CONCETTO] in modo chiaro per studente ITS.

**CONTESTO**
Sono uno studente ITS [primo/secondo anno].
Ho familiarità con: [lista concetti che conosci]
Non ho ancora studiato: [lista concetti avanzati]

**RICHIESTA**

Spiega [CONCETTO] seguendo questa struttura:

1. **Cos'è in 1 frase** (elevator pitch)

2. **Perché è importante** (motivazione)
   - Problema che risolve
   - Quando si usa

3. **Come funziona** (spiegazione con analogia)
   - Usa analogia del mondo reale
   - Diagramma ASCII se utile
   - Evita jargon o spiegalo

4. **Esempio pratico** (codice o scenario reale)
   ```c
   // Esempio minimo che mostra il concetto
   [codice commentato]
   ```

5. **Errori comuni** (cosa evitare)
   - Misconception tipica
   - Come riconoscere l'errore
   - Come fixare

6. **Approfondimento** (se voglio saperne di più)
   - Link risorse
   - Concetti correlati
   - Next steps

**STILE SPIEGAZIONE**
- Linguaggio semplice (livello scuola superiore)
- Costruisci da concetti base verso avanzati
- Usa esempi concreti, non astratti
- Lunghezza: 500-800 parole
```

### Esempio Riempito

```
Spiega il concetto di "puntatori a puntatori" in modo chiaro per studente ITS.

**CONTESTO**
Sono uno studente ITS primo anno.
Ho familiarità con: variabili, array, puntatori semplici (int*)
Non ho ancora studiato: liste linkate complesse, allocazione dinamica avanzata

**RICHIESTA**
[segui struttura sopra]
```

---

## 8.2 Template: Tutorial Step-by-Step 🟢

### Descrizione
Tutorial pratico che costruisce qualcosa da zero.

### Template

```
Crea tutorial step-by-step per [TASK/PROGETTO].

**OBIETTIVO FINALE**
[Cosa lo studente saprà fare alla fine]

**PREREQUISITI**
- Conoscenze richieste: [lista]
- Software necessario: [lista]
- Tempo stimato: [X minuti/ore]

**TUTORIAL STRUCTURE**

# Tutorial: [TITOLO]

## Introduction

[Breve intro: cosa costruiremo, perché è utile]

**What you'll learn:**
- [Skill 1]
- [Skill 2]
- [Skill 3]

---

## Step 1: Setup

**Goal:** [Cosa otterremo in questo step]

**Instructions:**

1. [Azione concreta]
   ```bash
   [comando esatto]
   ```

2. [Azione 2]
   ```bash
   [comando]
   ```

**Verify:**
```bash
# Verifica che setup ha funzionato
[comando verifica]
# Expected output: [cosa dovresti vedere]
```

**Troubleshooting:**
- Problem: [possibile errore]
  - Solution: [come risolvere]

---

## Step 2: [Nome Step]

**Goal:** [Cosa otterremo]

**Code:**

```c
// [file.c]
[codice con commenti ABBONDANTI]
```

**Explanation:**

Analizziamo il codice riga per riga:

- **Line X:** [spiegazione cosa fa]
- **Line Y:** [spiegazione]

**Try it:**
```bash
gcc file.c -o program
./program
# Expected output: [...]
```

---

## Step 3: [Estendi funzionalità]

**Goal:** [Aggiungi feature]

**Modify code:**

```c
// Aggiungi queste righe:
[codice nuovo]
```

**Why this works:**
[Spiegazione logica]

**Test:**
```bash
[comandi test]
```

---

[Continua step per tutti i passaggi necessari]

---

## Step N: Final Touches

**What we've built:**
[Riassunto progetto completo]

**Full code:**
```c
// Codice completo finale
[tutto insieme]
```

**Next steps:**
[Sfide opzionali per estendere]

---

## Recap

✅ **You've learned:**
- [Skill 1 con esempio]
- [Skill 2 con esempio]
- [Skill 3 con esempio]

**Challenge yourself:**
[Esercizi suggeriti per praticare]

**Resources:**
- [Link utile 1]
- [Link utile 2]
```

---

## 8.3 Template: Confronta Approcci 🟡

### Descrizione
Confronto sistematico di approcci alternativi.

### Template

```
Confronta approcci per [PROBLEMA/TASK].

**PROBLEMA**
[Descrizione dettagliata problema da risolvere]

**APPROCCI DA CONFRONTARE**

Confronta almeno 3 approcci differenti.

---

### Approach A: [NOME]

**Description:**
[Come funziona questo approccio]

**Code example:**
```c
[implementazione esempio]
```

**Pros:**
- ✅ [Pro 1]
- ✅ [Pro 2]

**Cons:**
- ❌ [Contro 1]
- ❌ [Contro 2]

**Performance:** O([complexity])

**Best for:** [Quando usarlo]

---

### Approach B: [NOME]

[Stessa struttura]

---

### Approach C: [NOME]

[Stessa struttura]

---

## COMPARISON TABLE

| Criteria | Approach A | Approach B | Approach C |
|----------|-----------|-----------|-----------|
| Time Complexity | O([...]) | O([...]) | O([...]) |
| Space Complexity | O([...]) | O([...]) | O([...]) |
| Ease of Implementation | [Easy/Medium/Hard] | [...] | [...] |
| Code Maintainability | [High/Medium/Low] | [...] | [...] |
| Memory Usage | [Low/Med/High] | [...] | [...] |
| Type Safety | [Strong/Weak] | [...] | [...] |
| Error Handling | [Good/OK/Poor] | [...] | [...] |

## RECOMMENDATION

**For your use case ([DESCRIZ USE CASE]):**

🏆 **Winner:** [Approach X]

**Rationale:**
[Spiegazione dettagliata perché questo è best per il caso specifico]

**Runner-up:** [Approach Y] - Consider if [condizione]

## CODE COMPARISON

```c
// Side-by-side comparison of key parts

// Approach A        | // Approach B
[code_a]            | [code_b]
[...]               | [...]
```

## REAL-WORLD USAGE

- **Approach A** è usato in: [progetti famosi]
- **Approach B** è usato in: [progetti famosi]
- **Approach C** è usato in: [progetti famosi]
```

---

---

# 9. CASI SPECIALI

---

## 9.1 Template: Arduino/Embedded Specific 🟡

### Descrizione
Prompt ottimizzati per programmazione Arduino/embedded.

### Template

```
Genera codice Arduino per [TASK].

**HARDWARE**
- Board: [Arduino Uno / Mega / Nano / ESP32 / etc]
- Componenti: [sensori, attuatori, etc]
- Pin assignment: [lista pin usati]

**VINCOLI EMBEDDED**
- RAM disponibile: [2KB / 8KB / etc]
- Flash memory: [32KB / etc]
- Clock speed: [16MHz / etc]

**TASK**
[Descrizione cosa deve fare]

**CODICE RICHIESTO**

```cpp
// Vincoli specifici embedded:
// - NO dynamic allocation (no malloc/new in loop())
// - NO String class (usa char arrays)
// - NO delay() per timing critico (usa millis())
// - Minimizza uso RAM (const, PROGMEM per string)

// Configurazione pin
#define [PIN_NAME] [numero]

// Variabili globali
[dichiarazioni global con commenti perché global]

void setup() {
    // Setup eseguito una volta
    Serial.begin(9600);

    // Pin mode
    pinMode([PIN], [INPUT/OUTPUT]);

    [altra inizializzazione]
}

void loop() {
    // Loop infinito

    // NON USARE delay() se serve responsiveness
    // Usa pattern millis() invece:

    static unsigned long previousMillis = 0;
    const unsigned long interval = 1000; // ms

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Azione periodica qui
        [...]
    }

    // Altre azioni non-blocking
    [...]
}

// Helper functions
[funzioni ausiliarie]
```

**BEST PRACTICES EMBEDDED**

1. **Memory optimization:**
```cpp
// BAD - spreca RAM
String msg = "Hello"; // String object dinamico

// GOOD - usa flash
const char msg[] PROGMEM = "Hello";
```

2. **Non-blocking timing:**
```cpp
// BAD - blocca tutto
delay(1000);
Serial.println("1 sec passed");

// GOOD - non-blocking
if (millis() - lastTime >= 1000) {
    lastTime = millis();
    Serial.println("1 sec passed");
}
```

3. **Debouncing:**
```cpp
// Button debounce pattern
#define DEBOUNCE_DELAY 50

int buttonState;
int lastButtonState = LOW;
unsigned long lastDebounceTime = 0;

int reading = digitalRead(BUTTON_PIN);

if (reading != lastButtonState) {
    lastDebounceTime = millis();
}

if ((millis() - lastDebounceTime) > DEBOUNCE_DELAY) {
    if (reading != buttonState) {
        buttonState = reading;
        // Azione su cambio stato
    }
}

lastButtonState = reading;
```

**TESTING**

Specifica come testare:
- Senza hardware (simulatore Wokwi?)
- Con hardware (procedura step-by-step)
- Expected serial output

**POWER CONSUMPTION** (se applicabile)

Tecniche per ridurre consumo:
- Sleep modes
- Pin stati
```

---

## 9.2 Template: Multi-threading 🔴

### Descrizione
Codice multi-thread con gestione sincronizzazione.

### Template

```
Implementa soluzione multi-threaded per [PROBLEMA].

**PROBLEMA**
[Descrizione task parallelo]

**ARCHITECTURE**

Threads:
1. **Thread 1**: [responsabilità]
2. **Thread 2**: [responsabilità]
3. **Thread N**: [responsabilità]

Shared resources:
- [Resource A]: [tipo, accesso read/write]
- [Resource B]: [tipo, accesso read/write]

**THREADING MODEL**

```c
#include <pthread.h>
#include <stdio.h>

// Shared data structure
typedef struct {
    [campi dati condivisi]
    pthread_mutex_t lock;     // Protegge accesso
    pthread_cond_t condition; // Sincronizzazione
} SharedData;

// Thread function signatures
void* thread_func_1(void* arg);
void* thread_func_2(void* arg);

// Global shared data (oppure passato via arg)
SharedData shared;

int main() {
    pthread_t tid1, tid2;

    // Initialize mutex and condition
    pthread_mutex_init(&shared.lock, NULL);
    pthread_cond_init(&shared.condition, NULL);

    // Create threads
    pthread_create(&tid1, NULL, thread_func_1, &shared);
    pthread_create(&tid2, NULL, thread_func_2, &shared);

    // Wait for threads
    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    // Cleanup
    pthread_mutex_destroy(&shared.lock);
    pthread_cond_destroy(&shared.condition);

    return 0;
}

void* thread_func_1(void* arg) {
    SharedData *data = (SharedData*)arg;

    while ([condition]) {
        // Lock before accessing shared data
        pthread_mutex_lock(&data->lock);

        // Critical section
        [accesso dati condivisi]

        // Signal other threads if needed
        pthread_cond_signal(&data->condition);

        // Unlock
        pthread_mutex_unlock(&data->lock);

        // Non-critical work
        [lavoro locale]
    }

    return NULL;
}

void* thread_func_2(void* arg) {
    SharedData *data = (SharedData*)arg;

    while ([condition]) {
        pthread_mutex_lock(&data->lock);

        // Wait for condition
        while (![condition_to_proceed]) {
            pthread_cond_wait(&data->condition, &data->lock);
        }

        // Critical section
        [...]

        pthread_mutex_unlock(&data->lock);
    }

    return NULL;
}
```

**SYNCHRONIZATION PATTERNS**

### Producer-Consumer with condition variable
```c
// Producer
pthread_mutex_lock(&lock);
buffer[in] = item;
in = (in + 1) % SIZE;
count++;
pthread_cond_signal(&not_empty);
pthread_mutex_unlock(&lock);

// Consumer
pthread_mutex_lock(&lock);
while (count == 0) {
    pthread_cond_wait(&not_empty, &lock);
}
item = buffer[out];
out = (out + 1) % SIZE;
count--;
pthread_cond_signal(&not_full);
pthread_mutex_unlock(&lock);
```

### Read-Write Lock
```c
pthread_rwlock_t rwlock;

// Readers (multiple concurrent OK)
pthread_rwlock_rdlock(&rwlock);
[read shared data]
pthread_rwlock_unlock(&rwlock);

// Writer (exclusive)
pthread_rwlock_wrlock(&rwlock);
[write shared data]
pthread_rwlock_unlock(&rwlock);
```

**COMMON PITFALLS**

### Race Condition
```c
// BAD - race condition
shared_counter++; // Non atomico!

// GOOD
pthread_mutex_lock(&lock);
shared_counter++;
pthread_mutex_unlock(&lock);
```

### Deadlock
```c
// BAD - possible deadlock
Thread 1:                    Thread 2:
  lock(A)                      lock(B)
  lock(B) // wait forever      lock(A) // wait forever

// GOOD - consistent lock order
Always lock in order: A then B
```

**TESTING**

Specific multi-threading tests:
- Thread sanitizer: `gcc -fsanitize=thread`
- Valgrind helgrind: `valgrind --tool=helgrind ./program`
- Stress test (run many iterations)

**COMPILE**
```bash
gcc -pthread program.c -o program
```
```

---

---

# 10. PROMPT COMPOSITI

---

## 10.1 Template: Progetto Completo Multi-Step 🔴

### Descrizione
Prompt per guidare IA attraverso progetto completo in step.

### Template

```
Guidami nell'implementazione completa di [PROGETTO] attraverso step incrementali.

**PROGETTO OVERVIEW**
[Descrizione cosa vogliamo costruire]

**TARGET**
- Utente finale: [chi]
- Platform: [OS/embedded/web]
- Requisiti chiave: [lista]

**WORKFLOW MULTI-STEP**

Segui questo workflow step-by-step, aspettando mio feedback tra ogni step:

---

## STEP 1: Requirements Analysis (non scrivere codice ancora)

**Task:** Analizza requisiti e crea lista strutturata.

Output richiesto:
```markdown
# Requirements - [PROGETTO]

## Functional Requirements
1. [REQ-001] [descrizione]
   - Priority: High/Medium/Low
   - Complexity: Simple/Medium/Complex

2. [REQ-002] ...

## Non-Functional Requirements
1. Performance: [vincoli]
2. Memory: [vincoli]
3. Security: [vincoli]
4. Usability: [vincoli]

## Out of Scope (cosa NON faremo)
- [Feature futura 1]
- [Feature futura 2]
```

**Wait for my approval before proceeding.**

---

## STEP 2: Architecture Design

**Task:** Proponi architettura modulare.

Output richiesto:
```markdown
# Architecture Design

## Module Breakdown

### Module 1: [Nome]
- **Responsibility:** [cosa fa]
- **Files:** [file.c, file.h]
- **Dependencies:** [altri moduli]
- **Public API:**
  ```c
  [prototipi funzioni pubbliche]
  ```

### Module 2: [Nome]
[...]

## Data Structures

```c
// Core structures
[definizioni struct chiave]
```

## Data Flow Diagram

```
[ASCII diagram mostrando flusso tra moduli]
```

## Build System

[Makefile structure proposto]
```

**Wait for my approval before proceeding.**

---

## STEP 3: Implement Module 1

**Task:** Implementa primo modulo [NOME].

Include:
- Header file (.h)
- Implementation (.c)
- Unit tests
- Example usage

**Wait for my feedback on Module 1 before proceeding.**

---

## STEP 4: Implement Module 2

[Simile a Step 3]

---

[Continua per tutti i moduli]

---

## STEP N: Integration

**Task:** Integra tutti i moduli.

Include:
- Main program che usa tutti i moduli
- Integration tests
- End-to-end test

---

## STEP N+1: Testing & Validation

**Task:** Testing completo.

Include:
- Valgrind check
- Edge case testing
- Performance benchmark

---

## STEP N+2: Documentation

**Task:** Documentazione finale.

Include:
- README.md completo
- Doxygen comments
- User guide
- Architecture document

---

## STEP N+3: Final Review

**Task:** Code review completo.

Checklist finale + eventuali fix.

---

**IMPORTANT:**
- Dopo ogni step, aspetta mio "OK" prima di procedere al successivo
- Se qualche step non è chiaro, chiedi chiarimenti
- Se voglio modificare qualcosa di uno step precedente, torniamo indietro
```

---

## 10.2 Template: Iterative Refinement 🟡

### Descrizione
Prompt che guida iterazioni successive.

### Template

```
Implementa [FEATURE] usando approccio iterativo TDD-like.

**ITERAZIONE 1: Simplest Possible**

Output V1:
```c
// Versione più semplice che funziona
// Può anche essere hardcoded
[codice minimal]
```

**Feedback atteso da me:** [cosa dovrei testare/validare]

---

**ITERAZIONE 2: Add Core Logic**

Based on my feedback, migliora V1:

Output V2:
```c
// Logica reale, non più hardcoded
// Gestisce happy path
[codice migliorato]
```

**Changes from V1:**
- [Change 1]
- [Change 2]

**Feedback atteso:** [cosa testare]

---

**ITERAZIONE 3: Error Handling**

Aggiungi gestione errori robusta:

Output V3:
```c
// Gestione errori completa
[codice con error handling]
```

**Changes from V2:**
- [Change 1]
- [Change 2]

---

**ITERAZIONE 4: Optimization**

Ottimizza performance/memoria se necessario:

Output V4:
```c
// Versione ottimizzata
[codice finale]
```

**Optimizations applied:**
- [Opt 1]: [impatto]
- [Opt 2]: [impatto]

---

**FINAL VERSION COMPARISON**

| Version | Lines | Complexity | Features | Performance |
|---------|-------|------------|----------|-------------|
| V1 | [n] | Simple | Minimal | Baseline |
| V2 | [n] | Medium | Core | 1x |
| V3 | [n] | Medium | + Errors | 1x |
| V4 | [n] | Medium | Full | 1.5x |

**Evolution Learnings:**
[Cosa ho imparato dall'approccio iterativo]
```

---

**Fine BIBLIOTECA_PROMPT.md**

---

## 📝 COME CONTRIBUIRE

Questa biblioteca è viva! Se hai template utili che usi spesso:

1. Testa il template (assicurati funzioni bene)
2. Documenta con esempio
3. Aggiungi alla categoria appropriata
4. [Condividi con la community se vuoi]

---

## 📚 RISORSE CORRELATE

- [Lezione 2](./02_LEZIONE_2.md) - Framework CLEAR e tecniche prompt
- [Lezione 3](./03_LEZIONE_3.md) - Sicurezza codice
- [Lezione 4](./04_LEZIONE_4.md) - Documentazione e Git
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

---

## ❓ FAQ

**Q: Devo usare esattamente questi template?**
A: No! Usa come punto di partenza, customizza per le tue esigenze.

**Q: Posso combinare template?**
A: Assolutamente! Ad esempio, usa "Funzione Base" + "Unit Test".

**Q: Quale LLM usare?**
A: Funzionano con tutti (ChatGPT, Claude, Gemini). Alcuni richiedono modelli avanzati (GPT-4, Claude Opus).

**Q: I template funzionano anche per altri linguaggi?**
A: Sì, ma sono ottimizzati per C. Adattali per Python/Java/ecc.

---

**🎉 Buon Coding con l'IA! 🚀**

**Ricorda:** Questi template sono tools. La tua creatività, critical thinking e validazione rimangono essenziali!

---

**Versione:** 1.0
**Ultima modifica:** Gennaio 2025
**Licenza:** CC BY-NC-SA 4.0
**Autore:** Materiale didattico ITS
