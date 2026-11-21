Dispensa ITS · Programmazione

# Programmare in C dai rudimenti alle librerie

78 esercizi a difficoltà crescente, ognuno con consegna, suggerimento e soluzione commentata. Ogni soluzione è stata compilata con `gcc -std=c11 -Wall -Wextra -pedantic` senza warning, e gli output riportati sono quelli reali.

**78**esercizi

**18**moduli

**6**parti

**C11**standard

[Introduzione](#intro)[Mappa](#mappa)[1](#m1)[2](#m2)[3](#m3)[4](#m4)[5](#m5)[6](#m6)[7](#m7)[8](#m8)[9](#m9)[10](#m10)[11](#m11)[12](#m12)[13](#m13)[14](#m14)[15](#m15)[16](#m16)[17](#m17)[18](#m18)[Appendice](#appendice)

## Prima di iniziare

La dispensa accompagna lo studente dal primo `printf` fino alla costruzione di una libreria riutilizzabile con il suo `Makefile`. Gli esercizi sono ordinati: ognuno usa solo concetti già introdotti, tranne pochi esercizi "ponte" segnalati nel commento. Le parti V e VI (algoritmi, strutture dati, approfondimenti) presuppongono i moduli 1-9 e si possono svolgere prima o dopo la parte IV. Le soluzioni sono nascoste: si aprono con **Mostra la soluzione** o tutte insieme dal pulsante nella barra in alto.

### 1 · L'ambiente di lavoro

#### Linux (Debian/Ubuntu)

```
# compilatore gcc, make e strumenti di base
$ sudo apt install build-essential
# verifica
$ gcc --version
```

#### Windows

Installare **MSYS2** (msys2.org), aprire il terminale *MSYS2 UCRT64* e digitare:

```
$ pacman -S mingw-w64-ucrt-x86_64-gcc make
```

L'eseguibile si chiama `prog.exe`; le librerie dinamiche sono file `.dll` invece di `.so`.

#### macOS

```
$ xcode-select --install
```

Il comando `gcc` richiama clang: opzioni e messaggi sono quasi identici.

#### OnlineGDB (nessuna installazione)

Compilatore e debugger nel browser su **onlinegdb.com**: copre 74 esercizi su 78 per intero e gli altri 4 in parte (vedi sotto). Ottimo per iniziare e per il debug passo-passo.

### 2 · Lavorare su OnlineGDB

1. Aprire **onlinegdb.com** e scegliere **C** nel menu *Language* in alto a destra.
2. Nelle impostazioni (icona a ingranaggio) scrivere in *Extra Compiler Flags*: `-Wall -Wextra -std=c11`. Così si ottengono gli stessi warning della dispensa.
3. Incollare il codice in `main.c` e premere **Run**. Quando il programma chiede un input, lo si digita nella console in basso (*Interactive Console*); in alternativa si sceglie *Text* e si scrive l'input in anticipo.
4. Per gli esercizi con più file (moduli 11-12) aggiungere ogni `.h` e `.c` con il pulsante **New File** a sinistra di Run: tutti i `.c` del progetto vengono compilati insieme. Lo stesso pulsante crea i file di dati (`testo.txt`, `dati.txt`).
5. Gli argomenti da riga di comando (`argv`, esercizi 10.3 e 12.3) si scrivono nel campo *Command line arguments*.
6. Con **Save** il progetto riceve un link da condividere: utile per consegnare un esercizio o chiedere aiuto.

Ogni esercizio porta un'etichetta: OnlineGDB: Sì si svolge per intero online; OnlineGDB: Parziale il codice gira online, ma i comandi da terminale (`nm`, `ar`, `ldd`, `make`), che sono l'obiettivo dell'esercizio, richiedono un ambiente locale. I 4 esercizi parziali sono l’11.2 e i tre del modulo 12. Le note "Su OnlineGDB" nelle soluzioni dicono come procedere.

### 3 · Debug passo-passo

Il pulsante **Debug** avvia il programma sotto **gdb**, il debugger di GNU. Si fissa un *breakpoint* facendo clic a sinistra del numero di riga; l'esecuzione si ferma lì e si prosegue un'istruzione alla volta (*step over* esegue la riga, *step into* entra nella funzione chiamata). I pannelli in basso mostrano la **pila delle chiamate** e le **variabili locali** con il loro valore corrente.

| Esercizio | Cosa osservare con il debugger |
| --- | --- |
| 4.5 Numeri primi | la variabile `d` e il momento in cui `primo` passa a 0 |
| 5.5 Fibonacci | la pila delle chiamate che cresce e si svuota con la ricorsione |
| 5.6 Passaggio per valore | la copia `x` dentro la funzione mentre `a` resta 5 |
| 6.4 Bubble sort | l'array `v` scambio dopo scambio |
| 8.2 Scambio | in `scambia`, i puntatori `a` e `b` contengono gli indirizzi di `x` e `y` |
| 13.4 Merge sort | la pila delle chiamate e le due metà prima della fusione |
| 14.3 Lista concatenata | espandere `lista` nel pannello delle variabili e seguire la catena di `next` fino a NULL |
| 11.3 Ring buffer | i campi `testa` e `coda` che tornano a 0 (wrap-around) |

### 4 · Compilare ed eseguire in locale

```
# -Wall -Wextra: attiva i warning (da leggere SEMPRE)
# -std=c11: standard del linguaggio usato nella dispensa
# -o prog: nome dell'eseguibile da produrre
$ gcc -Wall -Wextra -std=c11 main.c -o prog
$ ./prog
```

Un **errore** blocca la compilazione; un **warning** produce comunque l'eseguibile ma segnala quasi sempre un bug. Obiettivo per ogni esercizio: zero warning.

### 5 · Come affrontare ogni esercizio

1. Leggere la consegna e, se necessario, il riquadro **Concetti chiave** del modulo.
2. Scrivere la soluzione senza guardare quella proposta; usare il **suggerimento** solo se bloccati.
3. Compilare con i warning attivi e correggere finché non ne resta nessuno.
4. Eseguire con gli stessi input dell'esempio e confrontare l'output.
5. Aprire la soluzione e leggere il **commento**: spiega la scelta progettuale e gli errori tipici.

### 6 · Livelli di difficoltà

| Livello | Significato |
| --- | --- |
| *Base* | applicazione diretta di un concetto appena introdotto |
| *Intermedio* | combina due o tre concetti, richiede di ragionare sull'algoritmo |
| *Avanzato* | gestione degli errori, casi limite, più funzioni collaboranti |
| *Progetto* | più file sorgente, librerie e strumenti di build |

## Mappa del percorso

| # | Modulo ed esercizi | N. | Livelli |
| --- | --- | --- | --- |
| [1](#m1) | **Primi passi: output, variabili, input** Il primo programma · Tipi di dato e sizeof · Area e perimetro del rettangolo · Conversione di temperatura | 4 | 1–1 |
| [2](#m2) | **Operatori ed espressioni** Divisione intera, resto e cast · Scambio di due variabili · Da secondi a hh:mm:ss · Manipolazione di bit in un registro | 4 | 1–2 |
| [3](#m3) | **Selezione: if, else, switch** Pari o dispari · Il massimo di tre numeri · Da voto a giudizio · Calcolatrice con switch | 4 | 1–2 |
| [4](#m4) | **Cicli: for, while, do-while** Contare in avanti e all'indietro · Somma e media di N numeri · Tavola pitagorica · Validazione dell'input con do-while · Numeri primi | 5 | 1–3 |
| [5](#m5) | **Funzioni** Prototipo e definizione · Refactoring: il test di primalità come funzione · Fattoriale e limiti dei tipi · MCD e mcm con l'algoritmo di Euclide · Ricorsione: Fibonacci · Passaggio per valore e variabili static | 6 | 1–3 |
| [6](#m6) | **Array** Minimo, massimo e media di 5 voti · Invertire un array · Ricerca lineare · Ordinamento bubble sort · Matrici: trasposta e traccia | 5 | 1–3 |
| [7](#m7) | **Stringhe** Lunghezza di una stringa · Contare vocali e consonanti · Maiuscolo e palindromi · Parsing di un messaggio di telemetria | 4 | 1–3 |
| [8](#m8) | **Puntatori e memoria dinamica** Indirizzo e dereferenziazione · Lo scambio, finalmente in una funzione · Aritmetica dei puntatori · Più risultati da una funzione · Allocazione dinamica | 5 | 1–3 |
| [9](#m9) | **Strutture ed enumerazioni** Punti nel piano · Array di strutture: la classe · Sensori: modificare una struct tramite puntatore · Macchina a stati: il semaforo | 4 | 1–3 |
| [10](#m10) | **File** Scrivere, accodare e rileggere · Log di misure in formato CSV · Contare righe, parole e caratteri (argomenti da riga di comando) · File binari e accesso diretto | 4 | 1–3 |
| [11](#m11) | **Programmazione modulare: header e compilazione separata** Il primo modulo · Compilazione separata, static ed extern · Modulo ring buffer | 3 | 2–4 |
| [12](#m12) | **Librerie statiche, dinamiche e Makefile** Libreria statica di geometria · Libreria dinamica di conversioni per strumentazione · Progetto finale: libreria di statistica e Makefile | 3 | 3–4 |
| [13](#m13) | **Ricerca e ordinamento** Ricerca binaria · Selection sort e insertion sort · Confronto sperimentale degli ordinamenti · Merge sort · qsort e bsearch su un magazzino | 5 | 2–3 |
| [14](#m14) | **Strutture dati: pile, liste, alberi** Pila: controllo delle parentesi · Calcolatrice in notazione polacca inversa · Lista concatenata: operazioni di base · Lista ordinata: inserimento, ricerca, cancellazione · Albero binario di ricerca | 5 | 2–4 |
| [15](#m15) | **Algoritmi per l'automazione** Filtri: media mobile ed esponenziale · Debounce di un ingresso e rilevamento dei fronti · Linearizzazione con tabella e interpolazione · Bisezione: temperatura da una PT100 · CRC-16 Modbus RTU | 5 | 2–4 |
| [16](#m16) | **Funzioni avanzate** Ricorsione: la Torre di Hanoi · Puntatori a funzione: tabella di comandi · Funzioni variadiche: un logger · Macro e funzioni inline: le trappole del preprocessore | 4 | 2–3 |
| [17](#m17) | **Algoritmi classici** Il crivello di Eratostene · Conversioni tra basi numeriche · math.h per il tecnico · Tabella hash per codici articolo | 4 | 2–4 |
| [18](#m18) | **Algoritmi applicati** Regolatore PID su un forno simulato · Macchina a stati: stazione pick-and-place · Percorso minimo di un AGV con BFS · Lettura di frasi NMEA da un GPS | 4 | 3–4 |

Parte I

## Fondamenti

Modulo 1

### Primi passi: output, variabili, input

4 esercizi

Concetti chiave

Un programma C è un insieme di **funzioni**; l'esecuzione parte sempre da `main()`. Le direttive `#include` inseriscono le dichiarazioni delle librerie standard (es. `stdio.h` per `printf` e `scanf`). Ogni variabile ha un **tipo** che ne fissa dimensione in memoria e operazioni ammesse.

| Tipo | Uso | printf | scanf |
| --- | --- | --- | --- |
| `int` | interi | `%d` | `%d` |
| `float` | reali, 7 cifre circa | `%f` | `%f` |
| `double` | reali, 15 cifre circa | `%f` | `%lf` |
| `char` | un carattere (1 byte) | `%c` | `%c` |

`scanf` vuole l'**indirizzo** della variabile da riempire: per questo si scrive `&x`. Il perché si capirà nel modulo sui puntatori.

1.1

#### Il primo programma

*Base*OnlineGDB: Sì

Consegna

Scrivere un programma che stampi due righe: `Ciao, ITS!` e `Il mio primo programma in C.`

Suggerimento

Il carattere `\n` manda a capo.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 1.1 - Primo programma */
#include <stdio.h>      /* libreria standard di input/output: printf */

int main(void)          /* punto di ingresso del programma */
{
    printf("Ciao, ITS!\n");                 /* \n = a capo */
    printf("Il mio primo programma in C.\n");
    return 0;           /* 0 = terminazione corretta, valore letto dal sistema operativo */
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Ciao, ITS!
Il mio primo programma in C.
```

Commento

Ogni istruzione termina con `;`. Il valore restituito da `main` è il codice di uscita: su Linux si legge con `echo $?` subito dopo l'esecuzione.

1.2

#### Tipi di dato e sizeof

*Base*OnlineGDB: Sì

Consegna

Dichiarare e inizializzare una variabile per ciascun tipo base (`int`, `float`, `double`, `char`), stamparne il valore con lo specificatore corretto e stampare la dimensione in byte di ogni tipo con `sizeof`.

Suggerimento

`sizeof` restituisce un valore di tipo `size_t`, che si stampa con `%zu`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 1.2 - Tipi di dato e sizeof */
#include <stdio.h>

int main(void)
{
    int    eta      = 19;                  /* intero */
    float  altezza  = 1.78f;               /* reale a singola precisione: suffisso f */
    double pigreco  = 3.14159265358979;    /* reale a doppia precisione */
    char   iniziale = 'D';                 /* singolo carattere: apici singoli */

    printf("eta      = %d\n", eta);
    printf("altezza  = %.2f m\n", altezza);           /* %.2f: due decimali */
    printf("pigreco  = %.10f\n", pigreco);
    printf("iniziale = %c (codice ASCII %d)\n", iniziale, iniziale);

    /* sizeof restituisce la dimensione in byte (tipo size_t, formato %zu) */
    printf("\nDimensioni su questa macchina:\n");
    printf("char   : %zu byte\n", sizeof(char));
    printf("int    : %zu byte\n", sizeof(int));
    printf("float  : %zu byte\n", sizeof(float));
    printf("double : %zu byte\n", sizeof(double));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
eta      = 19
altezza  = 1.78 m
pigreco  = 3.1415926536
iniziale = D (codice ASCII 68)

Dimensioni su questa macchina:
char   : 1 byte
int    : 4 byte
float  : 4 byte
double : 8 byte
```

Commento

Le dimensioni dipendono dalla piattaforma: l'output è di un PC x86-64. Su Arduino Uno (AVR) `int` è di 2 byte e `double` coincide con `float` (4 byte); su ESP32 `int` è di 4 byte. Un `char` stampato con `%d` mostra il suo codice numerico: in C i caratteri *sono* piccoli interi.

1.3

#### Area e perimetro del rettangolo

*Base*OnlineGDB: Sì

Consegna

Leggere da tastiera base e altezza di un rettangolo (numeri reali) e stampare area e perimetro con due decimali.

Suggerimento

Per leggere un `double` con `scanf` serve `%lf`, non `%f`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 1.3 - Area e perimetro del rettangolo */
#include <stdio.h>

int main(void)
{
    double base, altezza;

    printf("Base: ");
    scanf("%lf", &base);         /* %lf per double; &base = indirizzo di base */
    printf("Altezza: ");
    scanf("%lf", &altezza);

    double area      = base * altezza;
    double perimetro = 2.0 * (base + altezza);

    printf("\nArea      = %.2f\n", area);
    printf("Perimetro = %.2f\n", perimetro);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Base: 4
Altezza: 2.5

Area      = 10.00
Perimetro = 13.00
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Dimenticare la `&` in `scanf` è l'errore più comune del principiante: il programma compila (con un warning) e poi va in crash. Per questo si compila sempre con `-Wall -Wextra` e si leggono i warning.

1.4

#### Conversione di temperatura

*Base*OnlineGDB: Sì

Consegna

Leggere una temperatura in gradi Celsius e stamparla convertita in Fahrenheit (`F = C·9/5 + 32`) e in Kelvin (`K = C + 273,15`).

Suggerimento

Attenzione a `9/5`: tra due interi la divisione è intera.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 1.4 - Conversione di temperatura */
#include <stdio.h>

int main(void)
{
    double celsius;
    printf("Temperatura in gradi Celsius: ");
    scanf("%lf", &celsius);

    /* 9/5 tra interi varrebbe 1: si usano costanti reali 9.0 e 5.0 */
    double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
    double kelvin     = celsius + 273.15;

    printf("%.1f C = %.1f F = %.2f K\n", celsius, fahrenheit, kelvin);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Temperatura in gradi Celsius: 36.6
36.6 C = 97.9 F = 309.75 K
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Prova a sostituire `9.0 / 5.0` con `9 / 5`: con 36,6 °C ottieni 68,6 °F invece di 97,9 °F. È un errore che il compilatore **non** segnala.

Modulo 2

### Operatori ed espressioni

4 esercizi

Concetti chiave

Gli operatori aritmetici sono `+ - * / %`. La **divisione tra interi tronca** il risultato; `%` (modulo) dà il resto ed è definito solo tra interi. Per ottenere un risultato reale da operandi interi si usa il **cast**: `(double)a / b`.

Gli operatori **bit a bit** (`& | ^ ~ << >>`) agiscono sui singoli bit e sono il pane quotidiano della programmazione dei microcontrollori: leggere, alzare, abbassare e invertire un bit di un registro.

| Operazione | Espressione |
| --- | --- |
| leggere il bit n | `(x >> n) & 1` |
| alzare il bit n | `x \| (1u << n)` |
| abbassare il bit n | `x & ~(1u << n)` |
| invertire il bit n | `x ^ (1u << n)` |

2.1

#### Divisione intera, resto e cast

*Base*OnlineGDB: Sì

Consegna

Leggere due interi `a` e `b` e stampare: il quoziente intero, il resto e il risultato della divisione reale con tre decimali.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 2.1 - Divisione intera, resto e cast */
#include <stdio.h>

int main(void)
{
    int a, b;
    printf("Inserisci due interi (a b): ");
    scanf("%d %d", &a, &b);

    printf("%d / %d = %d (divisione intera)\n", a, b, a / b);
    printf("%d %% %d = %d (resto)\n", a, b, a % b);      /* %% stampa il simbolo % */
    printf("%d / %d = %.3f (divisione reale con cast)\n", a, b, (double)a / b);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Inserisci due interi (a b): 17
5
17 / 5 = 3 (divisione intera)
17 % 5 = 2 (resto)
17 / 5 = 3.400 (divisione reale con cast)
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Il cast `(double)a` converte solo `a`; per le regole di promozione anche `b` viene convertito e la divisione diventa reale. Scrivere `(double)(a / b)` sarebbe sbagliato: la divisione intera avverrebbe *prima* della conversione. Con `b = 0` il programma si interrompe: la gestione dell'errore arriva nel modulo 3.

2.2

#### Scambio di due variabili

*Base*OnlineGDB: Sì

Consegna

Leggere due interi `x` e `y`, scambiarne il contenuto e stamparli prima e dopo lo scambio.

Suggerimento

Serve una terza variabile di appoggio.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 2.2 - Scambio di due variabili */
#include <stdio.h>

int main(void)
{
    int x, y;
    printf("x y: ");
    scanf("%d %d", &x, &y);
    printf("Prima : x = %d, y = %d\n", x, y);

    int tmp = x;    /* salvo x prima di sovrascriverlo */
    x = y;
    y = tmp;

    printf("Dopo  : x = %d, y = %d\n", x, y);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
x y: 3
8
Prima : x = 3, y = 8
Dopo  : x = 8, y = 3
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Senza `tmp`, scrivendo `x = y; y = x;` si perde il valore originale di `x`. Lo stesso scambio, scritto come funzione, sarà il primo esempio di uso dei puntatori (esercizio 8.2).

2.3

#### Da secondi a hh:mm:ss

*Intermedio*OnlineGDB: Sì

Consegna

Leggere un numero di secondi e convertirlo nel formato `hh:mm:ss`, con due cifre per ogni campo.

Suggerimento

Usare `/` e `%` con 3600 e 60. Il formato `%02d` riempie con zeri a sinistra.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 2.3 - Conversione secondi -> hh:mm:ss */
#include <stdio.h>

int main(void)
{
    int totale;
    printf("Secondi totali: ");
    scanf("%d", &totale);

    int ore     = totale / 3600;            /* ore intere */
    int minuti  = (totale % 3600) / 60;     /* minuti nel resto dell'ora */
    int secondi = totale % 60;              /* secondi rimanenti */

    /* %02d: almeno 2 cifre, completate con zeri a sinistra */
    printf("%d s = %02d:%02d:%02d\n", totale, ore, minuti, secondi);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Secondi totali: 3725
3725 s = 01:02:05
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

È lo stesso calcolo che si fa su un microcontrollore per mostrare un tempo di ciclo o un uptime a partire da un contatore di secondi.

2.4

#### Manipolazione di bit in un registro

*Intermedio*OnlineGDB: Sì

Consegna

Leggere un valore esadecimale a 8 bit (es. `5A`) che rappresenta un registro. Stampare: il valore del bit 3; il registro con il bit 0 alzato; con il bit 4 abbassato; con il bit 7 invertito; il nibble alto (4 bit più significativi).

Suggerimento

`scanf("%x", ...)` legge in esadecimale; `printf("0x%02X", ...)` stampa in esadecimale maiuscolo a due cifre. Usare `unsigned int`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 2.4 - Manipolazione di bit */
#include <stdio.h>

int main(void)
{
    unsigned int reg;
    printf("Valore del registro (esadecimale, es. 5A): ");
    scanf("%x", &reg);
    reg &= 0xFFu;                            /* maschera: tengo solo 8 bit */

    unsigned int bit3 = (reg >> 3) & 1u;     /* sposto il bit 3 in posizione 0 e lo isolo */

    printf("reg          = 0x%02X\n", reg);
    printf("bit 3        = %u\n", bit3);
    printf("set bit 0    = 0x%02X\n", reg | (1u << 0));            /* OR: alza il bit */
    printf("clear bit 4  = 0x%02X\n", reg & ~(1u << 4) & 0xFFu);   /* AND con maschera negata */
    printf("toggle bit 7 = 0x%02X\n", reg ^ (1u << 7));            /* XOR: inverte il bit */
    printf("nibble alto  = 0x%X\n", (reg >> 4) & 0x0Fu);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Valore del registro (esadecimale, es. 5A): 5A
reg          = 0x5A
bit 3        = 1
set bit 0    = 0x5B
clear bit 4  = 0x4A
toggle bit 7 = 0xDA
nibble alto  = 0x5
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

0x5A = `0101 1010`. Queste quattro espressioni sono esattamente quelle usate per configurare i registri di AVR, STM32 ed ESP32 (es. `PORTB |= (1 << PB5);`). Si usa `unsigned` perché lo scorrimento di valori con segno ha comportamenti non portabili.

Modulo 3

### Selezione: if, else, switch

4 esercizi

Concetti chiave

In C una condizione è **vera se vale un numero diverso da zero**, falsa se vale 0. Operatori relazionali: `== != < <= > >=`; logici: `&&` (AND), `||` (OR), `!` (NOT). `&&` e `||` valutano il secondo operando solo se necessario (*cortocircuito*).

`switch` confronta un valore intero (o un carattere) con costanti; ogni `case` va chiuso con `break`, altrimenti l'esecuzione prosegue nel `case` successivo.

Trappola classica: `if (x = 5)` **assegna** 5 a x ed è sempre vera. Il confronto si scrive `==`. Con `-Wall` il compilatore lo segnala.

3.1

#### Pari o dispari

*Base*OnlineGDB: Sì

Consegna

Leggere un intero e stampare se è pari o dispari.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 3.1 - Pari o dispari */
#include <stdio.h>

int main(void)
{
    int n;
    printf("Numero intero: ");
    scanf("%d", &n);

    if (n % 2 == 0)              /* resto della divisione per 2 */
        printf("%d è pari\n", n);
    else
        printf("%d è dispari\n", n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Numero intero: 7
7 è dispari
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Si confronta con `== 0` e non con `== 1`: in C il resto ha il segno del dividendo, quindi `-7 % 2` vale `-1`. Il test `n % 2 == 1` classificherebbe -7 come pari.

3.2

#### Il massimo di tre numeri

*Base*OnlineGDB: Sì

Consegna

Leggere tre interi e stampare il maggiore.

Suggerimento

Partire dall'ipotesi che il massimo sia il primo e aggiornarla.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 3.2 - Massimo di tre numeri */
#include <stdio.h>

int main(void)
{
    int a, b, c;
    printf("Tre numeri: ");
    scanf("%d %d %d", &a, &b, &c);

    int max = a;              /* ipotesi iniziale */
    if (b > max) max = b;     /* aggiorno se trovo un valore maggiore */
    if (c > max) max = c;

    printf("Massimo = %d\n", max);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Tre numeri: 4
9
2
Massimo = 9
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Lo schema "ipotesi iniziale + aggiornamento" si generalizza senza modifiche a N valori con un ciclo (esercizio 6.1), cosa che non vale per una cascata di `if` annidati.

3.3

#### Da voto a giudizio

*Intermedio*OnlineGDB: Sì

Consegna

Leggere un voto intero da 1 a 10 e stampare il giudizio: 9-10 Ottimo, 7-8 Buono, 6 Sufficiente, 1-5 Insufficiente. Valori fuori intervallo: "Voto non valido".

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 3.3 - Da voto a giudizio */
#include <stdio.h>

int main(void)
{
    int voto;
    printf("Voto (1-10): ");
    scanf("%d", &voto);

    if (voto < 1 || voto > 10) {         /* prima si scartano i valori non validi */
        printf("Voto non valido\n");
    } else if (voto >= 9) {
        printf("Ottimo\n");
    } else if (voto >= 7) {              /* qui si arriva solo se voto < 9 */
        printf("Buono\n");
    } else if (voto == 6) {
        printf("Sufficiente\n");
    } else {
        printf("Insufficiente\n");
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Voto (1-10): 7
Buono
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Nella catena `else if` ogni ramo viene valutato solo se i precedenti sono falsi: per questo basta `voto >= 7` senza scrivere anche `voto < 9`.

3.4

#### Calcolatrice con switch

*Intermedio*OnlineGDB: Sì

Consegna

Leggere un'espressione nella forma `numero operatore numero` (es. `12 * 4`) e stamparne il risultato. Gestire gli operatori `+ - * x /`, la divisione per zero e gli operatori non riconosciuti.

Suggerimento

`scanf` restituisce il numero di campi letti correttamente: va controllato.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 3.4 - Calcolatrice con switch */
#include <stdio.h>

int main(void)
{
    double a, b;
    char op;
    printf("Espressione (es. 12 * 4): ");
    if (scanf("%lf %c %lf", &a, &op, &b) != 3) {   /* devono essere letti 3 campi */
        printf("Formato non valido\n");
        return 1;
    }

    switch (op) {
    case '+': printf("= %g\n", a + b); break;
    case '-': printf("= %g\n", a - b); break;
    case '*':                                      /* due case con la stessa azione */
    case 'x': printf("= %g\n", a * b); break;
    case '/':
        if (b == 0.0) {
            printf("Errore: divisione per zero\n");
            return 1;
        }
        printf("= %g\n", a / b);
        break;
    default:                                       /* nessun case corrisponde */
        printf("Operatore '%c' non supportato\n", op);
        return 1;
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Espressione (es. 12 * 4): 12
*
4
= 48
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

`%g` sceglie automaticamente la notazione più compatta (48 invece di 48.000000). I `return 1` segnalano al sistema un'uscita con errore: è la convenzione usata da tutti i programmi a riga di comando.

Modulo 4

### Cicli: for, while, do-while

5 esercizi

Concetti chiave

`for (init; condizione; aggiornamento)` si usa quando il numero di ripetizioni è noto; `while (condizione)` quando dipende da un evento; `do { } while (condizione);` esegue il corpo **almeno una volta** ed è adatto alla validazione dell'input.

`break` esce dal ciclo, `continue` passa all'iterazione successiva. Un **accumulatore** (somma, contatore) va sempre inizializzato prima del ciclo: le variabili locali non inizializzate contengono valori casuali.

4.1

#### Contare in avanti e all'indietro

*Base*OnlineGDB: Sì

Consegna

Leggere N e stampare i numeri da 1 a N con un ciclo `for`, poi un conto alla rovescia da N a 1 con un ciclo `while` seguito da "Via!".

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 4.1 - Contare con for e while */
#include <stdio.h>

int main(void)
{
    int n;
    printf("N: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)     /* i esiste solo dentro il for (C99) */
        printf("%d ", i);
    printf("\n");

    int k = n;                       /* conto alla rovescia con while */
    while (k > 0) {
        printf("%d ", k);
        k--;                         /* senza questa riga il ciclo sarebbe infinito */
    }
    printf("Via!\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
N: 5
1 2 3 4 5 
5 4 3 2 1 Via!
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Ogni ciclo `for` si può riscrivere come `while` e viceversa; la scelta è di leggibilità.

4.2

#### Somma e media di N numeri

*Base*OnlineGDB: Sì

Consegna

Chiedere quanti numeri si vogliono inserire, leggerli uno alla volta e stampare somma e media.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 4.2 - Somma e media di N numeri */
#include <stdio.h>

int main(void)
{
    int n;
    printf("Quanti numeri? ");
    scanf("%d", &n);
    if (n <= 0) {
        printf("N deve essere positivo\n");
        return 1;
    }

    double somma = 0.0;              /* accumulatore: va inizializzato! */
    for (int i = 1; i <= n; i++) {
        double x;
        printf("Numero %d: ", i);
        scanf("%lf", &x);
        somma += x;                  /* equivale a somma = somma + x */
    }
    printf("\nSomma = %.2f\nMedia = %.2f\n", somma, somma / n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Quanti numeri? 5
Numero 1: 4
Numero 2: 8
Numero 3: 15
Numero 4: 16
Numero 5: 23

Somma = 66.00
Media = 13.20
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Il controllo `n <= 0` evita la divisione per zero nel calcolo della media. Essendo `somma` un `double`, `somma / n` è una divisione reale anche se `n` è intero.

4.3

#### Tavola pitagorica

*Intermedio*OnlineGDB: Sì

Consegna

Stampare la tavola pitagorica 6×6 con intestazione di righe e colonne, allineata in colonne.

Suggerimento

Due cicli annidati: l'esterno per le righe, l'interno per le colonne. `%4d` stampa su 4 caratteri.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 4.3 - Tavola pitagorica */
#include <stdio.h>

int main(void)
{
    const int N = 6;                     /* const: valore non modificabile */

    printf("   |");                      /* intestazione delle colonne */
    for (int c = 1; c <= N; c++) printf("%4d", c);
    printf("\n---+");
    for (int c = 1; c <= N; c++) printf("----");
    printf("\n");

    for (int r = 1; r <= N; r++) {       /* ciclo esterno: righe */
        printf("%2d |", r);
        for (int c = 1; c <= N; c++)     /* ciclo interno: colonne */
            printf("%4d", r * c);
        printf("\n");                    /* fine riga */
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
   |   1   2   3   4   5   6
---+------------------------
 1 |   1   2   3   4   5   6
 2 |   2   4   6   8  10  12
 3 |   3   6   9  12  15  18
 4 |   4   8  12  16  20  24
 5 |   5  10  15  20  25  30
 6 |   6  12  18  24  30  36
```

Commento

Il ciclo interno viene eseguito per intero a ogni iterazione dell'esterno: N×N = 36 prodotti. La larghezza fissa (`%4d`, `%2d`) è ciò che mantiene l'allineamento.

4.4

#### Validazione dell'input con do-while

*Intermedio*OnlineGDB: Sì

Consegna

Chiedere un valore tra 1 e 10 finché l'utente non ne inserisce uno valido, segnalando ogni valore fuori intervallo. Se l'input non è numerico, terminare con un messaggio.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 4.4 - Validazione con do-while */
#include <stdio.h>

int main(void)
{
    int n;
    do {
        printf("Inserisci un valore tra 1 e 10: ");
        if (scanf("%d", &n) != 1) {              /* input non numerico (o fine input) */
            printf("Input non numerico, esco.\n");
            return 1;
        }
        if (n < 1 || n > 10)
            printf("  -> %d fuori intervallo, riprova\n", n);
    } while (n < 1 || n > 10);                   /* ripeto finché non è valido */

    printf("Valore accettato: %d\n", n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Inserisci un valore tra 1 e 10: 0
  -> 0 fuori intervallo, riprova
Inserisci un valore tra 1 e 10: 15
  -> 15 fuori intervallo, riprova
Inserisci un valore tra 1 e 10: 7
Valore accettato: 7
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Il controllo sul valore restituito da `scanf` è essenziale: se l'utente digita una lettera, `scanf` non la consuma e, senza controllo, il ciclo diventerebbe infinito.

4.5

#### Numeri primi

*Avanzato*OnlineGDB: Sì

Consegna

Leggere un intero e dire se è primo. Stampare poi tutti i numeri primi fino a 50.

Suggerimento

Basta cercare divisori fino a √n, cioè finché `d * d <= n`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 4.5 - Numeri primi */
#include <stdio.h>

int main(void)
{
    int n;
    printf("Numero: ");
    scanf("%d", &n);

    int primo = (n >= 2);                         /* 0 e 1 non sono primi */
    for (int d = 2; d * d <= n && primo; d++) {   /* basta arrivare a radice di n */
        if (n % d == 0)
            primo = 0;                            /* trovato un divisore */
    }
    printf("%d %s primo\n", n, primo ? "è" : "non è");   /* operatore ternario */

    printf("Primi fino a 50:");
    for (int k = 2; k <= 50; k++) {
        int p = 1;
        for (int d = 2; d * d <= k; d++)
            if (k % d == 0) { p = 0; break; }     /* break: inutile proseguire */
        if (p) printf(" %d", k);
    }
    printf("\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Numero: 97
97 è primo
Primi fino a 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Il test di primalità compare **due volte** nel codice: è il segnale che serve una funzione. L'esercizio 5.2 riscrive questo programma in modo modulare. L'operatore ternario `cond ? a : b` vale `a` se la condizione è vera, `b` altrimenti.

Parte II

## Strutturare il codice

Modulo 5

### Funzioni

6 esercizi

Concetti chiave

Una funzione ha un **prototipo** (dichiarazione: nome, parametri, tipo restituito) e una **definizione** (il corpo). Il prototipo deve comparire prima dell'uso: sarà il contenuto dei file header nel modulo 11.

In C i parametri sono passati **per valore**: la funzione lavora su una copia. Le variabili locali nascono a ogni chiamata e spariscono al ritorno, tranne quelle dichiarate `static`, che conservano il valore tra una chiamata e l'altra.

Una funzione è **ricorsiva** se chiama sé stessa: servono sempre un *caso base* che termina la ricorsione e un *passo ricorsivo* che si avvicina al caso base.

5.1

#### Prototipo e definizione

*Base*OnlineGDB: Sì

Consegna

Scrivere le funzioni `quadrato(x)` e `cubo(x)` (con `cubo` che usa `quadrato`), dichiararle con prototipo prima di `main` e definirle dopo. Stampare quadrato e cubo dei numeri da 1 a 5.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.1 - Prototipo e definizione */
#include <stdio.h>

/* prototipi: dicono al compilatore nome, parametri e tipo restituito */
double quadrato(double x);
double cubo(double x);

int main(void)
{
    for (int i = 1; i <= 5; i++)       /* i (int) viene convertito in double */
        printf("x = %d   x^2 = %5.1f   x^3 = %6.1f\n", i, quadrato(i), cubo(i));
    return 0;
}

/* definizioni: il corpo delle funzioni */
double quadrato(double x)
{
    return x * x;
}

double cubo(double x)
{
    return quadrato(x) * x;            /* una funzione può chiamarne un'altra */
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
x = 1   x^2 =   1.0   x^3 =    1.0
x = 2   x^2 =   4.0   x^3 =    8.0
x = 3   x^2 =   9.0   x^3 =   27.0
x = 4   x^2 =  16.0   x^3 =   64.0
x = 5   x^2 =  25.0   x^3 =  125.0
```

Commento

Senza i prototipi il compilatore incontrerebbe `quadrato` dentro `main` senza conoscerla: in C11 è un errore (dichiarazione implicita).

5.2

#### Refactoring: il test di primalità come funzione

*Intermedio*OnlineGDB: Sì

Consegna

Riscrivere il test di primalità dell'esercizio 4.5 come funzione `bool e_primo(int n)` e usarla per stampare tutti i primi tra 1 e 100, dieci per riga, con il conteggio finale.

Suggerimento

Il tipo `bool` è in `<stdbool.h>`. Un `return` dentro il ciclo esce subito dalla funzione.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.2 - Funzione e_primo */
#include <stdio.h>
#include <stdbool.h>      /* tipo bool, valori true / false (C99) */

bool e_primo(int n)
{
    if (n < 2)
        return false;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return false;     /* return esce subito dalla funzione */
    return true;              /* nessun divisore trovato */
}

int main(void)
{
    int conteggio = 0;
    printf("Primi tra 1 e 100:\n");
    for (int k = 1; k <= 100; k++) {
        if (e_primo(k)) {
            printf("%4d", k);
            if (++conteggio % 10 == 0)    /* a capo ogni 10 numeri */
                printf("\n");
        }
    }
    printf("\nTotale: %d\n", conteggio);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Primi tra 1 e 100:
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97
Totale: 25
```

Commento

Il nome `e_primo` rende il `main` leggibile come una frase. Una funzione che risponde vero/falso si chiama *predicato*; per convenzione il nome è una domanda (`e_primo`, `is_valid`, `rb_vuoto`...).

5.3

#### Fattoriale e limiti dei tipi

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione iterativa che calcoli il fattoriale `n!` e stampare 0!, 5!, 10!, 15!, 20!.

Suggerimento

Il fattoriale cresce molto in fretta: usare `unsigned long long` (64 bit, formato `%llu`).

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.3 - Fattoriale */
#include <stdio.h>

unsigned long long fattoriale(unsigned int n)
{
    unsigned long long f = 1;          /* 0! = 1 per definizione */
    for (unsigned int i = 2; i <= n; i++)
        f *= i;
    return f;
}

int main(void)
{
    for (unsigned int n = 0; n <= 20; n += 5)
        printf("%2u! = %llu\n", n, fattoriale(n));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
 0! = 1
 5! = 120
10! = 3628800
15! = 1307674368000
20! = 2432902008176640000
```

Commento

20! è il massimo che entra in 64 bit senza segno: 21! supera 1,8·1019 e il risultato "fa il giro" (overflow) **senza alcun errore**. Conoscere il range dei tipi è responsabilità del programmatore.

5.4

#### MCD e mcm con l'algoritmo di Euclide

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere le funzioni `mcd(a, b)` con l'algoritmo di Euclide e `mcm(a, b)` che usa `mcd`. Leggere due interi positivi e stampare entrambi.

Suggerimento

Euclide: finché `b ≠ 0`, sostituire `(a, b)` con `(b, a % b)`. Inoltre `mcm = a·b / mcd`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.4 - MCD e mcm */
#include <stdio.h>

int mcd(int a, int b)
{
    while (b != 0) {          /* algoritmo di Euclide */
        int r = a % b;
        a = b;                /* a e b sono copie: modificarle non tocca il chiamante */
        b = r;
    }
    return a;
}

int mcm(int a, int b)
{
    return a / mcd(a, b) * b; /* divido prima di moltiplicare: riduco il rischio di overflow */
}

int main(void)
{
    int a, b;
    printf("Due interi positivi: ");
    scanf("%d %d", &a, &b);
    printf("MCD(%d, %d) = %d\n", a, b, mcd(a, b));
    printf("mcm(%d, %d) = %d\n", a, b, mcm(a, b));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Due interi positivi: 84
36
MCD(84, 36) = 12
mcm(84, 36) = 252
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Dentro `mcd` si modificano liberamente `a` e `b`: grazie al passaggio per valore le variabili di `main` restano intatte, come mostra la stampa finale.

5.5

#### Ricorsione: Fibonacci

*Avanzato*OnlineGDB: Sì

Consegna

Scrivere due versioni della funzione di Fibonacci, ricorsiva e iterativa. Per n = 10, 20, 30 stampare i due risultati e il numero di chiamate effettuate dalla versione ricorsiva.

Suggerimento

Usare una variabile globale incrementata a ogni chiamata ricorsiva.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.5 - Fibonacci ricorsivo e iterativo */
#include <stdio.h>

long chiamate = 0;                  /* variabile globale: visibile da tutte le funzioni */

long fib_ric(int n)                 /* elegante, ma costo esponenziale */
{
    chiamate++;
    if (n < 2)                      /* caso base */
        return n;
    return fib_ric(n - 1) + fib_ric(n - 2);    /* passo ricorsivo */
}

long fib_it(int n)                  /* costo lineare */
{
    long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long t = a + b;
        a = b;
        b = t;
    }
    return a;
}

int main(void)
{
    for (int n = 10; n <= 30; n += 10) {
        chiamate = 0;
        long r = fib_ric(n);
        printf("fib(%d) = %ld   iterativa = %ld   chiamate ricorsive = %ld\n",
               n, r, fib_it(n), chiamate);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
fib(10) = 55   iterativa = 55   chiamate ricorsive = 177
fib(20) = 6765   iterativa = 6765   chiamate ricorsive = 21891
fib(30) = 832040   iterativa = 832040   chiamate ricorsive = 2692537
```

Commento

La versione ricorsiva ricalcola gli stessi valori moltissime volte: per n = 30 servono quasi 2,7 milioni di chiamate contro 30 iterazioni. Su un microcontrollore la ricorsione profonda può anche esaurire lo stack. Le variabili globali vanno usate con parsimonia: qui servono solo a misurare.

5.6

#### Passaggio per valore e variabili static

*Avanzato*OnlineGDB: Sì

Consegna

Dimostrare con un programma che una funzione non può modificare una variabile passata per valore. Scrivere poi una funzione `prossimo_id()` che a ogni chiamata restituisca un numero progressivo (1, 2, 3...) senza usare variabili globali.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 5.6 - Passaggio per valore e static */
#include <stdio.h>

void prova_valore(int x)
{
    x = 100;                       /* modifica la COPIA locale */
    printf("  dentro la funzione x = %d\n", x);
}

int prossimo_id(void)
{
    static int contatore = 0;      /* inizializzata una sola volta, sopravvive tra le chiamate */
    return ++contatore;
}

int main(void)
{
    int a = 5;
    printf("prima:  a = %d\n", a);
    prova_valore(a);
    printf("dopo:   a = %d  (invariata: passaggio per valore)\n", a);

    printf("\nID generati:");
    for (int i = 0; i < 4; i++)
        printf(" %d", prossimo_id());
    printf("\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
prima:  a = 5
  dentro la funzione x = 100
dopo:   a = 5  (invariata: passaggio per valore)

ID generati: 1 2 3 4
```

Commento

Una variabile locale `static` ha la durata di una globale ma la visibilità di una locale: nessun'altra funzione può modificarla per errore. Per far modificare `a` a una funzione serve passarne l'indirizzo (modulo 8).

Modulo 6

### Array

5 esercizi

Concetti chiave

Un array è una sequenza di elementi **dello stesso tipo**, contigui in memoria, con indici da `0` a `N-1`. Il C **non controlla i limiti**: scrivere `v[N]` corrompe la memoria senza errori in compilazione.

Il numero di elementi di un array dichiarato nello stesso blocco si ricava con `sizeof v / sizeof v[0]`. Quando un array viene passato a una funzione, si passa in realtà l'**indirizzo** del primo elemento: la funzione può modificarlo e non ne conosce la lunghezza, che va passata come parametro separato.

6.1

#### Minimo, massimo e media di 5 voti

*Base*OnlineGDB: Sì

Consegna

Leggere 5 voti in un array e stampare minimo, massimo e media.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 6.1 - Min, max, media */
#include <stdio.h>
#define N 5                         /* costante simbolica: dimensione dell'array */

int main(void)
{
    double voti[N];
    for (int i = 0; i < N; i++) {   /* indici da 0 a N-1 */
        printf("Voto %d: ", i + 1);
        scanf("%lf", &voti[i]);
    }

    double min = voti[0], max = voti[0], somma = 0.0;
    for (int i = 0; i < N; i++) {
        if (voti[i] < min) min = voti[i];
        if (voti[i] > max) max = voti[i];
        somma += voti[i];
    }
    printf("\nMin = %.1f   Max = %.1f   Media = %.2f\n", min, max, somma / N);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Voto 1: 7
Voto 2: 5.5
Voto 3: 8
Voto 4: 6
Voto 5: 9.5

Min = 5.5   Max = 9.5   Media = 7.20
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

`#define N 5` permette di cambiare la dimensione in un solo punto. Il preprocessore sostituisce testualmente `N` con `5` prima della compilazione.

6.2

#### Invertire un array

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione `stampa(v, n)` e una funzione `inverti(v, n)` che inverta l'ordine degli elementi *sul posto*, senza array di appoggio.

Suggerimento

Due indici, uno dall'inizio e uno dalla fine, che si scambiano e si avvicinano.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 6.2 - Inversione di un array */
#include <stdio.h>

void stampa(const int v[], int n)    /* const: la funzione non modifica v */
{
    for (int i = 0; i < n; i++)
        printf("%d ", v[i]);
    printf("\n");
}

void inverti(int v[], int n)         /* v è l'indirizzo dell'array originale */
{
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = v[i];
        v[i] = v[j];
        v[j] = t;
    }
}

int main(void)
{
    int dati[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int n = sizeof dati / sizeof dati[0];      /* numero di elementi */

    printf("Originale: "); stampa(dati, n);
    inverti(dati, n);
    printf("Invertito: "); stampa(dati, n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Originale: 3 1 4 1 5 9 2 6 
Invertito: 6 2 9 5 1 4 1 3 
```

Commento

Diversamente da un `int`, l'array viene modificato dalla funzione: ciò che si passa è l'indirizzo. Il qualificatore `const` in `stampa` documenta (e fa verificare al compilatore) che quella funzione si limita a leggere.

6.3

#### Ricerca lineare

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione `cerca(v, n, chiave)` che restituisca la posizione della prima occorrenza di `chiave` oppure -1 se assente. Provarla su un array di codici articolo con tre chiavi.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 6.3 - Ricerca lineare */
#include <stdio.h>

int cerca(const int v[], int n, int chiave)
{
    for (int i = 0; i < n; i++)
        if (v[i] == chiave)
            return i;         /* trovato: restituisco la posizione */
    return -1;                /* convenzione: -1 = non trovato */
}

int main(void)
{
    int codici[] = {120, 340, 75, 980, 410, 75};
    int n = sizeof codici / sizeof codici[0];
    int da_cercare[] = {980, 75, 500};

    for (int k = 0; k < 3; k++) {
        int pos = cerca(codici, n, da_cercare[k]);
        if (pos >= 0)
            printf("%d trovato in posizione %d\n", da_cercare[k], pos);
        else
            printf("%d non presente\n", da_cercare[k]);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
980 trovato in posizione 3
75 trovato in posizione 2
500 non presente
```

Commento

Il valore 75 compare due volte: la funzione restituisce la prima occorrenza. Restituire un valore "impossibile" (-1) per segnalare un esito negativo è una convenzione molto diffusa nelle librerie C.

6.4

#### Ordinamento bubble sort

*Avanzato*OnlineGDB: Sì

Consegna

Implementare il bubble sort mostrando l'array dopo ogni passata. Interrompere l'algoritmo in anticipo se in una passata non avviene alcuno scambio.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 6.4 - Bubble sort */
#include <stdio.h>

void stampa(const int v[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%3d", v[i]);
    printf("\n");
}

void bubble_sort(int v[], int n)
{
    for (int passata = 0; passata < n - 1; passata++) {
        int scambi = 0;
        for (int i = 0; i < n - 1 - passata; i++) {  /* gli ultimi elementi sono già a posto */
            if (v[i] > v[i + 1]) {                   /* coppia fuori ordine: scambio */
                int t = v[i];
                v[i] = v[i + 1];
                v[i + 1] = t;
                scambi++;
            }
        }
        printf("passata %d:", passata + 1);
        stampa(v, n);
        if (scambi == 0)                             /* nessuno scambio: già ordinato */
            break;
    }
}

int main(void)
{
    int v[] = {29, 10, 14, 37, 13};
    int n = sizeof v / sizeof v[0];
    printf("iniziale :");
    stampa(v, n);
    bubble_sort(v, n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
iniziale : 29 10 14 37 13
passata 1: 10 14 29 13 37
passata 2: 10 14 13 29 37
passata 3: 10 13 14 29 37
passata 4: 10 13 14 29 37
```

Commento

A ogni passata il massimo tra gli elementi non ordinati "galleggia" in fondo, per questo il ciclo interno si accorcia di uno. Nella pratica si usa `qsort` di `<stdlib.h>`; implementarlo a mano serve a capire i cicli annidati.

6.5

#### Matrici: trasposta e traccia

*Avanzato*OnlineGDB: Sì

Consegna

Data una matrice 3×3, calcolare la trasposta e la traccia (somma degli elementi della diagonale principale) e stamparle.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 6.5 - Matrice: trasposta e traccia */
#include <stdio.h>
#define R 3
#define C 3

int main(void)
{
    int m[R][C] = { {1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9} };
    int t[C][R];
    int traccia = 0;

    for (int i = 0; i < R; i++) {
        traccia += m[i][i];              /* diagonale principale: riga == colonna */
        for (int j = 0; j < C; j++)
            t[j][i] = m[i][j];           /* trasposta: scambio indici */
    }

    printf("Matrice:\n");
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) printf("%3d", m[i][j]);
        printf("\n");
    }
    printf("Trasposta:\n");
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < R; j++) printf("%3d", t[i][j]);
        printf("\n");
    }
    printf("Traccia = %d\n", traccia);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Matrice:
  1  2  3
  4  5  6
  7  8  9
Trasposta:
  1  4  7
  2  5  8
  3  6  9
Traccia = 15
```

Commento

In memoria la matrice è memorizzata **per righe** (row-major): `m[1][0]` segue immediatamente `m[0][2]`. È importante quando si leggono o scrivono blocchi di dati su file o su un bus.

Modulo 7

### Stringhe

4 esercizi

Concetti chiave

In C una stringa è un **array di `char` terminato dal carattere nullo `'\0'`**. `char s[] = "ciao";` occupa 5 byte. Le funzioni di `<string.h>` (`strlen`, `strcpy`, `strcmp`, `strchr`, `strtok`...) si basano tutte sul terminatore.

Le stringhe non si confrontano con `==` (confronterebbe gli indirizzi) ma con `strcmp`. Per leggere una riga intera si usa `fgets`, che rispetta la dimensione del buffer; `gets` è stata rimossa dallo standard perché insicura.

Le funzioni di `<ctype.h>` (`toupper`, `isalpha`, `isdigit`...) classificano e convertono singoli caratteri.

7.1

#### Lunghezza di una stringa

*Base*OnlineGDB: Sì

Consegna

Scrivere una funzione `mia_strlen` che conti i caratteri di una stringa fino al terminatore. Confrontarla con `strlen` e con `sizeof`, e stampare primo e ultimo carattere.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 7.1 - Lunghezza di una stringa */
#include <stdio.h>
#include <string.h>

size_t mia_strlen(const char s[])
{
    size_t n = 0;
    while (s[n] != '\0')            /* la stringa termina con il carattere nullo */
        n++;
    return n;
}

int main(void)
{
    char parola[] = "Meccatronica";    /* il compilatore aggiunge '\0': 13 byte */

    printf("Stringa      : %s\n", parola);
    printf("mia_strlen   : %zu\n", mia_strlen(parola));
    printf("strlen       : %zu\n", strlen(parola));
    printf("sizeof       : %zu (include il terminatore)\n", sizeof parola);
    printf("Primo/ultimo : %c / %c\n", parola[0], parola[strlen(parola) - 1]);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Stringa      : Meccatronica
mia_strlen   : 12
strlen       : 12
sizeof       : 13 (include il terminatore)
Primo/ultimo : M / a
```

Commento

`strlen` conta i caratteri, `sizeof` misura la memoria occupata. Se il terminatore manca, `strlen` continua a leggere oltre la fine dell'array: è una delle cause più frequenti di bug nei programmi C.

7.2

#### Contare vocali e consonanti

*Intermedio*OnlineGDB: Sì

Consegna

Leggere una frase con `fgets` e contarne vocali, consonanti e spazi, senza distinguere maiuscole e minuscole.

Suggerimento

`tolower` converte in minuscolo; `strchr("aeiou", c)` è diverso da `NULL` se `c` è una vocale.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 7.2 - Vocali, consonanti, spazi */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char riga[100];
    printf("Frase: ");
    if (fgets(riga, sizeof riga, stdin) == NULL)   /* lettura sicura: al massimo 99 caratteri */
        return 1;
    riga[strcspn(riga, "\n")] = '\0';              /* elimino l'a capo letto da fgets */

    int vocali = 0, consonanti = 0, spazi = 0;
    for (size_t i = 0; riga[i] != '\0'; i++) {
        char c = (char)tolower((unsigned char)riga[i]);
        if (c == ' ')
            spazi++;
        else if (strchr("aeiou", c) != NULL)       /* c è tra le vocali? */
            vocali++;
        else if (isalpha((unsigned char)c))        /* lettera non vocale */
            consonanti++;
    }
    printf("\"%s\"\n", riga);
    printf("Vocali: %d   Consonanti: %d   Spazi: %d\n", vocali, consonanti, spazi);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Frase: Istituto Tecnico Superiore
"Istituto Tecnico Superiore"
Vocali: 12   Consonanti: 12   Spazi: 2
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

`fgets` conserva il `\n` finale: `strcspn` ne trova la posizione e lo si sostituisce con il terminatore. Il cast a `unsigned char` prima di `tolower`/`isalpha` evita comportamenti indefiniti con i caratteri accentati, che hanno codici negativi se `char` è con segno.

7.3

#### Maiuscolo e palindromi

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione `in_maiuscolo(s)` che converta la stringa sul posto e una funzione `palindromo(s)` che verifichi, ignorando le maiuscole, se una parola si legge uguale nei due sensi. Provarle su un elenco di parole.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 7.3 - Maiuscolo e palindromi */
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

void in_maiuscolo(char s[])
{
    for (size_t i = 0; s[i] != '\0'; i++)
        s[i] = (char)toupper((unsigned char)s[i]);
}

bool palindromo(const char s[])
{
    size_t n = strlen(s);
    if (n == 0)
        return true;
    size_t i = 0, j = n - 1;                /* due indici dai due estremi */
    while (i < j) {
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j]))
            return false;
        i++;
        j--;
    }
    return true;
}

int main(void)
{
    char prove[][16] = {"Anna", "radar", "Osso", "motore", "Ingegni"};   /* array di stringhe */
    int n = sizeof prove / sizeof prove[0];

    for (int k = 0; k < n; k++) {
        char copia[16];
        strcpy(copia, prove[k]);            /* lavoro su una copia: l'originale resta intatto */
        in_maiuscolo(copia);
        printf("%-8s -> %-8s %s\n", prove[k], copia,
               palindromo(prove[k]) ? "palindromo" : "-");
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Anna     -> ANNA     palindromo
radar    -> RADAR    palindromo
Osso     -> OSSO     palindromo
motore   -> MOTORE   -
Ingegni  -> INGEGNI  palindromo
```

Commento

`char prove[][16]` è una matrice di caratteri: 5 righe da 16 byte, ciascuna con una stringa. `%-8s` stampa la stringa allineata a sinistra su 8 caratteri. `strcpy` non controlla la dimensione della destinazione: qui è sicura perché le due dimensioni coincidono.

7.4

#### Parsing di un messaggio di telemetria

*Avanzato*OnlineGDB: Sì

Consegna

Un dispositivo invia messaggi nel formato `chiave=valore;chiave=valore;...`, ad esempio `temp=23.5;hum=61;press=1013.2;stato=OK`. Separare i campi, dividere chiave e valore e stampare i valori numerici come numeri e gli altri come testo.

Suggerimento

`strtok` separa sui `;`, `strchr` trova l'`=`, `strtod` converte il testo in `double` e indica dove si è fermata.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 7.4 - Parsing di un messaggio chiave=valore */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char messaggio[] = "temp=23.5;hum=61;press=1013.2;stato=OK";
    printf("Messaggio: %s\n\n", messaggio);

    /* strtok MODIFICA la stringa: deve essere un array, non una costante */
    char *campo = strtok(messaggio, ";");
    while (campo != NULL) {
        char *uguale = strchr(campo, '=');        /* posizione del carattere '=' */
        if (uguale != NULL) {
            *uguale = '\0';                       /* spezzo "chiave=valore" in due stringhe */
            const char *chiave = campo;
            const char *valore = uguale + 1;      /* il valore inizia dopo '=' */

            char *fine;
            double num = strtod(valore, &fine);   /* testo -> double */
            if (*fine == '\0' && fine != valore)  /* convertita tutta la stringa: è un numero */
                printf("%-6s : %8.2f (numero)\n", chiave, num);
            else
                printf("%-6s : %8s (testo)\n", chiave, valore);
        }
        campo = strtok(NULL, ";");                /* NULL = prosegui sulla stessa stringa */
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Messaggio: temp=23.5;hum=61;press=1013.2;stato=OK

temp   :    23.50 (numero)
hum    :    61.00 (numero)
press  :  1013.20 (numero)
stato  :       OK (testo)
```

Commento

Esercizio ponte verso i puntatori: `campo`, `uguale` e `fine` sono indirizzi di caratteri *dentro* `messaggio`. È la stessa tecnica usata per decodificare stringhe da seriale, MQTT o risposte AT di un modem. `strtod` è preferibile ad `atof` perché permette di riconoscere un valore non numerico.

Parte III

## Memoria e dati

Modulo 8

### Puntatori e memoria dinamica

5 esercizi

Concetti chiave

Un **puntatore** è una variabile che contiene un indirizzo di memoria. `&x` restituisce l'indirizzo di `x`; `*p` (dereferenziazione) accede al valore all'indirizzo contenuto in `p`.

| Scrittura | Significato |
| --- | --- |
| `int *p;` | p è un puntatore a int |
| `p = &x;` | p punta a x |
| `*p = 5;` | scrive 5 in x attraverso p |
| `p + 1` | indirizzo dell'int successivo (avanza di `sizeof(int)` byte) |
| `v[i]` | equivale a `*(v + i)` |

I puntatori servono a tre cose: far modificare variabili a una funzione, scorrere array, gestire memoria **allocata dinamicamente** con `malloc`/`free`. Ogni `malloc` va controllata (può restituire `NULL`) e bilanciata da una `free`.

8.1

#### Indirizzo e dereferenziazione

*Base*OnlineGDB: Sì

Consegna

Dichiarare un intero e un puntatore che lo punta. Stampare il valore, l'indirizzo, il contenuto del puntatore e il valore puntato. Modificare la variabile attraverso il puntatore.

Suggerimento

Gli indirizzi si stampano con `%p`, convertendo il puntatore a `(void *)`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 8.1 - Indirizzo e dereferenziazione */
#include <stdio.h>

int main(void)
{
    int valore = 42;
    int *p = &valore;            /* p contiene l'indirizzo di valore */

    printf("valore   = %d\n", valore);
    printf("&valore  = %p\n", (void *)&valore);
    printf("p        = %p\n", (void *)p);     /* stesso indirizzo */
    printf("*p       = %d\n", *p);            /* valore puntato */

    *p = 99;                     /* scrivo in valore attraverso il puntatore */
    printf("dopo *p = 99 -> valore = %d\n", valore);
    printf("sizeof(p) = %zu byte\n", sizeof p);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
valore   = 42
&valore  = 0x7ffccb4a5b1c
p        = 0x7ffccb4a5b1c
*p       = 42
dopo *p = 99 -> valore = 99
sizeof(p) = 8 byte
```

Commento

Gli indirizzi stampati cambiano a ogni esecuzione: il sistema operativo randomizza la posizione dello stack (ASLR). Un puntatore occupa 8 byte su un PC a 64 bit, 4 byte su ESP32 e 2 byte su Arduino Uno, indipendentemente dal tipo puntato.

8.2

#### Lo scambio, finalmente in una funzione

*Base*OnlineGDB: Sì

Consegna

Scrivere una funzione `scambia_errato(int a, int b)` e una funzione corretta `scambia(int *a, int *b)`. Mostrare che solo la seconda scambia davvero le variabili del chiamante.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 8.2 - Scambio con i puntatori */
#include <stdio.h>

void scambia_errato(int a, int b)     /* riceve COPIE dei valori */
{
    int t = a;
    a = b;
    b = t;
    printf("  (dentro scambia_errato: a=%d b=%d)\n", a, b);
}

void scambia(int *a, int *b)          /* riceve gli INDIRIZZI delle variabili */
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void)
{
    int x = 3, y = 8;
    scambia_errato(x, y);
    printf("dopo scambia_errato: x=%d y=%d\n", x, y);
    scambia(&x, &y);                  /* passo gli indirizzi */
    printf("dopo scambia       : x=%d y=%d\n", x, y);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
  (dentro scambia_errato: a=8 b=3)
dopo scambia_errato: x=3 y=8
dopo scambia       : x=8 y=3
```

Commento

Ora si capisce la `&` di `scanf("%d", &n)`: `scanf` deve *scrivere* in `n`, quindi ha bisogno del suo indirizzo, esattamente come `scambia`.

8.3

#### Aritmetica dei puntatori

*Intermedio*OnlineGDB: Sì

Consegna

Dato un array di 5 interi, mostrare per ogni elemento `v[i]`, `*(p + i)` e la distanza in byte dall'inizio. Calcolare poi la somma scorrendo l'array con un puntatore invece che con un indice.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 8.3 - Aritmetica dei puntatori */
#include <stdio.h>

int main(void)
{
    int v[] = {10, 20, 30, 40, 50};
    int n = sizeof v / sizeof v[0];

    int *p = v;              /* il nome dell'array vale l'indirizzo del primo elemento */
    for (int i = 0; i < n; i++) {
        /* differenza tra puntatori a char = distanza in byte (tipo ptrdiff_t, formato %td) */
        printf("v[%d] = %d   *(p+%d) = %d   offset = %td byte\n",
               i, v[i], i, *(p + i), (char *)(p + i) - (char *)p);
    }

    int somma = 0;
    for (int *q = v; q < v + n; q++)     /* q avanza di un int a ogni passo */
        somma += *q;
    printf("somma = %d\n", somma);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
v[0] = 10   *(p+0) = 10   offset = 0 byte
v[1] = 20   *(p+1) = 20   offset = 4 byte
v[2] = 30   *(p+2) = 30   offset = 8 byte
v[3] = 40   *(p+3) = 40   offset = 12 byte
v[4] = 50   *(p+4) = 50   offset = 16 byte
somma = 150
```

Commento

`p + 1` non aggiunge 1 byte ma `sizeof(int)` byte: l'aritmetica dei puntatori tiene conto del tipo puntato. `v + n` è l'indirizzo "subito dopo l'ultimo elemento": lo standard permette di calcolarlo e confrontarlo, ma non di dereferenziarlo.

8.4

#### Più risultati da una funzione

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione che, dato un array di misure, calcoli minimo, massimo e media restituendoli tramite parametri puntatore. Il valore di ritorno deve indicare l'esito: 0 se tutto è corretto, -1 se l'array è vuoto.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 8.4 - Parametri di uscita */
#include <stdio.h>
#include <stddef.h>

/* restituisce 0 se ok, -1 se l'array è vuoto; i risultati escono dai puntatori */
int statistiche(const double *v, size_t n, double *min, double *max, double *media)
{
    if (v == NULL || n == 0)
        return -1;
    *min = *max = v[0];
    double somma = 0.0;
    for (size_t i = 0; i < n; i++) {
        if (v[i] < *min) *min = v[i];
        if (v[i] > *max) *max = v[i];
        somma += v[i];
    }
    *media = somma / n;
    return 0;
}

int main(void)
{
    double misure[] = {12.02, 11.98, 12.10, 11.95, 12.05, 12.00};   /* correnti in mA */
    size_t n = sizeof misure / sizeof misure[0];
    double mn, mx, md;

    if (statistiche(misure, n, &mn, &mx, &md) == 0)
        printf("min = %.2f mA   max = %.2f mA   media = %.3f mA\n", mn, mx, md);

    if (statistiche(misure, 0, &mn, &mx, &md) != 0)
        printf("array vuoto: errore gestito\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
min = 11.95 mA   max = 12.10 mA   media = 12.017 mA
array vuoto: errore gestito
```

Commento

Valore di ritorno per l'esito, puntatori per i dati: è lo schema di quasi tutte le API C professionali (POSIX, ESP-IDF con `esp_err_t`, driver dei produttori di microcontrollori).

8.5

#### Allocazione dinamica

*Avanzato*OnlineGDB: Sì

Consegna

Chiedere all'utente quante misure vuole inserire, allocare un array della dimensione esatta con `malloc`, leggere le misure e stamparne la media. Ingrandire poi l'array di un elemento con `realloc` e liberare la memoria.

Suggerimento

`malloc(n * sizeof *v)` alloca spazio per n elementi del tipo puntato da `v`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 8.5 - malloc, realloc, free */
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    size_t n;
    printf("Quante misure? ");
    if (scanf("%zu", &n) != 1 || n == 0)
        return 1;

    double *v = malloc(n * sizeof *v);       /* n double allocati sullo heap */
    if (v == NULL) {                         /* controllo SEMPRE l'esito */
        fprintf(stderr, "Memoria insufficiente\n");
        return 1;
    }

    for (size_t i = 0; i < n; i++) {
        printf("Misura %zu: ", i + 1);
        scanf("%lf", &v[i]);                 /* si usa come un normale array */
    }
    double somma = 0.0;
    for (size_t i = 0; i < n; i++)
        somma += v[i];
    printf("\nMedia di %zu misure = %.3f\n", n, somma / n);

    double *tmp = realloc(v, (n + 1) * sizeof *v);   /* ridimensiono */
    if (tmp == NULL) {                       /* in caso di errore v è ancora valido */
        free(v);
        return 1;
    }
    v = tmp;
    v[n] = 0.0;
    printf("Array ridimensionato a %zu elementi\n", n + 1);

    free(v);                                 /* restituisco la memoria */
    v = NULL;                                /* evito un puntatore "pendente" */
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione (in ambra l'input digitato)

terminale

```
$ ./prog
Quante misure? 4
Misura 1: 1.5
Misura 2: 2.5
Misura 3: 3.0
Misura 4: 4.0

Media di 4 misure = 2.750
Array ridimensionato a 5 elementi
```

Su OnlineGDB

Digitare l'input nella console quando il programma lo chiede (modalità *Interactive Console*).

Commento

Il risultato di `realloc` va in un puntatore temporaneo: scrivendo direttamente `v = realloc(v, ...)`, in caso di errore si perderebbe l'unico riferimento alla memoria originale (memory leak). Sui microcontrollori l'allocazione dinamica si evita o si limita alla fase di avvio, per il rischio di frammentazione dell'heap.

Modulo 9

### Strutture ed enumerazioni

4 esercizi

Concetti chiave

Una `struct` raggruppa dati **di tipo diverso** che descrivono una stessa entità. Ai campi si accede con `.` (`p.x`) oppure, tramite un puntatore, con `->` (`pp->x`, equivalente a `(*pp).x`). `typedef` assegna un nome breve al tipo.

Una struct passata per valore viene copiata interamente: per strutture grandi o da modificare si passa un puntatore, aggiungendo `const` se la funzione deve solo leggere.

Un `enum` definisce un insieme di costanti intere con nome: rende leggibili stati, modi operativi e codici di errore. Insieme a `switch` è la base delle **macchine a stati**.

9.1

#### Punti nel piano

*Base*OnlineGDB: Sì

Consegna

Definire una `struct punto` con coordinate `x` e `y`. Scrivere una funzione che calcoli la distanza tra due punti e una che restituisca il punto medio. Provarle con (0, 0) e (3, 4).

Suggerimento

`sqrt` è in `<math.h>`; su Linux occorre collegare la libreria matematica con `-lm`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 9.1 - Struct punto */
#include <stdio.h>
#include <math.h>

struct punto {
    double x;
    double y;
};

double distanza(struct punto a, struct punto b)
{
    double dx = b.x - a.x;
    double dy = b.y - a.y;
    return sqrt(dx * dx + dy * dy);
}

struct punto medio(struct punto a, struct punto b)
{
    struct punto m = { (a.x + b.x) / 2.0, (a.y + b.y) / 2.0 };
    return m;                         /* una struct si può restituire per valore */
}

int main(void)
{
    struct punto p1 = {0.0, 0.0};
    struct punto p2 = {.x = 3.0, .y = 4.0};     /* inizializzatori designati (C99) */
    struct punto m = medio(p1, p2);

    printf("P1 = (%.1f, %.1f)   P2 = (%.1f, %.1f)\n", p1.x, p1.y, p2.x, p2.y);
    printf("Distanza    = %.2f\n", distanza(p1, p2));
    printf("Punto medio = (%.2f, %.2f)\n", m.x, m.y);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog -lm
```

Esecuzione

terminale

```
$ ./prog
P1 = (0.0, 0.0)   P2 = (3.0, 4.0)
Distanza    = 5.00
Punto medio = (1.50, 2.00)
```

Su OnlineGDB

Se il linker segnala `undefined reference to sqrt`, aggiungere `-lm` in *Extra Compiler Flags*.

Commento

`-lm` va scritto **dopo** i file sorgente: il linker risolve i simboli da sinistra a destra. È il primo incontro con il collegamento di una libreria esterna, tema del modulo 12.

9.2

#### Array di strutture: la classe

*Intermedio*OnlineGDB: Sì

Consegna

Definire con `typedef` un tipo `Studente` con nome e tre voti. Creare un array di 4 studenti, stampare la media di ciascuno e il nome dello studente con la media migliore.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 9.2 - Array di struct */
#include <stdio.h>

#define MAX_NOME 20
#define N_VOTI   3

typedef struct {
    char   nome[MAX_NOME];
    double voti[N_VOTI];
} Studente;

double media_studente(const Studente *s)    /* puntatore: evito di copiare la struct */
{
    double somma = 0.0;
    for (int i = 0; i < N_VOTI; i++)
        somma += s->voti[i];                /* -> accede al campo tramite puntatore */
    return somma / N_VOTI;
}

int main(void)
{
    Studente classe[] = {
        {"Rossi",   {7.0, 8.0, 6.5}},
        {"Bianchi", {9.0, 8.5, 9.5}},
        {"Verdi",   {5.5, 6.0, 7.0}},
        {"Neri",    {8.0, 7.5, 8.0}},
    };
    int n = sizeof classe / sizeof classe[0];
    int migliore = 0;

    printf("%-10s %6s\n", "Studente", "Media");
    for (int i = 0; i < n; i++) {
        double m = media_studente(&classe[i]);
        printf("%-10s %6.2f\n", classe[i].nome, m);
        if (m > media_studente(&classe[migliore]))
            migliore = i;
    }
    printf("\nMigliore: %s\n", classe[migliore].nome);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Studente    Media
Rossi        7.17
Bianchi      9.00
Verdi        6.17
Neri         7.83

Migliore: Bianchi
```

Commento

Si memorizza l'*indice* del migliore, non una copia della struct: è più economico e permette di accedere a tutti i suoi campi in seguito.

9.3

#### Sensori: modificare una struct tramite puntatore

*Intermedio*OnlineGDB: Sì

Consegna

Definire un tipo `Sensore` con tag, lettura grezza dell'ADC, guadagno, offset e valore calcolato. Scrivere `calibra(Sensore *s)` che calcoli `valore = grezzo·guadagno + offset` e `stampa_sensore(const Sensore *s)`. Provare con un trasmettitore di pressione 0-10 bar e uno di temperatura -50…+150 °C, entrambi letti da un ADC a 12 bit.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 9.3 - Calibrazione di sensori */
#include <stdio.h>

typedef struct {
    char   tag[12];
    double grezzo;       /* lettura ADC in conteggi */
    double guadagno;     /* unità ingegneristiche per conteggio */
    double offset;
    double valore;       /* risultato calcolato */
} Sensore;

void calibra(Sensore *s)                 /* modifica la struct originale */
{
    s->valore = s->grezzo * s->guadagno + s->offset;
}

void stampa_sensore(const Sensore *s)    /* const: sola lettura */
{
    printf("%-6s grezzo = %5.0f  ->  %8.2f\n", s->tag, s->grezzo, s->valore);
}

int main(void)
{
    /* ADC a 12 bit: 0..4095 conteggi */
    Sensore s[] = {
        {"PT01", 2048, 10.0 / 4095.0,   0.0, 0.0},   /* 0..10 bar      */
        {"TT01", 1500, 200.0 / 4095.0, -50.0, 0.0},  /* -50..+150 gradi */
    };
    size_t n = sizeof s / sizeof s[0];

    for (size_t i = 0; i < n; i++) {
        calibra(&s[i]);
        stampa_sensore(&s[i]);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
PT01   grezzo =  2048  ->      5.00
TT01   grezzo =  1500  ->     23.26
```

Commento

Il calcolo è una retta `y = m·x + q`: guadagno = (fondo scala − inizio scala) / conteggi, offset = inizio scala. La stessa struttura dati si ritrova nei blocchi di scalatura dei PLC.

9.4

#### Macchina a stati: il semaforo

*Avanzato*OnlineGDB: Sì

Consegna

Modellare un semaforo con un `enum` a tre stati (ROSSO, VERDE, GIALLO). Scrivere le funzioni che restituiscono il nome dello stato, lo stato successivo e la durata di ciascuno stato (30, 25, 5 s). Simulare 7 transizioni stampando il tempo trascorso.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 9.4 - Macchina a stati con enum */
#include <stdio.h>

typedef enum { ROSSO, VERDE, GIALLO } Stato;   /* valgono 0, 1, 2 */

const char *nome_stato(Stato s)
{
    switch (s) {
    case ROSSO:  return "ROSSO";
    case VERDE:  return "VERDE";
    case GIALLO: return "GIALLO";
    }
    return "?";
}

Stato prossimo(Stato s)                /* tabella delle transizioni */
{
    switch (s) {
    case ROSSO:  return VERDE;
    case VERDE:  return GIALLO;
    case GIALLO: return ROSSO;
    }
    return ROSSO;                      /* stato sconosciuto: posizione sicura */
}

int durata(Stato s)                    /* secondi di permanenza */
{
    static const int t[] = { [ROSSO] = 30, [VERDE] = 25, [GIALLO] = 5 };
    return t[s];
}

int main(void)
{
    Stato s = ROSSO;
    int tempo = 0;
    for (int ciclo = 0; ciclo < 7; ciclo++) {
        printf("t = %3d s   %-6s (per %2d s)\n", tempo, nome_stato(s), durata(s));
        tempo += durata(s);
        s = prossimo(s);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
t =   0 s   ROSSO  (per 30 s)
t =  30 s   VERDE  (per 25 s)
t =  55 s   GIALLO (per  5 s)
t =  60 s   ROSSO  (per 30 s)
t =  90 s   VERDE  (per 25 s)
t = 115 s   GIALLO (per  5 s)
t = 120 s   ROSSO  (per 30 s)
```

Commento

Con `-Wall` il compilatore avvisa se uno `switch` su un `enum` dimentica un valore: aggiungendo uno stato (es. LAMPEGGIANTE) si viene guidati a gestirlo ovunque. Il `return ROSSO` finale è lo stato di sicurezza, concetto chiave nelle macchine industriali.

Modulo 10

### File

4 esercizi

Concetti chiave

Un file si apre con `fopen(nome, modo)`, che restituisce un `FILE *` oppure `NULL` in caso di errore (da controllare sempre). Si chiude con `fclose`, che scrive su disco i dati ancora nel buffer.

| Modo | Effetto |
| --- | --- |
| `"r"` | lettura; il file deve esistere |
| `"w"` | scrittura; crea o **azzera** il file |
| `"a"` | scrittura in coda (append) |
| `"rb"`, `"wb"` | come sopra, in modalità binaria |

File di testo: `fprintf`, `fscanf`, `fgets`, `fgetc`. File binari: `fwrite` e `fread` copiano blocchi di memoria così come sono. `perror` stampa la causa dell'ultimo errore di sistema.

10.1

#### Scrivere, accodare e rileggere

*Base*OnlineGDB: Sì

Consegna

Creare il file `note.txt` scrivendo un titolo e tre righe numerate; riaprirlo in modalità append per aggiungere una riga; infine rileggerlo stampando ogni riga preceduta dal suo numero.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 10.1 - Scrivere, accodare, rileggere */
#include <stdio.h>

int main(void)
{
    const char *nome_file = "note.txt";

    FILE *f = fopen(nome_file, "w");          /* "w": crea o sovrascrive */
    if (f == NULL) { perror(nome_file); return 1; }
    fprintf(f, "Corso ITS - Programmazione C\n");
    for (int i = 1; i <= 3; i++)
        fprintf(f, "Riga %d\n", i);
    fclose(f);                                /* chiudere SEMPRE */

    f = fopen(nome_file, "a");                /* "a": aggiunge in coda */
    if (f == NULL) { perror(nome_file); return 1; }
    fprintf(f, "Riga aggiunta in append\n");
    fclose(f);

    f = fopen(nome_file, "r");                /* "r": sola lettura */
    if (f == NULL) { perror(nome_file); return 1; }
    char riga[128];
    int n = 0;
    while (fgets(riga, sizeof riga, f) != NULL)   /* NULL a fine file */
        printf("%2d| %s", ++n, riga);             /* riga contiene già il \n */
    fclose(f);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
 1| Corso ITS - Programmazione C
 2| Riga 1
 3| Riga 2
 4| Riga 3
 5| Riga aggiunta in append
```

Commento

Riaprire il file con `"w"` invece di `"a"` cancellerebbe il contenuto precedente. Prova a impostare `nome_file` su un percorso inesistente (es. `"/xyz/note.txt"`) per vedere il messaggio di `perror`.

10.2

#### Log di misure in formato CSV

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere in `misure.csv` un'intestazione e 5 righe `campione;tensione_V;corrente_mA`. Rileggere il file saltando l'intestazione, calcolare per ogni riga la potenza in mW e infine la potenza media.

Suggerimento

`fscanf(f, "%d;%lf;%lf", ...)` restituisce il numero di campi letti: il ciclo continua finché vale 3.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 10.2 - Log CSV */
#include <stdio.h>

int main(void)
{
    const char *nome = "misure.csv";

    FILE *f = fopen(nome, "w");
    if (f == NULL) { perror(nome); return 1; }
    fprintf(f, "campione;tensione_V;corrente_mA\n");          /* intestazione */
    double v[]    = {4.98, 5.01, 5.03, 4.97, 5.00};
    double i_ma[] = {12.1, 12.4, 11.9, 12.0, 12.3};
    for (int k = 0; k < 5; k++)
        fprintf(f, "%d;%.2f;%.1f\n", k + 1, v[k], i_ma[k]);
    fclose(f);

    f = fopen(nome, "r");
    if (f == NULL) { perror(nome); return 1; }
    char intestazione[100];
    if (fgets(intestazione, sizeof intestazione, f) == NULL) {  /* salto la prima riga */
        fclose(f);
        return 1;
    }

    int id, n = 0;
    double tens, corr, somma_p = 0.0;
    while (fscanf(f, "%d;%lf;%lf", &id, &tens, &corr) == 3) {  /* 3 campi = riga valida */
        double p_mw = tens * corr;                              /* V x mA = mW */
        printf("campione %d: %.2f V  %.1f mA  P = %.1f mW\n", id, tens, corr, p_mw);
        somma_p += p_mw;
        n++;
    }
    fclose(f);

    if (n > 0)
        printf("Potenza media = %.2f mW su %d campioni\n", somma_p / n, n);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
campione 1: 4.98 V  12.1 mA  P = 60.3 mW
campione 2: 5.01 V  12.4 mA  P = 62.1 mW
campione 3: 5.03 V  11.9 mA  P = 59.9 mW
campione 4: 4.97 V  12.0 mA  P = 59.6 mW
campione 5: 5.00 V  12.3 mA  P = 61.5 mW
Potenza media = 60.68 mW su 5 campioni
```

Commento

Il separatore `;` rende il file apribile direttamente con Excel in localizzazione italiana, dove la virgola è il separatore decimale. Il file prodotto si può controllare con `cat misure.csv`.

10.3

#### Contare righe, parole e caratteri (argomenti da riga di comando)

*Avanzato*OnlineGDB: Sì, con argomenti

Consegna

Scrivere un programma che riceva il nome di un file come **argomento da riga di comando** e ne stampi il numero di righe, parole e caratteri (come il comando `wc`). Se l'argomento manca, stampare le istruzioni d'uso.

Suggerimento

`int main(int argc, char *argv[])`: `argc` è il numero di argomenti, `argv[0]` il nome del programma, `argv[1]` il primo argomento.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 10.3 - wc semplificato con argc/argv */
#include <stdio.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Uso: %s nome_file\n", argv[0]);
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL) { perror(argv[1]); return 1; }

    long caratteri = 0, parole = 0, righe = 0;
    int in_parola = 0;
    int c;                              /* int, non char: deve poter contenere EOF */
    while ((c = fgetc(f)) != EOF) {
        caratteri++;
        if (c == '\n')
            righe++;
        if (isspace(c)) {
            in_parola = 0;              /* spazio, tab o a capo: fine parola */
        } else if (!in_parola) {        /* primo carattere di una nuova parola */
            in_parola = 1;
            parole++;
        }
    }
    fclose(f);
    printf("%s: %ld righe, %ld parole, %ld caratteri\n", argv[1], righe, parole, caratteri);
    return 0;
}
```

testo.txtdati

```
Il linguaggio C nasce nel 1972
ai Bell Labs per scrivere UNIX.
Oggi e' il linguaggio dei microcontrollori.
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog testo.txt
testo.txt: 3 righe, 18 parole, 107 caratteri
$ wc testo.txt
  3  18 107 testo.txt
$ ./prog
Uso: ./prog nome_file
```

Su OnlineGDB

Creare il file `testo.txt` con il pulsante *New File* e incollarvi il contenuto; scrivere `testo.txt` nel campo *Command line arguments*. Il confronto con `wc` va fatto in locale.

Commento

Il confronto con `wc` (che stampa righe, parole, byte) permette di verificare il programma. La variabile `in_parola` è una piccola macchina a stati a due stati. I messaggi di errore vanno su `stderr`, così non si mescolano con l'output utile se questo viene rediretto su file.

10.4

#### File binari e accesso diretto

*Avanzato*OnlineGDB: Sì

Consegna

Definire un record `{id, temperatura, umidita}`, scriverne 3 in `log.bin` con una sola `fwrite`, rileggerli con `fread` e stamparli. Usare infine `fseek` per leggere direttamente il secondo record.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 10.4 - File binari */
#include <stdio.h>

typedef struct {
    int   id;
    float temperatura;
    float umidita;
} Record;

int main(void)
{
    Record dati[] = { {1, 21.5f, 45.0f}, {2, 22.1f, 47.5f}, {3, 22.8f, 50.2f} };
    size_t n = sizeof dati / sizeof dati[0];

    FILE *f = fopen("log.bin", "wb");                    /* "b": modalità binaria */
    if (f == NULL) { perror("log.bin"); return 1; }
    size_t scritti = fwrite(dati, sizeof(Record), n, f); /* tutto l'array in un colpo */
    fclose(f);
    printf("Scritti %zu record da %zu byte\n", scritti, sizeof(Record));

    Record letti[10];
    f = fopen("log.bin", "rb");
    if (f == NULL) { perror("log.bin"); return 1; }
    size_t m = fread(letti, sizeof(Record), 10, f);      /* ne chiedo 10, ottengo m */
    printf("Letti %zu record, file di %ld byte\n", m, ftell(f));
    for (size_t i = 0; i < m; i++)
        printf("  id=%d  T=%.1f C  RH=%.1f %%\n",
               letti[i].id, letti[i].temperatura, letti[i].umidita);

    fseek(f, (long)sizeof(Record), SEEK_SET);           /* salto al 2° record */
    Record r;
    if (fread(&r, sizeof r, 1, f) == 1)
        printf("Accesso diretto al record 2: id=%d T=%.1f C\n", r.id, r.temperatura);
    fclose(f);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Scritti 3 record da 12 byte
Letti 3 record, file di 36 byte
  id=1  T=21.5 C  RH=45.0 %
  id=2  T=22.1 C  RH=47.5 %
  id=3  T=22.8 C  RH=50.2 %
Accesso diretto al record 2: id=2 T=22.1 C
```

Commento

Un file binario è compatto e permette l'accesso diretto (posizione = indice × dimensione record), ma **non è portabile**: dimensione dei tipi, padding delle struct e ordine dei byte (endianness) dipendono dalla piattaforma. Per scambiare dati tra un ESP32 e un PC si preferiscono formati testuali (CSV, JSON) o binari con layout definito campo per campo.

Parte IV

## Dal programma alla libreria

Modulo 11

### Programmazione modulare: header e compilazione separata

3 esercizi

Concetti chiave

Un progetto reale si divide in **moduli**: per ciascuno un file header `.h` (l'*interfaccia*: prototipi, tipi, costanti) e un file `.c` (l'*implementazione*). Chi usa il modulo include solo l'header.

La costruzione di un eseguibile avviene in due fasi: la **compilazione** trasforma ogni `.c` in un file oggetto `.o`, indipendentemente dagli altri; il **linking** unisce i `.o` risolvendo i riferimenti tra loro.

modulo.c*gcc -c*modulo.omain.o + modulo.o*gcc (linker)*eseguibile

| Elemento | Ruolo |
| --- | --- |
| `#ifndef X_H / #define X_H / #endif` | **include guard**: impedisce che l'header venga incluso due volte |
| `#include "x.h"` | header del progetto (cercato prima nella cartella corrente) |
| `#include <x.h>` | header di sistema |
| `static` (fuori dalle funzioni) | simbolo **privato** del file .c |
| `extern` | dichiara una variabile definita in un altro file |

11.1

#### Il primo modulo

*Intermedio*OnlineGDB: Sì, multi-file

Consegna

Spostare in un modulo `matematica` (header + implementazione) le funzioni `area_cerchio`, `area_rettangolo`, `massimo` e la costante `PI_GRECO`. Il `main.c` deve usarle includendo solo `matematica.h`.

Mostra la soluzioneNascondi la soluzione

matematica.hC

```
/* matematica.h - interfaccia del modulo: solo DICHIARAZIONI */
#ifndef MATEMATICA_H        /* include guard */
#define MATEMATICA_H

#define PI_GRECO 3.14159265358979

double area_cerchio(double r);
double area_rettangolo(double b, double h);
int    massimo(int a, int b);

#endif /* MATEMATICA_H */
```

matematica.cC

```
/* matematica.c - implementazione del modulo */
#include "matematica.h"      /* l'implementazione include il proprio header */

double area_cerchio(double r)
{
    return PI_GRECO * r * r;
}

double area_rettangolo(double b, double h)
{
    return b * h;
}

int massimo(int a, int b)
{
    return (a > b) ? a : b;
}
```

main.cC

```
/* main.c - usa il modulo matematica */
#include <stdio.h>
#include "matematica.h"      /* virgolette: header del progetto */

int main(void)
{
    printf("Area cerchio r=2      : %.3f\n", area_cerchio(2.0));
    printf("Area rettangolo 3 x 4 : %.1f\n", area_rettangolo(3.0, 4.0));
    printf("Massimo tra 7 e 12    : %d\n", massimo(7, 12));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c matematica.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Area cerchio r=2      : 12.566
Area rettangolo 3 x 4 : 12.0
Massimo tra 7 e 12    : 12
```

Su OnlineGDB

Aggiungere `matematica.h` e `matematica.c` con *New File*: OnlineGDB compila automaticamente tutti i `.c` del progetto.

Commento

Il file `.c` include il proprio header: così il compilatore verifica che prototipi e definizioni coincidano. Nel comando di compilazione si elencano solo i `.c`, mai gli `.h`: gli header vengono letti tramite `#include`.

11.2

#### Compilazione separata, static ed extern

*Avanzato*OnlineGDB: Parziale

Consegna

Realizzare un modulo `contatore` che registri eventi e conti gli errori. Il numero di errori deve essere leggibile da `main` (`extern`); il conteggio totale degli eventi e una funzione di formattazione devono restare privati del modulo (`static`). Compilare i due file separatamente, collegarli e ispezionare i simboli con `nm`.

Mostra la soluzioneNascondi la soluzione

contatore.hC

```
/* contatore.h */
#ifndef CONTATORE_H
#define CONTATORE_H

extern int contatore_errori;     /* dichiarazione: la variabile è DEFINITA in contatore.c */

void registra_evento(const char *msg, int errore);
void stampa_riepilogo(void);

#endif /* CONTATORE_H */
```

contatore.cC

```
/* contatore.c */
#include <stdio.h>
#include "contatore.h"

int contatore_errori = 0;          /* definizione: una sola in tutto il programma */
static int contatore_eventi = 0;   /* static: visibile SOLO in questo file */

static void intestazione(void)     /* funzione privata del modulo */
{
    printf("[%04d] ", contatore_eventi);
}

void registra_evento(const char *msg, int errore)
{
    contatore_eventi++;
    if (errore)
        contatore_errori++;
    intestazione();
    printf("%s%s\n", errore ? "ERRORE: " : "", msg);
}

void stampa_riepilogo(void)
{
    printf("Eventi: %d, di cui errori: %d\n", contatore_eventi, contatore_errori);
}
```

main.cC

```
/* main.c */
#include <stdio.h>
#include "contatore.h"

int main(void)
{
    registra_evento("Avvio impianto", 0);
    registra_evento("Pressione bassa", 1);
    registra_evento("Ciclo completato", 0);
    registra_evento("Timeout RS485", 1);
    stampa_riepilogo();

    printf("Errori letti da main tramite extern: %d\n", contatore_errori);
    /* contatore_eventi++;   -> errore: simbolo static, invisibile da qui */
    return 0;
}
```

Compilazione

```
# 1) compilazione: ogni .c diventa un .o
$ gcc -Wall -Wextra -std=c11 -c contatore.c
$ gcc -Wall -Wextra -std=c11 -c main.c
# 2) linking: i .o diventano un eseguibile
$ gcc main.o contatore.o -o prog
```

Esecuzione

terminale

```
$ ./prog
[0001] Avvio impianto
[0002] ERRORE: Pressione bassa
[0003] Ciclo completato
[0004] ERRORE: Timeout RS485
Eventi: 4, di cui errori: 2
Errori letti da main tramite extern: 2
$ nm contatore.o
0000000000000000 B contatore_errori
0000000000000004 b contatore_eventi
0000000000000000 t intestazione
                 U printf
0000000000000027 T registra_evento
0000000000000097 T stampa_riepilogo
```

Su OnlineGDB

Il programma gira come progetto multi-file (`contatore.h`, `contatore.c`). La compilazione separata con `-c` e l'ispezione con `nm` richiedono un terminale locale.

Commento

Nell'output di `nm`: `T` = funzione pubblica, `t` = funzione privata (static), `B`/`b` = variabile pubblica/privata non inizializzata o a zero, `U` = simbolo usato ma definito altrove (qui `printf`, risolto dal linker con la libreria C). Con la compilazione separata, se si modifica solo `main.c` basta ricompilare quel file e ricollegare: è il principio su cui si basa `make`.

11.3

#### Modulo ring buffer

*Progetto*OnlineGDB: Sì, multi-file

Consegna

Realizzare un modulo **buffer circolare** (FIFO a capacità fissa, 8 interi) con interfaccia `rb_init`, `rb_push`, `rb_pop`, `rb_size`, `rb_vuoto`, `rb_pieno`. `rb_push` deve rifiutare l'inserimento se il buffer è pieno, `rb_pop` deve segnalare il buffer vuoto. Nel `main` verificare riempimento, svuotamento parziale e *wrap-around* degli indici.

Suggerimento

Indice di scrittura (testa), indice di lettura (coda) e conteggio; gli indici avanzano con `(i + 1) % CAPACITA`.

Mostra la soluzioneNascondi la soluzione

ringbuf.hC

```
/* ringbuf.h - buffer circolare (FIFO) a capacità fissa */
#ifndef RINGBUF_H
#define RINGBUF_H

#include <stdbool.h>
#include <stddef.h>

#define RB_CAPACITA 8

typedef struct {
    int    dati[RB_CAPACITA];
    size_t testa;        /* prossima posizione di scrittura */
    size_t coda;         /* prossima posizione di lettura   */
    size_t conteggio;    /* elementi presenti               */
} RingBuffer;

void   rb_init(RingBuffer *rb);
bool   rb_push(RingBuffer *rb, int valore);    /* false se pieno */
bool   rb_pop(RingBuffer *rb, int *valore);    /* false se vuoto */
size_t rb_size(const RingBuffer *rb);
bool   rb_vuoto(const RingBuffer *rb);
bool   rb_pieno(const RingBuffer *rb);

#endif /* RINGBUF_H */
```

ringbuf.cC

```
/* ringbuf.c */
#include "ringbuf.h"

void rb_init(RingBuffer *rb)
{
    rb->testa = 0;
    rb->coda = 0;
    rb->conteggio = 0;
}

bool rb_pieno(const RingBuffer *rb)
{
    return rb->conteggio == RB_CAPACITA;
}

bool rb_vuoto(const RingBuffer *rb)
{
    return rb->conteggio == 0;
}

size_t rb_size(const RingBuffer *rb)
{
    return rb->conteggio;
}

bool rb_push(RingBuffer *rb, int valore)
{
    if (rb_pieno(rb))
        return false;
    rb->dati[rb->testa] = valore;
    rb->testa = (rb->testa + 1) % RB_CAPACITA;   /* dopo l'ultima cella torna a 0 */
    rb->conteggio++;
    return true;
}

bool rb_pop(RingBuffer *rb, int *valore)
{
    if (rb_vuoto(rb))
        return false;
    *valore = rb->dati[rb->coda];
    rb->coda = (rb->coda + 1) % RB_CAPACITA;
    rb->conteggio--;
    return true;
}
```

main.cC

```
/* main.c - test del ring buffer */
#include <stdio.h>
#include "ringbuf.h"

int main(void)
{
    RingBuffer rb;
    rb_init(&rb);

    for (int i = 1; i <= 10; i++)                 /* 10 inserimenti su 8 posti */
        if (!rb_push(&rb, i * 10))
            printf("push %3d rifiutato: buffer pieno\n", i * 10);
    printf("elementi: %zu\n", rb_size(&rb));

    int v;
    printf("pop:");
    for (int k = 0; k < 3 && rb_pop(&rb, &v); k++)
        printf(" %d", v);
    printf("\n");

    rb_push(&rb, 111);                            /* la testa torna all'inizio: wrap-around */
    rb_push(&rb, 222);

    printf("svuoto:");
    while (rb_pop(&rb, &v))
        printf(" %d", v);
    printf("\nvuoto = %s\n", rb_vuoto(&rb) ? "si" : "no");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c ringbuf.c -o prog
```

Esecuzione

terminale

```
$ ./prog
push  90 rifiutato: buffer pieno
push 100 rifiutato: buffer pieno
elementi: 8
pop: 10 20 30
svuoto: 40 50 60 70 80 111 222
vuoto = si
```

Su OnlineGDB

Aggiungere `ringbuf.h` e `ringbuf.c` con *New File*.

Commento

Il ring buffer è la struttura con cui i driver UART di Arduino ed ESP32 accumulano i byte ricevuti in interrupt in attesa che il programma li legga con `Serial.read()`. Il `main` conosce solo l'interfaccia: l'implementazione potrebbe cambiare (es. capacità potenza di 2 con maschera al posto di `%`) senza modificarlo.

Modulo 12

### Librerie statiche, dinamiche e Makefile

3 esercizi

Concetti chiave

Una **libreria** è un insieme di file oggetto pronto per essere riutilizzato, distribuito insieme ai suoi header.

|  | Statica | Dinamica (condivisa) |
| --- | --- | --- |
| File (Linux) | `libnome.a` | `libnome.so` |
| File (Windows) | `libnome.a` / `nome.lib` | `nome.dll` |
| Creazione | `ar rcs` | `gcc -shared -fPIC` |
| Quando entra nel programma | al link: il codice viene copiato nell'eseguibile | all'avvio: caricata dal sistema operativo |
| Aggiornamento | serve ricollegare il programma | basta sostituire il file .so |

Per collegare una libreria: `-L<cartella>` indica dove cercarla, `-l<nome>` quale usare (`-lgeometria` cerca `libgeometria.a` o `libgeometria.so`). È lo stesso meccanismo di `-lm`, visto nell'esercizio 9.1.

**make** automatizza la costruzione: un `Makefile` descrive per ogni file *da cosa dipende* e *come si costruisce*; make ricompila solo ciò che è cambiato.

12.1

#### Libreria statica di geometria

*Avanzato*OnlineGDB: Parziale

Consegna

Creare una libreria statica `libgeometria.a` che fornisca un tipo `Triangolo` e le funzioni `triangolo_valido`, `triangolo_perimetro`, `triangolo_area` (formula di Erone) e `triangolo_tipo`. Elencarne il contenuto con `ar t` e usarla da un programma che analizza tre triangoli.

Mostra la soluzioneNascondi la soluzione

geometria.hC

```
/* geometria.h - interfaccia pubblica della libreria */
#ifndef GEOMETRIA_H
#define GEOMETRIA_H

typedef struct { double a, b, c; } Triangolo;

int         triangolo_valido(Triangolo t);
double      triangolo_perimetro(Triangolo t);
double      triangolo_area(Triangolo t);       /* formula di Erone */
const char *triangolo_tipo(Triangolo t);

#endif /* GEOMETRIA_H */
```

geometria.cC

```
/* geometria.c */
#include <math.h>
#include "geometria.h"

int triangolo_valido(Triangolo t)
{
    /* lati positivi e disuguaglianza triangolare */
    return t.a > 0 && t.b > 0 && t.c > 0 &&
           t.a + t.b > t.c && t.a + t.c > t.b && t.b + t.c > t.a;
}

double triangolo_perimetro(Triangolo t)
{
    return t.a + t.b + t.c;
}

double triangolo_area(Triangolo t)
{
    double p = triangolo_perimetro(t) / 2.0;          /* semiperimetro */
    return sqrt(p * (p - t.a) * (p - t.b) * (p - t.c));
}

const char *triangolo_tipo(Triangolo t)
{
    if (t.a == t.b && t.b == t.c)
        return "equilatero";
    if (t.a == t.b || t.b == t.c || t.a == t.c)
        return "isoscele";
    return "scaleno";
}
```

main.cC

```
/* main.c - programma che usa libgeometria */
#include <stdio.h>
#include "geometria.h"

int main(void)
{
    Triangolo tr[] = { {3, 4, 5}, {2, 2, 2}, {1, 2, 10} };
    int n = sizeof tr / sizeof tr[0];

    for (int i = 0; i < n; i++) {
        printf("(%g, %g, %g): ", tr[i].a, tr[i].b, tr[i].c);
        if (!triangolo_valido(tr[i])) {
            printf("non è un triangolo\n");
            continue;
        }
        printf("%-10s perimetro = %5.2f   area = %5.3f\n",
               triangolo_tipo(tr[i]), triangolo_perimetro(tr[i]), triangolo_area(tr[i]));
    }
    return 0;
}
```

Compilazione

```
# 1) compilo il modulo della libreria
$ gcc -Wall -Wextra -std=c11 -c geometria.c -o geometria.o
# 2) creo l'archivio statico (r: inserisci, c: crea, s: indice dei simboli)
$ ar rcs libgeometria.a geometria.o
# 3) collego il programma alla libreria (-L. = cerca nella cartella corrente)
$ gcc -Wall -Wextra -std=c11 main.c -L. -lgeometria -lm -o prog
```

Esecuzione

terminale

```
$ ar t libgeometria.a
geometria.o
$ ./prog
(3, 4, 5): scaleno    perimetro = 12.00   area = 6.000
(2, 2, 2): equilatero perimetro =  6.00   area = 1.732
(1, 2, 10): non è un triangolo
```

Su OnlineGDB

Il codice gira come progetto multi-file (geometria.h/.c + main.c), eventualmente con `-lm` in *Extra Compiler Flags*. La creazione della libreria con `ar`, che è l'obiettivo dell'esercizio, richiede un terminale locale.

Commento

Chi riceve la libreria ha bisogno solo di `geometria.h` e `libgeometria.a`, non del sorgente. L'eseguibile finale è autonomo: si può cancellare `libgeometria.a` e il programma continua a funzionare, perché il codice è stato copiato al momento del link. `-lm` serve perché la libreria usa `sqrt`.

12.2

#### Libreria dinamica di conversioni per strumentazione

*Progetto*OnlineGDB: Parziale

Consegna

Creare una libreria dinamica `libconversioni.so` con tre funzioni: conversione conteggi ADC → volt (dati numero di bit e tensione di riferimento), scalatura di un segnale 4-20 mA nel range ingegneristico, diagnostica di guasto secondo NAMUR NE43 (corrente ≤ 3,6 mA o ≥ 21 mA). Eseguire il programma prima senza e poi con `LD_LIBRARY_PATH`, e verificare con `ldd` la dipendenza dalla libreria.

Mostra la soluzioneNascondi la soluzione

conversioni.hC

```
/* conversioni.h - conversioni per strumentazione */
#ifndef CONVERSIONI_H
#define CONVERSIONI_H

/* ADC a 'bit' bit con riferimento 'vref' volt: conteggi -> volt */
double adc_a_volt(unsigned conteggi, unsigned bit, double vref);

/* loop 4-20 mA: corrente -> valore ingegneristico nel range [min, max] */
double ma_a_valore(double ma, double min, double max);

/* diagnostica NAMUR NE43: restituisce 1 se la corrente segnala un guasto */
int ma_guasto(double ma);

#endif /* CONVERSIONI_H */
```

conversioni.cC

```
/* conversioni.c */
#include "conversioni.h"

double adc_a_volt(unsigned conteggi, unsigned bit, double vref)
{
    unsigned fondo_scala = (1u << bit) - 1u;      /* es. 12 bit -> 4095 */
    return (double)conteggi * vref / fondo_scala;
}

double ma_a_valore(double ma, double min, double max)
{
    return min + (ma - 4.0) * (max - min) / 16.0; /* 16 mA = escursione 4..20 */
}

int ma_guasto(double ma)
{
    return ma <= 3.6 || ma >= 21.0;
}
```

main.cC

```
/* main.c - usa libconversioni.so */
#include <stdio.h>
#include "conversioni.h"

int main(void)
{
    unsigned letture[] = {0, 2048, 4095};
    for (int i = 0; i < 3; i++)
        printf("ADC %4u -> %.3f V\n", letture[i], adc_a_volt(letture[i], 12, 3.3));

    double correnti[] = {4.0, 12.0, 20.0, 2.5};
    for (int i = 0; i < 4; i++) {
        if (ma_guasto(correnti[i]))
            printf("%5.1f mA -> GUASTO (NAMUR NE43)\n", correnti[i]);
        else
            printf("%5.1f mA -> %5.2f bar\n", correnti[i], ma_a_valore(correnti[i], 0.0, 10.0));
    }
    return 0;
}
```

Compilazione

```
# -fPIC: codice indipendente dalla posizione, necessario per le librerie condivise
$ gcc -Wall -Wextra -std=c11 -fPIC -c conversioni.c -o conversioni.o
$ gcc -shared -o libconversioni.so conversioni.o
$ gcc -Wall -Wextra -std=c11 main.c -L. -lconversioni -o prog
```

Esecuzione

terminale

```
$ ./prog
./prog: error while loading shared libraries: libconversioni.so: cannot open shared object file: No such file or directory
$ LD_LIBRARY_PATH=. ./prog
ADC    0 -> 0.000 V
ADC 2048 -> 1.650 V
ADC 4095 -> 3.300 V
  4.0 mA ->  0.00 bar
 12.0 mA ->  5.00 bar
 20.0 mA -> 10.00 bar
  2.5 mA -> GUASTO (NAMUR NE43)
$ LD_LIBRARY_PATH=. ldd ./prog | grep conversioni
	libconversioni.so => ./libconversioni.so (0x00007f6c8dfb0000)
```

Su OnlineGDB

Le funzioni si provano come progetto multi-file. Libreria `.so`, `LD_LIBRARY_PATH` e `ldd` richiedono un terminale locale.

Commento

Il primo avvio fallisce: il linker sa dove si trova la libreria (`-L.`), ma al momento dell'esecuzione è il *loader* del sistema a cercarla, nelle cartelle standard (`/usr/lib`...) o in quelle indicate da `LD_LIBRARY_PATH`. In produzione la libreria si installa in una cartella di sistema e si esegue `sudo ldconfig`. Su Windows il file si chiama `conversioni.dll` e viene cercato nella cartella dell'eseguibile e nel `PATH`.

12.3

#### Progetto finale: libreria di statistica e Makefile

*Progetto*OnlineGDB: Parziale

Consegna

Realizzare una libreria statica `libstat.a` che (1) legga da un file di testo valori numerici uno per riga, ignorando le righe di commento (`#`) e quelle non numeriche, e (2) ne calcoli numero di campioni, minimo, massimo, media e deviazione standard campionaria. Scrivere il programma `analizza` che riceve il nome del file da riga di comando. Automatizzare la costruzione con un `Makefile` con i target `all`, `run`, `clean`, e verificare che make ricompili solo ciò che è cambiato.

Suggerimento

Nel Makefile le righe di comando devono iniziare con un carattere **TAB**, non con spazi. `$@` = target, `$<` = prima dipendenza, `$^` = tutte le dipendenze.

Mostra la soluzioneNascondi la soluzione

stat.hC

```
/* stat.h - libreria di statistica descrittiva */
#ifndef STAT_H
#define STAT_H

#include <stddef.h>

typedef struct {
    size_t n;
    double min, max, media, devstd;
} Statistiche;

/* calcola le statistiche di v[0..n-1]; 0 se ok, -1 se n == 0 */
int stat_calcola(const double *v, size_t n, Statistiche *out);

/* legge al massimo 'max' valori da un file di testo (uno per riga);
   restituisce il numero di valori letti, -1 se il file non si apre */
long stat_leggi_file(const char *percorso, double *v, size_t max);

#endif /* STAT_H */
```

stat.cC

```
/* stat.c */
#include <stdio.h>
#include <math.h>
#include "stat.h"

int stat_calcola(const double *v, size_t n, Statistiche *out)
{
    if (v == NULL || out == NULL || n == 0)
        return -1;

    double somma = 0.0;
    out->min = out->max = v[0];
    for (size_t i = 0; i < n; i++) {
        somma += v[i];
        if (v[i] < out->min) out->min = v[i];
        if (v[i] > out->max) out->max = v[i];
    }
    out->n = n;
    out->media = somma / n;

    double sq = 0.0;                              /* somma degli scarti al quadrato */
    for (size_t i = 0; i < n; i++) {
        double d = v[i] - out->media;
        sq += d * d;
    }
    out->devstd = (n > 1) ? sqrt(sq / (n - 1)) : 0.0;   /* deviazione standard campionaria */
    return 0;
}

long stat_leggi_file(const char *percorso, double *v, size_t max)
{
    FILE *f = fopen(percorso, "r");
    if (f == NULL)
        return -1;

    char riga[64];
    size_t n = 0;
    while (n < max && fgets(riga, sizeof riga, f) != NULL) {
        if (riga[0] == '#')
            continue;                             /* commento */
        if (sscanf(riga, "%lf", &v[n]) == 1)      /* righe non numeriche scartate */
            n++;
    }
    fclose(f);
    return (long)n;
}
```

main.cC

```
/* main.c - programma "analizza" */
#include <stdio.h>
#include "stat.h"

#define MAX_VALORI 1000

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Uso: %s file_misure\n", argv[0]);
        return 1;
    }

    static double valori[MAX_VALORI];     /* static: fuori dallo stack */
    long n = stat_leggi_file(argv[1], valori, MAX_VALORI);
    if (n < 0) {
        perror(argv[1]);
        return 1;
    }

    Statistiche s;
    if (stat_calcola(valori, (size_t)n, &s) != 0) {
        fprintf(stderr, "Nessun valore valido in %s\n", argv[1]);
        return 1;
    }
    printf("File      : %s\n", argv[1]);
    printf("Campioni  : %zu\n", s.n);
    printf("Minimo    : %.3f\n", s.min);
    printf("Massimo   : %.3f\n", s.max);
    printf("Media     : %.3f\n", s.media);
    printf("Dev. std  : %.4f\n", s.devstd);
    return 0;
}
```

MakefileMakefile

```
# Makefile - progetto finale
CC     = gcc
CFLAGS = -Wall -Wextra -std=c11 -O2
LDLIBS = -lm

LIB = libstat.a
APP = analizza

# primo target = target di default (basta scrivere "make")
all: $(APP)

# regola generica: ogni file .o si ottiene dal .c omonimo
%.o: %.c stat.h
    $(CC) $(CFLAGS) -c $< -o $@

# la libreria statica dipende dal suo file oggetto
$(LIB): stat.o
    ar rcs $@ $^

# il programma dipende da main.o e dalla libreria
$(APP): main.o $(LIB)
    $(CC) $(CFLAGS) main.o -L. -lstat $(LDLIBS) -o $@

run: $(APP)
    ./$(APP) dati.txt

clean:
    rm -f *.o $(LIB) $(APP)

# target che non corrispondono a file
.PHONY: all run clean
```

dati.txtdati

```
# corrente loop sensore PT01 [mA]
12.02
11.98
12.10
ERR
12.05
11.95
12.00
```

Esecuzione

terminale

```
$ make
gcc -Wall -Wextra -std=c11 -O2 -c main.c -o main.o
gcc -Wall -Wextra -std=c11 -O2 -c stat.c -o stat.o
ar rcs libstat.a stat.o
gcc -Wall -Wextra -std=c11 -O2 main.o -L. -lstat -lm -o analizza
$ ./analizza dati.txt
File      : dati.txt
Campioni  : 6
Minimo    : 11.950
Massimo   : 12.100
Media     : 12.017
Dev. std  : 0.0532
$ make
make: Nothing to be done for 'all'.
$ touch stat.c

$ make
gcc -Wall -Wextra -std=c11 -O2 -c stat.c -o stat.o
ar rcs libstat.a stat.o
gcc -Wall -Wextra -std=c11 -O2 main.o -L. -lstat -lm -o analizza
$ ./analizza
Uso: ./analizza file_misure
$ make clean
rm -f *.o libstat.a analizza
```

Su OnlineGDB

Libreria e programma girano come progetto multi-file con `dati.txt` creato con *New File* e `dati.txt` negli argomenti. Il Makefile richiede un terminale locale.

Commento

Alla seconda invocazione make non fa nulla: tutti i target sono più recenti delle loro dipendenze. Dopo `touch stat.c` ricompila solo `stat.o`, ricrea la libreria e ricollega `analizza`, ma **non** ricompila `main.c`. La riga `ERR` del file dati viene scartata da `sscanf`. Esercizio aggiuntivo: aggiungere alla libreria una funzione che conti i campioni fuori da un intervallo di tolleranza, senza modificare `main.c` né il Makefile.

Parte V

## Algoritmi e strutture dati

Modulo 13

### Ricerca e ordinamento

5 esercizi

Concetti chiave

Un algoritmo si valuta da come cresce il lavoro al crescere dei dati (**complessità**). Non si misura il tempo, che dipende dalla macchina, ma si contano le operazioni fondamentali: confronti e spostamenti.

| Algoritmo | Caso medio | Con n = 1000 | Note |
| --- | --- | --- | --- |
| ricerca lineare | O(n) | \~500 confronti | funziona su qualsiasi array |
| ricerca binaria | O(log n) | \~10 confronti | richiede un array **ordinato** |
| bubble, selection, insertion sort | O(n²) | \~500 000 confronti | semplici; insertion è veloce su dati quasi ordinati |
| merge sort, qsort | O(n log n) | \~10 000 confronti | da usare su grandi quantità di dati |

Gli esercizi di questa parte si possono affrontare già dopo il modulo 9 (struct) e il modulo 8 (malloc).

13.1

#### Ricerca binaria

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere la ricerca binaria su un array ordinato di 1000 interi e confrontarla con la ricerca lineare, contando i confronti eseguiti da ciascuna per alcune chiavi presenti e una assente.

Suggerimento

Due indici `sx` e `dx` delimitano la zona ancora possibile; a ogni passo si guarda l'elemento centrale e si scarta metà della zona.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 13.1 - Ricerca binaria vs lineare */
#include <stdio.h>

#define N 1000

/* indice di chiave nell'array ORDINATO v, -1 se assente; *confronti conta i passi */
int ricerca_binaria(const int v[], int n, int chiave, int *confronti)
{
    int sx = 0, dx = n - 1;
    *confronti = 0;
    while (sx <= dx) {
        int m = sx + (dx - sx) / 2;     /* come (sx+dx)/2, ma senza rischio di overflow */
        (*confronti)++;
        if (v[m] == chiave)
            return m;
        else if (v[m] < chiave)
            sx = m + 1;                 /* la chiave può essere solo a destra */
        else
            dx = m - 1;                 /* la chiave può essere solo a sinistra */
    }
    return -1;
}

int ricerca_lineare(const int v[], int n, int chiave, int *confronti)
{
    *confronti = 0;
    for (int i = 0; i < n; i++) {
        (*confronti)++;
        if (v[i] == chiave)
            return i;
    }
    return -1;
}

int main(void)
{
    static int v[N];
    for (int i = 0; i < N; i++)
        v[i] = 3 * i + 1;               /* array ordinato: 1, 4, 7, 10, ... */

    int chiavi[] = {1, 1498, 2998, 500};
    for (int k = 0; k < 4; k++) {
        int cl, cb;
        int pl = ricerca_lineare(v, N, chiavi[k], &cl);
        int pb = ricerca_binaria(v, N, chiavi[k], &cb);
        printf("chiave %4d: pos. %4d / %4d   confronti: lineare %4d  binaria %2d\n",
               chiavi[k], pl, pb, cl, cb);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
chiave    1: pos.    0 /    0   confronti: lineare    1  binaria  9
chiave 1498: pos.  499 /  499   confronti: lineare  500  binaria  1
chiave 2998: pos.  999 /  999   confronti: lineare 1000  binaria 10
chiave  500: pos.   -1 /   -1   confronti: lineare 1000  binaria 10
```

Commento

Con 1000 elementi la ricerca binaria non supera mai 10 confronti (210 = 1024); con un milione ne bastano 20. Il prezzo è che l'array deve essere ordinato: conviene se le ricerche sono molte e gli inserimenti pochi. La chiave 500 non è presente: entrambe restituiscono -1, la lineare dopo aver guardato tutti gli elementi.

13.2

#### Selection sort e insertion sort

*Intermedio*OnlineGDB: Sì

Consegna

Implementare selection sort e insertion sort su due copie dello stesso array, contando per ciascuno confronti e spostamenti. Per l'insertion sort stampare l'array dopo ogni inserimento.

Suggerimento

Selection: a ogni passo si cerca il minimo della parte non ordinata e lo si porta in testa. Insertion: si prende il prossimo elemento e lo si fa scorrere a sinistra fino al suo posto, come si ordinano le carte in mano.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 13.2 - Selection sort e insertion sort */
#include <stdio.h>
#include <string.h>

typedef struct {
    long confronti;
    long spostamenti;
} Contatori;

void stampa(const int v[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%3d", v[i]);
    printf("\n");
}

void selection_sort(int v[], int n, Contatori *c)
{
    for (int i = 0; i < n - 1; i++) {
        int imin = i;                       /* posizione del minimo di v[i..n-1] */
        for (int j = i + 1; j < n; j++) {
            c->confronti++;
            if (v[j] < v[imin])
                imin = j;
        }
        if (imin != i) {                    /* un solo scambio per passata */
            int t = v[i]; v[i] = v[imin]; v[imin] = t;
            c->spostamenti++;
        }
    }
}

void insertion_sort(int v[], int n, Contatori *c)
{
    for (int i = 1; i < n; i++) {
        int x = v[i];                       /* elemento da inserire */
        int j = i - 1;
        while (j >= 0) {
            c->confronti++;
            if (v[j] <= x)
                break;                      /* trovato il posto */
            v[j + 1] = v[j];                /* sposto a destra il più grande */
            c->spostamenti++;
            j--;
        }
        v[j + 1] = x;
        printf("  inserito %2d:", x);
        stampa(v, n);
    }
}

int main(void)
{
    int originale[] = {29, 10, 14, 37, 13, 5, 42, 8};
    int n = sizeof originale / sizeof originale[0];
    int a[8], b[8];
    memcpy(a, originale, sizeof originale);    /* due copie identiche */
    memcpy(b, originale, sizeof originale);

    Contatori cs = {0, 0}, ci = {0, 0};
    printf("Originale    :");
    stampa(originale, n);

    selection_sort(a, n, &cs);
    printf("Selection    :");
    stampa(a, n);

    printf("Insertion passo per passo:\n");
    insertion_sort(b, n, &ci);

    printf("\n%-10s %10s %12s\n", "algoritmo", "confronti", "spostamenti");
    printf("%-10s %10ld %12ld\n", "selection", cs.confronti, cs.spostamenti);
    printf("%-10s %10ld %12ld\n", "insertion", ci.confronti, ci.spostamenti);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Originale    : 29 10 14 37 13  5 42  8
Selection    :  5  8 10 13 14 29 37 42
Insertion passo per passo:
  inserito 10: 10 29 14 37 13  5 42  8
  inserito 14: 10 14 29 37 13  5 42  8
  inserito 37: 10 14 29 37 13  5 42  8
  inserito 13: 10 13 14 29 37  5 42  8
  inserito  5:  5 10 13 14 29 37 42  8
  inserito 42:  5 10 13 14 29 37 42  8
  inserito  8:  5  8 10 13 14 29 37 42

algoritmo   confronti  spostamenti
selection          28            6
insertion          21           16
```

Commento

Il selection sort fa sempre n(n-1)/2 = 28 confronti, qualunque sia l'ordine iniziale, ma pochissimi scambi: utile quando scrivere costa (es. memoria flash). L'insertion sort si ferma appena trova il posto: su dati già quasi ordinati fa pochissimo lavoro, come mostra l'esercizio successivo.

13.3

#### Confronto sperimentale degli ordinamenti

*Avanzato*OnlineGDB: Sì

Consegna

Confrontare bubble sort (con uscita anticipata), selection sort e insertion sort su 1000 elementi in tre situazioni: dati casuali, già ordinati, in ordine inverso. Stampare una tabella con il numero di confronti. Per i dati casuali usare un generatore pseudo-casuale proprio con seme fisso, così che il risultato sia identico su ogni piattaforma.

Suggerimento

Un generatore lineare congruenziale: `seme = seme * 1103515245 + 12345` su un intero senza segno a 32 bit (`uint32_t`).

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 13.3 - Confronto sperimentale degli ordinamenti */
#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define N 1000

static uint32_t seme = 12345u;

int casuale(int max)                    /* generatore lineare congruenziale */
{
    seme = seme * 1103515245u + 12345u; /* uint32_t: l'overflow è definito (modulo 2^32) */
    return (int)((seme >> 16) % (uint32_t)max);
}

long bubble(int v[], int n)
{
    long c = 0;
    for (int p = 0; p < n - 1; p++) {
        int scambi = 0;
        for (int i = 0; i < n - 1 - p; i++) {
            c++;
            if (v[i] > v[i + 1]) { int t = v[i]; v[i] = v[i + 1]; v[i + 1] = t; scambi = 1; }
        }
        if (!scambi) break;
    }
    return c;
}

long selection(int v[], int n)
{
    long c = 0;
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) { c++; if (v[j] < v[m]) m = j; }
        int t = v[i]; v[i] = v[m]; v[m] = t;
    }
    return c;
}

long insertion(int v[], int n)
{
    long c = 0;
    for (int i = 1; i < n; i++) {
        int x = v[i], j = i - 1;
        while (j >= 0) { c++; if (v[j] <= x) break; v[j + 1] = v[j]; j--; }
        v[j + 1] = x;
    }
    return c;
}

int ordinato(const int v[], int n)      /* verifica del risultato */
{
    for (int i = 1; i < n; i++)
        if (v[i - 1] > v[i]) return 0;
    return 1;
}

int main(void)
{
    static int base[3][N], w[N];
    const char *casi[] = {"casuale", "ordinato", "inverso"};
    for (int i = 0; i < N; i++) {
        base[0][i] = casuale(10000);
        base[1][i] = i;
        base[2][i] = N - i;
    }

    long (*algoritmi[])(int[], int) = {bubble, selection, insertion};   /* puntatori a funzione */
    const char *nomi[] = {"bubble", "selection", "insertion"};

    printf("%-10s %10s %10s %10s\n", "confronti", casi[0], casi[1], casi[2]);
    for (int a = 0; a < 3; a++) {
        printf("%-10s", nomi[a]);
        for (int k = 0; k < 3; k++) {
            memcpy(w, base[k], sizeof w);           /* ogni algoritmo parte dagli stessi dati */
            long c = algoritmi[a](w, N);
            printf(" %10ld%s", c, ordinato(w, N) ? "" : "!");
        }
        printf("\n");
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
confronti     casuale   ordinato    inverso
bubble         498554        999     499500
selection      499500     499500     499500
insertion      259261        999     499500
```

Commento

I risultati confermano la teoria: selection fa sempre 499 500 confronti; bubble con uscita anticipata e insertion su dati già ordinati ne fanno solo 999. L'array `algoritmi` contiene **puntatori a funzione**: permette di provare tutti gli algoritmi con lo stesso ciclo. Non si usa `rand()` perché la sua sequenza cambia tra glibc (Linux) e Windows: con un generatore proprio il risultato è riproducibile ovunque, anche su un microcontrollore.

13.4

#### Merge sort

*Avanzato*OnlineGDB: Sì

Consegna

Implementare il merge sort ricorsivo usando un array di appoggio allocato una sola volta con `malloc`. Stampare, con un rientro proporzionale alla profondità della ricorsione, ogni porzione dopo la fusione.

Suggerimento

Dividi a metà, ordina ricorsivamente le due metà, poi fondi due sequenze ordinate prendendo ogni volta il più piccolo dei due elementi in testa.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 13.4 - Merge sort */
#include <stdio.h>
#include <stdlib.h>

/* fonde v[sx..m] e v[m+1..dx], già ordinati, usando tmp come appoggio */
static void fondi(int v[], int tmp[], int sx, int m, int dx)
{
    int i = sx, j = m + 1, k = sx;
    while (i <= m && j <= dx)
        tmp[k++] = (v[i] <= v[j]) ? v[i++] : v[j++];   /* il più piccolo dei due in testa */
    while (i <= m)  tmp[k++] = v[i++];                  /* copio ciò che avanza */
    while (j <= dx) tmp[k++] = v[j++];
    for (k = sx; k <= dx; k++)
        v[k] = tmp[k];
}

static void ms_ric(int v[], int tmp[], int sx, int dx, int livello)
{
    if (sx >= dx)                       /* caso base: 0 o 1 elementi */
        return;
    int m = sx + (dx - sx) / 2;
    ms_ric(v, tmp, sx, m, livello + 1);
    ms_ric(v, tmp, m + 1, dx, livello + 1);
    fondi(v, tmp, sx, m, dx);

    printf("%*s[%d..%d]:", livello * 4, "", sx, dx);    /* %*s: rientro variabile */
    for (int k = sx; k <= dx; k++)
        printf(" %d", v[k]);
    printf("\n");
}

int merge_sort(int v[], int n)
{
    int *tmp = malloc((size_t)n * sizeof *tmp);         /* appoggio allocato una volta sola */
    if (tmp == NULL)
        return -1;
    ms_ric(v, tmp, 0, n - 1, 0);
    free(tmp);
    return 0;
}

int main(void)
{
    int v[] = {38, 27, 43, 3, 9, 82, 10, 15};
    int n = sizeof v / sizeof v[0];
    if (merge_sort(v, n) != 0) {
        fprintf(stderr, "memoria insufficiente\n");
        return 1;
    }
    printf("Ordinato:");
    for (int i = 0; i < n; i++)
        printf(" %d", v[i]);
    printf("\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
        [0..1]: 27 38
        [2..3]: 3 43
    [0..3]: 3 27 38 43
        [4..5]: 9 82
        [6..7]: 10 15
    [4..7]: 9 10 15 82
[0..7]: 3 9 10 15 27 38 43 82
Ordinato: 3 9 10 15 27 38 43 82
```

Commento

La stampa mostra l'ordine reale delle operazioni: prima si fondono le coppie più profonde, l'intero array per ultimo. Ogni livello della ricorsione lavora su n elementi e i livelli sono log2 n, da cui O(n log n). Il merge sort è *stabile*: elementi uguali mantengono l'ordine originale, grazie al `<=` in `fondi`.

13.5

#### qsort e bsearch su un magazzino

*Avanzato*OnlineGDB: Sì

Consegna

Dato un array di articoli di magazzino (codice, descrizione, prezzo, scorta), ordinarlo con `qsort` della libreria standard prima per prezzo crescente, poi per scorta decrescente, poi per codice. Infine cercare due codici con `bsearch`.

Suggerimento

`qsort` riceve una funzione di confronto `int cmp(const void *a, const void *b)` che restituisce un valore negativo, zero o positivo.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 13.5 - qsort e bsearch */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char   codice[8];
    char   descr[24];
    double prezzo;
    int    scorta;
} Articolo;

/* le funzioni di confronto ricevono puntatori generici: si convertono al tipo vero */
int cmp_prezzo(const void *a, const void *b)
{
    const Articolo *x = a, *y = b;
    return (x->prezzo > y->prezzo) - (x->prezzo < y->prezzo);   /* -1, 0 o +1 */
}

int cmp_scorta_desc(const void *a, const void *b)
{
    const Articolo *x = a, *y = b;
    return (y->scorta > x->scorta) - (y->scorta < x->scorta);   /* invertito: decrescente */
}

int cmp_codice(const void *a, const void *b)
{
    const Articolo *x = a, *y = b;
    return strcmp(x->codice, y->codice);
}

void stampa(const Articolo v[], size_t n, const char *titolo)
{
    printf("-- %s\n", titolo);
    for (size_t i = 0; i < n; i++)
        printf("   %-6s %-20s %8.2f %5d\n", v[i].codice, v[i].descr, v[i].prezzo, v[i].scorta);
}

int main(void)
{
    Articolo mag[] = {
        {"M0342", "Motore 0,37 kW",     185.00, 15},
        {"S0110", "Sensore induttivo",   24.50, 40},
        {"R0007", "Rele' 24 Vdc",         8.90, 120},
        {"I0215", "Inverter 0,75 kW",   310.00,  2},
        {"C0099", "Cavo M12 5 m",        12.30,  8},
    };
    size_t n = sizeof mag / sizeof mag[0];

    qsort(mag, n, sizeof mag[0], cmp_prezzo);
    stampa(mag, n, "per prezzo crescente");
    qsort(mag, n, sizeof mag[0], cmp_scorta_desc);
    stampa(mag, n, "per scorta decrescente");
    qsort(mag, n, sizeof mag[0], cmp_codice);       /* bsearch richiede questo ordine */
    stampa(mag, n, "per codice");

    const char *cercati[] = {"I0215", "X9999"};
    for (int k = 0; k < 2; k++) {
        Articolo chiave;
        strcpy(chiave.codice, cercati[k]);
        Articolo *p = bsearch(&chiave, mag, n, sizeof mag[0], cmp_codice);
        if (p != NULL)
            printf("%s trovato: %s, scorta %d\n", cercati[k], p->descr, p->scorta);
        else
            printf("%s non presente\n", cercati[k]);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
-- per prezzo crescente
   R0007  Rele' 24 Vdc             8.90   120
   C0099  Cavo M12 5 m            12.30     8
   S0110  Sensore induttivo       24.50    40
   M0342  Motore 0,37 kW         185.00    15
   I0215  Inverter 0,75 kW       310.00     2
-- per scorta decrescente
   R0007  Rele' 24 Vdc             8.90   120
   S0110  Sensore induttivo       24.50    40
   M0342  Motore 0,37 kW         185.00    15
   C0099  Cavo M12 5 m            12.30     8
   I0215  Inverter 0,75 kW       310.00     2
-- per codice
   C0099  Cavo M12 5 m            12.30     8
   I0215  Inverter 0,75 kW       310.00     2
   M0342  Motore 0,37 kW         185.00    15
   R0007  Rele' 24 Vdc             8.90   120
   S0110  Sensore induttivo       24.50    40
I0215 trovato: Inverter 0,75 kW, scorta 2
X9999 non presente
```

Commento

`qsort` e `bsearch` sono generiche perché lavorano su `void *` e ricevono la funzione di confronto come **puntatore a funzione**: è il meccanismo delle *callback*, usato anche per gli interrupt e gli eventi nei framework embedded. Il confronto `(x > y) - (x < y)` evita la sottrazione `x - y`, che con gli interi può andare in overflow e con i `double` verrebbe troncata a `int`.

Modulo 14

### Strutture dati: pile, liste, alberi

5 esercizi

Concetti chiave

Una **struttura dati** organizza i dati in funzione delle operazioni da fare. Le tre fondamentali:

| Struttura | Principio | Uso tipico |
| --- | --- | --- |
| pila (stack) | LIFO: l'ultimo inserito è il primo estratto | chiamate di funzione, annulla/ripeti, parsing di espressioni |
| coda (queue) | FIFO: il primo inserito è il primo estratto | buffer di comunicazione (il ring buffer dell'esercizio 11.3) |
| lista concatenata | nodi allocati uno per uno, ciascuno con il puntatore al successivo | insiemi di dimensione variabile, inserimenti in mezzo senza spostare dati |
| albero binario di ricerca | a sinistra le chiavi minori, a destra le maggiori | ricerca, inserimento e ordinamento in O(log n) se l'albero è bilanciato |

Un nodo è una struct che contiene un puntatore a una struct dello stesso tipo: `struct Nodo { int valore; struct Nodo *next; };`. La lista termina con `NULL`; ogni nodo creato con `malloc` va liberato.

14.1

#### Pila: controllo delle parentesi

*Intermedio*OnlineGDB: Sì

Consegna

Realizzare una pila di caratteri su array con `push`, `pop` e test di pila vuota. Usarla per verificare se in una riga di codice le parentesi `() [] {}` sono bilanciate e correttamente annidate, indicando la posizione del primo errore.

Suggerimento

Ogni parentesi aperta va sulla pila; ogni parentesi chiusa deve corrispondere a quella in cima. A fine stringa la pila deve essere vuota.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 14.1 - Pila e parentesi bilanciate */
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_PILA 64

typedef struct {
    char dati[MAX_PILA];
    int  cima;                  /* numero di elementi presenti */
} Pila;

void pila_init(Pila *p)          { p->cima = 0; }
bool pila_vuota(const Pila *p)   { return p->cima == 0; }

bool pila_push(Pila *p, char c)
{
    if (p->cima == MAX_PILA)
        return false;           /* pila piena (overflow) */
    p->dati[p->cima++] = c;
    return true;
}

bool pila_pop(Pila *p, char *c)
{
    if (pila_vuota(p))
        return false;           /* pila vuota (underflow) */
    *c = p->dati[--p->cima];
    return true;
}

/* -1 se bilanciata, altrimenti la posizione del primo errore */
int controlla(const char *s)
{
    Pila p;
    pila_init(&p);
    int i;
    for (i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            if (!pila_push(&p, c))
                return i;
        } else if (c == ')' || c == ']' || c == '}') {
            char attesa = (c == ')') ? '(' : (c == ']') ? '[' : '{';
            char aperta;
            if (!pila_pop(&p, &aperta) || aperta != attesa)
                return i;       /* chiusa senza aperta, o tipo sbagliato */
        }
    }
    return pila_vuota(&p) ? -1 : i;    /* parentesi rimaste aperte: errore a fine riga */
}

int main(void)
{
    const char *righe[] = {
        "v[i] = (a + b) * {c - d[k]};",
        "if (x[2) > 0)",
        "y = ((a + b) * c;",
        "printf(\"%d\", f(v[g(i)]));",
    };
    for (int k = 0; k < 4; k++) {
        int pos = controlla(righe[k]);
        printf("%s\n", righe[k]);
        if (pos < 0)
            printf("  -> bilanciata\n");
        else
            printf("  %*s^ errore in posizione %d\n", pos, "", pos);   /* freccia sotto l'errore */
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
v[i] = (a + b) * {c - d[k]};
  -> bilanciata
if (x[2) > 0)
         ^ errore in posizione 7
y = ((a + b) * c;
                   ^ errore in posizione 17
printf("%d", f(v[g(i)]));
  -> bilanciata
```

Commento

È lo stesso controllo che fa il compilatore e che l'editor usa per evidenziare la parentesi corrispondente. La pila è la struttura naturale per tutto ciò che si "apre" e si "chiude" in modo annidato; anche le chiamate di funzione usano una pila, lo stack.

14.2

#### Calcolatrice in notazione polacca inversa

*Avanzato*OnlineGDB: Sì

Consegna

Valutare espressioni in notazione polacca inversa (RPN), in cui l'operatore segue gli operandi: `3 4 + 2 *` vale (3 + 4) · 2 = 14. Usare una pila di `double` e segnalare gli errori: operandi mancanti, operandi in eccesso, divisione per zero, simboli sconosciuti.

Suggerimento

Numero: push. Operatore: pop di due operandi (attenzione all'ordine: il primo estratto è quello di destra), calcolo, push del risultato. Alla fine la pila deve contenere esattamente un valore.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 14.2 - Calcolatrice RPN con pila */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 32

typedef struct {
    double v[MAX];
    int n;
} PilaD;

static int push(PilaD *p, double x) { if (p->n == MAX) return 0; p->v[p->n++] = x; return 1; }
static int pop(PilaD *p, double *x) { if (p->n == 0) return 0; *x = p->v[--p->n]; return 1; }

/* restituisce NULL se ok (risultato in *ris), altrimenti il messaggio d'errore */
const char *valuta(const char *espr, double *ris)
{
    char buf[128];
    strncpy(buf, espr, sizeof buf - 1);     /* strtok modifica la stringa: lavoro su una copia */
    buf[sizeof buf - 1] = '\0';

    PilaD p = { .n = 0 };
    for (char *t = strtok(buf, " "); t != NULL; t = strtok(NULL, " ")) {
        char *fine;
        double x = strtod(t, &fine);
        if (*fine == '\0') {                /* il token è un numero */
            if (!push(&p, x)) return "pila piena";
            continue;
        }
        if (strlen(t) != 1 || strchr("+-*/", t[0]) == NULL)
            return "simbolo sconosciuto";
        double b, a;
        if (!pop(&p, &b) || !pop(&p, &a))   /* b = operando destro, a = sinistro */
            return "operandi mancanti";
        switch (t[0]) {
        case '+': x = a + b; break;
        case '-': x = a - b; break;
        case '*': x = a * b; break;
        case '/':
            if (b == 0.0) return "divisione per zero";
            x = a / b;
            break;
        }
        push(&p, x);
    }
    if (p.n != 1)
        return p.n == 0 ? "espressione vuota" : "operandi in eccesso";
    *ris = p.v[0];
    return NULL;
}

int main(void)
{
    const char *prove[] = {
        "3 4 + 2 *",
        "5 1 2 + 4 * + 3 -",
        "2 3 4 +",
        "1 +",
        "8 0 /",
        "2 3 ^",
    };
    for (int k = 0; k < 6; k++) {
        double r;
        const char *err = valuta(prove[k], &r);
        if (err == NULL)
            printf("%-20s = %g\n", prove[k], r);
        else
            printf("%-20s : errore, %s\n", prove[k], err);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
3 4 + 2 *            = 14
5 1 2 + 4 * + 3 -    = 14
2 3 4 +              : errore, operandi in eccesso
1 +                  : errore, operandi mancanti
8 0 /                : errore, divisione per zero
2 3 ^                : errore, simbolo sconosciuto
```

Commento

La RPN non ha bisogno di parentesi né di regole di precedenza: è il formato usato dalle calcolatrici HP e, nella sostanza, da molte macchine virtuali e dai linguaggi a pila dei PLC (IL, Instruction List). Restituire un messaggio d'errore o `NULL` è un'alternativa ai codici numerici quando l'errore va mostrato all'utente.

14.3

#### Lista concatenata: operazioni di base

*Avanzato*OnlineGDB: Sì

Consegna

Definire un nodo di lista di interi e scrivere le funzioni: inserimento in testa, inserimento in coda, stampa, lunghezza, somma dei valori, liberazione di tutti i nodi. Le funzioni che modificano la lista ricevono un *puntatore al puntatore* di testa.

Suggerimento

`Nodo **testa`: la funzione può cambiare il puntatore `testa` del chiamante, ad esempio quando la lista è vuota e si inserisce il primo nodo.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 14.3 - Lista concatenata semplice */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Nodo {
    int valore;
    struct Nodo *next;          /* puntatore al nodo successivo (NULL = fine lista) */
} Nodo;

static Nodo *nuovo_nodo(int valore)
{
    Nodo *n = malloc(sizeof *n);
    if (n != NULL) {
        n->valore = valore;
        n->next = NULL;
    }
    return n;
}

bool inserisci_testa(Nodo **testa, int valore)
{
    Nodo *n = nuovo_nodo(valore);
    if (n == NULL) return false;
    n->next = *testa;           /* il nuovo nodo punta al vecchio primo */
    *testa = n;                 /* e diventa il primo */
    return true;
}

bool inserisci_coda(Nodo **testa, int valore)
{
    Nodo *n = nuovo_nodo(valore);
    if (n == NULL) return false;
    if (*testa == NULL) {       /* lista vuota: il nodo è anche il primo */
        *testa = n;
        return true;
    }
    Nodo *p = *testa;
    while (p->next != NULL)     /* scorro fino all'ultimo nodo */
        p = p->next;
    p->next = n;
    return true;
}

void stampa(const Nodo *p)
{
    for (; p != NULL; p = p->next)
        printf("[%d] -> ", p->valore);
    printf("NULL\n");
}

int lunghezza(const Nodo *p)
{
    int n = 0;
    for (; p != NULL; p = p->next) n++;
    return n;
}

long somma(const Nodo *p)
{
    long s = 0;
    for (; p != NULL; p = p->next) s += p->valore;
    return s;
}

void libera(Nodo **testa)
{
    Nodo *p = *testa;
    while (p != NULL) {
        Nodo *succ = p->next;   /* salvo il successivo PRIMA di liberare p */
        free(p);
        p = succ;
    }
    *testa = NULL;              /* la lista del chiamante risulta vuota */
}

int main(void)
{
    Nodo *lista = NULL;         /* lista vuota */
    stampa(lista);

    inserisci_testa(&lista, 7);
    inserisci_testa(&lista, 3);
    inserisci_coda(&lista, 12);
    inserisci_coda(&lista, 25);
    inserisci_testa(&lista, 1);
    stampa(lista);
    printf("lunghezza = %d, somma = %ld\n", lunghezza(lista), somma(lista));

    libera(&lista);
    printf("dopo libera: ");
    stampa(lista);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
NULL
[1] -> [3] -> [7] -> [12] -> [25] -> NULL
lunghezza = 5, somma = 48
dopo libera: NULL
```

Commento

In `libera` leggere `p->next` *dopo* `free(p)` sarebbe un accesso a memoria già restituita: spesso "funziona" per caso, ed è proprio questo che lo rende pericoloso. Per scoprire questi errori si compila con `-fsanitize=address` (appendice C). L'inserimento in coda scorre tutta la lista: per farlo in tempo costante si tiene anche un puntatore all'ultimo nodo.

14.4

#### Lista ordinata: inserimento, ricerca, cancellazione

*Progetto*OnlineGDB: Sì

Consegna

Mantenere una lista di interi sempre ordinata in senso crescente. Scrivere `inserisci_ordinato`, `cerca` (che restituisce il puntatore al nodo o `NULL`) ed `elimina` (che toglie la prima occorrenza di un valore e restituisce se l'ha trovata). Provare inserimenti in testa, in mezzo, in coda e cancellazioni in tutte e tre le posizioni.

Suggerimento

Con un puntatore al puntatore (`Nodo **pp`) che parte da `&testa` e avanza con `pp = &(*pp)->next`, il primo nodo non è più un caso particolare.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 14.4 - Lista ordinata */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Nodo {
    int valore;
    struct Nodo *next;
} Nodo;

bool inserisci_ordinato(Nodo **testa, int valore)
{
    Nodo **pp = testa;                       /* pp punta al "link" da modificare */
    while (*pp != NULL && (*pp)->valore < valore)
        pp = &(*pp)->next;                   /* avanzo al link del nodo successivo */

    Nodo *n = malloc(sizeof *n);
    if (n == NULL) return false;
    n->valore = valore;
    n->next = *pp;                           /* il nuovo nodo punta a quello che seguiva */
    *pp = n;                                 /* e il link precedente punta al nuovo nodo */
    return true;
}

Nodo *cerca(Nodo *testa, int valore)
{
    for (Nodo *p = testa; p != NULL && p->valore <= valore; p = p->next)
        if (p->valore == valore)
            return p;
    return NULL;                             /* la lista è ordinata: posso fermarmi prima */
}

bool elimina(Nodo **testa, int valore)
{
    Nodo **pp = testa;
    while (*pp != NULL && (*pp)->valore != valore)
        pp = &(*pp)->next;
    if (*pp == NULL)
        return false;                        /* valore non presente */
    Nodo *da_togliere = *pp;
    *pp = da_togliere->next;                 /* scavalco il nodo */
    free(da_togliere);
    return true;
}

void stampa(const char *msg, const Nodo *p)
{
    printf("%-18s", msg);
    if (p == NULL)
        printf(" (vuota)");
    for (; p != NULL; p = p->next)
        printf(" %d", p->valore);
    printf("\n");
}

void libera(Nodo **testa)
{
    while (*testa != NULL) {
        Nodo *t = *testa;
        *testa = t->next;
        free(t);
    }
}

int main(void)
{
    Nodo *lista = NULL;
    int valori[] = {40, 10, 30, 50, 20, 5, 60};
    for (int i = 0; i < 7; i++)
        inserisci_ordinato(&lista, valori[i]);
    stampa("dopo inserimenti:", lista);

    int da_cercare[] = {30, 35};
    for (int i = 0; i < 2; i++)
        printf("cerca %d: %s\n", da_cercare[i], cerca(lista, da_cercare[i]) ? "trovato" : "assente");

    elimina(&lista, 5);                      /* in testa */
    elimina(&lista, 30);                     /* in mezzo */
    elimina(&lista, 60);                     /* in coda  */
    stampa("dopo 3 elimina:", lista);
    printf("elimina 99: %s\n", elimina(&lista, 99) ? "ok" : "non presente");

    libera(&lista);
    stampa("dopo libera:", lista);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
dopo inserimenti:  5 10 20 30 40 50 60
cerca 30: trovato
cerca 35: assente
dopo 3 elimina:    10 20 40 50
elimina 99: non presente
dopo libera:       (vuota)
```

Commento

Con il puntatore al puntatore, inserire o togliere il primo nodo è identico a farlo in mezzo: si modifica sempre "il link che punta al nodo", sia esso `testa` o il campo `next` del nodo precedente. Conviene disegnare su carta nodi e frecce prima e dopo ogni operazione: è il modo più efficace per non sbagliare con le liste.

14.5

#### Albero binario di ricerca

*Progetto*OnlineGDB: Sì

Consegna

Realizzare un albero binario di ricerca di interi con: inserimento (ricorsivo), visita in ordine (che stampa le chiavi ordinate), ricerca con conteggio dei passi, calcolo dell'altezza, stampa grafica dell'albero ruotato di 90°, liberazione di tutti i nodi.

Suggerimento

Visita in ordine: sottoalbero sinistro, nodo, sottoalbero destro. Per la stampa ruotata: prima il sottoalbero destro, poi il nodo rientrato in base al livello, poi il sinistro.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 14.5 - Albero binario di ricerca */
#include <stdio.h>
#include <stdlib.h>

typedef struct Albero {
    int chiave;
    struct Albero *sx, *dx;      /* sx: chiavi minori, dx: chiavi maggiori */
} Albero;

Albero *inserisci(Albero *r, int k)
{
    if (r == NULL) {                         /* posto vuoto trovato: creo il nodo */
        Albero *n = malloc(sizeof *n);
        if (n == NULL) { fprintf(stderr, "memoria esaurita\n"); exit(1); }
        n->chiave = k;
        n->sx = n->dx = NULL;
        return n;
    }
    if (k < r->chiave)
        r->sx = inserisci(r->sx, k);
    else if (k > r->chiave)
        r->dx = inserisci(r->dx, k);
    return r;                                /* chiavi duplicate ignorate */
}

void in_ordine(const Albero *r)
{
    if (r == NULL) return;
    in_ordine(r->sx);
    printf(" %d", r->chiave);
    in_ordine(r->dx);
}

int cerca(const Albero *r, int k, int *passi)
{
    *passi = 0;
    while (r != NULL) {                      /* versione iterativa */
        (*passi)++;
        if (k == r->chiave) return 1;
        r = (k < r->chiave) ? r->sx : r->dx;
    }
    return 0;
}

int altezza(const Albero *r)
{
    if (r == NULL) return 0;
    int hs = altezza(r->sx), hd = altezza(r->dx);
    return 1 + (hs > hd ? hs : hd);
}

void disegna(const Albero *r, int livello)  /* albero ruotato: la radice è a sinistra */
{
    if (r == NULL) return;
    disegna(r->dx, livello + 1);
    printf("%*s%d\n", livello * 6, "", r->chiave);
    disegna(r->sx, livello + 1);
}

void libera(Albero *r)                       /* post-ordine: prima i figli, poi il nodo */
{
    if (r == NULL) return;
    libera(r->sx);
    libera(r->dx);
    free(r);
}

int main(void)
{
    int chiavi[] = {50, 30, 70, 20, 40, 60, 80, 35, 65};
    Albero *radice = NULL;
    for (int i = 0; i < 9; i++)
        radice = inserisci(radice, chiavi[i]);

    disegna(radice, 0);
    printf("\nIn ordine:");
    in_ordine(radice);
    printf("\nAltezza: %d\n", altezza(radice));

    int prove[] = {65, 20, 55};
    for (int i = 0; i < 3; i++) {
        int passi, ok = cerca(radice, prove[i], &passi);
        printf("cerca %d: %s in %d passi\n", prove[i], ok ? "trovato" : "assente", passi);
    }

    /* caso peggiore: chiavi inserite già ordinate -> l'albero degenera in una lista */
    Albero *degenere = NULL;
    for (int k = 1; k <= 9; k++)
        degenere = inserisci(degenere, k * 10);
    printf("Altezza con chiavi inserite in ordine: %d\n", altezza(degenere));

    libera(radice);
    libera(degenere);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
            80
      70
                  65
            60
50
            40
                  35
      30
            20

In ordine: 20 30 35 40 50 60 65 70 80
Altezza: 4
cerca 65: trovato in 4 passi
cerca 20: trovato in 3 passi
cerca 55: assente in 3 passi
Altezza con chiavi inserite in ordine: 9
```

Commento

La visita in ordine produce le chiavi ordinate: inserire n valori e visitarli è un algoritmo di ordinamento (*tree sort*). Con 9 chiavi l'albero ben formato ha altezza 4, quindi ogni ricerca richiede al massimo 4 passi; inserendo le chiavi già ordinate l'albero degenera in una lista di altezza 9. Gli alberi bilanciati (AVL, rosso-neri), usati dalle librerie reali, si riorganizzano a ogni inserimento per evitarlo.

Modulo 15

### Algoritmi per l'automazione

5 esercizi

Concetti chiave

Questo modulo raccoglie algoritmi che si incontrano ogni giorno nel firmware di microcontrollori e nei PLC. Sono scritti in C standard e girano su PC, ma sono pensati per essere portati senza modifiche su ESP32, STM32 o Arduino: niente allocazione dinamica, tipi a larghezza fissa (`<stdint.h>`), funzioni che lavorano un campione alla volta.

| Esercizio | Dove si usa |
| --- | --- |
| media mobile, filtro esponenziale | pulizia di letture analogiche (ADC, 4-20 mA) |
| debounce e fronti | ingressi digitali da pulsanti, finecorsa, encoder |
| interpolazione su tabella | linearizzazione di sensori, curve di calibrazione |
| bisezione | inversione di formule non risolvibili a mano (termoresistenze, termistori) |
| CRC-16 | integrità dei frame Modbus RTU su RS485 |

15.1

#### Filtri: media mobile ed esponenziale

*Intermedio*OnlineGDB: Sì

Consegna

Una sequenza di letture di un sensore contiene rumore e un picco isolato. Filtrarla con una media mobile su 4 campioni (con somma aggiornata in modo incrementale, senza risommare la finestra) e con un filtro esponenziale `y = y + α(x − y)` con α = 0,25. Stampare in colonna lettura grezza e uscite dei due filtri.

Suggerimento

Media mobile: un buffer circolare di 4 campioni; a ogni nuovo campione si sottrae dalla somma quello che esce e si aggiunge quello che entra.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 15.1 - Media mobile e filtro esponenziale */
#include <stdio.h>

#define FINESTRA 4

typedef struct {
    double buf[FINESTRA];
    double somma;
    int    indice;          /* prossima posizione da sovrascrivere */
    int    pieni;           /* campioni validi nel buffer (all'avvio < FINESTRA) */
} MediaMobile;

void mm_init(MediaMobile *m)
{
    for (int i = 0; i < FINESTRA; i++) m->buf[i] = 0.0;
    m->somma = 0.0;
    m->indice = 0;
    m->pieni = 0;
}

double mm_aggiorna(MediaMobile *m, double x)
{
    m->somma -= m->buf[m->indice];          /* tolgo il campione più vecchio */
    m->buf[m->indice] = x;
    m->somma += x;                          /* aggiungo il nuovo */
    m->indice = (m->indice + 1) % FINESTRA;
    if (m->pieni < FINESTRA) m->pieni++;
    return m->somma / m->pieni;
}

typedef struct {
    double alfa;            /* 0 < alfa <= 1: più è piccolo, più il filtro è "lento" */
    double y;
    int    avviato;
} FiltroEsp;

double fe_aggiorna(FiltroEsp *f, double x)
{
    if (!f->avviato) {      /* il primo campione inizializza l'uscita */
        f->y = x;
        f->avviato = 1;
    } else {
        f->y += f->alfa * (x - f->y);
    }
    return f->y;
}

int main(void)
{
    /* letture di una corrente 4-20 mA intorno a 12 mA, con un picco al campione 6 */
    double letture[] = {12.1, 11.8, 12.3, 11.9, 12.2, 17.5, 12.0, 11.7, 12.4, 12.1, 11.9, 12.0};
    int n = sizeof letture / sizeof letture[0];

    MediaMobile mm;
    mm_init(&mm);
    FiltroEsp fe = { .alfa = 0.25, .y = 0.0, .avviato = 0 };

    printf("%3s %8s %10s %10s\n", "n", "grezzo", "media(4)", "esp(0.25)");
    for (int i = 0; i < n; i++)
        printf("%3d %8.2f %10.2f %10.2f\n", i + 1, letture[i],
               mm_aggiorna(&mm, letture[i]), fe_aggiorna(&fe, letture[i]));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
  n   grezzo   media(4)  esp(0.25)
  1    12.10      12.10      12.10
  2    11.80      11.95      12.03
  3    12.30      12.07      12.09
  4    11.90      12.03      12.05
  5    12.20      12.05      12.08
  6    17.50      13.48      13.44
  7    12.00      13.40      13.08
  8    11.70      13.35      12.73
  9    12.40      13.40      12.65
 10    12.10      12.05      12.51
 11    11.90      12.03      12.36
 12    12.00      12.10      12.27
```

Commento

Entrambi i filtri attenuano il picco, ma lo "spalmano" sui campioni successivi: la media mobile per esattamente 4 campioni, l'esponenziale con una coda che decresce. Il filtro esponenziale occupa un solo valore di memoria ed è il filtro di primo ordine (passa-basso RC) in forma digitale. Contro i picchi isolati funziona meglio un filtro mediano, buon esercizio di estensione.

15.2

#### Debounce di un ingresso e rilevamento dei fronti

*Avanzato*OnlineGDB: Sì

Consegna

Un pulsante viene campionato ogni millisecondo; i rimbalzi del contatto producono brevi commutazioni spurie. Scrivere un debounce che accetti un cambio di stato solo dopo 3 campioni consecutivi uguali, e un rilevatore di fronte di salita (come il blocco R_TRIG dei PLC). Contare i fronti sul segnale grezzo e su quello filtrato.

Suggerimento

Il debounce tiene lo stato stabile e un contatore di campioni diversi da esso; il rilevatore di fronte confronta il valore attuale con quello del ciclo precedente.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 15.2 - Debounce e fronte di salita */
#include <stdio.h>
#include <stdbool.h>

#define CAMPIONI_STABILI 3

typedef struct {
    bool stato;             /* stato stabile riconosciuto */
    int  contatore;         /* campioni consecutivi diversi dallo stato */
} Debounce;

bool debounce(Debounce *d, bool ingresso)
{
    if (ingresso == d->stato) {
        d->contatore = 0;                   /* nessun cambiamento in corso */
    } else if (++d->contatore >= CAMPIONI_STABILI) {
        d->stato = ingresso;                /* cambiamento confermato */
        d->contatore = 0;
    }
    return d->stato;
}

typedef struct {
    bool precedente;
} RTrig;

bool fronte_salita(RTrig *t, bool x)        /* vero per un solo ciclo, sul passaggio 0 -> 1 */
{
    bool q = x && !t->precedente;
    t->precedente = x;
    return q;
}

int main(void)
{
    /* un ms per campione: due pressioni reali, con rimbalzi */
    const char *segnale = "000101011111111101000000001011111111001000";
    Debounce d = { false, 0 };
    RTrig tg = { false }, tf = { false };
    int fronti_grezzi = 0, fronti_filtrati = 0;

    printf("ms      ");
    for (int i = 0; segnale[i]; i++) printf("%d", i % 10);
    printf("\ngrezzo  ");
    for (int i = 0; segnale[i]; i++) printf("%c", segnale[i]);
    printf("\nfiltrato");
    for (int i = 0; segnale[i]; i++) {
        bool x = (segnale[i] == '1');
        bool y = debounce(&d, x);
        if (fronte_salita(&tg, x)) fronti_grezzi++;
        if (fronte_salita(&tf, y)) fronti_filtrati++;
        printf("%d", y);
    }
    printf("\n\nfronti di salita: grezzo %d, filtrato %d\n", fronti_grezzi, fronti_filtrati);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
ms      012345678901234567890123456789012345678901
grezzo  000101011111111101000000001011111111001000
filtrato000000000111111111110000000000111111111110

fronti di salita: grezzo 7, filtrato 2
```

Commento

Senza debounce un contapezzi conterebbe 7 pezzi invece di 2. Il prezzo è un ritardo di 3 ms sul riconoscimento, visibile nella riga "filtrato". Le due struct rendono le funzioni riutilizzabili per più ingressi: un'istanza per ciascuno, esattamente come le istanze dei blocchi funzione (FB) nei PLC IEC 61131-3.

15.3

#### Linearizzazione con tabella e interpolazione

*Avanzato*OnlineGDB: Sì

Consegna

Un serbatoio di forma irregolare ha una tabella di taratura altezza (mm) → volume (litri). Scrivere una funzione che, data un'altezza misurata, trovi con la ricerca binaria il tratto di tabella che la contiene e calcoli il volume per interpolazione lineare. Fuori tabella il valore va limitato agli estremi.

Suggerimento

Nel tratto `[x0, x1]`: `y = y0 + (x − x0)·(y1 − y0)/(x1 − x0)`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 15.3 - Interpolazione lineare su tabella */
#include <stdio.h>

typedef struct {
    double x;               /* altezza [mm] */
    double y;               /* volume  [l]  */
} Punto;

/* tabella di taratura (dati di esempio), x strettamente crescente */
static const Punto TARATURA[] = {
    {  0.0,   0.0}, {100.0,  35.0}, {200.0, 110.0},
    {300.0, 220.0}, {400.0, 350.0}, {500.0, 480.0},
};
#define N_PUNTI ((int)(sizeof TARATURA / sizeof TARATURA[0]))

double interpola(const Punto t[], int n, double x)
{
    if (x <= t[0].x)     return t[0].y;          /* limito agli estremi */
    if (x >= t[n - 1].x) return t[n - 1].y;

    int sx = 0, dx = n - 1;                      /* ricerca binaria del tratto */
    while (dx - sx > 1) {                        /* invariante: t[sx].x <= x < t[dx].x */
        int m = (sx + dx) / 2;
        if (t[m].x <= x) sx = m;
        else             dx = m;
    }
    const Punto *a = &t[sx], *b = &t[dx];
    return a->y + (x - a->x) * (b->y - a->y) / (b->x - a->x);
}

int main(void)
{
    double misure[] = {-5.0, 0.0, 50.0, 150.0, 250.0, 333.0, 400.0, 480.0, 520.0};
    printf("%10s %10s\n", "altezza", "volume");
    for (int i = 0; i < 9; i++)
        printf("%7.1f mm %8.1f l\n", misure[i], interpola(TARATURA, N_PUNTI, misure[i]));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
   altezza     volume
   -5.0 mm      0.0 l
    0.0 mm      0.0 l
   50.0 mm     17.5 l
  150.0 mm     72.5 l
  250.0 mm    165.0 l
  333.0 mm    262.9 l
  400.0 mm    350.0 l
  480.0 mm    454.0 l
  520.0 mm    480.0 l
```

Commento

È la tecnica usata per linearizzare termocoppie, sensori di livello e curve di valvole quando la formula esatta non esiste o è troppo costosa da calcolare: la si sostituisce con una tabella e si interpola. La tabella è `static const`: su un microcontrollore resta in flash e non occupa RAM. La ricerca binaria riprende l'esercizio 13.1.

15.4

#### Bisezione: temperatura da una PT100

*Avanzato*OnlineGDB: Sì

Consegna

La resistenza di una PT100 per T ≥ 0 °C è `R(T) = R0·(1 + A·T + B·T²)` con R0 = 100 Ω, A = 3,9083·10⁻³, B = −5,775·10⁻⁷ (IEC 60751). Data una resistenza misurata, trovare la temperatura con il metodo di bisezione tra 0 e 850 °C con tolleranza 0,001 °C, stampando il numero di iterazioni. Confrontare con la soluzione esatta dell'equazione di secondo grado.

Suggerimento

Bisezione: se f(a) e f(m) hanno segno opposto la radice è in \[a, m\], altrimenti in \[m, b\]. Qui f(T) = R(T) − Rmisurata.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 15.4 - Bisezione: temperatura di una PT100 */
#include <stdio.h>
#include <math.h>

#define R0 100.0
#define A  3.9083e-3
#define B  (-5.775e-7)

double r_pt100(double t)                /* resistenza in funzione della temperatura (T >= 0) */
{
    return R0 * (1.0 + A * t + B * t * t);
}

/* temperatura per resistenza r, con bisezione in [a, b]; *iter = iterazioni eseguite */
double bisezione(double r, double a, double b, double toll, int *iter)
{
    double fa = r_pt100(a) - r;
    *iter = 0;
    while (b - a > toll) {
        double m = 0.5 * (a + b);
        double fm = r_pt100(m) - r;
        (*iter)++;
        if (fa * fm <= 0.0) {           /* segno opposto (o zero): la radice è in [a, m] */
            b = m;
        } else {                        /* stesso segno: la radice è in [m, b] */
            a = m;
            fa = fm;
        }
    }
    return 0.5 * (a + b);
}

double formula_esatta(double r)        /* radice dell'equazione B*T^2 + A*T + (1 - r/R0) = 0 */
{
    double c = 1.0 - r / R0;
    return (-A + sqrt(A * A - 4.0 * B * c)) / (2.0 * B);
}

int main(void)
{
    double resistenze[] = {100.39, 119.40, 138.51, 175.86, 247.09};
    printf("%9s %12s %8s %12s\n", "R [ohm]", "T bisez.", "iter.", "T esatta");
    for (int i = 0; i < 5; i++) {
        int it;
        double t = bisezione(resistenze[i], 0.0, 850.0, 0.001, &it);
        printf("%9.2f %10.3f C %8d %10.3f C\n", resistenze[i], t, it, formula_esatta(resistenze[i]));
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog -lm
```

Esecuzione

terminale

```
$ ./prog
  R [ohm]     T bisez.    iter.     T esatta
   100.39      0.998 C       20      0.998 C
   119.40     50.008 C       20     50.007 C
   138.51    100.012 C       20    100.012 C
   175.86    200.011 C       20    200.011 C
   247.09    399.994 C       20    399.994 C
```

Su OnlineGDB

Se il linker segnala `undefined reference to sqrt`, aggiungere `-lm` in *Extra Compiler Flags*.

Commento

Ogni iterazione dimezza l'intervallo: da 850 °C a 0,001 °C servono log2(850 000) ≈ 20 passi, indipendentemente dalla funzione. Qui la formula esatta esiste e serve da verifica, ma per i termistori NTC (equazione di Steinhart-Hart) o per la PT100 sotto 0 °C la bisezione resta il metodo più robusto. Il test `fa * fm <= 0` include il caso in cui un estremo è già la radice: con il solo confronto dei segni, R = 100 Ω (0 °C esatti) farebbe convergere l'algoritmo a 850 °C. In `formula_esatta` si prende la radice con il `+` perché `B` è negativo: l'altra radice è fuori dal campo fisico.

15.5

#### CRC-16 Modbus RTU

*Progetto*OnlineGDB: Sì

Consegna

Scrivere la funzione che calcola il CRC-16 Modbus (valore iniziale 0xFFFF, polinomio riflesso 0xA001) e usarla per: costruire la richiesta "leggi 10 holding register dall'indirizzo 0" verso lo slave 1 (funzione 0x03), stampandola in esadecimale; verificare il frame ricevuto; mostrare che un singolo bit alterato viene rilevato.

Suggerimento

Nel frame Modbus indirizzo registro e quantità sono big-endian (byte alto prima); il CRC invece si trasmette con il **byte basso prima**. Un frame integro, CRC compreso, ha CRC calcolato pari a 0.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 15.5 - CRC-16 Modbus RTU */
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>

uint16_t crc16_modbus(const uint8_t *dati, size_t n)
{
    uint16_t crc = 0xFFFF;                  /* valore iniziale */
    for (size_t i = 0; i < n; i++) {
        crc ^= dati[i];                     /* il byte entra nella parte bassa */
        for (int b = 0; b < 8; b++) {       /* elaboro un bit alla volta */
            if (crc & 0x0001u)
                crc = (uint16_t)((crc >> 1) ^ 0xA001u);   /* polinomio 0x8005 riflesso */
            else
                crc >>= 1;
        }
    }
    return crc;
}

/* compone una richiesta "Read Holding Registers": restituisce la lunghezza del frame */
size_t richiesta_lettura(uint8_t frame[8], uint8_t slave, uint16_t reg, uint16_t qta)
{
    frame[0] = slave;
    frame[1] = 0x03;                        /* codice funzione */
    frame[2] = (uint8_t)(reg >> 8);         /* indirizzo: byte alto */
    frame[3] = (uint8_t)(reg & 0xFF);       /*            byte basso */
    frame[4] = (uint8_t)(qta >> 8);
    frame[5] = (uint8_t)(qta & 0xFF);
    uint16_t crc = crc16_modbus(frame, 6);
    frame[6] = (uint8_t)(crc & 0xFF);       /* CRC: byte BASSO prima */
    frame[7] = (uint8_t)(crc >> 8);
    return 8;
}

void stampa_frame(const char *msg, const uint8_t *f, size_t n)
{
    printf("%-22s", msg);
    for (size_t i = 0; i < n; i++)
        printf(" %02X", (unsigned)f[i]);
    printf("\n");
}

int frame_valido(const uint8_t *f, size_t n)
{
    return n >= 4 && crc16_modbus(f, n) == 0;   /* CRC su dati+CRC = 0 se integro */
}

int main(void)
{
    uint8_t frame[8];
    size_t n = richiesta_lettura(frame, 1, 0x0000, 10);
    stampa_frame("Richiesta:", frame, n);
    printf("CRC calcolato        : 0x%04X\n", (unsigned)crc16_modbus(frame, 6));
    printf("Frame valido?        : %s\n", frame_valido(frame, n) ? "si" : "no");

    frame[3] ^= 0x04;                       /* simulo un disturbo: un bit invertito */
    stampa_frame("Ricevuto con errore:", frame, n);
    printf("Frame valido?        : %s\n", frame_valido(frame, n) ? "si" : "no");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Richiesta:             01 03 00 00 00 0A C5 CD
CRC calcolato        : 0xCDC5
Frame valido?        : si
Ricevuto con errore:   01 03 00 04 00 0A C5 CD
Frame valido?        : no
```

Commento

Il frame `01 03 00 00 00 0A C5 CD` è l'esempio classico della specifica Modbus e si può confrontare con quello che mostra un analizzatore seriale o un tool come Modbus Poll. Il CRC rileva tutti gli errori su un singolo bit e tutte le raffiche di errori lunghe fino a 16 bit. Sui microcontrollori lenti si usa una versione con tabella di 256 valori precalcolati, che elabora un byte per volta invece di un bit: buon esercizio di estensione.

Parte VI

## Approfondimenti

Modulo 16

### Funzioni avanzate

4 esercizi

Concetti chiave

Oltre alle funzioni "normali", il C offre strumenti che compaiono continuamente nel codice professionale:

| Strumento | Scrittura | A cosa serve |
| --- | --- | --- |
| ricorsione | la funzione chiama sé stessa | problemi che si scompongono in sottoproblemi uguali e più piccoli |
| puntatore a funzione | `int (*f)(int)` | scegliere a run-time quale funzione chiamare: callback, tabelle di comandi |
| funzione variadica | `void log(const char *fmt, ...)` | numero variabile di argomenti, come `printf` |
| macro | `#define MAX(a,b) ...` | sostituzione testuale del preprocessore, prima della compilazione |
| funzione `static inline` | `static inline int max(int a, int b)` | velocità di una macro con i controlli di una funzione |

Un `typedef` rende leggibili i puntatori a funzione: `typedef int (*Comando)(Macchina *, int);` definisce il tipo "puntatore a una funzione che riceve una Macchina e un int e restituisce un int".

16.1

#### Ricorsione: la Torre di Hanoi

*Intermedio*OnlineGDB: Sì

Consegna

Tre pioli A, B, C; su A ci sono n dischi di diametro decrescente. Bisogna portarli tutti su C muovendo un disco alla volta e senza mai appoggiare un disco su uno più piccolo. Scrivere la soluzione ricorsiva, stampare le mosse per 3 dischi e il numero di mosse necessario per 10, 20 e 64 dischi.

Suggerimento

Per spostare n dischi da A a C: sposta n−1 dischi da A a B, sposta il disco più grande da A a C, sposta gli n−1 dischi da B a C.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 16.1 - Torre di Hanoi */
#include <stdio.h>
#include <limits.h>

long mosse = 0;

void hanoi(int n, char da, char a, char appoggio)
{
    if (n == 0)                         /* caso base: nessun disco da spostare */
        return;
    hanoi(n - 1, da, appoggio, a);      /* 1) libero il disco n spostando gli n-1 sopra */
    mosse++;
    printf("%2ld: disco %d da %c a %c\n", mosse, n, da, a);   /* 2) sposto il disco n */
    hanoi(n - 1, appoggio, a, da);      /* 3) rimetto gli n-1 dischi sopra il disco n */
}

int main(void)
{
    hanoi(3, 'A', 'C', 'B');
    printf("Mosse per 3 dischi: %ld\n\n", mosse);

    /* il numero di mosse è 2^n - 1 */
    printf("10 dischi: %lu mosse\n", (1UL << 10) - 1);
    printf("20 dischi: %lu mosse\n", (1UL << 20) - 1);
    printf("64 dischi: %llu mosse\n", ULLONG_MAX);    /* 2^64 - 1: il massimo di 64 bit */
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
 1: disco 1 da A a C
 2: disco 2 da A a B
 3: disco 1 da C a B
 4: disco 3 da A a C
 5: disco 1 da B a A
 6: disco 2 da B a C
 7: disco 1 da A a C
Mosse per 3 dischi: 7

10 dischi: 1023 mosse
20 dischi: 1048575 mosse
64 dischi: 18446744073709551615 mosse
```

Commento

La soluzione ricorsiva è di tre righe, mentre quella iterativa è molto meno intuitiva: è l'esempio classico di problema che "si descrive da solo" per ricorsione. Con 64 dischi, a una mossa al secondo, servirebbero circa 585 miliardi di anni: la crescita esponenziale 2n rende inutilizzabile qualsiasi algoritmo di questo tipo già per n modesti.

16.2

#### Puntatori a funzione: tabella di comandi

*Avanzato*OnlineGDB: Sì

Consegna

Un controllore riceve comandi testuali (`START`, `STOP`, `VEL 1500`, `STATO`). Implementare ciascun comando come funzione con la stessa firma e associarle ai nomi in una tabella di struct `{nome, puntatore a funzione}`. L'interprete cerca il nome nella tabella e chiama la funzione corrispondente, senza alcuna catena di `if`. Gestire comandi sconosciuti e valori non ammessi.

Suggerimento

`typedef int (*Comando)(Macchina *m, int arg);` poi `TABELLA[i].funzione(m, arg)`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 16.2 - Tabella di comandi con puntatori a funzione */
#include <stdio.h>
#include <string.h>

typedef struct {
    int in_marcia;
    int velocita;                     /* giri/min */
} Macchina;

typedef int (*Comando)(Macchina *m, int arg);    /* tipo: puntatore a funzione */

/* ogni comando ha la stessa firma; (void)arg evita il warning se non serve */
static int cmd_start(Macchina *m, int arg) { (void)arg; m->in_marcia = 1; return 0; }
static int cmd_stop(Macchina *m, int arg)  { (void)arg; m->in_marcia = 0; m->velocita = 0; return 0; }

static int cmd_vel(Macchina *m, int arg)
{
    if (arg < 0 || arg > 3000) return -1;        /* valore fuori range */
    if (!m->in_marcia)         return -2;        /* macchina ferma */
    m->velocita = arg;
    return 0;
}

static int cmd_stato(Macchina *m, int arg)
{
    (void)arg;
    printf("[%s, %d giri/min] ", m->in_marcia ? "IN MARCIA" : "FERMA", m->velocita);
    return 0;
}

typedef struct {
    const char *nome;
    Comando     funzione;
} VoceComando;

static const VoceComando TABELLA[] = {          /* aggiungere un comando = aggiungere una riga */
    {"START", cmd_start},
    {"STOP",  cmd_stop},
    {"VEL",   cmd_vel},
    {"STATO", cmd_stato},
};

int esegui(Macchina *m, const char *riga)
{
    char nome[16];
    int arg = 0;
    if (sscanf(riga, "%15s %d", nome, &arg) < 1)
        return -9;
    for (size_t i = 0; i < sizeof TABELLA / sizeof TABELLA[0]; i++)
        if (strcmp(nome, TABELLA[i].nome) == 0)
            return TABELLA[i].funzione(m, arg);  /* chiamata tramite puntatore */
    return -3;                                   /* nome non presente in tabella */
}

const char *descrivi(int codice)
{
    switch (codice) {
    case  0: return "ok";
    case -1: return "valore fuori range";
    case -2: return "rifiutato: macchina ferma";
    case -3: return "comando sconosciuto";
    default: return "riga non valida";
    }
}

int main(void)
{
    Macchina m = {0, 0};
    const char *sequenza[] = {"STATO", "VEL 1500", "START", "VEL 1500", "STATO",
                              "VEL 5000", "RESET", "STOP", "STATO"};
    for (size_t i = 0; i < sizeof sequenza / sizeof sequenza[0]; i++) {
        printf("> %-9s ", sequenza[i]);
        int r = esegui(&m, sequenza[i]);
        printf("%s\n", descrivi(r));
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
> STATO     [FERMA, 0 giri/min] ok
> VEL 1500  rifiutato: macchina ferma
> START     ok
> VEL 1500  ok
> STATO     [IN MARCIA, 1500 giri/min] ok
> VEL 5000  valore fuori range
> RESET     comando sconosciuto
> STOP      ok
> STATO     [FERMA, 0 giri/min] ok
```

Commento

La tabella è `static const`: su un microcontrollore resta in flash. Lo stesso schema si usa per i protocolli seriali a comandi (comandi AT, SCPI degli strumenti di misura), per i menu dei display e per le tabelle dei vettori di interrupt, che sono letteralmente array di puntatori a funzione.

16.3

#### Funzioni variadiche: un logger

*Avanzato*OnlineGDB: Sì

Consegna

Scrivere una funzione di log `log_msg(livello, formato, ...)` che accetti gli stessi argomenti di `printf`, anteponga a ogni messaggio un tempo in millisecondi e il livello (DEBUG, INFO, WARN, ERROR) e scarti i messaggi sotto una soglia configurabile. Scrivere anche `media(n, ...)` che calcoli la media di n valori `double`.

Suggerimento

`<stdarg.h>`: `va_list`, `va_start`, `va_arg`, `va_end`. Per passare gli argomenti a printf si usa `vprintf`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 16.3 - Funzioni variadiche */
#include <stdio.h>
#include <stdarg.h>

typedef enum { LOG_DEBUG, LOG_INFO, LOG_WARN, LOG_ERROR } LivelloLog;

static LivelloLog soglia = LOG_INFO;     /* sotto questa soglia i messaggi sono scartati */
static unsigned long tick_ms = 0;        /* tempo simulato */

void log_msg(LivelloLog liv, const char *fmt, ...)
{
    static const char *nomi[] = {"DEBUG", "INFO", "WARN", "ERROR"};
    if (liv < soglia)
        return;
    printf("[%6lu ms] %-5s ", tick_ms, nomi[liv]);

    va_list ap;
    va_start(ap, fmt);          /* ap parte dopo l'ultimo parametro fisso (fmt) */
    vprintf(fmt, ap);           /* versione di printf che riceve una va_list */
    va_end(ap);
    printf("\n");
}

double media(int n, ...)        /* n dice quanti valori seguono */
{
    va_list ap;
    va_start(ap, n);
    double somma = 0.0;
    for (int i = 0; i < n; i++)
        somma += va_arg(ap, double);    /* il tipo va indicato: il compilatore non lo sa */
    va_end(ap);
    return n > 0 ? somma / n : 0.0;
}

int main(void)
{
    log_msg(LOG_INFO, "avvio firmware v%d.%d", 1, 4);
    tick_ms = 120;
    log_msg(LOG_DEBUG, "questo messaggio non compare (soglia INFO)");
    log_msg(LOG_WARN, "temperatura %.1f C oltre la soglia di %d C", 78.5, 75);
    tick_ms = 2500;
    log_msg(LOG_ERROR, "timeout slave %d sulla linea %s", 3, "RS485-1");

    soglia = LOG_DEBUG;          /* abilito il livello di dettaglio */
    tick_ms = 2510;
    log_msg(LOG_DEBUG, "media letture = %.3f", media(4, 11.98, 12.02, 12.10, 11.95));
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
[     0 ms] INFO  avvio firmware v1.4
[   120 ms] WARN  temperatura 78.5 C oltre la soglia di 75 C
[  2500 ms] ERROR timeout slave 3 sulla linea RS485-1
[  2510 ms] DEBUG media letture = 12.012
```

Commento

Il compilatore non può controllare i tipi degli argomenti variabili: `media(3, 1.0, 2.0, 4)` passa un `int` dove `va_arg` si aspetta un `double`, e il risultato è indefinito. Per questo le variadiche si usano quasi solo per i logger. Con GCC si può aggiungere al prototipo `__attribute__((format(printf, 2, 3)))`: il compilatore controllerà il formato di `log_msg` come fa con `printf`.

16.4

#### Macro e funzioni inline: le trappole del preprocessore

*Avanzato*OnlineGDB: Sì

Consegna

Scrivere un programma che mostri tre trappole delle macro e il modo di evitarle: (1) la mancanza di parentesi in `QUADRATO(x)`; (2) la doppia valutazione degli argomenti in `MAX(a, b)` con `i++`, confrontata con una funzione `static inline`; (3) una macro di più istruzioni usata in un `if` senza graffe, risolta con `do { ... } while (0)`. Usare l'operatore `#` per stampare il nome di una variabile. Osservare infine il codice espanso con `gcc -E`.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 16.4 - Macro e inline */
#include <stdio.h>

#define QUADRATO_SBAGLIATO(x) x * x
#define QUADRATO(x)           ((x) * (x))                /* parentesi su argomenti e risultato */
#define MAX_MACRO(a, b)       ((a) > (b) ? (a) : (b))
#define STAMPA_VAR(v)         printf(#v " = %d\n", (v))  /* #v diventa la stringa "v" */
#define SCAMBIA(a, b)         do { int t_ = (a); (a) = (b); (b) = t_; } while (0)

static inline int max_inline(int a, int b)                /* argomenti valutati una volta sola */
{
    return a > b ? a : b;
}

int main(void)
{
    int x = 3;
    printf("QUADRATO_SBAGLIATO(x + 1) = %d\n", QUADRATO_SBAGLIATO(x + 1));  /* x + 1 * x + 1 */
    printf("QUADRATO(x + 1)           = %d\n", QUADRATO(x + 1));

    int i = 5, j = 5, k = 2;
    int m1 = MAX_MACRO(i++, k);       /* i++ compare due volte nel testo espanso */
    int m2 = max_inline(j++, k);
    printf("MAX_MACRO(i++, 2)  = %d, poi i = %d\n", m1, i);
    printf("max_inline(j++, 2) = %d, poi j = %d\n", m2, j);

    int a = 1, b = 2;
    if (a < b)
        SCAMBIA(a, b);                /* senza do-while(0) l'else seguente sarebbe un errore */
    else
        printf("mai eseguito\n");
    STAMPA_VAR(a);
    STAMPA_VAR(b);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
QUADRATO_SBAGLIATO(x + 1) = 7
QUADRATO(x + 1)           = 16
MAX_MACRO(i++, 2)  = 6, poi i = 7
max_inline(j++, 2) = 5, poi j = 6
a = 2
b = 1
$ gcc -E -P main.c | tail -n 20
}
int main(void)
{
    int x = 3;
    printf("QUADRATO_SBAGLIATO(x + 1) = %d\n", x + 1 * x + 1);
    printf("QUADRATO(x + 1)           = %d\n", ((x + 1) * (x + 1)));
    int i = 5, j = 5, k = 2;
    int m1 = ((i++) > (k) ? (i++) : (k));
    int m2 = max_inline(j++, k);
    printf("MAX_MACRO(i++, 2)  = %d, poi i = %d\n", m1, i);
    printf("max_inline(j++, 2) = %d, poi j = %d\n", m2, j);
    int a = 1, b = 2;
    if (a < b)
        do { int t_ = (a); (a) = (b); (b) = t_; } while (0);
    else
        printf("mai eseguito\n");
    printf("a" " = %d\n", (a));
    printf("b" " = %d\n", (b));
    return 0;
}
```

Su OnlineGDB

Il programma gira su OnlineGDB; l'espansione con `gcc -E` richiede un terminale locale.

Commento

`gcc -E` ferma la compilazione dopo il preprocessore e mostra il testo che il compilatore riceve davvero: è il modo più rapido per capire il comportamento di una macro. Oggi si preferiscono `static inline` e `const`/`enum` alle macro; le macro restano insostituibili per la compilazione condizionale (`#ifdef DEBUG`), per `#` e `##` e per gli include guard.

Modulo 17

### Algoritmi classici

4 esercizi

Concetti chiave

Una raccolta di algoritmi e funzioni di libreria che ogni programmatore C dovrebbe saper scrivere o usare: il crivello di Eratostene (prima vera ottimizzazione algoritmica rispetto al test di primalità del modulo 5), le conversioni tra basi numeriche (indispensabili per leggere registri e trame di comunicazione), le funzioni di `<math.h>` che servono nella pratica tecnica e la **tabella hash**, la struttura che permette di cercare per chiave in tempo praticamente costante.

In C11 rigoroso (`-std=c11`) la costante `M_PI` non è definita: è un'estensione POSIX. Si definisce una propria costante `PI` oppure si compila con `-std=gnu11`.

17.1

#### Il crivello di Eratostene

*Intermedio*OnlineGDB: Sì

Consegna

Stampare i numeri primi fino a 100 con il crivello di Eratostene: si scrivono tutti i numeri e, per ogni primo p, si cancellano i suoi multipli. Contare poi i primi fino a 1 000 000 allocando il crivello con `calloc`.

Suggerimento

Per ogni p basta partire da p·p: i multipli più piccoli sono già stati cancellati da primi minori.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 17.1 - Crivello di Eratostene */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* segna in composto[] i numeri non primi fino a limite; restituisce quanti primi ci sono */
long crivello(bool composto[], long limite)
{
    composto[0] = composto[1] = true;
    for (long p = 2; p * p <= limite; p++)
        if (!composto[p])
            for (long m = p * p; m <= limite; m += p)   /* cancello i multipli di p */
                composto[m] = true;

    long n = 0;
    for (long k = 2; k <= limite; k++)
        if (!composto[k]) n++;
    return n;
}

int main(void)
{
    bool piccolo[101] = {false};
    long n = crivello(piccolo, 100);
    int colonna = 0;
    for (int k = 2; k <= 100; k++)
        if (!piccolo[k]) {
            printf("%4d", k);
            if (++colonna % 10 == 0) printf("\n");
        }
    printf("\n%ld primi fino a 100\n", n);

    const long GRANDE = 1000000;
    bool *grande = calloc((size_t)GRANDE + 1, sizeof *grande);   /* calloc azzera la memoria */
    if (grande == NULL) {
        fprintf(stderr, "memoria insufficiente\n");
        return 1;
    }
    printf("%ld primi fino a %ld\n", crivello(grande, GRANDE), GRANDE);
    free(grande);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97
25 primi fino a 100
78498 primi fino a 1000000
```

Commento

Il crivello sostituisce le divisioni con semplici scritture in un array: fino a un milione è decine di volte più veloce del test di primalità ripetuto per ogni numero. È un caso tipico di scambio tra memoria e tempo: un byte per numero in cambio della velocità. `calloc` alloca e azzera, cioè imposta tutti i valori a `false`.

17.2

#### Conversioni tra basi numeriche

*Intermedio*OnlineGDB: Sì

Consegna

Scrivere una funzione che converta un numero senza segno in una stringa in qualsiasi base da 2 a 16, e usarla per stampare una tabella decimale / binario / ottale / esadecimale. Convertire poi alcune stringhe in numero con `strtol`, segnalando quelle non valide.

Suggerimento

Le cifre si ottengono con il resto della divisione per la base, dalla meno significativa: vanno poi scritte in ordine inverso.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 17.2 - Conversioni tra basi */
#include <stdio.h>
#include <stdlib.h>

/* rappresentazione di valore in base 2..16 dentro buf; NULL se base o spazio non validi */
char *in_base(unsigned long valore, unsigned base, char *buf, size_t dim)
{
    const char cifre[] = "0123456789ABCDEF";
    char tmp[65];
    size_t n = 0;
    if (base < 2 || base > 16)
        return NULL;
    do {
        tmp[n++] = cifre[valore % base];   /* cifra meno significativa */
        valore /= base;
    } while (valore > 0);                  /* do-while: anche 0 produce la cifra "0" */
    if (n + 1 > dim)
        return NULL;
    for (size_t i = 0; i < n; i++)
        buf[i] = tmp[n - 1 - i];           /* inverto l'ordine delle cifre */
    buf[n] = '\0';
    return buf;
}

int main(void)
{
    unsigned long valori[] = {0, 10, 255, 1000, 65535};
    char b2[65], b8[23], b16[17];

    printf("%8s %18s %8s %6s\n", "decimale", "binario", "ottale", "hex");
    for (int i = 0; i < 5; i++)
        printf("%8lu %18s %8s %6s\n", valori[i],
               in_base(valori[i], 2, b2, sizeof b2),
               in_base(valori[i], 8, b8, sizeof b8),
               in_base(valori[i], 16, b16, sizeof b16));

    const char *testi[] = {"1011", "0x1F", "777", "12A", "Z9"};
    int basi[] = {2, 16, 8, 10, 10};
    printf("\n");
    for (int i = 0; i < 5; i++) {
        char *fine;
        long v = strtol(testi[i], &fine, basi[i]);
        if (fine == testi[i] || *fine != '\0')     /* nessuna cifra, o caratteri avanzati */
            printf("\"%s\" non valido in base %d (lettura ferma a \"%s\")\n", testi[i], basi[i], fine);
        else
            printf("\"%s\" in base %d = %ld\n", testi[i], basi[i], v);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
decimale            binario   ottale    hex
       0                  0        0      0
      10               1010       12      A
     255           11111111      377     FF
    1000         1111101000     1750    3E8
   65535   1111111111111111   177777   FFFF

"1011" in base 2 = 11
"0x1F" in base 16 = 31
"777" in base 8 = 511
"12A" non valido in base 10 (lettura ferma a "A")
"Z9" non valido in base 10 (lettura ferma a "Z9")
```

Commento

`printf` sa già stampare in ottale (`%o`) ed esadecimale (`%X`), ma non in binario: per il binario la funzione va scritta. `strtol` con base 16 accetta anche il prefisso `0x`; con base 0 riconosce da sola il prefisso (`0x` esadecimale, `0` ottale). Il parametro `fine` permette di distinguere "12" da "12A": `atoi` restituirebbe 12 in entrambi i casi.

17.3

#### math.h per il tecnico

*Intermedio*OnlineGDB: Sì

Consegna

Mostrare con un programma: (1) la differenza tra `round`, `floor`, `ceil` e `trunc` su numeri positivi e negativi; (2) la normalizzazione di un angolo in \[0, 360) con `fmod`; (3) la conversione da coordinate cartesiane a polari con `hypot` e `atan2`; (4) la generazione di una tabella di 8 campioni di seno per un DAC a 12 bit.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 17.3 - Funzioni di math.h */
#include <stdio.h>
#include <math.h>

static const double PI = 3.14159265358979323846;   /* M_PI non è standard C11 */

int main(void)
{
    /* 1. arrotondamenti */
    double x[] = {2.5, -2.5, 2.4, -2.6};
    printf("%6s %7s %7s %7s %7s\n", "x", "round", "floor", "ceil", "trunc");
    for (int i = 0; i < 4; i++)
        printf("%6.1f %7.1f %7.1f %7.1f %7.1f\n", x[i], round(x[i]), floor(x[i]), ceil(x[i]), trunc(x[i]));

    /* 2. normalizzazione di un angolo */
    double angoli[] = {370.0, -30.0, 725.5};
    printf("\n");
    for (int i = 0; i < 3; i++) {
        double a = fmod(angoli[i], 360.0);   /* resto reale: mantiene il segno */
        if (a < 0.0) a += 360.0;
        printf("%7.1f gradi -> %6.1f gradi\n", angoli[i], a);
    }

    /* 3. cartesiane -> polari */
    double p[][2] = {{3, 4}, {-1, 1}, {0, -2}};
    printf("\n");
    for (int i = 0; i < 3; i++) {
        double r = hypot(p[i][0], p[i][1]);                  /* sqrt(x^2 + y^2) senza overflow */
        double teta = atan2(p[i][1], p[i][0]) * 180.0 / PI;  /* angolo nel quadrante corretto */
        printf("(%4.1f, %4.1f) -> r = %.3f, angolo = %7.2f gradi\n", p[i][0], p[i][1], r, teta);
    }

    /* 4. tabella di seno per DAC a 12 bit (0..4095) */
    printf("\nLUT seno 8 punti:");
    for (int k = 0; k < 8; k++) {
        long campione = lround((sin(2.0 * PI * k / 8.0) + 1.0) * 2047.5);   /* -1..1 -> 0..4095 */
        printf(" %ld", campione);
    }
    printf("\n");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog -lm
```

Esecuzione

terminale

```
$ ./prog
     x   round   floor    ceil   trunc
   2.5     3.0     2.0     3.0     2.0
  -2.5    -3.0    -3.0    -2.0    -2.0
   2.4     2.0     2.0     3.0     2.0
  -2.6    -3.0    -3.0    -2.0    -2.0

  370.0 gradi ->   10.0 gradi
  -30.0 gradi ->  330.0 gradi
  725.5 gradi ->    5.5 gradi

( 3.0,  4.0) -> r = 5.000, angolo =   53.13 gradi
(-1.0,  1.0) -> r = 1.414, angolo =  135.00 gradi
( 0.0, -2.0) -> r = 2.000, angolo =  -90.00 gradi

LUT seno 8 punti: 2048 3495 4095 3495 2048 600 0 600
```

Su OnlineGDB

Se il linker segnala `undefined reference` a funzioni matematiche, aggiungere `-lm` in *Extra Compiler Flags*.

Commento

`round` porta i casi .5 lontano da zero; `floor` e `ceil` vanno sempre verso −∞ e +∞; `trunc` taglia verso lo zero, come il cast a `int`. `atan2(y, x)` restituisce l'angolo nel quadrante giusto, cosa che `atan(y/x)` non fa (e fallisce con x = 0): è la funzione da usare per encoder, joystick e calcoli di direzione. La tabella di seno precalcolata è la base dei generatori di forme d'onda con DAC o PWM.

17.4

#### Tabella hash per codici articolo

*Progetto*OnlineGDB: Sì

Consegna

Realizzare una tabella hash a *chaining* che associ a un codice articolo (stringa) la giacenza. Usare la funzione di hash djb2 e 8 bucket (pochi apposta, per vedere le collisioni). Implementare inserimento (o aggiornamento se il codice esiste), ricerca, stampa del contenuto di ogni bucket e liberazione della memoria.

Suggerimento

Ogni bucket è la testa di una lista concatenata dei codici che hanno lo stesso valore di hash modulo il numero di bucket.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 17.4 - Tabella hash con liste di collisione */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define N_BUCKET 8

typedef struct Voce {
    char codice[12];
    int  giacenza;
    struct Voce *next;            /* altri codici nello stesso bucket */
} Voce;

typedef struct {
    Voce *bucket[N_BUCKET];
} Tabella;

uint32_t hash_djb2(const char *s)  /* uint32_t: stesso risultato su ogni piattaforma */
{
    uint32_t h = 5381;
    for (; *s != '\0'; s++)
        h = h * 33u + (unsigned char)*s;
    return h;
}

void tab_init(Tabella *t)
{
    for (int i = 0; i < N_BUCKET; i++)
        t->bucket[i] = NULL;
}

Voce *tab_cerca(const Tabella *t, const char *codice)
{
    Voce *v = t->bucket[hash_djb2(codice) % N_BUCKET];   /* vado diretto al bucket */
    for (; v != NULL; v = v->next)                        /* e scorro solo la sua lista */
        if (strcmp(v->codice, codice) == 0)
            return v;
    return NULL;
}

int tab_inserisci(Tabella *t, const char *codice, int giacenza)
{
    Voce *v = tab_cerca(t, codice);
    if (v != NULL) {                 /* già presente: aggiorno */
        v->giacenza = giacenza;
        return 0;
    }
    v = malloc(sizeof *v);
    if (v == NULL) return -1;
    snprintf(v->codice, sizeof v->codice, "%s", codice);   /* copia sicura, troncata se lunga */
    v->giacenza = giacenza;
    uint32_t b = hash_djb2(codice) % N_BUCKET;
    v->next = t->bucket[b];          /* inserimento in testa alla lista del bucket */
    t->bucket[b] = v;
    return 1;
}

void tab_stampa(const Tabella *t)
{
    for (int i = 0; i < N_BUCKET; i++) {
        printf("bucket %d:", i);
        for (const Voce *v = t->bucket[i]; v != NULL; v = v->next)
            printf(" [%s %d]", v->codice, v->giacenza);
        printf("\n");
    }
}

void tab_libera(Tabella *t)
{
    for (int i = 0; i < N_BUCKET; i++) {
        Voce *v = t->bucket[i];
        while (v != NULL) {
            Voce *succ = v->next;
            free(v);
            v = succ;
        }
        t->bucket[i] = NULL;
    }
}

int main(void)
{
    const char *codici[] = {"M0342", "S0110", "R0007", "I0215", "C0099",
                            "V0410", "P1200", "F0033", "E0501", "T0777"};
    int giacenze[] = {15, 40, 120, 2, 8, 33, 5, 60, 12, 3};

    Tabella t;
    tab_init(&t);
    for (int i = 0; i < 10; i++)
        tab_inserisci(&t, codici[i], giacenze[i]);
    tab_inserisci(&t, "R0007", 95);          /* aggiornamento di un codice esistente */
    tab_stampa(&t);

    const char *cercati[] = {"I0215", "R0007", "X9999"};
    for (int i = 0; i < 3; i++) {
        Voce *v = tab_cerca(&t, cercati[i]);
        if (v != NULL) printf("%s: giacenza %d\n", cercati[i], v->giacenza);
        else           printf("%s: non presente\n", cercati[i]);
    }
    tab_libera(&t);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
bucket 0: [E0501 12] [P1200 5] [V0410 33]
bucket 1: [F0033 60]
bucket 2: [C0099 8] [S0110 40]
bucket 3: [M0342 15]
bucket 4:
bucket 5:
bucket 6: [T0777 3] [I0215 2] [R0007 95]
bucket 7:
I0215: giacenza 2
R0007: giacenza 95
X9999: non presente
```

Commento

Con 10 codici in 8 bucket alcune liste hanno più elementi (collisioni), ma ogni ricerca scorre solo poche voci invece di tutto l'archivio. Se il numero di bucket cresce in proporzione ai dati, la ricerca richiede in media un tempo costante, O(1): è la struttura dietro i dizionari di Python, gli oggetti JavaScript e le tabelle di routing. `snprintf` è usata come copia di stringa sicura: non scrive mai oltre la dimensione indicata.

Modulo 18

### Algoritmi applicati

4 esercizi

Concetti chiave

Quattro problemi completi, ciascuno ispirato a un caso reale di automazione: la regolazione di temperatura, il ciclo di una stazione pick-and-place, la ricerca del percorso di un veicolo a guida automatica (AGV) e la lettura di un ricevitore GPS. In tutti gli esercizi la parte "fisica" (forno, attuatori, mappa, ricevitore) è **simulata** nel programma stesso: è la tecnica con cui si collaudano gli algoritmi prima di portarli sull'hardware, e permette di provarli anche su OnlineGDB.

18.1

#### Regolatore PID su un forno simulato

*Progetto*OnlineGDB: Sì

Consegna

Simulare un forno come sistema del primo ordine (temperatura ambiente 20 °C, costante di tempo 60 s, guadagno 2 °C per ogni % di potenza) e regolarne la temperatura a 150 °C con un PID discreto (passo 1 s, uscita limitata a 0-100 %). Implementare l'anti-windup dell'integrale. Stampare ogni 20 s temperatura, errore e potenza con una barra grafica, e confrontare la sovraelongazione con e senza anti-windup.

Suggerimento

u = Kp·e + Ki·∫e dt + Kd·de/dt. Anti-windup: se l'uscita è in saturazione e l'errore la spingerebbe ancora oltre, l'integrale non va aggiornato.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 18.1 - PID discreto con anti-windup */
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    double kp, ki, kd;
    double u_min, u_max;        /* limiti dell'attuatore */
    double integrale;
    double errore_prec;
    bool   anti_windup;
} Pid;

double pid_passo(Pid *c, double setpoint, double misura, double dt)
{
    double e = setpoint - misura;
    double derivata = (e - c->errore_prec) / dt;
    c->errore_prec = e;

    double nuovo_int = c->integrale + e * dt;
    double u = c->kp * e + c->ki * nuovo_int + c->kd * derivata;

    if (u > c->u_max) {
        u = c->u_max;
        if (c->anti_windup && e > 0) return u;   /* saturo in alto: non accumulo */
    } else if (u < c->u_min) {
        u = c->u_min;
        if (c->anti_windup && e < 0) return u;   /* saturo in basso: non accumulo */
    }
    c->integrale = nuovo_int;
    return u;
}

typedef struct {
    double t;                   /* temperatura [C] */
    double t_amb, tau, k;       /* ambiente, costante di tempo [s], guadagno [C/%] */
} Forno;

void forno_passo(Forno *f, double potenza, double dt)   /* modello del primo ordine (Eulero) */
{
    double t_regime = f->t_amb + f->k * potenza;
    f->t += (t_regime - f->t) * dt / f->tau;
}

double simula(bool anti_windup, bool stampa)
{
    Forno f = { .t = 20.0, .t_amb = 20.0, .tau = 60.0, .k = 2.0 };
    Pid c = { .kp = 4.0, .ki = 0.08, .kd = 0.0, .u_min = 0.0, .u_max = 100.0,
              .integrale = 0.0, .errore_prec = 0.0, .anti_windup = anti_windup };
    const double setpoint = 150.0, dt = 1.0;
    double massimo = f.t;

    for (int s = 0; s <= 400; s++) {
        double u = pid_passo(&c, setpoint, f.t, dt);
        if (stampa && s % 20 == 0) {
            printf("t=%3d s  T=%6.1f C  e=%6.1f  u=%5.1f%% |", s, f.t, setpoint - f.t, u);
            for (int b = 0; b < (int)(u / 5.0); b++) putchar('#');   /* una # ogni 5% */
            putchar('\n');
        }
        forno_passo(&f, u, dt);
        if (f.t > massimo) massimo = f.t;
    }
    double so = massimo - setpoint;
    return so > 0.0 ? so : 0.0;          /* nessun superamento: 0 */
}

int main(void)
{
    printf("PID con anti-windup, setpoint 150 C\n");
    double so_con = simula(true, true);
    double so_senza = simula(false, false);
    printf("\nSovraelongazione con anti-windup  : %5.1f C\n", so_con);
    printf("Sovraelongazione senza anti-windup: %5.1f C\n", so_senza);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
PID con anti-windup, setpoint 150 C
t=  0 s  T=  20.0 C  e= 130.0  u=100.0% |####################
t= 20 s  T=  77.1 C  e=  72.9  u=100.0% |####################
t= 40 s  T= 117.9 C  e=  32.1  u=100.0% |####################
t= 60 s  T= 137.9 C  e=  12.1  u= 69.8% |#############
t= 80 s  T= 142.6 C  e=   7.4  u= 66.0% |#############
t=100 s  T= 145.1 C  e=   4.9  u= 65.5% |#############
t=120 s  T= 146.7 C  e=   3.3  u= 65.3% |#############
t=140 s  T= 147.8 C  e=   2.2  u= 65.2% |#############
t=160 s  T= 148.6 C  e=   1.4  u= 65.2% |#############
t=180 s  T= 149.0 C  e=   1.0  u= 65.1% |#############
t=200 s  T= 149.4 C  e=   0.6  u= 65.1% |#############
t=220 s  T= 149.6 C  e=   0.4  u= 65.0% |#############
t=240 s  T= 149.7 C  e=   0.3  u= 65.0% |#############
t=260 s  T= 149.8 C  e=   0.2  u= 65.0% |#############
t=280 s  T= 149.9 C  e=   0.1  u= 65.0% |#############
t=300 s  T= 149.9 C  e=   0.1  u= 65.0% |#############
t=320 s  T= 149.9 C  e=   0.1  u= 65.0% |#############
t=340 s  T= 150.0 C  e=   0.0  u= 65.0% |#############
t=360 s  T= 150.0 C  e=   0.0  u= 65.0% |#############
t=380 s  T= 150.0 C  e=   0.0  u= 65.0% |#############
t=400 s  T= 150.0 C  e=   0.0  u= 65.0% |#############

Sovraelongazione con anti-windup  :   0.0 C
Sovraelongazione senza anti-windup:  32.9 C
```

Commento

All'avvio l'errore è grande, l'uscita resta al 100 % e, senza anti-windup, l'integrale continua a crescere: quando la temperatura arriva al setpoint il termine integrale è enorme e il forno lo supera di molto prima di "scaricarlo". Il confronto finale lo mostra in numeri. I PLC hanno blocchi PID già pronti (es. PID_Compact), ma la logica interna è questa: scriverla aiuta a scegliere i parametri e a capire i comportamenti anomali. Esercizio di estensione: aggiungere un disturbo (apertura della porta del forno) e osservare la reazione.

18.2

#### Macchina a stati: stazione pick-and-place

*Progetto*OnlineGDB: Sì

Consegna

Una stazione preleva pezzi con una ventosa: un cilindro verticale (finecorsa alto/basso), un traslatore orizzontale (finecorsa sinistra/destra), un vacuostato che conferma la presa. Ciclo: attesa pezzo → discesa → presa (con timeout di 5 cicli sul vuoto) → salita → traslazione → rilascio → ritorno. Implementare la logica come macchina a stati con `enum` e `switch`, separata dalla simulazione dell'impianto, e simulare due pezzi: il secondo con un guasto del vuoto che deve portare in ALLARME.

Suggerimento

Uscite di Moore: dipendono solo dallo stato. A ogni ciclo: leggo gli ingressi, calcolo stato e uscite, aggiorno l'impianto simulato. Stampo solo i cambi di stato.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 18.2 - Macchina a stati pick-and-place */
#include <stdio.h>
#include <stdbool.h>

typedef enum { ATTESA, DISCESA, PRESA, SALITA, TRASLAZIONE, RILASCIO, RITORNO, ALLARME } Stato;
static const char *NOMI[] = {"ATTESA", "DISCESA", "PRESA", "SALITA",
                             "TRASLAZIONE", "RILASCIO", "RITORNO", "ALLARME"};

typedef struct { bool pezzo, alto, basso, sinistra, destra, vuoto_ok; } Ingressi;
typedef struct { bool giu, vuoto, a_destra; } Uscite;

/* ------------------------------------------------ logica di controllo */
typedef struct {
    Stato stato;
    int   cicli_nello_stato;    /* per i timeout */
} Controllo;

#define TIMEOUT_VUOTO 5

Uscite controllo_passo(Controllo *c, const Ingressi *in)
{
    Stato prossimo = c->stato;
    switch (c->stato) {
    case ATTESA:      if (in->pezzo && in->alto && in->sinistra) prossimo = DISCESA; break;
    case DISCESA:     if (in->basso) prossimo = PRESA; break;
    case PRESA:
        if (in->vuoto_ok)                                   prossimo = SALITA;
        else if (c->cicli_nello_stato >= TIMEOUT_VUOTO)     prossimo = ALLARME;
        break;
    case SALITA:      if (in->alto) prossimo = TRASLAZIONE; break;
    case TRASLAZIONE: if (in->destra) prossimo = RILASCIO; break;
    case RILASCIO:    if (c->cicli_nello_stato >= 1) prossimo = RITORNO; break;
    case RITORNO:     if (in->sinistra) prossimo = ATTESA; break;
    case ALLARME:     break;                                /* serve un reset manuale */
    }
    if (prossimo != c->stato) {
        c->stato = prossimo;
        c->cicli_nello_stato = 0;
    } else {
        c->cicli_nello_stato++;
    }

    Uscite u = {false, false, false};                       /* uscite di Moore */
    switch (c->stato) {
    case DISCESA:     u.giu = true; break;
    case PRESA:       u.giu = true; u.vuoto = true; break;
    case SALITA:      u.vuoto = true; break;
    case TRASLAZIONE: u.vuoto = true; u.a_destra = true; break;
    case RILASCIO:    u.a_destra = true; break;
    default:          break;                                /* ATTESA, RITORNO, ALLARME: tutto off */
    }
    return u;
}

/* ------------------------------------------------ impianto simulato */
typedef struct {
    int  z, x;                  /* z: 0 alto .. 2 basso; x: 0 sinistra .. 3 destra */
    int  cicli_vuoto;
    bool pezzo_in_ingresso;
    bool pezzo_preso;
    bool guasto_vuoto;
} Impianto;

Ingressi impianto_leggi(const Impianto *p)
{
    Ingressi in;
    in.pezzo    = p->pezzo_in_ingresso;
    in.alto     = (p->z == 0);
    in.basso    = (p->z == 2);
    in.sinistra = (p->x == 0);
    in.destra   = (p->x == 3);
    in.vuoto_ok = (p->cicli_vuoto >= 2) && !p->guasto_vuoto;   /* il vuoto si forma in 2 cicli */
    return in;
}

void impianto_passo(Impianto *p, const Uscite *u)
{
    if (u->giu  && p->z < 2) p->z++;            /* il cilindro si muove di un passo per ciclo */
    if (!u->giu && p->z > 0) p->z--;
    if (u->a_destra  && p->x < 3) p->x++;
    if (!u->a_destra && p->x > 0) p->x--;
    p->cicli_vuoto = u->vuoto ? p->cicli_vuoto + 1 : 0;
    if (u->vuoto && p->cicli_vuoto >= 2 && !p->guasto_vuoto && p->z == 2) {
        p->pezzo_preso = true;                  /* il pezzo lascia la postazione d'ingresso */
        p->pezzo_in_ingresso = false;
    }
    if (!u->vuoto) p->pezzo_preso = false;      /* rilasciato */
}

int main(void)
{
    Controllo c = {ATTESA, 0};
    Impianto p = {0, 0, 0, false, false, false};
    Stato prec = ALLARME;

    for (int ciclo = 0; ciclo < 45; ciclo++) {
        if (ciclo == 2)  p.pezzo_in_ingresso = true;                    /* primo pezzo */
        if (ciclo == 22) { p.pezzo_in_ingresso = true; p.guasto_vuoto = true; }   /* secondo, con guasto */

        Ingressi in = impianto_leggi(&p);
        Uscite u = controllo_passo(&c, &in);
        if (c.stato != prec) {
            printf("ciclo %2d: %-11s  giu=%d vuoto=%d destra=%d\n",
                   ciclo, NOMI[c.stato], u.giu, u.vuoto, u.a_destra);
            prec = c.stato;
        }
        impianto_passo(&p, &u);
    }
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
ciclo  0: ATTESA       giu=0 vuoto=0 destra=0
ciclo  2: DISCESA      giu=1 vuoto=0 destra=0
ciclo  4: PRESA        giu=1 vuoto=1 destra=0
ciclo  6: SALITA       giu=0 vuoto=1 destra=0
ciclo  8: TRASLAZIONE  giu=0 vuoto=1 destra=1
ciclo 11: RILASCIO     giu=0 vuoto=0 destra=1
ciclo 13: RITORNO      giu=0 vuoto=0 destra=0
ciclo 16: ATTESA       giu=0 vuoto=0 destra=0
ciclo 22: DISCESA      giu=1 vuoto=0 destra=0
ciclo 24: PRESA        giu=1 vuoto=1 destra=0
ciclo 30: ALLARME      giu=0 vuoto=0 destra=0
```

Commento

La separazione tra `controllo_passo` (la logica) e `impianto_*` (la simulazione) è il punto chiave: su un microcontrollore o un PLC si sostituisce solo la parte di simulazione con la lettura e scrittura degli I/O veri. Lo stato ALLARME porta tutte le uscite a riposo e ne esce solo con un reset, come richiede la sicurezza delle macchine. La stessa struttura si traduce direttamente in SFC (Sequential Function Chart) o in ST con un `CASE` sullo stato.

18.3

#### Percorso minimo di un AGV con BFS

*Progetto*OnlineGDB: Sì

Consegna

La pianta di un magazzino è una griglia di caratteri: `#` ostacolo, `.` corsia libera, `S` partenza, `G` destinazione. Trovare il percorso più breve (movimenti in 4 direzioni) con la ricerca in ampiezza (BFS), stamparne la lunghezza e disegnarlo sulla mappa con `*`. Gestire il caso in cui la destinazione non è raggiungibile.

Suggerimento

BFS: una coda di celle da esplorare, partendo da S; per ogni cella si accodano i vicini liberi non ancora visitati, memorizzando da quale cella si è arrivati. Il percorso si ricostruisce a ritroso da G.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 18.3 - BFS su griglia: percorso minimo */
#include <stdio.h>
#include <string.h>

#define RIGHE   6
#define COLONNE 12

typedef struct { int r, c; } Cella;

/* restituisce la lunghezza del percorso (passi), -1 se G non è raggiungibile; disegna il percorso */
int bfs(char mappa[RIGHE][COLONNE + 1])
{
    int dist[RIGHE][COLONNE];
    Cella prec[RIGHE][COLONNE];
    Cella coda[RIGHE * COLONNE];
    int testa = 0, fondo = 0;
    Cella s = {-1, -1}, g = {-1, -1};

    for (int r = 0; r < RIGHE; r++)
        for (int c = 0; c < COLONNE; c++) {
            dist[r][c] = -1;                         /* -1 = non visitata */
            if (mappa[r][c] == 'S') s = (Cella){r, c};
            if (mappa[r][c] == 'G') g = (Cella){r, c};
        }
    if (s.r < 0 || g.r < 0) return -1;

    const int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};   /* su, giù, sinistra, destra */
    dist[s.r][s.c] = 0;
    coda[fondo++] = s;
    while (testa < fondo) {
        Cella u = coda[testa++];                     /* estraggo dalla coda (FIFO) */
        if (u.r == g.r && u.c == g.c) break;
        for (int k = 0; k < 4; k++) {
            int nr = u.r + dr[k], nc = u.c + dc[k];
            if (nr < 0 || nr >= RIGHE || nc < 0 || nc >= COLONNE) continue;   /* fuori mappa */
            if (mappa[nr][nc] == '#' || dist[nr][nc] >= 0) continue;          /* ostacolo o già vista */
            dist[nr][nc] = dist[u.r][u.c] + 1;
            prec[nr][nc] = u;                        /* ricordo da dove arrivo */
            coda[fondo++] = (Cella){nr, nc};
        }
    }
    if (dist[g.r][g.c] < 0) return -1;

    for (Cella p = prec[g.r][g.c]; !(p.r == s.r && p.c == s.c); p = prec[p.r][p.c])
        mappa[p.r][p.c] = '*';                       /* ricostruisco a ritroso da G */
    return dist[g.r][g.c];
}

void stampa(char mappa[RIGHE][COLONNE + 1])
{
    for (int r = 0; r < RIGHE; r++)
        printf("   %s\n", mappa[r]);
}

int main(void)
{
    char mappa[RIGHE][COLONNE + 1] = {
        "S...#.......",
        ".##.#.####..",
        ".#..#....#..",
        ".#.####.##.#",
        ".#......#...",
        "...##.#...#G",
    };
    char copia[RIGHE][COLONNE + 1];
    memcpy(copia, mappa, sizeof mappa);

    int n = bfs(mappa);
    printf("Percorso minimo: %d passi\n", n);
    stampa(mappa);

    copia[4][9] = '#';                               /* chiudo una corsia */
    copia[3][10] = '#';
    copia[5][9] = '#';
    n = bfs(copia);
    printf("\nCon corsie chiuse: %s\n", n < 0 ? "destinazione non raggiungibile" : "raggiungibile");
    stampa(copia);
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
Percorso minimo: 20 passi
   S...#.......
   *##.#.####..
   *#..#....#..
   *#.####.##.#
   *#******#***
   ***##.#***#G

Con corsie chiuse: destinazione non raggiungibile
   S...#.......
   .##.#.####..
   .#..#....#..
   .#.####.####
   .#......##..
   ...##.#..##G
```

Commento

La BFS esplora le celle "a onde" di distanza crescente, quindi la prima volta che raggiunge G lo fa con il percorso più corto. La coda è un semplice array con due indici, perché ogni cella entra al massimo una volta. Con costi diversi per cella (corsie lente, curve) si passa all'algoritmo di Dijkstra o ad A\*, usati dai sistemi di navigazione degli AGV e dai videogiochi.

18.4

#### Lettura di frasi NMEA da un GPS

*Avanzato*OnlineGDB: Sì

Consegna

I ricevitori GPS trasmettono frasi testuali NMEA 0183, come `$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47`. Verificare il checksum (XOR di tutti i caratteri tra `$` e `*`, confrontato con le due cifre esadecimali finali), separare i campi conservando quelli vuoti, e stampare ora, latitudine e longitudine in gradi decimali, qualità del fix, numero di satelliti e quota.

Suggerimento

`strtok` salta i campi vuoti (`,,`): serve una funzione di separazione propria basata su `strchr`. La latitudine `4807.038` significa 48° e 07,038 minuti.

Mostra la soluzioneNascondi la soluzione

main.cC

```
/* Esercizio 18.4 - Frasi NMEA GGA */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_CAMPI 20

bool checksum_ok(const char *frase)
{
    if (frase[0] != '$') return false;
    const char *asterisco = strchr(frase, '*');
    if (asterisco == NULL) return false;
    unsigned char x = 0;
    for (const char *p = frase + 1; p < asterisco; p++)
        x ^= (unsigned char)*p;                      /* XOR di tutti i caratteri */
    unsigned long atteso = strtoul(asterisco + 1, NULL, 16);
    return x == atteso;
}

/* divide s sui separatori ',' e '*' conservando i campi vuoti; restituisce il numero di campi */
int dividi(char *s, char *campi[], int max)
{
    int n = 0;
    campi[n++] = s;
    for (char *p = s; *p != '\0' && n < max; p++)
        if (*p == ',' || *p == '*') {
            *p = '\0';                               /* chiudo il campo corrente */
            campi[n++] = p + 1;                      /* il prossimo inizia subito dopo */
        }
    return n;
}

double gradi_decimali(const char *valore, const char *emisfero)
{
    double v = atof(valore);                         /* formato (g)ggmm.mmmm */
    int gradi = (int)(v / 100.0);
    double minuti = v - gradi * 100.0;
    double d = gradi + minuti / 60.0;
    if (emisfero[0] == 'S' || emisfero[0] == 'W') d = -d;
    return d;
}

void analizza(const char *frase)
{
    printf("%s\n", frase);
    if (!checksum_ok(frase)) {
        printf("  checksum NON valido: frase scartata\n\n");
        return;
    }
    char buf[100];
    snprintf(buf, sizeof buf, "%s", frase + 1);      /* copia senza il '$' */
    char *f[MAX_CAMPI];
    int n = dividi(buf, f, MAX_CAMPI);
    if (n < 15 || strcmp(f[0] + 2, "GGA") != 0) {    /* GPGGA, GNGGA... */
        printf("  frase non GGA o incompleta\n\n");
        return;
    }
    printf("  ora UTC   : %.2s:%.2s:%.2s\n", f[1], f[1] + 2, f[1] + 4);
    printf("  latitudine: %.6f\n", gradi_decimali(f[2], f[3]));
    printf("  longitud. : %.6f\n", gradi_decimali(f[4], f[5]));
    printf("  fix       : %s   satelliti: %d   quota: %s m\n", f[6], atoi(f[7]), f[9]);
    printf("  campi     : %d (il penultimo vuoto è conservato: \"%s\")\n\n", n, f[n - 2]);
}

int main(void)
{
    analizza("$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47");
    analizza("$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.9,M,46.9,M,,*47");
    return 0;
}
```

Compilazione

```
$ gcc -Wall -Wextra -std=c11 main.c -o prog
```

Esecuzione

terminale

```
$ ./prog
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
  ora UTC   : 12:35:19
  latitudine: 48.117300
  longitud. : 11.516667
  fix       : 1   satelliti: 8   quota: 545.4 m
  campi     : 16 (il penultimo vuoto è conservato: "")

$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.9,M,46.9,M,,*47
  checksum NON valido: frase scartata
```

Commento

La prima frase è l'esempio classico dello standard; nella seconda una sola cifra della quota è cambiata e il checksum lo rileva. Il checksum NMEA è un semplice XOR: rileva molti errori ma non tutti, a differenza del CRC dell'esercizio 15.5. I campi vuoti sono normali nelle frasi NMEA (dato non disponibile): un parser che li salta sposterebbe tutti i campi successivi e leggerebbe valori sbagliati senza accorgersene.

## Appendice

### A · Specificatori di formato più usati

| Tipo | printf | scanf | Note |
| --- | --- | --- | --- |
| `int` | `%d` | `%d` | `%5d` larghezza 5, `%05d` con zeri, `%-5d` a sinistra |
| `unsigned int` | `%u` `%x` `%X` | `%u` `%x` | esadecimale minuscolo / maiuscolo |
| `long` / `long long` | `%ld` / `%lld` | `%ld` / `%lld` | `unsigned long long`: `%llu` |
| `double` | `%f` `%e` `%g` | `%lf` | `%.3f` tre decimali; in scanf `%f` è per `float` |
| `char` | `%c` | `" %c"` | lo spazio prima di `%c` in scanf salta spazi e a capo |
| stringa | `%s` | `%19s` | in scanf indicare sempre la larghezza massima (dimensione − 1) |
| `size_t` | `%zu` | `%zu` | risultato di `sizeof` e `strlen` |
| puntatore | `%p` | — | convertire a `(void *)` |
| il carattere % | `%%` | — |  |

### B · Messaggi di gcc frequenti e loro causa

| Messaggio (estratto) | Causa probabile | Rimedio |
| --- | --- | --- |
| `expected ';' before ...` | punto e virgola mancante, spesso nella riga **precedente** | controllare la fine della riga sopra |
| `implicit declaration of function` | funzione usata senza prototipo o senza l'`#include` giusto | aggiungere prototipo / header |
| `format '%d' expects argument of type 'int *'` | `&` dimenticata in `scanf`, o specificatore errato | `scanf("%d", &x)` |
| `suggest parentheses around assignment used as truth value` | `if (x = 5)` al posto di `if (x == 5)` | usare `==` |
| `control reaches end of non-void function` | una funzione non `void` può terminare senza `return` | coprire tutti i percorsi |
| `'x' is used uninitialized` | variabile letta prima di averle assegnato un valore | inizializzare alla dichiarazione |
| `unused variable` | variabile dichiarata e mai usata | eliminarla |
| `undefined reference to 'sqrt'` | errore del **linker**: libreria non collegata | aggiungere `-lm` in fondo al comando |
| `undefined reference to 'funzione'` | il `.c` che la definisce non è stato compilato/collegato | aggiungere il file al comando o al Makefile |
| `multiple definition of 'x'` | variabile *definita* in un header incluso da più file | nell'header solo `extern`, definizione in un .c |
| `fatal error: xxx.h: No such file or directory` | header non trovato | controllare nome, virgolette, opzione `-I` |
| `Makefile: *** missing separator` | riga di comando indentata con spazi | usare un carattere TAB |
| `Segmentation fault` (in esecuzione) | accesso a memoria non valida: indice fuori dai limiti, puntatore NULL, `&` mancante | ricompilare con `-g -fsanitize=address` |

### C · Comandi di riferimento

```
# programma su un solo file
$ gcc -Wall -Wextra -std=c11 main.c -o prog
# più moduli in un solo passaggio
$ gcc -Wall -Wextra -std=c11 main.c modulo.c -o prog
# compilazione separata e link
$ gcc -Wall -Wextra -std=c11 -c modulo.c
$ gcc main.o modulo.o -o prog
# libreria statica
$ ar rcs libmodulo.a modulo.o
$ gcc main.c -L. -lmodulo -o prog
# libreria dinamica
$ gcc -fPIC -c modulo.c && gcc -shared -o libmodulo.so modulo.o
$ LD_LIBRARY_PATH=. ./prog
# debug: simboli per gdb e controllo degli accessi in memoria
$ gcc -Wall -Wextra -std=c11 -g -fsanitize=address main.c -o prog
```

Programmare in C — dispensa ITS · Compilatore di riferimento: GCC 13, standard C11, Linux x86-64