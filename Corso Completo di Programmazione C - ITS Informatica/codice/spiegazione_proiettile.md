# Simulatore di traiettorie in C ANSI: guida dettagliata al codice

Documento relativo al sorgente `proiettile.c`, versione per terminale con cinque traiettorie ASCII a colori. La versione grafica con raylib è soltanto una possibile evoluzione e non è implementata nel sorgente qui descritto.

## Indice

1. Obiettivo e comportamento generale
2. C ANSI, ASCII e sequenze ANSI
3. Compilazione ed esecuzione
4. Modello fisico e derivazione delle formule
5. Organizzazione del programma
6. Librerie incluse
7. Costanti e configurazione
8. Colori e simboli
9. Tipi, puntatori, array e durata delle variabili
10. Lettura e validazione dell'input
11. Preparazione dei dati fisici e delle scale
12. Trasformazione delle coordinate e rasterizzazione
13. Stampa del grafico e della tabella
14. Funzione main e flusso di esecuzione
15. Esempio numerico completo
16. Precisione, complessità e limiti
17. Verifiche riproducibili
18. Modifiche possibili e percorso verso la grafica
19. Glossario e sorgente integrale

## 1. Obiettivo e comportamento generale

Il programma confronta il moto di cinque proiettili ideali lanciati dalla medesima posizione, con identica velocità iniziale e diversi angoli rispetto all'orizzontale. In questo contesto il proiettile è un punto materiale: il programma non considera forma, rotazione, dimensioni o caratteristiche costruttive.

All'avvio vengono richiesti la velocità iniziale e i cinque angoli. Premere Invio senza scrivere un valore conferma quello proposto. Il programma calcola le traiettorie, le rappresenta nella stessa area del terminale e stampa i risultati numerici. Alla fine permette di ripetere il confronto mantenendo come valori proposti quelli dell'ultima simulazione.

La visualizzazione è statica: il programma calcola molti punti e stampa il risultato completo. Il ciclo sui punti non è un'animazione e non introduce ritardi temporali reali.

| Parametro | Valore iniziale | Intervallo accettato |
|---|---:|---:|
| Velocità iniziale | 30 m/s | Da 0,1 a 10000 m/s |
| Angoli | 15°, 30°, 45°, 60°, 75° | Da 0,1° a 89,9° |
| Accelerazione di gravità | 9,81 m/s² | Costante nel sorgente |
| Numero di traiettorie | 5 | Costante nel sorgente |

L'intervallo numerico accettato non costituisce una garanzia di realismo fisico: a velocità elevate il modello senza resistenza dell'aria è particolarmente idealizzato.

## 2. C ANSI, ASCII e sequenze ANSI

Sono tre concetti distinti.

**C ANSI/C89** indica la versione del linguaggio usata dal sorgente. Le variabili vengono dichiarate all'inizio dei blocchi e i commenti sono delimitati da `/* ... */`. Non vengono usati commenti `//`, dichiarazioni nelle inizializzazioni dei cicli `for`, array a lunghezza variabile o altre caratteristiche introdotte nelle versioni successive del C.

**ASCII art** indica il disegno mediante caratteri: cifre per le traiettorie, asterischi per le sovrapposizioni, trattini per il terreno e punti per una griglia di riferimento.

**Sequenze ANSI del terminale** indica una convenzione di controllo dell'output: alcune stringhe iniziano con il carattere ESC e vengono interpretate dal terminale come comandi per cambiare colore, pulire lo schermo o spostare il cursore. Il linguaggio C non garantisce che il terminale le interpreti.

Il codice usa solo intestazioni della libreria standard del C. I colori dipendono comunque dall'ambiente di esecuzione; una console di output interna a un IDE può comportarsi diversamente da un terminale. La modalità `--no-color` elimina le sequenze di controllo emesse dal programma.

## 3. Compilazione ed esecuzione

Con GCC e una toolchain già installata:

```bash
gcc -std=c89 -pedantic -Wall -Wextra proiettile.c -lm -o proiettile
./proiettile
```

| Elemento | Significato |
|---|---|
| `gcc` | Compilatore utilizzato |
| `-std=c89` | Seleziona il linguaggio C89 |
| `-pedantic` | Richiede diagnostica per costrutti non conformi allo standard selezionato |
| `-Wall -Wextra` | Attiva numerosi avvisi utili; non equivale a ogni avviso possibile |
| `proiettile.c` | File sorgente |
| `-lm` | Richiede la libreria matematica nelle toolchain che la separano |
| `-o proiettile` | Nome del file eseguibile |

L'ordine `proiettile.c -lm` mantiene la libreria dopo il sorgente che la utilizza, utile per i linker sensibili all'ordine degli argomenti.

Per salvare un output testuale privo di sequenze colore:

```bash
./proiettile --no-color
```

Il programma non riceve la velocità e gli angoli dalla riga di comando: questi dati vengono richiesti tramite input standard. Usare il punto per i decimali, per esempio `25.5`.

È consigliato un terminale largo almeno 100 colonne. L'altezza complessiva dell'output è superiore alle sole 24 righe del grafico, perché comprende intestazioni, scale e tabella.

## 4. Modello fisico e derivazione delle formule

### 4.1 Ipotesi

Il modello assume:

- origine del lancio in `x = 0`, `y = 0`;
- asse X orizzontale, positivo verso destra;
- asse Y verticale, positivo verso l'alto;
- accelerazione orizzontale nulla;
- accelerazione verticale costante e pari a `-G`;
- nessuna resistenza dell'aria;
- arrivo al terreno alla stessa quota della partenza;
- nessun ostacolo o variazione di quota del terreno.

Le distanze sono espresse in metri, i tempi in secondi e le velocità in metri al secondo.

### 4.2 Conversione dell'angolo

L'utente ragiona in gradi, mentre `sin` e `cos` della libreria matematica ricevono radianti:

```c
angle = angles[i] * PI / 180.0;
```

La relazione è `theta_rad = theta_gradi × pi / 180`. Per 45° si ottiene circa 0,785398 radianti. Passare direttamente `45` a `sin` significherebbe chiedere il seno di 45 radianti.

### 4.3 Componenti iniziali della velocità

```c
vx = speed * cos(angle);
vy = speed * sin(angle);
```

Le formule sono:

- `vx0 = v0 × cos(theta)`;
- `vy0 = v0 × sin(theta)`.

`vx` resta costante nel modello. La variabile `vy` del codice conserva la **componente verticale iniziale**, non la velocità verticale istantanea. Quest'ultima sarebbe `vy_istantanea(t) = vy - G × t` e non viene memorizzata nel sorgente.

