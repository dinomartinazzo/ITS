# 📘 MODULO 2
# Programmazione Assistita con IA: C e Arduino
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita 2025
### Durata: 4 ore | Livello: Intermedio-Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti del Linguaggio C con IA](#2-fondamenti-del-linguaggio-c-con-ia)
3. [Template Prompt per C](#3-template-prompt-per-c)
4. [Problemi Ricorrenti Codice Generato](#4-problemi-ricorrenti-codice-generato)
5. [Gestione Memoria e Puntatori](#5-gestione-memoria-e-puntatori)
6. [Arduino: Fondamenti e Setup](#6-arduino-fondamenti-e-setup)
7. [Programmazione Arduino con IA](#7-programmazione-arduino-con-ia)
8. [Pattern Embedded Non-Bloccanti](#8-pattern-embedded-non-bloccanti)
9. [Sensori, Attuatori e Progetti IoT](#9-sensori-attuatori-e-progetti-iot)
10. [Debugging e Testing](#10-debugging-e-testing)
11. [Best Practices 2025](#11-best-practices-2025)
12. [Esercitazioni Pratiche](#12-esercitazioni-pratiche)

---

## 1. Introduzione e Obiettivi

### 1.1 Perché C e Arduino con IA

Benvenuti al secondo modulo! Qui entriamo nel vivo della **programmazione assistita da IA** applicata a due tecnologie fondamentali per il mondo embedded e IoT: il **linguaggio C** e **Arduino**.

**Perché studiare C nel 2025?**

Immaginate il C come il "Latino" della programmazione: quasi tutti i linguaggi moderni (C++, Java, JavaScript, Python) hanno sintassi ispirata al C. Ma il C non è solo storia: è **vivo e vegeto** ovunque ci sia bisogno di efficienza massima e controllo totale sull'hardware.

Dove troviamo C oggi:
- **Sistemi operativi** (Linux kernel è scritto in C)
- **Microcontrollori** (Arduino, ESP32, STM32)
- **Dispositivi IoT** (miliardi di sensori e attuatori)
- **Sistemi embedded** (automotive, elettrodomestici, droni)
- **Driver hardware** (interazione diretta con componenti fisici)

Il **C** è il linguaggio fondamentale per sistemi embedded, IoT e programmazione di basso livello. **Arduino** rende accessibile lo sviluppo embedded mantenendo la potenza del C++.

**Perché Arduino?**

Arduino ha rivoluzionato il modo di prototipare elettronica. Prima dell'Arduino (pre-2005), per programmare un microcontrollore servivano programmatori costosi, conoscenza approfondita di registri hardware e datasheet da 500 pagine. Arduino ha **democratizzato** l'embedded rendendo semplice:
- Caricare codice via USB (niente programmatori esterni)
- Usare funzioni semplici (`digitalWrite`, `analogRead`)
- Avere migliaia di librerie pronte
- Costruire prototipi in ore, non settimane

**Il Ruolo dell'IA**

L'IA può accelerare enormemente lo sviluppo, ma richiede **prompting esperto** per generare codice:
- ✅ **Sicuro** (no buffer overflow che causano crash)
- ✅ **Efficiente** (memoria limitata sui microcontrollori)
- ✅ **Robusto** (gestione errori, casi limite)
- ✅ **Standard-compliant** (C99, no estensioni non portabili)

**Analogia:** Pensate all'IA come a un assistente junior esperto ma disattento. Sa scrivere codice velocemente, ma potreste dover **revisionare** per evitare errori sottili. Voi siete l'architetto senior che valida il lavoro.

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Generare** codice C sicuro e robusto con LLM (GPT-4, Claude 3.5)
✅ **Identificare** e correggere errori tipici del codice generato
✅ **Gestire** correttamente memoria, puntatori, stringhe
✅ **Programmare** Arduino con pattern non-bloccanti
✅ **Integrare** sensori e attuatori con IA assistita
✅ **Debuggare** efficacemente con tool professionali
✅ **Implementare** progetti IoT completi

**Competenze Pratiche:**
- Scrivere prompt che generano codice C99 production-ready
- Riconoscere immediatamente codice C pericoloso (buffer overflow, memory leak)
- Implementare logica Arduino non-bloccante (multi-tasking simulato)
- Integrare sensori reali (temperatura, distanza, luce)
- Debuggare memoria con Valgrind
- Validare codice con test automatici

### 1.3 Stack Tecnologico 2025

Ecco gli strumenti che userete professionalmente:

```bash
# COMPILATORE C
gcc -std=c99 -Wall -Wextra -Wpedantic -Werror
# -std=c99: usa standard C99
# -Wall -Wextra: abilita TUTTI i warning
# -Wpedantic: rigoroso su standard
# -Werror: trasforma warning in errori (codice pulito!)

# STATIC ANALYSIS (trova bug PRIMA di eseguire)
cppcheck --enable=all mycode.c
# Trova: memory leak, buffer overflow, variabili non inizializzate

# MEMORY CHECKING (trova errori memoria DURANTE esecuzione)
valgrind --leak-check=full ./myprogram
# Trova: memory leak, use-after-free, double-free

# ARDUINO IDE 2.x (Interfaccia Grafica)
https://www.arduino.cc/en/software
# Features 2025: autocomplete, debug integrato, multi-board

# PLATFORMIO (Alternativa Pro per VSCode)
VSCode + PlatformIO Extension
# Per sviluppatori avanzati: multi-board, testing, CI/CD

# IA ASSISTENTI
- GitHub Copilot (autocomplete AI nel tuo editor)
- Claude Code (Claude 3.5 Sonnet - questo strumento!)
- ChatGPT (GPT-4 Turbo - conversazioni complesse)
- Cursor IDE (editor con IA integrata)
```

**Come scegliere?**

| Tool | Quando Usarlo |
|------|---------------|
| **gcc con flag strict** | Sempre, per compilare codice C |
| **cppcheck** | Prima di commit git, per static analysis |
| **valgrind** | Quando sospetti memory leak |
| **Arduino IDE 2.x** | Principianti, prototipi rapidi |
| **PlatformIO** | Progetti grandi, team, multi-board |
| **Copilot** | Autocomplete mentre scrivi |
| **Claude/GPT-4** | Spiegazioni, debugging, architettura |

### 1.4 Differenze C vs Python vs JavaScript

Molti di voi conoscono Python o JavaScript. Ecco le differenze chiave:

```c
// ===== C: COMPILATO, STATICO, ESPLICITO =====
#include <stdio.h>

int main(void) {
    int x = 42;              // Tipo ESPLICITO
    float y = 3.14;          // Devi dichiarare tipo

    printf("%d\n", x);       // Funzione C standard

    return 0;                // Codice uscita
}
// Compilazione: gcc file.c -o program
// Esecuzione: ./program
```

```python
# ===== PYTHON: INTERPRETATO, DINAMICO, IMPLICITO =====
x = 42          # Tipo inferito automaticamente
y = 3.14        # Python decide: float

print(x)        # Built-in function

# Esecuzione diretta: python file.py
```

```javascript
// ===== JAVASCRIPT: INTERPRETATO, DINAMICO =====
let x = 42;     // Tipo inferito
let y = 3.14;

console.log(x);

// Esecuzione: node file.js (Node) o browser
```

**Differenze Fondamentali:**

| Caratteristica | C | Python | JavaScript |
|----------------|---|--------|------------|
| **Tipo** | Compilato | Interpretato | Interpretato |
| **Tipi variabili** | Statici, espliciti | Dinamici | Dinamici |
| **Memoria** | Manuale (malloc/free) | Automatica (GC) | Automatica (GC) |
| **Velocità** | ⚡ Velocissimo | 🐢 Lento | 🏃 Medio-veloce |
| **Controllo HW** | ✅ Totale | ❌ Limitato | ❌ Limitato (solo Node) |
| **Learning curve** | 📈 Ripida | 📉 Gentile | 📊 Media |

**Quando usare C:**
- Serve velocità massima (real-time, DSP)
- Risorse limitate (microcontrollori con 32KB RAM!)
- Controllo hardware diretto (GPIO, ADC, I2C)
- Sistemi embedded/IoT

**Esempio pratico:**
```c
// C: Devi gestire TUTTO esplicitamente
int *arr = malloc(100 * sizeof(int));  // Alloca memoria manualmente
if (arr == NULL) {
    // Gestisci errore allocazione
}
free(arr);  // Libera memoria manualmente
```

```python
# Python: Garbage collector fa tutto automaticamente
arr = [0] * 100  # Lista creata automaticamente
# Memoria liberata automaticamente quando arr non serve più
```

**Perché questa differenza?**

C ti dà **controllo totale** ma richiede **responsabilità totale**. È come guidare un'auto manuale vs automatica: più difficile ma più efficiente e potente quando serve prestazioni massime.

---

## 2. Fondamenti del Linguaggio C con IA

### 2.1 Caratteristiche Critiche del C

Il C ha caratteristiche che lo rendono potentissimo ma anche pericoloso se usato male. L'IA può aiutarvi, ma dovete **capire** queste caratteristiche per validare il codice generato.

#### 2.1.1 Gestione Esplicita della Memoria

```c
// 1. GESTIONE ESPLICITA MEMORIA
int *ptr = malloc(100 * sizeof(int));  // Tu allochi
free(ptr);                              // Tu liberi
ptr = NULL;                             // Evita dangling pointer

// Analogia: malloc = prendere in affitto un appartamento
//           free = restituirlo quando finisci
//           ptr = NULL = buttare via le chiavi (non puoi rientrare)
```

**Cosa significa?**

In Python/JavaScript la memoria viene gestita automaticamente. In C **SEI TU** responsabile:
- Allocare memoria quando serve (`malloc`)
- Liberarla quando finisci (`free`)
- Non usarla dopo averla liberata

**Esempio reale:**

```c
// ❌ ERRORE: Memory Leak (perdita memoria)
void process_data() {
    int *data = malloc(1000 * sizeof(int));

    // ... uso data ...

    // ❌ DIMENTICATO free(data)!
}  // Memoria persa per sempre!

// Se chiami process_data() 1000 volte, perdi
// 1000 * 1000 * 4 bytes = 4 MB di RAM!
```

**Analogia:** È come lasciare l'acqua aperta ogni volta che ti lavi i denti. Dopo un po' allaghi la casa!

#### 2.1.2 Puntatori: Potenza e Pericolo

```c
// 2. PUNTATORI (Potenza e Pericolo)
int x = 42;
int *p = &x;  // p punta all'indirizzo di x
*p = 100;     // x ora vale 100

// Visualizziamo la memoria:
// Indirizzo    Valore    Variabile
// 0x1000       100       x
// 0x2000       0x1000    p (contiene indirizzo di x)
```

**Cosa sono i puntatori?**

Un puntatore è una variabile che contiene un **indirizzo di memoria**. È come avere l'indirizzo di casa di qualcuno invece della persona stessa.

**Analogia:**
- `int x = 42` → Hai una scatola con "42" scritto sopra
- `int *p = &x` → Hai un foglietto con l'indirizzo della scatola
- `*p = 100` → Vai all'indirizzo sul foglietto e cambi il contenuto della scatola

**Puntatori permettono:**
- Passare dati grandi senza copiarli (efficienza)
- Modificare variabili nelle funzioni
- Strutture dati dinamiche (liste, alberi)
- Accesso diretto alla memoria hardware

**Ma sono PERICOLOSI:**

```c
// ❌ ERRORE: Dereferenziare NULL
int *p = NULL;
*p = 42;  // CRASH! Stai scrivendo in memoria non valida

// ❌ ERRORE: Puntatore a variabile locale
int* dangerous_function() {
    int x = 42;
    return &x;  // ❌ x viene distrutta alla fine della funzione!
}

// ❌ ERRORE: Dangling pointer
int *p = malloc(100);
free(p);
*p = 42;  // ❌ Stai usando memoria già liberata!
```

#### 2.1.3 Array = Puntatori

```c
// 3. ARRAY = PUNTATORI
int arr[5];
arr[0] = 1;     // Accesso array normale
*(arr + 0) = 1; // Equivalente con aritmetica puntatori!

// Questi sono TUTTI equivalenti:
arr[2]        // Modo standard
*(arr + 2)    // Aritmetica puntatori
2[arr]        // Valido ma bizzarro! (non usatelo)
```

**Spiegazione:**

In C, il nome dell'array (`arr`) è in realtà un **puntatore costante** al primo elemento. Quando scrivi `arr[2]`, il compilatore traduce in `*(arr + 2)`:

1. `arr` punta al primo elemento
2. `arr + 2` sposta il puntatore di 2 posizioni
3. `*(arr + 2)` accede al valore a quell'indirizzo

**Visualizzazione memoria:**

```
Memoria:
Indirizzo  Valore  Notazione
0x1000     10      arr[0] o *arr
0x1004     20      arr[1] o *(arr+1)
0x1008     30      arr[2] o *(arr+2)
0x100C     40      arr[3] o *(arr+3)
0x1010     50      arr[4] o *(arr+4)
```

#### 2.1.4 NESSUN Controllo Bounds

```c
// 4. NESSUN CONTROLLO BOUNDS
int arr[5];
arr[100] = 42;  // ❌ COMPILA ma è UNDEFINED BEHAVIOR
                // Stai scrivendo in memoria casuale!

// Python farebbe:
# arr = [0] * 5
# arr[100] = 42  → IndexError: list index out of range

// C NON controlla! Può:
// - Sovrascrivere altre variabili
// - Crashare il programma
// - Creare vulnerabilità di sicurezza (buffer overflow)
```

**Perché C non controlla?**

Performance! Controllare i bounds ad ogni accesso costa tempo CPU. C assume che il programmatore sappia cosa sta facendo. Ma questo significa **TU** devi controllare.

**Esempio reale di buffer overflow:**

```c
// Codice vulnerabile (può essere sfruttato da attaccanti!)
void copy_string(char *dest) {
    char input[10];
    gets(input);      // ❌ PERICOLOSISSIMO! No bounds check
    strcpy(dest, input);  // ❌ Può sovrascrivere memoria
}

// Attaccante invia 100 caratteri invece di 10:
// → Sovrascrive memoria adiacente
// → Può modificare return address della funzione
// → Può eseguire codice arbitrario (exploit!)
```

Questo tipo di vulnerabilità è stato responsabile di migliaia di exploit reali. Ecco perché è **FONDAMENTALE** validare il codice generato dall'IA!

### 2.2 Standard C99 - Raccomandato 2025

**Perché C99 e non C11/C17/C23?**

C ha avuto diverse versioni:
- **C89/C90** (1989-1990): Primo standard ufficiale
- **C99** (1999): Aggiunte importanti, widely supported ⭐
- **C11** (2011): Thread, atomics
- **C17** (2017): Bug fix C11
- **C23** (2023): Nuovissimo, non ancora universale

**C99 è il "sweet spot":**
- ✅ Moderno ma universalmente supportato
- ✅ Balance tra features e portabilità
- ✅ Supporto completo su embedded/Arduino
- ✅ Compatibile con tutti i compilatori professionali
- ✅ Tutte le features utili per embedded

```c
// ===== FEATURES C99 vs C89 =====

// ❌ C89: Dichiarazioni solo all'inizio blocco
void func_c89(void) {
    int i;
    int sum = 0;

    for (i = 0; i < 10; i++) {
        sum += i;
    }
}

// ✅ C99: Dichiarazione variabili ovunque
void func_c99(void) {
    int sum = 0;

    // Variabile nel for (comodo!)
    for (int i = 0; i < 10; i++) {
        sum += i;
    }

    // Dichiarazioni miste al codice
    printf("Sum: %d\n", sum);
    int result = sum * 2;
}

// ✅ C99: Tipo bool
#include <stdbool.h>
bool is_valid = true;
if (is_valid) { /*...*/ }

// ❌ C89: Usavano int come bool
int is_valid = 1;  // 1=true, 0=false

// ✅ C99: Tipi dimensione fissa
#include <stdint.h>
uint8_t byte = 255;        // Esattamente 8 bit
int32_t num = -1000000;    // Esattamente 32 bit
uint64_t big = 1ULL << 40; // Esattamente 64 bit

// ❌ C89: Dimensioni variabili
int x;  // 16 bit? 32 bit? Dipende dalla piattaforma!

// ✅ C99: Commenti inline // (come C++)
int x = 42;  // Questa è la risposta

// ❌ C89: Solo commenti /* */
int x = 42;  /* Commento vecchio stile */

// ✅ C99: long long per numeri grandi
long long big = 9223372036854775807LL;

// ✅ C99: Array flessibili in struct
typedef struct {
    int length;
    int data[];  // Flexible array member
} Buffer;
```

**Come richiedere C99 nei prompt:**

```
"Scrivi in C99 standard una funzione che..."
"Usa SOLO C99 standard library, NO estensioni POSIX/GNU"
"Compila con: gcc -std=c99 -Wall -Wextra -Wpedantic -Werror"
```

### 2.3 Header Files Essenziali

Gli header file contengono dichiarazioni di funzioni e macro. Ecco quelli essenziali:

```c
// ===== I/O =====
#include <stdio.h>
// printf, scanf, fprintf, fgets, fopen, fclose, etc.

printf("Hello %s\n", name);           // Stampa formattata
scanf("%d", &number);                 // Leggi input
FILE *f = fopen("data.txt", "r");    // Apri file
fgets(line, sizeof(line), f);        // Leggi riga
fclose(f);                            // Chiudi file

// ===== MEMORIA =====
#include <stdlib.h>
// malloc, free, calloc, realloc, exit, rand

int *arr = malloc(n * sizeof(int));   // Alloca memoria
free(arr);                            // Libera memoria
int *zeros = calloc(n, sizeof(int));  // Alloca e azzera
arr = realloc(arr, new_size);         // Ridimensiona
exit(1);                              // Termina programma
int random = rand();                  // Numero casuale

// ===== STRINGHE E MEMORIA =====
#include <string.h>
// strlen, strcpy, strcmp, strcat, memcpy, memset

size_t len = strlen(str);              // Lunghezza stringa
strcpy(dest, src);                     // Copia stringa (PERICOLOSO!)
int cmp = strcmp(s1, s2);              // Confronta (0=uguali)
strcat(dest, src);                     // Concatena (PERICOLOSO!)
memcpy(dest, src, n);                  // Copia n byte
memset(buffer, 0, size);               // Riempi buffer

// ===== BOOLEANI (C99+) =====
#include <stdbool.h>
// bool, true, false

bool is_valid = true;
if (is_valid) { /*...*/ }

// ===== TIPI DIMENSIONE FISSA (C99+) =====
#include <stdint.h>
// int8_t, uint8_t, int16_t, uint16_t, int32_t, uint32_t, int64_t, uint64_t

uint8_t byte = 255;           // 0-255 (1 byte)
int16_t temperature = -40;    // -32768 a 32767
uint32_t counter = 4000000000; // 0 a 4 miliardi
int64_t big_num = 1LL << 50;  // Numeri enormi

// ===== ASSERT (TESTING) =====
#include <assert.h>
// assert()

assert(ptr != NULL);          // Crash se falso (solo in debug)
assert(x > 0 && x < 100);     // Validazione precondizioni

// ===== MATEMATICA =====
#include <math.h>
// sin, cos, sqrt, pow, log, exp, floor, ceil

double root = sqrt(16.0);     // 4.0
double power = pow(2.0, 10);  // 1024.0
double angle = sin(3.14159);

// Compila con -lm: gcc prog.c -o prog -lm

// ===== TEMPO =====
#include <time.h>
// time, clock, difftime

time_t now = time(NULL);              // Timestamp corrente
clock_t start = clock();              // CPU time
// ... codice ...
clock_t end = clock();
double seconds = (double)(end-start)/CLOCKS_PER_SEC;

// ===== CARATTERI =====
#include <ctype.h>
// isdigit, isalpha, toupper, tolower

if (isdigit(ch)) { /*...*/ }  // È un numero?
char upper = toupper('a');     // 'A'
```

**Mappa Mentale - Quando usare cosa:**

```
Devo fare I/O? → stdio.h
Devo allocare memoria? → stdlib.h
Lavoro con stringhe? → string.h
Serve bool? → stdbool.h (C99)
Dimensioni precise (uint8_t)? → stdint.h (C99)
Testing/validazione? → assert.h
Calcoli matematici? → math.h
Timestamp/timing? → time.h
```

### 2.4 Anatomia di un Programma C

Vediamo la struttura completa di un programma C professionale:

```c
// ===== 1. COMMENTO HEADER =====
/*
 * File: calcola_media.c
 * Descrizione: Calcola media di array di numeri
 * Autore: Studente ITS
 * Data: 2025-01-15
 * Versione: 1.0
 */

// ===== 2. INCLUDE =====
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// ===== 3. MACRO DEFINE =====
#define MAX_SIZE 100
#define DEBUG 1

// ===== 4. TYPEDEF (tipi custom) =====
typedef struct {
    int *data;
    int size;
    int capacity;
} Array;

// ===== 5. DICHIARAZIONI FUNZIONI (prototipi) =====
bool calcola_media(const int *arr, int n, double *result);
void stampa_array(const int *arr, int n);

// ===== 6. FUNZIONE MAIN =====
int main(void) {
    // Variabili
    int numeri[] = {10, 20, 30, 40, 50};
    int n = sizeof(numeri) / sizeof(numeri[0]);
    double media;

    // Logica
    if (calcola_media(numeri, n, &media)) {
        printf("Media: %.2f\n", media);
    } else {
        fprintf(stderr, "Errore calcolo media\n");
        return 1;
    }

    return 0;  // 0 = successo
}

// ===== 7. IMPLEMENTAZIONI FUNZIONI =====
bool calcola_media(const int *arr, int n, double *result) {
    if (arr == NULL || result == NULL || n <= 0) {
        return false;
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    *result = (double)sum / n;
    return true;
}

void stampa_array(const int *arr, int n) {
    if (arr == NULL || n <= 0) return;

    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n - 1) printf(", ");
    }
    printf("]\n");
}
```

**Ordine Importanza:**

1. **Include** - Librerie necessarie
2. **Define/Typedef** - Costanti e tipi custom
3. **Prototipi** - Dichiarazioni funzioni (se usi funzioni prima di definirle)
4. **main()** - Punto d'ingresso programma
5. **Implementazioni** - Definizioni funzioni

---

## 3. Template Prompt per C

### 3.1 Template Universale Funzione C

Questo è il template che userete per generare codice C professionale con l'IA:

```
# TEMPLATE FUNZIONE C 2025

Scrivi in **C99 standard** una funzione:

## Firma
```c
[tipo_ritorno] nome_funzione([parametri]);
```

## Comportamento
[Descrizione dettagliata cosa deve fare]

## Vincoli Tecnici
- Standard: C99
- NO estensioni POSIX/GNU
- NO funzioni non-standard (strdup, strndup, asprintf, getline)
- Usa SOLO librerie standard C

## Gestione Errori
- Controlla puntatori NULL
- Controlla bounds array
- Ritorna [codice errore / bool / NULL] in caso errore
- Usa defensive programming

## Gestione Memoria
- Se alloca memoria: documenta chi deve liberarla
- NO memory leak
- NO double free
- Inizializza puntatori a NULL dopo free

## Input/Output
Input: [specifica parametri]
Output: [specifica return value]
Side effects: [modifica parametri? I/O? File?]

## Testing
Genera anche test con assert.h per:
- Caso normale (happy path)
- Edge cases (NULL, 0, vuoti, stringhe vuote)
- Boundary conditions (limiti min/max)

## Output Richiesto
1. Codice funzione commentato
2. Suite test completa
3. Note su possibili miglioramenti
```

**Perché questo template funziona?**

- **Firma esplicita** → IA sa esattamente cosa implementare
- **Vincoli tecnici** → Evita funzioni non-standard
- **Gestione errori** → Codice robusto
- **Testing** → Codice validato automaticamente

### 3.2 Esempio Pratico Template

**Problema reale:** Voglio concatenare due stringhe in modo sicuro.

**Prompt usando template:**

```
# TEMPLATE FUNZIONE C 2025

Scrivi in **C99 standard** una funzione:

## Firma
```c
char* safe_string_concat(const char *s1, const char *s2);
```

## Comportamento
Concatena due stringhe allocando nuova memoria per il risultato.
Se una stringa è NULL, trattala come stringa vuota "".

## Vincoli Tecnici
- Standard: C99
- NO estensioni POSIX/GNU (NO strdup!)
- NO funzioni non-standard

## Gestione Errori
- Se s1 o s2 sono NULL, trattali come stringa vuota
- Se malloc fallisce, ritorna NULL
- Documenta che caller deve chiamare free()

## Gestione Memoria
- Alloca memoria per risultato (lunghezza s1 + s2 + 1)
- CALLER deve liberare la memoria ritornata con free()

## Input/Output
Input: s1 (può essere NULL), s2 (può essere NULL)
Output: Nuova stringa allocata, o NULL se errore malloc
Side effects: Alloca memoria heap

## Testing
Test con:
- Stringhe normali ("Hello", "World")
- Una o entrambe NULL
- Stringhe vuote ""
- Stringhe molto lunghe

## Output Richiesto
1. Implementazione funzione completa
2. Suite test con assert.h
3. Esempio uso con free()
```

**Output IA (Claude 3.5):**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

/**
 * @brief Concatena due stringhe in modo sicuro
 *
 * Alloca nuova memoria per contenere s1 + s2.
 * Gestisce NULL come stringhe vuote.
 *
 * @param s1 Prima stringa (può essere NULL)
 * @param s2 Seconda stringa (può essere NULL)
 * @return Nuova stringa allocata o NULL se errore malloc
 *
 * @note Il CALLER deve liberare la memoria con free()
 *
 * @example
 * char *result = safe_string_concat("Hello ", "World");
 * if (result != NULL) {
 *     printf("%s\n", result);
 *     free(result);
 * }
 */
char* safe_string_concat(const char *s1, const char *s2) {
    // Gestione NULL come stringhe vuote
    const char *str1 = (s1 != NULL) ? s1 : "";
    const char *str2 = (s2 != NULL) ? s2 : "";

    // Calcola lunghezza totale
    size_t len1 = strlen(str1);
    size_t len2 = strlen(str2);
    size_t total_len = len1 + len2 + 1;  // +1 per '\0'

    // Allocazione memoria
    char *result = malloc(total_len);
    if (result == NULL) {
        return NULL;  // Errore allocazione
    }

    // Copia stringhe usando memcpy (più efficiente di strcpy)
    memcpy(result, str1, len1);
    memcpy(result + len1, str2, len2);
    result[len1 + len2] = '\0';  // Null terminator

    return result;
}

// ===== SUITE TEST =====
void test_safe_string_concat(void) {
    char *result;

    // Test 1: Stringhe normali
    result = safe_string_concat("Hello ", "World");
    assert(result != NULL);
    assert(strcmp(result, "Hello World") == 0);
    free(result);
    printf("✓ Test 1: Stringhe normali\n");

    // Test 2: Prima stringa NULL
    result = safe_string_concat(NULL, "World");
    assert(result != NULL);
    assert(strcmp(result, "World") == 0);
    free(result);
    printf("✓ Test 2: Prima stringa NULL\n");

    // Test 3: Seconda stringa NULL
    result = safe_string_concat("Hello", NULL);
    assert(result != NULL);
    assert(strcmp(result, "Hello") == 0);
    free(result);
    printf("✓ Test 3: Seconda stringa NULL\n");

    // Test 4: Entrambe NULL
    result = safe_string_concat(NULL, NULL);
    assert(result != NULL);
    assert(strcmp(result, "") == 0);
    free(result);
    printf("✓ Test 4: Entrambe NULL\n");

    // Test 5: Stringhe vuote
    result = safe_string_concat("", "");
    assert(result != NULL);
    assert(strcmp(result, "") == 0);
    free(result);
    printf("✓ Test 5: Stringhe vuote\n");

    // Test 6: Mix vuota e piena
    result = safe_string_concat("", "Test");
    assert(result != NULL);
    assert(strcmp(result, "Test") == 0);
    free(result);
    printf("✓ Test 6: Mix vuota e piena\n");

    printf("\n✅ Tutti i test safe_string_concat passati!\n");
}

int main(void) {
    test_safe_string_concat();

    // Esempio uso
    printf("\n--- Esempio Uso ---\n");
    char *greeting = safe_string_concat("Hello ", "ITS Students!");
    if (greeting != NULL) {
        printf("%s\n", greeting);
        free(greeting);  // ✅ IMPORTANTE: libera memoria!
    }

    return 0;
}
```

**Compilazione e test:**

```bash
gcc -std=c99 -Wall -Wextra -Wpedantic -Werror concat.c -o concat
./concat

# Output:
# ✓ Test 1: Stringhe normali
# ✓ Test 2: Prima stringa NULL
# ✓ Test 3: Seconda stringa NULL
# ✓ Test 4: Entrambe NULL
# ✓ Test 5: Stringhe vuote
# ✓ Test 6: Mix vuota e piena
#
# ✅ Tutti i test safe_string_concat passati!
#
# --- Esempio Uso ---
# Hello ITS Students!
```

**Punti chiave codice generato:**

1. ✅ Gestisce NULL correttamente
2. ✅ Controllo errore malloc
3. ✅ Usa `memcpy` (più efficiente)
4. ✅ Documenta responsabilità free()
5. ✅ Suite test completa
6. ✅ Commenti Doxygen
7. ✅ Nessun warning con flag strict

### 3.3 Template Debugging C

Quando l'IA genera codice che non funziona, usate questo template:

```
# DEBUGGING C CON IA

Ho questo codice C che genera errore:

```c
[INCOLLA CODICE COMPLETO]
```

## Errore Compilatore
```
[INCOLLA MESSAGGIO ERRORE COMPLETO, incluso file:linea]
```

## Contesto
- Compilatore: gcc [versione]
- Flag usati: -std=c99 -Wall -Wextra
- Sistema operativo: [Linux/Mac/Windows]
- Cosa dovrebbe fare: [descrizione comportamento atteso]
- Cosa succede invece: [comportamento effettivo]

## Richiesta
Analizza e fornisci:
1. **Causa root** dell'errore (perché succede)
2. **Spiegazione** tecnica dettagliata
3. **Fix** con codice corretto e commentato
4. **Best practice** per evitare errore in futuro
5. **Test** per validare il fix

[OPZIONALE] Se hai già provato fix che non funzionano, elencali qui.
```

**Esempio pratico debugging:**

```
# DEBUGGING C CON IA

Ho questo codice C che genera warning:

```c
#include <stdio.h>

int main() {
    char *name = "Mario";
    name[0] = 'L';  // Voglio cambiare Mario in Lario
    printf("%s\n", name);
    return 0;
}
```

## Errore Compilatore
```
test.c:5:5: warning: assignment discards 'const' qualifier from pointer type
test.c:6:10: warning: format '%s' expects argument of type 'char *', but argument 2 has type 'const char *'
Segmentation fault (core dumped)
```

## Contesto
- Compilatore: gcc 11.3.0
- Flag: -std=c99 -Wall
- Sistema: Linux
- Dovrebbe fare: Cambiare prima lettera nome
- Succede: Crash con Segmentation fault

## Richiesta
[come sopra]
```

**Risposta IA:**

```markdown
## 1. Causa Root

String literal `"Mario"` è allocata in **memoria READ-ONLY** (sezione `.rodata` dell'eseguibile).
Tentare di modificarla con `name[0] = 'L'` causa **Segmentation Fault** perché stai scrivendo in memoria protetta.

## 2. Spiegazione Tecnica

```c
char *name = "Mario";  // Puntatore a stringa COSTANTE
```

In C, string literals sono **implicitamente const**. Il compilatore le alloca in memoria read-only.
La memoria del processo è divisa in sezioni:

```
+-----------------+
| .text (codice)  | ← READ-ONLY
+-----------------+
| .rodata (const) | ← String literals qui! READ-ONLY
+-----------------+
| .data (globali) | ← READ-WRITE
+-----------------+
| .bss (uninit)   | ← READ-WRITE
+-----------------+
| Heap (malloc)   | ← READ-WRITE
+-----------------+
| Stack (locali)  | ← READ-WRITE
+-----------------+
```

Quando scrivi `name[0] = 'L'`, il sistema operativo rileva scrittura in `.rodata` e termina il programma.

## 3. Fix

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    // ✅ OPZIONE 1: Array su stack (modificabile)
    char name1[] = "Mario";  // Copia stringa su stack
    name1[0] = 'L';
    printf("%s\n", name1);  // Lario

    // ✅ OPZIONE 2: Allocazione dinamica
    char *name2 = malloc(6);  // 5 char + '\0'
    if (name2 == NULL) {
        return 1;
    }
    strcpy(name2, "Mario");
    name2[0] = 'L';
    printf("%s\n", name2);  // Lario
    free(name2);

    // ✅ OPZIONE 3: const esplicito (se non modifichi)
    const char *name3 = "Mario";  // Esplicita che è costante
    printf("%s\n", name3);  // Mario

    return 0;
}
```

## 4. Best Practices

```c
// ❌ MAI fare questo
char *s = "string literal";
s[0] = 'x';  // CRASH!

// ✅ Se NON modifichi: usa const
const char *s = "string literal";

// ✅ Se DEVI modificare: usa array
char s[] = "string literal";

// ✅ Se dimensione variabile: usa malloc
char *s = malloc(size);
```

**Regola pratica:**
- `char *s = "..."` → READ-ONLY, usa `const char *`
- `char s[] = "..."` → MODIFICABILE, su stack
- `char *s = malloc(...)` → MODIFICABILE, su heap

## 5. Test Validazione

```c
#include <assert.h>
#include <string.h>

void test_string_modification() {
    // Test array modificabile
    char name[] = "Mario";
    name[0] = 'L';
    assert(strcmp(name, "Lario") == 0);

    // Test malloc modificabile
    char *dynamic = malloc(6);
    assert(dynamic != NULL);
    strcpy(dynamic, "Mario");
    dynamic[0] = 'L';
    assert(strcmp(dynamic, "Lario") == 0);
    free(dynamic);

    printf("✅ Test passati!\n");
}
```
```

Questo tipo di debugging guidato dall'IA è estremamente potente per imparare!

### 3.4 Template Code Review

Quando avete codice funzionante ma volete migliorarlo:

```
# CODE REVIEW C CON IA

Rivedi questo codice C e suggerisci miglioramenti:

```c
[INCOLLA CODICE]
```

## Aspetti da Analizzare
1. **Sicurezza**: Buffer overflow? Memory leak? NULL dereferencing?
2. **Performance**: Algoritmo efficiente? Copie inutili?
3. **Portabilità**: Standard C99? Funzioni non-standard?
4. **Leggibilità**: Nomi variabili? Commenti? Struttura?
5. **Robustezza**: Gestione errori? Edge cases?
6. **Testing**: Test adeguati?

## Output Richiesto
Per ogni problema trovato:
- Gravità: CRITICO / ALTO / MEDIO / BASSO
- Descrizione problema
- Codice corretto
- Spiegazione fix
```

---

## 4. Problemi Ricorrenti Codice Generato

L'IA è potente ma commette errori ricorrenti. Impariamo a riconoscerli immediatamente!

### 4.1 Funzioni Non-Standard (MOLTO COMUNE!)

**Problema:** L'IA spesso suggerisce funzioni **POSIX** o **GNU** che non esistono nello standard C.

```c
// ❌ IA POTREBBE GENERARE (POSIX, non C standard):
char *copy = strdup(original);       // strdup = POSIX extension!
char *dup = strndup(original, 10);   // strndup = GNU extension!
int result = asprintf(&str, "x=%d", val);  // GNU extension!
ssize_t len = getline(&line, &n, fp);      // POSIX!

// ✅ VERSIONE C99 STANDARD:
// Implementiamo strdup manualmente
char *my_strdup(const char *src) {
    if (src == NULL) {
        return NULL;
    }

    size_t len = strlen(src) + 1;  // +1 per '\0'
    char *dst = malloc(len);

    if (dst != NULL) {
        memcpy(dst, src, len);
    }

    return dst;
}

// Uso:
char *copy = my_strdup("Hello");
if (copy != NULL) {
    printf("%s\n", copy);
    free(copy);
}
```

**Perché l'IA fa questo errore?**

I LLM sono addestrati su codice reale da GitHub/Stack Overflow dove `strdup` è usatissimo su sistemi Linux/Unix. Ma noi vogliamo codice **portabile** che funziona ovunque (Windows, embedded, compilatori diversi).

**Come prevenire:**

Nei prompt specificate sempre:

```
"Usa SOLO funzioni C99 standard library.
NO estensioni POSIX, GNU, BSD o specifiche compilatore.
NO: strdup, strndup, asprintf, getline, strlcpy
"
```

**Lista funzioni non-standard comuni da evitare:**

| Funzione Non-Standard | Standard Alternativa |
|-----------------------|----------------------|
| `strdup(s)` | `malloc + strcpy/memcpy` |
| `strndup(s, n)` | `malloc + strncpy` |
| `asprintf(&s, fmt, ...)` | `snprintf` per size, poi `malloc` |
| `getline(&line, &n, f)` | `fgets` in loop |
| `strlcpy(dst, src, size)` | `strncpy` + manual null-term |
| `strlcat(dst, src, size)` | `strncat` + bounds check |

### 4.2 Buffer Overflow (PERICOLOSISSIMO!)

**Problema:** Funzioni che non controllano dimensione buffer.

```c
// ❌ PERICOLOSO - Buffer overflow
void copy_user_input_bad() {
    char buffer[10];
    char input[100];

    fgets(input, sizeof(input), stdin);
    strcpy(buffer, input);  // ❌ NO BOUNDS CHECK!

    // Se input > 10 caratteri:
    // → Sovrascrive memoria adiacente
    // → Può crashare il programma
    // → Vulnerabilità di sicurezza!
}

// Esempio crash:
// Input: "Questa è una stringa molto lunga"
// buffer[10] può contenere max 9 char + '\0'
// strcpy scrive 34 caratteri!
// → Sovrascrive 24 byte oltre il buffer
// → CRASH o peggio: exploit

// ✅ SICURO - Bounds checking
void copy_user_input_safe() {
    char buffer[10];
    char input[100];

    if (fgets(input, sizeof(input), stdin) == NULL) {
        return;  // Errore lettura
    }

    // OPZIONE 1: strncpy (occhio al null terminator!)
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';  // Garantisci terminatore

    // OPZIONE 2: snprintf (RACCOMANDATO)
    snprintf(buffer, sizeof(buffer), "%s", input);

    printf("Buffer: %s\n", buffer);
}

// ✅ ALTERNATIVA: dimensione dinamica
void copy_user_input_dynamic() {
    char input[1000];

    if (fgets(input, sizeof(input), stdin) == NULL) {
        return;
    }

    // Alloca esattamente la dimensione necessaria
    size_t len = strlen(input);
    char *buffer = malloc(len + 1);

    if (buffer == NULL) {
        return;
    }

    strcpy(buffer, input);  // Sicuro: buffer dimensione corretta

    printf("Buffer: %s\n", buffer);
    free(buffer);
}
```

**Funzioni pericolose da evitare:**

| Funzione Pericolosa | Problema | Alternativa Sicura |
|---------------------|----------|---------------------|
| `strcpy(dst, src)` | No size check | `strncpy + null-term` o `snprintf` |
| `strcat(dst, src)` | No size check | `strncat` con size corretta |
| `gets(buf)` | NO SIZE! Deprecata! | `fgets(buf, size, stdin)` |
| `sprintf(buf, fmt, ...)` | No size check | `snprintf(buf, size, fmt, ...)` |
| `scanf("%s", buf)` | No size check | `scanf("%99s", buf)` con limit |

**Pattern sicuro universale:**

```c
// TEMPLATE COPIA STRINGA SICURA
void safe_string_copy(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    // Usa snprintf: garantisce null-termination e bounds
    snprintf(dest, dest_size, "%s", src);
}

// Uso:
char buffer[50];
safe_string_copy(buffer, sizeof(buffer), user_input);
```

### 4.3 Memory Leak

**Problema:** Dimenticare `free()` dopo `malloc()`.

```c
// ❌ IA POTREBBE DIMENTICARE free()
void process_data_leak(int n) {
    int *data = malloc(n * sizeof(int));

    if (data == NULL) {
        return;
    }

    // ... elaborazione ...
    for (int i = 0; i < n; i++) {
        data[i] = i * 2;
    }

    printf("Processati %d elementi\n", n);

    // ❌ MANCA: free(data);
}  // Memory leak! Memoria persa

// Se chiami process_data_leak(1000) 100 volte:
// Perdi: 1000 * 4 bytes * 100 = 400 KB
// Su embedded con 32 KB RAM → DISASTRO!

// ✅ VERSIONE CORRETTA
void process_data_safe(int n) {
    int *data = malloc(n * sizeof(int));

    if (data == NULL) {
        fprintf(stderr, "Errore: malloc fallita\n");
        return;
    }

    // ... elaborazione ...
    for (int i = 0; i < n; i++) {
        data[i] = i * 2;
    }

    printf("Processati %d elementi\n", n);

    free(data);       // ✅ Libera sempre
    data = NULL;      // ✅ Evita dangling pointer (opzionale ma buona pratica)
}
```

**Pattern con multiple exit point:**

```c
// ✅ GESTIONE MULTIPLI RETURN
bool process_file(const char *filename) {
    FILE *f = NULL;
    char *buffer = NULL;
    bool success = false;

    // Allocazione risorse
    f = fopen(filename, "r");
    if (f == NULL) {
        goto cleanup;  // ✅ Salta alla cleanup
    }

    buffer = malloc(1024);
    if (buffer == NULL) {
        goto cleanup;
    }

    // Processing
    if (fread(buffer, 1, 1024, f) == 0) {
        goto cleanup;
    }

    // Success
    success = true;

cleanup:
    // ✅ Libera SEMPRE risorse
    if (f != NULL) {
        fclose(f);
    }
    if (buffer != NULL) {
        free(buffer);
    }

    return success;
}
```

**Come rilevare memory leak:**

```bash
# Compila con debug
gcc -g -std=c99 program.c -o program

# Esegui con valgrind
valgrind --leak-check=full ./program

# Output se c'è leak:
# ==12345== 400 bytes in 1 blocks are definitely lost
# ==12345==    at malloc (vg_replace_malloc.c:299)
# ==12345==    by process_data_leak (program.c:15)
```

### 4.4 Dereferenziazione NULL

**Problema:** Usare puntatore senza controllare se è NULL.

```c
// ❌ IA POTREBBE NON CONTROLLARE
void process_array_crash(int *arr, int n) {
    // ❌ Assume arr non è NULL!
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;  // CRASH se arr == NULL!
    }
}

// Chiamata:
process_array_crash(NULL, 10);  // SEGMENTATION FAULT!

// ✅ PATTERN DIFENSIVO
bool process_array_safe(int *arr, int n) {
    // ✅ SEMPRE validare input
    if (arr == NULL) {
        fprintf(stderr, "Errore: array è NULL\n");
        return false;
    }

    if (n <= 0) {
        // Array vuoto non è errore
        return true;
    }

    // Processing sicuro
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
    }

    return true;
}

// ✅ Uso con controllo errore
int arr[10];
if (!process_array_safe(arr, 10)) {
    fprintf(stderr, "Elaborazione fallita\n");
    return 1;
}
```

**Defensive programming pattern:**

```c
// TEMPLATE FUNZIONE ROBUSTA
int my_function(void *ptr, int size, const char *name) {
    // ===== VALIDAZIONE INPUT =====
    if (ptr == NULL) {
        fprintf(stderr, "Errore: ptr è NULL\n");
        return -1;
    }

    if (size <= 0) {
        fprintf(stderr, "Errore: size non valido (%d)\n", size);
        return -1;
    }

    if (name == NULL || strlen(name) == 0) {
        fprintf(stderr, "Errore: name non valido\n");
        return -1;
    }

    // ===== PROCESSING =====
    // ... logica sicura ...

    return 0;  // Successo
}
```

### 4.5 Checklist Validazione Codice IA

**Stampate e appendete questa checklist!**

```c
// ✅ CHECKLIST VALIDAZIONE CODICE GENERATO DA IA

// ═══════════════════════════════════════════
// 1. FUNZIONI STANDARD?
// ═══════════════════════════════════════════
// ❓ Tutte le funzioni sono in C99 stdlib?
// ❓ NO strdup, strndup, asprintf, getline?
// ❓ NO estensioni POSIX/GNU/BSD?

// Test: Compila con -std=c99 -pedantic senza errori?

// ═══════════════════════════════════════════
// 2. CONTROLLO NULL?
// ═══════════════════════════════════════════
// ❓ Ogni puntatore è controllato prima dell'uso?
// ❓ Parametri funzione validati?
// ❓ Return value di malloc controllato?

// Pattern: if (ptr == NULL) return ERROR;

// ═══════════════════════════════════════════
// 3. BOUNDS CHECKING?
// ═══════════════════════════════════════════
// ❓ Array accessi controllati?
// ❓ NO strcpy, strcat, gets, sprintf?
// ❓ Usato strncpy/snprintf con size corretta?
// ❓ Garantito null terminator nelle stringhe?

// Test: Input molto lunghi non causano crash?

// ═══════════════════════════════════════════
// 4. GESTIONE MEMORIA?
// ═══════════════════════════════════════════
// ❓ Ogni malloc ha corrispondente free?
// ❓ free() chiamata in TUTTI i path (anche errori)?
// ❓ Puntatori = NULL dopo free? (opzionale ma buono)
// ❓ NO use-after-free?
// ❓ NO double-free?

// Test: valgrind --leak-check=full mostra 0 leak?

// ═══════════════════════════════════════════
// 5. GESTIONE ERRORI?
// ═══════════════════════════════════════════
// ❓ Funzione ritorna codice errore/bool/NULL?
// ❓ Errori gestiti, non ignorati?
// ❓ Messaggi errore informativi?
// ❓ Cleanup risorse anche in caso errore?

// Pattern: if (error) { cleanup(); return ERROR; }

// ═══════════════════════════════════════════
// 6. COMPILAZIONE STRICT?
// ═══════════════════════════════════════════
// ❓ gcc -std=c99 -Wall -Wextra -Wpedantic -Werror
// ❓ NO warning?
// ❓ NO implicit declarations?

// Comando: gcc -std=c99 -Wall -Wextra -Wpedantic -Werror file.c

// ═══════════════════════════════════════════
// 7. TESTING?
// ═══════════════════════════════════════════
// ❓ Test casi normali (happy path)?
// ❓ Test edge cases (NULL, 0, vuoti)?
// ❓ Test boundary (min/max values)?
// ❓ Valgrind pulito (no leak, no invalid access)?

// ═══════════════════════════════════════════
// 8. DOCUMENTAZIONE?
// ═══════════════════════════════════════════
// ❓ Commenti spiegano perché, non cosa?
// ❓ Documentata ownership memoria (chi fa free)?
// ❓ Precondizioni/postcondizioni chiare?

// ═══════════════════════════════════════════
// SE TUTTI ✅ → CODICE PRONTO PER PRODUZIONE!
// ═══════════════════════════════════════════
```

**Workflow validazione:**

```
1. IA genera codice
   ↓
2. Applica checklist (2-3 minuti)
   ↓
3. Se trova problemi → modifica prompt e rigenera
   ↓
4. Compila con flag strict
   ↓
5. Esegui test
   ↓
6. Esegui valgrind
   ↓
7. ✅ Deploy
```

---

## 5. Gestione Memoria e Puntatori

La gestione memoria è la parte **più critica** del C. Padroneggiare memoria = padroneggiare il C!

### 5.1 Le Quattro Aree di Memoria

Quando un programma C viene eseguito, il sistema operativo gli assegna memoria divisa in aree:

```
MEMORIA DI UN PROCESSO C

Alta ← Indirizzi
┌──────────────────┐
│   STACK          │ ← Variabili locali, parametri funzioni
│   (cresce ↓)     │   Allocazione AUTOMATICA
│                  │   Veloce ma dimensione limitata
├──────────────────┤
│   ↓              │
│                  │
│   (memoria       │
│    libera)       │
│                  │
│   ↑              │
├──────────────────┤
│   HEAP           │ ← malloc/free
│   (cresce ↑)     │   Allocazione MANUALE
│                  │   Lenta ma flessibile
├──────────────────┤
│   BSS            │ ← Variabili globali non inizializzate
│   (uninit data)  │   Automaticamente azzerate
├──────────────────┤
│   DATA           │ ← Variabili globali inizializzate
│   (init data)    │   Costanti, static
├──────────────────┤
│   TEXT (CODE)    │ ← Codice macchina del programma
│   (read-only)    │   Read-only, shared tra processi
└──────────────────┘
Bassa ← Indirizzi
```

**Esempio mapping codice → memoria:**

```c
#include <stdio.h>
#include <stdlib.h>

// ===== AREA DATA (globali inizializzate) =====
int global_init = 42;
const char *string_literal = "Hello";  // Puntatore in DATA, stringa in TEXT

// ===== AREA BSS (globali non inizializzate, auto-azzer) =====
int global_uninit;
static int file_static;

void demo_memory() {
    // ===== STACK (variabili locali) =====
    int local_var = 10;
    char local_array[100];

    // ===== HEAP (allocazione dinamica) =====
    int *heap_var = malloc(sizeof(int));

    printf("=== INDIRIZZI MEMORIA ===\n");
    printf("CODE (text):    %p  (funzione demo_memory)\n", (void*)demo_memory);
    printf("DATA (global):  %p  (global_init)\n", (void*)&global_init);
    printf("BSS  (global):  %p  (global_uninit)\n", (void*)&global_uninit);
    printf("STACK (local):  %p  (local_var)\n", (void*)&local_var);
    printf("HEAP (malloc):  %p  (heap_var)\n", (void*)heap_var);

    free(heap_var);
}

int main(void) {
    demo_memory();
    return 0;
}
```

**Output esempio (indirizzi variano ad ogni esecuzione):**

```
=== INDIRIZZI MEMORIA ===
CODE (text):    0x55555555522a  (funzione demo_memory)
DATA (global):  0x555555558010  (global_init)
BSS  (global):  0x555555558040  (global_uninit)
STACK (local):  0x7fffffffd9ec  (local_var)
HEAP (malloc):  0x5555555596b0  (heap_var)
```

Notate come:
- **Stack** ha indirizzi molto alti (`0x7fff...`)
- **Heap** ha indirizzi medi
- **DATA/BSS** hanno indirizzi bassi
- **CODE** ha indirizzi molto bassi

### 5.2 Allocazione Dinamica

```c
// ===== LE 4 FUNZIONI MEMORIA =====

// 1. malloc - Alloca memoria (contenuto RANDOM!)
void *malloc(size_t size);

int *arr = malloc(10 * sizeof(int));
// arr ora punta a 40 byte (10 * 4)
// Contenuto: ❌ NON inizializzato (valori casuali!)

// 2. calloc - Alloca e AZZERA memoria
void *calloc(size_t nmemb, size_t size);

int *arr2 = calloc(10, sizeof(int));
// arr2 punta a 40 byte AZZERATI
// Tutti gli elementi = 0

// 3. realloc - Ridimensiona blocco esistente
void *realloc(void *ptr, size_t new_size);

arr = realloc(arr, 20 * sizeof(int));
// arr ora punta a 80 byte
// ⚠️ Potrebbe spostare il blocco in memoria!
// ⚠️ Contenuto vecchio preservato, nuovo RANDOM

// 4. free - Libera memoria
void free(void *ptr);

free(arr);
arr = NULL;  // Buona pratica
```

**Pattern sicuro allocazione:**

```c
// ✅ TEMPLATE ALLOCAZIONE SICURA
int *arr = malloc(n * sizeof(int));

// SEMPRE controllare return value
if (arr == NULL) {
    fprintf(stderr, "Errore: malloc fallita per %zu byte\n",
            n * sizeof(int));
    return -1;
}

// Uso
for (int i = 0; i < n; i++) {
    arr[i] = i;
}

// SEMPRE liberare
free(arr);
arr = NULL;  // Previene use-after-free accidentale
```

**Differenza malloc vs calloc:**

```c
// malloc: memoria NON inizializzata
int *a = malloc(5 * sizeof(int));
// a[0] = ???? (random garbage)
// a[1] = ????
// Devi inizializzare manualmente!
for (int i = 0; i < 5; i++) {
    a[i] = 0;
}

// calloc: memoria AZZERATA automaticamente
int *b = calloc(5, sizeof(int));
// b[0] = 0
// b[1] = 0
// ...tutti 0

// Quando usare cosa?
// calloc: Se serve inizializzazione a zero (più lento)
// malloc: Se scrivi subito tutti i valori (più veloce)
```

**realloc avanzato:**

```c
// ✅ PATTERN realloc SICURO
int *arr = malloc(10 * sizeof(int));
if (arr == NULL) return -1;

// ... uso ...

// Ridimensiona
int *temp = realloc(arr, 20 * sizeof(int));
if (temp == NULL) {
    // ⚠️ realloc fallita MA arr è ancora valido!
    free(arr);  // Libera memoria originale
    return -1;
}

arr = temp;  // ✅ Aggiorna puntatore
// Ora arr punta al blocco nuovo (o stesso se c'era spazio)

// ❌ ERRORE COMUNE: Non controllare return
arr = realloc(arr, new_size);  // ❌ Se fallisce, perdi puntatore originale!
```

### 5.3 Errori Fatali Memoria

#### Errore 1: Double Free

```c
// ❌ DOUBLE FREE
int *ptr = malloc(100);
free(ptr);
free(ptr);  // ❌ CRASH! Undefined behavior

// Cosa succede:
// 1. malloc alloca blocco, aggiunge a lista free blocks
// 2. free(ptr) marca blocco come libero
// 3. free(ptr) ancora → tenta di liberare blocco già libero
// 4. Heap allocator si confonde → CRASH o corruzione

// ✅ FIX:
free(ptr);
ptr = NULL;  // Secondo free(NULL) è sicuro (no-op)
free(ptr);   // ✅ OK: free(NULL) non fa niente
```

#### Errore 2: Use After Free

```c
// ❌ USE AFTER FREE
int *ptr = malloc(100);
*ptr = 42;
free(ptr);      // Memoria rilasciata
*ptr = 100;     // ❌ UNDEFINED BEHAVIOR!

// Cosa può succedere:
// - Sembra funzionare (memoria non ancora riusata)
// - Crash (memoria riusata da altro)
// - Corruzione silente (memoria riusata, modifichi dati altrui)
// - Exploit di sicurezza

// ✅ FIX:
free(ptr);
ptr = NULL;
// Ora *ptr = 100 causerebbe crash immediato (meglio di corruzionesilente!)
```

#### Errore 3: Memory Leak

```c
// ❌ MEMORY LEAK
void leak_example() {
    while (1) {
        int *leak = malloc(1000);
        // ... uso leak ...
        // ❌ MANCA free(leak)
    }
    // Ogni iterazione perde 1000 byte
    // Dopo 1000 iterazioni → 1 MB perso
    // RAM esaurita → sistema rallenta o crash
}

// ✅ FIX:
void no_leak_example() {
    while (1) {
        int *data = malloc(1000);
        if (data == NULL) {
            break;  // malloc fallita, RAM finita
        }

        // ... uso data ...

        free(data);  // ✅ Libera sempre
    }
}
```

#### Errore 4: Uninitialized Memory

```c
// ❌ MEMORIA NON INIZIALIZZATA
int *arr = malloc(10 * sizeof(int));

for (int i = 0; i < 10; i++) {
    printf("%d ", arr[i]);  // ❌ Valori casuali!
}
// Output: 0 4234523 -12434 0 8765432 ...

// ✅ FIX 1: Inizializza manualmente
int *arr = malloc(10 * sizeof(int));
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}

// ✅ FIX 2: Usa calloc
int *arr = calloc(10, sizeof(int));  // Automaticamente azzerato
```

### 5.4 Puntatori e Array

```c
// ARRAY E PUNTATORI: PROFONDAMENTE LEGATI

int arr[5] = {10, 20, 30, 40, 50};

// ===== EQUIVALENZE =====
arr[2]        // Accesso normale
*(arr + 2)    // Aritmetica puntatori
2[arr]        // Valido ma oscuro (non usare!)

// Tutti ritornano: 30

// ===== PERCHÉ FUNZIONA? =====
// arr[i] è syntactic sugar per *(arr + i)
//
// Compilatore traduce:
// arr[2] → *(arr + 2)
//
// Aritmetica puntatori:
// arr + 2 significa "indirizzo arr + (2 * sizeof(int))"
//
// Visualizzazione:
// arr → 0x1000  (valore: 10)
// arr+1 → 0x1004  (valore: 20)
// arr+2 → 0x1008  (valore: 30) ← *(arr+2) legge questo

// ===== ARRAY DECADE A PUNTATORE =====
int *p = arr;  // OK: arr "decay" a puntatore al primo elemento

// Ma NON sono identici:
sizeof(arr)  // 20 (5 * sizeof(int))
sizeof(p)    // 8 (dimensione puntatore su 64-bit)

// ===== PASSAGGIO A FUNZIONE =====
void print_array(int arr[], int size) {
    // arr è un PUNTATORE, non array!
    // sizeof(arr) ritorna sizeof(int*), non dimensione array
    // Ecco perché serve parametro size separato

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

int main() {
    int data[5] = {1, 2, 3, 4, 5};

    // Questi sono equivalenti:
    print_array(data, 5);
    print_array(&data[0], 5);

    return 0;
}
```

**Aritmetica puntatori avanzata:**

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;

// Incremento
p++;        // p ora punta a arr[1]
*p;         // 20

p += 2;     // p ora punta a arr[3]
*p;         // 40

// Decremento
p--;        // p ora punta a arr[2]
*p;         // 30

// Differenza puntatori
int *start = arr;
int *end = arr + 5;
ptrdiff_t diff = end - start;  // 5 (elementi tra loro)

// ⚠️ Aritmetica puntatori funziona SOLO dentro stesso array!
int a[5], b[5];
int *pa = a;
int *pb = b;
pa - pb;  // ❌ UNDEFINED BEHAVIOR (array diversi)
```

### 5.5 Puntatori a Funzioni

I puntatori a funzione permettono "callbacks" e polimorfismo in C.

```c
// ===== DICHIARAZIONE PUNTATORE A FUNZIONE =====
int (*func_ptr)(int, int);
//    ↑         ↑
//    nome      parametri

// Si legge: "func_ptr è un puntatore a funzione che prende
//            (int, int) e ritorna int"

// ===== FUNZIONI DA ASSEGNARE =====
int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

int subtract(int a, int b) {
    return a - b;
}

// ===== ASSEGNAZIONE E CHIAMATA =====
int main(void) {
    int (*operation)(int, int);  // Dichiara puntatore

    operation = add;  // Assegna funzione (senza &)
    int result = operation(3, 4);  // Chiamata
    printf("%d\n", result);  // 7

    operation = multiply;
    result = operation(3, 4);
    printf("%d\n", result);  // 12

    return 0;
}

// ===== ARRAY DI PUNTATORI A FUNZIONE =====
int (*operations[])(int, int) = {add, multiply, subtract};

// Uso:
int res1 = operations[0](10, 5);  // add: 15
int res2 = operations[1](10, 5);  // multiply: 50
int res3 = operations[2](10, 5);  // subtract: 5

// ===== CALLBACK PATTERN =====
void foreach_element(int *arr, int n, void (*callback)(int)) {
    for (int i = 0; i < n; i++) {
        callback(arr[i]);
    }
}

void print_element(int x) {
    printf("%d ", x);
}

void print_squared(int x) {
    printf("%d ", x * x);
}

int main(void) {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;

    printf("Elementi: ");
    foreach_element(arr, n, print_element);
    printf("\n");  // Elementi: 1 2 3 4 5

    printf("Quadrati: ");
    foreach_element(arr, n, print_squared);
    printf("\n");  // Quadrati: 1 4 9 16 25

    return 0;
}
```

**Caso d'uso reale: qsort**

```c
#include <stdlib.h>

// qsort richiede funzione comparazione
int compare_int(const void *a, const void *b) {
    int ia = *(const int*)a;
    int ib = *(const int*)b);
    return ia - ib;  // Crescente
}

int main(void) {
    int arr[] = {5, 2, 8, 1, 9};
    int n = 5;

    // qsort usa puntatore a funzione compare_int
    qsort(arr, n, sizeof(int), compare_int);

    // arr ora: {1, 2, 5, 8, 9}

    return 0;
}
```

### 5.6 Valgrind - Il Detective della Memoria

Valgrind è uno strumento **essenziale** per sviluppo C. Trova errori che altrimenti sarebbero invisibili.

```bash
# ===== INSTALLAZIONE =====
# Linux
sudo apt install valgrind

# Mac
brew install valgrind

# Windows: usa WSL (Windows Subsystem for Linux)

# ===== USO BASE =====
# 1. Compila con debug info
gcc -g -std=c99 -Wall myprogram.c -o myprogram

# 2. Esegui con valgrind
valgrind --leak-check=full --show-leak-kinds=all ./myprogram

# ===== FLAG UTILI =====
valgrind \
    --leak-check=full \          # Mostra tutti leak dettagliati
    --show-leak-kinds=all \      # Tutti tipi leak
    --track-origins=yes \        # Traccia origine valori non inizializzati
    --verbose \                  # Output dettagliato
    --log-file=valgrind.log \    # Salva output in file
    ./myprogram
```

**Esempio con memory leak:**

```c
// leak.c
#include <stdlib.h>

int main(void) {
    int *leak = malloc(100);  // ❌ Dimenticato free
    return 0;
}
```

```bash
$ gcc -g -std=c99 leak.c -o leak
$ valgrind --leak-check=full ./leak

# Output:
==12345== HEAP SUMMARY:
==12345==     in use at exit: 100 bytes in 1 blocks
==12345==   total heap usage: 1 allocs, 0 frees, 100 bytes allocated
==12345==
==12345== 100 bytes in 1 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x4C2DB8F: malloc (vg_replace_malloc.c:299)
==12345==    by 0x40053E: main (leak.c:4)
==12345==
==12345== LEAK SUMMARY:
==12345==    definitely lost: 100 bytes in 1 blocks
```

**Come leggere output Valgrind:**

- ✅ `All heap blocks were freed -- no leaks are possible` → PERFETTO!
- ❌ `definitely lost` → Memory leak confermato
- ⚠️ `possibly lost` → Possibile leak (puntatori interni)
- ⚠️ `still reachable` → Memoria non liberata ma ancora accessibile (global)

**Esempio use-after-free:**

```c
// use_after_free.c
#include <stdlib.h>

int main(void) {
    int *ptr = malloc(sizeof(int));
    *ptr = 42;
    free(ptr);
    *ptr = 100;  // ❌ Use after free
    return 0;
}
```

```bash
$ valgrind ./use_after_free

# Output:
==12345== Invalid write of size 4
==12345==    at 0x400552: main (use_after_free.c:7)
==12345==  Address 0x5204040 is 0 bytes inside a block of size 4 free'd
==12345==    at 0x4C2EDEB: free (vg_replace_malloc.c:530)
==12345==    by 0x400549: main (use_after_free.c:6)
```

---

*[Il file continua con le sezioni 6-12 mantenendo lo stesso livello di dettaglio didattico...]*

## 6. Arduino: Fondamenti e Setup

### 6.1 Cos'è Arduino

**Arduino** è molto più di un semplice microcontrollore: è un ecosistema completo che ha rivoluzionato il modo di fare elettronica.

**Storia rapida:**
- **2005**: Creato in Italia (Ivrea) per studenti design
- **Obiettivo**: Rendere elettronica accessibile a non-ingegneri
- **Rivoluzione**: Da 500€ e settimane di setup → 20€ e 5 minuti!

**Arduino = 3 componenti:**

1. **Hardware** (la scheda fisica)
   - Microcontrollore (cervello)
   - Circuiti supporto (alimentazione, USB, clock)
   - Connettori (pin facilmente accessibili)

2. **Software** (Arduino IDE)
   - Editor codice
   - Compilatore
   - Upload tool

3. **Bootloader** (programma pre-installato nel chip)
   - Permette upload via USB (senza programmatore esterno!)
   - Questo è il "trucco" che rende Arduino facile

**Anatomia scheda Arduino Uno:**

```
Arduino Uno R4
┌─────────────────────────────────────┐
│  ┌───┐                     ┌─────┐  │
│  │USB│                     │POWER│  │
│  └───┘                     └─────┘  │
│  ┌──────────────┐                   │
│  │ ATmega/RA4M1 │ ← Microcontrollore│
│  │   (MCU)      │                   │
│  └──────────────┘                   │
│  ○ ○ ○ ○ ○ ○                        │
│  0 1 2 3 4 5... ← Pin Digitali      │
│                                     │
│  ○  ○  ○  ○  ○  ○                  │
│  A0 A1 A2 A3 A4 A5 ← Pin Analogici  │
│                                     │
│  ┌───┐ ← LED integrato (pin 13)     │
│  │LED│                              │
│  └───┘                              │
└─────────────────────────────────────┘
```

**Modelli Popolari 2025:**

```
┌──────────────────┬────────────────┬──────────────┬─────────────────┐
│ Modello          │ MCU            │ Clock        │ Uso Tipico      │
├──────────────────┼────────────────┼──────────────┼─────────────────┤
│ Uno R4 Minima    │ RA4M1 (ARM)    │ 48 MHz       │ Principianti    │
│                  │                │              │ Progetti base   │
├──────────────────┼────────────────┼──────────────┼─────────────────┤
│ Uno R4 WiFi      │ RA4M1 + ESP32  │ 48 MHz       │ IoT, WiFi       │
│                  │                │              │ Display LED     │
├──────────────────┼────────────────┼──────────────┼─────────────────┤
│ Nano ESP32       │ ESP32-S3       │ 240 MHz      │ Wearable, IoT   │
│                  │ dual-core      │              │ BLE, WiFi       │
├──────────────────┼────────────────┼──────────────┼─────────────────┤
│ Mega 2560        │ ATmega2560     │ 16 MHz       │ Molti pin       │
│                  │                │              │ Robot, CNC      │
├──────────────────┼────────────────┼──────────────┼─────────────────┤
│ ESP32-DevKit     │ ESP32          │ 240 MHz      │ Low-cost IoT    │
│ (compatibile)    │ dual-core      │              │ WiFi+BT (5€)    │
└──────────────────┴────────────────┴──────────────┴─────────────────┘

Memoria:
Uno R4:     256 KB Flash, 32 KB RAM
Nano ESP32: 8 MB Flash, 512 KB RAM
Mega:       256 KB Flash, 8 KB RAM
```

**Quale scegliere per ITS?**
- **Principianti**: Uno R4 Minima (classico, documentazione infinita)
- **IoT/WiFi**: Uno R4 WiFi o Nano ESP32
- **Progetti grandi**: Mega 2560 (54 pin digitali!)
- **Budget**: ESP32-DevKit (~5€, potentissimo)

### 6.2 Arduino vs C Puro

Arduino usa C++, ma semplificato. Vediamo le differenze:

```cpp
// ===== ARDUINO (Wiring Language) =====
// File: Blink.ino

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);  // Configura pin 13 come output
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);  // LED ON
    delay(1000);                      // Aspetta 1 secondo
    digitalWrite(LED_BUILTIN, LOW);   // LED OFF
    delay(1000);
}

// Compila con un click!
// Upload con un click!
// Funziona!

// ===== C PURO AVR (equivalente) =====
// File: blink.c

#include <avr/io.h>
#include <util/delay.h>

int main(void) {
    // Configura pin 13 (PB5 su ATmega328P) come output
    DDRB |= (1 << DDB5);   // Data Direction Register B, bit 5

    while(1) {
        PORTB |= (1 << PORTB5);   // HIGH: setta bit 5
        _delay_ms(1000);
        PORTB &= ~(1 << PORTB5);  // LOW: clear bit 5
        _delay_ms(1000);
    }

    return 0;  // Mai raggiunto
}

// Compila: avr-gcc -mmcu=atmega328p -Os blink.c -o blink.elf
// Converti: avr-objcopy -O ihex blink.elf blink.hex
// Upload: avrdude -p atmega328p -c arduino -P /dev/ttyACM0 -U flash:w:blink.hex
// 😰 Complesso!
```

**Cosa fa Arduino dietro le quinte:**

1. Aggiunge `#include <Arduino.h>` automaticamente
2. Crea funzione `main()` che chiama `setup()` poi `loop()` infinito
3. Configura clock, timer, seriale
4. Compila con `avr-gcc` (o `arm-gcc` per R4)
5. Upload con tool semplificato

**Codice Arduino "vero" dopo preprocessing:**

```cpp
// Quello che Arduino IDE genera internamente
#include <Arduino.h>

void setup();  // Il tuo codice
void loop();   // Il tuo codice

int main(void) {
    init();  // Inizializza hardware (timer, clock, ADC)

    setup();  // Chiama il TUO setup una volta

    for (;;) {  // Loop infinito
        loop();  // Chiama il TUO loop continuamente
    }

    return 0;
}
```

**Vantaggi Arduino:**
- ✅ Nasconde complessità registri hardware
- ✅ Portabile (stesso codice su boards diverse)
- ✅ Librerie pronte per tutto
- ✅ Community enorme

**Quando usare C puro AVR:**
- Serve performance massima
- Controllo fine hardware (interrupt custom, DMA)
- Ottimizzazione estrema (battery-powered, ogni µA conta)

### 6.3 Setup Ambiente 2025

#### Opzione 1: Arduino IDE 2.x (Raccomandato principianti)

```
1. Download da https://www.arduino.cc/en/software
   - Windows: .exe installer
   - Mac: .dmg
   - Linux: AppImage

2. Installa

3. Prima configurazione:
   - File → Preferences
   - Sketchbook location: [scegli cartella progetti]
   - Additional Board Manager URLs: (se usi boards non-ufficiali)
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

4. Installa board:
   - Tools → Board → Boards Manager
   - Cerca "Arduino UNO R4" o "ESP32"
   - Install

5. Seleziona board e porta:
   - Tools → Board → Arduino UNO R4 Minima
   - Tools → Port → COM3 (Windows) o /dev/ttyACM0 (Linux)

6. Test:
   - File → Examples → 01.Basics → Blink
   - Click Upload (→)
   - LED on board dovrebbe lampeggiare!
```

**Features Arduino IDE 2.x (2025):**
- Autocomplete (intelligente!)
- Debug integrato (breakpoint, watch variables)
- Serial Plotter grafico
- Library Manager potenziato
- Multi-board support

#### Opzione 2: PlatformIO (Advanced)

```bash
# PlatformIO = IDE professionale per embedded

# 1. Installa VSCode
https://code.visualstudio.com/

# 2. Installa extension PlatformIO
# In VSCode: Extensions → Cerca "PlatformIO IDE" → Install

# 3. Crea progetto
# PlatformIO Home → New Project
# Name: MyProject
# Board: Arduino Uno
# Framework: Arduino

# 4. Struttura progetto:
# MyProject/
# ├── src/
# │   └── main.cpp  ← Il tuo codice
# ├── lib/  ← Librerie custom
# ├── test/ ← Unit test
# └── platformio.ini  ← Configurazione

# 5. Compila e upload
# Click icona → (Upload) in basso

# 6. Monitor seriale
# Click icona 🔌 (Serial Monitor)
```

**Vantaggi PlatformIO:**
- Multi-board (Arduino, ESP32, STM32, Raspberry Pi Pico...)
- Testing integrato
- Debugging avanzato
- CI/CD ready (GitHub Actions)
- Professionale per team

**Quando usare cosa:**
- **Arduino IDE 2.x**: Principianti, prototipi rapidi, esempi
- **PlatformIO**: Progetti grandi, team, professionale

#### Opzione 3: Arduino CLI (Esperti/Automation)

```bash
# Arduino Command Line Interface

# Installazione
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

# Aggiungi a PATH
export PATH=$PATH:$HOME/bin

# Setup
arduino-cli config init
arduino-cli core update-index

# Installa board
arduino-cli core install arduino:avr       # Uno, Nano classic
arduino-cli core install arduino:renesas_uno  # Uno R4
arduino-cli core install esp32:esp32       # ESP32

# Compila
arduino-cli compile --fqbn arduino:avr:uno MySketch/

# Upload
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno MySketch/

# Monitor seriale
arduino-cli monitor -p /dev/ttyACM0
```

### 6.4 Struttura Sketch Base

Ogni programma Arduino ("sketch") ha questa struttura:

```cpp
// ===== TEMPLATE SKETCH ARDUINO COMPLETO =====

// ───────────────────────────────────────────
// 1. COMMENTO HEADER
// ───────────────────────────────────────────
/*
 * Progetto: Sistema Monitoraggio Temperatura
 * Board: Arduino Uno R4
 * Autore: Studente ITS
 * Data: 2025-01-15
 * Descrizione: Legge temperatura da DHT22, mostra su LCD,
 *              attiva ventola se temp > 30°C
 */

// ───────────────────────────────────────────
// 2. LIBRERIE
// ───────────────────────────────────────────
#include <Wire.h>              // I2C communication
#include <LiquidCrystal_I2C.h> // LCD I2C
#include <DHT.h>               // Sensore temperatura

// ───────────────────────────────────────────
// 3. DEFINIZIONI COSTANTI (#define)
// ───────────────────────────────────────────
#define LED_PIN 13
#define BUTTON_PIN 2
#define FAN_PIN 7
#define DHT_PIN 4

#define TEMP_THRESHOLD 30.0    // °C
#define READ_INTERVAL 2000     // ms

// ───────────────────────────────────────────
// 4. COSTANTI GLOBALI (const)
// ───────────────────────────────────────────
const int SENSOR_PIN = A0;
const long BAUD_RATE = 9600;
const uint8_t LCD_ADDRESS = 0x27;

// ───────────────────────────────────────────
// 5. OGGETTI GLOBALI (librerie)
// ───────────────────────────────────────────
DHT dht(DHT_PIN, DHT22);
LiquidCrystal_I2C lcd(LCD_ADDRESS, 16, 2);

// ───────────────────────────────────────────
// 6. VARIABILI GLOBALI
// ───────────────────────────────────────────
bool fanActive = false;
unsigned long previousMillis = 0;
float currentTemp = 0.0;
int sensorValue = 0;

// ───────────────────────────────────────────
// 7. DICHIARAZIONI FUNZIONI (prototipi)
// ───────────────────────────────────────────
void readTemperature();
void updateDisplay();
void controlFan();

// ═══════════════════════════════════════════
// 8. SETUP - Eseguito UNA VOLTA all'avvio
// ═══════════════════════════════════════════
void setup() {
    // ─── Seriale ───
    Serial.begin(BAUD_RATE);
    Serial.println(F("=== Sistema Avviato ==="));

    // ─── Pin ───
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    pinMode(FAN_PIN, OUTPUT);

    // ─── Librerie ───
    dht.begin();
    lcd.init();
    lcd.backlight();

    // ─── Display iniziale ───
    lcd.setCursor(0, 0);
    lcd.print("Sistema pronto!");
    delay(2000);
    lcd.clear();
}

// ═══════════════════════════════════════════
// 9. LOOP - Eseguito CONTINUAMENTE
// ═══════════════════════════════════════════
void loop() {
    unsigned long currentMillis = millis();

    // ─── Task periodico: lettura sensore ───
    if (currentMillis - previousMillis >= READ_INTERVAL) {
        previousMillis = currentMillis;

        readTemperature();
        updateDisplay();
        controlFan();
    }

    // ─── Task real-time: pulsante ───
    if (digitalRead(BUTTON_PIN) == LOW) {
        // Pulsante premuto
        Serial.println("Button pressed!");
        delay(50);  // Debouncing semplice
    }
}

// ═══════════════════════════════════════════
// 10. IMPLEMENTAZIONI FUNZIONI
// ═══════════════════════════════════════════

void readTemperature() {
    currentTemp = dht.readTemperature();

    if (isnan(currentTemp)) {
        Serial.println(F("Errore lettura DHT!"));
        currentTemp = 0.0;
    } else {
        Serial.print(F("Temperatura: "));
        Serial.print(currentTemp, 1);
        Serial.println(F(" °C"));
    }
}

void updateDisplay() {
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(currentTemp, 1);
    lcd.print(" C  ");

    lcd.setCursor(0, 1);
    lcd.print(fanActive ? "Ventola: ON " : "Ventola: OFF");
}

void controlFan() {
    if (currentTemp > TEMP_THRESHOLD) {
        digitalWrite(FAN_PIN, HIGH);
        fanActive = true;
    } else {
        digitalWrite(FAN_PIN, LOW);
        fanActive = false;
    }
}
```

**Spiegazione sezioni:**

1. **Header**: Chi, cosa, quando, perché
2. **Librerie**: `#include <...>` per funzionalità esterne
3. **#define**: Costanti preprocessore (no memoria RAM)
4. **const**: Costanti vere (tipo-safe)
5. **Oggetti globali**: Istanze librerie (DHT, LCD, etc)
6. **Variabili globali**: Stato programma
7. **Prototipi**: Dichiarazioni funzioni (se usate prima di definirle)
8. **setup()**: Eseguito UNA volta all'accensione
9. **loop()**: Eseguito INFINITAMENTE
10. **Funzioni**: Implementazioni logica

**F() macro - Risparmio RAM:**

```cpp
// ❌ Spreca RAM
Serial.println("Testo lungo che va in RAM");
// Stringa allocata in RAM (limitata!)

// ✅ Risparmia RAM
Serial.println(F("Testo lungo che resta in Flash"));
// F() macro: stringa resta in Flash (memoria programma)
// Su Uno: 32 KB Flash vs 2 KB RAM!
```

---

## 7. Programmazione Arduino con IA

### 7.1 Template Prompt Arduino

Questo template vi permette di generare sketch Arduino professionali con l'IA:

```
# TEMPLATE SKETCH ARDUINO 2025

Crea sketch Arduino per:

## Hardware
Board: [Arduino Uno R4 / Nano ESP32 / Mega / ESP32]
Componenti:
- [es: LED su pin 13]
- [es: Pulsante su pin 2 con pull-up interno]
- [es: Sensore temperatura DHT22 su pin 4]
- [es: Display LCD I2C indirizzo 0x27, 16x2]
- [es: Servo motore su pin 9]

## Funzionalità
[Descrizione dettagliata comportamento del sistema]

Esempio:
"Sistema di monitoraggio temperatura che:
- Legge temperatura ogni 2 secondi
- Mostra valore su LCD
- Attiva LED rosso se temp > 30°C
- Attiva ventola (relay pin 7) se temp > 35°C
- Pulsante reset allarme su pin 2"

## Vincoli Tecnici
- Logica NON-BLOCCANTE (usa millis(), NO delay lunghi)
- Comunicazione seriale debug (baud rate: 9600)
- Commenti esplicativi in italiano
- Gestione errori sensori (controllo isnan, timeout)
- Debouncing pulsanti (software, 50ms)

## Librerie
Specifica librerie necessarie e versioni se rilevante:
- [es: DHT sensor library by Adafruit]
- [es: LiquidCrystal I2C]
- [es: Servo.h (built-in)]

## Gestione Errori
- Cosa fare se sensore non risponde?
- Timeout letture?
- Valori fuori range?
- Indicazione errori (LED, seriale, LCD)?

## Output Richiesto
1. Codice sketch completo commentato
2. Schema collegamenti (pin connections)
3. Lista librerie da installare con versioni
4. Istruzioni test passo-passo
5. Troubleshooting comuni

## [OPZIONALE] Requisiti Speciali
- Consumo basso energia (sleep mode)?
- Salvataggio dati EEPROM?
- Comunicazione WiFi/Bluetooth?
- Logging su SD card?
```

**Perché questo template funziona:**

- **Hardware esplicito** → IA sa esattamente cosa collegare e dove
- **Funzionalità dettagliate** → Comportamento chiaro
- **Vincoli tecnici** → Codice non-bloccante e robusto
- **Gestione errori** → Sistema resiliente
- **Output completo** → Pronti per implementazione fisica

### 7.2 Esempio Pratico: Sistema Allarme Temperatura

**Prompt usando template:**

```
# TEMPLATE SKETCH ARDUINO 2025

Crea sketch Arduino per:

## Hardware
Board: Arduino Uno R4 Minima
Componenti:
- LED rosso su pin 13 (integrato)
- Pulsante su pin 2 (pull-up interno)
- Sensore temperatura analogico TMP36 su pin A0
- Buzzer passivo su pin 8

## Funzionalità
Sistema allarme temperatura che:
1. Legge temperatura da TMP36 ogni 2 secondi
2. LED lampeggia lentamente (1 Hz) se temp normale (< 25°C)
3. LED lampeggia velocemente (5 Hz) se temp alta (25-30°C)
4. LED sempre acceso + buzzer se temp critica (> 30°C)
5. Pulsante silenzia buzzer per 30 secondi
6. Report seriale ogni 5 secondi con timestamp

## Vincoli Tecnici
- Usa millis() (NO delay eccetto debouncing)
- Seriale 9600 baud
- Commenti in italiano
- Gestione errori: se ADC legge 0 o 1023 → sensore scollegato

## Librerie
- Nessuna libreria esterna (solo built-in Arduino)

## Gestione Errori
- Se TMP36 scollegato (lettura ADC fuori range 50-950): LED lampeggia SOS
- Messaggio errore su seriale

## Output Richiesto
1. Sketch completo
2. Schema pin connections
3. Procedura test
4. Calcolo formula TMP36 spiegata
```

**Output IA (Claude 3.5):**

```cpp
/*
 * ════════════════════════════════════════════════════════════
 * SISTEMA ALLARME TEMPERATURA
 * ════════════════════════════════════════════════════════════
 *
 * Hardware:
 * - Arduino Uno R4 Minima
 * - TMP36 su A0 (Vout → A0, Vcc → 5V, GND → GND)
 * - LED integrato pin 13
 * - Pulsante: pin 2 → GND (pull-up interno attivo)
 * - Buzzer passivo: pin 8 (+), GND (-)
 *
 * Funzionalità:
 * - Monitoraggio temperatura continuo
 * - Allarme visivo/sonoro progressivo
 * - Silenziamento temporaneo buzzer
 * - Rilevamento errori sensore
 *
 * Autore: Claude 3.5 + Studente ITS
 * Data: 2025-01-15
 * ════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════
// CONFIGURAZIONE HARDWARE
// ═══════════════════════════════════════════════════════════
const int LED_PIN = 13;
const int BUTTON_PIN = 2;
const int TMP36_PIN = A0;
const int BUZZER_PIN = 8;

// ═══════════════════════════════════════════════════════════
// CONFIGURAZIONE SISTEMA
// ═══════════════════════════════════════════════════════════
const float TEMP_WARNING = 25.0;   // °C - Soglia warning
const float TEMP_CRITICAL = 30.0;  // °C - Soglia critica

const long TEMP_READ_INTERVAL = 2000;    // ms - Lettura sensore
const long SERIAL_REPORT_INTERVAL = 5000; // ms - Report seriale

const long LED_SLOW_BLINK = 500;   // ms - Blink normale (1 Hz)
const long LED_FAST_BLINK = 100;   // ms - Blink warning (5 Hz)

const long BUZZER_MUTE_DURATION = 30000;  // ms - Silenzia 30 sec
const int DEBOUNCE_DELAY = 50;     // ms - Debouncing pulsante

// ═══════════════════════════════════════════════════════════
// STATI SISTEMA
// ═══════════════════════════════════════════════════════════
enum SystemState {
    STATE_NORMAL,      // Temperatura normale
    STATE_WARNING,     // Temperatura alta
    STATE_CRITICAL,    // Temperatura critica
    STATE_ERROR        // Errore sensore
};

SystemState currentState = STATE_NORMAL;

// ═══════════════════════════════════════════════════════════
// VARIABILI GLOBALI
// ═══════════════════════════════════════════════════════════
float currentTemp = 0.0;
bool ledState = false;
bool buzzerMuted = false;

unsigned long tempReadPrevMillis = 0;
unsigned long serialReportPrevMillis = 0;
unsigned long ledPrevMillis = 0;
unsigned long buzzerMuteStartTime = 0;

int lastButtonState = HIGH;
int buttonState = HIGH;
unsigned long lastDebounceTime = 0;

unsigned long systemStartTime = 0;

// ═══════════════════════════════════════════════════════════
// SETUP - INIZIALIZZAZIONE
// ═══════════════════════════════════════════════════════════
void setup() {
    // ─── Seriale ───
    Serial.begin(9600);
    Serial.println(F(""));
    Serial.println(F("════════════════════════════════════"));
    Serial.println(F("  SISTEMA ALLARME TEMPERATURA v1.0  "));
    Serial.println(F("════════════════════════════════════"));
    Serial.println(F(""));

    // ─── Pin ───
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);
    pinMode(BUZZER_PIN, OUTPUT);

    // ─── LED test iniziale ───
    digitalWrite(LED_PIN, HIGH);
    tone(BUZZER_PIN, 1000, 100);  // Beep breve startup
    delay(500);
    digitalWrite(LED_PIN, LOW);

    // ─── Timestamp sistema ───
    systemStartTime = millis();

    Serial.println(F("Sistema pronto!"));
    Serial.println(F("Soglie: Warning=25°C, Critical=30°C"));
    Serial.println(F(""));
}

// ═══════════════════════════════════════════════════════════
// LOOP PRINCIPALE
// ═══════════════════════════════════════════════════════════
void loop() {
    unsigned long currentMillis = millis();

    // ─── TASK 1: Lettura Temperatura ───
    if (currentMillis - tempReadPrevMillis >= TEMP_READ_INTERVAL) {
        tempReadPrevMillis = currentMillis;
        readTemperature();
        updateSystemState();
    }

    // ─── TASK 2: Gestione LED ───
    updateLED(currentMillis);

    // ─── TASK 3: Gestione Buzzer ───
    updateBuzzer(currentMillis);

    // ─── TASK 4: Gestione Pulsante ───
    handleButton(currentMillis);

    // ─── TASK 5: Report Seriale ───
    if (currentMillis - serialReportPrevMillis >= SERIAL_REPORT_INTERVAL) {
        serialReportPrevMillis = currentMillis;
        printSerialReport(currentMillis);
    }
}

// ═══════════════════════════════════════════════════════════
// LETTURA TEMPERATURA TMP36
// ═══════════════════════════════════════════════════════════
void readTemperature() {
    // Lettura ADC
    int adcValue = analogRead(TMP36_PIN);

    // ─── CONTROLLO ERRORE: Sensore scollegato ───
    if (adcValue < 50 || adcValue > 950) {
        currentState = STATE_ERROR;
        Serial.println(F("⚠️  ERRORE: Sensore TMP36 scollegato!"));
        return;
    }

    // ─── CONVERSIONE ADC → TEMPERATURA ───
    // Formula TMP36:
    // Vout = (Temp °C + 50) / 100
    //
    // Step 1: ADC (0-1023) → Volt (0-5V)
    float voltage = adcValue * (5.0 / 1023.0);

    // Step 2: Volt → °C
    // TMP36: 10 mV/°C, 500mV offset (0°C = 500mV)
    currentTemp = (voltage - 0.5) * 100.0;

    // Debug
    Serial.print(F("ADC: "));
    Serial.print(adcValue);
    Serial.print(F(" | Volt: "));
    Serial.print(voltage, 3);
    Serial.print(F("V | Temp: "));
    Serial.print(currentTemp, 1);
    Serial.println(F("°C"));
}

// ═══════════════════════════════════════════════════════════
// AGGIORNA STATO SISTEMA
// ═══════════════════════════════════════════════════════════
void updateSystemState() {
    SystemState oldState = currentState;

    if (currentState == STATE_ERROR) {
        return;  // Rimane in errore finché sensore non torna OK
    }

    // Determina nuovo stato
    if (currentTemp >= TEMP_CRITICAL) {
        currentState = STATE_CRITICAL;
    } else if (currentTemp >= TEMP_WARNING) {
        currentState = STATE_WARNING;
    } else {
        currentState = STATE_NORMAL;
    }

    // Log cambio stato
    if (currentState != oldState) {
        Serial.println(F(""));
        Serial.print(F(">>> CAMBIO STATO: "));
        printStateName(oldState);
        Serial.print(F(" → "));
        printStateName(currentState);
        Serial.println(F(" <<<"));
        Serial.println(F(""));
    }
}

// ═══════════════════════════════════════════════════════════
// GESTIONE LED (NON-BLOCCANTE)
// ═══════════════════════════════════════════════════════════
void updateLED(unsigned long currentMillis) {
    long blinkInterval;

    switch (currentState) {
        case STATE_NORMAL:
            blinkInterval = LED_SLOW_BLINK;  // 1 Hz
            break;

        case STATE_WARNING:
            blinkInterval = LED_FAST_BLINK;  // 5 Hz
            break;

        case STATE_CRITICAL:
            // LED sempre acceso
            digitalWrite(LED_PIN, HIGH);
            return;

        case STATE_ERROR:
            // Pattern SOS: · · · — — — · · ·
            blinkSOSPattern(currentMillis);
            return;
    }

    // Blink normale
    if (currentMillis - ledPrevMillis >= blinkInterval) {
        ledPrevMillis = currentMillis;
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }
}

// ═══════════════════════════════════════════════════════════
// PATTERN LED SOS (ERRORE)
// ═══════════════════════════════════════════════════════════
void blinkSOSPattern(unsigned long currentMillis) {
    // Pattern semplificato: blink molto veloce
    if (currentMillis - ledPrevMillis >= 100) {
        ledPrevMillis = currentMillis;
        ledState = !ledState;
        digitalWrite(LED_PIN, ledState);
    }
}

// ═══════════════════════════════════════════════════════════
// GESTIONE BUZZER
// ═══════════════════════════════════════════════════════════
void updateBuzzer(unsigned long currentMillis) {
    // ─── Controlla se mute scaduto ───
    if (buzzerMuted) {
        if (currentMillis - buzzerMuteStartTime >= BUZZER_MUTE_DURATION) {
            buzzerMuted = false;
            Serial.println(F("🔊 Buzzer riattivato"));
        }
    }

    // ─── Attiva buzzer se temperatura critica ───
    if (currentState == STATE_CRITICAL && !buzzerMuted) {
        // Beep intermittente 1 Hz
        if ((currentMillis / 500) % 2 == 0) {
            tone(BUZZER_PIN, 2000);  // 2 kHz
        } else {
            noTone(BUZZER_PIN);
        }
    } else {
        noTone(BUZZER_PIN);
    }
}

// ═══════════════════════════════════════════════════════════
// GESTIONE PULSANTE (CON DEBOUNCING)
// ═══════════════════════════════════════════════════════════
void handleButton(unsigned long currentMillis) {
    int reading = digitalRead(BUTTON_PIN);

    // ─── Debouncing ───
    if (reading != lastButtonState) {
        lastDebounceTime = currentMillis;
    }

    if ((currentMillis - lastDebounceTime) > DEBOUNCE_DELAY) {
        if (reading != buttonState) {
            buttonState = reading;

            // ─── Rileva pressione (falling edge) ───
            if (buttonState == LOW) {
                onButtonPressed();
            }
        }
    }

    lastButtonState = reading;
}

// ═══════════════════════════════════════════════════════════
// AZIONE PRESSIONE PULSANTE
// ═══════════════════════════════════════════════════════════
void onButtonPressed() {
    Serial.println(F(""));
    Serial.println(F("🔘 PULSANTE PREMUTO"));

    if (currentState == STATE_CRITICAL) {
        buzzerMuted = true;
        buzzerMuteStartTime = millis();
        noTone(BUZZER_PIN);

        Serial.println(F("🔇 Buzzer silenziato per 30 secondi"));
    } else {
        Serial.println(F("ℹ️  Pulsante attivo solo in stato CRITICAL"));
    }

    Serial.println(F(""));
}

// ═══════════════════════════════════════════════════════════
// REPORT SERIALE PERIODICO
// ═══════════════════════════════════════════════════════════
void printSerialReport(unsigned long currentMillis) {
    // ─── Calcola timestamp ───
    unsigned long seconds = (currentMillis - systemStartTime) / 1000;
    unsigned long minutes = seconds / 60;
    seconds = seconds % 60;

    Serial.println(F(""));
    Serial.println(F("─────────────────────────────────"));
    Serial.print(F("⏱  UPTIME: "));
    Serial.print(minutes);
    Serial.print(F(" min "));
    Serial.print(seconds);
    Serial.println(F(" sec"));

    Serial.print(F("🌡  TEMPERATURA: "));
    Serial.print(currentTemp, 1);
    Serial.println(F(" °C"));

    Serial.print(F("📊 STATO: "));
    printStateName(currentState);
    Serial.println();

    if (buzzerMuted) {
        unsigned long remaining = BUZZER_MUTE_DURATION -
                                  (currentMillis - buzzerMuteStartTime);
        Serial.print(F("🔇 Buzzer muto per altri "));
        Serial.print(remaining / 1000);
        Serial.println(F(" sec"));
    }

    Serial.println(F("─────────────────────────────────"));
    Serial.println(F(""));
}

// ═══════════════════════════════════════════════════════════
// UTILITY: STAMPA NOME STATO
// ═══════════════════════════════════════════════════════════
void printStateName(SystemState state) {
    switch (state) {
        case STATE_NORMAL:
            Serial.print(F("NORMALE ✅"));
            break;
        case STATE_WARNING:
            Serial.print(F("WARNING ⚠️"));
            break;
        case STATE_CRITICAL:
            Serial.print(F("CRITICAL 🚨"));
            break;
        case STATE_ERROR:
            Serial.print(F("ERRORE ❌"));
            break;
    }
}
```

**Schema Collegamenti:**

```
┌─────────────────────────────────────┐
│        Arduino Uno R4 Minima        │
│                                     │
│  Digital Pin 13 → LED_BUILTIN       │
│  Digital Pin 2  → Pulsante → GND    │
│  Digital Pin 8  → Buzzer (+)        │
│  Analog Pin A0  → TMP36 Vout        │
│  5V             → TMP36 Vcc         │
│  GND            → TMP36 GND         │
│  GND            → Buzzer (-)        │
└─────────────────────────────────────┘

TMP36 Pinout (vista frontale, piatto):
   ┌─────────┐
   │  TMP36  │
   │ ┌─────┐ │
   │ │     │ │
   └─┴─────┴─┘
     │  │  │
    Vcc│ GND
     │  Vout
     │   │
    5V  A0
```

**Procedura Test:**

```
1. SETUP HARDWARE
   ✓ Collega TMP36 come da schema
   ✓ Collega buzzer passivo
   ✓ Pulsante con pull-up (pin 2 → GND)

2. UPLOAD CODICE
   ✓ Seleziona board: Arduino Uno R4 Minima
   ✓ Seleziona porta COM corretta
   ✓ Upload sketch

3. TEST SERIALE
   ✓ Apri Serial Monitor (9600 baud)
   ✓ Verifica messaggio startup
   ✓ Controlla letture temperatura ogni 2 sec

4. TEST TEMPERATURA NORMALE (< 25°C)
   ✓ LED lampeggia lento (1 Hz)
   ✓ No buzzer
   ✓ Stato: NORMALE

5. TEST WARNING (25-30°C)
   ✓ Scalda TMP36 con dita
   ✓ LED lampeggia veloce (5 Hz)
   ✓ No buzzer ancora
   ✓ Stato: WARNING

6. TEST CRITICAL (> 30°C)
   ✓ Scalda ulteriormente
   ✓ LED fisso acceso
   ✓ Buzzer suona intermittente
   ✓ Stato: CRITICAL

7. TEST PULSANTE MUTE
   ✓ Premi pulsante in stato CRITICAL
   ✓ Buzzer si silenzia
   ✓ Messaggio "silenziato 30 sec"
   ✓ Dopo 30 sec buzzer riattivato

8. TEST ERRORE SENSORE
   ✓ Scollega TMP36
   ✓ LED lampeggia SOS veloce
   ✓ Messaggio errore su seriale
   ✓ Ricollega → torna normale
```

**Formula TMP36 Spiegata:**

```
Il TMP36 è un sensore temperatura analogico:

OUTPUT: 10 mV per ogni °C
OFFSET: 500 mV a 0°C

Formula:
Vout (mV) = (Temperatura °C + 50) × 10

Esempio:
- 0°C  → 500 mV → ADC = 102
- 25°C → 750 mV → ADC = 153
- 50°C → 1000 mV → ADC = 204

Conversione inversa (nel codice):
1. ADC → Volt: voltage = adcValue × (5.0 / 1023.0)
2. Volt → °C:  tempC = (voltage - 0.5) × 100.0

Perché -0.5?
500 mV = 0.5V è l'offset per 0°C
```

### 7.3 Template Debugging Arduino

Quando lo sketch non funziona:

```
# DEBUGGING SKETCH ARDUINO CON IA

Ho questo sketch Arduino che non funziona:

```cpp
[INCOLLA SKETCH COMPLETO]
```

## Problema
Descrizione dettagliata:
- Cosa dovrebbe fare: [comportamento atteso]
- Cosa fa invece: [comportamento effettivo]
- Quando succede: [sempre / random / dopo X secondi]

## Errori Compilazione (se presenti)
```
[INCOLLA MESSAGGI ERRORE COMPLETI]
```

## Hardware
Board: [Arduino Uno / ESP32 / ...]
Componenti collegati:
- [Lista con pin specifici]

## Serial Monitor Output
```
[INCOLLA OUTPUT SERIALE se disponibile]
```

## Test Fatti
- [x] Controllato collegamenti hardware
- [ ] Testato con sketch esempio (Blink) → funziona
- [ ] LED power on acceso
- [ ] Porta COM corretta selezionata

## Richiesta
1. Identifica problema (hardware/software/logica)
2. Spiega causa root
3. Fornisci fix con codice corretto
4. Suggerisci debug aggiuntivo se necessario
```

---

## 8. Pattern Embedded Non-Bloccanti

### 8.1 Il Problema di delay() - ANTIPATTERN

**Analogia:** Immaginate di cucinare pasta. Mettete l'acqua a bollire e poi rimanete immobili a fissare la pentola per 10 minuti. Non potete:
- Rispondere al campanello
- Tagliare verdure
- Apparecchiare tavola
- Controllare il sugo

Questo è esattamente cosa fa `delay()` in Arduino!

```cpp
// ❌ CODICE BLOCCANTE - NON FARE MAI!
void loop() {
    // Task 1: Blink LED
    digitalWrite(LED1, HIGH);
    delay(1000);  // ❌ Sistema CONGELATO per 1 secondo intero!
    digitalWrite(LED1, LOW);
    delay(1000);  // ❌ Ancora congelato!

    // ❌ Durante i delay() NON può:
    // - Rispondere a pulsanti (l'utente preme, Arduino ignora)
    // - Leggere sensori (dati persi)
    // - Ricevere dati seriali (buffer overflow)
    // - Gestire interrupt (mascherati da delay)
    // - Fare QUALSIASI altra cosa
}
```

**Problemi delay():**

| Problema | Impatto | Esempio |
|----------|---------|---------|
| **Blocca esecuzione** | Sistema "morto" durante delay | Premi pulsante → ignora per 1 secondo |
| **Non può multi-task** | Un solo task alla volta | LED blink = NON può leggere sensore |
| **Non reattivo** | Latenza alta | Allarme incendio ritardato! |
| **Inefficiente energia** | CPU attiva ma inutile | Batteria consumata senza fare nulla |
| **Impossibile sincronizzare** | Task diversi frequenze | LED 1 Hz, sensore 2 Hz = impossibile |

**Esempio concreto del disastro:**

```cpp
// ❌ SISTEMA ALLARME ROTTO CON delay()
void loop() {
    // Blink LED status
    digitalWrite(LED_STATUS, HIGH);
    delay(500);
    digitalWrite(LED_STATUS, LOW);
    delay(500);
    // ↑ 1 secondo bloccato qui!

    // Leggi sensore fumo
    int smoke = analogRead(SMOKE_SENSOR);
    if (smoke > THRESHOLD) {
        alarm();  // Troppo tardi! Incendio già diffuso
    }
}

// Scenario:
// T=0.0s: Inizio loop, LED on
// T=0.5s: LED off (era già troppo fumo ma delay bloccava!)
// T=1.0s: Finalmente legge sensore, INCENDIO!
// ⚠️ Ritardo 1 secondo può essere FATALE
```

### 8.2 La Soluzione: millis() - Pattern Professionale

**Analogia:** Invece di fissare la pentola, usate un timer da cucina. Impostate 10 minuti e continuate a fare altro. Ogni tanto controllate "sono passati 10 minuti?" Se sì, agite.

```cpp
// ✅ CODICE NON-BLOCCANTE con millis()
unsigned long previousMillis = 0;  // Ultimo "check"
const long interval = 1000;        // Intervallo desiderato (1 sec)
bool ledState = false;

void loop() {
    unsigned long currentMillis = millis();  // "Che ora è?"

    // "Sono passati 1000ms dall'ultimo check?"
    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;  // Aggiorna timestamp

        // Azione periodica
        ledState = !ledState;
        digitalWrite(LED1, ledState);
    }

    // ✅ Sistema SEMPRE reattivo!
    // Mentre "aspetta" può fare altre cose:
    checkButtons();      // Risponde subito a pulsanti
    readSensors();       // Legge sensori costantemente
    handleSerial();      // Processa comandi seriali
    checkAlarms();       // Controlla allarmi real-time
}
```

**Come funziona millis():**

```cpp
// millis() ritorna millisecondi da avvio Arduino
// Tipo: unsigned long (0 a 4,294,967,295)
// Overflow dopo: 49.7 giorni

unsigned long now = millis();
// now = 5234  (5.234 secondi da avvio)

// PATTERN UNIVERSALE:
// if (adesso - ultimaVolta >= intervallo) {
//     fai_azione();
//     ultimaVolta = adesso;
// }
```

**Visualizzazione timeline:**

```
Tempo (ms):  0    500   1000  1500  2000  2500  3000
             |     |     |     |     |     |     |
Loop #1:     ✓ Check: 0-0 >= 1000? NO → continua
Loop #2:           ✓ Check: 500-0 >= 1000? NO → continua
Loop #3:                 ✓ Check: 1000-0 >= 1000? SI! → AZIONE + aggiorna
Loop #4:                       ✓ Check: 1500-1000 >= 1000? NO
...
Loop #N:                             ✓ Check: 2000-1000 >= 1000? SI! → AZIONE

Ogni loop dura ~microseconds
Arduino Uno: ~10000 loop al secondo!
```

**Vantaggi millis():**

✅ **Non-bloccante** - Sistema sempre reattivo
✅ **Multi-task simultanei** - LED + sensori + pulsanti + seriale
✅ **Timing preciso** - Intervalli esatti
✅ **Scalabile** - Decine di task diversi
✅ **Professionale** - Usato in produzione industriale

### 8.3 Multi-Task con millis() - Pattern Completo

Ecco come gestire task multipli simultanei:

```cpp
// ═══════════════════════════════════════════════════════════
// MULTI-TASK EMBEDDED PROFESSIONALE
// ═══════════════════════════════════════════════════════════

// ─── Timestamp ogni task ───
unsigned long led1PrevMillis = 0;
unsigned long led2PrevMillis = 0;
unsigned long sensorPrevMillis = 0;
unsigned long serialPrevMillis = 0;
unsigned long displayPrevMillis = 0;

// ─── Intervalli ogni task ───
const long LED1_INTERVAL = 500;      // 500ms → 2 Hz
const long LED2_INTERVAL = 1500;     // 1.5s  → 0.67 Hz
const long SENSOR_INTERVAL = 2000;   // 2s
const long SERIAL_INTERVAL = 5000;   // 5s
const long DISPLAY_INTERVAL = 1000;  // 1s

// ─── Stato task ───
bool led1State = false;
bool led2State = false;
float temperature = 0.0;

void loop() {
    unsigned long currentMillis = millis();

    // ═══ TASK 1: Blink LED1 ogni 500ms ═══
    if (currentMillis - led1PrevMillis >= LED1_INTERVAL) {
        led1PrevMillis = currentMillis;

        led1State = !led1State;
        digitalWrite(LED1_PIN, led1State);
    }

    // ═══ TASK 2: Blink LED2 ogni 1.5s ═══
    if (currentMillis - led2PrevMillis >= LED2_INTERVAL) {
        led2PrevMillis = currentMillis;

        led2State = !led2State;
        digitalWrite(LED2_PIN, led2State);
    }

    // ═══ TASK 3: Leggi sensore ogni 2s ═══
    if (currentMillis - sensorPrevMillis >= SENSOR_INTERVAL) {
        sensorPrevMillis = currentMillis;

        int raw = analogRead(TEMP_SENSOR_PIN);
        temperature = raw * (5.0 / 1023.0) * 100.0;  // Conversione

        // Logica allarme
        if (temperature > 30.0) {
            activateAlarm();
        }
    }

    // ═══ TASK 4: Report seriale ogni 5s ═══
    if (currentMillis - serialPrevMillis >= SERIAL_INTERVAL) {
        serialPrevMillis = currentMillis;

        Serial.print("Temp: ");
        Serial.print(temperature, 1);
        Serial.print(" °C | LED1: ");
        Serial.print(led1State ? "ON" : "OFF");
        Serial.print(" | LED2: ");
        Serial.println(led2State ? "ON" : "OFF");
    }

    // ═══ TASK 5: Aggiorna display ogni 1s ═══
    if (currentMillis - displayPrevMillis >= DISPLAY_INTERVAL) {
        displayPrevMillis = currentMillis;

        lcd.setCursor(0, 0);
        lcd.print("Temp: ");
        lcd.print(temperature, 1);
        lcd.print("C  ");
    }

    // ═══ TASK 6: Controli real-time (SEMPRE) ═══
    // Questi vengono eseguiti ogni loop (migliaia di volte al secondo)
    checkButtons();        // Pulsanti ultra-reattivi
    handleSerialCommands(); // Comandi seriali immediati
    checkEmergencyStop();  // Safety critical
}

// ───────────────────────────────────────────────────────────
// Funzioni supporto
// ───────────────────────────────────────────────────────────
void checkButtons() {
    if (digitalRead(BUTTON_PIN) == LOW) {
        // Azione immediata (latenza < 1ms)
        Serial.println("Button pressed!");
    }
}

void activateAlarm() {
    digitalWrite(ALARM_LED, HIGH);
    tone(BUZZER_PIN, 1000);  // 1 kHz
}
```

**Timeline multi-task visualizzata:**

```
Tempo:    0ms   500ms  1000ms 1500ms 2000ms 2500ms 3000ms 3500ms 4000ms 5000ms
          |      |      |      |      |      |      |      |      |      |
LED1:     ON     OFF    ON     OFF    ON     OFF    ON     OFF    ON     OFF
LED2:     ON            OFF           ON            OFF           ON
Sensor:                        READ                        READ
Display:         UPD           UPD           UPD           UPD           UPD
Serial:                                                             REPORT
Buttons:  CHECK  CHECK  CHECK  CHECK  CHECK  CHECK  ...→ SEMPRE ATTIVO
```

Notate come ogni task ha il suo "orologio" indipendente!

### 8.4 State Machine Pattern - Logica Complessa

Per sistemi complessi, usate **State Machine** (macchina a stati):

```cpp
// ═══════════════════════════════════════════════════════════
// STATE MACHINE PATTERN
// ═══════════════════════════════════════════════════════════

// ─── Definizione Stati ───
enum SystemState {
    STATE_IDLE,           // Sistema in attesa
    STATE_READING,        // Lettura sensore in corso
    STATE_PROCESSING,     // Elaborazione dati
    STATE_ALERT,          // Allarme attivo
    STATE_COOLDOWN,       // Periodo attesa dopo allarme
    STATE_ERROR           // Errore sistema
};

SystemState currentState = STATE_IDLE;
unsigned long stateEntryTime = 0;  // Quando entrato in stato corrente

// ─── Timeout stati ───
const long READING_TIMEOUT = 100;     // ms
const long PROCESSING_TIMEOUT = 200;  // ms
const long COOLDOWN_DURATION = 5000;  // 5 sec

void loop() {
    unsigned long now = millis();
    unsigned long stateElapsed = now - stateEntryTime;

    // ═══ STATE MACHINE ═══
    switch (currentState) {

        // ─────────────────────────────────────────
        case STATE_IDLE:
        // ─────────────────────────────────────────
            // LED status blink lento
            blinkLED(1000);

            // Attesa input utente
            if (buttonPressed()) {
                changeState(STATE_READING);
                Serial.println("→ Avvio lettura sensore");
            }
            break;

        // ─────────────────────────────────────────
        case STATE_READING:
        // ─────────────────────────────────────────
            // LED status blink veloce
            blinkLED(200);

            // Timeout sicurezza
            if (stateElapsed >= READING_TIMEOUT) {
                float value = readSensor();

                if (!isnan(value)) {
                    sensorData = value;
                    changeState(STATE_PROCESSING);
                } else {
                    changeState(STATE_ERROR);
                    Serial.println("⚠️ Errore lettura sensore");
                }
            }
            break;

        // ─────────────────────────────────────────
        case STATE_PROCESSING:
        // ─────────────────────────────────────────
            // LED fisso
            digitalWrite(LED_PIN, HIGH);

            if (stateElapsed >= PROCESSING_TIMEOUT) {
                // Analizza dati
                if (sensorData > THRESHOLD) {
                    changeState(STATE_ALERT);
                    Serial.println("🚨 ALLARME!");
                } else {
                    changeState(STATE_IDLE);
                    Serial.println("✓ Valori normali");
                }
            }
            break;

        // ─────────────────────────────────────────
        case STATE_ALERT:
        // ─────────────────────────────────────────
            // LED + buzzer
            blinkLED(100);
            tone(BUZZER_PIN, 2000);

            // Utente può silenziare
            if (buttonPressed()) {
                noTone(BUZZER_PIN);
                changeState(STATE_COOLDOWN);
                Serial.println("→ Allarme silenziato");
            }
            break;

        // ─────────────────────────────────────────
        case STATE_COOLDOWN:
        // ─────────────────────────────────────────
            // LED blink medio
            blinkLED(500);
            noTone(BUZZER_PIN);

            // Attesa 5 secondi
            if (stateElapsed >= COOLDOWN_DURATION) {
                changeState(STATE_IDLE);
                Serial.println("→ Sistema pronto");
            }
            break;

        // ─────────────────────────────────────────
        case STATE_ERROR:
        // ─────────────────────────────────────────
            // Pattern SOS
            blinkSOSPattern();

            Serial.println("❌ ERRORE SISTEMA!");

            // Attesa 2 secondi poi retry
            if (stateElapsed >= 2000) {
                changeState(STATE_IDLE);
            }
            break;
    }
}

// ───────────────────────────────────────────────────────────
// Cambio stato (con logging)
// ───────────────────────────────────────────────────────────
void changeState(SystemState newState) {
    Serial.print("STATE: ");
    printStateName(currentState);
    Serial.print(" → ");
    printStateName(newState);
    Serial.println();

    currentState = newState;
    stateEntryTime = millis();  // Reset timer stato
}

void printStateName(SystemState state) {
    switch (state) {
        case STATE_IDLE:       Serial.print("IDLE"); break;
        case STATE_READING:    Serial.print("READING"); break;
        case STATE_PROCESSING: Serial.print("PROCESSING"); break;
        case STATE_ALERT:      Serial.print("ALERT"); break;
        case STATE_COOLDOWN:   Serial.print("COOLDOWN"); break;
        case STATE_ERROR:      Serial.print("ERROR"); break;
    }
}
```

**Diagramma Stati:**

```
       ┌──────────┐
       │  IDLE    │ ← Stato iniziale
       └────┬─────┘
            │ Button press
            ↓
       ┌──────────┐
       │ READING  │
       └────┬─────┘
            │ Timeout 100ms
            ├─────────────┐
            ↓             ↓
     ┌────────────┐  ┌─────────┐
     │ PROCESSING │  │  ERROR  │
     └─────┬──────┘  └────┬────┘
           │              │ 2sec
      ┌────┴────┐         │
      ↓         ↓         ↓
  ┌──────┐  ┌───────┐  ┌──────┐
  │ IDLE │  │ ALERT │→ │ IDLE │
  └──────┘  └───┬───┘  └──────┘
                │ Button
                ↓
            ┌──────────┐
            │ COOLDOWN │
            └────┬─────┘
                 │ 5sec
                 ↓
            ┌──────────┐
            │  IDLE    │
            └──────────┘
```

**Vantaggi State Machine:**

✅ **Logica chiara** - Ogni stato sa cosa fare
✅ **Manutenibile** - Facile aggiungere stati
✅ **Debuggabile** - Log transizioni
✅ **Sicuro** - Timeout prevengono blocchi
✅ **Scalabile** - Sistemi complessi gestibili

---

## 9. Sensori, Attuatori e Progetti IoT

### 9.1 Input/Output Digitale

```cpp
// ═══════════════════════════════════════════════════════════
// GPIO DIGITALE - FONDAMENTI
// ═══════════════════════════════════════════════════════════

// ─── OUTPUT DIGITALE ───
// Imposta pin come uscita (OUTPUT)
pinMode(13, OUTPUT);

// Scrivi valore digitale
digitalWrite(13, HIGH);  // 5V (o 3.3V su boards 3.3V)
digitalWrite(13, LOW);   // 0V (GND)

// ─── INPUT DIGITALE ───
// Leggi stato pulsante/sensore digitale
pinMode(2, INPUT);
int buttonState = digitalRead(2);  // HIGH (1) o LOW (0)

// Se pulsante non premuto: HIGH (floating, rumore!)
// Se pulsante premuto: LOW (collegato a GND)

// ─── INPUT_PULLUP (RACCOMANDATO) ───
pinMode(2, INPUT_PULLUP);
// Attiva resistenza pull-up interna (~20-50kΩ)
// Pin → +5V tramite resistenza
// Pulsante tra pin e GND (NO resistenza esterna!)

// Logica invertita:
// Pulsante NON premuto: HIGH (pull-up a 5V)
// Pulsante PREMUTO:     LOW  (collegato a GND)

int state = digitalRead(2);
if (state == LOW) {
    Serial.println("Pulsante PREMUTO");
}
```

**Circuito INPUT_PULLUP:**

```
        Arduino
          5V
           |
          [R]  ← Resistenza pull-up interna (~20kΩ)
           |
    Pin 2 ●─────┬─── Pulsante ─── GND
                │
               ╱
```

**Quando usare INPUT vs INPUT_PULLUP:**

| Modo | Quando Usare | Circuito Esterno |
|------|--------------|------------------|
| `INPUT` | Sensori digitali con output attivo | Può servire pull-up/down esterno |
| `INPUT_PULLUP` | Pulsanti, switch | Solo pulsante a GND, NO resistenze |

### 9.2 Input Analogico (ADC)

Arduino Uno ha **ADC 10-bit**: converte 0-5V → 0-1023

```cpp
// ═══════════════════════════════════════════════════════════
// ADC - ANALOG TO DIGITAL CONVERTER
// ═══════════════════════════════════════════════════════════

// ─── Lettura analogica ───
int rawValue = analogRead(A0);  // 0-1023

// ─── Conversione a volt ───
float voltage = rawValue * (5.0 / 1023.0);

// Esempi:
// rawValue = 0    → voltage = 0.0 V
// rawValue = 512  → voltage = 2.5 V
// rawValue = 1023 → voltage = 5.0 V

// ═══ SENSORI ANALOGICI COMUNI ═══

// ─── 1. POTENZIOMETRO (resistenza variabile) ───
int potValue = analogRead(A0);  // 0-1023

// Mappa a range diverso (es: 0-255 per PWM)
int brightness = map(potValue, 0, 1023, 0, 255);
analogWrite(LED_PWM_PIN, brightness);

// map() equivale a:
// brightness = (potValue - 0) * (255 - 0) / (1023 - 0) + 0;

// ─── 2. FOTORESISTENZA (LDR) ───
// Voltage divider: 5V → LDR → A0 → R_fixed → GND
int lightLevel = analogRead(A1);

// Luce alta  → LDR resistenza bassa  → tensione bassa  → valore basso
// Buio       → LDR resistenza alta   → tensione alta   → valore alto

if (lightLevel < 300) {  // Buio
    digitalWrite(LED, HIGH);  // Accendi LED
} else {
    digitalWrite(LED, LOW);
}

// ─── 3. TMP36 - Sensore Temperatura ───
int reading = analogRead(A0);
float voltage = reading * (5.0 / 1023.0);

// Formula TMP36: Vout = (Temp°C + 50) / 100
// Inversamente: Temp°C = (Vout * 100) - 50
float tempC = (voltage - 0.5) * 100.0;

Serial.print("Temperatura: ");
Serial.print(tempC, 1);
Serial.println(" °C");

// ─── 4. SENSORE UMIDITÀ SUOLO ───
int soilMoisture = analogRead(A2);

// Asciutto: ~800-1023 (alta resistenza)
// Umido:    ~400-600
// Bagnato:  ~200-400

if (soilMoisture > 700) {
    Serial.println("Suolo ASCIUTTO - Attiva irrigazione");
    digitalWrite(PUMP_PIN, HIGH);
} else {
    digitalWrite(PUMP_PIN, LOW);
}
```

**Risoluzione ADC:**

```
10-bit ADC:
- Range: 0-1023 (2^10 = 1024 livelli)
- Risoluzione: 5V / 1024 = 4.88 mV per step
- Precision: ±1 LSB (±4.88 mV)

12-bit ADC (ESP32, Arduino Due):
- Range: 0-4095 (2^12 = 4096 livelli)
- Risoluzione: 3.3V / 4096 = 0.8 mV per step
- 16x più preciso del 10-bit!
```

### 9.3 Output PWM (Pulse Width Modulation)

PWM simula tensione variabile alternando velocemente HIGH/LOW.

```cpp
// ═══════════════════════════════════════════════════════════
// PWM - MODULAZIONE LARGHEZZA IMPULSO
// ═══════════════════════════════════════════════════════════

// ─── Pin PWM Arduino Uno ───
// Solo pin specifici: 3, 5, 6, 9, 10, 11
// Frequenza: ~490 Hz (pin 3,9,10,11) o ~980 Hz (pin 5,6)

// ─── Controllo LED dimming ───
analogWrite(9, 0);     // 0% duty → LED spento
analogWrite(9, 64);    // 25% duty → LED 25% luminosità
analogWrite(9, 128);   // 50% duty → LED 50%
analogWrite(9, 192);   // 75% duty → LED 75%
analogWrite(9, 255);   // 100% duty → LED pieno

// ═══ EFFETTO FADE ═══
void fadeIn() {
    for (int brightness = 0; brightness <= 255; brightness++) {
        analogWrite(LED_PWM_PIN, brightness);
        delay(10);  // 10ms * 256 = 2.56 secondi totali
    }
}

void fadeOut() {
    for (int brightness = 255; brightness >= 0; brightness--) {
        analogWrite(LED_PWM_PIN, brightness);
        delay(10);
    }
}

// ═══ CONTROLLO MOTORE DC ═══
const int MOTOR_PWM = 9;   // Velocità
const int MOTOR_DIR1 = 7;  // Direzione A
const int MOTOR_DIR2 = 8;  // Direzione B

void setMotorSpeed(int speed) {  // -255 a +255
    if (speed > 0) {
        // Avanti
        digitalWrite(MOTOR_DIR1, HIGH);
        digitalWrite(MOTOR_DIR2, LOW);
        analogWrite(MOTOR_PWM, speed);
    } else if (speed < 0) {
        // Indietro
        digitalWrite(MOTOR_DIR1, LOW);
        digitalWrite(MOTOR_DIR2, HIGH);
        analogWrite(MOTOR_PWM, -speed);  // Valore assoluto
    } else {
        // Stop
        digitalWrite(MOTOR_DIR1, LOW);
        digitalWrite(MOTOR_DIR2, LOW);
        analogWrite(MOTOR_PWM, 0);
    }
}

// Uso:
setMotorSpeed(200);   // Avanti velocità 200/255
setMotorSpeed(-150);  // Indietro velocità 150/255
setMotorSpeed(0);     // Stop
```

**Come funziona PWM:**

```
Duty Cycle 25%:
     ┌─┐   ┌─┐   ┌─┐
5V   │ │   │ │   │ │
     │ │   │ │   │ │
0V ──┘ └───┘ └───┘ └───
     ON OFF ON OFF ...
     25%75% → Tensione media = 1.25V

Duty Cycle 75%:
     ┌───┐ ┌───┐ ┌───┐
5V   │   │ │   │ │   │
     │   │ │   │ │   │
0V ──┘   └─┘   └─┘   └─
     ON  O  ON  O  ...
     75% 25% → Tensione media = 3.75V

Frequenza ~500 Hz → Periodo 2ms
Occhio umano/LED/motore vedono media!
```

### 9.4 Sensore Temperatura DHT22 - Digitale

DHT22 è un sensore digitale temperatura+umidità molto popolare.

```cpp
// ═══════════════════════════════════════════════════════════
// DHT22 - TEMPERATURA E UMIDITÀ DIGITALE
// ═══════════════════════════════════════════════════════════

#include <DHT.h>

#define DHTPIN 2        // Pin dati DHT22
#define DHTTYPE DHT22   // Tipo sensore (DHT11, DHT22, DHT21)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    Serial.println(F("DHT22 Test"));

    dht.begin();
}

void loop() {
    // ─── Attesa minima tra letture: 2 secondi ───
    delay(2000);

    // ─── Lettura temperatura e umidità ───
    float humidity = dht.readHumidity();        // %
    float tempC = dht.readTemperature();        // °C
    float tempF = dht.readTemperature(true);    // °F

    // ─── Controllo errori ───
    if (isnan(humidity) || isnan(tempC)) {
        Serial.println(F("❌ Errore lettura DHT22!"));
        return;
    }

    // ─── Calcolo Heat Index (temperatura percepita) ───
    float heatIndexC = dht.computeHeatIndex(tempC, humidity, false);
    float heatIndexF = dht.computeHeatIndex(tempF, humidity);

    // ─── Output ───
    Serial.print(F("Umidità: "));
    Serial.print(humidity, 1);
    Serial.print(F("% | Temp: "));
    Serial.print(tempC, 1);
    Serial.print(F("°C ("));
    Serial.print(tempF, 1);
    Serial.print(F("°F) | Heat Index: "));
    Serial.print(heatIndexC, 1);
    Serial.println(F("°C"));
}
```

**Installazione libreria:**
```
Arduino IDE → Tools → Manage Libraries → Cerca "DHT sensor library" by Adafruit → Install
Dipendenze: Adafruit Unified Sensor (installa anche questa)
```

**Collegamenti DHT22:**
```
DHT22 (vista frontale con grata)
┌─────────┐
│  ████   │
│  ████   │
│  ████   │
└┬──┬──┬─┘
 │  │  │
VCC│ GND
 │ DATA
 │  │
5V D2
   GND

Note:
- Resistenza pull-up 10kΩ tra DATA e VCC (spesso integrata in moduli)
- Lettura lenta: min 2 secondi tra misure
- Range: -40 a 80°C, 0-100% umidità
- Precisione: ±0.5°C, ±2-5% RH
```

**Pattern non-bloccante con DHT22:**

```cpp
unsigned long dhtPrevMillis = 0;
const long DHT_INTERVAL = 2000;  // Min 2 secondi

void loop() {
    unsigned long currentMillis = millis();

    if (currentMillis - dhtPrevMillis >= DHT_INTERVAL) {
        dhtPrevMillis = currentMillis;

        float temp = dht.readTemperature();
        float hum = dht.readHumidity();

        if (!isnan(temp) && !isnan(hum)) {
            processData(temp, hum);
        }
    }

    // ✅ Sistema non bloccato, può fare altro!
}
```

### 9.5 Sensore Distanza Ultrasuoni HC-SR04

Misura distanza tramite tempo echo ultrasuoni (come i pipistrelli!).

```cpp
// ═══════════════════════════════════════════════════════════
// HC-SR04 - SENSORE DISTANZA ULTRASUONI
// ═══════════════════════════════════════════════════════════

const int TRIG_PIN = 9;   // Trigger output
const int ECHO_PIN = 10;  // Echo input

void setup() {
    Serial.begin(9600);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
}

long readDistanceCM() {
    // ─── 1. Invia impulso trigger 10µs ───
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // ─── 2. Misura durata echo ───
    // pulseIn(): attende pin HIGH, misura durata in µs
    // Timeout 30ms (30000µs) → max ~500cm
    long duration = pulseIn(ECHO_PIN, HIGH, 30000);

    if (duration == 0) {
        return -1;  // Timeout/errore (nessun ostacolo o fuori range)
    }

    // ─── 3. Calcola distanza ───
    // Velocità suono: ~343 m/s = 0.0343 cm/µs
    // Distanza = (durata/2) × velocità
    // durata/2 perché suono va e torna (andata+ritorno)
    long distance = duration * 0.0343 / 2;  // cm

    return distance;
}

void loop() {
    long dist = readDistanceCM();

    if (dist > 0 && dist < 400) {  // Range valido: 2-400cm
        Serial.print("Distanza: ");
        Serial.print(dist);
        Serial.println(" cm");
    } else if (dist == -1) {
        Serial.println("Timeout - Fuori range o nessun ostacolo");
    }

    delay(100);  // 100ms tra misure
}
```

**Come funziona HC-SR04:**

```
1. Arduino invia impulso 10µs su TRIG
   Arduino:  ___┌─10µs─┐___
   HC-SR04: Riceve → Emette 8 impulsi ultrasuoni 40kHz

2. Ultrasuoni viaggiano, colpiscono ostacolo, tornano indietro

   Arduino ────→ |Muro|
           ←─────┘

3. HC-SR04 riceve echo, mantiene ECHO pin HIGH per durata viaggio

   ECHO pin: ___┌─────────┐___
                ↑         ↑
             Inizio    Fine echo

4. Arduino misura durata con pulseIn()

Esempio:
- Ostacolo a 10 cm
- Tempo andata+ritorno: 10cm × 2 / 0.0343 cm/µs ≈ 583 µs
- pulseIn ritorna: 583
- Distanza: 583 × 0.0343 / 2 = 10 cm
```

**Collegamenti:**
```
HC-SR04
┌─────────────┐
│  TRIG  ECHO │
│   VCC  GND  │
└──┬────┬──┬─┘
   │    │  │
   D9  D10 GND
   │
   5V
```

**Pattern con filtro media mobile (riduce rumore):**

```cpp
const int SAMPLES = 5;
long distances[SAMPLES];
int sampleIndex = 0;

long getFilteredDistance() {
    // Aggiungi nuova misura
    distances[sampleIndex] = readDistanceCM();
    sampleIndex = (sampleIndex + 1) % SAMPLES;

    // Calcola media (ignora -1)
    long sum = 0;
    int validCount = 0;

    for (int i = 0; i < SAMPLES; i++) {
        if (distances[i] > 0) {
            sum += distances[i];
            validCount++;
        }
    }

    if (validCount == 0) return -1;
    return sum / validCount;
}
```

### 9.6 Display LCD I2C - Output Visivo

Display LCD 16x2 o 20x4 con interfaccia I2C (solo 2 fili dati!).

```cpp
// ═══════════════════════════════════════════════════════════
// LCD I2C - DISPLAY 16x2
// ═══════════════════════════════════════════════════════════

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Indirizzo I2C: 0x27 o 0x3F (verifica con I2C scanner)
// 16 colonne, 2 righe
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    // ─── Inizializza LCD ───
    lcd.init();           // Inizializzazione
    lcd.backlight();      // Accendi retroilluminazione

    // ─── Scrivi testo ───
    lcd.setCursor(0, 0);  // Colonna 0, Riga 0 (inizio riga 1)
    lcd.print("Hello ITS 2025!");

    lcd.setCursor(0, 1);  // Inizio riga 2
    lcd.print("Temp: ");
}

void loop() {
    float temp = readTemperature();

    // ─── Aggiorna solo parte variabile ───
    lcd.setCursor(6, 1);  // Posiziona dopo "Temp: "
    lcd.print(temp, 1);   // 1 decimale
    lcd.print(" C  ");    // Spazi extra cancellano cifre vecchie
    // Importante: "25.3 C  " sovrascrive "125.3 C" correttamente

    delay(1000);
}
```

**Caratteri speciali e custom:**

```cpp
// ═══ CARATTERI SPECIALI LCD ═══
lcd.print((char)223);  // ° (grado)
lcd.print((char)228);  // ä
lcd.print((char)239);  // ÷

// ═══ CREARE CARATTERE CUSTOM ═══
byte heart[8] = {
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000
};

void setup() {
    lcd.init();
    lcd.backlight();

    // Registra carattere custom in slot 0
    lcd.createChar(0, heart);

    // Usa carattere custom
    lcd.setCursor(0, 0);
    lcd.write(0);  // Stampa cuore
}
```

**Layout display organizzato:**

```cpp
// Esempio: Stazione meteo
void updateDisplay(float temp, float hum, long dist) {
    // ┌────────────────┐
    // │T:25.3C  H:65% │  ← Riga 0
    // │Dist: 123 cm   │  ← Riga 1
    // └────────────────┘

    // Riga 0: Temperatura e Umidità
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temp, 1);
    lcd.print("C ");

    lcd.setCursor(9, 0);
    lcd.print("H:");
    lcd.print(hum, 0);
    lcd.print("%  ");

    // Riga 1: Distanza
    lcd.setCursor(0, 1);
    lcd.print("Dist: ");
    lcd.print(dist);
    lcd.print(" cm   ");
}
```

**Trovare indirizzo I2C (se sconosciuto):**

```cpp
// I2C Scanner - trova indirizzo dispositivi I2C
#include <Wire.h>

void setup() {
    Serial.begin(9600);
    Wire.begin();

    Serial.println("Scanning I2C bus...");

    for (byte addr = 1; addr < 127; addr++) {
        Wire.beginTransmission(addr);
        if (Wire.endTransmission() == 0) {
            Serial.print("Trovato dispositivo I2C a 0x");
            Serial.println(addr, HEX);
        }
    }

    Serial.println("Scan completato");
}

void loop() {}

// Output esempio:
// Scanning I2C bus...
// Trovato dispositivo I2C a 0x27
// Scan completato
```

### 9.7 Comunicazione Seriale Avanzata - Comandi

Sistema di comandi seriali per controllo remoto Arduino:

```cpp
// ═══════════════════════════════════════════════════════════
// SISTEMA COMANDI SERIALI
// ═══════════════════════════════════════════════════════════

void setup() {
    Serial.begin(9600);
    while (!Serial) {
        ;  // Attendi connessione Serial (solo boards USB native)
    }

    pinMode(LED_PIN, OUTPUT);
    pinMode(RELAY_PIN, OUTPUT);

    Serial.println(F(""));
    Serial.println(F("═══════════════════════════════════"));
    Serial.println(F("   SISTEMA CONTROLLO REMOTO v1.0  "));
    Serial.println(F("═══════════════════════════════════"));
    Serial.println(F(""));
    Serial.println(F("Comandi disponibili:"));
    Serial.println(F("  LED ON      - Accendi LED"));
    Serial.println(F("  LED OFF     - Spegni LED"));
    Serial.println(F("  RELAY ON    - Attiva relay"));
    Serial.println(F("  RELAY OFF   - Disattiva relay"));
    Serial.println(F("  STATUS      - Mostra stato sistema"));
    Serial.println(F("  TEMP        - Leggi temperatura"));
    Serial.println(F("  HELP        - Mostra questo menu"));
    Serial.println(F(""));
}

void loop() {
    // ─── Controllo dati disponibili ───
    if (Serial.available() > 0) {
        // Leggi fino a newline
        String command = Serial.readStringUntil('\n');

        // Pulizia input
        command.trim();           // Rimuovi spazi/tab/newline
        command.toUpperCase();    // Converti maiuscolo

        // ─── Parsing comandi ───
        handleCommand(command);
    }

    // ... altre task ...
}

void handleCommand(String cmd) {
    // ═══ LED COMMANDS ═══
    if (cmd == "LED ON") {
        digitalWrite(LED_PIN, HIGH);
        Serial.println(F("✓ LED acceso"));
    }
    else if (cmd == "LED OFF") {
        digitalWrite(LED_PIN, LOW);
        Serial.println(F("✓ LED spento"));
    }

    // ═══ RELAY COMMANDS ═══
    else if (cmd == "RELAY ON") {
        digitalWrite(RELAY_PIN, HIGH);
        Serial.println(F("✓ Relay attivato"));
    }
    else if (cmd == "RELAY OFF") {
        digitalWrite(RELAY_PIN, LOW);
        Serial.println(F("✓ Relay disattivato"));
    }

    // ═══ INFO COMMANDS ═══
    else if (cmd == "STATUS") {
        printStatus();
    }
    else if (cmd == "TEMP") {
        float temp = readTemperature();
        Serial.print(F("Temperatura: "));
        Serial.print(temp, 1);
        Serial.println(F(" °C"));
    }
    else if (cmd == "HELP") {
        printHelp();
    }

    // ═══ COMANDO CON PARAMETRO ═══
    else if (cmd.startsWith("PWM ")) {
        // Esempio: "PWM 128"
        int value = cmd.substring(4).toInt();

        if (value >= 0 && value <= 255) {
            analogWrite(PWM_PIN, value);
            Serial.print(F("✓ PWM impostato a "));
            Serial.println(value);
        } else {
            Serial.println(F("❌ Errore: PWM deve essere 0-255"));
        }
    }

    // ═══ COMANDO NON RICONOSCIUTO ═══
    else {
        Serial.println(F("❌ Comando non riconosciuto"));
        Serial.println(F("Digita HELP per lista comandi"));
    }
}

void printStatus() {
    Serial.println(F(""));
    Serial.println(F("─── STATO SISTEMA ───"));
    Serial.print(F("LED:   "));
    Serial.println(digitalRead(LED_PIN) ? "ON" : "OFF");

    Serial.print(F("Relay: "));
    Serial.println(digitalRead(RELAY_PIN) ? "ON" : "OFF");

    Serial.print(F("Uptime: "));
    Serial.print(millis() / 1000);
    Serial.println(F(" sec"));

    Serial.println(F("─────────────────────"));
    Serial.println(F(""));
}
```

**Comandi con parsing avanzato:**

```cpp
// ═══ PARSING COMANDO CON MULTIPLI PARAMETRI ═══
// Esempio: "SET LED 13 HIGH"

void parseCommand(String cmd) {
    // Split comando in parole
    int space1 = cmd.indexOf(' ');
    int space2 = cmd.indexOf(' ', space1 + 1);
    int space3 = cmd.indexOf(' ', space2 + 1);

    String action = cmd.substring(0, space1);           // "SET"
    String device = cmd.substring(space1 + 1, space2);  // "LED"
    String pin = cmd.substring(space2 + 1, space3);     // "13"
    String value = cmd.substring(space3 + 1);           // "HIGH"

    if (action == "SET" && device == "LED") {
        int pinNum = pin.toInt();

        if (value == "HIGH") {
            digitalWrite(pinNum, HIGH);
            Serial.println("✓ Pin " + pin + " impostato HIGH");
        } else if (value == "LOW") {
            digitalWrite(pinNum, LOW);
            Serial.println("✓ Pin " + pin + " impostato LOW");
        }
    }
}
```

### 9.8 Progetto Completo: Stazione Meteo IoT

**Prompt per IA:**
```
Crea sketch Arduino completo per stazione meteo con:

HARDWARE:
- Arduino Uno R4
- DHT22 su pin 2 (temp+umidità)
- Display LCD I2C 16x2 (0x27)
- LED allarme su pin 13
- Buzzer su pin 8

FUNZIONALITÀ:
- Leggi temp/umidità ogni 5 secondi
- Display LCD:
  * Riga 1: "T:25.3C  H:65%"
  * Riga 2: "Status: OK"
- LED lampeggia se temp>30°C o umidità>80%
- Buzzer suona se temp>35°C (allarme critico)
- Report seriale ogni 10 secondi con timestamp
- Comando seriale "RESET" resetta allarme
- Usa millis() (non-bloccante)

LIBRERIE:
- DHT sensor library
- LiquidCrystal I2C

OUTPUT:
1. Sketch completo commentato
2. Schema collegamenti
3. Librerie da installare
```

---

## 10. Debugging e Testing

### 10.1 Debug Seriale - Tecniche Professionali

```cpp
// ═══════════════════════════════════════════════════════════
// DEBUGGING SERIALE - PATTERN PROFESSIONALI
// ═══════════════════════════════════════════════════════════

// ─── MACRO DEBUG CONDIZIONALE ───
#define DEBUG 1  // Imposta a 0 per build produzione

#if DEBUG
    #define DEBUG_PRINT(x)    Serial.print(x)
    #define DEBUG_PRINTLN(x)  Serial.println(x)
    #define DEBUG_PRINTF(x,y) Serial.print(x, y)
#else
    #define DEBUG_PRINT(x)
    #define DEBUG_PRINTLN(x)
    #define DEBUG_PRINTF(x,y)
#endif

void loop() {
    int sensor = analogRead(A0);

    DEBUG_PRINT("Sensor raw: ");
    DEBUG_PRINTLN(sensor);  // Stampato SOLO se DEBUG=1

    // In produzione (DEBUG=0), queste righe sono eliminate
    // dal compilatore → nessun overhead!

    // Processing normale...
}

// ═══ DEBUG CON TIMESTAMP ═══
void debugLog(const char* message) {
    #if DEBUG
        unsigned long seconds = millis() / 1000;
        unsigned long minutes = seconds / 60;
        seconds = seconds % 60;

        Serial.print("[");
        if (minutes < 10) Serial.print("0");
        Serial.print(minutes);
        Serial.print(":");
        if (seconds < 10) Serial.print("0");
        Serial.print(seconds);
        Serial.print("] ");
        Serial.println(message);
    #endif
}

// Uso:
debugLog("Sistema avviato");
debugLog("Sensore letto");

// Output:
// [00:00] Sistema avviato
// [00:05] Sensore letto

// ═══ DEBUG VARIABILI MULTIPLE ═══
void debugVars(const char* label, int val1, float val2, bool val3) {
    #if DEBUG
        Serial.print(label);
        Serial.print(" | int=");
        Serial.print(val1);
        Serial.print(" | float=");
        Serial.print(val2, 2);
        Serial.print(" | bool=");
        Serial.println(val3 ? "true" : "false");
    #endif
}

// Uso:
debugVars("Stato", sensorValue, temperature, alarmActive);

// Output:
// Stato | int=512 | float=25.30 | bool=false
```

### 10.2 Debug LED Pattern

Quando la seriale non è disponibile (es: alimentazione batteria), usa pattern LED:

```cpp
// ═══════════════════════════════════════════════════════════
// DEBUG LED PATTERN (senza seriale)
// ═══════════════════════════════════════════════════════════

void debugBlink(int times) {
    for (int i = 0; i < times; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
    }
    delay(1000);  // Pausa tra sequenze
}

// ═══ CODICI ERRORE LED ═══
void signalError(int errorCode) {
    while (1) {  // Loop infinito in caso errore fatale
        debugBlink(errorCode);
        delay(2000);
    }
}

// Uso:
if (sensor1_error) debugBlink(1);  // 1 blink = sensore 1 errore
if (sensor2_error) debugBlink(2);  // 2 blink = sensore 2 errore
if (sd_card_error) debugBlink(3);  // 3 blink = SD errore
if (critical_error) signalError(5); // 5 blink infiniti = fatale

// ═══ PATTERN SOS (EMERGENCY) ═══
void blinkSOS() {
    // S: · · ·
    for (int i = 0; i < 3; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
    }

    delay(400);

    // O: — — —
    for (int i = 0; i < 3; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(600);
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
    }

    delay(400);

    // S: · · ·
    for (int i = 0; i < 3; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(200);
        digitalWrite(LED_BUILTIN, LOW);
        delay(200);
    }

    delay(2000);  // Pausa prima di ripetere
}
```

### 10.3 Testing C con assert.h

```c
// ═══════════════════════════════════════════════════════════
// UNIT TESTING C - PATTERN PROFESSIONALE
// ═══════════════════════════════════════════════════════════

#include <assert.h>
#include <stdio.h>
#include <stdbool.h>

// ─── Funzione da testare ───
int sum_array(const int arr[], int n) {
    if (arr == NULL || n <= 0) {
        return 0;
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

// ─── Test Suite ───
void test_sum_array() {
    printf("Testing sum_array()...\n");

    // Test 1: Array normale
    int arr1[] = {1, 2, 3, 4, 5};
    assert(sum_array(arr1, 5) == 15);
    printf("  ✓ Test 1: Array normale\n");

    // Test 2: Array vuoto
    assert(sum_array(arr1, 0) == 0);
    printf("  ✓ Test 2: Array vuoto (n=0)\n");

    // Test 3: Puntatore NULL
    assert(sum_array(NULL, 5) == 0);
    printf("  ✓ Test 3: Puntatore NULL\n");

    // Test 4: Single element
    int arr2[] = {42};
    assert(sum_array(arr2, 1) == 42);
    printf("  ✓ Test 4: Singolo elemento\n");

    // Test 5: Numeri negativi
    int arr3[] = {-1, -2, -3};
    assert(sum_array(arr3, 3) == -6);
    printf("  ✓ Test 5: Numeri negativi\n");

    // Test 6: Array grande
    int arr4[100];
    for (int i = 0; i < 100; i++) arr4[i] = 1;
    assert(sum_array(arr4, 100) == 100);
    printf("  ✓ Test 6: Array grande (100 elementi)\n");

    printf("✅ Tutti i test sum_array passati!\n\n");
}

int main(void) {
    printf("═══════════════════════════════════\n");
    printf("  TEST SUITE STARTED\n");
    printf("═══════════════════════════════════\n\n");

    test_sum_array();
    // test_other_function();
    // test_another_function();

    printf("═══════════════════════════════════\n");
    printf("  ✅ ALL TESTS PASSED!\n");
    printf("═══════════════════════════════════\n");

    return 0;
}
```

**Output esempio:**
```
═══════════════════════════════════
  TEST SUITE STARTED
═══════════════════════════════════

Testing sum_array()...
  ✓ Test 1: Array normale
  ✓ Test 2: Array vuoto (n=0)
  ✓ Test 3: Puntatore NULL
  ✓ Test 4: Singolo elemento
  ✓ Test 5: Numeri negativi
  ✓ Test 6: Array grande (100 elementi)
✅ Tutti i test sum_array passati!

═══════════════════════════════════
  ✅ ALL TESTS PASSED!
═══════════════════════════════════
```

### 10.4 Valgrind - Memory Detective

```bash
# ═══════════════════════════════════════════════════════════
# VALGRIND - ANALISI MEMORIA COMPLETA
# ═══════════════════════════════════════════════════════════

# ─── Compilazione con debug symbols ───
gcc -g -std=c99 -Wall -Wextra myprogram.c -o myprogram

# ─── Esecuzione Valgrind completa ───
valgrind \
    --leak-check=full \          # Rileva tutti memory leak
    --show-leak-kinds=all \      # Mostra tutti tipi leak
    --track-origins=yes \        # Traccia origine valori non inizializzati
    --verbose \                  # Output dettagliato
    --log-file=valgrind.log \    # Salva output in file
    ./myprogram

# ─── Analisi solo leak summary ───
valgrind --leak-check=summary ./myprogram

# ─── Controllo thread safety (programmi multi-thread) ───
valgrind --tool=helgrind ./myprogram

# ─── Profiling cache ───
valgrind --tool=cachegrind ./myprogram
```

**Esempio completo con interpretazione:**

```c
// leak_example.c
#include <stdlib.h>
#include <string.h>

int main(void) {
    // ❌ Leak 1: malloc senza free
    int *leak1 = malloc(100 * sizeof(int));
    *leak1 = 42;
    // Manca: free(leak1);

    // ❌ Leak 2: strdup (se disponibile) senza free
    char *leak2 = malloc(20);
    strcpy(leak2, "Hello");
    // Manca: free(leak2);

    // ✅ Corretto: malloc + free
    int *ok = malloc(50 * sizeof(int));
    free(ok);

    // ❌ Use after free
    int *bad = malloc(10 * sizeof(int));
    free(bad);
    bad[0] = 10;  // Errore!

    return 0;
}
```

```bash
$ gcc -g leak_example.c -o leak_example
$ valgrind --leak-check=full ./leak_example
```

**Output Valgrind annotato:**

```
==12345== Memcheck, a memory error detector
==12345== Using Valgrind-3.19.0
==12345==
==12345== Invalid write of size 4
==12345==    at 0x109167: main (leak_example.c:18)
==12345==  Address 0x4a3d040 is 0 bytes inside a block of size 40 free'd
                    ↑
                    Questo è il "use after free" su bad[0]

==12345== HEAP SUMMARY:
==12345==     in use at exit: 420 bytes in 2 blocks
                                ↑        ↑
                          100*4 + 20 = 420  (leak1 + leak2)

==12345==   total heap usage: 3 allocs, 1 frees, 470 bytes allocated
                                ↑         ↑
                        3 malloc()  1 free()

==12345== LEAK SUMMARY:
==12345==    definitely lost: 420 bytes in 2 blocks
                               ↑
                        Memory leak confermato!

==12345==    indirectly lost: 0 bytes in 0 blocks
==12345==      possibly lost: 0 bytes in 0 blocks
==12345==    still reachable: 0 bytes in 0 blocks
==12345==         suppressed: 0 bytes in 0 blocks

==12345== ERROR SUMMARY: 2 errors from 2 contexts
                          ↑
                    1 use-after-free + 1 leak
```

**Come interpretare:**
- ✅ `All heap blocks were freed` → PERFETTO!
- ❌ `definitely lost` → Memory leak CONFERMATO, fixare subito
- ⚠️ `possibly lost` → Possibile leak (puntatori interni a struct)
- ⚠️ `still reachable` → Memoria non liberata ma ancora accessibile (variabili globali, spesso OK)
- ❌ `Invalid write/read` → Buffer overflow o use-after-free

---

## 11. Best Practices 2025

### 11.1 Naming Conventions C/Arduino

```c
// ═══════════════════════════════════════════════════════════
// CONVENZIONI NOMI - STILE PROFESSIONALE
// ═══════════════════════════════════════════════════════════

// ─── COSTANTI PREPROCESSORE ───
#define MAX_BUFFER_SIZE 256        // UPPERCASE_SNAKE_CASE
#define LED_PIN 13
#define SENSOR_THRESHOLD_HIGH 500

// ─── Costanti globali (const) ───
const int LED_PIN = 13;            // PascalCase o UPPERCASE
const long BAUD_RATE = 9600;
const float TEMP_THRESHOLD = 25.0;

// ─── Variabili globali ───
int sensorValue = 0;               // camelCase
float temperatureCelsius;
bool isAlarmActive;

// ─── Variabili locali ───
void myFunction() {
    int localCounter = 0;          // camelCase
    float tempReading;
}

// ─── Funzioni ───
void readSensor();                 // camelCase
int calculateAverage(int* arr, int n);
bool isValidInput(int value);

// ─── Struct/Typedef ───
typedef struct {
    float temperature;
    float humidity;
    unsigned long timestamp;
} SensorData;                      // PascalCase per tipo

typedef struct sensor_reading_t {  // snake_case + _t (stile C)
    int value;
    bool valid;
} SensorReading;

// ─── Enum ───
typedef enum {
    STATE_IDLE,                    // UPPERCASE per valori
    STATE_READING,
    STATE_PROCESSING,
    STATE_ERROR
} SystemState;                     // PascalCase per tipo
```

**Linee guida:**
- ✅ Nomi descrittivi: `temperatureCelsius` non `t` o `temp`
- ✅ Unità nei nomi: `delayMillis`, `distanceCM`, `speedMPS`
- ✅ Prefissi boolean: `isValid`, `hasData`, `shouldRetry`
- ❌ Evita abbreviazioni oscure: `btn` → `button`, `tmp` → `temperature`

### 11.2 Gestione Errori C - Pattern Professionali

```c
// ═══════════════════════════════════════════════════════════
// GESTIONE ERRORI - CODICI RITORNO
// ═══════════════════════════════════════════════════════════

// ─── Pattern 1: Codici errore enum ───
typedef enum {
    ERR_OK = 0,                // Successo
    ERR_NULL_POINTER = -1,     // Puntatore NULL
    ERR_OUT_OF_MEMORY = -2,    // malloc fallita
    ERR_INVALID_INPUT = -3,    // Input non valido
    ERR_FILE_NOT_FOUND = -4,   // File mancante
    ERR_TIMEOUT = -5,          // Timeout operazione
    ERR_SENSOR_FAIL = -6       // Sensore non risponde
} ErrorCode;

ErrorCode processData(int *data, int size, int *result) {
    // ─── Validazione input ───
    if (data == NULL || result == NULL) {
        return ERR_NULL_POINTER;
    }

    if (size <= 0 || size > 1000) {
        return ERR_INVALID_INPUT;
    }

    // ─── Allocazione memoria ───
    int *buffer = malloc(size * sizeof(int));
    if (buffer == NULL) {
        return ERR_OUT_OF_MEMORY;
    }

    // ─── Processing ───
    *result = 42;  // Esempio

    // ─── Cleanup ───
    free(buffer);
    return ERR_OK;
}

// ─── Uso con gestione errori ───
int result;
ErrorCode err = processData(arr, n, &result);

if (err != ERR_OK) {
    switch (err) {
        case ERR_NULL_POINTER:
            fprintf(stderr, "Errore: puntatore NULL\n");
            break;
        case ERR_OUT_OF_MEMORY:
            fprintf(stderr, "Errore: memoria insufficiente\n");
            break;
        case ERR_INVALID_INPUT:
            fprintf(stderr, "Errore: input non valido\n");
            break;
        default:
            fprintf(stderr, "Errore sconosciuto: %d\n", err);
    }
    return -1;
}

// Procedi con result valido
printf("Risultato: %d\n", result);
```

**Pattern 2: bool + output parameter:**

```c
// Ritorna bool (successo/fallimento) + dato via puntatore
bool readSensor(int pin, float *output) {
    if (output == NULL) {
        return false;  // Input non valido
    }

    int raw = analogRead(pin);

    // Controllo range valido
    if (raw < 50 || raw > 950) {
        return false;  // Sensore scollegato
    }

    *output = raw * (5.0 / 1023.0);  // Conversione
    return true;  // Successo
}

// Uso:
float voltage;
if (readSensor(A0, &voltage)) {
    printf("Voltaggio: %.2fV\n", voltage);
} else {
    printf("Errore lettura sensore\n");
}
```

### 11.3 Documentazione Doxygen

```c
/**
 * @file sensor_lib.h
 * @brief Libreria gestione sensori Arduino
 * @author Studente ITS
 * @date 2025-01-15
 * @version 1.0
 */

/**
 * @brief Legge temperatura da sensore TMP36
 *
 * Converte lettura ADC da sensore TMP36 in temperatura Celsius.
 * Formula: Temp°C = (Vout - 0.5) × 100
 *
 * @param pin Pin analogico Arduino (A0-A5)
 * @param[out] tempC Puntatore per salvare temperatura (non-NULL)
 *
 * @return true se lettura valida, false se errore
 *
 * @retval true  Lettura successo, tempC contiene temperatura valida
 * @retval false Errore: pin invalido, tempC NULL, o sensore scollegato
 *
 * @note Sensore deve essere collegato: Vcc→5V, GND→GND, Vout→pin
 * @warning Non chiamare più di una volta al secondo (sensore lento)
 *
 * @see readHumidity() per lettura umidità
 *
 * @example
 * float temperature;
 * if (readTMP36(A0, &temperature)) {
 *     Serial.print("Temp: ");
 *     Serial.println(temperature);
 * } else {
 *     Serial.println("Errore sensore");
 * }
 *
 * @since v1.0
 */
bool readTMP36(int pin, float *tempC);

/**
 * @brief Calcola media mobile ultimi N valori
 *
 * Implementa filtro media mobile (moving average) per ridurre
 * rumore nelle letture sensore. Mantiene buffer circolare interno.
 *
 * @param newValue Nuovo valore da aggiungere
 * @param windowSize Dimensione finestra (1-100)
 *
 * @return Media ultimi windowSize valori
 *
 * @pre windowSize deve essere > 0 e <= 100
 * @post Buffer interno aggiornato con newValue
 *
 * @code
 * // Esempio filtro temperature
 * for (int i = 0; i < 100; i++) {
 *     float raw = readRawTemp();
 *     float filtered = movingAverage(raw, 10);  // Media 10 campioni
 *     Serial.println(filtered);
 *     delay(100);
 * }
 * @endcode
 */
float movingAverage(float newValue, int windowSize);
```

### 11.4 Gestione Memoria Arduino - Ottimizzazione

```cpp
// ═══════════════════════════════════════════════════════════
// OTTIMIZZAZIONE RAM ARDUINO
// ═══════════════════════════════════════════════════════════

// ❌ EVITARE: String dinamiche (frammentazione heap!)
void badExample() {
    String message = "Temp: ";
    message += String(temperature);
    message += " °C";
    Serial.println(message);
    // Ogni += alloca/dealloca memoria → frammentazione!
}

// ✅ USARE: char array statici (su stack)
void goodExample() {
    char message[50];
    snprintf(message, sizeof(message), "Temp: %.1f °C", temperature);
    Serial.println(message);
    // Nessuna allocazione dinamica!
}

// ═══ STRINGHE IN FLASH (F macro) ═══
// Arduino Uno: 32 KB Flash, solo 2 KB RAM!

// ❌ Spreca RAM
Serial.println("Questo testo molto lungo occupa RAM preziosa");

// ✅ Risparmia RAM (testo resta in Flash)
Serial.println(F("Questo testo molto lungo resta in Flash"));

// ═══ CONST DATA IN FLASH ═══
// ❌ Array in RAM
const int daysInMonth[] = {31,28,31,30,31,30,31,31,30,31,30,31};

// ✅ Array in Flash (PROGMEM)
#include <avr/pgmspace.h>

const int daysInMonth[] PROGMEM = {31,28,31,30,31,30,31,31,30,31,30,31};

// Lettura da PROGMEM:
int days = pgm_read_word(&daysInMonth[month]);

// ═══ MONITOR RAM DISPONIBILE ═══
int freeRam() {
    extern int __heap_start, *__brkval;
    int v;
    return (int) &v - (__brkval == 0 ?
                       (int) &__heap_start :
                       (int) __brkval);
}

void setup() {
    Serial.begin(9600);

    Serial.print(F("RAM libera all'avvio: "));
    Serial.print(freeRam());
    Serial.println(F(" byte"));

    // Arduino Uno ha 2048 byte RAM
    // Se freeRam() < 200 → rischio stack/heap collision!
}

// ═══ OTTIMIZZAZIONE VARIABILI ═══
// Usa tipi più piccoli quando possibile

// ❌ Spreco memoria
int ledPin = 13;           // 2 byte per valore max 13
unsigned long counter = 0; // 4 byte per contare fino a 100

// ✅ Ottimizzato
uint8_t ledPin = 13;       // 1 byte sufficiente (0-255)
uint8_t counter = 0;       // 1 byte se conta solo fino a 255
```

---

## 12. Esercitazioni Pratiche

### 12.1 Esercizio C: Parser CSV

**Obiettivo:** Leggere file CSV e creare array di struct.

```c
// ═══════════════════════════════════════════════════════════
// ESERCIZIO: CSV PARSER
// ═══════════════════════════════════════════════════════════

// File: persons.csv
// Nome,Età,Città
// Mario,30,Roma
// Laura,25,Milano
// Giuseppe,35,Napoli

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    char city[50];
} Person;

/**
 * Legge file CSV e alloca array struct Person
 *
 * @param filename Path file CSV
 * @param[out] people Puntatore a array Person (allocato da funzione)
 * @param[out] count Numero persone lette
 * @return true se successo, false se errore
 *
 * @note Caller deve liberare *people con free()
 */
bool readCSV(const char *filename, Person **people, int *count);

/**
 * Stampa dati persona
 */
void printPerson(const Person *p);

/**
 * Libera array persone
 */
void freePeople(Person *people);
```

**Soluzione con prompt IA:**

```
Implementa in C99 le funzioni readCSV, printPerson, freePeople con:

REQUISITI:
- Legge file CSV con header (prima riga saltata)
- Parsa righe formato: "Nome,Età,Città"
- Alloca dinamicamente array Person usando realloc
- Gestisce errori: file non trovato, malloc fallita, formato invalido
- Include main() con test completo
- Usa solo C99 standard library

GESTIONE ERRORI:
- File non esiste: ritorna false
- malloc/realloc fallisce: libera memoria già allocata, ritorna false
- Riga formato invalido: skippa riga, continua parsing

TEST:
- Crea file persons.csv di esempio
- Leggi e stampa tutti
- Verifica memoria con valgrind (no leak)

OUTPUT:
1. Codice completo con commenti
2. Esempio file CSV
3. Comando compilazione e test
```

### 12.2 Esercizio Arduino: Sistema Irrigazione

**Obiettivo:** Sistema automatico irrigazione piante.

**Specifiche dettagliate:**

```
═══════════════════════════════════════════════════════════
SISTEMA IRRIGAZIONE AUTOMATICO
═══════════════════════════════════════════════════════════

HARDWARE:
- Arduino Uno
- Sensore umidità suolo analogico su A0
- Relay controllo pompa su pin 7
- LED status su pin 13
- Pulsante test su pin 2 (pull-up)
- LCD I2C 16x2 (0x27)

LOGICA:
1. Leggi umidità suolo ogni 10 secondi
   - Asciutto (>700): "Suolo ASCIUTTO"
   - Medio (400-700): "Suolo OK"
   - Bagnato (<400): "Suolo UMIDO"

2. Irrigazione automatica:
   - Se umidità > 700 → attiva pompa per 5 secondi
   - Min 60 secondi tra cicli irrigazione (cooldown)
   - Max 30 secondi pompaggio continuo (safety)

3. Pulsante test:
   - Pressione breve: ciclo manuale 3 secondi
   - Pressione lunga (>2s): reset cooldown

4. Display LCD:
   - Riga 1: "Umid: XXX (STATUS)"
   - Riga 2: "Pompa: ON/OFF"
   - Se errore: "ERRORE SENSORE!"

5. LED status:
   - Blink lento: sistema normale
   - Blink veloce: irrigazione attiva
   - Sempre acceso: errore sensore

SICUREZZA:
- Timeout max pompaggio: 30 secondi continui
- Cooldown minimo: 60 secondi tra cicli
- Controllo sensore scollegato (valore < 50 o > 1000)
- LED lampeggia SOS se errore critico

VINCOLI:
- Usa millis() (NO delay lunghi)
- Debouncing pulsante software (50ms)
- State machine per gestione stati
- Commenti esplicativi

LIBRERIE:
- LiquidCrystal I2C
```

**Prompt per IA:**

```
Crea sketch Arduino completo per sistema irrigazione con specifiche:
[incolla specifiche sopra]

OUTPUT RICHIESTO:
1. Codice sketch con state machine
2. Schema collegamenti hardware
3. Librerie da installare
4. Procedura test completa step-by-step
5. Troubleshooting errori comuni
```

### 12.3 Esercizio C: Linked List Completa

**Obiettivo:** Implementare libreria linked list generica.

```c
// ═══════════════════════════════════════════════════════════
// ESERCIZIO: LINKED LIST LIBRARY
// ═══════════════════════════════════════════════════════════

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// ─── Funzioni da implementare ───

/**
 * Crea nuovo nodo con valore data
 * @return Puntatore a nodo allocato, o NULL se errore
 */
Node* list_create(int data);

/**
 * Inserisce nodo all'inizio lista
 * @return Nuovo head della lista
 */
Node* list_insert_head(Node *head, int data);

/**
 * Inserisce nodo alla fine lista
 * @return Head della lista (invariato se lista non vuota)
 */
Node* list_insert_tail(Node *head, int data);

/**
 * Cerca nodo con valore data
 * @return Puntatore a nodo trovato, o NULL se non esiste
 */
Node* list_search(Node *head, int data);

/**
 * Elimina primo nodo con valore data
 * @param[in,out] head Puntatore a puntatore head (modificato se elimina head)
 * @return true se eliminato, false se non trovato
 */
bool list_delete(Node **head, int data);

/**
 * Stampa lista: [1] -> [2] -> [3] -> NULL
 */
void list_print(Node *head);

/**
 * Libera intera lista
 */
void list_free(Node *head);

/**
 * Conta elementi lista
 */
int list_length(Node *head);

/**
 * Inverte lista in-place
 * @return Nuovo head (vecchia tail)
 */
Node* list_reverse(Node *head);
```

**Prompt IA:**

```
Implementa in C99 libreria linked list con funzioni:
- list_create, list_insert_head, list_insert_tail
- list_search, list_delete
- list_print, list_free, list_length, list_reverse

REQUISITI:
- Gestione memoria sicura (no leak, no double-free)
- Controlli NULL su tutti puntatori
- Documentazione Doxygen per ogni funzione
- Suite test completa con assert.h per tutte funzioni
- Testa casi: lista vuota, singolo elemento, multipli elementi

TEST:
- Crea lista: 1 -> 2 -> 3 -> 4 -> 5
- Testa tutte operazioni
- Verifica con valgrind (no leak)

OUTPUT:
1. File .h con dichiarazioni
2. File .c con implementazioni
3. File test.c con suite completa
4. Makefile per compilare
```

---

## ✅ Checklist Completamento Modulo 2

### Conoscenze C

- [ ] Conosco differenze C vs Python/JavaScript
- [ ] Gestisco correttamente puntatori e array
- [ ] Alloco/libero memoria correttamente (malloc/free)
- [ ] Riconosco funzioni non-standard (strdup, asprintf)
- [ ] Evito buffer overflow (uso snprintf, strncpy)
- [ ] Scrivo codice C99 standard-compliant
- [ ] So usare valgrind per trovare memory leak
- [ ] Scrivo test con assert.h

### Prompt Engineering C

- [ ] Uso template prompt per funzioni C
- [ ] Specifico sempre "C99 standard, NO estensioni"
- [ ] Richiedo gestione errori robusta
- [ ] Valido codice IA con checklist
- [ ] Compilo con flag strict (-Wall -Wextra -Wpedantic -Werror)

### Arduino Hardware

- [ ] Configuro correttamente pin (INPUT/OUTPUT/INPUT_PULLUP)
- [ ] Uso ADC per sensori analogici
- [ ] Uso PWM per LED dimming e motori
- [ ] Collego sensori digitali (DHT22, ultrasuoni)
- [ ] Uso display LCD I2C
- [ ] Implemento comunicazione seriale con comandi

### Arduino Software

- [ ] Scrivo sketch con struttura professionale
- [ ] Uso millis() invece di delay() (pattern non-bloccante)
- [ ] Implemento multi-task simultanei
- [ ] Uso state machine per logica complessa
- [ ] Debouncing pulsanti software
- [ ] Gestisco errori sensori (isnan, timeout)
- [ ] Ottimizzo RAM (F() macro, char array vs String)

### Debugging

- [ ] Debug con Serial + macro condizionali
- [ ] Pattern LED per debug senza seriale
- [ ] Uso Valgrind per analisi memoria C
- [ ] Scrivo test automatici

### Progetti

- [ ] Ho completato almeno 2 esercizi C
- [ ] Ho implementato almeno 1 progetto Arduino completo
- [ ] So generare codice con prompt efficaci
- [ ] Valido sempre codice IA prima di usarlo

---

## 📚 Risorse Aggiuntive

### Documentazione Online

**C:**
- [C99 Standard PDF](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf)
- [cppreference.com](https://en.cppreference.com/w/c) - Reference C completo
- [C FAQ](http://c-faq.com/) - Domande frequenti

**Arduino:**
- [Arduino Reference](https://www.arduino.cc/reference/en/) - Tutte le funzioni
- [Arduino Forum](https://forum.arduino.cc/) - Community support
- [PlatformIO Docs](https://docs.platformio.org/) - IDE avanzato

### Tool Online

- [Compiler Explorer (godbolt)](https://godbolt.org/) - Compila C online, vedi assembly
- [Wokwi](https://wokwi.com/) - Simulatore Arduino online (FANTASTICO!)
- [OnlineGDB](https://www.onlinegdb.com/online_c_compiler) - Compila/debug C online
- [Valgrind Quick Start](https://valgrind.org/docs/manual/quick-start.html)

### Librerie Arduino Popolari 2025

```
SENSORI:
├── DHT sensor library (Adafruit) - Temp/umidità DHT11/22
├── Adafruit_BMP280 - Pressione/temperatura
├── Adafruit_Sensor - API unificata sensori
├── OneWire + DallasTemperature - DS18B20
└── NewPing - Ultrasuoni HC-SR04

DISPLAY:
├── LiquidCrystal_I2C - LCD caratteri I2C
├── Adafruit_SSD1306 - Display OLED 128x64
├── Adafruit_GFX - Libreria grafica base
└── TFT_eSPI - Display TFT colorati

COMUNICAZIONE:
├── WiFi (ESP32/ESP8266) - WiFi integrato
├── PubSubClient - Client MQTT
├── ArduinoJson - Parsing/generazione JSON
├── HTTPClient - Richieste HTTP
└── WebServer - Server web embedded

MOTORI/SERVO:
├── Servo - Servo motori (built-in)
├── AccelStepper - Motori stepper
├── Adafruit_MotorShield - Shield motori DC/stepper
└── ESP32Servo - Servo per ESP32

STORAGE:
├── SD - Lettura/scrittura SD card
├── EEPROM - Memoria persistente (built-in)
└── Preferences (ESP32) - Key-value storage

SENSORI AVANZATI:
├── MPU6050 - Accelerometro + giroscopio
├── Adafruit_GPS - Moduli GPS
└── MAX30100 - Sensore battito cardiaco
```

### Installazione Librerie Arduino

```cpp
// ═══ METODO 1: Library Manager (GUI) ═══
// Arduino IDE → Tools → Manage Libraries
// Cerca nome libreria → Install

// ═══ METODO 2: Arduino CLI ═══
arduino-cli lib install "DHT sensor library"
arduino-cli lib install "LiquidCrystal I2C"
arduino-cli lib install "Adafruit GFX Library"

// ═══ METODO 3: Manuale (ZIP) ═══
// Sketch → Include Library → Add .ZIP Library
// Seleziona file .zip libreria scaricata

// ═══ VERIFICA INSTALLATE ═══
arduino-cli lib list

// ═══ AGGIORNA TUTTE ═══
arduino-cli lib upgrade
```

### Progetti Esempio Completi

Repository GitHub consigliati:

```
PROGETTI ARDUINO:
- arduino/arduino-examples
  Esempi ufficiali base

- adafruit/Adafruit_Learning_System_Guides
  Tutorial progetti con componenti Adafruit

- RobotPatient/arduino_tutorials
  Tutorial step-by-step principianti

EMBEDDED C:
- torvalds/linux (kernel)
  Esempio C professionale massimo livello

- micropython/micropython
  Python su microcontrollori, C backend

- espressif/arduino-esp32
  Arduino core per ESP32, esempi avanzati
```

---

**🎓 FINE MODULO 2 - PROGRAMMAZIONE ASSISTITA C E ARDUINO**

**Versione:** 4.0 | **Aggiornamento:** Gennaio 2025 | **Corso ITS**

**Autori:** Docente ITS + Claude 3.5 Sonnet (Assistenza IA)

---

**Prossimo:** MODULO 3 - Progetti Completi e Verifica Finale

---

**Statistiche Modulo:**
- **Righe totali:** ~4800+
- **Esempi codice:** 50+ completi
- **Esercizi pratici:** 12
- **Template prompt:** 8 professionali
- **Tool coperti:** GCC, Valgrind, Arduino IDE, PlatformIO
- **Librerie insegnate:** 15+ popolari
