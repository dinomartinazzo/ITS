# 📘 LEZIONE 4: GESTIONE PROGETTI E DOCUMENTAZIONE
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Durata:** 2 ore
**Struttura:** 1 ora teoria + 1 ora pratica
**Livello:** Intermedio-Avanzato
**Prerequisiti:** Lezioni 1-3 completate, familiarità con programmazione base

---

## 🎯 Obiettivi della Lezione

Al termine di questa lezione sarai in grado di:

✅ **Pianificare** progetti software con metodologia strutturata
✅ **Progettare** architetture con supporto IA
✅ **Documentare** codice professionalmente (README, commenti, Doxygen)
✅ **Usare** Git per version control
✅ **Collaborare** efficacemente in team con IA
✅ **Creare** portfolio di progetti per colloqui
✅ **Applicare** workflow professionali end-to-end

---

## 📋 Struttura della Lezione

### **PARTE 1: TEORIA (60 minuti)**

1. **Metodologia di Progetto con IA** (15 min)
   - Dalla idea al codice funzionante
   - Design-first vs code-first
   - Ruolo dell'IA in ogni fase

2. **Workflow Professionale** (15 min)
   - Requirements → Design → Implementation → Testing → Documentation
   - Iterazione e feedback loop
   - Quality assurance

3. **Documentazione Tecnica** (15 min)
   - README.md efficaci
   - Commenti in-code (Doxygen)
   - Schemi e diagrammi
   - Documentation-driven development

4. **Git e Version Control** (15 min)
   - Concetti base: repository, commit, branch
   - Workflow Git standard
   - Best practices per commit message
   - Collaborazione e code review

### **PARTE 2: PRATICA (60 minuti)**

5. **Workshop: Progettare con IA** (15 min)
   - Definire requirements
   - Creare design document
   - Generare scheletro progetto

6. **Generare Documentazione** (15 min)
   - README.md completo
   - Commenti Doxygen
   - User guide

7. **Git Hands-On** (20 min)
   - Inizializzare repository
   - Commit workflow
   - Branching e merging
   - Push su GitHub

8. **Progetto Completo** (10 min)
   - Integrazione di tutti i concetti
   - Checklist finale

---

---

# PARTE 1: TEORIA (60 MINUTI)

---

## 1. METODOLOGIA DI PROGETTO CON IA (15 minuti)

### 1.1 Dalla Idea al Codice Funzionante

**Il processo tradizionale (senza IA):**

```
Idea → Ricerca → Design → Implementazione (lenta) → Debug → Test → Deploy
        ↑                                                              ↓
        └──────────────── Feedback (settimane) ─────────────────────────┘
```

**Il processo moderno (con IA):**

```
Idea → Design con IA → Implementazione rapida → Validazione → Iterazione
       ↓                      ↓                      ↓
    Minuti               Ore (non giorni)      Feedback immediato
```

**Differenze chiave:**

| Fase | Senza IA | Con IA |
|------|----------|--------|
| **Ricerca** | Ore su Stack Overflow | Chiedi all'IA (minuti) |
| **Design** | Carta e penna | IA genera opzioni con pro/contro |
| **Implementazione** | Scrivi tutto a mano | IA genera boilerplate, tu customizzi |
| **Debug** | Printf debugging | IA analizza errori e suggerisce fix |
| **Documentazione** | Compito noioso | IA genera bozza, tu raffini |

**Importante:** L'IA accelera OGNI fase, ma **tu rimani il decision maker**.

### 1.2 Design-First vs Code-First

**❌ Code-First (Approccio istintivo ma rischioso):**

```
Studente: "Voglio fare un gestionale studenti"
          ↓
     Apre editor, inizia a scrivere codice
          ↓
     Dopo 100 righe: "Aspetta, come gestisco errori?"
          ↓
     Dopo 200 righe: "Come faccio a testare questo?"
          ↓
     Dopo 500 righe: "Devo rifare tutto da capo!"
```

**Risultato:** Codice disorganizzato, difficile da mantenere, tempo sprecato.

---

**✅ Design-First (Approccio professionale):**

```
Idea: "Gestionale studenti"
  ↓
Definisci requirements (con IA):
  - Cosa deve fare esattamente?
  - Quali dati gestisce?
  - Quali operazioni serve?
  ↓
Design architettura (con IA):
  - Quali strutture dati?
  - Quali moduli/file?
  - Interfaccia utente?
  ↓
Implementa modulo per modulo
  ↓
Testa sistematicamente
  ↓
Documenta
```

**Risultato:** Codice pulito, manutenibile, meno bug, tempo risparmiato.

**Analogia:**

> Costruire software senza design è come costruire una casa senza progetto. Forse riesci a fare 4 muri, ma probabilmente dovrai demolire e rifare.

### 1.3 Le 5 Fasi del Progetto con IA

**FASE 1: REQUIREMENTS (Cosa serve?)**

**Cosa fare:**
- Definisci obiettivi chiari
- Elenca funzionalità richieste
- Identifica vincoli (tempo, risorse, skills)

**Come l'IA aiuta:**

```
Prompt:
Ho un'idea per un progetto: [descrivi idea].
Aiutami a definire requirements chiari e strutturati.
Dividi in:
- Must have (essenziale)
- Should have (importante)
- Nice to have (opzionale)
```

**Output IA:** Lista organizzata di features.

---

**FASE 2: DESIGN (Come farlo?)**

**Cosa fare:**
- Scegli architettura
- Definisci strutture dati
- Pianifica moduli e interfacce
- Considera alternatives (trade-offs)

**Come l'IA aiuta:**

```
Prompt:
Per il progetto [X] con requirements [Y],
proponi 3 alternative di architettura.
Per ognuna, analizza:
- Pro e contro
- Complessità implementazione
- Estendibilità futura
- Performance
```

