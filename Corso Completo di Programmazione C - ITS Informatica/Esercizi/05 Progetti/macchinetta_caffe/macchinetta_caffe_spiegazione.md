# Macchinetta del caffè in C: spiegazione del codice

Guida al file `macchinetta_caffe.c`, pensata per chi ha appena iniziato a programmare in C. Il programma simula un distributore di bevande calde: mostra un menu, accetta monete, calcola il resto e "prepara" la bevanda.

## 1. Cosa imparerai

| Argomento | Dove compare nel programma |
|---|---|
| Macchina a stati finiti | ciclo principale in `main` |
| `enum` | elenco degli stati |
| `switch` e fall-through | scelta dello stato, del menu, della moneta |
| `do-while` | ciclo dell'automa, pulizia dell'input |
| `for` | stampa del menu, calcolo del resto, preparazione |
| `if` / `else` | controlli sì/no (credito sufficiente, annullamento) |
| Array e costanti | listino bevande e tagli delle monete |
| Funzioni | suddivisione del programma in compiti |
| Divisione intera e resto (`/` e `%`) | stampa in euro, calcolo del resto |

## 2. L'idea: la macchina a stati finiti

Una macchinetta vera si trova sempre in una situazione ben precisa: aspetta una scelta, oppure aspetta monete, oppure sta dando il resto, oppure sta preparando la bevanda. Ognuna di queste situazioni si chiama **stato**. Il passaggio da uno stato all'altro si chiama **transizione** e avviene quando succede qualcosa (un **evento**): l'utente sceglie, inserisce una moneta, annulla.

Una macchina a stati finiti è quindi descritta da tre cose: l'elenco degli stati, lo stato di partenza, la tabella delle transizioni.

```
            scelta 1-4                credito >= prezzo
 SELEZIONE ------------> INSERIMENTO -------------------> RESTO ------> PREPARAZIONE
   ^  |  ^                 |   ^   |        0 (annulla)     ^  |              |
   |  |  |                 |___|   |________________________|  |              |
   |  |  |             moneta, credito                         |              |
   |  |  |             ancora insufficiente                    |              |
   |  |  |_____________________________________________________|              |
   |  |                  dopo il rimborso (annullamento)                      |
   |  |_______ scelta 0 ______> SPENTA                                        |
   |__________________________________________________________________________|
                               bevanda pronta
```

| Stato attuale | Evento | Stato successivo |
|---|---|---|
| SELEZIONE | scelta da 1 a 4 | INSERIMENTO |
| SELEZIONE | scelta 0 | SPENTA |
| SELEZIONE | qualsiasi altro valore | SELEZIONE |
| INSERIMENTO | moneta valida, credito ancora insufficiente | INSERIMENTO |
| INSERIMENTO | credito maggiore o uguale al prezzo | RESTO |
| INSERIMENTO | 0 (annulla) | RESTO |
| RESTO | acquisto regolare | PREPARAZIONE |
| RESTO | acquisto annullato | SELEZIONE |
| PREPARAZIONE | bevanda pronta | SELEZIONE |

Il vantaggio di questo modo di ragionare: il programma non è un groviglio di condizioni, ma una tabella. Per ogni stato basta chiedersi "cosa faccio qui?" e "dove vado dopo?".

## 3. Struttura del file

Il file è diviso in quattro zone, separate da commenti.

| Zona | Contenuto | Perché è separata |
|---|---|---|
| Configurazione | costanti, listino, tagli, elenco degli stati | per cambiare prezzi o bevande senza toccare la logica |
| Ingresso / uscita | `leggi_intero`, `stampa_euro`, `stampa_menu` | tutto ciò che riguarda tastiera e schermo |
| Logica | `eroga_resto`, `prepara_bevanda` | i calcoli veri e propri |
| Programma principale | `main` | il ciclo dell'automa |

## 4. Le librerie

```c
#include <stdio.h>
#include <stdlib.h>
```

