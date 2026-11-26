# Le stringhe in C

*Dispensa didattica per lo studio della creazione, gestione e manipolazione delle stringhe*

---

## Indice

1. Che cos'è una stringa in C
2. Il terminatore '\\0'
3. Dichiarare e inizializzare una stringa
4. Stringhe e puntatori: attenzione alla differenza
5. Input e output di stringhe
6. Scorrere una stringa carattere per carattere
7. La libreria string.h
8. La libreria ctype.h
9. Conversioni tra stringhe e numeri
10. Esempi completi di manipolazione
11. Array di stringhe
12. Gli errori più comuni
13. Esercizi

---

## 1. Che cos'è una stringa in C

In molti linguaggi (Python, Java, JavaScript) esiste un tipo di dato apposito per il testo, chiamato `string`. **In C questo tipo non esiste.**

In C una **stringa è semplicemente un array di caratteri (`char`) che termina con un carattere speciale**, chiamato *terminatore*.

Per capire bene il concetto, ricordiamo prima due cose:

- un `char` è una variabile che contiene **un solo carattere** (per esempio `'a'`, `'7'`, `'?'`). Si scrive tra **apici singoli**;
- un array è un insieme di variabili dello stesso tipo, messe una dopo l'altra in memoria.

Una stringa, quindi, è una sequenza di `char` messi uno dopo l'altro. Si scrive tra **apici doppi**: `"ciao"`.

> **Attenzione alla differenza:** `'a'` è un carattere singolo, `"a"` è una stringa (contiene la lettera a più il terminatore).

---

## 2. Il terminatore '\\0'

Quando scriviamo una stringa, come fa il computer a sapere dove finisce? Un array in C non conosce la propria lunghezza. Per questo motivo si usa una convenzione: **l'ultimo carattere di una stringa è sempre il carattere nullo, scritto `'\0'`**, il cui codice ASCII vale 0.

La stringa `"ciao"` in memoria è fatta così:

| posizione | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| contenuto | 'c' | 'i' | 'a' | 'o' | '\\0' |

Le parole sono 4 lettere, ma servono **5 celle** di memoria. Questa è la regola da ricordare:

> **Per memorizzare una stringa di N caratteri servono N + 1 celle**, perché l'ultima è occupata dal terminatore.

Tutte le funzioni che lavorano sulle stringhe (`printf`, `strlen`, `strcpy`...) cominciano a leggere dall'inizio e **si fermano quando trovano `'\0'`**. Se il terminatore manca, queste funzioni continuano a leggere la memoria oltre la stringa, fino a trovare per caso uno zero: il risultato sono caratteri strani, errori o crash del programma.

**Lunghezza e dimensione non sono la stessa cosa.** Se dichiariamo un array di 20 caratteri e dentro ci mettiamo `"ciao"`:

- la **dimensione** dell'array è 20 (lo spazio disponibile);
- la **lunghezza** della stringa è 4 (i caratteri prima del terminatore).

Le celle dopo il terminatore esistono ancora, ma sono ignorate.

---

## 3. Dichiarare e inizializzare una stringa

Ci sono diversi modi per creare una stringa. Vediamoli uno per uno.

### 3.1 Dichiarazione senza valore iniziale

```c
char nome[20];
```

Si riserva spazio per 20 caratteri, quindi per una stringa lunga **al massimo 19 caratteri** (il ventesimo posto serve per il terminatore). Il contenuto iniziale è **casuale**: finché non ci scriviamo qualcosa, non è una stringa valida.

### 3.2 Inizializzazione con una stringa tra apici doppi

```c
char saluto[20] = "ciao";
```

Il compilatore copia le lettere `c`, `i`, `a`, `o` nelle prime 4 celle e **aggiunge da solo il terminatore**. Le celle rimanenti vengono riempite con `'\0'`.

### 3.3 Dimensione lasciata calcolare al compilatore

```c
char saluto[] = "ciao";
```

Se lasciamo vuote le parentesi quadre, il compilatore conta le lettere e crea un array di **5 celle** (4 lettere + terminatore). È comodo, ma poi l'array **non si può allungare**: non potremo mai metterci dentro una parola più lunga di 4 lettere.

### 3.4 Inizializzazione carattere per carattere

```c
char saluto[5] = {'c', 'i', 'a', 'o', '\0'};
```

È il modo "faticoso" e serve solo per capire cosa succede davvero. Qui il terminatore **va scritto a mano**: se lo dimentichiamo, non otteniamo una stringa ma un semplice array di caratteri.

### 3.5 Il grande errore: assegnare una stringa dopo la dichiarazione

```c
char nome[20];
nome = "Mario";     // ERRORE! Non compila
```

In C **non si può assegnare un array con l'operatore `=`** dopo averlo dichiarato. L'uguale funziona solo nel momento della dichiarazione (punti 3.2 e 3.3). Per copiare una stringa in un array già esistente si usa la funzione `strcpy` (vedi paragrafo 7).

---

## 4. Stringhe e puntatori: attenzione alla differenza

Esiste un altro modo di scrivere una stringa, con un puntatore:

```c
char *p = "ciao";
```

Sembra uguale a `char saluto[] = "ciao";`, ma **non lo è**:

|  | `char s[] = "ciao";` | `char *p = "ciao";` |
| --- | --- | --- |
| Cosa è | un array con una **copia** modificabile | un puntatore a una stringa **costante** |
| Posso modificare le lettere? | Sì: `s[0] = 'C';` | **No**: comportamento indefinito, spesso crash |
| Posso riassegnarla? | No | Sì: `p = "altro";` |

Regola pratica per i principianti: **se devi modificare la stringa, usa sempre un array** (`char s[...]`). Usa `char *` solo per stringhe che vuoi soltanto leggere, per esempio come parametro di una funzione.

---

## 5. Input e output di stringhe

### 5.1 Output

Per stampare una stringa si usa `printf` con il segnaposto **`%s`** (s come *string*):

```c
#include <stdio.h>

int main(void) {
    char nome[] = "Mario";
    printf("Ciao %s!\n", nome);
    return 0;
}
```

Output: `Ciao Mario!`

Esiste anche `puts(nome);`, che stampa la stringa e va a capo automaticamente.

### 5.2 Input con scanf

```c
char nome[20];
printf("Come ti chiami? ");
scanf("%s", nome);
```

Due osservazioni importanti:

1. **Non si mette la `&` davanti a `nome`**. Con i numeri scriviamo `scanf("%d", &eta)`, ma il nome di un array è già, di per sé, l'indirizzo della sua prima cella.
2. `scanf("%s", ...)` **si ferma al primo spazio**. Se l'utente scrive `Mario Rossi`, nell'array finisce solo `Mario`. Inoltre, se l'utente scrive più di 19 caratteri, `scanf` scrive **oltre la fine dell'array** (si chiama *buffer overflow*, un errore grave). Per limitare i caratteri letti si può scrivere:

```c
scanf("%19s", nome);   // legge al massimo 19 caratteri
```

Il numero deve essere **uguale alla dimensione meno 1**, per lasciare posto al terminatore.

### 5.3 Input di frasi intere con fgets

Per leggere una riga completa, spazi compresi, la funzione giusta è `fgets`:

```c
char frase[100];
printf("Scrivi una frase: ");
fgets(frase, sizeof(frase), stdin);
```

I tre parametri sono:

