# 📘 LEZIONE 3: PROGRAMMAZIONE C SICURA CON IA
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Durata:** 2 ore
**Struttura:** 1 ora teoria + 1 ora pratica
**Livello:** Intermedio
**Prerequisiti:** Lezione 1 e 2 completate, conoscenza base di C (puntatori, memoria dinamica)

---

## 🎯 Obiettivi della Lezione

Al termine di questa lezione sarai in grado di:

✅ **Identificare** problemi ricorrenti nel codice generato da IA
✅ **Riconoscere** e **prevenire** buffer overflow
✅ **Gestire** correttamente memoria dinamica (malloc/free)
✅ **Evitare** memory leak e dangling pointer
✅ **Usare** Valgrind per identificare problemi di memoria
✅ **Applicare** best practices per codice C sicuro
✅ **Validare** sistematicamente codice generato da IA
✅ **Scrivere** codice memory-safe con assistenza IA

---

## 📋 Struttura della Lezione

### **PARTE 1: TEORIA (60 minuti)**

1. **Problemi Ricorrenti del Codice IA** (15 min)
   - Pattern di errori comuni
   - Perché l'IA sbaglia in C
   - Esempi reali di codice pericoloso

2. **Buffer Overflow e Gestione Stringhe** (15 min)
   - Cos'è un buffer overflow
   - Funzioni pericolose (gets, strcpy, sprintf)
   - Alternative sicure (fgets, strncpy, snprintf)

3. **Gestione Memoria Dinamica** (15 min)
   - malloc, calloc, realloc, free
   - Memory leak: cause e prevenzione
   - Dangling pointer e double free
   - Use-after-free

4. **Puntatori e Sicurezza** (15 min)
   - Dereferenziare NULL
   - Array bounds checking
   - Pointer arithmetic pericoloso
   - Const correctness

### **PARTE 2: PRATICA (60 minuti)**

5. **Workshop Valgrind** (20 min)
   - Installazione e setup
   - Uso base: memory leak detection
   - Invalid memory access
   - Interpretare output

6. **Correggere Codice IA Pericoloso** (20 min)
   - Esercizi pratici guidati
   - Identificare vulnerabilità
   - Applicare fix

7. **Progetto: Sistema Gestione Dati Sicuro** (15 min)
   - Implementare struttura dati con IA
   - Validare con Valgrind
   - Code review

8. **Best Practices e Checklist** (5 min)
   - Checklist di sicurezza
   - Pattern da seguire sempre

---

---

# PARTE 1: TEORIA (60 MINUTI)

---

## 1. PROBLEMI RICORRENTI DEL CODICE IA (15 minuti)

### 1.1 Perché l'IA Sbaglia in C

**Contesto importante:**

L'IA ha "visto" durante il training miliardi di righe di codice C, incluso:
- ✅ Codice ottimo e sicuro
- ❌ Codice buggy e vulnerabile
- ❌ Codice didattico semplificato (senza error handling)
- ❌ Snippet incompleti

**Risultato:** L'IA genera spesso codice che "funziona in casi normali" ma **fallisce con edge cases** o ha **vulnerabilità sottili**.

**Analogia:**

Immagina di imparare a guidare guardando video su YouTube:
- Vedi molti esempi di guida corretta
- Ma vedi anche video di incidenti
- Vedi tutorial semplificati che saltano dettagli
- Non sai distinguere cosa è "buona pratica" da "esempio didattico"

Stesso problema per l'IA con il codice C.

### 1.2 Le 10 Trappole Più Comuni

**TRAPPOLA #1: Manca controllo malloc**

```c
// ❌ CODICE GENERATO DA IA (PERICOLOSO)
int* create_array(int size) {
    int *arr = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        arr[i] = 0;  // ← CRASH se malloc fallisce!
    }
    return arr;
}
```

**Problema:** Se `malloc()` fallisce (memoria insufficiente), ritorna NULL. Dereferenziare NULL → segmentation fault.

**Fix:**
```c
// ✅ CODICE CORRETTO
int* create_array(int size) {
    int *arr = malloc(size * sizeof(int));
    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }
    for (int i = 0; i < size; i++) {
        arr[i] = 0;
    }
    return arr;
}
```

---

**TRAPPOLA #2: Buffer overflow con strcpy**

```c
// ❌ CODICE GENERATO DA IA (PERICOLOSO)
void copy_name(char *dest, const char *src) {
    strcpy(dest, src);  // ← Buffer overflow se src > dest!
}

// Uso:
char buffer[10];
copy_name(buffer, "This is a very long string");  // ← OVERFLOW!
```

**Problema:** `strcpy` non controlla dimensione buffer destinazione.

**Fix:**
```c
// ✅ CODICE CORRETTO
void copy_name(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';  // Assicura null-termination
}

// Uso:
char buffer[10];
copy_name(buffer, sizeof(buffer), "This is a very long string");
```

---

**TRAPPOLA #3: Memory leak (dimenticato free)**

```c
// ❌ CODICE GENERATO DA IA (MEMORY LEAK)
void process_data() {
    int *data = malloc(100 * sizeof(int));

    // ... processa data ...

    if (some_error) {
        return;  // ← Leak! Dimenticato free(data)
    }

    free(data);
}
```

**Problema:** Early return senza liberare memoria.

**Fix:**
```c
// ✅ CODICE CORRETTO
void process_data() {
    int *data = malloc(100 * sizeof(int));
    if (data == NULL) {
        return;
    }

    // ... processa data ...

    if (some_error) {
        free(data);  // ← Free prima di return
        return;
    }

    free(data);
}
```

---

**TRAPPOLA #4: Off-by-one error**

```c
// ❌ CODICE GENERATO DA IA (BUG SOTTILE)
void print_array(int *arr, int size) {
    for (int i = 0; i <= size; i++) {  // ← <= invece di <
        printf("%d ", arr[i]);
    }
}

// Array di 5 elementi: arr[0] a arr[4]
// Ma loop accede arr[5]! Fuori bounds!
```

**Fix:**
```c
// ✅ CODICE CORRETTO
void print_array(int *arr, int size) {
    for (int i = 0; i < size; i++) {  // ← < (non <=)
        printf("%d ", arr[i]);
    }
}
```

---

**TRAPPOLA #5: Use-after-free**