### 4.4 Leggi orarie

Integrando l'accelerazione con le condizioni iniziali scelte:

```text
x(t) = vx0 × t
y(t) = vy0 × t - (G × t²) / 2
```

Nel codice:

```c
x = vx * t;
y = vy * t - 0.5 * G * t * t;
```

Il prodotto `t * t` calcola il quadrato senza chiamare `pow`. Il coefficiente `0.5` equivale a un mezzo ed è un valore in virgola mobile. Scrivere `1 / 2` in C produrrebbe invece zero, perché entrambi gli operandi sarebbero interi.

### 4.5 Tempo di volo

L'arrivo al terreno soddisfa `y(t) = 0`:

```text
vy0 × t - G × t² / 2 = 0
t × (vy0 - G × t / 2) = 0
```

Le radici sono `t = 0`, istante di partenza, e `T = 2 × vy0 / G`, istante di arrivo:

```c
times[i] = 2.0 * vy / G;
```

Questa formula non si può applicare senza modifiche se la quota iniziale è diversa da quella finale.

### 4.6 Gittata

La distanza orizzontale finale è:

```c
ranges[i] = vx * times[i];
```

Sostituendo le componenti della velocità:

```text
R = v0² × sin(2 × theta) / G
```

A pari velocità e nelle ipotesi elencate, la gittata massima si ottiene a 45°. Angoli complementari, per esempio 30° e 60°, producono la stessa gittata ma tempi di volo e quote massime diversi.

### 4.7 Altezza massima

Il punto più alto si raggiunge quando la velocità verticale istantanea si annulla:

```text
vy0 - G × t_apice = 0
t_apice = vy0 / G = T / 2
```

Sostituendo nella legge oraria:

```c
peaks[i] = vy * vy / (2.0 * G);
```

Quindi `h_max = vy0² / (2 × G)`. L'apice è a metà del tempo di volo e, per questo modello, anche a metà della gittata.

### 4.8 Perché la traiettoria è una parabola

Poiché `vx0 > 0` nell'intervallo degli angoli accettati, si può scrivere `t = x / vx0`. Sostituendo:

```text
y(x) = x × tan(theta) - G × x² / (2 × v0² × cos²(theta))
```

È un polinomio di secondo grado in X con coefficiente quadratico negativo. Il sorgente usa comunque la parametrizzazione temporale, che è naturale per descrivere il moto.

## 5. Organizzazione del programma

| Parte | Responsabilità |
|---|---|
| Direttive `#include` | Rendere disponibili le dichiarazioni delle funzioni di libreria |
| Direttive `#define` | Stabilire dimensioni, costanti fisiche e sequenza di ripristino |
| Array `colors` e `symbols` | Associare colore e carattere alle traiettorie |
| `read_value` | Richiedere un numero, controllarlo e aggiornare il valore del chiamante |
| `draw` | Calcolare risultati, costruire la matrice grafica e stamparla |
| `main` | Gestire configurazione, input, ripetizione e uscita |

`draw` contiene tre fasi concettuali: calcolo fisico, rasterizzazione nella matrice e stampa. Non esiste un archivio permanente delle simulazioni, né una finestra grafica.

## 6. Librerie incluse

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
```

| Intestazione | Identificatori effettivamente usati |
|---|---|
| `stdio.h` | `printf`, `puts`, `fputs`, `putchar`, `fgets`, `getchar`, `fflush`, `feof`, `sprintf`, `stdin`, `stdout`, `EOF` |
| `stdlib.h` | `strtod` |
| `math.h` | `sin`, `cos` |
| `string.h` | `strchr`, `strcmp` |

Un'intestazione fornisce dichiarazioni e definizioni previste dalla libreria; non equivale a copiare nel sorgente l'intera implementazione delle funzioni.

`stdin` è il flusso di input standard; `stdout` quello di output standard. Possono riferirsi al terminale oppure essere reindirizzati a file o pipe.

## 7. Costanti e configurazione

```c
#define W 79
#define H 23
#define N 5
#define PI 3.14159265358979323846
#define G 9.81
#define RESET "\033[0m"
```

`#define` è una direttiva del preprocessore: sostituisce token prima della compilazione e non crea, da sola, una variabile con memoria propria.

### 7.1 Dimensioni del grafico: attenzione agli intervalli

`W` e `H` sono i massimi indici del grafico, non il numero di celle:

```c
int cells[H + 1][W + 1];
```

Con i valori attuali si hanno **24 righe e 80 colonne**, cioè 1920 celle. Gli indici validi sono `row = 0 ... 23` e `col = 0 ... 79`. I cicli usano `<=` proprio per includere gli estremi.

Fra 80 posizioni orizzontali ci sono 79 intervalli; fra 24 posizioni verticali ci sono 23 intervalli. Per questo le scale usano `xmax / W` e `ymax / H`, non `W + 1` e `H + 1`.

### 7.2 Numero di traiettorie

`N` dimensiona gli array dei dati, dei colori e dei simboli. Cambiare soltanto `N` non è sufficiente per estendere correttamente il programma: occorre aggiornare anche gli inizializzatori. Aumentando N, i puntatori ai colori mancanti sarebbero inizializzati a null e non sarebbero validi da passare a `fputs`.

### 7.3 Gravità e pi greco

`G` rappresenta il modulo dell'accelerazione; il segno negativo compare nella formula della quota. `PI` evita di dipendere da costanti come `M_PI`, non richieste da C89. Le cifre del letterale vengono convertite nel formato `double` dell'implementazione: non tutte le cifre scritte sono necessariamente rappresentabili.

## 8. Colori e simboli

```c
static const char *colors[N] = {
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"
};
static const char symbols[N] = {'1', '2', '3', '4', '5'};
```

### 8.1 Significato delle dichiarazioni

`colors` è un array di puntatori a caratteri costanti. Ogni puntatore indica una stringa di controllo. `const char *` impedisce di modificare i caratteri attraverso quel puntatore; non rende necessariamente immutabile il puntatore stesso.

`symbols` è un array di cinque caratteri costanti. `'1'` è un carattere, mentre `"1"` è una stringa contenente il carattere e il terminatore nullo.

Il qualificatore `static` a livello di file attribuisce collegamento interno: questi nomi non vengono esportati come simboli utilizzabili da altre unità di traduzione. Gli oggetti hanno durata statica, quindi esistono per tutta l'esecuzione.

### 8.2 Struttura di una sequenza