**Output IA:** Opzioni confrontabili. **TU decidi** quale usare.

---

**FASE 3: IMPLEMENTATION (Codice)**

**Cosa fare:**
- Implementa modulo per modulo
- Usa IA per generare boilerplate
- Customizza per il tuo caso
- Valida continuamente

**Come l'IA aiuta:**

```
Prompt:
Genera scheletro del modulo [X] che implementa [Y].
Include:
- Strutture dati
- Funzioni pubbliche (solo firma)
- Gestione errori
- Commenti TODO per logica
```

**Tu completi la logica specifica.**

---

**FASE 4: TESTING (Funziona?)**

**Cosa fare:**
- Test ogni funzione
- Test integrazione
- Edge cases
- Valgrind/sanitizer

**Come l'IA aiuta:**

```
Prompt:
Genera suite di test per questa funzione:
[codice]

Include test per:
- Happy path
- Edge cases (NULL, empty, boundary)
- Error handling
```

---

**FASE 5: DOCUMENTATION (Spiegare agli altri)**

**Cosa fare:**
- README per overview
- Commenti in-code per dettagli
- User guide se applicabile
- Architecture document (per progetti grandi)

**Come l'IA aiuta:**

```
Prompt:
Genera README.md professionale per questo progetto:
[descrizione]

Include:
- Overview
- Installation
- Usage examples
- API documentation
- Contributing guidelines
```

### 1.4 Esempio: Progetto "Task Manager" CLI

**Applichiamo le 5 fasi:**

**FASE 1: Requirements**

```
Progetto: Task Manager da linea di comando

Must have:
- Aggiungere task (titolo, descrizione, priorità)
- Elencare task
- Marcare task come completato
- Salvare su file (persistenza)

Should have:
- Filtrare per priorità
- Ricerca per parola chiave

Nice to have:
- Deadline con reminder
- Categorie/tag
```

**FASE 2: Design**

```
Architettura scelta:
- task.h/task.c: Struttura Task e operazioni base
- storage.h/storage.c: Salvataggio/caricamento da file
- ui.h/ui.c: Interfaccia utente (menu)
- main.c: Entry point

Strutture dati:
- typedef struct Task { int id; char *title; ... }
- Dynamic array di Task per gestire lista

File storage:
- Format: JSON o CSV (scegliamo CSV per semplicità)
```

**FASE 3-5:** Implementazione, testing, documentazione (vedremo in pratica).

---

## 2. WORKFLOW PROFESSIONALE (15 minuti)

### 2.1 Il Ciclo di Sviluppo

**Workflow standard professionale:**

```
┌─────────────────────────────────────────────────────────┐
│                    SVILUPPO SOFTWARE                    │
└─────────────────────────────────────────────────────────┘
         ↓
┌─────────────────┐
│ 1. REQUIREMENTS │  ← Cosa serve?
│   - User stories│
│   - Specs       │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. DESIGN       │  ← Come farlo?
│   - Architecture│
│   - Data models │
│   - API design  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. IMPLEMENT    │  ← Scrivi codice
│   - Modulo 1    │
│   - Modulo 2... │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. TEST         │  ← Funziona?
│   - Unit tests  │
│   - Integration │
│   - Valgrind    │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 5. CODE REVIEW  │  ← Qualità OK?
│   - Peer review │
│   - Refactoring │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 6. DOCUMENTATION│  ← Comprensibile?
│   - README      │
│   - Comments    │
│   - User guide  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 7. DEPLOY       │  ← Rilascia!
│   - Git tag     │
│   - Release     │
└─────────────────┘
         │
         └──────► Manutenzione e iterazione
```

### 2.2 Iterazione e Feedback Loop

**Sviluppo NON è lineare!**

```
        ┌─────────────────┐
        │   Requirements  │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
    ┌──→│     Design      │←──┐
    │   └────────┬────────┘   │
    │            ↓             │
    │   ┌─────────────────┐   │
    │   │  Implementation │   │
    │   └────────┬────────┘   │
    │            ↓             │
    │   ┌─────────────────┐   │
    └───│     Testing     │   │
        └────────┬────────┘   │
                 ↓             │
        ┌─────────────────┐   │
        │  Trovato bug?   │───┘ (torna a design/implementation)
        └────────┬────────┘
                 ↓ (no bug)
        ┌─────────────────┐
        │   Documentation │
        └────────┬────────┘
                 ↓
        ┌─────────────────┐
        │     Deploy      │
        └─────────────────┘
```

**È normale tornare indietro!** Trovare bug durante testing che richiedono modifica design è **parte del processo**.

### 2.3 Quality Assurance Checklist

**Prima di considerare un progetto "completo":**

**✅ Funzionalità:**
- [ ] Tutte le features richieste implementate
- [ ] Edge cases gestiti
- [ ] Error handling completo

**✅ Codice:**
- [ ] Compila senza warning (`-Wall -Wextra`)
- [ ] Nessun memory leak (Valgrind clean)
- [ ] Naming consistente e significativo
- [ ] Funzioni < 50 righe (se possibile)
- [ ] Nessuna duplicazione evidente

**✅ Testing:**
- [ ] Unit test per ogni funzione critica
- [ ] Integration test per workflow completi
- [ ] Testato su input edge case
- [ ] Performance accettabile

**✅ Documentazione:**
- [ ] README.md completo
- [ ] Commenti in-code dove necessario
- [ ] API documentation (se libreria)
- [ ] User guide (se applicazione)

**✅ Version Control:**
- [ ] Tutto committato su Git
- [ ] Commit message significativi
- [ ] Tagged release version
- [ ] Pushed su GitHub/GitLab

### 2.4 Time Management con IA

**Stima tradizionale vs con IA:**

| Task | Tempo senza IA | Tempo con IA | Saving |
|------|---------------|--------------|--------|
| Requirements gathering | 2h | 1h | -50% |
| Design architettura | 4h | 2h | -50% |
| Implementazione base | 8h | 3h | -62% |
| Debugging | 4h | 2h | -50% |
| Testing | 3h | 2h | -33% |
| Documentazione | 3h | 1h | -67% |
| **TOTALE** | **24h** | **11h** | **-54%** |

**Nota:** I numeri variano, ma trend è chiaro: **IA dimezza tempi**.

**Dove l'IA risparmia più tempo:**
1. **Boilerplate code** (struct, header guards, ecc.)
2. **Debugging** (analisi errori compilatore)
3. **Documentazione** (genera bozze)
4. **Ricerca** (Stack Overflow integrato)

**Dove l'IA NON risparmia tempo:**
- Pensiero critico (design decisions)
- Comprensione del dominio
- Testing approfondito
- Code review finale

---

## 3. DOCUMENTAZIONE TECNICA (15 minuti)

### 3.1 README.md Efficaci

**README.md è la PRIMA cosa che la gente vede del tuo progetto.**

Un buon README risponde a queste domande:
1. **Cosa fa** questo progetto?
2. **Perché** dovrei usarlo?
3. **Come** lo installo?
4. **Come** lo uso?
5. **Come** contribuisco? (se open source)

**Struttura standard README.md:**

```markdown
# Nome Progetto

Breve descrizione (1-2 frasi) di cosa fa.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Comandi per installare dipendenze e compilare
git clone https://github.com/user/project.git
cd project
make
```

## Usage

```bash
# Esempi di uso base
./program --help
./program input.txt output.txt
```

## Examples

[Screenshot o esempi di output]

## Documentation

Link a documentazione dettagliata se disponibile.

## Testing

```bash
# Come eseguire i test
make test
```

## Contributing

Linee guida per contribuire (se open source).

## License

MIT / GPL / etc.

## Authors