```c
// ❌ CODICE GENERATO DA IA (PERICOLOSISSIMO)
int* get_temporary_buffer() {
    int *buffer = malloc(100 * sizeof(int));
    // ... inizializza buffer ...
    free(buffer);
    return buffer;  // ← Ritorna pointer a memoria liberata!
}

// Uso:
int *data = get_temporary_buffer();
data[0] = 42;  // ← Use-after-free! Undefined behavior!
```

**Problema:** Restituisce pointer a memoria già liberata.

**Fix:**
```c
// ✅ CODICE CORRETTO - Approccio 1: Caller alloca
void fill_buffer(int *buffer, size_t size) {
    if (buffer == NULL) return;
    // ... riempi buffer ...
}

// Uso:
int *data = malloc(100 * sizeof(int));
fill_buffer(data, 100);
// ... usa data ...
free(data);

// ✅ CODICE CORRETTO - Approccio 2: Trasferisci ownership
int* create_buffer() {
    int *buffer = malloc(100 * sizeof(int));
    // ... inizializza buffer ...
    return buffer;  // Caller DEVE fare free!
}
```

---

**TRAPPOLA #6: Double free**

```c
// ❌ CODICE GENERATO DA IA (CRASH)
void cleanup(int **ptr) {
    if (*ptr != NULL) {
        free(*ptr);
        // ← Manca: *ptr = NULL;
    }
}

int main() {
    int *data = malloc(100 * sizeof(int));

    cleanup(&data);
    cleanup(&data);  // ← Double free! Crash!
}
```

**Fix:**
```c
// ✅ CODICE CORRETTO
void cleanup(int **ptr) {
    if (*ptr != NULL) {
        free(*ptr);
        *ptr = NULL;  // ← Previene double free
    }
}
```

---

**TRAPPOLA #7: Sizeof su pointer**

```c
// ❌ CODICE GENERATO DA IA (BUG SOTTILE)
void allocate_and_zero(int **arr, int count) {
    *arr = malloc(count * sizeof(int));
    memset(*arr, 0, sizeof(*arr));  // ← SBAGLIATO!
}

// sizeof(*arr) = sizeof(int*) = 8 byte (su 64bit)
// Ma dovrebbe essere: count * sizeof(int)
```

**Fix:**
```c
// ✅ CODICE CORRETTO
void allocate_and_zero(int **arr, int count) {
    *arr = malloc(count * sizeof(int));
    if (*arr == NULL) return;
    memset(*arr, 0, count * sizeof(int));  // ← Corretto
}
```

---

**TRAPPOLA #8: Return di array locale**

```c
// ❌ CODICE GENERATO DA IA (UNDEFINED BEHAVIOR)
int* create_sequence() {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    return arr;  // ← Ritorna pointer a stack locale!
}

// arr è nello stack, viene distrutto al return
// Pointer ritornato punta a memoria non valida!
```

**Fix:**
```c
// ✅ CODICE CORRETTO - Alloca su heap
int* create_sequence() {
    int *arr = malloc(10 * sizeof(int));
    if (arr == NULL) return NULL;

    for (int i = 0; i < 10; i++) {
        arr[i] = i + 1;
    }
    return arr;  // Caller deve fare free!
}
```

---

**TRAPPOLA #9: Funzioni inesistenti (allucinazione)**

```c
// ❌ CODICE GENERATO DA IA (FUNZIONE INVENTATA)
#include <safestring.h>  // ← Header inesistente!

void my_function(char *dest, const char *src) {
    safe_strcpy(dest, src);  // ← Funzione inesistente!
}
```

**Come riconoscere:**
- Header mai sentito → cerca documentazione online
- Funzione dal nome "troppo perfetto" → verifica su cppreference.com
- Compilatore: "undefined reference" → probabilmente inventata

---

**TRAPPOLA #10: Integer overflow**

```c
// ❌ CODICE GENERATO DA IA (OVERFLOW)
int* allocate_matrix(int rows, int cols) {
    int total = rows * cols;  // ← Overflow se rows e cols grandi!
    return malloc(total * sizeof(int));
}

// Esempio: rows=100000, cols=100000
// total = 10000000000 (overflow in int a 32bit!)
// malloc riceve valore sbagliato!
```

**Fix:**
```c
// ✅ CODICE CORRETTO
int* allocate_matrix(int rows, int cols) {
    if (rows <= 0 || cols <= 0) return NULL;

    // Check overflow
    if (rows > INT_MAX / cols) {
        fprintf(stderr, "Size overflow\n");
        return NULL;
    }

    size_t total = (size_t)rows * (size_t)cols;
    return malloc(total * sizeof(int));
}
```

### 1.3 Pattern di Riconoscimento

**Quando sospettare codice IA pericoloso:**

🚩 **Mancano controlli NULL** dopo malloc/fopen/ecc
🚩 **Usa funzioni pericolose** (gets, strcpy, sprintf)
🚩 **Nessun controllo bounds** su array
🚩 **Free assente** o in posizione sbagliata
🚩 **Sizeof su pointer** invece che su tipo
🚩 **Return di variabili locali**
🚩 **Nomi troppo perfetti** di funzioni mai sentite
🚩 **Commenti vaghi** ("this does something complex")

**Regola d'oro:**

> **"Se codice sembra 'troppo semplice', probabilmente manca gestione errori."**

---

## 2. BUFFER OVERFLOW E GESTIONE STRINGHE (15 minuti)

### 2.1 Cos'è un Buffer Overflow

**Definizione:**

Un **buffer overflow** avviene quando si scrivono dati oltre i limiti di un buffer allocato.

**Esempio visivo:**

```
Buffer: char name[10];

Memory layout:
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │  name[10]
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
┌─────────────────────────────────────────┐
│        Altra memoria (stack)            │  Variabili vicine
└─────────────────────────────────────────┘

Se scrivo "Hello World\0" (12 byte):
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ H │ e │ l │ l │ o │   │ W │ o │ r │ l │  name[10]
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
    ↓
┌───┬───┐
│ d │ \0│  ← OVERFLOW! Sovrascritto memoria non nostra!
└───┴───┘
```

**Conseguenze:**

1. **Crash del programma** (segmentation fault)
2. **Corruzione dati** di altre variabili
3. **Vulnerabilità di sicurezza** (attacker può iniettare codice)

### 2.2 Funzioni Pericolose

**🔴 LISTA NERA - NON USARE MAI:**

| Funzione Pericolosa | Perché è Pericolosa | Alternativa Sicura |
|---------------------|---------------------|---------------------|
| `gets(buffer)` | Nessun controllo lunghezza | `fgets(buffer, size, stdin)` |
| `strcpy(dest, src)` | Nessun controllo bounds | `strncpy()` o `strlcpy()` |
| `strcat(dest, src)` | Nessun controllo bounds | `strncat()` o `strlcat()` |
| `sprintf(buf, fmt, ...)` | Nessun limite buffer | `snprintf(buf, size, fmt, ...)` |
| `scanf("%s", buf)` | Nessun controllo lunghezza | `scanf("%99s", buf)` con limite |

**Esempio pericoloso → sicuro:**

**❌ gets() - LA FUNZIONE PIÙ PERICOLOSA**

```c
char name[50];
printf("Enter name: ");
gets(name);  // ← Se utente scrive 100 caratteri: OVERFLOW!
```

**✅ fgets() - Versione sicura**

```c
char name[50];
printf("Enter name: ");
fgets(name, sizeof(name), stdin);

// Remove newline se presente
name[strcspn(name, "\n")] = '\0';
```

---

**❌ strcpy() - Copia senza controllo**

```c
char dest[10];
char src[] = "This string is too long";
strcpy(dest, src);  // ← OVERFLOW!
```

**✅ strncpy() - Copia con limite**

```c
char dest[10];
char src[] = "This string is too long";
strncpy(dest, src, sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';  // Assicura null-termination
```

**⚠️ Attenzione:** `strncpy` NON garantisce null-termination se src è più lunga di dest!

**✅✅ Ancora meglio: wrapper sicuro**

```c
void safe_strcpy(char *dest, size_t dest_size, const char *src) {
    if (dest == NULL || src == NULL || dest_size == 0) {
        return;
    }
    strncpy(dest, src, dest_size - 1);
    dest[dest_size - 1] = '\0';
}

// Uso:
char dest[10];
safe_strcpy(dest, sizeof(dest), "Very long string");
```

---

**❌ sprintf() - Formattazione senza limiti**

```c
char buffer[20];
int value = 12345678;
sprintf(buffer, "Value: %d", value);  // Se risultato > 20 char: overflow!
```

**✅ snprintf() - Formattazione sicura**

```c
char buffer[20];
int value = 12345678;
int written = snprintf(buffer, sizeof(buffer), "Value: %d", value);

if (written >= sizeof(buffer)) {
    fprintf(stderr, "Warning: output truncated\n");
}
```

---

**❌ scanf("%s") - Input senza limite**

```c
char name[10];
scanf("%s", name);  // Utente può scrivere 1000 caratteri!
```

**✅ scanf con limite**

```c
char name[10];
scanf("%9s", name);  // Max 9 caratteri + \0
```

### 2.3 Best Practices per Stringhe

**Regola #1: Sempre usare dimensioni esplicite**

```c
// ❌ MALE
char buffer[100];
strcpy(buffer, input);

// ✅ BENE
char buffer[100];
strncpy(buffer, input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';
```

**Regola #2: Validare input utente**

```c
// ❌ MALE
char name[50];
fgets(name, sizeof(name), stdin);
// Assume che input sia valido

// ✅ BENE
char name[50];
if (fgets(name, sizeof(name), stdin) == NULL) {
    fprintf(stderr, "Error reading input\n");
    return -1;
}

// Remove newline
name[strcspn(name, "\n")] = '\0';

// Validate lunghezza
if (strlen(name) == 0) {
    fprintf(stderr, "Empty name not allowed\n");
    return -1;
}
```

**Regola #3: Usa const per parametri read-only**

```c
// Indica che src non sarà modificata
void copy_string(char *dest, size_t dest_size, const char *src) {
    // ...
}
```

### 2.4 Esercizio: Trova il Bug

**Codice generato da IA:**

```c
#include <stdio.h>
#include <string.h>

void create_greeting(char *buffer, const char *name) {
    strcpy(buffer, "Hello, ");
    strcat(buffer, name);
    strcat(buffer, "!");
}

int main() {
    char greeting[20];
    create_greeting(greeting, "Alessandro");
    printf("%s\n", greeting);
    return 0;
}
```

**Quanti bug trovi?**

<details>
<summary>Clicca per vedere i bug</summary>

**Bug #1:** `strcpy` senza controllo dimensione
**Bug #2:** `strcat` senza controllo dimensione
**Bug #3:** Manca parametro `buffer_size` in `create_greeting`
**Bug #4:** Se name è molto lungo: buffer overflow!

**Fix:**

```c
void create_greeting(char *buffer, size_t buffer_size, const char *name) {
    if (buffer == NULL || name == NULL || buffer_size < 10) {
        return;
    }

    snprintf(buffer, buffer_size, "Hello, %s!", name);
}
```

</details>

---

## 3. GESTIONE MEMORIA DINAMICA (15 minuti)

### 3.1 malloc, calloc, realloc, free

**malloc() - Memory Allocation**

```c
// Alloca N byte NON inizializzati
void* malloc(size_t size);

// Uso:
int *arr = malloc(10 * sizeof(int));
if (arr == NULL) {
    // Errore: memoria insufficiente
    return -1;
}

// arr[0], arr[1], ... contengono valori casuali (garbage)!

free(arr);
```

**calloc() - Contiguous Allocation (con zero-init)**

```c
// Alloca N elementi, ognuno di size byte, INIZIALIZZATI A ZERO
void* calloc(size_t nmemb, size_t size);

// Uso:
int *arr = calloc(10, sizeof(int));
if (arr == NULL) {
    return -1;
}

// arr[0], arr[1], ... sono TUTTI 0

free(arr);
```

**Quando usare calloc vs malloc:**

- **calloc:** Quando serve inizializzazione a zero (strutture, array di puntatori)
- **malloc:** Quando inizializzerai subito dopo (performance legg migliore)

**realloc() - Reallocation**

```c
// Cambia dimensione blocco memoria
void* realloc(void *ptr, size_t new_size);

// Uso:
int *arr = malloc(10 * sizeof(int));

// Voglio espandere a 20 elementi
int *new_arr = realloc(arr, 20 * sizeof(int));
if (new_arr == NULL) {
    // realloc fallito, arr è ancora valido!
    free(arr);
    return -1;
}

// realloc può aver spostato memoria
arr = new_arr;  // Usa nuovo puntatore

free(arr);
```

**⚠️ Errore comune con realloc:**

```c
// ❌ SBAGLIATO
arr = realloc(arr, new_size);
if (arr == NULL) {
    // Problema: se realloc fallisce, il puntatore originale è perso!
}

// ✅ CORRETTO
int *temp = realloc(arr, new_size);
if (temp == NULL) {
    free(arr);  // Libera memoria originale
    return -1;
}
arr = temp;
```

**free() - Libera memoria**

```c
void free(void *ptr);

// Uso:
int *arr = malloc(100 * sizeof(int));
// ... usa arr ...
free(arr);
arr = NULL;  // Buona pratica: previene use-after-free
```

### 3.2 Memory Leak: Cause e Prevenzione

**Definizione:**

Un **memory leak** avviene quando memoria allocata NON viene liberata prima che il puntatore venga perso.

**Causa #1: Dimenticato free()**

```c
// ❌ MEMORY LEAK
void process_data() {
    int *data = malloc(1000 * sizeof(int));
    // ... usa data ...
    // ← Manca free(data)!
}

// Ogni chiamata a process_data() perde 4KB di memoria!
```

**Fix:**
```c
// ✅ CORRETTO
void process_data() {
    int *data = malloc(1000 * sizeof(int));
    if (data == NULL) return;

    // ... usa data ...

    free(data);
}
```

---

**Causa #2: Early return senza free**

```c
// ❌ MEMORY LEAK
int process(const char *filename) {
    char *buffer = malloc(1024);

    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        return -1;  // ← Leak! buffer non liberato
    }

    // ... processa ...

    fclose(fp);
    free(buffer);
    return 0;
}
```

**Fix:**
```c
// ✅ CORRETTO - Metodo 1: Free prima di ogni return
int process(const char *filename) {
    char *buffer = malloc(1024);
    if (buffer == NULL) return -1;

    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        free(buffer);  // ← Free prima di return
        return -1;
    }

    // ... processa ...

    fclose(fp);
    free(buffer);
    return 0;
}

// ✅ CORRETTO - Metodo 2: Goto cleanup pattern
int process(const char *filename) {
    char *buffer = NULL;
    FILE *fp = NULL;
    int result = -1;

    buffer = malloc(1024);
    if (buffer == NULL) goto cleanup;

    fp = fopen(filename, "r");
    if (fp == NULL) goto cleanup;

    // ... processa ...

    result = 0;

cleanup:
    if (buffer != NULL) free(buffer);
    if (fp != NULL) fclose(fp);
    return result;
}
```

---

**Causa #3: Leak in strutture complesse**

```c
// ❌ MEMORY LEAK
typedef struct {
    char *name;
    int *data;
} Record;

Record* create_record() {
    Record *rec = malloc(sizeof(Record));
    rec->name = malloc(100);
    rec->data = malloc(10 * sizeof(int));
    return rec;
}

// Uso:
Record *r = create_record();
free(r);  // ← Libera solo struct, ma non name e data! LEAK!
```

**Fix:**
```c
// ✅ CORRETTO
void free_record(Record *rec) {
    if (rec == NULL) return;

    free(rec->name);  // Prima i membri
    free(rec->data);
    free(rec);  // Poi la struct
}

// Uso:
Record *r = create_record();
free_record(r);
```

---

**Tool: Valgrind per trovare leak**

```bash
gcc -g program.c -o program
valgrind --leak-check=full ./program

# Output:
# ==12345== HEAP SUMMARY:
# ==12345==     in use at exit: 100 bytes in 1 blocks
# ==12345==   total heap usage: 2 allocs, 1 frees, 100 bytes allocated
# ==12345==
# ==12345== 100 bytes in 1 blocks are definitely lost
# ==12345==    at malloc (vg_replace_malloc.c:309)
# ==12345==    by create_record (program.c:15)
```

### 3.3 Dangling Pointer e Double Free

**Dangling Pointer:**

Puntatore che riferisce a memoria già liberata.

```c
// ❌ DANGLING POINTER
int *ptr = malloc(sizeof(int));
*ptr = 42;
free(ptr);

// ptr ora è "dangling" - punta a memoria non valida

*ptr = 100;  // ← Use-after-free! Undefined behavior!
printf("%d\n", *ptr);  // ← Può stampare qualunque cosa o crashare
```

**Fix:**
```c
// ✅ CORRETTO
int *ptr = malloc(sizeof(int));
*ptr = 42;
free(ptr);
ptr = NULL;  // ← Marca come invalido

if (ptr != NULL) {
    *ptr = 100;  // Non eseguito
}
```

---

**Double Free:**

Chiamare `free()` due volte sullo stesso puntatore.

```c
// ❌ DOUBLE FREE
int *ptr = malloc(sizeof(int));
free(ptr);
free(ptr);  // ← CRASH! Double free!
```

**Perché è pericoloso:**
- Corrompe lo heap manager interno
- Può causare crash imprevedibili
- Vulnerabilità di sicurezza

**Fix:**
```c
// ✅ CORRETTO
int *ptr = malloc(sizeof(int));
free(ptr);
ptr = NULL;

free(ptr);  // free(NULL) è sicuro e non fa nulla
```

### 3.4 Use-After-Free

**Definizione:**

Usare memoria dopo averla liberata.

**Esempio pericoloso:**

```c
// ❌ USE-AFTER-FREE
typedef struct Node {
    int value;
    struct Node *next;
} Node;

void remove_node(Node **head) {
    if (*head == NULL) return;

    Node *temp = *head;
    *head = (*head)->next;
    free(temp);

    printf("Removed: %d\n", temp->value);  // ← Use-after-free!
}
```

**Fix:**
```c
// ✅ CORRETTO
void remove_node(Node **head) {
    if (*head == NULL) return;

    Node *temp = *head;
    int value = temp->value;  // ← Salva valore PRIMA di free

    *head = (*head)->next;
    free(temp);

    printf("Removed: %d\n", value);  // ← Usa valore salvato
}
```

---

## 4. PUNTATORI E SICUREZZA (15 minuti)

### 4.1 Dereferenziare NULL

**Problema #1: Null Pointer Dereference**

```c
// ❌ CRASH
int *ptr = NULL;
*ptr = 42;  // ← Segmentation fault!
```

**Sempre controllare:**

```c
// ✅ CORRETTO
int *ptr = malloc(sizeof(int));
if (ptr != NULL) {
    *ptr = 42;
    free(ptr);
} else {
    fprintf(stderr, "Memory allocation failed\n");
}
```

**Pattern: Defensive programming**

```c
void process_data(int *data, size_t size) {
    // Valida parametri ALL'INIZIO
    if (data == NULL) {
        fprintf(stderr, "Error: NULL data pointer\n");
        return;
    }

    if (size == 0) {
        fprintf(stderr, "Error: Zero size\n");
        return;
    }

    // Ora è sicuro usare data
    for (size_t i = 0; i < size; i++) {
        data[i] = 0;
    }
}
```

### 4.2 Array Bounds Checking

**Problema: Accesso fuori dai limiti**

```c
int arr[10];

// ❌ PERICOLOSO
for (int i = 0; i <= 10; i++) {  // <= invece di <
    arr[i] = 0;  // arr[10] è fuori bounds!
}
```

**C NON controlla bounds automaticamente!**

A differenza di linguaggi come Python o Java, C ti permette di accedere oltre array → undefined behavior.

**Come proteggersi:**

```c
// ✅ CORRETTO
#define ARRAY_SIZE 10
int arr[ARRAY_SIZE];

for (int i = 0; i < ARRAY_SIZE; i++) {  // <, non <=
    arr[i] = 0;
}

// Oppure con sizeof:
for (size_t i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
    arr[i] = 0;
}
```

**Macro utile:**

```c
#define ARRAY_LENGTH(arr) (sizeof(arr) / sizeof((arr)[0]))

int arr[10];
for (size_t i = 0; i < ARRAY_LENGTH(arr); i++) {
    arr[i] = 0;
}
```

### 4.3 Pointer Arithmetic Pericoloso

**Aritmetica dei puntatori è potente ma pericolosa:**

```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;

printf("%d\n", *ptr);      // 1
printf("%d\n", *(ptr+1));  // 2
printf("%d\n", *(ptr+2));  // 3

// ❌ PERICOLOSO
printf("%d\n", *(ptr+10)); // Fuori bounds! Undefined behavior!
```

**Best practice:**

```c
// ✅ CORRETTO - Controlla bounds
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;
int *end = arr + 5;

while (ptr < end) {  // Sicuro: controlla di non superare fine
    printf("%d\n", *ptr);
    ptr++;
}
```

### 4.4 Const Correctness

**Usa `const` per indicare intent:**

```c
// ✅ BUONA PRATICA
void print_array(const int *arr, size_t size) {
//               ^^^^^
// const indica: questa funzione NON modificherà arr

    for (size_t i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

// Se provi a modificare:
void print_array(const int *arr, size_t size) {
    arr[0] = 999;  // ← Errore di compilazione!
}
```

**Livelli di const:**

```c
const int *ptr;        // Puntatore a int costante
                       // Puoi cambiare ptr, non *ptr

int * const ptr;       // Puntatore costante a int
                       // Puoi cambiare *ptr, non ptr

const int * const ptr; // Entrambi costanti
                       // Non puoi cambiare né ptr né *ptr
```

**Best practice:**

> **Usa `const` ovunque possibile. Il compilatore ti aiuterà a prevenire bug.**

---

---

# PARTE 2: PRATICA (60 MINUTI)

---

## 5. WORKSHOP VALGRIND (20 minuti)

### 5.1 Installazione Valgrind

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install valgrind
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install valgrind
```

**macOS:**
```bash
brew install valgrind
```

**Windows:**
Valgrind non è disponibile nativamente su Windows. Alternative:
- **Dr. Memory:** https://drmemory.org/
- **WSL (Windows Subsystem for Linux):** Installa Valgrind in WSL

### 5.2 Uso Base - Memory Leak Detection

**Esempio di programma con leak:**

```c
// leak_example.c
#include <stdlib.h>

int main() {
    int *arr1 = malloc(100 * sizeof(int));
    // ... usa arr1 ...

    int *arr2 = malloc(50 * sizeof(int));
    free(arr2);  // Questa è liberata

    // ← Manca free(arr1)! LEAK!

    return 0;
}
```

**Compila con debug symbols:**

```bash
gcc -g leak_example.c -o leak_example
```

**Esegui con Valgrind:**

```bash
valgrind --leak-check=full --show-leak-kinds=all ./leak_example
```

**Output:**

```
==12345== Memcheck, a memory error detector
==12345== HEAP SUMMARY:
==12345==     in use at exit: 400 bytes in 1 blocks
==12345==   total heap usage: 2 allocs, 1 frees, 600 bytes allocated
==12345==
==12345== 400 bytes in 1 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck.so)
==12345==    by 0x108654: main (leak_example.c:4)
==12345==
==12345== LEAK SUMMARY:
==12345==    definitely lost: 400 bytes in 1 blocks
==12345==    indirectly lost: 0 bytes in 0 blocks
==12345==      possibly lost: 0 bytes in 0 blocks
==12345==    still reachable: 0 bytes in 0 blocks
==12345==         suppressed: 0 bytes in 0 blocks
```

**Interpretazione:**

- **definitely lost:** Memory leak confermato (400 byte)
- **at malloc ... by main (leak_example.c:4):** Allocazione alla linea 4
- **1 allocs, 1 frees:** 2 allocazioni, solo 1 liberata

**Fix:**

```c
// leak_example_fixed.c
#include <stdlib.h>

int main() {
    int *arr1 = malloc(100 * sizeof(int));
    int *arr2 = malloc(50 * sizeof(int));

    free(arr2);
    free(arr1);  // ← Aggiunto!

    return 0;
}
```

**Verifica fix:**

```bash
gcc -g leak_example_fixed.c -o leak_example_fixed
valgrind --leak-check=full ./leak_example_fixed

# Output:
# ==12346== HEAP SUMMARY:
# ==12346==     in use at exit: 0 bytes in 0 blocks
# ==12346==   total heap usage: 2 allocs, 2 frees, 600 bytes allocated
# ==12346==
# ==12346== All heap blocks were freed -- no leaks are possible
```

✅ **Perfetto! Nessun leak.**

### 5.3 Invalid Memory Access

**Esempio: Accesso fuori bounds**

```c
// invalid_access.c
#include <stdlib.h>