`stdio.h` fornisce `printf` (scrivere a schermo), `scanf` (leggere da tastiera) e `getchar` (leggere un singolo carattere). `stdlib.h` fornisce `exit`, che termina subito il programma.

## 5. La configurazione

### 5.1 Costanti con `#define`

```c
#define NUM_BEVANDE         4
#define NUM_TAGLI           6
#define PASSI_PREPARAZIONE  5
```

`#define` assegna un nome a un valore. Prima della compilazione, ogni `NUM_BEVANDE` nel testo viene sostituito con `4`. Scrivere il nome al posto del numero ha due vantaggi: il codice si legge meglio, e per cambiare il valore basta modificare una sola riga.

### 5.2 Gli array del listino

```c
const char *NOMI_BEVANDE[NUM_BEVANDE]   = { "Caffe'", "Cappuccino", "Te'", "Cioccolata" };
const int   PREZZI_BEVANDE[NUM_BEVANDE] = { 60, 90, 75, 110 };
```

Un **array** è una fila di valori dello stesso tipo, numerati a partire da **0**. I due array sono "paralleli": la posizione 0 contiene nome e prezzo del caffè, la posizione 1 quelli del cappuccino, e così via.

| Indice | `NOMI_BEVANDE` | `PREZZI_BEVANDE` |
|---|---|---|
| 0 | Caffe' | 60 |
| 1 | Cappuccino | 90 |
| 2 | Te' | 75 |
| 3 | Cioccolata | 110 |

`const` significa che i valori non possono essere modificati durante l'esecuzione. `const char *` è il modo in cui il C indica una stringa di testo fissa.

Gli apostrofi in `Caffe'` e `Te'` sostituiscono le lettere accentate, che su alcuni terminali verrebbero mostrate male.

### 5.3 Perché i prezzi sono in centesimi

I prezzi sono scritti come `60` e non come `0.60`. Il motivo: i numeri con la virgola (`float`, `double`) nel computer sono approssimati. Il valore 0.10 non è rappresentabile in modo esatto, e sommando più volte piccoli importi si accumulano errori: un confronto come "credito uguale a prezzo" può fallire anche quando i conti a mano tornano. Con i centesimi interi i calcoli sono sempre esatti. È la regola generale per il denaro nei programmi.

### 5.4 I tagli delle monete

```c
const int TAGLI_MONETE[NUM_TAGLI] = { 200, 100, 50, 20, 10, 5 };
```

Sono le monete da 2 €, 1 €, 50 c, 20 c, 10 c, 5 c, in centesimi. L'ordine **decrescente** è importante: serve al calcolo del resto (capitolo 7.1).

### 5.5 L'elenco degli stati con `enum`

```c
typedef enum {
    SELEZIONE,
    INSERIMENTO,
    RESTO,
    PREPARAZIONE,
    SPENTA
} Stato;
```

`enum` crea un elenco di nomi. Dietro le quinte il compilatore assegna a ogni nome un numero (SELEZIONE vale 0, INSERIMENTO vale 1, ...), ma nel codice si usano solo i nomi. Confronta:

```c
stato = 2;        /* cosa vuol dire 2? */
stato = RESTO;    /* chiaro */
```

`typedef ... Stato;` dà un nome al nuovo tipo, così si può dichiarare una variabile scrivendo `Stato stato;`.

## 6. Le funzioni di ingresso e uscita

Una **funzione** è un blocco di codice con un nome, che svolge un compito preciso. Si scrive una volta e si richiama quando serve.

### 6.1 `leggi_intero`: leggere un numero in modo sicuro

```c
int leggi_intero(void)
{
    int valore = -1;
    int c;
    int letti;

    letti = scanf("%d", &valore);
    if (letti == EOF) {
        printf("\nIngresso terminato.\n");
        exit(0);
    }
    if (letti != 1) {
        valore = -1;
    }

    do {
        c = getchar();
    } while (c != '\n' && c != EOF);

    return valore;
}
```

La prima riga, `int leggi_intero(void)`, dice che la funzione restituisce un numero intero (`int`) e non riceve nulla in ingresso (`void`).

`scanf("%d", &valore)` prova a leggere un intero e a metterlo nella variabile `valore`. La `&` indica a `scanf` *dove* si trova la variabile, in modo che possa scriverci dentro. Poco noto ma fondamentale: `scanf` restituisce a sua volta un numero, che dice com'è andata la lettura.

| Valore restituito da `scanf` | Significato | Cosa fa il programma |
|---|---|---|
| 1 | ha letto un intero | usa il valore letto |
| 0 | l'utente ha scritto qualcosa che non è un numero (es. `abc`) | imposta `valore` a -1 |
| `EOF` | l'ingresso è stato chiuso (es. Ctrl+D su Linux, Ctrl+Z su Windows) | termina il programma con `exit(0)` |

Il valore -1 è una convenzione scelta da noi: significa "input non valido". Funziona perché -1 non è né una voce del menu né una moneta, quindi finirà sempre nel ramo "non valido" degli `switch`.

Il ciclo finale risolve un problema classico. Se l'utente scrive `abc` e preme Invio, `scanf` non riesce a leggere e **lascia quei caratteri in attesa**. Alla lettura successiva li ritroverebbe e fallirebbe di nuovo, all'infinito. Il `do-while` legge e butta via un carattere alla volta finché incontra il fine riga (`'\n'`):

```c
do {
    c = getchar();
} while (c != '\n' && c != EOF);
```

Il `do-while` esegue il corpo **almeno una volta** e controlla la condizione **dopo**. Qui è la scelta giusta perché prima bisogna leggere un carattere, e solo dopo ha senso controllarlo. La variabile `c` è di tipo `int` e non `char` perché `getchar` può restituire anche il valore speciale `EOF`, che non è un carattere.

### 6.2 `stampa_euro`: da centesimi a euro

```c
void stampa_euro(int centesimi)
{
    printf("%d.%02d EUR", centesimi / 100, centesimi % 100);
}
```

`void` davanti al nome significa che la funzione non restituisce nulla: si limita a stampare. Riceve un parametro, `centesimi`.

Con i numeri interi, `/` è la **divisione intera** (scarta la parte decimale) e `%` è il **resto** della divisione.

| `centesimi` | `centesimi / 100` | `centesimi % 100` | Stampa |
|---|---|---|---|
| 110 | 1 | 10 | 1.10 EUR |
| 60 | 0 | 60 | 0.60 EUR |
| 205 | 2 | 5 | 2.05 EUR |

Nel formato `%02d`, il `2` chiede almeno due cifre e lo `0` chiede di riempire con zeri. Senza, 205 centesimi verrebbero stampati come `2.5` invece di `2.05`.

### 6.3 `stampa_menu`: il primo `for`

```c
for (i = 0; i < NUM_BEVANDE; i++) {
    printf(" %d) %-12s ", i + 1, NOMI_BEVANDE[i]);
    stampa_euro(PREZZI_BEVANDE[i]);
    printf("\n");
}
```

Il `for` ha tre parti tra parentesi, separate da punto e virgola.

| Parte | Codice | Quando viene eseguita |
|---|---|---|
| Inizializzazione | `i = 0` | una volta sola, all'inizio |
| Condizione | `i < NUM_BEVANDE` | prima di ogni giro; se è falsa il ciclo finisce |
| Incremento | `i++` | alla fine di ogni giro |

Quindi `i` assume i valori 0, 1, 2, 3 e a ogni giro viene stampata una riga del menu. Si stampa `i + 1` perché gli array partono da 0, ma per l'utente è più naturale un menu che parte da 1. `%-12s` stampa una stringa occupando sempre 12 caratteri, allineata a sinistra: così i prezzi risultano incolonnati.

Il `for` si usa quando si sa in anticipo quante volte ripetere: qui, una volta per ogni bevanda.

## 7. Le funzioni di logica

### 7.1 `eroga_resto`: il calcolo del resto