La stringa `"\033[91m"` contiene:

1. `\033`: escape ottale per il valore decimale 27, cioè ESC nei terminali ASCII compatibili;
2. `[`: introduzione della sequenza di controllo;
3. `91`: codice del colore rosso brillante nei terminali che lo supportano;
4. `m`: comando relativo agli attributi grafici del testo.

I codici 92, 93, 94 e 95 selezionano rispettivamente verde, giallo, blu e magenta brillanti secondo le comuni convenzioni dei terminali. L'aspetto effettivo dipende dal tema del terminale.

`RESET`, cioè `ESC[0m`, ripristina gli attributi predefiniti; non imposta necessariamente un particolare colore, per esempio bianco.

Le cifre distinguono le curve anche senza colore. Le celle condivise vengono rappresentate da un asterisco senza un colore specifico della singola traiettoria.

## 9. Tipi, puntatori, array e durata delle variabili

### 9.1 Perché usare double

Coordinate, tempi, velocità e angoli sono numeri reali approssimati. `double` offre normalmente una precisione maggiore di `float`, anche se i dettagli del formato dipendono dall'implementazione. Su molte piattaforme correnti è un formato a 64 bit; C89 non impone tale dimensione esatta.

Non bisogna aspettarsi identità algebriche perfette nelle operazioni in virgola mobile: una quota finale teoricamente nulla può diventare un valore negativo molto piccolo.

### 9.2 Perché usare int

Indici, contatori, identificativi e valori logici vengono memorizzati in `int`. In C89 una condizione è falsa quando vale zero e vera quando è diversa da zero. Non è necessario il tipo `bool`, introdotto tramite libreria in una versione successiva del linguaggio.

### 9.3 Passaggio per valore e indirizzo

La velocità viene passata a `draw` come valore:

```c
draw(speed, angles, colored);
```

Una modifica locale al parametro `speed` di `draw` non modificherebbe `speed` di `main`.

Invece `read_value` riceve un indirizzo:

```c
read_value("Velocita iniziale in m/s", &speed, 0.1, 10000.0)
```

`&speed` significa “indirizzo di speed”. Il parametro `double *value` contiene quell'indirizzo; `*value` permette di leggere o scrivere il valore originale. Il C passa comunque per valore anche il puntatore: ciò che viene copiato è l'indirizzo.

### 9.4 Array come parametri

Nel parametro `const double angles[N]`, la dichiarazione viene adattata a un puntatore a `const double`. Non viene copiata l'intera sequenza e N non costituisce una verifica automatica della dimensione dell'array ricevuto. Il programma è corretto perché il chiamante fornisce l'array previsto.

### 9.5 Variabili automatiche

Le variabili locali delle funzioni hanno normalmente durata automatica: nascono entrando nel relativo blocco e cessano di esistere uscendo. I parametri e i buffer locali di `read_value` non conservano i dati dopo il ritorno. I valori persistenti fra simulazioni sono invece le variabili di `main`, che resta attiva durante il ciclo.

## 10. Lettura e validazione dell'input

### 10.1 Contratto della funzione

```c
static int read_value(const char *label, double *value,
                      double minimum, double maximum)
```

| Parametro/ritorno | Significato |
|---|---|
| `label` | Testo della richiesta |
| `value` | Indirizzo del valore proposto, da aggiornare se l'input è valido |
| `minimum` | Limite inferiore incluso |
| `maximum` | Limite superiore incluso |
| Ritorno `1` | Lettura riuscita oppure valore proposto confermato |
| Ritorno `0` | `fgets` non ha fornito una riga: fine input o errore di lettura |

`static` limita l'utilizzo del nome della funzione a questo file sorgente.

### 10.2 Buffer e puntatore finale

```c
char line[128], *end;
double parsed;
int ch;
```

`line` può contenere al massimo 127 caratteri letti più il terminatore `\0`. `end` riceverà la posizione in cui si arresta la conversione numerica. `parsed` contiene il risultato temporaneo. `ch` deve essere `int`, perché `getchar` deve poter rappresentare sia un carattere letto sia il valore speciale `EOF`.

### 10.3 Ripetizione della richiesta

```c
for (;;) {
```

L'assenza delle tre espressioni produce un ciclo senza termine prestabilito. La funzione esce con `return`; per gli input errati usa `continue` e ricomincia dal messaggio iniziale.

```c
printf("%s [%.2f]: ", label, *value);
fflush(stdout);
```

`%s` stampa una stringa; `%.2f` un numero con due cifre dopo il separatore decimale. La richiesta non termina con un a capo. `fflush(stdout)` sollecita l'invio dei dati bufferizzati al dispositivo, così l'utente vede il messaggio prima della lettura. Non viene usato `fflush(stdin)`, che non è una soluzione portabile per svuotare l'input.

### 10.4 Lettura limitata

```c
if (fgets(line, sizeof line, stdin) == NULL) return 0;
```

`sizeof line` misura la dimensione dell'array locale, cioè 128 byte. `fgets` legge al massimo un carattere in meno, aggiunge il terminatore nullo e conserva l'eventuale `\n` letto. Il valore nullo indica che non è stata ottenuta una riga utilizzabile.

### 10.5 Righe troppo lunghe

```c
if (strchr(line, '\n') == NULL && !feof(stdin)) {
    while ((ch = getchar()) != '\n' && ch != EOF) { }
    puts("Riga troppo lunga.");
    continue;
}
```

`strchr` cerca il primo a capo. Se manca e l'indicatore di fine file non è impostato, il codice considera la riga troppo lunga e consuma il resto. Il corpo vuoto del `while` è intenzionale: il lavoro consiste nella chiamata a `getchar` nella condizione.

`&&` usa valutazione a corto circuito: il secondo operando viene valutato soltanto se il primo è vero. `!feof(stdin)` nega il risultato del controllo di fine file.

**Limite preciso:** `feof` segnala una fine file già rilevata, non predice quella futura. Una riga lunga esattamente quanto la capacità utile del buffer può essere rifiutata anche se termina immediatamente dopo. Per un'interfaccia interattiva con numeri brevi è un limite marginale, ma non va confuso con un lettore generale di righe senza limiti.

### 10.6 Conferma con Invio

```c
if (line[0] == '\n') return 1;
```

Solo una riga che inizia direttamente con a capo conferma il valore. Una riga composta da spazi e poi Invio non viene interpretata come conferma: passerà alla conversione e risulterà non valida.

### 10.7 Conversione con strtod

```c
parsed = strtod(line, &end);
```