int main() {
    int *arr = malloc(10 * sizeof(int));

    for (int i = 0; i <= 10; i++) {  // <= (dovrebbe essere <)
        arr[i] = i;  // arr[10] è fuori bounds!
    }

    free(arr);
    return 0;
}
```

**Valgrind output:**

```
==12347== Invalid write of size 4
==12347==    at 0x108678: main (invalid_access.c:7)
==12347==  Address 0x522d068 is 0 bytes after a block of size 40 alloc'd
==12347==    at 0x4C2FB0F: malloc (in /usr/lib/valgrind/vgpreload_memcheck.so)
==12347==    by 0x108654: main (invalid_access.c:4)
```

**Significato:**
- **Invalid write of size 4:** Scrittura invalida di 4 byte (sizeof(int))
- **0 bytes after a block:** Scritto immediatamente DOPO il blocco allocato

**Fix:**
```c
for (int i = 0; i < 10; i++) {  // < invece di <=
    arr[i] = i;
}
```

### 5.4 Use-After-Free Detection

**Esempio:**

```c
// use_after_free.c
#include <stdlib.h>
#include <stdio.h>

int main() {
    int *ptr = malloc(sizeof(int));
    *ptr = 42;

    free(ptr);

    printf("%d\n", *ptr);  // ← Use-after-free!

    return 0;
}
```

**Valgrind output:**

```
==12348== Invalid read of size 4
==12348==    at 0x10867C: main (use_after_free.c:9)
==12348==  Address 0x522d040 is 0 bytes inside a block of size 4 free'd
==12348==    at 0x4C30D3B: free (in /usr/lib/valgrind/vgpreload_memcheck.so)
==12348==    by 0x108675: main (use_after_free.c:7)
```

**Significato:**
- **Invalid read:** Lettura da memoria già liberata
- **inside a block ... free'd:** Blocco è stato liberato alla linea 7

### 5.5 Esercizio Guidato

**Ti do questo codice. Trova tutti gli errori con Valgrind:**

```c
// exercise.c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
    int age;
} Person;

Person* create_person(const char *name, int age) {
    Person *p = malloc(sizeof(Person));
    p->name = malloc(strlen(name));  // ← Bug #1?
    strcpy(p->name, name);
    p->age = age;
    return p;
}

int main() {
    Person *p1 = create_person("Alice", 30);
    Person *p2 = create_person("Bob", 25);

    free(p1);  // ← Bug #2?
    free(p2);  // ← Bug #3?

    return 0;
}
```

**Compila ed esegui con Valgrind:**

```bash
gcc -g exercise.c -o exercise
valgrind --leak-check=full ./exercise
```

<details>
<summary>Clicca per vedere i bug</summary>

**Bug #1:** `malloc(strlen(name))` - Manca +1 per null terminator!
```c
p->name = malloc(strlen(name) + 1);  // ← Fix
```

**Bug #2 e #3:** `free(p1)` e `free(p2)` liberano solo la struct, non `p->name`!

**Fix completo:**

```c
void free_person(Person *p) {
    if (p == NULL) return;
    free(p->name);  // Prima libera membri
    free(p);        // Poi libera struct
}

int main() {
    Person *p1 = create_person("Alice", 30);
    Person *p2 = create_person("Bob", 25);

    free_person(p1);
    free_person(p2);

    return 0;
}
```

</details>

---

## 6. CORREGGERE CODICE IA PERICOLOSO (20 minuti)

### 6.1 Esercizio #1: Codice con Memory Leak

**L'IA ha generato questo codice:**

```c
#include <stdio.h>
#include <stdlib.h>

int* read_numbers(const char *filename, int *count) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        return NULL;
    }

    int *numbers = malloc(100 * sizeof(int));
    *count = 0;

    while (fscanf(fp, "%d", &numbers[*count]) == 1) {
        (*count)++;
        if (*count >= 100) break;
    }

    fclose(fp);
    return numbers;
}

int main() {
    int count;
    int *data = read_numbers("numbers.txt", &count);

    if (data != NULL) {
        for (int i = 0; i < count; i++) {
            printf("%d ", data[i]);
        }
        printf("\n");
    }

    return 0;  // ← Bug: manca free(data)!
}
```

**Task:**
1. Identifica il/i bug
2. Correggilo
3. Verifica con Valgrind

<details>
<summary>Soluzione</summary>

**Bug:** Manca `free(data)` nel main.

**Fix:**

```c
int main() {
    int count;
    int *data = read_numbers("numbers.txt", &count);

    if (data != NULL) {
        for (int i = 0; i < count; i++) {
            printf("%d ", data[i]);
        }
        printf("\n");
        free(data);  // ← Fix
    }

    return 0;
}
```

</details>

### 6.2 Esercizio #2: Buffer Overflow

**L'IA ha generato questo codice:**

```c
#include <stdio.h>
#include <string.h>

void format_name(char *output, const char *first, const char *last) {
    strcpy(output, first);
    strcat(output, " ");
    strcat(output, last);
}

int main() {
    char full_name[20];
    format_name(full_name, "Christopher", "Montgomery");
    printf("%s\n", full_name);
    return 0;
}
```

**Task:**
1. Identifica vulnerabilità
2. Calcola quanti byte servono per "Christopher Montgomery"
3. Cosa succede?
4. Correggi il codice

<details>
<summary>Soluzione</summary>

**Vulnerabilità:** Buffer overflow

**Calcolo:**
- "Christopher" = 11 char
- " " = 1 char
- "Montgomery" = 10 char
- Null terminator = 1 char
- **Totale = 23 byte**

Ma `full_name[20]` ha solo 20 byte! **OVERFLOW di 3 byte!**

**Fix:**

```c
#include <stdio.h>
#include <string.h>

void format_name(char *output, size_t output_size,
                 const char *first, const char *last) {
    if (output == NULL || first == NULL || last == NULL) {
        return;
    }

    snprintf(output, output_size, "%s %s", first, last);
}

int main() {
    char full_name[50];  // Aumentato dimensione
    format_name(full_name, sizeof(full_name),
                "Christopher", "Montgomery");
    printf("%s\n", full_name);
    return 0;
}
```

</details>

### 6.3 Esercizio #3: Use-After-Free

**L'IA ha generato questo codice:**

```c
#include <stdlib.h>
#include <stdio.h>

