# 📘 LEZIONE 5: PROGETTO FINALE INTEGRATO
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Durata:** 2 ore
**Struttura:** 100% pratica hands-on
**Livello:** Avanzato (integrazione)
**Prerequisiti:** Lezioni 1-4 completate

---

## 🎯 Obiettivi della Lezione

Al termine di questa lezione sarai in grado di:

✅ **Implementare** un progetto completo end-to-end con IA
✅ **Integrare** tutte le competenze apprese (prompt engineering, C sicuro, Git, documentazione)
✅ **Applicare** workflow professionale completo
✅ **Creare** un progetto portfolio-ready
✅ **Presentare** il lavoro in modo professionale
✅ **Debuggare** e validare sistematicamente

---

## 📋 Struttura della Lezione

**100% PRATICA INTEGRATA (120 minuti)**

1. **Scelta e Setup Progetto** (15 min)
   - Scegli tra 4 progetti proposti
   - Setup repository e struttura
   - Definisci MVP (Minimum Viable Product)

2. **Implementazione Core** (60 min)
   - Design architettura con IA
   - Implementazione moduli principali
   - Testing continuo

3. **Testing e Validazione** (20 min)
   - Test sistematico
   - Valgrind verification
   - Edge cases

4. **Documentazione Finale** (15 min)
   - README completo
   - Commenti Doxygen
   - User guide

5. **Presentazione** (10 min)
   - Demo progetto
   - Discussione scelte tecniche
   - Lessons learned

---

---

# PROGETTI DISPONIBILI

---

## PROGETTO 1: STUDENT MANAGEMENT SYSTEM 🎓

### Descrizione

Sistema di gestione studenti per scuola/università. Gestisce studenti, corsi, iscrizioni, voti e genera statistiche.

### Features Core (MVP)

**Must Have:**
- Aggiungere/rimuovere studenti (nome, matricola, email)
- Aggiungere corsi (nome, codice, crediti)
- Iscrivere studente a corso
- Registrare voti (0-30)
- Visualizzare elenco studenti/corsi
- Calcolare media voti per studente
- Persistenza su file