- `frase`: dove salvare il testo;
- `sizeof(frase)`: quanti byte al massimo può usare (così non si va mai fuori dall'array);
- `stdin`: da dove leggere (la tastiera).

`fgets` ha un comportamento da conoscere: **conserva il carattere di a capo `'\n'`** premuto con Invio. La stringa letta, scrivendo `ciao` e premendo Invio, è quindi `"ciao\n"`. Per eliminarlo si usa questa riga:

```c
frase[strcspn(frase, "\n")] = '\0';
```

Spiegazione: `strcspn` restituisce la posizione in cui compare `'\n'`; noi scriviamo in quella posizione un terminatore, accorciando così la stringa. (Serve `#include <string.h>`.)

---

## 6. Scorrere una stringa carattere per carattere

Siccome una stringa è un array, si accede a ogni lettera con l'indice tra parentesi quadre. **L'indice parte da 0.**

```c
char s[] = "ciao";
printf("%c\n", s[0]);   // stampa c
printf("%c\n", s[3]);   // stampa o
```

Per scorrere tutta la stringa, senza sapere quanto è lunga, si sfrutta il terminatore: **si continua finché il carattere corrente è diverso da `'\0'`**.

```c
char s[] = "ciao";
int i = 0;

while (s[i] != '\0') {
    printf("Lettera in posizione %d: %c\n", i, s[i]);
    i++;
}
```

Output:

```
Lettera in posizione 0: c
Lettera in posizione 1: i
Lettera in posizione 2: a
Lettera in posizione 3: o
```

Si può scrivere anche con un `for`, più compatto:

```c
for (int i = 0; s[i] != '\0'; i++) {
    printf("%c\n", s[i]);
}
```

Questo schema è **la base di tutta la manipolazione delle stringhe**: lo ritroveremo in quasi tutti gli esempi.

---

## 7. La libreria string.h

Il C offre una raccolta di funzioni già pronte per lavorare sulle stringhe. Per usarle bisogna scrivere in cima al programma:

```c
#include <string.h>
```

### 7.1 strlen: la lunghezza

```c
int n = strlen("ciao");   // n vale 4
```

`strlen` conta i caratteri **prima del terminatore** (il terminatore non viene contato). Fa esattamente ciò che abbiamo fatto con il `while` del paragrafo 6.

> Non confonderla con `sizeof`: `sizeof(s)` restituisce la dimensione dell'array, `strlen(s)` la lunghezza del testo contenuto.

### 7.2 strcpy: copiare una stringa

```c
char origine[] = "ciao";
char destinazione[20];

strcpy(destinazione, origine);   // copia origine dentro destinazione
```

L'ordine dei parametri è **(destinazione, origine)**: come in un'assegnazione, a sinistra c'è chi riceve. Copia anche il terminatore. **Attenzione**: `destinazione` deve essere abbastanza grande, altrimenti si scrive fuori dall'array.

Questa è la funzione che risolve il problema del punto 3.5:

```c
char nome[20];
strcpy(nome, "Mario");   // così funziona
```

### 7.3 strcat: unire (concatenare) due stringhe

```c
char s[30] = "buon";
strcat(s, "giorno");     // ora s contiene "buongiorno"
```

`strcat` cerca il terminatore della prima stringa e **da lì in poi** scrive la seconda. L'array di destinazione deve avere spazio sufficiente per il testo totale **più il terminatore**.

### 7.4 strcmp: confrontare due stringhe

Questo è uno dei punti in cui i principianti sbagliano di più. **Non si possono confrontare le stringhe con `==`**:

```c
if (a == b)   // SBAGLIATO: confronta gli indirizzi in memoria, non il testo
```

Si usa invece `strcmp`:

```c
if (strcmp(a, b) == 0) {
    printf("Le stringhe sono uguali\n");
}
```

La funzione restituisce:

| Valore restituito | Significato |
| --- | --- |
| `0` | le stringhe sono **uguali** |
| numero **negativo** | `a` viene **prima** di `b` in ordine alfabetico |
| numero **positivo** | `a` viene **dopo** `b` in ordine alfabetico |

Ricorda: **uguali = zero** (può sembrare al contrario, ma è così). Il confronto distingue maiuscole e minuscole: `"Ciao"` e `"ciao"` sono diverse.

### 7.5 strchr e strstr: cercare

```c
char *p = strchr("ciao", 'a');      // cerca un carattere
char *q = strstr("buongiorno", "giorno");  // cerca una sottostringa
```

Entrambe restituiscono un puntatore al punto in cui hanno trovato ciò che cercavano, oppure `NULL` se non c'è. Per ora ci basta usarle come "domanda":

```c
if (strstr(frase, "ciao") != NULL) {
    printf("La frase contiene la parola ciao\n");
}
```

### 7.6 Riepilogo

| Funzione | A cosa serve |
| --- | --- |
| `strlen(s)` | lunghezza della stringa |
| `strcpy(dest, src)` | copia `src` in `dest` |
| `strcat(dest, src)` | aggiunge `src` in fondo a `dest` |
| `strcmp(a, b)` | confronta (0 = uguali) |
| `strchr(s, c)` | cerca un carattere |
| `strstr(s, t)` | cerca una sottostringa |

---

## 8. La libreria ctype.h

Per lavorare sui **singoli caratteri** c'è un'altra libreria:

```c
#include <ctype.h>
```

Le funzioni più utili:

| Funzione | Cosa fa | Esempio |
| --- | --- | --- |
| `toupper(c)` | converte in maiuscolo | `toupper('a')` dà `'A'` |
| `tolower(c)` | converte in minuscolo | `tolower('A')` dà `'a'` |
| `isalpha(c)` | è una lettera? | `isalpha('x')` è vero |
| `isdigit(c)` | è una cifra? | `isdigit('7')` è vero |
| `isspace(c)` | è uno spazio? | `isspace(' ')` è vero |
| `isupper(c)` / `islower(c)` | è maiuscola / minuscola? |  |

Le funzioni di tipo `is...` restituiscono **zero se la risposta è no**, un valore diverso da zero se è sì, quindi si usano comodamente dentro un `if`.

---

## 9. Conversioni tra stringhe e numeri

La stringa `"123"` **non è il numero 123**: è una sequenza di tre caratteri. Per usarla nei calcoli bisogna convertirla. Serve `#include <stdlib.h>`.

```c
int n = atoi("123");        // da stringa a intero: n vale 123
double d = atof("3.14");    // da stringa a numero decimale
```

Per fare il contrario, cioè **scrivere un numero dentro una stringa**, si usa `snprintf`, che funziona come `printf` ma invece di stampare a video scrive dentro un array:

```c
char testo[50];
int eta = 17;
snprintf(testo, sizeof(testo), "Ho %d anni", eta);
// testo contiene "Ho 17 anni"
```

---

## 10. Esempi completi di manipolazione

Ora mettiamo insieme tutto con programmi completi. Per ogni esempio c'è la spiegazione di come funziona.

### Esempio 1: contare le vocali

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char frase[100];
    int vocali = 0;

    printf("Scrivi una frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        char c = tolower(frase[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vocali++;
        }
    }

    printf("Vocali trovate: %d\n", vocali);
    return 0;
}
```

**Come funziona:** il ciclo `for` scorre la stringa fino al terminatore. Per ogni lettera la convertiamo in minuscolo (così `A` e `a` vengono trattate allo stesso modo) e controlliamo se è una vocale. Se sì, incrementiamo il contatore.

### Esempio 2: trasformare in maiuscolo

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char s[] = "programmare in C";

    for (int i = 0; s[i] != '\0'; i++) {
        s[i] = toupper(s[i]);
    }

    printf("%s\n", s);   // PROGRAMMARE IN C
    return 0;
}
```