int* get_max_pointer(int *arr, int size) {
    int max_index = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] > arr[max_index]) {
            max_index = i;
        }
    }
    return &arr[max_index];
}

int main() {
    int *numbers = malloc(5 * sizeof(int));
    numbers[0] = 10;
    numbers[1] = 50;
    numbers[2] = 30;
    numbers[3] = 90;
    numbers[4] = 20;

    int *max_ptr = get_max_pointer(numbers, 5);

    free(numbers);

    printf("Max value: %d\n", *max_ptr);  // ← Use-after-free!

    return 0;
}
```

**Task:**
1. Identifica il problema
2. Perché è pericoloso?
3. Proponi 2 fix diversi

<details>
<summary>Soluzione</summary>

**Problema:** `max_ptr` punta dentro `numbers`, che viene liberato. Poi `*max_ptr` accede memoria liberata.

**Fix #1: Salva valore, non puntatore**

```c
int get_max_value(int *arr, int size) {  // Ritorna int, non int*
    int max_index = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] > arr[max_index]) {
            max_index = i;
        }
    }
    return arr[max_index];  // Ritorna valore
}

int main() {
    int *numbers = malloc(5 * sizeof(int));
    // ... inizializza ...

    int max_value = get_max_value(numbers, 5);  // Salva valore

    free(numbers);

    printf("Max value: %d\n", max_value);  // Sicuro!

    return 0;
}
```

**Fix #2: Non liberare fino a dopo l'uso**

```c
int main() {
    int *numbers = malloc(5 * sizeof(int));
    // ... inizializza ...

    int *max_ptr = get_max_pointer(numbers, 5);

    printf("Max value: %d\n", *max_ptr);  // Usa PRIMA di free

    free(numbers);  // Libera DOPO

    return 0;
}
```

</details>

---

## 7. PROGETTO: SISTEMA GESTIONE DATI SICURO (15 minuti)

### 7.1 Specifica

**Implementa una struttura dati "dynamic array" sicura con l'IA.**

**Requisiti:**

```c
typedef struct {
    int *data;
    size_t size;      // Elementi correnti
    size_t capacity;  // Capacità allocata
} DynamicArray;

// Funzioni da implementare:
DynamicArray* da_create(size_t initial_capacity);
int da_append(DynamicArray *arr, int value);
int da_get(const DynamicArray *arr, size_t index, int *out_value);
void da_free(DynamicArray *arr);
```

**Vincoli:**
- Memory-safe (nessun leak)
- Controllo errori su tutti i parametri
- Espansione automatica quando capacity raggiunta
- Valgrind-clean (zero errori)

### 7.2 Implementazione Guidata

**Step 1: Chiedi all'IA**

**Prompt consigliato:**

```
Scrivi una implementazione di dynamic array in C con le seguenti specifiche:

[CONTEXT]
Sono uno studente ITS. Sto imparando gestione memoria sicura.

[TASK]
Implementa una struttura DynamicArray con funzioni:
- create: alloca array con capacità iniziale
- append: aggiunge elemento (espande se necessario)
- get: ottiene elemento a indice (con controllo bounds)
- free: libera tutta la memoria

[REQUISITI SICUREZZA]
- Controlla TUTTI i puntatori NULL
- Controlla TUTTI i malloc failures
- Nessun memory leak
- Nessun buffer overflow
- Usa size_t per dimensioni

[OUTPUT]
- Codice completo con commenti
- Gestione errori (ritorna codice errore)
- Main con esempio d'uso
- Include controlli per Valgrind
```

**Step 2: Valida l'output**

Controlla che l'IA abbia incluso:
- [ ] Controllo NULL su tutti i puntatori
- [ ] Controllo malloc failures
- [ ] Free di tutti i membri in da_free
- [ ] Controllo bounds in da_get
- [ ] Espansione corretta in da_append

**Step 3: Compila e testa con Valgrind**

```bash
gcc -g -Wall -Wextra dynamic_array.c -o dynamic_array
valgrind --leak-check=full ./dynamic_array
```

**Step 4: Se Valgrind trova errori**

Usa questo prompt:

```
Valgrind ha riportato questo errore nel mio codice:

[incolla output Valgrind]

Ecco il codice:

[incolla codice]

Analizza usando Chain-of-Thought:
1. Cosa significa l'errore Valgrind?
2. A quale linea di codice si riferisce?
3. Qual è la causa root?
4. Come posso fixare?
```

### 7.3 Esempio di Implementazione Corretta

<details>
<summary>Clicca per vedere implementazione di riferimento</summary>

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} DynamicArray;

/**
 * @brief Crea un nuovo dynamic array
 * @param initial_capacity Capacità iniziale
 * @return Puntatore al dynamic array, o NULL se errore
 */
DynamicArray* da_create(size_t initial_capacity) {
    if (initial_capacity == 0) {
        initial_capacity = 10;  // Default
    }

    DynamicArray *arr = malloc(sizeof(DynamicArray));
    if (arr == NULL) {
        return NULL;
    }

    arr->data = malloc(initial_capacity * sizeof(int));
    if (arr->data == NULL) {
        free(arr);
        return NULL;
    }

    arr->size = 0;
    arr->capacity = initial_capacity;
    return arr;
}

/**
 * @brief Aggiunge elemento alla fine
 * @return 0 se successo, -1 se errore
 */
int da_append(DynamicArray *arr, int value) {
    if (arr == NULL) {
        return -1;
    }

    // Espandi se necessario
    if (arr->size >= arr->capacity) {
        size_t new_capacity = arr->capacity * 2;

        int *new_data = realloc(arr->data, new_capacity * sizeof(int));
        if (new_data == NULL) {
            return -1;  // realloc fallito
        }

        arr->data = new_data;
        arr->capacity = new_capacity;
    }

    arr->data[arr->size] = value;
    arr->size++;
    return 0;
}

/**
 * @brief Ottiene elemento a indice
 * @return 0 se successo, -1 se errore
 */
int da_get(const DynamicArray *arr, size_t index, int *out_value) {
    if (arr == NULL || out_value == NULL) {
        return -1;
    }

    if (index >= arr->size) {
        return -1;  // Out of bounds
    }

    *out_value = arr->data[index];
    return 0;
}

/**
 * @brief Libera memoria
 */
void da_free(DynamicArray *arr) {
    if (arr == NULL) {
        return;
    }

    free(arr->data);
    free(arr);
}

// Test
int main() {
    DynamicArray *arr = da_create(5);
    if (arr == NULL) {
        fprintf(stderr, "Failed to create array\n");
        return 1;
    }

    // Aggiungi elementi
    for (int i = 0; i < 10; i++) {
        if (da_append(arr, i * 10) != 0) {
            fprintf(stderr, "Failed to append\n");
            da_free(arr);
            return 1;
        }
    }

    // Leggi elementi
    for (size_t i = 0; i < 10; i++) {
        int value;
        if (da_get(arr, i, &value) == 0) {
            printf("%d ", value);
        }
    }
    printf("\n");

    da_free(arr);
    return 0;
}
```