`strtod` converte la parte iniziale interpretabile come numero e scrive in `end` l'indirizzo del primo carattere non convertito. `&end` è l'indirizzo del puntatore `end`, coerente con il parametro di tipo puntatore a puntatore previsto dalla funzione.

Esempi concettuali:

| Input | Parte convertita | Cosa rimane | Esito nel programma |
|---|---|---|---|
| `30` | `30` | A capo o terminatore | Accettato se nei limiti |
| `30.5` | `30.5` | A capo o terminatore | Accettato se nei limiti |
| `3e1` | `3e1` | A capo o terminatore | Vale 30, accettato |
| `30abc` | `30` | `abc` | Rifiutato |
| `abc` | Nessuna conversione | Tutto l'input | Rifiutato |
| `30,5` | Generalmente `30` nella locale C | `,5` | Rifiutato |

All'avvio di un programma C l'ambiente locale è quello C finché non viene cambiato con `setlocale`; questo sorgente non lo modifica. Perciò viene richiesto il punto decimale.

```c
if (end != line) {
```

La condizione verifica che sia avvenuta una conversione, non che tutta la riga sia corretta. Il controllo successivo è quindi necessario.

### 10.8 Spazi finali e intervallo

```c
while (*end == ' ' || *end == '\t' || *end == '\r') ++end;
```

Il codice ignora spazi, tabulazioni e ritorni carrello dopo il numero. `++end` sposta il puntatore al carattere successivo; non modifica il contenuto della stringa. `||` rappresenta l'OR logico e usa anch'esso il corto circuito.

```c
if ((*end == '\n' || *end == '\0') &&
    parsed >= minimum && parsed <= maximum) {
    *value = parsed;
    return 1;
}
```

La riga deve terminare dopo il numero e gli spazi ammessi. Il valore deve appartenere all'intervallo chiuso. Solo allora viene aggiornato il dato originale del chiamante.

L'uso di `>=` e `<=` significa che 0,1 è accettato sia per la velocità sia per l'angolo; zero viene rifiutato. Il sorgente non controlla esplicitamente `errno` per distinguere overflow e underflow di `strtod`: i limiti ammessi respingono ordinariamente risultati fuori intervallo, ma non producono messaggi specifici per l'errore di conversione numerica.

## 11. Preparazione dei dati fisici e delle scale

### 11.1 Parametri e array di lavoro

```c
static void draw(double speed, const double angles[N], int colored)
```

`void` indica che la funzione non restituisce un valore. L'effetto osservabile è la scrittura su `stdout`.

```c
int cells[H + 1][W + 1];
double ranges[N], peaks[N], times[N];
```

Le tre sequenze numeriche usano lo stesso indice della traiettoria: `ranges[2]`, `peaks[2]`, `times[2]` riguardano tutti l'angolo `angles[2]` e il simbolo `symbols[2]`.

### 11.2 Ricerca dei massimi

`xmax` e `ymax` partono da zero. Nel primo ciclo il programma converte ogni angolo, calcola componenti della velocità, tempo, gittata e apice; poi conserva la gittata maggiore e la quota maggiore.

I limiti degli input garantiscono valori strettamente positivi per le scale nel contesto numerico previsto. Permettere velocità zero o tutti angoli nulli richiederebbe gestire esplicitamente i denominatori nulli nella trasformazione grafica.

### 11.3 Margine visivo

```c
xmax *= 1.05;
ymax *= 1.10;
```

`a *= b` è un'assegnazione composta: per queste variabili equivale a `a = a * b`. Il programma aggiunge il 5% di spazio orizzontale e il 10% verticale, così le curve non toccano necessariamente i bordi superiore e destro.

Gli estremi sono comuni alle cinque curve. Calcolare una scala diversa per ogni curva impedirebbe un confronto diretto delle distanze sullo stesso disegno.

### 11.4 Inizializzazione della matrice

```c
for (row = 0; row <= H; ++row)
    for (col = 0; col <= W; ++col) cells[row][col] = -1;
```

Per ogni riga si visitano tutte le colonne e si imposta lo stato di cella vuota. Senza inizializzazione l'array automatico conterrebbe valori indeterminati, che non si potrebbero usare correttamente come identificativi delle curve.

| Valore della cella | Interpretazione |
|---:|---|
| `-1` | Nessuna traiettoria |
| Da `0` a `N - 1` | Una sola traiettoria identificata dall'indice |
| `N` | Sovrapposizione di almeno due traiettorie |

N funge da sentinella e non è un indice valido per `colors` o `symbols`.

## 12. Trasformazione delle coordinate e rasterizzazione

### 12.1 Campionamento temporale

```c
for (step = 0; step <= 4000; ++step) {
    t = times[i] * (double)step / 4000.0;
```

Si ottengono **4001 campioni** per curva, comprendendo sia la partenza sia l'arrivo. L'intervallo temporale è `T / 4000`. Le curve hanno lo stesso numero di campioni ma non necessariamente lo stesso passo temporale, perché T varia con l'angolo.

Il cast `(double)step` converte il contatore intero. In questa espressione la presenza di `times[i]`, già double, renderebbe comunque reale la moltiplicazione; il cast esplicita l'intenzione. Il divisore `4000.0` è un letterale double.

Non viene eseguita un'integrazione numerica iterativa: ogni posizione viene ricavata direttamente dalle formule analitiche. Un errore a un campione non si accumula come stato iniziale del campione successivo.

### 12.2 Correzione della quota negativa

```c
if (y < 0.0) y = 0.0;
```

Nel tempo di volo ideale la quota non è negativa. Vicino all'atterraggio l'aritmetica in virgola mobile può produrre una piccola quantità negativa: il codice la riporta a zero. Questo controllo non simula un rimbalzo o una collisione articolata con il terreno.

### 12.3 Coordinata orizzontale

```c
col = (int)(x / xmax * W + 0.5);
```

La trasformazione si divide in quattro passaggi:

1. `x / xmax` normalizza la distanza rispetto all'estremo del grafico;
2. la moltiplicazione per W porta il risultato nell'intervallo degli indici;
3. l'aggiunta di 0,5 prepara l'arrotondamento al più vicino per valori non negativi;
4. il cast a `int` elimina la parte frazionaria.

Per `x = 0` si ottiene la colonna 0; per `x = xmax` si otterrebbe la colonna W. Le gittate reali restano prima di tale estremo grazie al margine del 5%.

La tecnica `+ 0.5` non è una regola generale di arrotondamento per numeri negativi. Qui è appropriata perché le coordinate trasformate sono non negative.