```c
void eroga_resto(int importo)
{
    int i;
    int quante;

    if (importo == 0) {
        printf("Nessun resto da erogare.\n");
    } else {
        printf("Resto: ");
        stampa_euro(importo);
        printf("\n");
        for (i = 0; i < NUM_TAGLI; i++) {
            quante  = importo / TAGLI_MONETE[i];
            importo = importo % TAGLI_MONETE[i];
            if (quante > 0) {
                printf("  %d x ", quante);
                stampa_euro(TAGLI_MONETE[i]);
                printf("\n");
            }
        }
    }
}
```

L'`if / else` sceglie tra due strade: se l'importo è zero stampa un messaggio, altrimenti calcola le monete. Attenzione: il confronto si scrive con **due** uguali (`==`). Un solo `=` è un'assegnazione, ed è uno degli errori più comuni.

Il metodo usato è quello che applica chiunque dia un resto a mano: si parte dalla moneta più grande, se ne usano quante ne stanno nell'importo, e si passa alla successiva con ciò che rimane. Per ogni taglio:

- `importo / TAGLI_MONETE[i]` dice quante monete di quel taglio servono;
- `importo % TAGLI_MONETE[i]` dice quanto resta ancora da dare.

Esempio con un resto di 160 centesimi:

| Giro (`i`) | Taglio | `quante` = importo / taglio | Nuovo `importo` = importo % taglio | Stampa |
|---|---|---|---|---|
| 0 | 200 | 160 / 200 = 0 | 160 | nulla |
| 1 | 100 | 160 / 100 = 1 | 60 | 1 x 1.00 EUR |
| 2 | 50 | 60 / 50 = 1 | 10 | 1 x 0.50 EUR |
| 3 | 20 | 10 / 20 = 0 | 10 | nulla |
| 4 | 10 | 10 / 10 = 1 | 0 | 1 x 0.10 EUR |
| 5 | 5 | 0 / 5 = 0 | 0 | nulla |

L'`if (quante > 0)` evita di stampare righe inutili come "0 x 2.00 EUR". Con i tagli dell'euro questo metodo dà sempre il numero minimo di monete; per questo l'array deve essere in ordine decrescente.

### 7.2 `prepara_bevanda`

```c
for (passo = 1; passo <= PASSI_PREPARAZIONE; passo++) {
    printf("  [%d/%d] %d%%\n", passo, PASSI_PREPARAZIONE,
           passo * 100 / PASSI_PREPARAZIONE);
}
```

Un `for` che conta da 1 a 5 e stampa l'avanzamento. La percentuale è `passo * 100 / 5`: si moltiplica **prima** di dividere, perché con gli interi `passo / 5` darebbe 0 per i primi quattro passi. Per stampare il simbolo `%` dentro `printf` si scrive `%%`.

## 8. Il programma principale

### 8.1 Le variabili

| Variabile | Tipo | A cosa serve |
|---|---|---|
| `stato` | `Stato` | stato attuale dell'automa; parte da `SELEZIONE` |
| `bevanda` | `int` | indice (0-3) della bevanda scelta |
| `credito` | `int` | centesimi inseriti finora |
| `annullato` | `int` | 1 se l'utente ha annullato, 0 altrimenti |
| `scelta` | `int` | numero digitato nel menu |
| `moneta` | `int` | valore digitato come moneta |
| `resto` | `int` | importo da restituire |

Le prime quattro sono la **memoria** della macchina: conservano le informazioni tra un giro del ciclo e il successivo. `annullato` è una variabile "bandierina" (in inglese *flag*): in C il valore 0 significa falso e qualsiasi valore diverso da 0 significa vero.

### 8.2 Lo scheletro dell'automa

```c
do {
    switch (stato) {
        case SELEZIONE:    /* ... */ break;
        case INSERIMENTO:  /* ... */ break;
        case RESTO:        /* ... */ break;
        case PREPARAZIONE: /* ... */ break;
        default:           stato = SPENTA;
    }
} while (stato != SPENTA);
```

Questo è il cuore del programma. A ogni giro del `do-while`:

1. lo `switch` guarda il valore di `stato` e salta al `case` corrispondente;
2. il codice di quel `case` fa il suo lavoro e, se serve, cambia `stato`;
3. `break` fa uscire dallo `switch`;
4. il `while` controlla: se lo stato non è `SPENTA`, si ricomincia.

Lo stato `SPENTA` non ha un `case` proprio: appena `stato` diventa `SPENTA` il ciclo termina, quindi lo `switch` non viene più eseguito. Il `default` (il ramo "in tutti gli altri casi") è una protezione in più.

### 8.3 Stato SELEZIONE

```c
case SELEZIONE:
    stampa_menu();
    scelta = leggi_intero();
    switch (scelta) {
        case 0:
            stato = SPENTA;
            break;
        case 1:
        case 2:
        case 3:
        case 4:
            bevanda   = scelta - 1;
            credito   = 0;
            annullato = 0;
            stato     = INSERIMENTO;
            break;
        default:
            printf("Scelta non valida.\n");
    }
    break;
```

Qui c'è uno `switch` dentro un altro `switch`: quello esterno sceglie in base allo stato, quello interno in base al numero digitato.

**Il fall-through.** I `case 1:`, `case 2:`, `case 3:` sono vuoti di proposito. In C, quando lo `switch` salta a un `case`, l'esecuzione prosegue verso il basso **finché non incontra un `break`**. Se l'utente digita 2, il programma salta a `case 2:`, non trova istruzioni, scivola su `case 3:`, poi su `case 4:`, ed esegue il blocco comune. È il modo standard per dire "per 1, 2, 3 oppure 4 fai la stessa cosa".

La stessa regola spiega perché dimenticare un `break` è un errore grave: il programma proseguirebbe nel `case` successivo senza volerlo.

Nel blocco comune, `bevanda = scelta - 1` converte il numero del menu (1-4) nell'indice dell'array (0-3). `credito` e `annullato` vengono azzerati perché inizia un nuovo acquisto.

Nel ramo `default` lo stato non viene modificato: al giro successivo si è ancora in `SELEZIONE` e il menu viene ristampato.

### 8.4 Stato INSERIMENTO

```c
case INSERIMENTO:
    /* ... stampa prezzo e credito ... */
    moneta = leggi_intero();
    switch (moneta) {
        case 5:
        case 10:
        case 20:
        case 50:
        case 100:
        case 200:
            credito += moneta;
            break;
        case 0:
            annullato = 1;
            printf("Acquisto annullato.\n");
            break;
        default:
            printf("Moneta non accettata.\n");
    }
    if (annullato || credito >= PREZZI_BEVANDE[bevanda]) {
        stato = RESTO;
    }
    break;
```

Di nuovo il fall-through: tutte e sei le monete valide eseguono la stessa istruzione. `credito += moneta` è la forma breve di `credito = credito + moneta`.

Un valore come 3 o 25 finisce nel `default`: la moneta viene rifiutata e il credito non cambia.

L'`if` finale decide la transizione. `||` significa "oppure": si passa allo stato RESTO se l'utente ha annullato **oppure** se il credito ha raggiunto il prezzo. Se nessuna delle due condizioni è vera, `stato` non cambia, e al giro successivo la macchina chiede un'altra moneta. È così che un solo stato gestisce un numero qualsiasi di monete, senza un ciclo dedicato: il ciclo è quello esterno dell'automa.

### 8.5 Stato RESTO

```c
case RESTO:
    if (annullato) {
        resto = credito;
        stato = SELEZIONE;
    } else {
        resto = credito - PREZZI_BEVANDE[bevanda];
        stato = PREPARAZIONE;
    }
    eroga_resto(resto);
    credito = 0;
    break;
```

Due casi. Se l'acquisto è stato annullato, si restituisce tutto il credito e si torna al menu senza preparare nulla. Altrimenti si restituisce la differenza tra credito e prezzo e si passa alla preparazione. `if (annullato)` equivale a `if (annullato != 0)`.

In entrambi i casi il credito viene poi azzerato: i soldi sono stati usati o restituiti.

### 8.6 Stato PREPARAZIONE

```c
case PREPARAZIONE:
    prepara_bevanda(NOMI_BEVANDE[bevanda]);
    stato = SELEZIONE;
    break;
```

Chiama la funzione di preparazione passandole il nome della bevanda scelta, poi torna al menu: la macchina è pronta per il cliente successivo.

## 9. Un acquisto seguito passo per passo

Cappuccino (0.90 €) pagato con 50 c e poi 2 €.

| Giro | Stato all'inizio | Input | Cosa succede | `credito` | Stato alla fine |
|---|---|---|---|---|---|
| 1 | SELEZIONE | `2` | `bevanda = 1`, credito azzerato | 0 | INSERIMENTO |
| 2 | INSERIMENTO | `50` | moneta valida; 50 < 90 | 50 | INSERIMENTO |
| 3 | INSERIMENTO | `200` | moneta valida; 250 >= 90 | 250 | RESTO |
| 4 | RESTO | nessuno | `resto = 250 - 90 = 160`; eroga 1 €, 50 c, 10 c | 0 | PREPARAZIONE |
| 5 | PREPARAZIONE | nessuno | stampa l'avanzamento | 0 | SELEZIONE |

Nota che i giri 4 e 5 non chiedono nulla all'utente: non tutti gli stati aspettano un input.

## 10. Compilare ed eseguire

```
gcc -std=c99 -Wall -Wextra -o macchinetta macchinetta_caffe.c
./macchinetta
```

`-Wall -Wextra` attivano gli avvisi del compilatore: conviene usarli sempre, perché segnalano molti errori di distrazione. Su Windows il programma si avvia con `macchinetta.exe`.

Prove consigliate:

| Sequenza di input | Risultato atteso |
|---|---|
| `1`, `50`, `10` | "Nessun resto da erogare", poi caffè pronto |
| `2`, `50`, `200` | resto 1.60 EUR = 1 x 1.00 + 1 x 0.50 + 1 x 0.10, poi cappuccino pronto |
| `1`, `20`, `0` | "Acquisto annullato", rimborso 1 x 0.20 EUR, ritorno al menu |
| `2`, `3` | "Moneta non accettata", credito invariato |
| `9` oppure `abc` (nel menu) | "Scelta non valida", menu ristampato |
| `0` (nel menu) | "Macchina spenta" |

## 11. Errori tipici da evitare

| Errore | Conseguenza |
|---|---|
| Dimenticare `break` alla fine di un `case` | l'esecuzione prosegue nel `case` successivo |
| Scrivere `=` al posto di `==` in un `if` | assegnazione invece di confronto; la condizione dà risultati sbagliati |
| Dimenticare `&` in `scanf("%d", &valore)` | comportamento imprevedibile, spesso il programma si blocca |
| Usare `float` per il denaro | errori di arrotondamento nei confronti |
| Usare l'indice 4 su un array di 4 elementi | lettura fuori dall'array: gli indici validi sono 0-3 |
| Scrivere `passo / 5 * 100` con gli interi | risultato 0 per i primi passi: prima si moltiplica, poi si divide |

## 12. Esercizi

1. **Nuova bevanda.** Aggiungi il "Latte macchiato" a 0.80 €. Devi modificare tre punti: `NUM_BEVANDE`, i due array, i `case` dello stato SELEZIONE.
2. **Messaggio di cortesia.** Nello stato INSERIMENTO stampa anche quanto manca per raggiungere il prezzo.
3. **Zucchero.** Aggiungi uno stato `ZUCCHERO` tra SELEZIONE e INSERIMENTO, in cui l'utente sceglie un livello da 0 a 3. Aggiorna prima la tabella delle transizioni, poi il codice.
4. **Contatore vendite.** Conta le bevande erogate e stampa il totale e l'incasso allo spegnimento.
5. **Scorta di monete (difficile).** Dai alla macchina una quantità limitata di monete per ogni taglio, con un array `SCORTA_MONETE`. Se il resto non è erogabile, la macchina deve rifiutare l'acquisto e rimborsare.