</details>

---

## 8. BEST PRACTICES E CHECKLIST (5 minuti)

### 8.1 Checklist di Sicurezza Memoria

**Prima di considerare codice "completo", verifica:**

**✅ Allocazione:**
- [ ] Ogni `malloc/calloc/realloc` ha controllo NULL
- [ ] Size argument corretto (es: `n * sizeof(type)`, non solo `n`)
- [ ] Controllo overflow in calcolo size (`n > SIZE_MAX / sizeof(type)`)

**✅ Uso:**
- [ ] Nessun accesso oltre array bounds
- [ ] Nessun dereference di NULL
- [ ] Const correctness (parametri read-only sono `const`)

**✅ Liberazione:**
- [ ] Ogni `malloc` ha corrispondente `free`
- [ ] Free in TUTTI i percorsi (inclusi error paths)
- [ ] Strutture complesse: free membri prima di struct
- [ ] Dopo free: puntatore settato a NULL

**✅ Stringhe:**
- [ ] Nessuna funzione pericolosa (gets, strcpy, sprintf)
- [ ] Sempre limiti espliciti (fgets, strncpy, snprintf)
- [ ] Spazio per null terminator (+1)
- [ ] Null termination garantita

**✅ Testing:**
- [ ] Compila con `-Wall -Wextra -Werror`
- [ ] Valgrind clean (zero errori, zero leak)
- [ ] Test edge cases (NULL, size=0, molto grandi)

### 8.2 Pattern Anti-Bug

**Pattern #1: Goto Cleanup**

```c
int function() {
    char *buffer = NULL;
    FILE *fp = NULL;
    int result = -1;

    buffer = malloc(1024);
    if (buffer == NULL) goto cleanup;

    fp = fopen("file.txt", "r");
    if (fp == NULL) goto cleanup;

    // ... logica ...

    result = 0;  // Success

cleanup:
    if (buffer) free(buffer);
    if (fp) fclose(fp);
    return result;
}
```

**Pattern #2: Macro sicure**

```c
// Free e setta NULL
#define SAFE_FREE(ptr) do { \
    free(ptr); \
    (ptr) = NULL; \
} while(0)

// Uso:
int *arr = malloc(100 * sizeof(int));
SAFE_FREE(arr);  // arr ora è NULL
```

**Pattern #3: Wrapper allocation**

```c
void* safe_malloc(size_t size) {
    void *ptr = malloc(size);
    if (ptr == NULL) {
        fprintf(stderr, "Fatal: out of memory\n");
        exit(1);
    }
    return ptr;
}

// Uso (se OOM è fatale):
int *arr = safe_malloc(100 * sizeof(int));  // O succede o exit
```

---

## 🎯 RIEPILOGO LEZIONE 3

### Cosa Abbiamo Imparato

**Teoria:**
- ✅ 10 trappole comuni del codice IA
- ✅ Buffer overflow e funzioni pericolose
- ✅ Gestione memoria: malloc/free, leak, dangling pointer
- ✅ Best practices per sicurezza puntatori

**Pratica:**
- ✅ Uso di Valgrind per debug memoria
- ✅ Correzione di codice IA pericoloso
- ✅ Implementazione dynamic array memory-safe
- ✅ Checklist e pattern anti-bug

### Key Takeaways

1. **L'IA sbaglia spesso in C** (gestione memoria, edge cases)
2. **SEMPRE validare** con compilatore + Valgrind
3. **Funzioni pericolose** (gets, strcpy) → mai usare
4. **Ogni malloc → free** (in TUTTI i percorsi)
5. **Valgrind è tuo amico** (usalo sempre)

---

## 📚 COMPITI PER CASA

### Esercizio 1: Bug Hunt

Trova e fixa tutti i bug (sono 8!) in questo codice:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
    int *scores;
    int num_scores;
} Student;

Student* create_student(char *name, int num_scores) {
    Student *s = malloc(sizeof(Student));
    s->name = malloc(strlen(name));
    strcpy(s->name, name);
    s->scores = malloc(num_scores * sizeof(int));
    s->num_scores = num_scores;
    return s;
}

int main() {
    Student *alice = create_student("Alice", 5);

    for (int i = 0; i <= alice->num_scores; i++) {
        alice->scores[i] = i * 10;
    }

    free(alice);
    return 0;
}
```

### Esercizio 2: Valgrind Master

Scrivi 3 programmi con bug intenzionali:
1. Programma con memory leak
2. Programma con buffer overflow
3. Programma con use-after-free

Poi usa Valgrind per identificarli e fixarli.

### Esercizio 3: Libreria Sicura

Implementa una libreria di "safe string functions":
- `safe_strdup(const char *s)`
- `safe_strcat(char *dest, size_t dest_size, const char *src)`
- `safe_sprintf(char *buf, size_t buf_size, const char *fmt, ...)`

Tutti con gestione errori completa e Valgrind-clean.

---

## 🎓 PROSSIMA LEZIONE

**LEZIONE 4: Gestione Progetti e Documentazione**

**Anteprima:**
- Metodologia di progetto con IA
- Workflow professionale
- Documentazione tecnica (README, commenti)
- Git e version control
- Best practices sviluppo collaborativo

---

**Fine Lezione 3**

**🔒 Ora sai scrivere codice C sicuro e robusto con l'IA!**

**Ricorda:**
> "Il codice che non crasha con input normali è facile. Il codice che gestisce edge cases e non ha leak è professionale."

**Ottimo lavoro! Continua a praticare! 💻✨**