- Nome Cognome - [@github](https://github.com/username)
```

**Esempio concreto: Task Manager**

````markdown
# Task Manager CLI

Un semplice ma potente task manager da linea di comando scritto in C.
Perfetto per gestire le tue TODO list direttamente dal terminale.

## Features

- ✅ Aggiungere, elencare, completare task
- 💾 Persistenza automatica su file
- 🔍 Ricerca e filtraggio per priorità
- 🎯 Interfaccia semplice e intuitiva

## Installation

### Requisiti

- GCC o Clang
- Make
- Linux/macOS/Windows (MinGW)

### Compilazione

```bash
git clone https://github.com/yourusername/taskmanager.git
cd taskmanager
make
```

## Usage

### Comandi Base

```bash
# Aggiungere un task
./taskmanager add "Studiare per esame" --priority high

# Elencare tutti i task
./taskmanager list

# Marcare come completato
./taskmanager complete 1

# Filtrare per priorità
./taskmanager list --priority high
```

### Esempi

```
$ ./taskmanager list
┌────┬───────────────────────────────────┬──────────┬───────────┐
│ ID │ Title                             │ Priority │ Status    │
├────┼───────────────────────────────────┼──────────┼───────────┤
│ 1  │ Studiare per esame                │ HIGH     │ Pending   │
│ 2  │ Comprare latte                    │ LOW      │ Completed │
└────┴───────────────────────────────────┴──────────┴───────────┘
```

## Documentation

Vedi [DOCUMENTATION.md](DOCUMENTATION.md) per API dettagliate.

## Testing

```bash
make test
# O con Valgrind:
make valgrind-test
```

## Project Structure

```
taskmanager/
├── src/
│   ├── main.c
│   ├── task.c/.h       # Struttura Task e operazioni
│   ├── storage.c/.h    # Persistenza file
│   └── ui.c/.h         # Interfaccia utente
├── tests/
│   └── test_task.c
├── Makefile
└── README.md
```

## Contributing

Contributi sono benvenuti! Apri una issue o pull request.

## License

MIT License - vedi [LICENSE](LICENSE)

## Author

- Mario Rossi - [@mariorossi](https://github.com/mariorossi)

---

**Made with ❤️ and Claude Code**
````

**🎯 Prompt per generare README:**

```
Genera un README.md professionale per questo progetto:

Progetto: [nome e descrizione]
Features: [lista features]
Tecnologie: [C, Make, ecc.]
Target utente: [chi userà questo?]

Includi:
- Badge (se applicabile)
- Sezioni standard (Installation, Usage, etc.)
- Esempi di comandi
- Project structure
- Emoji appropriati per leggibilità
```

### 3.2 Commenti In-Code (Doxygen)

**Quando commentare:**

**❌ NON commentare ovvietà:**

```c
// Incrementa i
i++;

// Somma a e b
int sum = a + b;
```

**✅ Commenta il "PERCHÉ", non il "COSA":**

```c
// Skip header row (data starts at line 2)
for (int i = 1; i < size; i++) { ... }

// Use binary search since array is pre-sorted
int index = binary_search(arr, value);
```

**Commenti Doxygen per API:**

```c
/**
 * @brief Aggiunge un task alla lista
 *
 * Crea un nuovo task con i parametri specificati e lo aggiunge
 * alla lista dinamica, espandendo se necessario.
 *
 * @param list Puntatore alla lista di task
 * @param title Titolo del task (max 100 caratteri)
 * @param priority Priorità: 0=low, 1=medium, 2=high
 * @return 0 se successo, -1 se errore (malloc failure o parametri invalidi)
 *
 * @note list deve essere inizializzata con task_list_create()
 * @warning title viene copiato, quindi può essere liberato dal caller
 *
 * @code
 * TaskList *list = task_list_create();
 * task_add(list, "Buy milk", 0);
 * task_add(list, "Study for exam", 2);
 * @endcode
 */
int task_add(TaskList *list, const char *title, int priority);
```

**Tag Doxygen comuni:**

| Tag | Uso |
|-----|-----|
| `@brief` | Descrizione breve (1 riga) |
| `@param` | Descrizione parametro |
| `@return` | Descrizione valore di ritorno |
| `@note` | Nota importante |
| `@warning` | Avvertimento |
| `@code ... @endcode` | Esempio di codice |
| `@see` | Riferimento ad altra funzione |

**Generare HTML da Doxygen:**

```bash
# Installa Doxygen
sudo apt install doxygen

# Genera config
doxygen -g

# Genera documentazione
doxygen Doxyfile

# Apri html/index.html nel browser
```

### 3.3 Architecture Documentation

**Per progetti complessi, documenta architettura:**

**File: ARCHITECTURE.md**

```markdown
# Architecture

## Overview

Questo progetto è organizzato in 3 layer principali:
- **Data Layer**: Gestione strutture dati (task.c)
- **Storage Layer**: Persistenza (storage.c)
- **UI Layer**: Interfaccia utente (ui.c)

## Data Flow

```
User Input (ui.c)
    ↓
Validation (ui.c)
    ↓
Business Logic (task.c)
    ↓
Persistence (storage.c)
    ↓
File System
```

## Module Dependencies

```
main.c
  ├── ui.c
  │   └── task.c
  └── storage.c
      └── task.c
```

## Key Design Decisions

### Why CSV instead of JSON for storage?
- Semplicità parsing
- Nessuna dipendenza esterna
- Human-readable

### Why dynamic array instead of linked list?
- Accesso O(1) per indice
- Migliore cache locality
- Array piccoli (<1000 elementi)
```

### 3.4 User Guide (se applicazione)

**Per applicazioni end-user, includi guida:**

**File: USER_GUIDE.md**

```markdown
# Task Manager - User Guide

## Getting Started

### First Launch

Alla prima esecuzione, il programma crea automaticamente
il file `tasks.csv` nella directory corrente.

### Adding Your First Task

```bash
./taskmanager add "My first task"
```

## Common Workflows

### Daily Review

1. Visualizza task pendenti:
   ```bash
   ./taskmanager list --status pending
   ```

2. Completa task finiti:
   ```bash
   ./taskmanager complete <id>
   ```

3. Aggiungi nuovi task per domani

### Priority Management

Task con priorità HIGH vengono mostrati per primi:

```bash
./taskmanager list --sort priority
```

## Troubleshooting

### "File not found"
Assicurati di essere nella directory giusta o specifica
path con `--file /path/to/tasks.csv`

### "Permission denied"
Controlla permessi file tasks.csv: `chmod 644 tasks.csv`
```

---

## 4. GIT E VERSION CONTROL (15 minuti)

### 4.1 Concetti Base

**Cos'è Git?**

Sistema di **version control distribuito** che traccia modifiche al codice.

**Perché usare Git?**

1. **Storia completa**: Vedi ogni modifica mai fatta
2. **Backup**: Codice al sicuro su GitHub/GitLab
3. **Collaborazione**: Lavora in team senza conflitti
4. **Esperimenti**: Prova modifiche senza rompere codice funzionante
5. **Portfolio**: Mostra progetti a recruiter

**Concetti chiave:**

```
┌──────────────────────────────────────────┐
│          REPOSITORY (Progetto)           │
├──────────────────────────────────────────┤
│  main (branch principale)                │
│    ↓                                     │
│  [Commit 1] ← [Commit 2] ← [Commit 3]    │
│    "Initial"  "Add feature" "Fix bug"    │
│                                          │
│  feature-branch (branch sviluppo)        │
│    ↓                                     │
│  [Commit 4] ← [Commit 5]                 │
│    "WIP"      "Feature done"             │
└──────────────────────────────────────────┘
```

**Repository:** Cartella del progetto tracciata da Git
**Commit:** Snapshot del codice in un momento specifico
**Branch:** Linea di sviluppo parallela
**Remote:** Copia del repository su server (es: GitHub)

### 4.2 Workflow Git Standard

**Setup iniziale (una volta sola):**

```bash
# Configura identità
git config --global user.name "Mario Rossi"
git config --global user.email "mario@example.com"

# Editor preferito
git config --global core.editor "code"  # VSCode
```

**Workflow quotidiano:**

```bash
# 1. Inizializza repository (prima volta)
git init

# 2. Aggiungi file allo stage
git add file.c file.h

# 3. Crea commit
git commit -m "Add feature X"

# 4. Push su GitHub
git push origin main
```

**Workflow dettagliato:**

```
┌─────────────────────────────────────────────┐
│  Working Directory (i tuoi file)            │
│    file.c (modificato)                      │
└────────────┬────────────────────────────────┘
             │ git add file.c
             ↓
┌─────────────────────────────────────────────┐
│  Staging Area (pronti per commit)           │
│    file.c (staged)                          │
└────────────┬────────────────────────────────┘
             │ git commit -m "message"
             ↓
┌─────────────────────────────────────────────┐
│  Local Repository (storia locale)           │
│    [Commit con file.c]                      │
└────────────┬────────────────────────────────┘
             │ git push
             ↓
┌─────────────────────────────────────────────┐
│  Remote Repository (GitHub)                 │
│    [Commit accessibile a tutti]             │
└─────────────────────────────────────────────┘
```

**Comandi essenziali:**

```bash
# Vedere stato corrente
git status

# Vedere modifiche
git diff

# Storia commit
git log
git log --oneline --graph

# Creare branch
git branch feature-x
git checkout feature-x
# O in un comando:
git checkout -b feature-x

# Merge branch
git checkout main
git merge feature-x

# Pull (scaricare aggiornamenti)
git pull origin main

# Clone (scaricare progetto esistente)
git clone https://github.com/user/project.git
```

### 4.3 Best Practices per Commit Message

**❌ Commit message CATTIVI:**

```
git commit -m "fix"
git commit -m "update"
git commit -m "stuff"
git commit -m "asdfasdf"
```

Tra 6 mesi non capirai cosa hai fatto!

**✅ Commit message BUONI:**

```
git commit -m "Fix buffer overflow in parse_input()"
git commit -m "Add priority filtering to task list"
git commit -m "Refactor storage module for better error handling"
git commit -m "Update README with installation instructions"
```

**Formato standard:**

```
<type>: <short description>

[optional body]

[optional footer]
```

**Types comuni:**

- `feat`: Nuova feature
- `fix`: Bug fix
- `docs`: Documentazione
- `refactor`: Refactoring (no new feature, no bug fix)
- `test`: Aggiunta test
- `chore`: Task vari (build, config)

**Esempi:**

```
feat: Add CSV export functionality

Implemented export_to_csv() function that writes all tasks
to a CSV file with proper escaping.

Closes #42
```

```
fix: Prevent memory leak in task_free()

task_free() was not freeing the title string, causing
a leak detected by Valgrind.
```

```
docs: Update API documentation for storage module

Added Doxygen comments to all public functions.
```

**Regole d'oro:**

1. **Prima riga max 50 caratteri** (titolo)
2. **Usa imperativo**: "Add feature" not "Added feature"
3. **Spiega il WHY**, non il WHAT (il codice mostra il WHAT)
4. **Reference issue** se applicabile (#42)

### 4.4 Branching Strategy

**Per progetti personali:**

```
main (sempre funzionante)
  │
  ├─ feature-1 (sviluppo feature)
  │
  └─ bugfix-x (fix urgente)
```

**Workflow:**

```bash
# 1. Crea branch per feature
git checkout -b feature-task-search
# 2. Sviluppa e committa
git add search.c search.h
git commit -m "feat: Add task search functionality"
# 3. Torna a main
git checkout main
# 4. Merge feature
git merge feature-task-search
# 5. Elimina branch (opzionale)
git branch -d feature-task-search
```

**Per team:**

Strategie comuni: Git Flow, GitHub Flow, GitLab Flow (oltre scope di questo corso).

### 4.5 .gitignore

**File da NON committare:**

- File compilati (`*.o`, `*.exe`, `a.out`)
- File di build (`build/`, `bin/`)
- File dell'editor (`.vscode/`, `.idea/`)
- Dati personali/sensibili
- File temporanei

**Esempio .gitignore:**

```
# Compiled files
*.o
*.exe
*.out
a.out

# Build directories
build/
bin/
obj/

# Editor files
.vscode/
.idea/
*.swp
*~

# OS files
.DS_Store
Thumbs.db

# Dependencies
lib/

# Data files (se contengono dati sensibili)
# *.csv
# *.db
```

---

---

# PARTE 2: PRATICA (60 MINUTI)

---

## 5. WORKSHOP: PROGETTARE CON IA (15 minuti)

### 5.1 Esercizio Guidato: Sistema di Biblioteca

**Scenario:** Vuoi creare un sistema per gestire prestiti di libri in una biblioteca.

**STEP 1: Definire Requirements con IA**

**Prompt:**

```
Voglio creare un sistema di gestione biblioteca in C per un progetto ITS.

Aiutami a definire requirements chiari e strutturati.

Contesto:
- Biblioteca piccola (max 1000 libri, 100 utenti)
- Sistema CLI (non GUI)
- Dati persistiti su file
- Progetto didattico (semplicità priorità su performance)

Dividi requirements in:
- Must have (essenziale MVP)
- Should have (importante)
- Nice to have (se c'è tempo)

Per ogni requirement, indica stima complessità (low/medium/high).
```

**Output atteso IA:**

```
REQUIREMENTS - Sistema Gestione Biblioteca

MUST HAVE (MVP):
1. [LOW] Aggiungere libri (titolo, autore, ISBN)
2. [MEDIUM] Registrare prestiti (chi ha preso cosa, quando)
3. [MEDIUM] Restituire libri
4. [LOW] Elencare libri disponibili
5. [MEDIUM] Salvare/caricare dati da file

SHOULD HAVE:
6. [MEDIUM] Ricerca libri per titolo/autore
7. [LOW] Visualizzare storico prestiti utente
8. [MEDIUM] Gestione utenti (aggiungere, rimuovere)
9. [LOW] Calcolare multe per ritardi

NICE TO HAVE:
10. [HIGH] Sistema di prenotazioni
11. [MEDIUM] Statistiche (libri più prestati)
12. [HIGH] Import/export CSV
13. [LOW] Supporto multi-lingua

STIMA TOTALE: ~40 ore sviluppo (solo MVP: ~20 ore)
```

**STEP 2: Design Architettura con IA**

**Prompt:**

```
Per il sistema biblioteca con questi requirements:
[incolla requirements must-have]

Proponi architettura modulare in C.

Specifica:
1. Strutture dati principali
2. Moduli (file .c/.h) e responsabilità
3. Interfacce tra moduli
4. Format file per persistenza

Obiettivo: Codice manutenibile e testabile.
```

**Output atteso IA:**

```
ARCHITETTURA - Sistema Biblioteca

STRUTTURE DATI:

```c
typedef struct {
    char isbn[14];
    char title[100];
    char author[100];
    bool is_available;
} Book;

typedef struct {
    int user_id;
    char name[100];
} User;

typedef struct {
    char isbn[14];
    int user_id;
    time_t loan_date;
    time_t return_date;  // 0 se non ancora restituito
} Loan;

typedef struct {
    Book *books;
    size_t book_count;
    size_t book_capacity;
} BookCatalog;

typedef struct {
    Loan *loans;
    size_t loan_count;
    size_t loan_capacity;
} LoanHistory;
```

MODULI:

1. **book.c/book.h**
   - Gestione catalogo libri
   - Funzioni: book_add(), book_find(), book_list()

2. **loan.c/loan.h**
   - Gestione prestiti
   - Funzioni: loan_create(), loan_return(), loan_list_active()

3. **user.c/user.h**
   - Gestione utenti
   - Funzioni: user_add(), user_find()

4. **storage.c/storage.h**
   - Persistenza dati
   - Funzioni: save_all(), load_all()

5. **ui.c/ui.h**
   - Interfaccia utente (menu)
   - Funzioni: show_menu(), get_user_choice()

6. **main.c**
   - Entry point, loop principale

FILE PERSISTENZA:
- books.csv: isbn,title,author,is_available
- users.csv: id,name
- loans.csv: isbn,user_id,loan_date,return_date

FLUSSO DATI:
main.c → ui.c → loan.c/book.c → storage.c → file system
```

**STEP 3: Generare Scheletro Progetto**

**Prompt:**

```
Genera lo scheletro completo del progetto (solo header e funzioni vuote).

Per book.h e book.c, implementa la struttura completa con:
- Commenti Doxygen per ogni funzione
- Strutture dati definite
- Funzioni con solo firma (corpo vuoto con TODO)
- Include guards in header

Formato:
// book.h
[codice]

// book.c
[codice]
```

L'IA genererà scheletro che puoi poi riempire.

### 5.2 Task per Te

**Applica lo stesso processo a uno di questi progetti:**

1. **Sistema di Voti Studenti**
   - Gestire studenti, corsi, voti
   - Calcolare medie, statistiche
   - Generare pagelle

2. **Inventario Magazzino**
   - Prodotti con quantità
   - Operazioni: carico, scarico, inventario
   - Alert per scorte basse

3. **Budget Tracker**
   - Tracciare entrate/uscite
   - Categorie (cibo, trasporti, ecc.)
   - Report mensili

**Usa i 3 prompt visti sopra per:**
1. Definire requirements
2. Progettare architettura
3. Generare scheletro

---

## 6. GENERARE DOCUMENTAZIONE (15 minuti)

### 6.1 README.md Automatico

**Prompt per generare README:**

```
Genera un README.md professionale per questo progetto:

Progetto: Sistema Gestione Biblioteca
Descrizione: CLI tool per gestire prestiti libri in biblioteca
Linguaggio: C
Target: Studenti ITS, uso didattico

Features principali:
- Catalogo libri
- Gestione prestiti/restituzioni
- Persistenza su file CSV
- Interfaccia menu interattivo

Requisiti sistema:
- GCC o Clang
- Make
- Linux/macOS/Windows

Includi sezioni:
- Overview con emoji
- Installation instructions
- Usage examples con screenshot ASCII
- Project structure tree
- Testing instructions
- Contributing guidelines
- License (MIT)
- Badge se appropriati
```

**L'IA genererà README completo.** Tu dovrai:
1. Verificare accuratezza
2. Aggiungere screenshot reali
3. Personalizzare esempi

### 6.2 Commenti Doxygen Automatici

**Hai questa funzione senza commenti:**

```c
int loan_create(LoanHistory *history, const char *isbn,
                int user_id, BookCatalog *catalog) {
    if (history == NULL || isbn == NULL || catalog == NULL) {
        return -1;
    }

    Book *book = book_find(catalog, isbn);
    if (book == NULL || !book->is_available) {
        return -2;
    }

    if (history->loan_count >= history->loan_capacity) {
        size_t new_cap = history->loan_capacity * 2;
        Loan *new_loans = realloc(history->loans, new_cap * sizeof(Loan));
        if (new_loans == NULL) {
            return -3;
        }
        history->loans = new_loans;
        history->loan_capacity = new_cap;
    }

    Loan *loan = &history->loans[history->loan_count];
    strncpy(loan->isbn, isbn, sizeof(loan->isbn) - 1);
    loan->user_id = user_id;
    loan->loan_date = time(NULL);
    loan->return_date = 0;

    book->is_available = false;
    history->loan_count++;

    return 0;
}
```

**Prompt:**

```
Genera commento Doxygen completo per questa funzione:

[incolla codice]

Include:
- @brief (1 riga)
- @param per ogni parametro (spiega vincoli)
- @return (spiega tutti i codici ritorno)
- @note per informazioni importanti
- @code esempio d'uso @endcode
```

**Output IA:**

```c
/**
 * @brief Crea un nuovo prestito per un libro
 *
 * Registra un prestito assegnando un libro a un utente. Il libro
 * viene marcato come non disponibile. La storia prestiti viene
 * espansa automaticamente se necessario.
 *
 * @param history Puntatore alla storia prestiti (non NULL)
 * @param isbn ISBN del libro da prestare (non NULL, 13 caratteri)
 * @param user_id ID dell'utente che prende in prestito (>= 0)
 * @param catalog Puntatore al catalogo libri (non NULL)
 *
 * @return Codici di ritorno:
 *   - 0: Successo
 *   - -1: Parametro NULL
 *   - -2: Libro non trovato o non disponibile
 *   - -3: Fallimento realloc (out of memory)
 *
 * @note history e catalog devono essere inizializzati prima della chiamata
 * @warning Questa funzione modifica catalog (book->is_available = false)
 *
 * @code
 * LoanHistory *history = loan_history_create();
 * BookCatalog *catalog = book_catalog_create();
 * book_add(catalog, "978-0123456789", "Il Signore degli Anelli", "Tolkien");
 *
 * int result = loan_create(history, "978-0123456789", 42, catalog);
 * if (result == 0) {
 *     printf("Prestito creato con successo\n");
 * }
 * @endcode
 *
 * @see loan_return()
 */
int loan_create(LoanHistory *history, const char *isbn,
                int user_id, BookCatalog *catalog);
```

### 6.3 User Guide Automatica

**Prompt:**

```
Scrivi una User Guide completa per end-user non tecnici.

Applicazione: Sistema Biblioteca CLI

Include:
1. Getting Started (primi passi)
2. Common Workflows (use case tipici)
   - Prestare un libro
   - Restituire un libro
   - Cercare libri
3. Troubleshooting (problemi comuni e soluzioni)
4. FAQ

Usa linguaggio semplice, evita termini tecnici.
Includi esempi concreti con output simulato.
```

---

## 7. GIT HANDS-ON (20 minuti)

### 7.1 Inizializzare Repository

**Scenario:** Hai il progetto Biblioteca. Vuoi metterlo su Git.

**Step 1: Crea .gitignore**

```bash
# Crea file .gitignore
cat > .gitignore << EOF
# Compiled files
*.o
*.exe
*.out
library

# Data files (se vuoi ignorare dati di test)
# *.csv

# Editor
.vscode/
*.swp
EOF
```

**Step 2: Inizializza Git**

```bash
# Nella directory del progetto
git init

# Verifica
git status
```

**Output:**
```
On branch main
No commits yet

Untracked files:
  .gitignore
  Makefile
  src/
  include/
  README.md
```

**Step 3: Primo commit**

```bash
# Aggiungi tutti i file
git add .

# Controlla cosa verrà committato
git status

# Crea commit iniziale
git commit -m "Initial commit: Project skeleton

Added:
- Project structure (src/, include/)
- Makefile
- README.md
- .gitignore
"
```

### 7.2 Workflow Tipico

**Scenario: Aggiungi una feature**

```bash
# 1. Crea branch per feature
git checkout -b feature-book-search

# 2. Implementa feature (modifica file)
# ... scrivi codice in book.c ...

# 3. Verifica modifiche
git diff

# 4. Aggiungi file modificati
git add src/book.c include/book.h

# 5. Commit
git commit -m "feat: Add book search by title

Implemented book_search_by_title() function that performs
case-insensitive substring matching.
"

# 6. Torna a main
git checkout main

# 7. Merge feature
git merge feature-book-search

# 8. (Opzionale) Elimina branch
git branch -d feature-book-search
```

### 7.3 Push su GitHub

**Step 1: Crea repository su GitHub**

1. Vai su https://github.com
2. Clicca "New repository"
3. Nome: "library-management"
4. Descrizione: "C library management system"
5. Public o Private
6. **NON** inizializzare con README (hai già quello locale)
7. Clicca "Create repository"

**Step 2: Collega local a remote**

```bash
# Aggiungi remote
git remote add origin https://github.com/yourusername/library-management.git

# Verifica
git remote -v
```

**Step 3: Push**

```bash
# Push branch main
git push -u origin main

# -u setta upstream, prossime volte basta:
git push
```

**Step 4: Verifica su GitHub**

Apri https://github.com/yourusername/library-management

Dovresti vedere:
- README.md renderizzato
- File del progetto
- Commit history

### 7.4 Collaborazione: Pull Request (Cenni)

**Workflow collaborativo:**

```
1. Fork repository → Tua copia

2. Clone tua copia:
   git clone https://github.com/tuousername/project.git

3. Crea branch feature:
   git checkout -b fix-memory-leak

4. Implementa fix, commit, push:
   git push origin fix-memory-leak

5. Su GitHub: Apri Pull Request
   - Descrivi cosa hai fatto
   - Owner originale rivede
   - Se OK, fa merge

6. Pull modifiche accettate:
   git pull upstream main
```

### 7.5 Esercizio Pratico

**Task:**

1. Inizializza Git nel tuo progetto Task Manager (o Biblioteca)
2. Crea almeno 3 commit significativi:
   - Initial commit
   - Implementazione feature X
   - Fix bug Y
3. Crea branch "feature-test" e mergea
4. Push su GitHub
5. Condividi link repository

**Verifica finale:**

```bash
# Storia commit ben formattata?
git log --oneline

# Tutto pushato?
git status  # Should say "up to date with origin/main"
```

---

## 8. PROGETTO COMPLETO (10 minuti)

### 8.1 Checklist Progetto Completo

**Prima di considerare un progetto "finito":**

**✅ CODICE:**
- [ ] Compila senza warning (`-Wall -Wextra -Werror`)
- [ ] Tutte le features richieste implementate
- [ ] Gestione errori completa
- [ ] Memory-safe (Valgrind clean)
- [ ] Codice organizzato in moduli logici
- [ ] Naming consistente

**✅ TESTING:**
- [ ] Unit test per funzioni critiche
- [ ] Integration test per workflow completi
- [ ] Testato edge cases (NULL, empty, large inputs)
- [ ] Performance accettabile

**✅ DOCUMENTAZIONE:**
- [ ] README.md completo (Installation, Usage, Examples)
- [ ] Commenti Doxygen per API pubbliche
- [ ] User guide (se applicazione end-user)
- [ ] Architettura documentata (se progetto complesso)

**✅ VERSION CONTROL:**
- [ ] Repository Git inizializzato
- [ ] Commit significativi con message descrittivi
- [ ] .gitignore appropriato
- [ ] Pushed su GitHub/GitLab
- [ ] Tagged release (es: v1.0.0)

**✅ BUILD SYSTEM:**
- [ ] Makefile funzionante
- [ ] Target: all, clean, test, install
- [ ] Dipendenze corrette

**✅ LICENSE:**
- [ ] File LICENSE incluso (MIT, GPL, ecc.)

### 8.2 Creare Release

**Tag versione:**

```bash
# Tag annotato
git tag -a v1.0.0 -m "Release version 1.0.0

Features:
- Book catalog management
- Loan tracking
- CSV persistence
- Interactive CLI menu
"

# Push tag
git push origin v1.0.0
```

**Su GitHub: Create Release**

1. Vai su repository → Releases → "Draft a new release"
2. Tag: v1.0.0
3. Release title: "Version 1.0.0 - First Stable Release"
4. Descrizione:
   ```
   First stable release of Library Management System.

   Features:
   - ✅ Book catalog
   - ✅ Loan management
   - ✅ Persistent storage

   Installation:
   ```bash
   git clone https://github.com/user/library.git
   cd library
   make
   ./library
   ```

   See README.md for full documentation.
   ```
5. Attach binaries se applicabile
6. Publish release

### 8.3 Portfolio-Ready Checklist

**Per usare progetto in portfolio/CV:**

**✅ README deve includere:**
- [ ] Badge (build status, license, etc.)
- [ ] Screenshot o GIF demo
- [ ] Sezione "Skills Demonstrated" (C, Git, Valgrind, ecc.)

**✅ Repository deve avere:**
- [ ] Descrizione chiara (in "About" su GitHub)
- [ ] Topics/tags relevanti (c, cli, library-management)
- [ ] License badge
- [ ] Almeno 1 release

**✅ Codice deve essere:**
- [ ] Clean (no commented-out code)
- [ ] Consistente (formatting uniforme)
- [ ] Ben documentato

**✅ Opzionale ma impressionante:**
- [ ] CI/CD (GitHub Actions che compila e testa)
- [ ] Code coverage report
- [ ] Documentazione Doxygen generata e hostata
- [ ] Demo video su YouTube

---

## 🎯 RIEPILOGO LEZIONE 4

### Cosa Abbiamo Imparato

**Teoria:**
- ✅ Metodologia progetto in 5 fasi (Requirements → Design → Implementation → Testing → Documentation)
- ✅ Workflow professionale e quality assurance
- ✅ Documentazione tecnica (README, Doxygen, User Guide)
- ✅ Git fundamentals e best practices

**Pratica:**
- ✅ Progettazione architettura con IA
- ✅ Generazione documentazione automatica
- ✅ Setup repository Git completo
- ✅ Workflow Git end-to-end (init → commit → push)

### Key Takeaways

1. **Design prima di codice** (evita refactoring massivo dopo)
2. **IA accelera OGNI fase** (ma tu decidi)
3. **Documentazione non è opzionale** (README è marketing del tuo codice)
4. **Git è essenziale** (non solo backup, ma workflow professionale)
5. **Portfolio conta** (progetti GitHub = CV tecnico)

---

## 📚 COMPITI PER CASA

### Esercizio 1: Progetto Completo

**Completa uno dei progetti iniziati:**

1. Definisci requirements (con IA)
2. Progetta architettura (con IA)
3. Implementa MVP (must-have features)
4. Testa (Valgrind clean)
5. Documenta (README + commenti)
6. Push su GitHub

**Deliverable:**
- Link repository GitHub pubblico

### Esercizio 2: Portfolio Setup

**Crea il tuo portfolio GitHub:**

1. GitHub profile README (repository speciale `username/username`)
2. Pin i tuoi 3 progetti migliori
3. Aggiungi bio professionale
4. Link a LinkedIn/email

**Esempio README profile:**

```markdown
# Hi, I'm Mario Rossi 👋

🎓 ITS Student | 💻 C Programmer | 🤖 AI Enthusiast

## Skills
- Languages: C, Python
- Tools: Git, Valgrind, Make
- AI: ChatGPT, Claude for assisted development

## Projects
📚 [Library Management System](https://github.com/mario/library) - CLI tool in C
📝 [Task Manager](https://github.com/mario/taskmanager) - Productivity app
🎮 [Snake Game](https://github.com/mario/snake) - Terminal game

## Stats
![GitHub stats](https://github-readme-stats.vercel.app/api?username=mario)

## Contact
📧 mario.rossi@example.com
🔗 [LinkedIn](https://linkedin.com/in/mario-rossi)
```

### Esercizio 3: Contribuire a Open Source

**Trova un progetto C open source su GitHub:**

1. Cerca "good first issue" label
2. Fork repository
3. Implementa fix o feature
4. Apri Pull Request

**Obiettivo:** Esperienza collaborazione reale.

---

## 🎓 PROSSIMA LEZIONE

**LEZIONE 5: Progetto Finale Integrato**

**Anteprima:**
- Implementazione sistema completo end-to-end
- Integrazione tutti i concetti appresi
- Testing sistematico e debugging
- Documentazione finale professionale
- Presentazione lavoro

**Preparazione:**
- Rivedi tutte le lezioni precedenti
- Pensa a un progetto che ti appassiona
- Prepara domande

---

**Fine Lezione 4**

**📂 Ora sai gestire progetti professionalmente con IA e Git!**

**Ricorda:**
> "Il codice senza documentazione è come una macchina senza manuale: funziona, ma nessuno sa come usarla."

**Ottimo lavoro! Prepara il progetto finale! 💻✨**