### 12.4 Coordinata verticale e inversione

```c
row = H - (int)(y / ymax * H + 0.5);
```

Nel mondo fisico Y cresce verso l'alto; nella matrice stampata le righe crescono verso il basso. La sottrazione da H risolve questa differenza:

| Quota fisica | Indice della riga |
|---|---:|
| `0` | `H`, riga inferiore |
| `ymax` | `0`, riga superiore |

La matrice viene quindi stampata dalla riga superiore a quella inferiore senza invertire l'ordine del ciclo di stampa.

### 12.5 Controllo dei limiti

```c
if (row >= 0 && row <= H && col >= 0 && col <= W) {
```

Il programma accede alla matrice soltanto dopo aver verificato gli indici. In C non esiste un controllo automatico generale dei limiti degli array: un accesso fuori intervallo avrebbe comportamento non definito.

### 12.6 Proprietario della cella e sovrapposizioni

```c
owner = cells[row][col];
if (owner == -1 || owner == i) cells[row][col] = i;
else cells[row][col] = N;
```

I casi sono:

- cella vuota: viene assegnata alla traiettoria corrente;
- cella già della stessa traiettoria: rimane invariata;
- cella di un'altra traiettoria: diventa condivisa;
- cella già condivisa: rimane condivisa, perché N è diverso da ogni indice i valido.

La stessa curva può occupare una cella per molti campioni consecutivi. Questo non produce un asterisco: il controllo `owner == i` distingue la ripetizione della stessa curva dalla sovrapposizione di curve diverse.

Un asterisco non prova un'intersezione geometrica esatta: curve diverse possono semplicemente cadere nella stessa cella a causa della risoluzione limitata. Tutte condividono realmente l'origine; curve con uguale gittata condividono anche il punto finale teorico.

### 12.7 Scale indipendenti

Il rapporto metri/colonna può essere diverso dal rapporto metri/riga. Inoltre un carattere del terminale non è necessariamente quadrato. Il disegno non conserva quindi automaticamente angoli e proporzioni geometriche.

Un lancio di 45° può apparire inizialmente più o meno inclinato sullo schermo: l'angolo fisico resta quello inserito. Per confronti quantitativi bisogna leggere le scale e la tabella.

## 13. Stampa del grafico e della tabella

### 13.1 Pulizia dello schermo

```c
if (colored) printf("\033[2J\033[H");
```

La prima sequenza richiede la cancellazione dell'area visibile; la seconda riporta il cursore alla posizione iniziale. La gestione dello storico di scorrimento dipende dal terminale: non viene garantita la cancellazione dello scrollback.

La variabile `colored` controlla sia i colori sia questa pulizia. Con `--no-color` si conservano le richieste precedenti nell'output, perché non viene emesso il comando di cancellazione.

### 13.2 Etichetta della quota per ogni riga

```c
printf("%9.2f |", ymax * (H - row) / H);
```

`%9.2f` richiede almeno nove posizioni e due cifre decimali. La larghezza è minima, non massima: valori molto grandi possono occupare più spazio.

`ymax` è double, quindi l'intera espressione usa una divisione in virgola mobile anche se H e row sono interi. Alla riga 0 si stampa ymax; alla riga H si stampa zero. È la quota rappresentativa della riga, non la quota esatta di ciascun campione che vi è stato arrotondato.

### 13.3 Cella appartenente a una curva

```c
if (owner >= 0 && owner < N) {
    if (colored) fputs(colors[owner], stdout);
    putchar(symbols[owner]);
    if (colored) fputs(RESET, stdout);
}
```

Il controllo protegge l'accesso agli array di stile. `fputs` scrive una stringa senza aggiungere un a capo. `putchar` scrive un solo carattere. Il ripristino immediato del colore impedisce che gli elementi successivi ereditino il colore della curva.

Questa soluzione è semplice ma emette molte sequenze di controllo, una coppia per ciascuna cella colorata. Si potrebbe ottimizzare conservando il colore corrente durante la stampa.

### 13.4 Cella condivisa

```c
else if (owner == N) {
    putchar('*');
}
```

Il simbolo è deliberatamente neutro: la matrice non conserva l'elenco delle curve presenti, ma soltanto l'informazione che sono almeno due.

### 13.5 Terreno, griglia e spazi

```c
putchar(row == H ? '-' :
        ((row % 5 == 0 && col % 10 == 0) ? '.' : ' '));
```

L'operatore ternario ha forma `condizione ? valore_se_vera : valore_se_falsa`. La logica è:

1. se la riga è l'ultima, stampare `-`;
2. altrimenti, se la riga è multipla di 5 e la colonna multipla di 10, stampare `.`;
3. altrimenti stampare uno spazio.

`%` calcola il resto della divisione intera. La griglia contiene punti alle intersezioni di passi regolari, non linee continue. Poiché questa logica riguarda soltanto le celle vuote, le curve prevalgono sul terreno e sulla griglia.

### 13.6 Asse orizzontale

Dopo il grafico il programma stampa una riga separata con `+`, trattini e `> x [m]`. La quota zero è già la riga inferiore della matrice: la riga successiva serve da cornice e indicatore dell'asse.

Il prefisso delle righe usa nove posizioni numeriche, uno spazio e `|`: la barra verticale si trova dopo dieci caratteri. La cornice usa dieci spazi e poi `+`, allineando quindi il più alla barra verticale, purché il numero della quota rientri nella larghezza minima di nove posizioni. Le celle del grafico e i trattini della cornice iniziano subito dopo. Quote stampate con più di nove caratteri sposterebbero invece l'allineamento.

### 13.7 Tabella finale

```c
printf("   %c     %6.1f gradi  %9.2f m    %9.2f m      %8.3f s",
       symbols[i], angles[i], ranges[i], peaks[i], times[i]);
```

| Specificatore | Interpretazione |
|---|---|
| `%c` | Un carattere |
| `%6.1f` | Numero con almeno sei posizioni e una cifra decimale |
| `%9.2f` | Numero con almeno nove posizioni e due decimali |
| `%8.3f` | Numero con almeno otto posizioni e tre decimali |

La precisione di stampa non cambia la precisione dei calcoli precedenti. Gli angoli sono acquisiti come double ma mostrati con una sola cifra decimale nella tabella: un angolo inserito con più decimali viene calcolato usando il valore acquisito e soltanto visualizzato arrotondato.

## 14. Funzione main e flusso di esecuzione

### 14.1 Parametri del programma

```c
int main(int argc, char *argv[])
```