**Come funziona:** a ogni giro leggiamo la lettera `s[i]`, la convertiamo e la **riscriviamo nella stessa posizione**. Questo è possibile perché `s` è un array (vedi paragrafo 4): se fosse stato `char *s = "..."` il programma sarebbe andato in errore.

### Esempio 3: invertire una stringa

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "ciao";
    int n = strlen(s);

    for (int i = 0; i < n / 2; i++) {
        char temp = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = temp;
    }

    printf("%s\n", s);   // oaic
    return 0;
}
```

**Come funziona:** si scambiano la prima lettera con l'ultima, la seconda con la penultima, e così via. Basta arrivare **a metà** della stringa (`n / 2`): se andassimo fino alla fine, rifaremmo gli scambi al contrario e la stringa tornerebbe com'era. Per lo scambio serve una variabile d'appoggio, `temp`, altrimenti una delle due lettere andrebbe persa.

Ecco lo scambio passo per passo con `"ciao"` (n = 4):

| giro | i | scambio | stringa risultante |
| --- | --- | --- | --- |
| 1 | 0 | `s[0]` con `s[3]` | `oiac` |
| 2 | 1 | `s[1]` con `s[2]` | `oaic` |

### Esempio 4: verificare se una parola è palindroma

Una parola è palindroma se si legge uguale da sinistra a destra e da destra a sinistra (per esempio `anna`, `osso`).

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char parola[50];
    int palindroma = 1;   // partiamo supponendo che lo sia

    printf("Scrivi una parola: ");
    scanf("%49s", parola);

    int n = strlen(parola);
    for (int i = 0; i < n / 2; i++) {
        if (parola[i] != parola[n - 1 - i]) {
            palindroma = 0;   // trovata una differenza
        }
    }

    if (palindroma) {
        printf("%s e' palindroma\n", parola);
    } else {
        printf("%s non e' palindroma\n", parola);
    }
    return 0;
}
```

**Come funziona:** usiamo una variabile "bandiera" (`palindroma`) che vale 1 (vero). Confrontiamo la prima lettera con l'ultima, la seconda con la penultima, ecc. Appena troviamo due lettere diverse, abbassiamo la bandiera a 0. Alla fine basta guardare il valore della bandiera.

### Esempio 5: copiare una stringa "a mano"

Per capire cosa fa davvero `strcpy`, proviamo a scriverla noi:

```c
#include <stdio.h>

int main(void) {
    char origine[] = "ciao";
    char copia[20];
    int i = 0;

    while (origine[i] != '\0') {
        copia[i] = origine[i];
        i++;
    }
    copia[i] = '\0';   // IMPORTANTE: aggiungere il terminatore

    printf("%s\n", copia);
    return 0;
}
```