**Should Have (se c'è tempo):**
- Generare pagella studente
- Statistiche corso (media classe, distribuzione voti)
- Ricerca studenti/corsi
- Export CSV

### Strutture Dati Suggerite

```c
typedef struct {
    int id;
    char name[100];
    char email[100];
    int enrollment_year;
} Student;

typedef struct {
    char code[10];        // es: "PROG101"
    char name[100];
    int credits;
} Course;

typedef struct {
    int student_id;
    char course_code[10];
    int grade;            // 0-30
    char date[11];        // YYYY-MM-DD
} Enrollment;

typedef struct {
    Student *students;
    size_t student_count;
    size_t student_capacity;
} StudentDB;

// ... simile per Course e Enrollment
```

### Difficoltà
⭐⭐⭐ (Media)

### Skills Dimostrate
- Gestione multiple strutture dati complesse
- Relazioni tra entità (student-course N:M)
- Calcoli statistici
- Report generation

---

## PROGETTO 2: DATA LOGGER & ANALYZER 📊

### Descrizione

Sistema che legge dati da sensori simulati (file CSV o generati random), li analizza e genera report.

### Features Core (MVP)

**Must Have:**
- Leggere dati da CSV (timestamp, sensor_id, value)
- Memorizzare in struttura dati efficiente
- Calcolare statistiche: min, max, media, deviazione standard
- Rilevare anomalie (valori fuori soglia)
- Generare report testuale
- Visualizzazione dati (ASCII chart)

**Should Have:**
- Export dati filtrati
- Multiple sensors support
- Aggregazione temporale (oraria, giornaliera)

### Strutture Dati Suggerite

```c
typedef struct {
    time_t timestamp;
    int sensor_id;
    double value;
} DataPoint;

typedef struct {
    DataPoint *points;
    size_t count;
    size_t capacity;
} TimeSeries;

typedef struct {
    double min;
    double max;
    double mean;
    double std_dev;
    int anomaly_count;
} Statistics;
```

### Esempio CSV Input

```csv
timestamp,sensor_id,value
2025-01-15 10:00:00,1,23.5
2025-01-15 10:01:00,1,23.8
2025-01-15 10:02:00,1,24.1
2025-01-15 10:03:00,1,55.0
2025-01-15 10:04:00,1,23.9
```

### Esempio Output

```
===== SENSOR DATA ANALYSIS =====

Sensor ID: 1
Period: 2025-01-15 10:00 - 10:04
Samples: 5

Statistics:
  Min: 23.5°C
  Max: 55.0°C
  Mean: 30.06°C
  Std Dev: 12.8

Anomalies Detected: 1
  - 2025-01-15 10:03:00: 55.0°C (spike +131% from mean)

Visualization (last 24h):
60°C │           ●
50°C │
40°C │
30°C │    ●  ●     ●
20°C │  ●
     └─────────────────────
      10h 11h 12h 13h 14h
```

### Difficoltà
⭐⭐⭐⭐ (Media-Alta)

### Skills Dimostrate
- File parsing (CSV)
- Time series data management
- Statistical algorithms
- ASCII visualization
- Anomaly detection

---

## PROGETTO 3: COMMAND-LINE TODO MANAGER ✅

### Descrizione

Todo list avanzata con priorità, categorie, ricerca e statistiche produttività.

### Features Core (MVP)

**Must Have:**
- Add task (title, description, priority, category)
- List tasks (all, pending, completed)
- Complete task
- Delete task
- Persistenza file
- Interfaccia interattiva (menu)

**Should Have:**
- Filtrare per priorità/categoria
- Ricerca per keyword
- Deadline support
- Statistiche produttività (completed per day/week)

### Strutture Dati Suggerite

```c
typedef enum {
    PRIORITY_LOW,
    PRIORITY_MEDIUM,
    PRIORITY_HIGH
} Priority;

typedef enum {
    STATUS_PENDING,
    STATUS_COMPLETED,
    STATUS_CANCELLED
} Status;

typedef struct {
    int id;
    char title[200];
    char description[500];
    Priority priority;
    Status status;
    char category[50];
    time_t created_at;
    time_t completed_at;
    time_t deadline;      // 0 se nessuna deadline
} Task;

typedef struct {
    Task *tasks;
    size_t count;
    size_t capacity;
} TaskList;
```

### Esempio UI

```
===== TODO MANAGER =====

1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Filter by Priority
6. Search
7. Statistics
8. Exit

Choice: 2

===== TASK LIST =====
┌────┬──────────────────────────────────┬──────────┬────────────┐
│ ID │ Title                            │ Priority │ Status     │
├────┼──────────────────────────────────┼──────────┼────────────┤
│ 1  │ Studiare per esame C             │ HIGH     │ Pending    │
│ 2  │ Comprare latte                   │ LOW      │ Completed  │
│ 3  │ Finire progetto ITS              │ HIGH     │ Pending    │
└────┴──────────────────────────────────┴──────────┴────────────┘

Total: 3 tasks (2 pending, 1 completed)
```

### Difficoltà
⭐⭐ (Bassa-Media)

### Skills Dimostrate
- CLI interface design
- Enum usage
- Time handling
- Filtering algorithms
- User experience

---

## PROGETTO 4: CONFIG FILE PARSER 🔧

### Descrizione

Parser e validator per file di configurazione custom format (stile INI o YAML semplificato).

### Features Core (MVP)

**Must Have:**
- Parsing file config custom format
- Supporto sezioni [Section]
- Supporto key=value
- Supporto commenti (#)
- Validazione sintassi
- API per query config (get_value, get_section)
- Error reporting dettagliato (linea errore)

**Should Have:**
- Type validation (int, string, bool)
- Default values
- Config merging (override)
- Export to JSON/XML

### Esempio Config Format

```ini
# Database Configuration
[database]
host = localhost
port = 5432
username = admin
# password = secret123  # commented out
max_connections = 100
enable_logging = true

[server]
bind_address = 0.0.0.0
port = 8080
workers = 4

[features]
enable_cache = true
cache_ttl = 3600
```

### Strutture Dati Suggerite

```c
typedef struct {
    char key[100];
    char value[200];
} ConfigEntry;

typedef struct {
    char name[100];
    ConfigEntry *entries;
    size_t entry_count;
} ConfigSection;

typedef struct {
    ConfigSection *sections;
    size_t section_count;
} Config;
```

### Esempio API Usage

```c
Config *cfg = config_load("app.conf");

// Query values
const char *host = config_get(cfg, "database", "host");
int port = config_get_int(cfg, "database", "port");
bool logging = config_get_bool(cfg, "database", "enable_logging");

// Validate
if (config_validate(cfg, schema) != 0) {
    config_print_errors(cfg);
}

config_free(cfg);
```

### Difficoltà
⭐⭐⭐⭐⭐ (Alta)

### Skills Dimostrate
- Text parsing
- Lexical analysis
- Error handling robusto
- API design
- String manipulation avanzata

---

---

# WORKFLOW IMPLEMENTAZIONE

---

## FASE 1: SETUP E DESIGN (15 minuti)

### Step 1.1: Scelta Progetto

**Scegli UN progetto tra i 4 proposti.**

**Criteri decisione:**
- ⏱️ Tempo disponibile (2 ore)
- 🎯 Interesse personale
- 📊 Skills che vuoi dimostrare
- 🏆 Portfolio value

**Consiglio:** Se sei incerto, scegli **PROGETTO 3 (TODO Manager)** - è bilanciato tra complessità e tempo.

### Step 1.2: Setup Repository

```bash
# Crea directory progetto
mkdir my-project
cd my-project

# Inizializza Git
git init

# Crea .gitignore
cat > .gitignore << EOF
*.o
*.exe
*.out
build/
.vscode/
*.swp
EOF

# Crea struttura base
mkdir src
mkdir include
mkdir tests

# Primo commit
git add .
git commit -m "Initial commit: Project structure"
```

### Step 1.3: Definisci MVP con IA

**Prompt per IA:**

```
Progetto scelto: [NOME PROGETTO]

Aiutami a definire un MVP realistico implementabile in 90 minuti.

Contesto:
- Sono studente ITS, livello intermedio in C
- Ho già struttura progetto pronta
- Userò IA per generare boilerplate
- Priorità: funzionalità core working, non polish

Fornisci:
1. Lista features MVP (must-have only, max 5)
2. Strutture dati essenziali
3. Moduli da implementare (ordine priorità)
4. Stima tempo per modulo
5. Punti rischio (cosa potrebbe rallentare)

Output in formato checklist.
```

**Salva output in `MVP.md`**

### Step 1.4: Design Architettura

**Prompt per IA:**

```
Per il mio progetto [NOME] con MVP:
[incolla features MVP]

Genera:
1. Architettura modulare (quali file .c/.h)
2. Strutture dati complete in C
3. Firma funzioni pubbliche principali (solo prototipi)
4. Diagramma dipendenze moduli

Vincoli:
- C99
- Massima semplicità (no over-engineering)
- Memory-safe by design
- Testabile

Format output:
- Codice C per struct
- Lista file con responsabilità
- Include guards negli header
```

**Salva struct e prototipi in file header appropriati.**

### Step 1.5: Commit Design

```bash
git add MVP.md src/ include/
git commit -m "docs: Add MVP definition and architecture design"
```

---

## FASE 2: IMPLEMENTAZIONE CORE (60 minuti)

### Strategia Implementazione

**Ordine consigliato:**

```
1. Strutture dati + allocazione/free (15 min)
   ↓
2. Persistenza (load/save) (15 min)
   ↓
3. Operazioni core (20 min)
   ↓
4. UI/Menu (10 min)
```

**Regole d'oro:**
- ✅ **Compila dopo ogni modulo** (catch errori subito)
- ✅ **Testa incrementalmente** (non tutto alla fine)
- ✅ **Commit frequenti** (ogni 15-20 min)
- ✅ **Chiedi all'IA** quando bloccato (non perdere tempo)

### 2.1 Implementare Strutture Dati (15 min)

**Prompt template:**

```
Implementa queste strutture dati complete:

[incolla struct dal design]

Includi funzioni:
- create: alloca e inizializza
- free: libera memoria (no leak)
- add: aggiungi elemento (con resize automatico)
- remove: rimuovi elemento
- find: cerca elemento

Requisiti:
- Controllo NULL su tutti i parametri
- Controllo malloc failures
- Dynamic array che si espande
- Codice memory-safe (Valgrind clean)
- Commenti Doxygen

File: [nome].h e [nome].c
```

**Implementa, compila, testa:**

```bash
# Compila
gcc -Wall -Wextra -g -c src/data.c -I include/

# Se compila OK, commit
git add src/data.c include/data.h
git commit -m "feat: Implement core data structures"
```

### 2.2 Implementare Persistenza (15 min)

**Prompt template:**

```
Implementa modulo storage per salvare/caricare dati su file.

Strutture: [lista struct da salvare]
Formato file: CSV (semplice parsing)

Funzioni:
- int save_to_file(const char *filename, DataStruct *data)
- int load_from_file(const char *filename, DataStruct *data)

Requisiti:
- Gestione errori (file not found, permission denied)
- CSV format: header + data rows
- Proper escaping (se string con virgole)
- Validazione durante load (skip linee malformate)

Error handling:
- Return 0 success, -1 error
- Log errori su stderr

File: storage.c, storage.h
```

**Test manuale:**

```bash
# Crea file test dati
# Testa load
# Testa save
# Verifica file generato è valido
```

**Commit:**

```bash
git add src/storage.c include/storage.h
git commit -m "feat: Add file persistence (CSV format)"
```

### 2.3 Implementare Operazioni Core (20 min)

**Per ogni operazione core (es: add, remove, list, complete):**

**Prompt template:**

```
Implementa la funzione [NOME_OPERAZIONE]:

Signature: [firma funzione]

Comportamento:
- [descrizione dettagliata]

Input validation:
- [vincoli parametri]

Output:
- [cosa ritorna, side effects]

Edge cases:
- [casi limite da gestire]

Esempio uso:
- [snippet di esempio]

Include error handling e commenti Doxygen.
```

**Workflow:**

```
Implementa operazione 1
  ↓
Compila
  ↓
Test veloce manuale
  ↓
Fix eventuali bug
  ↓
Commit
  ↓
Ripeti per operazione 2, 3, ...
```

**Commit example:**

```bash
git commit -m "feat: Add task creation with validation"
git commit -m "feat: Implement task listing with filters"
git commit -m "feat: Add task completion functionality"
```

### 2.4 Implementare UI/Menu (10 min)

**Prompt per interfaccia:**

```
Genera interfaccia menu interattiva per CLI app.

Operazioni disponibili:
1. [operazione 1]
2. [operazione 2]
3. [operazione 3]
...
N. Exit

Requirements:
- Loop infinito fino a exit
- Input validation (scelta non valida → richiedi)
- Clear screen tra operazioni (opzionale)
- User-friendly prompts
- Error messages chiari

Stile:
┌─────────────────────┐
│   APP NAME          │
├─────────────────────┤
│ 1. Option 1         │
│ 2. Option 2         │
│ ...                 │
└─────────────────────┘

File: ui.c, ui.h, main.c
```

**Test UI:**

```bash
# Compila tutto
gcc -Wall -Wextra -g src/*.c -I include/ -o myapp

# Testa UI
./myapp

# Verifica tutti i menu funzionano
```

**Commit:**

```bash
git add src/ui.c include/ui.h src/main.c
git commit -m "feat: Add interactive CLI menu"
```

---

## FASE 3: TESTING E VALIDAZIONE (20 minuti)

### 3.1 Test Sistematico Funzionalità

**Checklist test funzionali:**

**Per ogni operazione core:**

- [ ] **Happy path:** Input normale → output corretto
- [ ] **Edge case:** Input limite (vuoto, NULL, max size)
- [ ] **Error handling:** Input invalido → errore gestito
- [ ] **Persistenza:** Dati salvati → reload → dati identici

**Esempio test TODO app:**

```bash
# Test Add
./myapp
> 1 (Add Task)
> "Test task"
> High priority
→ Verifica: task aggiunto in lista

# Test Persistenza
> 8 (Exit)
./myapp (riapri)
> 2 (List)
→ Verifica: task precedente ancora presente

# Test Complete
> 3 (Complete task)
> 1
> 2 (List)
→ Verifica: task marcato completed

# Test Edge Case
> 1 (Add)
> "" (empty title)
→ Verifica: errore "Title cannot be empty"
```

### 3.2 Valgrind Check

**Memory leak verification:**

```bash
# Compila con debug symbols
gcc -g -Wall -Wextra src/*.c -I include/ -o myapp

# Valgrind full check
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./myapp

# Interagisci con app (test vari workflow)
# ...
# Exit

# Verifica output Valgrind:
# HEAP SUMMARY:
#   in use at exit: 0 bytes in 0 blocks  ← DEVE essere 0!
#   total heap usage: N allocs, N frees   ← allocs == frees
#
# All heap blocks were freed -- no leaks are possible  ← PERFETTO!
```

**Se Valgrind trova leak:**

1. Identifica quale malloc non ha free corrispondente
2. Usa prompt IA:

```
Valgrind ha trovato memory leak:

[incolla output Valgrind]

Codice sospetto:
[incolla funzione indicata]

Analizza e suggerisci fix.
```

3. Applica fix, ricompila, ritesta

### 3.3 Edge Cases

**Test casi limite:**

```c
// Test con struct vuota
TaskList *empty_list = task_list_create();
task_list_print(empty_list);  // Non deve crashare

// Test con input NULL
task_add(NULL, "Title");  // Deve ritornare errore, non crashare
task_add(list, NULL);     // Deve ritornare errore

// Test con input molto grande
char long_title[10000];
memset(long_title, 'A', 9999);
long_title[9999] = '\0';
task_add(list, long_title);  // Deve troncare o gestire

// Test con file non esistente
load_from_file("nonexistent.csv", list);  // Deve gestire errore
```

### 3.4 Fix e Commit

**Ogni bug trovato:**

```bash
# Fix bug
# Verifica fix funziona
git add [files modificati]
git commit -m "fix: [descrizione bug fixato]"
```

**Esempio:**

```bash
git commit -m "fix: Prevent segfault on empty task list print"
git commit -m "fix: Add NULL check in task_add()"
git commit -m "fix: Free title string in task_free() (memory leak)"
```

---

## FASE 4: DOCUMENTAZIONE (15 minuti)

### 4.1 README.md Completo

**Genera con IA:**

```
Genera README.md professionale per questo progetto:

Nome: [nome progetto]
Descrizione: [breve descrizione]
Features implementate:
- [feature 1]
- [feature 2]
...

Tecnologie: C99, Make, CSV

Include sezioni:
- Overview (con emoji)
- Features
- Installation (compilazione)
- Usage (esempi comandi)
- Project Structure (tree files)
- Testing (come testare)
- Known Issues (se ci sono)
- Future Improvements
- Author

Stile: Professionale ma friendly, con emoji appropriati.
```

**Customizza output IA con dettagli specifici.**

### 4.2 Commenti Finali

**Assicurati che ogni funzione pubblica abbia Doxygen comment:**

```c
/**
 * @brief [breve descrizione]
 * @param [nome] [descrizione]
 * @return [descrizione]
 */
```

**Usa IA per generare velocemente:**

```
Genera commento Doxygen per queste funzioni:

[incolla funzioni senza commenti]
```

### 4.3 Commit Documentazione

```bash
git add README.md src/ include/
git commit -m "docs: Add comprehensive README and code comments"
```

### 4.4 Tag Release

```bash
# Crea tag versione 1.0
git tag -a v1.0.0 -m "First release - MVP complete

Features:
- [lista features]

Tested:
- Functional tests passed
- Valgrind clean (no leaks)
- Edge cases handled
"

# Push tag (se hai remote)
git push origin v1.0.0
```

---

## FASE 5: PRESENTAZIONE (10 minuti)

### 5.1 Preparare Demo

**Script di demo (cosa mostrare):**

1. **Overview (30 sec)**
   - "Ho sviluppato [nome progetto], un [descrizione]"
   - "Risolve il problema di [problema]"

2. **Live Demo (2 min)**
   - Avvia applicazione
   - Mostra 2-3 operazioni core
   - Evidenzia feature interessante

3. **Code Walkthrough (1 min)**
   - Mostra architettura (tree files)
   - Evidenzia modulo più interessante
   - Spiega scelta design chiave

4. **Quality Assurance (1 min)**
   - Mostra Valgrind output (0 leaks)
   - Mostra README.md
   - Mostra git log (commit significativi)

5. **Q&A e Lessons Learned (5 min)**
   - Cosa è andato bene
   - Cosa rifaresti diversamente
   - Come l'IA ha aiutato

### 5.2 Domande Tipiche (Preparati)

**Domanda:** "Perché hai scelto questo progetto?"
**Risposta:** [motivazione personale + skills dimostrate]

**Domanda:** "Qual è stata la parte più difficile?"
**Risposta:** [challenge tecnico + come l'hai risolto]

**Domanda:** "Come hai usato l'IA?"
**Risposta:** [esempi concreti: boilerplate, debugging, doc]

**Domanda:** "Qual è il prossimo miglioramento che faresti?"
**Risposta:** [feature should-have non implementata + perché importante]

### 5.3 Self-Evaluation Checklist

**Valuta il tuo progetto:**

**Funzionalità:** ⭐⭐⭐⭐⭐
- [ ] Tutte features MVP implementate
- [ ] App funziona end-to-end
- [ ] Edge cases gestiti
- [ ] Error handling robusto

**Qualità Codice:** ⭐⭐⭐⭐⭐
- [ ] Compila senza warning
- [ ] Valgrind clean (0 leak)
- [ ] Codice ben organizzato
- [ ] Naming consistente

**Documentazione:** ⭐⭐⭐⭐⭐
- [ ] README completo e chiaro
- [ ] Commenti appropriati
- [ ] API documentata

**Git Workflow:** ⭐⭐⭐⭐⭐
- [ ] Commit frequenti e significativi
- [ ] Commit messages descrittivi
- [ ] History pulita

**Voto globale:** ___ / 20

---

---

# TROUBLESHOOTING COMUNE

---

## Problema 1: "Non riesco a compilare"

**Sintomi:**
```
gcc: error: ...
undefined reference to ...
```

**Soluzioni:**

**Step 1:** Verifica command line

```bash
# Corretto:
gcc -Wall -Wextra -g src/*.c -I include/ -o myapp

# Elementi chiave:
# -I include/  ← dice dove trovare header
# src/*.c      ← compila tutti .c in src/
# -o myapp     ← nome output
```

**Step 2:** Verifica include guards

```c
// In ogni header
#ifndef NOME_H
#define NOME_H

// ... contenuto ...

#endif
```

**Step 3:** Chiedi all'IA

```
Ho questo errore di compilazione:

[incolla errore completo]

File coinvolti:
[lista file]

Come posso fixare?
```

## Problema 2: "Segmentation Fault"

**Debugging:**

```bash
# Compila con debug
gcc -g ...

# Run con GDB
gdb ./myapp

# In GDB:
(gdb) run
[... crash ...]
(gdb) backtrace  # Mostra dove è crashato
(gdb) print variable  # Ispeziona variabile
```

**Oppure chiedi IA:**

```
La mia app crasha con segfault quando [azione che causa crash].

Backtrace GDB:
[incolla backtrace]

Codice funzione sospetta:
[incolla funzione]

Dove potrebbe essere il bug?
```

## Problema 3: "Valgrind Trova Leak"

**Interpretare output:**

```
==12345== 400 bytes in 1 blocks are definitely lost
==12345==    at malloc (...)
==12345==    by create_task (task.c:15)
==12345==    by main (main.c:42)
```

**Significa:**
- 400 byte non liberati
- Allocati in `create_task()` linea 15
- Chiamato da `main()` linea 42

**Fix:**
1. Trova il `malloc` a task.c:15
2. Verifica che esista `free` corrispondente
3. Aggiungi `free` mancante

## Problema 4: "Non Ho Tempo"

**Priorità:**

Se ti rimangono solo 30 minuti:

1. ✅ **Funzionalità base working** (70% tempo)
2. ✅ **Fix crash e leak critici** (20% tempo)
3. ✅ **README minimo** (10% tempo)

**Non fare:**
- ❌ Feature "nice to have"
- ❌ Refactoring estetico
- ❌ UI polish

**Fai:**
- ✅ MVP che funziona
- ✅ Codice che non crasha
- ✅ README che spiega cosa fa

---

---

# CHECKLIST FINALE

---

## Prima di Considerare "Finito"

### ✅ Funzionalità

- [ ] Tutte features MVP implementate
- [ ] App avvia senza errori
- [ ] Workflow completo funziona end-to-end
- [ ] Dati persistono correttamente (save/load)
- [ ] Edge cases gestiti (non crash con input strani)

### ✅ Qualità Codice

- [ ] Compila con `gcc -Wall -Wextra -Werror`
- [ ] Valgrind reports: "All heap blocks were freed"
- [ ] Nessun warning ignorato
- [ ] Codice organizzato in moduli logici
- [ ] Naming consistente

### ✅ Testing

- [ ] Testato happy path (uso normale)
- [ ] Testato edge cases (empty, NULL, max size)
- [ ] Testato error handling (input invalido)
- [ ] Testato persistenza (save → exit → load → data OK)

### ✅ Documentazione

- [ ] README.md presente e completo:
  - [ ] Overview chiaro
  - [ ] Installation instructions
  - [ ] Usage examples
  - [ ] Project structure
- [ ] Commenti Doxygen su funzioni pubbliche
- [ ] Commenti inline dove necessario (WHY not WHAT)

### ✅ Git

- [ ] Repository inizializzato
- [ ] Almeno 5 commit significativi
- [ ] Commit messages descrittivi
- [ ] .gitignore appropriato
- [ ] Tagged release (v1.0.0)

### ✅ Presentation Ready

- [ ] Demo script preparato
- [ ] Può spiegare scelte architetturali
- [ ] Può discutere challenges e solutions
- [ ] Può mostrare Valgrind clean

---

---

# ESEMPI DI PROGETTI COMPLETATI

---

## Esempio 1: TODO Manager (by Student A)

**Repository:** https://github.com/studentA/todo-cli

**Features Implementate:**
- ✅ CRUD tasks (Create, Read, Update, Delete)
- ✅ Priority system (Low, Medium, High)
- ✅ Filter by status/priority
- ✅ CSV persistence
- ✅ Interactive menu

**Highlights:**
- Valgrind clean (0 leaks)
- 87% code coverage (unit tests)
- Comprehensive README with GIFs
- 23 meaningful commits

**Demo Video:** (link)

**Grade:** 19/20

---

## Esempio 2: Data Logger (by Student B)

**Repository:** https://github.com/studentB/data-logger

**Features Implementate:**
- ✅ CSV parsing (1000+ rows)
- ✅ Statistical analysis (min/max/mean/stddev)
- ✅ Anomaly detection (threshold-based)
- ✅ ASCII chart visualization
- ✅ Export filtered data

**Highlights:**
- Handles large files efficiently
- Clean separation of concerns (parser, analyzer, visualizer)
- Excellent error reporting
- Doxygen documentation generated

**Performance:**
- Processes 10,000 data points in <100ms

**Grade:** 20/20

---

---

# RISORSE E SUPPORTO

---

## Durante Implementazione

**Se bloccato:**

1. **Consulta lezioni precedenti**
   - Lezione 2: Prompt engineering
   - Lezione 3: Memory management
   - Lezione 4: Git workflow

2. **Chiedi all'IA** (formula prompt specifico)

3. **Chiedi al docente** (se IA non risolve)

4. **Cerca su Stack Overflow** (se problema comune)

## Prompt Utili Generici

**Debugging generico:**
```
Ho questo problema: [descrizione]

Sintomi: [cosa succede]
Aspettative: [cosa dovrebbe succedere]

Codice rilevante:
[incolla codice]

Error output:
[incolla errore se presente]

Cosa potrebbe essere? Suggerisci debug steps.
```

**Refactoring:**
```
Questo codice funziona ma è disorganizzato:

[incolla codice]

Come posso refactorarlo per essere:
- Più leggibile
- Più testabile
- Senza duplicazione

Mantieni funzionalità identica.
```

**Ottimizzazione:**
```
Questa funzione è troppo lenta con grandi input:

[incolla funzione]

Input tipico: [descrizione input]

Come posso ottimizzare? Considera:
- Algoritmo più efficiente
- Data structure migliore
- Trade-off memory vs speed
```

## Risorse Online

**Documentazione C:**
- https://en.cppreference.com/w/c

**Git:**
- https://git-scm.com/docs

**Valgrind:**
- https://valgrind.org/docs/manual/quick-start.html

**Markdown:**
- https://www.markdownguide.org/basic-syntax/

---

---

# 🎯 CONGRATULATIONS!

---

## Hai Completato il Corso!

### 🎓 Skills Acquisite

Durante questo corso hai imparato:

**Tecniche:**
- ✅ Prompt engineering efficace (framework CLEAR)
- ✅ Programmazione C sicura (memory management, buffer overflow prevention)
- ✅ Testing sistematico (Valgrind, edge cases)
- ✅ Git workflow professionale
- ✅ Documentazione tecnica (README, Doxygen)

**Mindset:**
- ✅ Design-first thinking
- ✅ Critical validation di output IA
- ✅ Iterazione e continuous improvement
- ✅ Quality assurance mindset

**Portfolio:**
- ✅ Progetto completo su GitHub
- ✅ README professionale
- ✅ Git history pulita
- ✅ Codice production-quality

### 🚀 Prossimi Passi

**Immediate (questa settimana):**

1. **Completa progetto se non finito**
   - Implementa feature mancanti
   - Fix bug noti
   - Migliora documentazione

2. **Push su GitHub**
   - Repository pubblico
   - README professionale
   - Tag release

3. **Update portfolio**
   - Pin progetto su profilo
   - Update bio
   - Link da LinkedIn/CV

**Short-term (questo mese):**

4. **Implement 2-3 progetti aggiuntivi**
   - Diversifica portfolio
   - Applica skills in contesti diversi
   - Sperimenta con librerie/tool nuovi

5. **Contribuisci a open source**
   - Cerca "good first issue" su GitHub
   - Fork, implement, PR
   - Build reputation

6. **Approfondisci una area**
   - Embedded systems (Arduino, ESP32)
   - Web development (learn backend)
   - Systems programming (OS concepts)

**Long-term (quest'anno):**

7. **Build significant project**
   - 1000+ lines of code
   - Multiple contributors
   - Used by others

8. **Partecipa a hackathon**
   - Network con altri developer
   - Fast-paced development experience
   - Portfolio piece

9. **Technical blog/YouTube**
   - Documenta quello che impari
   - "Best way to learn is teach"
   - Build online presence

### 💼 Preparazione Colloqui

**Il tuo progetto finale è interview-ready se:**

- ✅ GitHub repository pubblico ben documentato
- ✅ Può spiegare ogni scelta tecnica
- ✅ Può discutere trade-offs
- ✅ Può spiegare come hai usato IA (senza nasconderlo!)
- ✅ Può fare live demo senza crash

**Domande tipiche colloquio:**

**Q:** "Raccontami di un progetto di cui sei orgoglioso"
**A:** [Descrivi progetto finale, focus su challenges risolti]

**Q:** "Come usi l'IA nella programmazione?"
**A:** "Uso IA come assistente per boilerplate e debugging, ma valido sempre criticamente. Per esempio, nel mio progetto [X], l'IA ha generato struttura base ma io ho..."

**Q:** "Come gestisci i bug?"
**A:** "Approccio sistematico: riproduco, uso debugger/Valgrind, formulo ipotesi, testo fix, valido con test. Nel progetto [X] ho affrontato [bug specifico] e..."

### 🌟 Final Advice

**Sull'uso dell'IA:**

> **"L'IA è come un junior developer molto veloce. Ti può aiutare enormemente, ma tu devi essere il senior che supervisiona, valida e decide."**

**Non dire mai:**
- ❌ "L'IA lo ha scritto per me"
- ❌ "Non so come funziona, l'ha fatto ChatGPT"

**Dì invece:**
- ✅ "Ho usato IA per generare boilerplate, poi ho customizzato"
- ✅ "L'IA ha suggerito 3 approcci, ho scelto X perché..."
- ✅ "Uso IA per accelerare, ma valido tutto con test e Valgrind"

**Sulla carriera:**

> **"Il futuro della programmazione è collaborazione umano-IA. I programmatori che sapranno usare IA efficacemente saranno i più richiesti."**

**Skills che nessuna IA sostituirà:**
- 🧠 **Problem decomposition** (dividere problema complesso)
- 🎯 **Requirements gathering** (capire cosa serve davvero)
- 🏗️ **Architecture design** (decidere struttura sistema)
- 🔍 **Critical thinking** (validare correttezza)
- 🤝 **Communication** (spiegare soluzioni)

**Investi su queste.**

---

## 📞 Resta in Contatto

**Docente:**
- Email: [email docente]
- LinkedIn: [link]

**Community:**
- Discord: [link se disponibile]
- Forum: [link se disponibile]

**Risorse:**
- Repository materiale corso: [link]
- Registrazioni lezioni: [link se disponibile]

---

## 🙏 Feedback

**Aiutaci a migliorare il corso!**

Se hai 5 minuti, lascia feedback:

1. **Cosa ha funzionato bene?**
2. **Cosa miglioreresti?**
3. **Quale lezione ti è piaciuta di più?**
4. **Il corso ha soddisfatto le aspettative?**
5. **Consiglieresti questo corso?**

[Link form feedback]

---

## 🎊 CONGRATULAZIONI DI NUOVO!

Hai completato il corso **"Intelligenza Artificiale e Programmazione Assistita"**.

Ora hai le skills per:
- 🚀 Sviluppare software in modo 2x più veloce
- 🛡️ Scrivere codice sicuro e robusto
- 📚 Documentare professionalmente
- 🤝 Collaborare con Git
- 🧠 Usare IA in modo intelligente e critico

**Il tuo viaggio come developer moderno è appena iniziato.**

**Buon coding e buona fortuna! 💻✨**

---

**Made with ❤️ and Claude**

**Corso ITS - Intelligenza Artificiale e Programmazione Assistita 2025**

---