`argc` è il numero di argomenti disponibili, compreso normalmente il nome del programma; `argv` è l'array delle stringhe degli argomenti.

```c
colored = !(argc > 1 && strcmp(argv[1], "--no-color") == 0);
```

La lettura è:

1. controllare che esista almeno un argomento dopo il nome;
2. confrontare il primo argomento con `--no-color`;
3. se coincide, l'espressione tra parentesi è vera e la negazione produce zero;
4. negli altri casi `colored` vale uno.

`strcmp` restituisce zero quando le stringhe sono uguali. Il corto circuito evita di leggere `argv[1]` quando l'argomento non esiste. Il programma controlla soltanto il primo argomento e non segnala argomenti sconosciuti.

### 14.2 Valori iniziali

```c
double speed = 30.0;
double angles[N] = {15.0, 30.0, 45.0, 60.0, 75.0};
char label[80], line[32];
int i, colored;
```

`label` contiene la richiesta costruita per il singolo angolo. `line` raccoglie la risposta alla domanda finale. Sono buffer diversi da quello locale di `read_value`.

### 14.3 Richiesta della velocità

```c
if (!read_value("Velocita iniziale in m/s", &speed, 0.1, 10000.0)) break;
```

`!` trasforma il ritorno zero in una condizione vera, facendo uscire dal ciclo principale. Un input numerico errato non causa l'uscita, perché viene gestito internamente da `read_value` con una nuova richiesta.

### 14.4 Richiesta degli angoli

```c
for (i = 0; i < N; ++i) {
    sprintf(label, "Angolo traiettoria %d in gradi", i + 1);
    if (!read_value(label, &angles[i], 0.1, 89.9)) return 0;
}
```

`sprintf` costruisce una stringa nel buffer `label`, senza stamparla sul terminale. `%d` converte il numero intero. L'indice interno parte da zero, ma il numero proposto all'utente parte da uno grazie a `i + 1`.

Nel caso attuale il testo ha una lunghezza ben inferiore agli 80 caratteri disponibili. `sprintf` non riceve la dimensione del buffer e non previene in generale un superamento; modificando il formato bisogna controllare di nuovo la capacità. `snprintf` non fa parte del C89 standard, quindi non è una sostituzione neutra rispetto al requisito di versione.

Se finisce l'input durante gli angoli, `return 0` termina subito `main`. Se finisce durante la velocità si usa invece `break` e si raggiunge il `return 0` finale: l'esito esterno è comunque una terminazione con stato di successo.

### 14.5 Disegno e ripetizione

```c
draw(speed, angles, colored);
printf("\nNuova simulazione? [s/N]: ");
fflush(stdout);
if (fgets(line, sizeof line, stdin) == NULL ||
    (line[0] != 's' && line[0] != 'S')) break;
```

La simulazione si ripete se il primo carattere della risposta è `s` oppure `S`. Anche `si` viene quindi accettato. Invio, `n`, spazi iniziali o qualsiasi altro primo carattere fanno uscire.

Il lettore della domanda finale è più semplice di quello numerico: non svuota il resto di una risposta troppo lunga. Se una riga lunga inizia con `s`, i caratteri rimasti possono essere letti alla successiva richiesta numerica. È un limite effettivo migliorabile riutilizzando una routine comune per l'acquisizione di righe.

Le variabili `speed` e `angles` non vengono reinizializzate a ogni giro: i valori dell'ultima simulazione diventano i successivi valori proposti.

### 14.6 Percorso completo

```text
Avvio e valori predefiniti
Richiesta della velocita
Richiesta dei cinque angoli
Calcolo dei risultati fisici
Scelta delle scale comuni
Riempimento della matrice
Stampa del grafico e della tabella
Richiesta di ripetizione
Ritorno alla richiesta della velocita oppure terminazione
```

L'elenco descrive l'ordine delle operazioni; non ci sono thread, processi paralleli o eventi asincroni.

## 15. Esempio numerico completo

### 15.1 Risultati predefiniti

Con velocità 30 m/s e G = 9,81 m/s², la stampa del programma restituisce:

| Simbolo | Angolo | Gittata [m] | Quota massima [m] | Tempo di volo [s] |
|---|---:|---:|---:|---:|
| 1 | 15° | 45,87 | 3,07 | 1,583 |
| 2 | 30° | 79,45 | 11,47 | 3,058 |
| 3 | 45° | 91,74 | 22,94 | 4,325 |
| 4 | 60° | 79,45 | 34,40 | 5,297 |
| 5 | 75° | 45,87 | 42,80 | 5,908 |

I valori sono arrotondati come nell'output. La curva a 45° raggiunge la distanza maggiore; quella a 75° raggiunge la quota maggiore e resta in volo più a lungo.

### 15.2 Calcolo a 45°

Le componenti iniziali sono entrambe circa 21,2132 m/s:

```text
T = 2 × 21,2132 / 9,81 ≈ 4,32481 s
R = 21,2132 × T ≈ 91,74312 m
h_max = 21,2132² / (2 × 9,81) ≈ 22,93578 m
```

All'apice, `t ≈ 2,16241 s`, `x ≈ 45,87156 m`, `y ≈ 22,93578 m`.

### 15.3 Scale ottenute dal confronto

La massima gittata proviene da 45°; la massima quota da 75°. Applicando i margini:

```text
xmax ≈ 91,74312 × 1,05 ≈ 96,33028 m
ymax ≈ 42,79875 × 1,10 ≈ 47,07863 m
Scala X ≈ 96,33028 / 79 ≈ 1,21937 m/colonna
Scala Y ≈ 47,07863 / 23 ≈ 2,04690 m/riga
```

Questi valori spiegano perché una curva bassa, per esempio 15°, occupa poche righe verticali.

### 15.4 Dall'apice alla cella

Per l'apice della curva a 45°:

```text
col = int(45,87156 / 96,33028 × 79 + 0,5) = 38
row = 23 - int(22,93578 / 47,07863 × 23 + 0,5) = 12
```

Il campione occupa dunque `cells[12][38]`. La cella contiene l'identificativo 2, salvo eventuale sovrapposizione con altre traiettorie. L'identificativo 2 seleziona il terzo simbolo, cioè `'3'`.

## 16. Precisione, complessità e limiti

### 16.1 Tre livelli di precisione

Occorre distinguere:

1. **Modello fisico:** trascura fenomeni reali; è il limite principale per descrivere lanci reali.
2. **Calcolo numerico:** usa double e formule analitiche, con arrotondamenti in virgola mobile.
3. **Rappresentazione:** riduce ogni coordinata a una delle 1920 celle disponibili.