**Come funziona:** copiamo una lettera alla volta finché non arriviamo al terminatore dell'origine. Il ciclo si ferma **prima** di copiarlo, quindi dobbiamo scriverlo noi alla fine. Se dimentichiamo l'ultima riga, `copia` non è una stringa valida e `printf` stamperà caratteri casuali dopo `ciao`.

---

## 11. Array di stringhe

Per memorizzare più parole (per esempio i nomi di una classe) serve un **array di stringhe**, cioè una tabella con una riga per ogni parola.

```c
char nomi[3][20] = {"Anna", "Luca", "Giulia"};
```

Si legge così: **3 stringhe, ognuna lunga al massimo 19 caratteri**. Il primo indice sceglie la stringa, il secondo (se serve) la lettera.

```c
printf("%s\n", nomi[1]);      // Luca
printf("%c\n", nomi[1][0]);   // L
```

Per stamparle tutte:

```c
for (int i = 0; i < 3; i++) {
    printf("%d: %s\n", i, nomi[i]);
}
```

Per leggerle da tastiera:

```c
for (int i = 0; i < 3; i++) {
    printf("Nome %d: ", i + 1);
    scanf("%19s", nomi[i]);
}
```

---

## 12. Gli errori più comuni

| Errore | Perché è sbagliato | Come si corregge |
| --- | --- | --- |
| `char s[4] = "ciao";` | servono 5 celle: manca lo spazio per il terminatore | `char s[5]` oppure `char s[]` |
| `s = "ciao";` | un array non si assegna con `=` | `strcpy(s, "ciao");` |
| `if (a == b)` | confronta gli indirizzi, non il testo | `if (strcmp(a, b) == 0)` |
| `scanf("%s", &nome)` | la `&` non serve con gli array | `scanf("%s", nome)` |
| `scanf("%s", nome)` senza limite | può scrivere oltre la fine dell'array | `scanf("%19s", nome)` |
| dimenticare `'\0'` quando si costruisce la stringa a mano | la stringa non ha fine | scrivere `s[i] = '\0';` alla fine |
| `char *p = "ciao"; p[0] = 'C';` | si modifica una costante | usare `char p[] = "ciao";` |
| usare `'ciao'` con apici singoli | gli apici singoli sono per **un solo** carattere | usare `"ciao"` |

---

## 13. Esercizi

### Livello base

1. Dichiara una stringa con il tuo nome e stampala insieme alla sua lunghezza (usa `strlen`).
2. Chiedi all'utente una parola e stampala **una lettera per riga**.
3. Chiedi due parole e stampa se sono uguali oppure diverse (usa `strcmp`).
4. Chiedi una parola e stampala trasformata in **minuscolo**.

### Livello intermedio

5. Chiedi una frase con `fgets` e conta quante **cifre** contiene (usa `isdigit`).
6. Chiedi nome e cognome come due stringhe separate e uniscile in una sola con uno spazio in mezzo (usa `strcpy` e `strcat`). Stampa il risultato.
7. Chiedi una frase e stampala **al contrario**, senza modificare la stringa originale (scorri da `strlen(s) - 1` fino a 0).
8. Chiedi una frase e conta quante **parole** contiene (suggerimento: conta gli spazi e aggiungi 1).

### Livello avanzato

9. Scrivi un programma che legge 5 nomi in un array di stringhe e stampa il **più lungo**.
10. Scrivi la tua versione di `strlen` (una funzione che prende una stringa e restituisce la lunghezza) senza usare `string.h`.
11. Chiedi una frase e sostituisci ogni spazio con il carattere `'_'`.
12. Cifrario di Cesare: chiedi una parola in minuscolo e stampala spostando ogni lettera di 3 posizioni in avanti nell'alfabeto (`a` diventa `d`, `b` diventa `e`, ... `z` diventa `c`).

---

## Riepilogo finale: le 5 regole d'oro

1. Una stringa è un **array di `char` che finisce con `'\0'`**.
2. Per una stringa di N caratteri servono **N + 1 celle**.
3. Gli array **non si assegnano né si confrontano con `=` e `==`**: si usano `strcpy` e `strcmp`.
4. Per scorrere una stringa: `for (i = 0; s[i] != '\0'; i++)`.
5. Prima di scrivere in una stringa, controlla sempre che **lo spazio basti**.
