# 📘 MODULO 3
# Programmazione C con Intelligenza Artificiale
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita 2025
### Durata: 6 ore | Livello: Intermedio-Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti del Linguaggio C](#2-fondamenti-del-linguaggio-c)
3. [Setup Ambiente di Sviluppo](#3-setup-ambiente-di-sviluppo)
4. [Problemi Ricorrenti del Codice Generato](#4-problemi-ricorrenti-del-codice-generato)
5. [Gestione della Memoria](#5-gestione-della-memoria)
6. [Puntatori e Array](#6-puntatori-e-array)
7. [Stringhe in C](#7-stringhe-in-c)
8. [Strutture Dati](#8-strutture-dati)
9. [File I/O](#9-file-io)
10. [Debugging Assistito con IA](#10-debugging-assistito-con-ia)
11. [Testing e Validazione](#11-testing-e-validazione)
12. [Best Practices C Professionale](#12-best-practices-c-professionale)
13. [Pattern di Programmazione Sicura](#13-pattern-di-programmazione-sicura)
14. [Progetti Completi Guidati](#14-progetti-completi-guidati)
15. [Esercizi Pratici](#15-esercizi-pratici)

---

## 1. Introduzione e Obiettivi

### 1.1 Perché C nel 2025?

Il linguaggio **C** è nato nel 1972, ma nel 2025 è ancora **fondamentale** per:

**Sistemi Embedded:**
- Arduino, ESP32, STM32
- Firmware per dispositivi IoT
- Controllo industriale (PLC)
- Automotive (ABS, airbag, centraline)

**Sistemi Operativi:**
- Linux kernel (98% C)
- Windows kernel
- macOS/iOS core

**Performance Critiche:**
- Database (PostgreSQL, MySQL core)
- Driver hardware
- Librerie di calcolo scientifico

**Perché C è ancora rilevante:**
- ✅ **Controllo totale** su memoria e hardware
- ✅ **Velocità massima** di esecuzione
- ✅ **Footprint minimo** (perfetto per embedded)
- ✅ **Portabilità** su qualsiasi architettura
- ✅ **Standard stabile** (C99/C11/C17)

**Ma... C è anche pericoloso:**
- ❌ Gestione manuale della memoria (memory leak)
- ❌ Buffer overflow e vulnerabilità
- ❌ Nessun controllo bounds automatico
- ❌ Undefined behavior difficile da debuggare

**Soluzione: IA come assistente esperto!**

L'IA può aiutarvi a scrivere codice C **sicuro** e **corretto**, ma solo se sapete:
1. Come **formulare richieste precise**
2. Come **riconoscere codice pericoloso**
3. Come **validare l'output**

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo (6 ore) sarai in grado di:

✅ **Scrivere** codice C sicuro con supporto IA
   → Evitare buffer overflow, memory leak, undefined behavior

✅ **Identificare** errori tipici del codice generato
   → Riconoscere funzioni non-standard, gestione errata puntatori

✅ **Gestire** correttamente memoria dinamica
   → malloc/free senza leak, validazione puntatori

✅ **Implementare** strutture dati robuste
   → Liste, stack, code con gestione errori completa

✅ **Debuggare** efficacemente con tool professionali
   → GDB, Valgrind, static analyzers

✅ **Testare** sistematicamente il codice
   → Unit test, edge cases, boundary conditions

✅ **Applicare** best practices professionali
   → Naming, documentazione, error handling patterns

### 1.3 Prerequisiti

**Conoscenze Richieste:**
- Modulo 1 (Fondamenti IA e Prompt Engineering)
- Modulo 2 (Prompt Engineering Avanzato)
- Conoscenze base programmazione (qualsiasi linguaggio)

**Software Necessario:**
- GCC compiler (MinGW su Windows, gcc su Linux/Mac)
- Editor/IDE (VSCode raccomandato)
- Git (versioning)
- Valgrind (debugging memoria - Linux/Mac)

**Hardware:**
- PC con almeno 4GB RAM
- Qualsiasi sistema operativo (Windows/Linux/Mac)

### 1.4 Toolchain Professionale

```bash
# COMPILAZIONE CON WARNING COMPLETI
gcc -std=c99 -Wall -Wextra -Wpedantic -Werror mycode.c -o myprogram

# Spiegazione flag:
# -std=c99        : Standard C99 (moderno ma portabile)
# -Wall           : Tutti i warning comuni
# -Wextra         : Warning extra
# -Wpedantic      : Aderenza stretta allo standard
# -Werror         : Tratta warning come errori (no compile se warning)

# STATIC ANALYSIS (trova bug senza eseguire)
cppcheck --enable=all --suppress=missingIncludeSystem mycode.c

# MEMORY CHECK (trova memory leak)
valgrind --leak-check=full --track-origins=yes ./myprogram

# DEBUGGING INTERATTIVO
gcc -g mycode.c -o myprogram   # Compila con simboli debug
gdb ./myprogram                # Avvia debugger
```

---

## 2. Fondamenti del Linguaggio C

### 2.1 Caratteristiche Chiave del C

**1. Gestione Esplicita della Memoria**
```c
// Tu allochi
int *ptr = malloc(100 * sizeof(int));

// Tu controlli
if (ptr == NULL) {
    // Gestisci errore
}

// Tu usi
ptr[0] = 42;

// Tu liberi
free(ptr);
ptr = NULL;  // Buona pratica
```

**2. Puntatori: Potenza e Pericolo**
```c
int x = 42;
int *p = &x;     // p contiene l'indirizzo di x
*p = 100;        // x ora vale 100 (modifica attraverso puntatore)

// PERICOLO: puntatore non inizializzato
int *bad;        // ❌ Punta a memoria casuale!
*bad = 10;       // ❌ CRASH o corruzione dati

// CORRETTO:
int *good = NULL;  // ✅ Inizializzato a NULL
if (good != NULL) {
    *good = 10;
}
```

**3. Array e Puntatori sono Intercambiabili**
```c
int arr[5] = {1, 2, 3, 4, 5};

// Tutti questi sono equivalenti:
arr[2]          // Notazione array
*(arr + 2)      // Aritmetica puntatori
2[arr]          // Valido ma oscuro (non usare!)

// Array "decade" a puntatore
int *p = arr;   // OK: arr diventa puntatore al primo elemento
p[2] = 100;     // Modifica arr[2]
```

**4. Nessun Controllo Bounds (PERICOLO!)**
```c
int arr[5];
arr[10] = 42;   // ❌ COMPILA ma è UNDEFINED BEHAVIOR
                // Può crashare, corrompere dati, sembrare funzionare

// Il compilatore NON ti avvisa!
// DEVI controllare tu i limiti:
int index = 10;
if (index >= 0 && index < 5) {
    arr[index] = 42;  // ✅ Sicuro
}
```

### 2.2 Standard C: C99 vs C11 vs C17

**Per questo corso: raccomandato C99**

| Caratteristica | C89/C90 | C99 | C11 | C17 |
|----------------|---------|-----|-----|-----|
| Dichiarazioni nel for | ❌ | ✅ | ✅ | ✅ |
| Tipo `bool` (stdbool.h) | ❌ | ✅ | ✅ | ✅ |
| Tipo `long long` | ❌ | ✅ | ✅ | ✅ |
| Commenti `//` | ❌ | ✅ | ✅ | ✅ |
| VLA (Variable Length Array) | ❌ | ✅ | Opzionale | Opzionale |
| Threading (threads.h) | ❌ | ❌ | ✅ | ✅ |
| Supporto universale | ✅✅✅ | ✅✅ | ✅ | ✅ |

**C99 - Il Sweet Spot:**
- Moderno ma ampiamente supportato
- Tutte le features utili
- Supporto universale su embedded
- Standard più usato nell'industria

```c
// C89 (vecchio)
void func_old(void) {
    int i;
    for (i = 0; i < 10; i++) {  // Dichiarazione fuori dal for
        /* Commenti multilinea obbligatori */
    }
}

// C99 (raccomandato)
void func_modern(void) {
    for (int i = 0; i < 10; i++) {  // ✅ Dichiarazione nel for
        // Commenti // permessi
    }

    bool flag = true;  // ✅ Tipo bool
    long long big = 10000000000LL;  // ✅ long long
}
```

### 2.3 Tipi di Dati

**Tipi Base:**
```c
// Interi
char c = 'A';           // 1 byte (8 bit)
short s = 100;          // 2 byte (tipicamente)
int i = 1000;           // 4 byte (tipicamente su 32/64-bit)
long l = 100000L;       // 4 o 8 byte (dipende da piattaforma)
long long ll = 10000000000LL;  // Almeno 8 byte

// Unsigned (solo positivi)
unsigned int u = 4000000000U;  // Doppia capacità positiva

// Floating point
float f = 3.14f;        // 4 byte, precisione ~7 cifre
double d = 3.14159265;  // 8 byte, precisione ~15 cifre

// Tipo bool (C99+)
#include <stdbool.h>
bool flag = true;       // true o false
```

**Tipi a Dimensione Fissa (stdint.h - C99+):**
```c
#include <stdint.h>

int8_t    i8  = -128;          // Esattamente 8-bit signed
uint8_t   u8  = 255;           // Esattamente 8-bit unsigned
int16_t   i16 = -32768;        // Esattamente 16-bit signed
uint16_t  u16 = 65535;         // Esattamente 16-bit unsigned
int32_t   i32 = -2147483648;   // Esattamente 32-bit signed
uint32_t  u32 = 4294967295U;   // Esattamente 32-bit unsigned
int64_t   i64 = -9223372036854775807LL;  // Esattamente 64-bit signed
uint64_t  u64 = 18446744073709551615ULL; // Esattamente 64-bit unsigned

// RACCOMANDATO per embedded e portabilità!
```

### 2.4 Header Files Essenziali

```c
#include <stdio.h>     // I/O: printf, scanf, fopen, fclose
                       // printf, fprintf, sprintf, snprintf
                       // scanf, fscanf, sscanf
                       // fgets, fputs, fread, fwrite

#include <stdlib.h>    // Memoria: malloc, calloc, realloc, free
                       // Conversioni: atoi, atof, strtol
                       // Random: rand, srand
                       // Altro: exit, system, qsort

#include <string.h>    // Stringhe: strlen, strcpy, strncpy, strcmp
                       // strcat, strncat, strchr, strstr
                       // memcpy, memmove, memset, memcmp

#include <stdbool.h>   // Tipo bool, true, false (C99+)

#include <stdint.h>    // Tipi size fissa: int8_t, uint32_t, etc.

#include <assert.h>    // Testing: assert(condition)

#include <errno.h>     // Codici errore: errno, EINVAL, ENOMEM

#include <math.h>      // Matematica: sqrt, pow, sin, cos
                       // NOTA: richiede -lm al linking su Linux
```

---

## 3. Setup Ambiente di Sviluppo

### 3.1 Installazione Compilatore

**Windows:**
```bash
# Opzione 1: MinGW-w64 (raccomandato)
1. Download: https://www.mingw-w64.org/
2. Installer con MSYS2: https://www.msys2.org/
3. Installare pacchetto gcc:
   pacman -S mingw-w64-x86_64-gcc

# Opzione 2: TDM-GCC
Download: https://jmeubank.github.io/tdm-gcc/

# Verifica installazione:
gcc --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install build-essential
gcc --version
```

**macOS:**
```bash
# Opzione 1: Xcode Command Line Tools
xcode-select --install

# Opzione 2: Homebrew + gcc
brew install gcc
```

### 3.2 IDE/Editor Raccomandati

**VSCode (Raccomandato)**
```
1. Download: https://code.visualstudio.com/
2. Estensioni da installare:
   - C/C++ (Microsoft)
   - C/C++ Extension Pack
   - Better C++ Syntax
   - Code Runner

3. Configurazione: settings.json
{
  "C_Cpp.default.cStandard": "c99",
  "C_Cpp.default.compilerPath": "/usr/bin/gcc",
  "code-runner.executorMap": {
    "c": "cd $dir && gcc -std=c99 -Wall -Wextra $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
  }
}
```

**Alternative:**
- CLion (JetBrains) - Eccellente ma a pagamento
- Code::Blocks - Gratis, semplice
- Vim/Emacs - Per puristi

### 3.3 Primo Programma con IA

**Prompt per IA:**
```
Scrivi in C99 un programma "Hello World" che:
1. Stampa "Hello, World!" seguito da una nuova riga
2. Include commenti che spiegano ogni parte
3. Usa convenzioni di codice professionali
4. Ritorna 0 per indicare successo
```

**Output IA (validato):**
```c
/**
 * @file hello.c
 * @brief Programma Hello World di esempio
 * @author Corso ITS 2025
 * @date 2025-01-XX
 */

#include <stdio.h>  // Include libreria standard I/O per printf

/**
 * @brief Funzione principale del programma
 *
 * @return 0 se esecuzione corretta
 */
int main(void) {
    // Stampa messaggio su standard output
    printf("Hello, World!\n");

    // Ritorna 0 per indicare successo (convenzione UNIX)
    return 0;
}
```

**Compilazione e Esecuzione:**
```bash
# Compila
gcc -std=c99 -Wall hello.c -o hello

# Esegui
./hello              # Linux/Mac
hello.exe            # Windows

# Output:
Hello, World!
```

### 3.4 Workflow Tipico

```
1. SCRIVI codice (con supporto IA)
2. COMPILA con warning abilitati
3. CORREGGI warning/errori
4. TESTA funzionalità
5. DEBUG se necessario
6. VALIDA con tool (valgrind, cppcheck)
7. DOCUMENTA
8. COMMIT (git)
```

---

## 4. Problemi Ricorrenti del Codice Generato

### 4.1 Funzioni Non Standard

**PROBLEMA COMUNE:** L'IA spesso suggerisce funzioni che NON esistono nello standard C!

**Esempio 1: strdup()**
```c
// ❌ IA potrebbe generare:
char *copy = strdup(original);
// PROBLEMA: strdup() è POSIX, NON C standard!
// Non compila su tutti i sistemi.

// ✅ Versione standard C99:
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

**Esempio 2: strlcpy/strlcat (BSD)**
```c
// ❌ IA potrebbe suggerire:
strlcpy(dest, src, sizeof(dest));  // BSD, non standard C!

// ✅ Alternativa standard C:
void safe_strcpy(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // Garantisci null-terminator
}
```

**Esempio 3: getline() (POSIX)**
```c
// ❌ IA potrebbe usare:
getline(&line, &len, stdin);  // POSIX, non C standard

// ✅ Alternativa standard C:
char *read_line(FILE *fp, size_t *length) {
    char buffer[1024];
    if (fgets(buffer, sizeof(buffer), fp) == NULL) {
        return NULL;
    }

    size_t len = strlen(buffer);
    if (len > 0 && buffer[len-1] == '\n') {
        buffer[len-1] = '\0';
        len--;
    }

    if (length != NULL) {
        *length = len;
    }

    return strdup(buffer);  // OK se implementi my_strdup
}
```

**SOLUZIONE: Prompt Preciso**
```
"Scrivi in STANDARD C99 puro.
NON usare:
- Estensioni POSIX (strdup, getline, etc)
- Estensioni GNU (asprintf, etc)
- Estensioni specifiche compilatore

Usa SOLO funzioni definite in:
- stdio.h (standard)
- stdlib.h (standard)
- string.h (standard)
- stdbool.h (C99)"
```

### 4.2 Buffer Overflow

**PROBLEMA:** Scrittura oltre i limiti del buffer → vulnerabilità #1

**Esempio 1: strcpy() - PERICOLOSO**
```c
// ❌ PERICOLOSO:
void copy_string(char *dest, const char *src) {
    strcpy(dest, src);  // BUFFER OVERFLOW se src > dest!
}

char buffer[10];
copy_string(buffer, "Questa stringa è troppo lunga!");  // OVERFLOW!

// ✅ VERSIONE SICURA:
void copy_string_safe(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // FONDAMENTALE!
}

char buffer[10];
copy_string_safe(buffer, "Testo lungo", sizeof(buffer));
// buffer = "Testo lun\0" (troncato ma sicuro)
```

**Esempio 2: gets() - MAI USARE**
```c
// ❌ VIETATO (rimosso in C11):
char buffer[100];
gets(buffer);  // VULNERABILITÀ CRITICA! Nessun limite!

// ✅ USA fgets():
char buffer[100];
if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
    // Rimuovi newline se presente
    size_t len = strlen(buffer);
    if (len > 0 && buffer[len-1] == '\n') {
        buffer[len-1] = '\0';
    }
}
```

**Esempio 3: sprintf() vs snprintf()**
```c
// ❌ PERICOLOSO:
char buffer[50];
sprintf(buffer, "Name: %s, Age: %d", long_name, age);  // Overflow?

// ✅ SICURO:
char buffer[50];
snprintf(buffer, sizeof(buffer), "Name: %s, Age: %d", long_name, age);
// Garantito non overflow
```

**Pattern Sicuro Universale:**
```c
// ✅ SEMPRE:
// 1. Passa dimensione buffer
// 2. Usa funzioni "n" (strncpy, snprintf)
// 3. Termina esplicitamente con '\0'
// 4. Controlla dimensioni

void safe_operation(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    size_t src_len = strlen(src);
    size_t copy_len = (src_len < dest_size - 1) ? src_len : dest_size - 1;

    memcpy(dest, src, copy_len);
    dest[copy_len] = '\0';
}
```

### 4.3 Memory Leak

**PROBLEMA:** Memoria allocata ma mai liberata → esaurimento risorse

**Esempio 1: Leak Semplice**
```c
// ❌ IA potrebbe dimenticare free():
void process_data(int n) {
    int *data = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        data[i] = i * 2;
    }

    printf("Elaborazione completata\n");
    // ❌ LEAK: manca free(data)!
}

// Chiamato 1000 volte → 1000 leak!

// ✅ CORRETTO:
void process_data_safe(int n) {
    int *data = malloc(n * sizeof(int));

    if (data == NULL) {
        fprintf(stderr, "Errore allocazione\n");
        return;
    }

    for (int i = 0; i < n; i++) {
        data[i] = i * 2;
    }

    printf("Elaborazione completata\n");

    free(data);      // ✅ Libera memoria
    data = NULL;     // Buona pratica: evita dangling pointer
}
```

**Esempio 2: Leak su Early Return**
```c
// ❌ LEAK su percorso errore:
int process_file(const char *filename) {
    FILE *fp = fopen(filename, "r");
    int *buffer = malloc(1000 * sizeof(int));

    if (fp == NULL) {
        return -1;  // ❌ LEAK: buffer non liberato!
    }

    // ... elaborazione ...

    fclose(fp);
    free(buffer);
    return 0;
}

// ✅ CORRETTO: goto cleanup pattern
int process_file_safe(const char *filename) {
    FILE *fp = NULL;
    int *buffer = NULL;
    int result = -1;

    buffer = malloc(1000 * sizeof(int));
    if (buffer == NULL) {
        goto cleanup;
    }

    fp = fopen(filename, "r");
    if (fp == NULL) {
        goto cleanup;
    }

    // ... elaborazione ...
    result = 0;

cleanup:
    if (fp != NULL) fclose(fp);
    if (buffer != NULL) free(buffer);
    return result;
}
```

**Esempio 3: Leak in Strutture**
```c
// ❌ LEAK in struct con membri dinamici:
typedef struct {
    char *name;
    int *grades;
    int num_grades;
} Student;

void destroy_student_WRONG(Student *s) {
    free(s);  // ❌ LEAK: name e grades non liberati!
}

// ✅ CORRETTO:
void destroy_student(Student *s) {
    if (s == NULL) return;

    free(s->name);     // Libera stringa nome
    free(s->grades);   // Libera array voti
    free(s);           // Libera struct
}
```

**Detection con Valgrind:**
```bash
# Compila con -g per simboli debug
gcc -g -std=c99 myprogram.c -o myprogram

# Esegui con valgrind
valgrind --leak-check=full --show-leak-kinds=all ./myprogram

# Output esempio:
==12345== LEAK SUMMARY:
==12345==    definitely lost: 1,000 bytes in 1 blocks
==12345==    indirectly lost: 0 bytes in 0 blocks
==12345==      possibly lost: 0 bytes in 0 blocks
==12345==    still reachable: 0 bytes in 0 blocks
==12345==         suppressed: 0 bytes in 0 blocks
```

### 4.4 Dereferenziazione NULL

**PROBLEMA:** Accesso a memoria attraverso puntatore NULL → crash

```c
// ❌ IA potrebbe NON controllare:
void process_array(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;  // CRASH se arr == NULL!
    }
}

// ✅ PATTERN DIFENSIVO:
bool process_array_safe(int *arr, int n) {
    // Controllo parametri
    if (arr == NULL) {
        return false;
    }

    if (n <= 0) {
        return true;  // Niente da fare, ma non errore
    }

    // Elaborazione sicura
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
    }

    return true;
}

// Uso:
int data[10];
if (!process_array_safe(data, 10)) {
    fprintf(stderr, "Errore elaborazione\n");
}
```

**Pattern Validazione Parametri:**
```c
// ✅ TEMPLATE per funzioni robuste:
ReturnType function_name(Type *ptr, int size, ...) {
    // 1. Validazione puntatori
    if (ptr == NULL) {
        return ERROR_VALUE;  // o false, NULL, -1, etc.
    }

    // 2. Validazione dimensioni/range
    if (size <= 0 || size > MAX_SIZE) {
        return ERROR_VALUE;
    }

    // 3. Logica funzione
    // ...

    return SUCCESS_VALUE;
}
```

### 4.5 Off-by-One Errors

**PROBLEMA:** Errori di +1/-1 nei limiti → buffer overflow

```c
// ❌ ERRORE CLASSICO:
void copy_bad(char *dest, const char *src, int dest_size) {
    for (int i = 0; i <= dest_size; i++) {  // ❌ <= invece di <
        dest[i] = src[i];
    }
}
// Se dest_size = 10, accede a dest[10] → overflow!

// ✅ CORRETTO:
void copy_good(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    size_t i;
    for (i = 0; i < dest_size - 1 && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';  // Terminator nell'ultima posizione valida
}
```

**Checklist Off-by-One:**
```c
// ❌ ERRORI COMUNI:
for (i = 0; i <= n; i++)        // ❌ Dovrebbe essere i < n
arr[n] = value;                 // ❌ Ultimo indice valido è n-1
malloc(strlen(str));            // ❌ Manca spazio per '\0'
strncpy(dest, src, sizeof(dest));  // ❌ Potrebbe non terminare con '\0'

// ✅ CORRETTO:
for (i = 0; i < n; i++)         // ✅ Range corretto
arr[n-1] = value;               // ✅ Ultimo elemento
malloc(strlen(str) + 1);        // ✅ Spazio per '\0'
strncpy(dest, src, sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';  // ✅ Garantisci terminatore
```

### 4.6 Prompt per Codice Sicuro

**Template Prompt Anti-Errori:**
```
Scrivi in standard C99 una funzione [DESCRIZIONE].

REQUISITI SICUREZZA (OBBLIGATORI):
1. Valida TUTTI i puntatori (NULL check)
2. Valida dimensioni/range parametri
3. USA funzioni sicure (strncpy, snprintf, NON strcpy/sprintf)
4. Previeni buffer overflow
5. Gestisci correttamente memoria (free tutto ciò che malloc)
6. Evita off-by-one errors
7. Ritorna codice errore se fallisce
8. Aggiungi assert() per debug

VIETATO USARE:
- strcpy, strcat, sprintf, gets
- strdup, getline (non C99 standard)
- Array Variable Length (VLA) di grandi dimensioni

RICHIESTO:
- Commenti che spiegano logica
- Gestione errori esplicita
- Esempio di uso
```

---

## 5. Gestione della Memoria

### 5.1 Stack vs Heap

**Stack (Automatica):**
```c
void function() {
    int x = 10;           // Stack: allocata automaticamente
    char buffer[100];     // Stack: allocata automaticamente

    // Vantaggi: veloce, automatica, nessun leak possibile
    // Svantaggi: dimensione limitata (~1-8MB), scope locale

}  // x e buffer distrutti automaticamente qui
```

**Heap (Dinamica):**
```c
void function() {
    int *x = malloc(sizeof(int));           // Heap: manuale
    char *buffer = malloc(100);             // Heap: manuale

    *x = 10;
    buffer[0] = 'A';

    // Vantaggi: dimensione grande, scope controllato
    // Svantaggi: lenta, manuale, possibile leak

    free(x);
    free(buffer);
}  // DEVI liberare manualmente!
```

**Quando Usare Cosa:**
```c
// ✅ USA STACK quando:
// - Dimensione piccola e nota a compile-time
// - Scope limitato alla funzione
int small_array[10];
char name[50];

// ✅ USA HEAP quando:
// - Dimensione grande o sconosciuta a compile-time
// - Dati devono sopravvivere alla funzione
// - Strutture dati dinamiche (liste, alberi)
int *large_array = malloc(1000000 * sizeof(int));
```

### 5.2 Funzioni di Allocazione

**malloc() - Alloca Memoria**
```c
void *malloc(size_t size);

// Uso corretto:
int *arr = malloc(10 * sizeof(int));  // Alloca spazio per 10 int
if (arr == NULL) {
    // Gestisci errore allocazione
    fprintf(stderr, "Out of memory!\n");
    return -1;
}

// Usa arr...
arr[0] = 42;

free(arr);  // Libera quando fatto
arr = NULL; // Buona pratica
```

**calloc() - Alloca e Azzera**
```c
void *calloc(size_t num, size_t size);

// Differenza da malloc: inizializza a zero
int *arr1 = malloc(10 * sizeof(int));   // Valori casuali
int *arr2 = calloc(10, sizeof(int));    // Tutti zero

// calloc equivale a:
int *arr = malloc(10 * sizeof(int));
if (arr != NULL) {
    memset(arr, 0, 10 * sizeof(int));
}
```

**realloc() - Ridimensiona**
```c
void *realloc(void *ptr, size_t new_size);

// Esempio: array dinamico che cresce
int *arr = malloc(10 * sizeof(int));
int capacity = 10;
int count = 0;

// Aggiungi elemento
if (count >= capacity) {
    capacity *= 2;  // Raddoppia capacità

    int *temp = realloc(arr, capacity * sizeof(int));
    if (temp == NULL) {
        // Errore: arr ancora valido, non modificato
        free(arr);
        return -1;
    }
    arr = temp;  // Aggiorna puntatore
}
arr[count++] = new_value;
```

**free() - Libera Memoria**
```c
void free(void *ptr);

// Regole:
// 1. Libera SOLO memoria da malloc/calloc/realloc
// 2. NON liberare due volte (double-free)
// 3. NON usare dopo free (use-after-free)
// 4. OK liberare NULL (no-op)

int *ptr = malloc(100);
free(ptr);        // ✅ OK
ptr = NULL;       // ✅ Buona pratica

free(ptr);        // ✅ OK (NULL è no-op)
// free(ptr);     // ❌ Double free se non NULL!

// Non fare:
// int *p = malloc(100);
// free(p);
// *p = 10;       // ❌ Use-after-free!
```

### 5.3 Pattern Allocazione Sicura

**Pattern 1: Allocazione con Controllo**
```c
// ✅ TEMPLATE BASE:
Type *allocate_type(size_t count) {
    if (count == 0 || count > MAX_REASONABLE_SIZE) {
        return NULL;
    }

    Type *ptr = malloc(count * sizeof(Type));
    if (ptr == NULL) {
        fprintf(stderr, "Allocation failed for %zu elements\n", count);
        return NULL;
    }

    return ptr;
}

// Uso:
int *arr = allocate_type(100);
if (arr == NULL) {
    // Gestisci errore
    return -1;
}
```

**Pattern 2: Allocazione + Inizializzazione**
```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} DynamicArray;

DynamicArray *create_array(size_t initial_capacity) {
    if (initial_capacity == 0) {
        initial_capacity = 10;  // Default
    }

    DynamicArray *arr = malloc(sizeof(DynamicArray));
    if (arr == NULL) {
        return NULL;
    }

    arr->data = malloc(initial_capacity * sizeof(int));
    if (arr->data == NULL) {
        free(arr);  // ✅ Cleanup parziale
        return NULL;
    }

    arr->size = 0;
    arr->capacity = initial_capacity;

    return arr;
}

void destroy_array(DynamicArray *arr) {
    if (arr == NULL) return;

    free(arr->data);  // Libera membri prima
    free(arr);        // Poi libera struct
}
```

**Pattern 3: Realloc Sicuro**
```c
// ❌ ERRORE COMUNE:
arr = realloc(arr, new_size);  // LEAK se realloc fallisce!

// ✅ CORRETTO:
void *temp = realloc(arr, new_size);
if (temp == NULL) {
    // arr ancora valido!
    free(arr);
    return -1;
}
arr = temp;  // Aggiorna solo se successo
```

### 5.4 Debugging Memoria con Valgrind

**Setup:**
```bash
# Installa Valgrind (Linux/Mac)
sudo apt install valgrind  # Ubuntu/Debian
brew install valgrind      # macOS (può richiedere workaround)

# Compila con simboli debug
gcc -g -std=c99 -Wall myprogram.c -o myprogram

# Esegui con Valgrind
valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./myprogram
```

**Esempio Output:**
```
==12345== Invalid write of size 4
==12345==    at 0x4005F6: main (test.c:10)
==12345==  Address 0x5201068 is 0 bytes after a block of size 40 alloc'd
==12345==    at 0x4C2BBAF: malloc (vg_replace_malloc.c:299)
==12345==    by 0x4005E2: main (test.c:8)

Significa: scritto oltre fine buffer allocato (buffer overflow)

==12345== LEAK SUMMARY:
==12345==    definitely lost: 100 bytes in 1 blocks
==12345==    indirectly lost: 0 bytes in 0 blocks

Significa: 100 byte non liberati (memory leak)
```

**Codice Esempio per Testing:**
```c
#include <stdlib.h>

int main(void) {
    // Test 1: Leak
    int *leak = malloc(100 * sizeof(int));
    // ❌ Nessun free → leak

    // Test 2: Invalid write
    int *arr = malloc(10 * sizeof(int));
    arr[10] = 42;  // ❌ Buffer overflow
    free(arr);

    // Test 3: Use after free
    int *ptr = malloc(sizeof(int));
    free(ptr);
    *ptr = 10;  // ❌ Use after free

    return 0;
}
```

### 5.5 Esercizi Memoria

**Esercizio 1: Fix Memory Leak**
```c
// ❌ Trova e correggi il leak:
char *concatenate(const char *s1, const char *s2) {
    size_t len1 = strlen(s1);
    size_t len2 = strlen(s2);

    char *result = malloc(len1 + len2 + 1);
    strcpy(result, s1);
    strcat(result, s2);

    return result;
}

int main(void) {
    for (int i = 0; i < 1000; i++) {
        concatenate("Hello", " World");  // ❌ LEAK!
    }
    return 0;
}

// ✅ Soluzione:
int main(void) {
    for (int i = 0; i < 1000; i++) {
        char *str = concatenate("Hello", " World");
        if (str != NULL) {
            printf("%s\n", str);
            free(str);  // ✅ Libera
        }
    }
    return 0;
}
```

**Esercizio 2: Implementa Array Dinamico**
```c
// Implementa queste funzioni:
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntArray;

IntArray *array_create(size_t initial_capacity);
bool array_push(IntArray *arr, int value);
bool array_pop(IntArray *arr, int *value);
int array_get(IntArray *arr, size_t index);
void array_destroy(IntArray *arr);

// Requisiti:
// - Nessun memory leak
// - Gestione errori completa
// - Crescita automatica quando pieno
```

---

## 6. Puntatori e Array

### 6.1 Puntatori Base

**Concetto:**
Un puntatore è una variabile che contiene un **indirizzo di memoria**.

```c
int x = 42;       // Variabile normale
int *p;           // Puntatore a int (non inizializzato!)

p = &x;           // p ora contiene l'indirizzo di x
printf("%p\n", (void*)p);  // Stampa indirizzo (es: 0x7ffd5c4)

*p = 100;         // Modifica il valore puntato (x diventa 100)
printf("%d\n", x);         // Stampa: 100
```

**Operatori:**
```c
int x = 42;
int *p = &x;

&x    // Operatore "address-of": restituisce indirizzo di x
*p    // Operatore "dereference": accede al valore puntato
p     // Il puntatore stesso (l'indirizzo)

// Esempio:
printf("Indirizzo di x: %p\n", (void*)&x);
printf("Valore di p: %p\n", (void*)p);     // Stesso indirizzo
printf("Valore puntato da p: %d\n", *p);   // 42
```

**Tipi di Puntatori:**
```c
int *pi;         // Puntatore a int
char *pc;        // Puntatore a char
double *pd;      // Puntatore a double
void *pv;        // Puntatore generico (può puntare a qualsiasi tipo)

// void* richiede cast per dereference:
int x = 10;
void *pv = &x;
// *pv = 20;           // ❌ Errore: non puoi dereferenziare void*
int *pi = (int*)pv;    // Cast necessario
*pi = 20;              // ✅ OK
```

### 6.2 Aritmetica dei Puntatori

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;  // p punta al primo elemento

// Incremento puntatore:
printf("%d\n", *p);        // 10
p++;                       // p punta al secondo elemento
printf("%d\n", *p);        // 20

// p++ NON aggiunge 1 all'indirizzo, ma sizeof(int)!
// Se int è 4 byte e p era 0x1000, dopo p++ diventa 0x1004

// Accesso tramite offset:
p = arr;
printf("%d\n", *(p + 2));  // 30 (equivale a arr[2])

// Array notation è zucchero sintattico:
arr[i]  ≡  *(arr + i)  ≡  *(i + arr)  ≡  i[arr]
// Ultimo è valido ma oscuro!
```

**Esempi Pratici:**
```c
int arr[] = {1, 2, 3, 4, 5};
int *p = arr;

// Iterazione con puntatori:
for (int *p = arr; p < arr + 5; p++) {
    printf("%d ", *p);
}
// Output: 1 2 3 4 5

// Differenza tra puntatori (elementi di distanza):
int *start = &arr[0];
int *end = &arr[4];
ptrdiff_t distance = end - start;  // 4
```

### 6.3 Array e Puntatori

**Array Decay:**
```c
int arr[10];

// Nella maggior parte dei contesti, arr "decade" a puntatore:
int *p = arr;      // ✅ OK: arr diventa &arr[0]

// MA non sono identici:
sizeof(arr)        // 40 (10 * sizeof(int) = 10 * 4)
sizeof(p)          // 8 (dimensione puntatore su 64-bit)

// & comportamento diverso:
int (*pa)[10] = &arr;  // Puntatore all'intero array
int *p = arr;          // Puntatore al primo elemento
```

**Passaggio Array a Funzioni:**
```c
// Questi sono EQUIVALENTI:
void func(int arr[]);
void func(int arr[10]);  // 10 ignorato!
void func(int *arr);

// Array SEMPRE passato come puntatore!
// Dimensione NON trasmessa automaticamente:
void print_array(int arr[], int size) {  // Serve size!
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

int main(void) {
    int data[5] = {1, 2, 3, 4, 5};
    print_array(data, 5);  // DEVI passare dimensione
}
```

**Array Multidimensionali:**
```c
// Array 2D statico:
int matrix[3][4] = {
    {1, 2, 3, 4},
    {5, 6, 7, 8},
    {9, 10, 11, 12}
};

// Accesso:
matrix[1][2]  // 7

// In memoria: layout contiguo row-major:
// [1][2][3][4][5][6][7][8][9][10][11][12]

// Passaggio a funzione:
void process(int matrix[][4], int rows) {  // DEVI specificare colonne!
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", matrix[i][j]);
        }
    }
}

// Array 2D dinamico:
int rows = 3, cols = 4;

// Metodo 1: Array di puntatori (non contiguo)
int **matrix = malloc(rows * sizeof(int*));
for (int i = 0; i < rows; i++) {
    matrix[i] = malloc(cols * sizeof(int));
}

// Uso:
matrix[1][2] = 7;

// Deallocazione:
for (int i = 0; i < rows; i++) {
    free(matrix[i]);
}
free(matrix);

// Metodo 2: Singola allocazione contigua (preferito)
int *matrix = malloc(rows * cols * sizeof(int));

// Macro accesso:
#define MATRIX(i, j) matrix[(i) * cols + (j)]

// Uso:
MATRIX(1, 2) = 7;  // Equivale a matrix[1*4 + 2]

// Deallocazione:
free(matrix);  // Singola free!
```

### 6.4 Puntatori a Funzioni

```c
// Dichiarazione:
int (*func_ptr)(int, int);

// Definizione funzione:
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

// Assegnazione:
func_ptr = add;  // o &add (equivalente)

// Chiamata:
int result = func_ptr(5, 3);  // 8
// o:
int result = (*func_ptr)(5, 3);  // Equivalente

// Uso: tabella di funzioni
int (*operations[4])(int, int) = {add, subtract, multiply, divide};

int op = 0;  // Scegli operazione
int result = operations[op](10, 5);  // Chiama add(10, 5)
```

**Typedef per Leggibilità:**
```c
// Senza typedef (oscuro):
int (*func_ptr)(int, int);

// Con typedef (chiaro):
typedef int (*BinaryOp)(int, int);

BinaryOp func_ptr;  // Molto più leggibile!
func_ptr = add;
```

### 6.5 Puntatori Pericolosi

**Dangling Pointer:**
```c
// ❌ Puntatore a stack locale (distrutto)
int *dangerous_function(void) {
    int x = 42;
    return &x;  // ❌ x distrutto quando funzione finisce!
}

int main(void) {
    int *p = dangerous_function();
    printf("%d\n", *p);  // ❌ UNDEFINED BEHAVIOR
}

// ✅ Soluzioni:
// 1. Usa heap:
int *safe_function(void) {
    int *x = malloc(sizeof(int));
    *x = 42;
    return x;  // ✅ heap sopravvive
}

// 2. Usa parametro out:
void safe_function2(int *out) {
    *out = 42;  // ✅ caller fornisce storage
}

int main(void) {
    int value;
    safe_function2(&value);
    printf("%d\n", value);  // ✅ OK
}
```

**Wild Pointer:**
```c
// ❌ Puntatore non inizializzato
int *p;       // Contiene valore casuale!
*p = 10;      // ❌ CRASH (o peggio: corrompe memoria)

// ✅ Sempre inizializza:
int *p = NULL;
if (p != NULL) {
    *p = 10;
}
```

**Use After Free:**
```c
// ❌ Uso dopo free
int *p = malloc(sizeof(int));
*p = 42;
free(p);
printf("%d\n", *p);  // ❌ UNDEFINED BEHAVIOR

// ✅ Metti NULL dopo free:
int *p = malloc(sizeof(int));
*p = 42;
free(p);
p = NULL;  // ✅ Previene uso accidentale
```

### 6.6 Const con Puntatori

```c
int x = 10, y = 20;

// Puntatore a const int: NON puoi modificare il valore puntato
const int *p1 = &x;
*p1 = 30;    // ❌ Errore: valore è const
p1 = &y;     // ✅ OK: puntatore non è const

// Puntatore const: NON puoi modificare il puntatore
int * const p2 = &x;
*p2 = 30;    // ✅ OK: valore non è const
p2 = &y;     // ❌ Errore: puntatore è const

// Puntatore const a const int: NON puoi modificare nulla
const int * const p3 = &x;
*p3 = 30;    // ❌ Errore: valore è const
p3 = &y;     // ❌ Errore: puntatore è const

// Regola: leggi da destra a sinistra
// const int *p     → p è puntatore a int che è const
// int * const p    → p è puntatore const a int
// const int * const p → p è puntatore const a int che è const
```

**Uso Pratico:**
```c
// Funzione che NON modifica array:
int sum(const int *arr, int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
        // arr[i] = 0;  // ❌ Errore: arr è const
    }
    return total;
}

// const garantisce al caller che array non sarà modificato
```

---

## 7. Stringhe in C

### 7.1 Fondamenti Stringhe

**Definizione:**
In C, una stringa è un **array di char terminato da '\0'**.

```c
// Queste sono EQUIVALENTI:
char str1[] = "Hello";
char str2[] = {'H', 'e', 'l', 'l', 'o', '\0'};

// In memoria:
// [H][e][l][l][o][\0]
//  0  1  2  3  4  5

sizeof(str1)  // 6 (5 caratteri + '\0')
strlen(str1)  // 5 (NON conta '\0')
```

**String Literal:**
```c
char *str = "Hello";  // String literal (in read-only memory!)

str[0] = 'h';  // ❌ UNDEFINED BEHAVIOR (modifica read-only memory)

// ✅ Se devi modificare, usa array:
char str[] = "Hello";  // Copia in array modificabile
str[0] = 'h';          // ✅ OK
```

**Carattere Terminatore OBBLIGATORIO:**
```c
// ❌ ERRORE: nessun terminatore
char bad[5] = {'H', 'e', 'l', 'l', 'o'};
printf("%s\n", bad);  // ❌ UNDEFINED BEHAVIOR (legge oltre array)

// ✅ CORRETTO:
char good[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
printf("%s\n", good);  // ✅ OK
```

### 7.2 Funzioni Stringa Standard

```c
#include <string.h>

// LUNGHEZZA
size_t strlen(const char *s);
// Ritorna numero caratteri SENZA contare '\0'
strlen("Hello")  // 5

// COPIA (PERICOLOSO!)
char *strcpy(char *dest, const char *src);
// ❌ PROBLEMA: nessun controllo dimensione dest

// COPIA SICURA
char *strncpy(char *dest, const char *src, size_t n);
char dest[10];
strncpy(dest, "Hello World", sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';  // ⚠️ strncpy NON garantisce '\0'!

// CONFRONTO
int strcmp(const char *s1, const char *s2);
// Ritorna: 0 se uguali, <0 se s1<s2, >0 se s1>s2
if (strcmp(str1, str2) == 0) {
    printf("Uguali\n");
}

// CONCATENA (PERICOLOSO!)
char *strcat(char *dest, const char *src);

// CERCA CARATTERE
char *strchr(const char *s, int c);
char *p = strchr("Hello", 'l');  // Punta a prima 'l'

// CERCA SOTTOSTRINGA
char *strstr(const char *haystack, const char *needle);
char *p = strstr("Hello World", "World");  // Punta a "World"
```

### 7.3 Funzioni Stringa Sicure

**Problema funzioni standard:**
```c
// ❌ strcpy: buffer overflow
char dest[5];
strcpy(dest, "Hello World");  // OVERFLOW!

// ❌ strcat: buffer overflow
char dest[10] = "Hello";
strcat(dest, " World");  // OVERFLOW!
```

**Soluzioni:**

**1. strncpy (con attenzione):**
```c
void safe_strcpy(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }

    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // FONDAMENTALE!
}

// ⚠️ strncpy NON garantisce '\0' se src >= n caratteri!
```

**2. snprintf (RACCOMANDATO):**
```c
char dest[50];
snprintf(dest, sizeof(dest), "%s", "Hello World");
// ✅ Garantisce '\0'
// ✅ Mai overflow
// ✅ Supporta formatting

// Concatenazione con snprintf:
char dest[50] = "Hello";
size_t len = strlen(dest);
snprintf(dest + len, sizeof(dest) - len, " %s", "World");
```

**3. Funzione Custom Robusta:**
```c
/**
 * @brief Copia stringa in modo sicuro
 *
 * @param dest Buffer destinazione
 * @param src Stringa sorgente
 * @param dest_size Dimensione dest (incluso '\0')
 * @return true se copiato tutto, false se troncato
 */
bool safe_string_copy(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return false;
    }

    size_t src_len = strlen(src);
    size_t copy_len = (src_len < dest_size - 1) ? src_len : dest_size - 1;

    memcpy(dest, src, copy_len);
    dest[copy_len] = '\0';

    return (src_len < dest_size);  // true se non troncato
}
```

### 7.4 Input Stringhe Sicuro

**❌ MAI usare gets():**
```c
char buffer[100];
gets(buffer);  // ❌ RIMOSSO in C11! Vulnerabilità critica!
```

**✅ Usa fgets():**
```c
char buffer[100];

// Leggi da stdin
if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
    // Rimuovi newline se presente
    size_t len = strlen(buffer);
    if (len > 0 && buffer[len - 1] == '\n') {
        buffer[len - 1] = '\0';
    }

    printf("Input: %s\n", buffer);
}

// fgets include '\n' se c'era spazio
// ✅ Mai overflow
// ✅ Ritorna NULL su errore/EOF
```

**Funzione Helper:**
```c
/**
 * @brief Legge riga da input rimuovendo newline
 */
bool read_line(char *buffer, size_t size) {
    if (buffer == NULL || size == 0) {
        return false;
    }

    if (fgets(buffer, size, stdin) == NULL) {
        return false;  // EOF o errore
    }

    // Rimuovi newline
    size_t len = strlen(buffer);
    if (len > 0 && buffer[len - 1] == '\n') {
        buffer[len - 1] = '\0';
    }

    return true;
}

// Uso:
char name[50];
printf("Nome: ");
if (read_line(name, sizeof(name))) {
    printf("Ciao %s!\n", name);
}
```

### 7.5 Manipolazione Stringhe

**Tokenizzazione (split):**
```c
#include <string.h>

char str[] = "Hello,World,From,C";
char *token = strtok(str, ",");

while (token != NULL) {
    printf("%s\n", token);
    token = strtok(NULL, ",");  // NULL = continua stringa precedente
}

// Output:
// Hello
// World
// From
// C

// ⚠️ strtok MODIFICA la stringa originale (inserisce '\0')!
```

**Versione Sicura (non modifica originale):**
```c
void split_string(const char *str, char delimiter) {
    if (str == NULL) return;

    // Copia stringa (strtok modifica)
    char *copy = strdup(str);  // O implementa my_strdup
    if (copy == NULL) return;

    char delim[2] = {delimiter, '\0'};
    char *token = strtok(copy, delim);

    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, delim);
    }

    free(copy);
}
```

**Conversioni:**
```c
#include <stdlib.h>

// String → Int
const char *str_num = "42";
int num = atoi(str_num);  // 42
// ⚠️ atoi ritorna 0 su errore (ambiguo con "0"!)

// Versione robusta:
char *endptr;
long num = strtol(str_num, &endptr, 10);  // base 10
if (*endptr != '\0') {
    printf("Errore conversione\n");
}

// String → Double
const char *str_double = "3.14";
double d = strtod(str_double, &endptr);

// Int → String
char buffer[50];
int num = 42;
snprintf(buffer, sizeof(buffer), "%d", num);  // "42"
```

### 7.6 Esercizi Stringhe

**Esercizio 1: Implementa strlen**
```c
size_t my_strlen(const char *s) {
    // TODO: implementa senza usare strlen()
    // Conta caratteri fino a '\0'
}
```

**Esercizio 2: Reverse String**
```c
// In-place reverse
void reverse_string(char *s) {
    // TODO: inverti stringa
    // "Hello" → "olleH"
}
```

**Esercizio 3: Substring**
```c
// Estrai sottostringa [start, end)
char *substring(const char *s, size_t start, size_t length) {
    // TODO: alloca e ritorna sottostringa
    // Gestisci errori (NULL, index fuori range)
    // Chiamante deve fare free()
}
```

---

## 8. Strutture Dati

### 8.1 Struct Base

**Definizione:**
```c
// Struct semplice
struct Point {
    int x;
    int y;
};

// Creazione
struct Point p1;
p1.x = 10;
p1.y = 20;

// Inizializzazione
struct Point p2 = {30, 40};

// Accesso membri
printf("(%d, %d)\n", p2.x, p2.y);
```

**Typedef per Convenienza:**
```c
// Senza typedef:
struct Point {
    int x, y;
};
struct Point p;  // "struct" obbligatorio

// Con typedef:
typedef struct {
    int x, y;
} Point;

Point p;  // ✅ Più pulito

// O:
typedef struct Point Point;
struct Point {
    int x, y;
};
Point p;
```

### 8.2 Struct con Allocazione Dinamica

**Esempio: Student**
```c
typedef struct {
    char *name;          // Allocato dinamicamente
    int age;
    float *grades;       // Array dinamico
    int num_grades;
    int grades_capacity;
} Student;

// Costruttore
Student *create_student(const char *name, int age) {
    if (name == NULL || age < 0) {
        return NULL;
    }

    Student *s = malloc(sizeof(Student));
    if (s == NULL) {
        return NULL;
    }

    // Alloca nome
    s->name = malloc(strlen(name) + 1);
    if (s->name == NULL) {
        free(s);
        return NULL;
    }
    strcpy(s->name, name);

    s->age = age;

    // Array voti iniziale
    s->grades_capacity = 10;
    s->grades = malloc(s->grades_capacity * sizeof(float));
    if (s->grades == NULL) {
        free(s->name);
        free(s);
        return NULL;
    }

    s->num_grades = 0;

    return s;
}

// Distruttore
void destroy_student(Student *s) {
    if (s == NULL) return;

    free(s->name);     // Libera membri dinamici prima
    free(s->grades);
    free(s);           // Poi libera struct
}

// Aggiungi voto
bool add_grade(Student *s, float grade) {
    if (s == NULL || grade < 0.0 || grade > 100.0) {
        return false;
    }

    // Espandi array se necessario
    if (s->num_grades >= s->grades_capacity) {
        int new_capacity = s->grades_capacity * 2;
        float *temp = realloc(s->grades, new_capacity * sizeof(float));
        if (temp == NULL) {
            return false;
        }
        s->grades = temp;
        s->grades_capacity = new_capacity;
    }

    s->grades[s->num_grades++] = grade;
    return true;
}

// Calcola media
float calculate_average(const Student *s) {
    if (s == NULL || s->num_grades == 0) {
        return 0.0;
    }

    float sum = 0.0;
    for (int i = 0; i < s->num_grades; i++) {
        sum += s->grades[i];
    }

    return sum / s->num_grades;
}

// Stampa
void print_student(const Student *s) {
    if (s == NULL) return;

    printf("Nome: %s\n", s->name);
    printf("Età: %d\n", s->age);
    printf("Voti: ");
    for (int i = 0; i < s->num_grades; i++) {
        printf("%.1f ", s->grades[i]);
    }
    printf("\nMedia: %.2f\n", calculate_average(s));
}
```

### 8.3 Liste Linkate

**Nodo Lista:**
```c
typedef struct Node {
    int data;
    struct Node *next;  // ⚠️ "struct" necessario qui!
} Node;
```

**Operazioni Base:**
```c
// Crea nodo
Node *create_node(int value) {
    Node *node = malloc(sizeof(Node));
    if (node == NULL) {
        return NULL;
    }

    node->data = value;
    node->next = NULL;

    return node;
}

// Inserimento in testa (O(1))
Node *insert_head(Node *head, int value) {
    Node *new_node = create_node(value);
    if (new_node == NULL) {
        return head;  // Errore: lista non modificata
    }

    new_node->next = head;
    return new_node;  // Nuova testa
}

// Inserimento in coda (O(n))
Node *insert_tail(Node *head, int value) {
    Node *new_node = create_node(value);
    if (new_node == NULL) {
        return head;
    }

    if (head == NULL) {
        return new_node;  // Lista vuota
    }

    // Trova ultimo nodo
    Node *curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }

    curr->next = new_node;
    return head;
}

// Ricerca
Node *search(Node *head, int value) {
    Node *curr = head;
    while (curr != NULL) {
        if (curr->data == value) {
            return curr;  // Trovato
        }
        curr = curr->next;
    }
    return NULL;  // Non trovato
}

// Eliminazione valore
Node *delete_value(Node *head, int value) {
    if (head == NULL) {
        return NULL;
    }

    // Caso speciale: testa
    if (head->data == value) {
        Node *temp = head->next;
        free(head);
        return temp;
    }

    // Cerca nodo precedente
    Node *curr = head;
    while (curr->next != NULL && curr->next->data != value) {
        curr = curr->next;
    }

    if (curr->next != NULL) {
        // Trovato: elimina
        Node *temp = curr->next;
        curr->next = temp->next;
        free(temp);
    }

    return head;
}

// Stampa lista
void print_list(Node *head) {
    Node *curr = head;
    printf("[");
    while (curr != NULL) {
        printf("%d", curr->data);
        if (curr->next != NULL) {
            printf(" -> ");
        }
        curr = curr->next;
    }
    printf("]\n");
}

// Libera lista
void free_list(Node *head) {
    while (head != NULL) {
        Node *temp = head;
        head = head->next;
        free(temp);
    }
}

// Lunghezza
int list_length(Node *head) {
    int count = 0;
    Node *curr = head;
    while (curr != NULL) {
        count++;
        curr = curr->next;
    }
    return count;
}
```

**Uso:**
```c
int main(void) {
    Node *list = NULL;

    // Costruisci lista: 3 -> 2 -> 1
    list = insert_head(list, 1);
    list = insert_head(list, 2);
    list = insert_head(list, 3);

    print_list(list);  // [3 -> 2 -> 1]

    // Aggiungi in coda
    list = insert_tail(list, 4);
    print_list(list);  // [3 -> 2 -> 1 -> 4]

    // Cerca
    if (search(list, 2) != NULL) {
        printf("2 trovato\n");
    }

    // Elimina
    list = delete_value(list, 2);
    print_list(list);  // [3 -> 1 -> 4]

    // Cleanup
    free_list(list);

    return 0;
}
```

### 8.4 Stack (LIFO)

```c
#define STACK_MAX_SIZE 100

typedef struct {
    int data[STACK_MAX_SIZE];
    int top;  // Indice elemento in cima (-1 se vuoto)
} Stack;

// Inizializza
void stack_init(Stack *s) {
    if (s != NULL) {
        s->top = -1;
    }
}

// Push
bool stack_push(Stack *s, int value) {
    if (s == NULL || s->top >= STACK_MAX_SIZE - 1) {
        return false;  // Stack pieno
    }

    s->data[++(s->top)] = value;
    return true;
}

// Pop
bool stack_pop(Stack *s, int *value) {
    if (s == NULL || s->top < 0) {
        return false;  // Stack vuoto
    }

    if (value != NULL) {
        *value = s->data[s->top];
    }
    s->top--;

    return true;
}

// Peek (guarda senza rimuovere)
bool stack_peek(const Stack *s, int *value) {
    if (s == NULL || s->top < 0) {
        return false;
    }

    if (value != NULL) {
        *value = s->data[s->top];
    }

    return true;
}

// Vuoto?
bool stack_is_empty(const Stack *s) {
    return (s == NULL || s->top < 0);
}

// Pieno?
bool stack_is_full(const Stack *s) {
    return (s != NULL && s->top >= STACK_MAX_SIZE - 1);
}
```

### 8.5 Queue (FIFO)

```c
#define QUEUE_MAX_SIZE 100

typedef struct {
    int data[QUEUE_MAX_SIZE];
    int front;  // Indice primo elemento
    int rear;   // Indice ultimo elemento
    int count;  // Numero elementi
} Queue;

// Inizializza
void queue_init(Queue *q) {
    if (q != NULL) {
        q->front = 0;
        q->rear = -1;
        q->count = 0;
    }
}

// Enqueue (inserisci in coda)
bool queue_enqueue(Queue *q, int value) {
    if (q == NULL || q->count >= QUEUE_MAX_SIZE) {
        return false;  // Piena
    }

    q->rear = (q->rear + 1) % QUEUE_MAX_SIZE;  // Circolare
    q->data[q->rear] = value;
    q->count++;

    return true;
}

// Dequeue (rimuovi da testa)
bool queue_dequeue(Queue *q, int *value) {
    if (q == NULL || q->count == 0) {
        return false;  // Vuota
    }

    if (value != NULL) {
        *value = q->data[q->front];
    }

    q->front = (q->front + 1) % QUEUE_MAX_SIZE;  // Circolare
    q->count--;

    return true;
}

// Vuota?
bool queue_is_empty(const Queue *q) {
    return (q == NULL || q->count == 0);
}

// Piena?
bool queue_is_full(const Queue *q) {
    return (q != NULL && q->count >= QUEUE_MAX_SIZE);
}
```

---

## 9. File I/O

### 9.1 Operazioni Base

```c
#include <stdio.h>

// Apertura file
FILE *fp = fopen("file.txt", "r");  // Modalità
if (fp == NULL) {
    perror("Errore apertura file");
    return -1;
}

// Modalità:
// "r"   → Read (deve esistere)
// "w"   → Write (crea/tronca)
// "a"   → Append (crea/aggiunge)
// "r+"  → Read/Write (deve esistere)
// "w+"  → Read/Write (crea/tronca)
// "a+"  → Read/Append

// Chiusura (SEMPRE!)
fclose(fp);
```

### 9.2 Lettura File

```c
// Lettura carattere
int c;
while ((c = fgetc(fp)) != EOF) {
    putchar(c);
}

// Lettura riga
char buffer[256];
while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    printf("%s", buffer);  // buffer include '\n'
}

// Lettura formattata
int num;
char name[50];
while (fscanf(fp, "%d %49s", &num, name) == 2) {
    printf("%d: %s\n", num, name);
}

// Lettura binaria
int data[100];
size_t count = fread(data, sizeof(int), 100, fp);
printf("Letti %zu elementi\n", count);
```

### 9.3 Scrittura File

```c
FILE *fp = fopen("output.txt", "w");

// Scrittura carattere
fputc('A', fp);

// Scrittura stringa
fputs("Hello World\n", fp);

// Scrittura formattata
fprintf(fp, "Nome: %s, Età: %d\n", "Mario", 25);

// Scrittura binaria
int data[] = {1, 2, 3, 4, 5};
fwrite(data, sizeof(int), 5, fp);

fclose(fp);
```

### 9.4 Esempio Completo: CSV

```c
typedef struct {
    char name[50];
    int age;
    float salary;
} Person;

// Scrittura CSV
bool write_csv(const char *filename, Person *people, int count) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        return false;
    }

    // Header
    fprintf(fp, "Name,Age,Salary\n");

    // Dati
    for (int i = 0; i < count; i++) {
        fprintf(fp, "%s,%d,%.2f\n",
                people[i].name,
                people[i].age,
                people[i].salary);
    }

    fclose(fp);
    return true;
}

// Lettura CSV
bool read_csv(const char *filename, Person **people, int *count) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        return false;
    }

    // Salta header
    char line[256];
    fgets(line, sizeof(line), fp);

    // Alloca array dinamico
    int capacity = 10;
    *people = malloc(capacity * sizeof(Person));
    if (*people == NULL) {
        fclose(fp);
        return false;
    }
    *count = 0;

    // Leggi righe
    while (fgets(line, sizeof(line), fp) != NULL) {
        // Espandi se necessario
        if (*count >= capacity) {
            capacity *= 2;
            Person *temp = realloc(*people, capacity * sizeof(Person));
            if (temp == NULL) {
                free(*people);
                fclose(fp);
                return false;
            }
            *people = temp;
        }

        // Parse riga
        if (sscanf(line, "%49[^,],%d,%f",
                   (*people)[*count].name,
                   &(*people)[*count].age,
                   &(*people)[*count].salary) == 3) {
            (*count)++;
        }
    }

    fclose(fp);
    return true;
}

// Uso
int main(void) {
    Person people[] = {
        {"Mario Rossi", 30, 35000.0},
        {"Luigi Verdi", 25, 28000.0}
    };

    write_csv("people.csv", people, 2);

    Person *loaded;
    int count;
    if (read_csv("people.csv", &loaded, &count)) {
        for (int i = 0; i < count; i++) {
            printf("%s, %d, %.2f\n",
                   loaded[i].name,
                   loaded[i].age,
                   loaded[i].salary);
        }
        free(loaded);
    }

    return 0;
}
```

---

## 10. Debugging Assistito con IA

### 10.1 Prompt per Debugging

**Template:**
```
Ho questo codice C che genera errore:

[INSERISCI CODICE]

Messaggio errore del compilatore:
[INSERISCI ERRORE]

Analizza e:
1. Identifica la causa precisa dell'errore
2. Spiega PERCHÉ accade (concetti C sottostanti)
3. Fornisci FIX con commenti esplicativi
4. Suggerisci come PREVENIRE in futuro
5. Se ci sono altri problemi potenziali nel codice, elencali
```

### 10.2 GDB - GNU Debugger

```bash
# Compila con simboli debug
gcc -g -std=c99 -Wall myprogram.c -o myprogram

# Avvia GDB
gdb ./myprogram

# Comandi GDB essenziali:
(gdb) break main          # Breakpoint all'inizio di main
(gdb) break file.c:25     # Breakpoint a riga 25
(gdb) run                 # Esegui programma
(gdb) next                # Esegui prossima riga (step over)
(gdb) step                # Entra in funzione (step into)
(gdb) continue            # Continua fino a breakpoint
(gdb) print variabile     # Stampa valore
(gdb) print *pointer      # Dereferenzia puntatore
(gdb) backtrace           # Stack trace completo
(gdb) quit                # Esci
```

### 10.3 Valgrind

```bash
valgrind --leak-check=full \
         --show-leak-kinds=all \
         --track-origins=yes \
         --verbose \
         ./myprogram
```

### 10.4 Static Analysis

```bash
# cppcheck
cppcheck --enable=all --suppress=missingIncludeSystem mycode.c

# Compiler warnings
gcc -Wall -Wextra -Wpedantic -Werror mycode.c
```

---

## 11. Testing e Validazione

### 11.1 Unit Testing con Assert

```c
#include <assert.h>

void test_sum_array() {
    // Test normale
    int arr1[] = {1, 2, 3, 4, 5};
    assert(sum_array(arr1, 5) == 15);

    // Test edge cases
    assert(sum_array(NULL, 5) == 0);
    assert(sum_array(arr1, 0) == 0);
    assert(sum_array(arr1, -1) == 0);

    // Test array singolo
    int arr2[] = {42};
    assert(sum_array(arr2, 1) == 42);

    printf("✅ test_sum_array passed\n");
}

int main(void) {
    test_sum_array();
    // Altri test...

    printf("Tutti i test passati!\n");
    return 0;
}
```

### 11.2 Test Coverage

```
TEST CASES da considerare:
1. Caso normale (happy path)
2. Boundary conditions (limiti)
   - Input minimo/massimo
   - Array vuoto
   - Dimensione 1
3. Edge cases
   - NULL pointers
   - Valori negativi
   - Valori zero
4. Error conditions
   - Out of memory
   - Invalid input
5. Stress test
   - Input molto grandi
   - Chiamate ripetute
```

---

## 12. Best Practices C Professionale

### 12.1 Naming Conventions

```c
// ✅ BUONE CONVENZIONI
#define MAX_BUFFER_SIZE 1024     // Costanti: UPPER_SNAKE_CASE
typedef struct person_t Person;   // Typedef: PascalCase
int user_count = 0;               // Variabili: snake_case
void calculate_average(void);     // Funzioni: snake_case

// ❌ DA EVITARE
#define max 100                   // Minuscolo
int UserCount;                    // PascalCase per variabili
void CalcAvg(void);               // Nome abbreviato oscuro
```

### 12.2 Gestione Errori

```c
typedef enum {
    ERR_OK = 0,
    ERR_NULL_POINTER,
    ERR_OUT_OF_MEMORY,
    ERR_INVALID_INPUT,
    ERR_FILE_NOT_FOUND,
    ERR_OVERFLOW
} ErrorCode;

ErrorCode process_data(int *data, int size, int *result) {
    if (data == NULL || result == NULL) {
        return ERR_NULL_POINTER;
    }

    if (size <= 0 || size > MAX_SIZE) {
        return ERR_INVALID_INPUT;
    }

    // Processing...

    return ERR_OK;
}
```

### 12.3 Documentazione

```c
/**
 * @brief Calcola la media di un array di interi
 *
 * @param arr Array di interi (non NULL)
 * @param n Dimensione array (> 0)
 * @param result Puntatore per salvare risultato (non NULL)
 * @return ERR_OK se successo, codice errore altrimenti
 *
 * @note La media è calcolata come double per maggiore precisione
 * @warning Non gestisce overflow nella somma
 *
 * @example
 * int data[] = {10, 20, 30};
 * double avg;
 * if (calculate_average(data, 3, &avg) == ERR_OK) {
 *     printf("Media: %.2f\n", avg);
 * }
 */
ErrorCode calculate_average(const int arr[], int n, double *result);
```

---

## 13. Pattern di Programmazione Sicura

### 13.1 RAII Pattern (Resource Acquisition Is Initialization)

```c
// Macro helper per auto-cleanup
#define AUTO_FREE __attribute__((cleanup(cleanup_free)))

void cleanup_free(void *p) {
    free(*(void**)p);
}

void function() {
    AUTO_FREE char *buffer = malloc(100);

    // Usa buffer...

    // free() automatico quando esce da scope!
}
```

### 13.2 Goto Cleanup Pattern

```c
int complex_function(const char *filename) {
    FILE *fp = NULL;
    char *buffer = NULL;
    int *data = NULL;
    int result = -1;

    buffer = malloc(1024);
    if (buffer == NULL) {
        goto cleanup;
    }

    fp = fopen(filename, "r");
    if (fp == NULL) {
        goto cleanup;
    }

    data = malloc(100 * sizeof(int));
    if (data == NULL) {
        goto cleanup;
    }

    // ... elaborazione ...

    result = 0;  // Successo

cleanup:
    free(data);
    free(buffer);
    if (fp != NULL) fclose(fp);

    return result;
}
```

---

## 14. Progetti Completi Guidati

### 14.1 Progetto: Database Studenti

**Requisiti:**
- Struct Student con nome, età, voti
- Funzioni CRUD (Create, Read, Update, Delete)
- Salvataggio/caricamento da file CSV
- Menu interattivo
- Gestione memoria robusta
- Test completi

### 14.2 Progetto: Parser JSON Semplificato

**Requisiti:**
- Parsing file JSON con struttura fissa
- Strutture dati appropriate
- Gestione errori sintassi
- Validazione

---

## 15. Esercizi Pratici

### Esercizio 1: Safe String Operations
Implementa libreria di funzioni stringa sicure.

### Esercizio 2: Dynamic Array
Implementa array dinamico generico con crescita automatica.

### Esercizio 3: Hash Table
Implementa hash table semplice.

---

## ✅ Checklist Completamento Modulo

- [ ] Conosco problemi tipici codice C generato da IA
- [ ] Gestisco correttamente allocazione/deallocazione memoria
- [ ] Uso puntatori in modo sicuro
- [ ] Implemento funzioni stringa senza buffer overflow
- [ ] Creo strutture dati complete e robuste
- [ ] Gestisco file I/O in modo sicuro
- [ ] Uso GDB e Valgrind per debugging
- [ ] Scrivo test completi per validazione
- [ ] Applico best practices C professionali
- [ ] Ho completato almeno 2 progetti guidati

---

**Fine Modulo 3**

*Prossimo: Modulo 4 - Arduino e Sistemi Embedded*

---

**Versione:** 3.0 | **Aggiornamento:** Gennaio 2025 | **Corso ITS - IA e Programmazione Assistita**