Aumentare il numero di campioni non elimina i limiti della matrice. Due quote diverse possono essere indistinguibili sul grafico e risultare differenti nella tabella.

### 16.2 Campionamento e continuità

Con 4001 punti per curva il disegno è fitto per la configurazione attuale, ma il metodo non collega formalmente ogni coppia di celle successive mediante un algoritmo di linea. Con dimensioni o parametri diversi non è una garanzia generale di assenza di buchi. Una rasterizzazione tramite segmenti sarebbe una soluzione più sistematica.

### 16.3 Complessità temporale

Indicando con S il numero di campioni per curva:

- calcolo dei risultati: ordine N;
- azzeramento della matrice: ordine `(H + 1) × (W + 1)`;
- campionamento: ordine `N × S`;
- stampa: ordine del numero di celle più N righe di tabella.

Nel complesso la complessità è `O(N × S + H × W)`. Con i valori attuali vengono valutati 20005 campioni, oltre ai cicli sulla matrice.

### 16.4 Memoria

La matrice occupa `24 × 80 × sizeof(int)` byte. Se `sizeof(int)` vale 4, sono 7680 byte; non è una dimensione imposta dal C89. Gli array `ranges`, `peaks` e `times` occupano complessivamente `15 × sizeof(double)` byte. Non viene usata allocazione dinamica con `malloc`.

### 16.5 Limiti funzionali

Il programma non include animazione, esportazione CSV, salvataggio dei parametri, resize automatico, mouse, attrito, vento, quote iniziali differenti, masse, energia o rimbalzi. Il comando colore non abilita automaticamente le funzionalità ANSI di ogni console possibile. Gli errori di scrittura su stdout non vengono controllati.

### 16.6 Dimensioni costanti e sicurezza delle modifiche

W e H devono restare positivi, perché compaiono come divisori nelle scale. N deve restare coerente con dati iniziali e stili. Dimensioni molto grandi aumentano la memoria automatica e l'output. Le larghezze dei campi di printf non limitano la lunghezza effettiva di numeri molto grandi.

## 17. Verifiche riproducibili

Il sorgente è stato compilato con controlli C89 rigorosi:

```bash
gcc -std=c89 -pedantic-errors -Wall -Wextra -Werror proiettile.c -lm -o proiettile
```

La compilazione senza avvisi verifica la conformità accettata da quella toolchain; non dimostra da sola l'assenza di ogni difetto possibile.

### 17.1 Valori predefiniti

```bash
printf '\n\n\n\n\n\nn\n' | ./proiettile --no-color
```

I primi sei a capo confermano velocità e cinque angoli; `n` termina. Controllare la riga a 45°: gittata 91,74 m, quota 22,94 m e tempo 4,325 s, con punto decimale nell'output reale.

### 17.2 Simmetria delle gittate

Confrontare 30° e 60°, poi 15° e 75°: le gittate devono coincidere entro l'approssimazione numerica. Tempi e quote devono essere differenti.

### 17.3 Validazione

Provare `abc`, `30abc`, `0`, `-5`, `10001` alla richiesta della velocità; devono essere rifiutati. Provare `30.5`, che deve essere accettato. Alla richiesta dell'angolo verificare il rifiuto di 0 e 90.

### 17.4 Ripetizione e sovrapposizioni

Rispondere `s` e confermare i valori: la nuova simulazione mantiene la configurazione. Impostare cinque angoli identici: le curve ricadono nelle stesse celle e la rappresentazione usa asterischi per la sovrapposizione. I dati della tabella restano disponibili per ogni curva.

### 17.5 Proprietà di scala

Raddoppiando la velocità, il modello prevede tempo doppio, gittata quadrupla e quota massima quadrupla. Poiché il grafico si adatta automaticamente ai massimi, la forma in celle può restare sostanzialmente uguale: cambiano le scale e i risultati numerici.

Queste prove sono controlli significativi del modello e dell'interfaccia, non misure sperimentali di un moto reale.

## 18. Modifiche possibili e percorso verso la grafica

### 18.1 Rendere configurabile il campionamento

Una costante `#define STEPS 4000` potrebbe sostituire le occorrenze del numero 4000. Bisognerebbe usarla coerentemente sia nel limite del ciclo sia nel divisore, convertendo il divisore a double. È una proposta, non una modifica applicata al file attuale.

### 18.2 Migliorare il terminale

Si possono separare calcolo e stampa, usare una routine comune per tutte le righe di input e aggiungere una scala X con tacche. Un'animazione richiederebbe un controllo del tempo: C89 da solo non offre una funzione standard di sospensione a millisecondi. L'attesa attiva con cicli vuoti non è un buon riferimento temporale.

### 18.3 Quota iniziale diversa da zero

Con quota iniziale `y0`, la legge diventa `y(t) = y0 + vy0 × t - G × t² / 2`. Per `y0 >= 0` e arrivo a quota zero, la radice non negativa del tempo di arrivo è:

```text
T = (vy0 + sqrt(vy0² + 2 × G × y0)) / G
```

Occorre quindi aggiornare tempo, quota massima, scale, limiti e grafico: aggiungere solo y0 alla formula dei campioni senza aggiornare il tempo di volo sarebbe incoerente.

### 18.4 Finestra grafica con raylib

In una futura versione il modello fisico potrebbe restare separato dalla visualizzazione. La matrice di caratteri verrebbe sostituita da coordinate in pixel; le curve sarebbero disegnate con segmenti e il proiettile con un cerchio. Testi, colori e input sarebbero gestiti dalla libreria grafica.

Per un'animazione, ogni fotogramma mostrerebbe la posizione a un tempo di simulazione aggiornato mediante il tempo trascorso. Non bisognerebbe confondere la frequenza dei fotogrammi con il tempo fisico del volo. La versione attuale non contiene queste funzionalità e non richiede raylib.

## 19. Glossario e sorgente integrale

| Termine | Significato nel programma |
|---|---|
| Gittata | Distanza orizzontale tra partenza e ritorno alla quota del terreno |
| Apice | Punto di quota massima |
| Campione | Una posizione calcolata a un istante scelto |
| Rasterizzazione | Conversione di coordinate continue in celle discrete |
| Buffer | Area di memoria usata per raccogliere caratteri |
| Terminatore nullo | Carattere `\0` che conclude una stringa C |
| Sentinella | Valore speciale che rappresenta uno stato, come N per una cella condivisa |
| Cast | Conversione esplicita di tipo |
| Corto circuito | Valutazione condizionale del secondo operando di `&&` o `||` |
| Unità di traduzione | Sorgente dopo l'elaborazione delle direttive di preprocessing |

Il listato seguente è una copia integrale del sorgente esaminato, senza applicare i miglioramenti proposti nei capitoli precedenti.

```c
/* C ANSI / C89. Grafica ASCII con sequenze di controllo ANSI.
 * Compilazione: gcc -std=c89 -pedantic -Wall -Wextra proiettile.c -lm -o proiettile
 * Terminale consigliato: almeno 100 colonne. Nessuna libreria esterna.
 * Modello: lancio da terra, gravita costante, assenza di attrito.
 * Le scale X e Y sono indipendenti: leggere le coordinate in metri.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define W 79
#define H 23
#define N 5
#define PI 3.14159265358979323846
#define G 9.81
#define RESET "\033[0m"

static const char *colors[N] = {
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"
};
static const char symbols[N] = {'1', '2', '3', '4', '5'};

/* Legge una riga intera; un semplice Invio mantiene il valore proposto. */
static int read_value(const char *label, double *value,
                      double minimum, double maximum)
{
    char line[128], *end;
    double parsed;
    int ch;
    for (;;) {
        printf("%s [%.2f]: ", label, *value);
        fflush(stdout);
        if (fgets(line, sizeof line, stdin) == NULL) return 0;
        if (strchr(line, '\n') == NULL && !feof(stdin)) {
            while ((ch = getchar()) != '\n' && ch != EOF) { }
            puts("Riga troppo lunga.");
            continue;
        }
        if (line[0] == '\n') return 1;
        parsed = strtod(line, &end);
        if (end != line) {
            while (*end == ' ' || *end == '\t' || *end == '\r') ++end;
            if ((*end == '\n' || *end == '\0') &&
                parsed >= minimum && parsed <= maximum) {
                *value = parsed;
                return 1;
            }
        }
        printf("Inserire un numero tra %.2f e %.2f (punto decimale).\n",
               minimum, maximum);
    }
}

static void draw(double speed, const double angles[N], int colored)
{
    int cells[H + 1][W + 1];
    double ranges[N], peaks[N], times[N];
    double xmax, ymax, angle, vx, vy, t, x, y;
    int i, j, row, col, step, owner;

    xmax = 0.0;
    ymax = 0.0;
    for (i = 0; i < N; ++i) {
        angle = angles[i] * PI / 180.0;
        vx = speed * cos(angle);
        vy = speed * sin(angle);
        times[i] = 2.0 * vy / G;
        ranges[i] = vx * times[i];
        peaks[i] = vy * vy / (2.0 * G);
        if (ranges[i] > xmax) xmax = ranges[i];
        if (peaks[i] > ymax) ymax = peaks[i];
    }
    xmax *= 1.05;
    ymax *= 1.10;
    for (row = 0; row <= H; ++row)
        for (col = 0; col <= W; ++col) cells[row][col] = -1;

    for (i = 0; i < N; ++i) {
        angle = angles[i] * PI / 180.0;
        vx = speed * cos(angle);
        vy = speed * sin(angle);
        for (step = 0; step <= 4000; ++step) {
            t = times[i] * (double)step / 4000.0;
            x = vx * t;
            y = vy * t - 0.5 * G * t * t;
            if (y < 0.0) y = 0.0;
            col = (int)(x / xmax * W + 0.5);
            row = H - (int)(y / ymax * H + 0.5);
            if (row >= 0 && row <= H && col >= 0 && col <= W) {
                owner = cells[row][col];
                if (owner == -1 || owner == i) cells[row][col] = i;
                else cells[row][col] = N;
            }
        }
    }

    if (colored) printf("\033[2J\033[H");
    puts("TRAIETTORIE DI UN PROIETTILE - confronto a pari velocita");
    printf("v0 = %.2f m/s | g = %.2f m/s^2 | partenza e arrivo a terra\n", speed, G);
    puts("Quota y [m]");
    for (row = 0; row <= H; ++row) {
        printf("%9.2f |", ymax * (H - row) / H);
        for (col = 0; col <= W; ++col) {
            owner = cells[row][col];
            if (owner >= 0 && owner < N) {
                if (colored) fputs(colors[owner], stdout);
                putchar(symbols[owner]);
                if (colored) fputs(RESET, stdout);
            } else if (owner == N) {
                putchar('*');
            } else {
                putchar(row == H ? '-' :
                        ((row % 5 == 0 && col % 10 == 0) ? '.' : ' '));
            }
        }
        putchar('\n');
    }
    printf("          +");
    for (j = 0; j <= W; ++j) putchar('-');
    printf("> x [m]\n");
    printf("           0     Scala X: %.3f m/colonna; estremo destro: %.2f m\n",
           xmax / W, xmax);
    printf("                 Scala Y: %.3f m/riga (scala diversa da X)\n", ymax / H);
    puts("\nSimbolo   Angolo       Gittata     Quota massima    Tempo di volo");
    for (i = 0; i < N; ++i) {
        if (colored) fputs(colors[i], stdout);
        printf("   %c     %6.1f gradi  %9.2f m    %9.2f m      %8.3f s",
               symbols[i], angles[i], ranges[i], peaks[i], times[i]);
        if (colored) fputs(RESET, stdout);
        putchar('\n');
    }
    puts("* = piu traiettorie nella stessa cella; risoluzione ASCII limitata.");
}

int main(int argc, char *argv[])
{
    double speed = 30.0;
    double angles[N] = {15.0, 30.0, 45.0, 60.0, 75.0};
    char label[80], line[32];
    int i, colored;

    colored = !(argc > 1 && strcmp(argv[1], "--no-color") == 0);
    puts("SIMULATORE BALISTICO - C ANSI (C89)");
    puts("Invio conferma il valore proposto. Usare il punto decimale.");
    puts("Opzione --no-color: disattiva colori e pulizia schermo.");
    for (;;) {
        if (!read_value("Velocita iniziale in m/s", &speed, 0.1, 10000.0)) break;
        for (i = 0; i < N; ++i) {
            sprintf(label, "Angolo traiettoria %d in gradi", i + 1);
            if (!read_value(label, &angles[i], 0.1, 89.9)) return 0;
        }
        draw(speed, angles, colored);
        printf("\nNuova simulazione? [s/N]: ");
        fflush(stdout);
        if (fgets(line, sizeof line, stdin) == NULL ||
            (line[0] != 's' && line[0] != 'S')) break;
    }
    return 0;
}

```
