# 📘 DISPENSA COMPLETA - MODULO 3
# Programmazione in C con Supporto di Intelligenza Artificiale
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 3 ore | Livello: Intermedio-Avanzato

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti del Linguaggio C](#2-fondamenti-del-linguaggio-c)
3. [Problemi Ricorrenti del Codice Generato](#3-problemi-ricorrenti-del-codice-generato)
4. [Prompt Tecnici Specifici per C](#4-prompt-tecnici-specifici-per-c)
5. [Gestione della Memoria](#5-gestione-della-memoria)
6. [Puntatori e Array](#6-puntatori-e-array)
7. [Stringhe in C](#7-stringhe-in-c)
8. [Strutture Dati](#8-strutture-dati)
9. [File I/O](#9-file-io)
10. [Debugging Assistito](#10-debugging-assistito)
11. [Refactoring Professionale](#11-refactoring-professionale)
12. [Testing e Validazione](#12-testing-e-validazione)
13. [Progetti Completi Guidati](#13-progetti-completi-guidati)
14. [Esercizi Pratici](#14-esercizi-pratici)
15. [Best Practices C](#15-best-practices-c)

---

## 1. Introduzione e Obiettivi

### 1.1 Benvenuti al Modulo 3

Il **Modulo 3** è il cuore pratico del corso. Dopo aver compreso i fondamenti dell'IA (Modulo 1) e le tecniche di prompt engineering (Modulo 2), ora applichiamo tutto alla **programmazione in C** - il linguaggio fondamentale per sistemi embedded e ITS.

Il C è un linguaggio **potente ma pericoloso**: permette controllo totale sulla macchina, ma non perdona errori. L'IA può aiutare enormemente, ma richiede **guida esperta** per generare codice sicuro e affidabile.

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Generare** funzioni C robuste e sicure con supporto IA  
✅ **Identificare** errori tipici del codice generato (buffer overflow, memory leak, undefined behavior)  
✅ **Gestire** correttamente memoria, puntatori e array  
✅ **Implementare** strutture dati complete con IA assistita  
✅ **Debuggare** efficacemente codice C con supporto IA  
✅ **Refactorare** codice complesso migliorandone qualità e manutenibilità  
✅ **Scrivere** test completi per validare il codice  
✅ **Applicare** best practices professionali C  

### 1.3 Prerequisiti

- Moduli 1 e 2 completati
- Conoscenze base di C (variabili, cicli, funzioni)
- Compilatore C installato (gcc, clang)
- Editor/IDE preferito
- Accesso a LLM per programmazione

### 1.4 Perché il C è Speciale per l'IA

Il C presenta sfide uniche:

```
SFIDA 1: Gestione Manuale Memoria
→ IA può dimenticare free(), causare memory leak

SFIDA 2: Puntatori
→ IA può generare dereferenziazioni unsafe

SFIDA 3: Assenza di Controlli Runtime
→ Buffer overflow, array out-of-bounds non rilevati

SFIDA 4: Standard Multipli
→ C89, C99, C11, C17 - IA deve sapere quale usare

SFIDA 5: Differenze Compilatori
→ Codice valido su gcc può fallire su altri
```

**Per questo motivo serve MASSIMA attenzione nella validazione!**

### 1.5 Toolchain Raccomandata

```bash
# Compilatore con tutti i warning
gcc -std=c99 -Wall -Wextra -Wpedantic -Werror

# Static analysis
cppcheck --enable=all mycode.c

# Memory checking
valgrind --leak-check=full --track-origins=yes ./myprogram

# Code formatter
clang-format -style="{BasedOnStyle: Google}" mycode.c
```

---

## 2. Fondamenti del Linguaggio C

### 2.1 Caratteristiche Chiave del C

```c
/*
 * IL LINGUAGGIO C - CARATTERISTICHE FONDAMENTALI
 */

// 1. GESTIONE ESPLICITA MEMORIA
int *ptr = malloc(100 * sizeof(int));  // Tu allochi
// ... uso ...
free(ptr);  // Tu liberi

// 2. PUNTATORI (Potenza e Pericolo)
int x = 42;
int *p = &x;  // p punta a x
*p = 100;     // x ora vale 100

// 3. ARRAY = PUNTATORI
int arr[5];
arr[0] = 1;     // Equivalente a...
*(arr + 0) = 1; // ...questo

// 4. NESSUN CONTROLLO BOUNDS
arr[100] = 42;  // COMPILA ma è UNDEFINED BEHAVIOR

// 5. STRINGHE = ARRAY DI CHAR
char str[] = "Hello";  // = {'H','e','l','l','o','\0'}
```

### 2.2 Standard C: Quale Usare?

```c
/*
 * STANDARD C E DIFFERENZE
 */

// C89/C90 (ANSI C) - Vecchio ma ultra-portabile
void func_c89(void) {
    int i;  // Dichiarazioni SOLO all'inizio blocco
    for (i = 0; i < 10; i++) {
        // codice
    }
}

// C99 - Standard moderno raccomandato
void func_c99(void) {
    for (int i = 0; i < 10; i++) {  // ✅ Dichiarazione nel for
        // codice
    }
    
    // Altri vantaggi C99:
    // - Tipo bool (stdbool.h)
    // - long long
    // - Commenti //
    // - Inizializzatori designati
}

// C11 - Aggiunge features avanzate
#include <threads.h>   // Threading standard
#include <stdatomic.h> // Operazioni atomiche

// C17/C18 - Bug fix di C11, no nuove feature
```

**Raccomandazione per questo corso: C99**
- Moderno ma ampiamente supportato
- Balance tra features e portabilità
- Supporto universale su embedded

### 2.3 Header Files Essenziali

```c
#include <stdio.h>    // I/O: printf, scanf, fopen, etc.
#include <stdlib.h>   // Memoria: malloc, free, rand, etc.
#include <string.h>   // Stringhe: strlen, strcpy, strcmp, etc.
#include <stdbool.h>  // Tipo bool (C99+)
#include <stdint.h>   // Tipi size fissa: int32_t, uint8_t, etc.
#include <assert.h>   // Testing: assert()
#include <math.h>     // Matematica: sqrt, sin, etc. (-lm per linkare)
#include <ctype.h>    // Caratteri: isdigit, toupper, etc.
#include <time.h>     // Tempo: time, clock, etc.
```

### 2.4 Tipi di Dato e Dimensioni

```c
#include <stdint.h>
#include <stdio.h>
#include <limits.h>

void mostra_dimensioni(void) {
    printf("=== DIMENSIONI TIPI (può variare su architetture) ===\n");
    
    // Tipi base
    printf("char:      %zu byte  [%d, %d]\n", 
           sizeof(char), CHAR_MIN, CHAR_MAX);
    printf("short:     %zu byte  [%d, %d]\n", 
           sizeof(short), SHRT_MIN, SHRT_MAX);
    printf("int:       %zu byte  [%d, %d]\n", 
           sizeof(int), INT_MIN, INT_MAX);
    printf("long:      %zu byte\n", sizeof(long));
    printf("long long: %zu byte\n", sizeof(long long));
    printf("float:     %zu byte\n", sizeof(float));
    printf("double:    %zu byte\n", sizeof(double));
    printf("pointer:   %zu byte\n", sizeof(void*));
    
    // Tipi dimensione fissa (C99+)
    printf("\n=== TIPI DIMENSIONE FISSA (stdint.h) ===\n");
    printf("int8_t:    %zu byte\n", sizeof(int8_t));
    printf("int16_t:   %zu byte\n", sizeof(int16_t));
    printf("int32_t:   %zu byte\n", sizeof(int32_t));
    printf("int64_t:   %zu byte\n", sizeof(int64_t));
    printf("uint32_t:  %zu byte\n", sizeof(uint32_t));
}
```

**Quando usare tipi fixed-size:**
```c
// ✅ Embedded / hardware interface
uint32_t registro_hardware = 0xDEADBEEF;
int16_t adc_value = read_adc();

// ✅ Protocolli / serializzazione
struct Packet {
    uint32_t id;
    uint16_t length;
    uint8_t  data[256];
};

// ❌ Codice generale (usa int, long, etc.)
// int è ottimizzato per l'architettura target
```

---

## 3. Problemi Ricorrenti del Codice Generato

### 3.1 Problema 1: Funzioni Non Standard

L'IA spesso suggerisce funzioni che **non esistono** nello standard C.

#### **Esempio: strdup()**

```c
// ❌ IA potrebbe generare:
char *copy = strdup(original);

// PROBLEMA: strdup() è POSIX, non C standard!
// Non compila su alcuni sistemi (Windows MSVC, embedded bare-metal)
```

**Soluzione Standard:**
```c
// ✅ Versione standard C99:
char *my_strdup(const char *src) {
    if (src == NULL) {
        return NULL;
    }
    
    size_t len = strlen(src) + 1;  // +1 per '\0'
    char *dst = malloc(len);
    
    if (dst != NULL) {
        memcpy(dst, src, len);
        // Oppure: strcpy(dst, src);
    }
    
    return dst;
}
```

#### **Altre Funzioni Non Standard Comuni:**

```c
// ❌ NON STANDARD (ma IA può suggerirle):
strdup()     // → Usa malloc + strcpy
strndup()    // → Implementa manualmente
itoa()       // → Usa sprintf/snprintf
strlcpy()    // → Usa strncpy (con attenzione)
strlcat()    // → Usa strncat (con attenzione)
```

**Come Evitare:**
```
Prompt: "Usa SOLO funzioni C99 standard. 
NO estensioni POSIX, GNU, o specifiche compilatore."
```

### 3.2 Problema 2: Buffer Overflow

```c
// ❌ PERICOLOSO - IA potrebbe generare:
void copy_string(char *dest, const char *src) {
    strcpy(dest, src);  // BUFFER OVERFLOW se src > dest size!
}

// Esempio di disastro:
char buffer[10];
copy_string(buffer, "Questa stringa è troppo lunga!");
// → CRASH o COMPORTAMENTO IMPREVEDIBILE
```

**Soluzioni Safe:**

```c
// ✅ OPZIONE 1: strncpy (con caveats)
void copy_string_safe_v1(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }
    
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // Garantisci null-terminator
}

// ✅ OPZIONE 2: Manual loop (più controllo)
void copy_string_safe_v2(char *dest, const char *src, size_t dest_size) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }
    
    size_t i;
    for (i = 0; i < dest_size - 1 && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
}

// ✅ OPZIONE 3: snprintf (per stringhe formattate)
snprintf(dest, dest_size, "%s", src);  // Safe, sempre null-terminated
```

### 3.3 Problema 3: Memory Leak

```c
// ❌ IA potrebbe dimenticare free():
int* create_array(int n) {
    int *arr = malloc(n * sizeof(int));
    // ... init ...
    return arr;
}

void process_data(int n) {
    int *data = create_array(n);
    // ... uso data ...
    // ❌ MANCA: free(data);
}
// → MEMORY LEAK: memoria non liberata!
```

**Pattern Corretto:**

```c
// ✅ ALLOCAZIONE/LIBERAZIONE BILANCIATA
void process_data_safe(int n) {
    int *data = create_array(n);
    
    if (data == NULL) {
        // Gestione errore allocazione
        return;
    }
    
    // ... uso data ...
    
    free(data);  // ✅ Libera sempre!
    data = NULL; // Buona pratica: evita dangling pointer
}
```

**Valgrind per Rilevare Leak:**
```bash
$ gcc -g myprogram.c -o myprogram
$ valgrind --leak-check=full ./myprogram

# Output mostra:
# - Memoria allocata non liberata
# - Dove è stata allocata
# - Stack trace completo
```

### 3.4 Problema 4: Dereferenziazione NULL

```c
// ❌ IA potrebbe non controllare:
void process_array(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;  // CRASH se arr == NULL!
    }
}
```

**Pattern Difensivo:**

```c
// ✅ CONTROLLO ESPLICITO
bool process_array_safe(int *arr, int n) {
    // Validazione input
    if (arr == NULL) {
        return false;  // Indica errore
    }
    
    if (n <= 0) {
        return true;  // Successo (niente da fare)
    }
    
    // Processing sicuro
    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
    }
    
    return true;
}
```

### 3.5 Problema 5: Integer Overflow

```c
// ❌ IA potrebbe non gestire overflow:
int sum_array(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];  // Può overflow!
    }
    return sum;
}

// Esempio problematico:
int huge[] = {INT_MAX, INT_MAX};
int result = sum_array(huge, 2);  // Overflow → risultato sbagliato
```

**Soluzione con Rilevamento:**

```c
#include <limits.h>
#include <stdbool.h>

// ✅ Con rilevamento overflow
bool sum_array_safe(int arr[], int n, long long *result) {
    if (arr == NULL || result == NULL) {
        return false;
    }
    
    *result = 0;
    
    for (int i = 0; i < n; i++) {
        *result += arr[i];
        
        // Check overflow long long
        if (*result > LLONG_MAX - arr[i+1]) {  // Prossimo overflow?
            return false;  // Segnala overflow
        }
    }
    
    return true;
}
```

### 3.6 Problema 6: Off-by-One Errors

```c
// ❌ CLASSICO ERRORE:
void clear_array(int arr[], int n) {
    for (int i = 0; i <= n; i++) {  // ❌ <= invece di <
        arr[i] = 0;  // Accede a arr[n] → fuori range!
    }
}
```

**Regola Aurea:**
```c
// ✅ Array di n elementi: indici [0, n-1]
for (int i = 0; i < n; i++) {  // Corretto
    arr[i] = ...;
}

// ✅ Stringa di n char + '\0': [0, n-1] + [n] per '\0'
char str[n+1];
```

---

## 4. Prompt Tecnici Specifici per C

### 4.1 Template Prompt per Funzione C

```markdown
# TEMPLATE PROFESSIONALE PER FUNZIONI C

Scrivi in **standard C99** una funzione:

```c
[tipo_ritorno] nome_funzione([parametri]);
```

## Specifiche Comportamento
- [Cosa deve fare]
- [Come gestire input invalidi]
- [Valori di ritorno e significato]

## Vincoli
- SOLO C99 standard (no estensioni POSIX/GNU)
- No VLA (Variable Length Arrays) se [specificare]
- Gestione esplicita errori
- Controllo NULL per tutti i puntatori
- Controllo bounds per array

## Gestione Errori
[Descrivere strategia: return code, parametro output, etc.]

## Complessità
- Tempo: [O(?) attesa]
- Spazio: [O(?) attesa]

## Requisiti Output
1. Header file (.h) con:
   - Dichiarazione funzione
   - Documentazione Doxygen
   - Descrizione parametri ed errori
2. Implementation file (.c)
3. Test file con 5+ test cases coprendo:
   - Caso normale
   - Edge cases (vuoto, singolo, grande)
   - Errori (NULL, overflow)

## Esempio Uso
```c
// Mostra chiamata tipica
```
```

### 4.2 Esempi di Prompt Efficaci

#### **Esempio 1: Funzione Matematica**

```
Scrivi in standard C99 una funzione per calcolare la deviazione standard 
di un array di double:

double std_deviation(const double data[], int n);

COMPORTAMENTO:
- Calcola deviazione standard campionaria (n-1 nel denominatore)
- Ritorna 0.0 se n <= 1 (deviazione non definita)
- Gestisce data == NULL (ritorna 0.0)

VINCOLI:
- Solo C99 standard
- No librerie esterne (calc manuale di mean e variance)
- Include <math.h> per sqrt()
- Nessun overflow assumendo valori ragionevoli

FORMULA:
σ = sqrt( Σ(xi - mean)² / (n-1) )

OUTPUT:
- Header con Doxygen
- Implementation
- 4 test cases

ESEMPIO:
double data[] = {2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0};
double std = std_deviation(data, 8);
// std ≈ 2.138
```

#### **Esempio 2: Manipolazione Stringhe**

```
Scrivi in standard C99 una funzione per rimuovere spazi bianchi 
all'inizio e fine di una stringa (trim):

char* string_trim(const char *str);

COMPORTAMENTO:
- Alloca nuova stringa con malloc()
- Rimuove spazi/tab/newline da inizio e fine
- Ritorna puntatore a nuova stringa allocata
- Ritorna NULL se str == NULL o allocazione fallisce
- Chiamante responsabile di free()

VINCOLI:
- Solo C99 standard
- Usa isspace() da <ctype.h>
- Gestione errori esplicita

ESEMPI:
Input: "  hello  "   → Output: "hello"
Input: "\n\ttest\t"  → Output: "test"
Input: "   "         → Output: ""
Input: "no spaces"   → Output: "no spaces"

OUTPUT:
- Header + Implementation
- 5 test cases inclusi memory leak check
```

#### **Esempio 3: Struttura Dati**

```
Implementa in standard C99 una struttura Stack dinamico per interi:

INTERFACCIA RICHIESTA:

typedef struct Stack Stack;

Stack* stack_create(void);           // Crea stack vuoto
void stack_destroy(Stack *s);        // Libera memoria
bool stack_push(Stack *s, int val);  // Inserisce, return success
bool stack_pop(Stack *s, int *val);  // Rimuove, salva in *val
bool stack_peek(Stack *s, int *val); // Legge top senza rimuovere
bool stack_is_empty(Stack *s);       // Check vuoto
int stack_size(Stack *s);            // Numero elementi

IMPLEMENTAZIONE:
- Usa linked list interna (no array fisso)
- stack_create() ritorna NULL se allocazione fallisce
- Gestione errori: ritorna false/NULL su errore
- stack_destroy() gestisce s == NULL (no-op)

VINCOLI:
- Solo C99 standard
- No memory leak
- Complessità O(1) per tutte le operazioni

OUTPUT:
- stack.h (header con struct opaca)
- stack.c (implementation)
- test_stack.c (test completo)
```

### 4.3 Prompt per Conversione/Refactoring

```
REFACTORING ASSISTITO

Ho questa funzione C che funziona ma è poco leggibile:

```c
[CODICE ORIGINALE]
```

COMPITI:
1. Migliora nomi variabili (descrittivi, min 3 caratteri)
2. Aggiungi commenti significativi
3. Estrai sotto-funzioni se logica complessa
4. Aggiungi gestione errori se mancante
5. Aggiungi documentazione Doxygen
6. Mantieni identico comportamento esterno

VINCOLI:
- Solo C99 standard
- Mantieni stessa firma funzione
- No cambio algoritmo (solo riorganizzazione)

VERIFICA:
- Fornisci test che dimostrano equivalenza comportamentale
```

### 4.4 Prompt per Debugging

```
DEBUGGING ASSISTITO

Ho questo codice C che compila ma ha un bug:

```c
[CODICE CON BUG]
```

ERRORE OSSERVATO:
[Descrizione comportamento errato o crash]

COMPITI:
1. Identifica il/i bug
2. Spiega PERCHÉ il bug causa il problema
3. Fornisci versione corretta
4. Aggiungi test che rileva il bug (deve fallire su versione buggata)

VINCOLI:
- Spiega in modo didattico (sto imparando)
- Mostra differenze fianco a fianco
```

---

## 5. Gestione della Memoria

### 5.1 Allocazione Dinamica

```c
#include <stdlib.h>

/*
 * FUNZIONI ALLOCAZIONE MEMORIA
 */

// malloc() - Alloca n byte (contenuto indefinito)
void esempio_malloc(void) {
    int *arr = malloc(10 * sizeof(int));
    
    if (arr == NULL) {
        // SEMPRE controllare allocazione!
        fprintf(stderr, "Allocazione fallita!\n");
        return;
    }
    
    // Usa arr...
    for (int i = 0; i < 10; i++) {
        arr[i] = i;  // Contenuto era indefinito, ora inizializzato
    }
    
    free(arr);  // Libera
    arr = NULL; // Buona pratica
}

// calloc() - Alloca e inizializza a zero
void esempio_calloc(void) {
    int *arr = calloc(10, sizeof(int));
    
    if (arr == NULL) {
        return;
    }
    
    // arr[i] è già 0 per tutti i ∈ [0,9]
    
    free(arr);
}

// realloc() - Ridimensiona blocco esistente
void esempio_realloc(void) {
    int *arr = malloc(10 * sizeof(int));
    if (arr == NULL) return;
    
    // ... uso arr[0..9] ...
    
    // Serve più spazio
    int *new_arr = realloc(arr, 20 * sizeof(int));
    
    if (new_arr == NULL) {
        // realloc fallito, arr ancora valido!
        free(arr);
        return;
    }
    
    arr = new_arr;  // Ora arr punta a blocco più grande
    
    // arr[0..9] contiene dati originali
    // arr[10..19] ha contenuto indefinito
    
    free(arr);
}
```

### 5.2 Pattern Comuni e Insidie

#### **Pattern: Allocazione Array 2D**

```c
// ❌ SBAGLIATO (non continuo in memoria):
int **matrix = malloc(rows * sizeof(int*));
for (int i = 0; i < rows; i++) {
    matrix[i] = malloc(cols * sizeof(int));
}
// Problema: memoria frammentata, più lenta

// ✅ CORRETTO (memoria contigua):
int **matrix_create(int rows, int cols) {
    // Alloca puntatori righe
    int **matrix = malloc(rows * sizeof(int*));
    if (matrix == NULL) return NULL;
    
    // Alloca TUTTO lo spazio dati in un blocco
    int *data = malloc(rows * cols * sizeof(int));
    if (data == NULL) {
        free(matrix);
        return NULL;
    }
    
    // Collega puntatori a dati
    for (int i = 0; i < rows; i++) {
        matrix[i] = data + i * cols;
    }
    
    return matrix;
}

void matrix_destroy(int **matrix) {
    if (matrix != NULL) {
        free(matrix[0]);  // Libera dati
        free(matrix);     // Libera puntatori
    }
}

// Uso:
int **m = matrix_create(100, 100);
m[5][10] = 42;  // Accesso normale
matrix_destroy(m);
```

#### **Pattern: Struct con Membri Dinamici**

```c
typedef struct {
    char *name;      // Dinamico
    int *scores;     // Dinamico
    int num_scores;
} Student;

// ✅ Creazione corretta
Student* student_create(const char *name, int num_scores) {
    Student *s = malloc(sizeof(Student));
    if (s == NULL) return NULL;
    
    // Copia nome
    s->name = malloc(strlen(name) + 1);
    if (s->name == NULL) {
        free(s);
        return NULL;
    }
    strcpy(s->name, name);
    
    // Alloca array scores
    s->scores = calloc(num_scores, sizeof(int));
    if (s->scores == NULL) {
        free(s->name);
        free(s);
        return NULL;
    }
    
    s->num_scores = num_scores;
    return s;
}

// ✅ Distruzione corretta
void student_destroy(Student *s) {
    if (s != NULL) {
        free(s->name);    // Libera membri
        free(s->scores);
        free(s);          // Libera struct
    }
}
```

### 5.3 Rilevamento Memory Leak

**Setup Valgrind:**
```bash
# Compila con debug symbols
gcc -g -std=c99 -Wall program.c -o program

# Run con Valgrind
valgrind --leak-check=full \
         --show-leak-kinds=all \
         --track-origins=yes \
         --verbose \
         --log-file=valgrind-out.txt \
         ./program
```

**Output Valgrind:**
```
==12345== HEAP SUMMARY:
==12345==     in use at exit: 100 bytes in 1 blocks
==12345==   total heap usage: 10 allocs, 9 frees, 1,000 bytes allocated
==12345==
==12345== 100 bytes in 1 blocks are definitely lost
==12345==    at malloc (vg_replace_malloc.c:309)
==12345==    by create_array (program.c:42)
==12345==    by main (program.c:100)
```

**Interpretazione:**
- `1 blocks definitely lost` = Memory leak confermato
- Mostra dove allocato (program.c:42)
- Mostra chi ha chiamato (main a linea 100)

---

## 6. Puntatori e Array

### 6.1 Relazione Array-Puntatore

```c
/*
 * ARRAY E PUNTATORI: LA VERITÀ
 */

void array_pointer_demo(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    
    // arr "decade" a puntatore al primo elemento
    int *p = arr;  // Equivalente a: int *p = &arr[0];
    
    printf("arr[0] = %d\n", arr[0]);   // 10
    printf("*p = %d\n", *p);            // 10 (stesso)
    
    printf("arr[2] = %d\n", arr[2]);   // 30
    printf("*(p+2) = %d\n", *(p+2));   // 30 (stesso)
    printf("p[2] = %d\n", p[2]);       // 30 (stesso!)
    
    // Aritmetica puntatori
    p++;              // p punta a arr[1]
    printf("*p = %d\n", *p);  // 20
    
    // DIFFERENZE CHIAVE:
    // sizeof(arr) = 5 * sizeof(int) = 20 byte
    // sizeof(p) = sizeof(pointer) = 8 byte (su 64-bit)
    
    printf("sizeof(arr) = %zu\n", sizeof(arr));  // 20
    printf("sizeof(p) = %zu\n", sizeof(p));      // 8
}
```

### 6.2 Array Multidimensionali

```c
/*
 * ARRAY 2D: MEMORIA CONTIGUA
 */

void array_2d_demo(void) {
    int matrix[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    
    // Accesso standard
    printf("matrix[1][2] = %d\n", matrix[1][2]);  // 7
    
    // Accesso come array flat
    int *flat = (int*)matrix;
    printf("flat[6] = %d\n", flat[6]);  // 7 (riga 1, col 2)
    // Indice flat = riga * num_col + col = 1 * 4 + 2 = 6
    
    // Iterazione
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }
}

/*
 * PASSAGGIO ARRAY 2D A FUNZIONE
 */

// ✅ METODO 1: Dimensioni note a compile-time
void print_matrix_fixed(int m[3][4]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
}

// ✅ METODO 2: Seconda dimensione come parametro
void print_matrix_variable(int rows, int cols, int m[][cols]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
}

// ✅ METODO 3: Pointer + calcolo manuale indici
void print_matrix_flat(int *m, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            int index = i * cols + j;
            printf("%d ", m[index]);
        }
        printf("\n");
    }
}
```

### 6.3 Const Correctness

```c
/*
 * USO CORRETTO DI CONST CON PUNTATORI
 */

// const int *p - Puntatore a int const (non posso modificare *p)
void read_only_data(const int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);  // ✅ Lettura OK
        // arr[i] = 0;  // ❌ ERRORE: modifica dato const
    }
    arr++;  // ✅ OK: posso modificare il puntatore
}

// int * const p - Puntatore const a int (non posso modificare p)
void fixed_pointer(int * const arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = 0;  // ✅ OK: posso modificare dati
    }
    // arr++;  // ❌ ERRORE: puntatore è const
}

// const int * const p - Puntatore const a int const
void read_only_all(const int * const arr, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];  // ✅ Solo lettura
    }
    // arr[i] = 0;  // ❌ ERRORE
    // arr++;       // ❌ ERRORE
}

// Regola mnemonica: Leggi da DESTRA a SINISTRA
// const int *p  →  puntatore a (int che è const)
// int * const p  →  puntatore const a int
```

### 6.4 Puntatori a Funzione

```c
/*
 * PUNTATORI A FUNZIONE
 */

// Definizione tipo per chiarezza
typedef int (*CompareFunc)(int a, int b);

// Funzioni di confronto
int compare_asc(int a, int b) {
    return a - b;  // Crescente
}

int compare_desc(int a, int b) {
    return b - a;  // Decrescente
}

// Sort generico con funzione di confronto
void bubble_sort(int arr[], int n, CompareFunc compare) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (compare(arr[j], arr[j+1]) > 0) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

// Uso
void demo_function_pointers(void) {
    int arr[] = {5, 2, 8, 1, 9};
    
    // Ordina crescente
    bubble_sort(arr, 5, compare_asc);
    
    // Ordina decrescente
    bubble_sort(arr, 5, compare_desc);
}
```

---

## 7. Stringhe in C

### 7.1 Fondamenti Stringhe

```c
/*
 * STRINGHE IN C: ARRAY DI CHAR TERMINATI DA '\0'
 */

#include <string.h>

void string_basics(void) {
    // Metodo 1: Literal (read-only, in segment costante)
    const char *s1 = "Hello";  // ✅ const perché in memoria read-only
    
    // Metodo 2: Array (modificabile, sullo stack)
    char s2[] = "Hello";  // = {'H','e','l','l','o','\0'}
    s2[0] = 'h';  // ✅ OK: posso modificare
    
    // Metodo 3: Array con dimensione esplicita
    char s3[10] = "Hello";  // Spazio per 9 char + '\0'
    
    // ATTENZIONE: Dimensione array vs lunghezza stringa
    printf("sizeof(s2) = %zu\n", sizeof(s2));    // 6 (include '\0')
    printf("strlen(s2) = %zu\n", strlen(s2));    // 5 (escluso '\0')
    
    // Iterazione
    for (int i = 0; s2[i] != '\0'; i++) {
        printf("%c", s2[i]);
    }
    printf("\n");
    
    // Equivalente con pointer
    for (char *p = s2; *p != '\0'; p++) {
        printf("%c", *p);
    }
    printf("\n");
}
```

### 7.2 Funzioni Stringhe Standard

```c
#include <string.h>
#include <stdio.h>

void string_functions_demo(void) {
    char dest[50];
    const char *src = "Hello World";
    
    // strlen() - Lunghezza (escluso '\0')
    size_t len = strlen(src);  // 11
    
    // strcpy() - Copia (PERICOLOSO se dest troppo piccolo)
    strcpy(dest, src);  // ⚠️ No size check!
    
    // strncpy() - Copia sicura (ma caveats)
    strncpy(dest, src, sizeof(dest) - 1);
    dest[sizeof(dest) - 1] = '\0';  // Garantisci '\0'
    
    // strcmp() - Confronto
    if (strcmp(dest, src) == 0) {
        printf("Stringhe uguali\n");
    }
    // ritorna: < 0 se s1 < s2, 0 se uguali, > 0 se s1 > s2
    
    // strcat() - Concatenazione (PERICOLOSO)
    strcat(dest, "!");  // ⚠️ No size check!
    
    // strncat() - Concatenazione sicura
    strncat(dest, "!", sizeof(dest) - strlen(dest) - 1);
    
    // strchr() - Cerca carattere
    char *pos = strchr(src, 'W');
    if (pos != NULL) {
        printf("'W' trovato a posizione %ld\n", pos - src);
    }
    
    // strstr() - Cerca sottostringa
    char *sub = strstr(src, "World");
    if (sub != NULL) {
        printf("Trovato: %s\n", sub);  // "World"
    }
    
    // sprintf() - Formattazione
    char buffer[100];
    int n = 42;
    sprintf(buffer, "Il numero è %d", n);
    
    // snprintf() - Formattazione sicura (PREFERIBILE)
    snprintf(buffer, sizeof(buffer), "Il numero è %d", n);
}
```

### 7.3 Implementazione Funzioni Custom

```c
/*
 * IMPLEMENTAZIONI STRINGHE DA ZERO (Didattico)
 */

// strlen() custom
size_t my_strlen(const char *s) {
    const char *p = s;
    while (*p != '\0') {
        p++;
    }
    return p - s;
}

// strcpy() custom
char* my_strcpy(char *dest, const char *src) {
    char *saved = dest;
    while ((*dest++ = *src++) != '\0') {
        // Copy e avanza entrambi
    }
    return saved;
}

// strcmp() custom
int my_strcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    return *(unsigned char*)s1 - *(unsigned char*)s2;
}

// strcat() custom
char* my_strcat(char *dest, const char *src) {
    char *saved = dest;
    
    // Trova fine di dest
    while (*dest != '\0') {
        dest++;
    }
    
    // Copia src
    while ((*dest++ = *src++) != '\0') {
        // Copy
    }
    
    return saved;
}

// strtok() - Tokenizzazione (modifica stringa!)
void tokenization_example(void) {
    char str[] = "Hello,World,Test";  // Deve essere modificabile
    
    char *token = strtok(str, ",");
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok(NULL, ",");  // NULL per continuare
    }
    // Dopo: str è modificato con '\0' al posto delle ','
}
```

### 7.4 String Safety Checklist

```c
/*
 * CHECKLIST SICUREZZA STRINGHE
 */

// ✅ VERSIONE SAFE di copy string
void safe_string_copy(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }
    
    // METODO 1: strncpy + garantisci '\0'
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';
    
    // METODO 2: Manual loop (più controllo)
    size_t i;
    for (i = 0; i < dest_size - 1 && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';
    
    // METODO 3: snprintf
    snprintf(dest, dest_size, "%s", src);
}

// ✅ VERSIONE SAFE di concat string
bool safe_string_concat(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return false;
    }
    
    size_t dest_len = strlen(dest);
    size_t available = dest_size - dest_len - 1;  // -1 per '\0'
    
    if (available == 0) {
        return false;  // Nessuno spazio
    }
    
    strncat(dest, src, available);
    return true;
}
```

---

## 8. Strutture Dati

### 8.1 Struct Base

```c
/*
 * STRUTTURE (STRUCT)
 */

// Definizione
struct Point {
    int x;
    int y;
};

// Uso con typedef
typedef struct {
    double x;
    double y;
} Point2D;

// Struct con membri dinamici
typedef struct {
    char *name;
    int age;
    double *grades;
    int num_grades;
} Student;

// Inizializzazione
void struct_basics(void) {
    // Metodo 1: Inizializzazione completa
    struct Point p1 = {10, 20};
    
    // Metodo 2: Inizializzazione parziale (resto a zero)
    struct Point p2 = {.x = 5};  // y = 0
    
    // Metodo 3: Assegnamento
    Point2D p3;
    p3.x = 1.5;
    p3.y = 2.5;
    
    // Accesso membri
    printf("p1: (%d, %d)\n", p1.x, p1.y);
    
    // Copia struct (shallow copy)
    Point2D p4 = p3;  // Copia tutti i membri
    
    // Pointer a struct
    Point2D *ptr = &p3;
    printf("ptr->x = %.2f\n", ptr->x);  // -> invece di .
    // Equivalente a: (*ptr).x
}
```

### 8.2 Linked List Completa

```c
/*
 * IMPLEMENTAZIONE LINKED LIST COMPLETA
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Nodo
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Lista
typedef struct {
    Node *head;
    int size;
} LinkedList;

// Crea lista vuota
LinkedList* list_create(void) {
    LinkedList *list = malloc(sizeof(LinkedList));
    if (list != NULL) {
        list->head = NULL;
        list->size = 0;
    }
    return list;
}

// Inserisci all'inizio
bool list_prepend(LinkedList *list, int value) {
    if (list == NULL) return false;
    
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL) return false;
    
    new_node->data = value;
    new_node->next = list->head;
    list->head = new_node;
    list->size++;
    
    return true;
}

// Inserisci alla fine
bool list_append(LinkedList *list, int value) {
    if (list == NULL) return false;
    
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL) return false;
    
    new_node->data = value;
    new_node->next = NULL;
    
    if (list->head == NULL) {
        list->head = new_node;
    } else {
        Node *current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_node;
    }
    
    list->size++;
    return true;
}

// Cerca valore
bool list_contains(LinkedList *list, int value) {
    if (list == NULL) return false;
    
    Node *current = list->head;
    while (current != NULL) {
        if (current->data == value) {
            return true;
        }
        current = current->next;
    }
    return false;
}

// Rimuovi valore
bool list_remove(LinkedList *list, int value) {
    if (list == NULL || list->head == NULL) {
        return false;
    }
    
    // Caso speciale: rimuovi head
    if (list->head->data == value) {
        Node *temp = list->head;
        list->head = list->head->next;
        free(temp);
        list->size--;
        return true;
    }
    
    // Cerca in resto lista
    Node *current = list->head;
    while (current->next != NULL) {
        if (current->next->data == value) {
            Node *temp = current->next;
            current->next = current->next->next;
            free(temp);
            list->size--;
            return true;
        }
        current = current->next;
    }
    
    return false;  // Non trovato
}

// Stampa lista
void list_print(LinkedList *list) {
    if (list == NULL) return;
    
    printf("[");
    Node *current = list->head;
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) {
            printf(", ");
        }
        current = current->next;
    }
    printf("]\n");
}

// Distruggi lista
void list_destroy(LinkedList *list) {
    if (list == NULL) return;
    
    Node *current = list->head;
    while (current != NULL) {
        Node *next = current->next;
        free(current);
        current = next;
    }
    
    free(list);
}

// Test
int main(void) {
    LinkedList *list = list_create();
    
    list_append(list, 10);
    list_append(list, 20);
    list_prepend(list, 5);
    
    list_print(list);  // [5, 10, 20]
    
    printf("Contains 10? %s\n", list_contains(list, 10) ? "Yes" : "No");
    
    list_remove(list, 10);
    list_print(list);  // [5, 20]
    
    list_destroy(list);
    return 0;
}
```

### 8.3 Stack Dinamico

```c
/*
 * STACK DINAMICO (LIFO)
 */

typedef struct {
    int *data;
    int top;
    int capacity;
} Stack;

Stack* stack_create(int initial_capacity) {
    if (initial_capacity <= 0) {
        return NULL;
    }
    
    Stack *s = malloc(sizeof(Stack));
    if (s == NULL) return NULL;
    
    s->data = malloc(initial_capacity * sizeof(int));
    if (s->data == NULL) {
        free(s);
        return NULL;
    }
    
    s->top = -1;
    s->capacity = initial_capacity;
    
    return s;
}

bool stack_push(Stack *s, int value) {
    if (s == NULL) return false;
    
    // Espandi se necessario
    if (s->top >= s->capacity - 1) {
        int new_capacity = s->capacity * 2;
        int *new_data = realloc(s->data, new_capacity * sizeof(int));
        if (new_data == NULL) return false;
        
        s->data = new_data;
        s->capacity = new_capacity;
    }
    
    s->data[++s->top] = value;
    return true;
}

bool stack_pop(Stack *s, int *value) {
    if (s == NULL || s->top < 0) {
        return false;
    }
    
    if (value != NULL) {
        *value = s->data[s->top];
    }
    s->top--;
    
    return true;
}

bool stack_peek(Stack *s, int *value) {
    if (s == NULL || s->top < 0) {
        return false;
    }
    
    if (value != NULL) {
        *value = s->data[s->top];
    }
    
    return true;
}

bool stack_is_empty(Stack *s) {
    return (s == NULL || s->top < 0);
}

int stack_size(Stack *s) {
    return (s == NULL) ? 0 : (s->top + 1);
}

void stack_destroy(Stack *s) {
    if (s != NULL) {
        free(s->data);
        free(s);
    }
}
```

---

## 9. File I/O

### 9.1 Operazioni Base su File

```c
#include <stdio.h>
#include <stdlib.h>

/*
 * FILE I/O SICURO
 */

// Lettura file testuale completo
char* read_text_file(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("Errore apertura file");
        return NULL;
    }
    
    // Trova dimensione file
    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    
    // Alloca buffer
    char *content = malloc(size + 1);
    if (content == NULL) {
        fclose(fp);
        return NULL;
    }
    
    // Leggi
    size_t read = fread(content, 1, size, fp);
    content[read] = '\0';
    
    fclose(fp);
    return content;
}

// Scrittura file testuale
bool write_text_file(const char *filename, const char *content) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        perror("Errore apertura file");
        return false;
    }
    
    size_t len = strlen(content);
    size_t written = fwrite(content, 1, len, fp);
    
    fclose(fp);
    return (written == len);
}

// Lettura riga per riga
void read_file_lines(const char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("Errore apertura file");
        return;
    }
    
    char line[256];
    int line_num = 1;
    
    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%d: %s", line_num++, line);
    }
    
    fclose(fp);
}

// Scrittura formattata
void write_data_file(const char *filename) {
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        perror("Errore apertura file");
        return;
    }
    
    fprintf(fp, "Temperatura: %.2f C\n", 25.5);
    fprintf(fp, "Umidita: %d%%\n", 60);
    fprintf(fp, "Timestamp: %ld\n", time(NULL));
    
    fclose(fp);
}
```

### 9.2 File Binari

```c
/*
 * I/O BINARIO
 */

typedef struct {
    int id;
    char name[50];
    double salary;
} Employee;

// Scrittura array struct su file binario
bool save_employees(const char *filename, Employee *emps, int count) {
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) return false;
    
    size_t written = fwrite(emps, sizeof(Employee), count, fp);
    fclose(fp);
    
    return (written == count);
}

// Lettura array struct da file binario
Employee* load_employees(const char *filename, int *count) {
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) return NULL;
    
    // Trova numero elementi
    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    
    *count = size / sizeof(Employee);
    
    Employee *emps = malloc((*count) * sizeof(Employee));
    if (emps == NULL) {
        fclose(fp);
        return NULL;
    }
    
    size_t read = fread(emps, sizeof(Employee), *count, fp);
    fclose(fp);
    
    if (read != *count) {
        free(emps);
        return NULL;
    }
    
    return emps;
}
```

---

## 10. Debugging Assistito

### 10.1 Strategia di Debugging con IA

```
PROCESSO DI DEBUGGING ASSISTITO:

1. RIPRODUZIONE
   - Codice minimo che mostra il bug
   - Input che causa il problema
   - Output atteso vs ottenuto

2. ANALISI SINTOMI
   - Crash? (Segfault, abort)
   - Output errato?
   - Memory leak?
   - Comportamento imprevedibile?

3. PROMPT PER IA
   "Ho questo codice che [sintomo]:
   
   [Codice minimo]
   
   Input: [esempio]
   Output atteso: [...]
   Output ottenuto: [...]
   
   Analizza e identifica bug."

4. VALIDAZIONE FIX
   - Compila fix proposto
   - Testa su caso problematico
   - Testa su edge cases
   - Valgrind per memory issues

5. COMPRENSIONE
   - Perché il bug si verificava?
   - Come il fix risolve?
   - Come prevenire in futuro?
```

### 10.2 Esempi di Debugging

#### **Caso 1: Segmentation Fault**

```c
// ❌ Codice con bug
void reverse_string(char *str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i];      // ❌ BUG! Dovrebbe essere len-i-1
        str[len - i] = temp;
    }
}

int main(void) {
    char *s = "Hello";              // ❌ BUG! String literal (read-only)
    reverse_string(s);
    printf("%s\n", s);
    return 0;
}

// Prompt per IA:
```
Questo codice causa segfault:

[codice sopra]

Errore: Segmentation fault (core dumped)

Analizza e correggi entrambi i bug.
```

#### **Risposta IA (esempio):**

```c
/*
 * BUG IDENTIFICATI:
 * 1. String literal è read-only → serve array modificabile
 * 2. Indice errato: len-i invece di len-i-1
 */

// ✅ VERSIONE CORRETTA
void reverse_string(char *str) {
    if (str == NULL) return;
    
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];  // ✅ Corretto
        str[len - i - 1] = temp;
    }
}

int main(void) {
    char s[] = "Hello";  // ✅ Array modificabile
    reverse_string(s);
    printf("%s\n", s);   // Output: "olleH"
    return 0;
}
```

#### **Caso 2: Memory Leak**

```c
// ❌ Codice con leak
char* concat_strings(const char *s1, const char *s2) {
    char *result = malloc(strlen(s1) + strlen(s2) + 1);
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

int main(void) {
    for (int i = 0; i < 1000; i++) {
        char *s = concat_strings("Hello", "World");
        printf("%s\n", s);
        // ❌ MANCA: free(s);
    }
    return 0;
}

// Prompt:
```
Valgrind mostra memory leak:

==12345== 11,000 bytes in 1,000 blocks are definitely lost

[codice sopra]

Come fixare?
```

#### **Risposta:**

```c
// ✅ SOLUZIONE: Libera memoria allocata
int main(void) {
    for (int i = 0; i < 1000; i++) {
        char *s = concat_strings("Hello", "World");
        printf("%s\n", s);
        free(s);  // ✅ Libera
    }
    return 0;
}

// ALTERNATIVA: Gestione automatica con cleanup attribute (GCC)
__attribute__((cleanup(cleanup_string))) char *s = concat_strings("Hello", "World");
// s viene automaticamente liberato quando esce di scope
```

---

## 11. Refactoring Professionale

### 11.1 Principi di Refactoring

```
OBIETTIVI REFACTORING:
1. Leggibilità → Nomi descrittivi, struttura chiara
2. Manutenibilità → Funzioni piccole, singola responsabilità
3. Testabilità → Funzioni pure, side effects minimizzati
4. Performance → Solo se necessario (measure first!)
```

### 11.2 Esempio Completo di Refactoring

#### **Before - Codice da Refactorare:**

```c
// ❌ CODICE POCO LEGGIBILE
int f(int *a, int n) {
    int x = 0, y = a[0], z = a[0];
    for (int i = 1; i < n; i++) {
        x += a[i];
        if (a[i] > y) y = a[i];
        if (a[i] < z) z = a[i];
    }
    return x / n;  // BUG: divisione intera!
}
```

**Problemi:**
- Nomi variabili criptici (x, y, z, f)
- Nessun commento
- Nessuna gestione errori
- Bug: divisione intera perde precisione
- Troppa logica in una funzione

#### **After - Codice Refactorato:**

```c
/**
 * @brief Struttura per statistiche array
 */
typedef struct {
    double average;
    int max;
    int min;
    bool valid;
} ArrayStats;

/**
 * @brief Calcola statistiche base di un array di interi
 * 
 * @param array Array di interi da analizzare
 * @param size Dimensione array
 * @return Struttura con statistiche, valid=false se errore
 */
ArrayStats calculate_array_statistics(const int *array, int size) {
    ArrayStats stats = {0.0, 0, 0, false};
    
    // Validazione input
    if (array == NULL || size <= 0) {
        return stats;
    }
    
    // Inizializzazione
    long long sum = array[0];  // long long per evitare overflow
    int max_value = array[0];
    int min_value = array[0];
    
    // Calcolo statistiche
    for (int i = 1; i < size; i++) {
        sum += array[i];
        
        if (array[i] > max_value) {
            max_value = array[i];
        }
        
        if (array[i] < min_value) {
            min_value = array[i];
        }
    }
    
    // Risultato
    stats.average = (double)sum / size;  // Cast per divisione float
    stats.max = max_value;
    stats.min = min_value;
    stats.valid = true;
    
    return stats;
}

// Uso
void demo_refactored(void) {
    int data[] = {5, 2, 8, 1, 9, 3};
    ArrayStats stats = calculate_array_statistics(data, 6);
    
    if (stats.valid) {
        printf("Average: %.2f\n", stats.average);
        printf("Max: %d\n", stats.max);
        printf("Min: %d\n", stats.min);
    }
}
```

**Miglioramenti:**
✅ Nome funzione descrittivo
✅ Struct per ritorno multiplo valori
✅ Commenti Doxygen
✅ Gestione errori esplicita
✅ Nomi variabili chiari
✅ Fix bug divisione
✅ Gestione overflow (long long)

---

## 12. Testing e Validazione

### 12.1 Framework di Testing Minimale

```c
/*
 * MINI TESTING FRAMEWORK
 */

#include <stdio.h>
#include <stdbool.h>

int tests_run = 0;
int tests_passed = 0;

#define TEST(name) \
    void test_##name(void); \
    void run_test_##name(void) { \
        printf("Running: %s... ", #name); \
        test_##name(); \
    } \
    void test_##name(void)

#define ASSERT(condition) \
    do { \
        tests_run++; \
        if (condition) { \
            tests_passed++; \
        } else { \
            printf("\n  FAIL: %s:%d: %s\n", __FILE__, __LINE__, #condition); \
        } \
    } while (0)

#define ASSERT_EQ(a, b) ASSERT((a) == (b))
#define ASSERT_NEQ(a, b) ASSERT((a) != (b))
#define ASSERT_TRUE(x) ASSERT(x)
#define ASSERT_FALSE(x) ASSERT(!(x))
#define ASSERT_NULL(x) ASSERT((x) == NULL)
#define ASSERT_NOT_NULL(x) ASSERT((x) != NULL)

// Uso:
TEST(array_sum_normal) {
    int arr[] = {1, 2, 3, 4, 5};
    int result = sum_array(arr, 5);
    ASSERT_EQ(result, 15);
    printf("OK\n");
}

TEST(array_sum_empty) {
    int result = sum_array(NULL, 0);
    ASSERT_EQ(result, 0);
    printf("OK\n");
}

int main(void) {
    printf("=== Running Tests ===\n");
    
    run_test_array_sum_normal();
    run_test_array_sum_empty();
    
    printf("\n=== Results ===\n");
    printf("Tests run: %d\n", tests_run);
    printf("Tests passed: %d\n", tests_passed);
    printf("Tests failed: %d\n", tests_run - tests_passed);
    
    return (tests_run == tests_passed) ? 0 : 1;
}
```

### 12.2 Test Coverage Completo

```c
/*
 * ESEMPIO: TEST COMPLETO PER BINARY SEARCH
 */

#include <assert.h>

// Funzione da testare (dichiarata altrove)
int binary_search(const int arr[], int n, int target);

void test_binary_search_suite(void) {
    printf("=== Binary Search Test Suite ===\n");
    
    // Test 1: Elemento presente (centro)
    {
        int arr[] = {1, 3, 5, 7, 9, 11, 13};
        assert(binary_search(arr, 7, 7) == 3);
        printf("✓ Test 1: elemento al centro\n");
    }
    
    // Test 2: Elemento presente (inizio)
    {
        int arr[] = {10, 20, 30, 40, 50};
        assert(binary_search(arr, 5, 10) == 0);
        printf("✓ Test 2: elemento all'inizio\n");
    }
    
    // Test 3: Elemento presente (fine)
    {
        int arr[] = {2, 4, 6, 8, 10};
        assert(binary_search(arr, 5, 10) == 4);
        printf("✓ Test 3: elemento alla fine\n");
    }
    
    // Test 4: Elemento NON presente
    {
        int arr[] = {1, 2, 3, 4, 5};
        assert(binary_search(arr, 5, 99) == -1);
        printf("✓ Test 4: elemento non presente\n");
    }
    
    // Test 5: Array vuoto
    {
        assert(binary_search(NULL, 0, 5) == -1);
        printf("✓ Test 5: array vuoto\n");
    }
    
    // Test 6: Array singolo elemento (match)
    {
        int arr[] = {42};
        assert(binary_search(arr, 1, 42) == 0);
        printf("✓ Test 6: singolo elemento (match)\n");
    }
    
    // Test 7: Array singolo elemento (no match)
    {
        int arr[] = {42};
        assert(binary_search(arr, 1, 100) == -1);
        printf("✓ Test 7: singolo elemento (no match)\n");
    }
    
    // Test 8: Array grande
    {
        int arr[1000];
        for (int i = 0; i < 1000; i++) {
            arr[i] = i * 2;  // Array pari: 0, 2, 4, ..., 1998
        }
        assert(binary_search(arr, 1000, 500) == 250);
        assert(binary_search(arr, 1000, 501) == -1);  // Dispari non presente
        printf("✓ Test 8: array grande\n");
    }
    
    // Test 9: Valori negativi
    {
        int arr[] = {-50, -30, -10, 0, 10, 30, 50};
        assert(binary_search(arr, 7, -30) == 1);
        printf("✓ Test 9: valori negativi\n");
    }
    
    // Test 10: Tutti elementi uguali
    {
        int arr[] = {5, 5, 5, 5, 5};
        int result = binary_search(arr, 5, 5);
        assert(result >= 0 && result < 5);  // Può ritornare qualsiasi indice valido
        printf("✓ Test 10: elementi duplicati\n");
    }
    
    printf("\n✅ Tutti i test passati!\n");
}
```

---

## 13. Progetti Completi Guidati

### 13.1 Progetto: Gestione Contatti

**Obiettivo:** Sistema completo CRUD (Create, Read, Update, Delete) per contatti.

```c
/*
 * PROGETTO: SISTEMA GESTIONE CONTATTI
 * Features:
 * - Aggiunta contatto
 * - Ricerca per nome
 * - Modifica contatto
 * - Eliminazione
 * - Salvataggio su file
 * - Caricamento da file
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_NAME 50
#define MAX_PHONE 20
#define MAX_EMAIL 50

// Struttura Contatto
typedef struct {
    int id;
    char name[MAX_NAME];
    char phone[MAX_PHONE];
    char email[MAX_EMAIL];
} Contact;

// Struttura Agenda
typedef struct {
    Contact *contacts;
    int size;
    int capacity;
} ContactBook;

// === FUNZIONI CORE ===

ContactBook* contactbook_create(int initial_capacity) {
    if (initial_capacity <= 0) {
        initial_capacity = 10;
    }
    
    ContactBook *book = malloc(sizeof(ContactBook));
    if (book == NULL) return NULL;
    
    book->contacts = malloc(initial_capacity * sizeof(Contact));
    if (book->contacts == NULL) {
        free(book);
        return NULL;
    }
    
    book->size = 0;
    book->capacity = initial_capacity;
    
    return book;
}

void contactbook_destroy(ContactBook *book) {
    if (book != NULL) {
        free(book->contacts);
        free(book);
    }
}

bool contactbook_add(ContactBook *book, const char *name, 
                     const char *phone, const char *email) {
    if (book == NULL || name == NULL) {
        return false;
    }
    
    // Espandi se necessario
    if (book->size >= book->capacity) {
        int new_cap = book->capacity * 2;
        Contact *new_contacts = realloc(book->contacts, 
                                        new_cap * sizeof(Contact));
        if (new_contacts == NULL) {
            return false;
        }
        book->contacts = new_contacts;
        book->capacity = new_cap;
    }
    
    // Aggiungi contatto
    Contact *c = &book->contacts[book->size];
    c->id = book->size + 1;
    
    strncpy(c->name, name, MAX_NAME - 1);
    c->name[MAX_NAME - 1] = '\0';
    
    if (phone != NULL) {
        strncpy(c->phone, phone, MAX_PHONE - 1);
        c->phone[MAX_PHONE - 1] = '\0';
    } else {
        c->phone[0] = '\0';
    }
    
    if (email != NULL) {
        strncpy(c->email, email, MAX_EMAIL - 1);
        c->email[MAX_EMAIL - 1] = '\0';
    } else {
        c->email[0] = '\0';
    }
    
    book->size++;
    return true;
}

Contact* contactbook_find_by_name(ContactBook *book, const char *name) {
    if (book == NULL || name == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < book->size; i++) {
        if (strcmp(book->contacts[i].name, name) == 0) {
            return &book->contacts[i];
        }
    }
    
    return NULL;
}

bool contactbook_remove_by_id(ContactBook *book, int id) {
    if (book == NULL) {
        return false;
    }
    
    for (int i = 0; i < book->size; i++) {
        if (book->contacts[i].id == id) {
            // Shifta elementi successivi
            for (int j = i; j < book->size - 1; j++) {
                book->contacts[j] = book->contacts[j + 1];
            }
            book->size--;
            return true;
        }
    }
    
    return false;
}

void contactbook_print_all(ContactBook *book) {
    if (book == NULL) {
        return;
    }
    
    printf("\n=== Contact Book (%d contacts) ===\n", book->size);
    for (int i = 0; i < book->size; i++) {
        Contact *c = &book->contacts[i];
        printf("ID: %d\n", c->id);
        printf("  Name:  %s\n", c->name);
        printf("  Phone: %s\n", c->phone);
        printf("  Email: %s\n", c->email);
        printf("\n");
    }
}

// === PERSISTENZA FILE ===

bool contactbook_save(ContactBook *book, const char *filename) {
    if (book == NULL || filename == NULL) {
        return false;
    }
    
    FILE *fp = fopen(filename, "wb");
    if (fp == NULL) {
        return false;
    }
    
    // Salva size
    fwrite(&book->size, sizeof(int), 1, fp);
    
    // Salva contatti
    fwrite(book->contacts, sizeof(Contact), book->size, fp);
    
    fclose(fp);
    return true;
}

ContactBook* contactbook_load(const char *filename) {
    if (filename == NULL) {
        return NULL;
    }
    
    FILE *fp = fopen(filename, "rb");
    if (fp == NULL) {
        return NULL;
    }
    
    // Leggi size
    int size;
    if (fread(&size, sizeof(int), 1, fp) != 1) {
        fclose(fp);
        return NULL;
    }
    
    // Crea book
    ContactBook *book = contactbook_create(size);
    if (book == NULL) {
        fclose(fp);
        return NULL;
    }
    
    // Leggi contatti
    if (fread(book->contacts, sizeof(Contact), size, fp) != size) {
        contactbook_destroy(book);
        fclose(fp);
        return NULL;
    }
    
    book->size = size;
    fclose(fp);
    
    return book;
}

// === MAIN DI TEST ===

int main(void) {
    // Crea agenda
    ContactBook *book = contactbook_create(5);
    
    // Aggiungi contatti
    contactbook_add(book, "Mario Rossi", "333-1234567", "mario@example.com");
    contactbook_add(book, "Luisa Verdi", "347-7654321", "luisa@example.com");
    contactbook_add(book, "Paolo Bianchi", "320-9876543", NULL);
    
    // Mostra tutti
    contactbook_print_all(book);
    
    // Cerca
    Contact *found = contactbook_find_by_name(book, "Luisa Verdi");
    if (found != NULL) {
        printf("Trovato: %s - %s\n", found->name, found->phone);
    }
    
    // Salva su file
    if (contactbook_save(book, "contacts.dat")) {
        printf("Salvato su file\n");
    }
    
    // Distruggi
    contactbook_destroy(book);
    
    // Ricarica da file
    book = contactbook_load("contacts.dat");
    if (book != NULL) {
        printf("\nRicaricato da file:\n");
        contactbook_print_all(book);
        contactbook_destroy(book);
    }
    
    return 0;
}
```

---

## 14. Esercizi Pratici

### Esercizio 1: Media Mobile

**Implementa filtro media mobile per segnali.**

<details>
<summary>Prompt Suggerito</summary>

```
Implementa in C99 un filtro media mobile (moving average) per segnali:

INTERFACCIA:
typedef struct MovingAverage MovingAverage;

MovingAverage* ma_create(int window_size);
void ma_destroy(MovingAverage *ma);
double ma_update(MovingAverage *ma, double new_value);
void ma_reset(MovingAverage *ma);

COMPORTAMENTO:
- Mantiene ultimi N valori (window_size)
- Ritorna media degli ultimi N valori
- Usa circular buffer interno

VINCOLI:
- Solo C99 standard
- O(1) per update
- Gestione errori

TEST: 5 casi inclusi
```

</details>

### Esercizio 2: Parser CSV

**Leggi file CSV e salva in array struct.**

<details>
<summary>Soluzione Parziale</summary>

```c
typedef struct {
    int id;
    char name[50];
    double value;
} Record;

Record* parse_csv(const char *filename, int *count) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        *count = 0;
        return NULL;
    }
    
    // Prima passata: conta righe
    int lines = 0;
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        lines++;
    }
    
    // Alloca array
    Record *records = malloc(lines * sizeof(Record));
    if (records == NULL) {
        fclose(fp);
        *count = 0;
        return NULL;
    }
    
    // Seconda passata: parsing
    rewind(fp);
    int i = 0;
    while (fgets(buffer, sizeof(buffer), fp) != NULL && i < lines) {
        sscanf(buffer, "%d,%49[^,],%lf", 
               &records[i].id, 
               records[i].name, 
               &records[i].value);
        i++;
    }
    
    fclose(fp);
    *count = i;
    return records;
}
```

</details>

### Esercizio 3: Hash Table Semplice

**Implementa hash table per stringhe.**

<details>
<summary>Prompt</summary>

```
Implementa hash table semplice in C99:

INTERFACCIA:
typedef struct HashTable HashTable;

HashTable* ht_create(int size);
void ht_destroy(HashTable *ht);
bool ht_insert(HashTable *ht, const char *key, int value);
bool ht_get(HashTable *ht, const char *key, int *value);
bool ht_remove(HashTable *ht, const char *key);

IMPLEMENTAZIONE:
- Array di liste (chaining per collisioni)
- Hash function: djb2 o simile
- Gestione memoria dinamica

VINCOLI: C99, no memory leak

TEST: Includi test con collisioni
```

</details>

---

## 15. Best Practices C

### 15.1 Checklist Qualità Codice

```
✅ COMPILAZIONE
[ ] gcc -std=c99 -Wall -Wextra -Wpedantic -Werror
[ ] Nessun warning
[ ] cppcheck senza issue

✅ MEMORIA
[ ] Ogni malloc ha corrispondente free
[ ] Valgrind --leak-check=full pulito
[ ] No buffer overflow
[ ] Puntatori NULL controllati

✅ STILE
[ ] Nomi variabili descrittivi (min 3 char)
[ ] Funzioni < 50 righe
[ ] Nesting depth < 4
[ ] Commenti significativi
[ ] Documentazione Doxygen per API pubblica

✅ SICUREZZA
[ ] Input validation su tutte le funzioni pubbliche
[ ] Bounds checking su array
[ ] Uso strncpy/snprintf invece strcpy/sprintf
[ ] Integer overflow considerato

✅ TESTING
[ ] Test per caso normale
[ ] Test per edge cases
[ ] Test per errori
[ ] Coverage > 80%

✅ PORTABILITÀ
[ ] Solo C99 standard
[ ] stdint.h per tipi fixed-size
[ ] No assunzioni su sizeof(int), endianness
```

### 15.2 Coding Style Raccomandato

```c
/*
 * STYLE GUIDE ESEMPIO
 */

// Nomi: snake_case per funzioni e variabili
int calculate_sum(int array[], int size);

// Costanti: UPPER_CASE
#define MAX_BUFFER_SIZE 256
#define PI 3.14159265359

// Tipi custom: PascalCase con typedef
typedef struct {
    int x;
    int y;
} Point;

// Enums: UPPER_CASE con prefix
typedef enum {
    STATUS_OK = 0,
    STATUS_ERROR = -1,
    STATUS_INVALID_INPUT = -2
} StatusCode;

// Indentazione: 4 spazi (no tab)
void example_function(void) {
    if (condition) {
        do_something();
    } else {
        do_something_else();
    }
}

// Braces: Same-line per funzioni piccole, new-line per grandi
void small_function(void) {
    // code
}

void large_function(int param1, int param2,
                    int param3, int param4)
{
    // code molto lungo
}

// Commenti: // per single-line, /* */ per block
// Questo è un commento single-line

/*
 * Questo è un commento
 * multi-linea
 */

/**
 * Doxygen comment per documentazione API
 */
```

---

## ✅ Checklist Completamento Modulo 3

- [ ] Ho compreso problemi specifici del C con IA
- [ ] So scrivere prompt efficaci per funzioni C
- [ ] Gestisco correttamente allocazione/liberazione memoria
- [ ] Conosco pattern sicuri per puntatori e array
- [ ] So manipolare stringhe in modo sicuro
- [ ] Ho implementato almeno 2 strutture dati complete
- [ ] So debuggare codice C con supporto IA
- [ ] Applico refactoring professionale
- [ ] Scrivo test completi per validazione
- [ ] Seguo best practices C99
- [ ] Ho completato almeno 2 progetti guidati
- [ ] Mi sento pronto per Modulo 4 (Arduino)

---

**Fine Modulo 3**

*Prossimo passo: Modulo 4 - Programmazione Arduino con Supporto IA*

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita
