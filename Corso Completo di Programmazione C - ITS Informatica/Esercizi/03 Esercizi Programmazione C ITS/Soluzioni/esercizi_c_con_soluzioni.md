# Esercizi introduttivi di programmazione in C per ITS
## Con soluzioni "metodo semplice"

Di seguito gli stessi 50 esercizi con una possibile soluzione in C, usando solo costrutti di base (variabili, `if`, `switch`, cicli, array, funzioni semplici). Le soluzioni sono volutamente lineari e non ottimizzate, adatte a un corso introduttivo.

---
## 1. Basi di input/output e variabili

### Esercizio 1
Stampare la frase "Benvenuto nel corso ITS di Programmazione in C".

```c
#include <stdio.h>

int main(void) {
    printf("Benvenuto nel corso ITS di Programmazione in C\n");
    return 0;
}
```

---
### Esercizio 2
Chiedere all’utente il suo nome e stampare "Ciao, <nome>!".

```c
#include <stdio.h>

int main(void) {
    char nome[50];

    printf("Inserisci il tuo nome: ");
    scanf("%49s", nome);   /* semplice: legge una parola */

    printf("Ciao, %s!\n", nome);
    return 0;
}
```

---
### Esercizio 3
Leggere due numeri interi e stampare la loro somma.

```c
#include <stdio.h>

int main(void) {
    int a, b, somma;

    printf("Inserisci due interi: ");
    scanf("%d %d", &a, &b);

    somma = a + b;
    printf("Somma = %d\n", somma);
    return 0;
}
```

---
### Esercizio 4
Leggere due numeri interi e stampare somma, differenza, prodotto e quoziente intero.

```c
#include <stdio.h>

int main(void) {
    int a, b;

    printf("Inserisci due interi: ");
    scanf("%d %d", &a, &b);

    printf("Somma = %d\n", a + b);
    printf("Differenza = %d\n", a - b);
    printf("Prodotto = %d\n", a * b);

    if (b != 0) {
        printf("Quoziente intero = %d\n", a / b);
    } else {
        printf("Divisione per zero non consentita.\n");
    }

    return 0;
}
```

---
### Esercizio 5
Dato un numero intero, determinare se è positivo, negativo o zero.

```c
#include <stdio.h>

int main(void) {
    int n;

    printf("Inserisci un intero: ");
    scanf("%d", &n);

    if (n > 0) {
        printf("Positivo\n");
    } else if (n < 0) {
        printf("Negativo\n");
    } else {
        printf("Zero\n");
    }

    return 0;
}
```

---
## 2. Condizioni

### Esercizio 6
Stabilire se un numero è pari o dispari.

```c
#include <stdio.h>

int main(void) {
    int n;

    printf("Inserisci un intero: ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Pari\n");
    } else {
        printf("Dispari\n");
    }

    return 0;
}
```

---
### Esercizio 7
Leggere tre numeri e stampare il maggiore.

```c
#include <stdio.h>

int main(void) {
    int a, b, c, max;

    printf("Inserisci tre interi: ");
    scanf("%d %d %d", &a, &b, &c);

    max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    printf("Il maggiore e': %d\n", max);
    return 0;
}
```

---
### Esercizio 8
Determinare se un anno è bisestile.

```c
#include <stdio.h>

int main(void) {
    int anno;

    printf("Inserisci un anno: ");
    scanf("%d", &anno);

    if ((anno % 4 == 0 && anno % 100 != 0) || (anno % 400 == 0)) {
        printf("Anno bisestile\n");
    } else {
        printf("Anno non bisestile\n");
    }

    return 0;
}
```

---
### Esercizio 9
Implementare un menu con 3 opzioni: somma, sottrazione, uscita.

```c
#include <stdio.h>

int main(void) {
    int scelta;
    int a, b;

    do {
        printf("1) Somma\n");
        printf("2) Sottrazione\n");
        printf("3) Uscita\n");
        printf("Scelta: ");
        scanf("%d", &scelta);

        if (scelta == 1 || scelta == 2) {
            printf("Inserisci due interi: ");
            scanf("%d %d", &a, &b);
        }

        switch (scelta) {
            case 1:
                printf("Somma = %d\n", a + b);
                break;
            case 2:
                printf("Differenza = %d\n", a - b);
                break;
            case 3:
                printf("Uscita...\n");
                break;
            default:
                printf("Scelta non valida.\n");
        }
    } while (scelta != 3);

    return 0;
}
```

---
### Esercizio 10
Assegnare una valutazione a un voto da 0 a 100.

```c
#include <stdio.h>

int main(void) {
    int voto;

    printf("Inserisci un voto (0-100): ");
    scanf("%d", &voto);

    if (voto < 0 || voto > 100) {
        printf("Voto non valido\n");
    } else if (voto >= 90) {
        printf("Eccellente\n");
    } else if (voto >= 75) {
        printf("Buono\n");
    } else if (voto >= 60) {
        printf("Sufficiente\n");
    } else {
        printf("Insufficiente\n");
    }

    return 0;
}
```

---
## 3. Cicli

### Esercizio 11
Stampare i numeri da 1 a 100.

```c
#include <stdio.h>

int main(void) {
    int i;
    for (i = 1; i <= 100; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

---
### Esercizio 12
Calcolare la somma dei primi N naturali.

```c
#include <stdio.h>

int main(void) {
    int N, i;
    int somma = 0;

    printf("Inserisci N: ");
    scanf("%d", &N);

    for (i = 1; i <= N; i++) {
        somma += i;
    }

    printf("Somma = %d\n", somma);
    return 0;
}
```

---
### Esercizio 13
Stampare la tabellina di un numero scelto.

```c
#include <stdio.h>

int main(void) {
    int n, i;

    printf("Inserisci un intero: ");
    scanf("%d", &n);

    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }

    return 0;
}
```

---
### Esercizio 14
Dato un numero, stampare i suoi divisori.

```c
#include <stdio.h>

int main(void) {
    int n, i;

    printf("Inserisci un intero: ");
    scanf("%d", &n);

    printf("Divisori di %d:\n", n);
    for (i = 1; i <= n; i++) {
        if (n % i == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
```

---
### Esercizio 15
Chiedere numeri finché l’utente inserisce 0; stampare il totale.

```c
#include <stdio.h>

int main(void) {
    int n;
    int somma = 0;

    do {
        printf("Inserisci un intero (0 per terminare): ");
        scanf("%d", &n);
        somma += n;
    } while (n != 0);

    printf("Somma totale = %d\n", somma);
    return 0;
}
```

---
## 4. Array

Per gli esercizi con array, usiamo dimensioni fisse semplici.

### Esercizio 16
Leggere 10 interi in array e calcolare la somma.

```c
#include <stdio.h>

int main(void) {
    int v[10];
    int i, somma = 0;

    for (i = 0; i < 10; i++) {
        printf("Inserisci elemento %d: ", i + 1);
        scanf("%d", &v[i]);
        somma += v[i];
    }

    printf("Somma = %d\n", somma);
    return 0;
}
```

---
### Esercizio 17
Leggere 5 interi e trovare il massimo.

```c
#include <stdio.h>

int main(void) {
    int v[5];
    int i, max;

    for (i = 0; i < 5; i++) {
        printf("Inserisci elemento %d: ", i + 1);
        scanf("%d", &v[i]);
    }

    max = v[0];
    for (i = 1; i < 5; i++) {
        if (v[i] > max) {
            max = v[i];
        }
    }

    printf("Massimo = %d\n", max);
    return 0;
}
```

---
### Esercizio 18
Contare numeri pari e dispari in un array di 10 elementi.

```c
#include <stdio.h>

int main(void) {
    int v[10];
    int i, c_pari = 0, c_dispari = 0;

    for (i = 0; i < 10; i++) {
        printf("Inserisci elemento %d: ", i + 1);
        scanf("%d", &v[i]);
        if (v[i] % 2 == 0) {
            c_pari++;
        } else {
            c_dispari++;
        }
    }

    printf("Pari: %d, Dispari: %d\n", c_pari, c_dispari);
    return 0;
}
```

---
### Esercizio 19
Stampare un array di 8 valori in ordine inverso.

```c
#include <stdio.h>

int main(void) {
    int v[8];
    int i;

    for (i = 0; i < 8; i++) {
        printf("Inserisci elemento %d: ", i + 1);
        scanf("%d", &v[i]);
    }

    printf("Array in ordine inverso:\n");
    for (i = 7; i >= 0; i--) {
        printf("%d\n", v[i]);
    }

    return 0;
}
```

---
### Esercizio 20
Calcolare la media di N valori (max 100).

```c
#include <stdio.h>

int main(void) {
    int N, i;
    int v[100];
    int somma = 0;
    double media;

    printf("Quanti valori (max 100)? ");
    scanf("%d", &N);

    if (N < 1 || N > 100) {
        printf("N non valido\n");
        return 1;
    }

    for (i = 0; i < N; i++) {
        printf("Valore %d: ", i + 1);
        scanf("%d", &v[i]);
        somma += v[i];
    }

    media = (double)somma / N;
    printf("Media = %.2f\n", media);
    return 0;
}
```

---
## 5. Funzioni

Per gli esercizi 21–25 mostriamo solo le funzioni e un `main` di esempio.

### Esercizio 21
Funzione `somma(a, b)`.

```c
#include <stdio.h>

int somma(int a, int b) {
    return a + b;
}

int main(void) {
    int x = 3, y = 5;
    printf("Somma = %d\n", somma(x, y));
    return 0;
}
```

---
### Esercizio 22
Funzione che calcola il fattoriale (iterativo).

```c
#include <stdio.h>

long fattoriale(int n) {
    long f = 1;
    int i;
    for (i = 1; i <= n; i++) {
        f *= i;
    }
    return f;
}

int main(void) {
    int n;
    printf("Inserisci n (>=0): ");
    scanf("%d", &n);
    printf("%d! = %ld\n", n, fattoriale(n));
    return 0;
}
```

---
### Esercizio 23
Funzione per trovare il massimo in un array.

```c
#include <stdio.h>

int massimo(int a[], int n) {
    int i, max = a[0];
    for (i = 1; i < n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;
}

int main(void) {
    int v[5] = {3, 7, 1, 9, 4};
    printf("Massimo = %d\n", massimo(v, 5));
    return 0;
}
```

---
### Esercizio 24
Funzione per invertire gli elementi di un array.

```c
#include <stdio.h>

void inverti(int a[], int n) {
    int i, temp;
    for (i = 0; i < n / 2; i++) {
        temp = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = temp;
    }
}

int main(void) {
    int v[5] = {1, 2, 3, 4, 5};
    int i;

    inverti(v, 5);

    for (i = 0; i < 5; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
    return 0;
}
```

---
### Esercizio 25
Funzione che verifica se un numero è primo.

```c
#include <stdio.h>
#include <stdbool.h>

bool is_primo(int n) {
    int i;
    if (n <= 1) return false;
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(void) {
    int n;
    printf("Inserisci un intero: ");
    scanf("%d", &n);

    if (is_primo(n)) {
        printf("Primo\n");
    } else {
        printf("Non primo\n");
    }
    return 0;
}
```

---
## 6. Stringhe

### Esercizio 26
Leggere una stringa e calcolarne la lunghezza senza usare `strlen`.

```c
#include <stdio.h>

int main(void) {
    char s[100];
    int i = 0;

    printf("Inserisci una parola: ");
    scanf("%99s", s);

    while (s[i] != '\0') {
        i++;
    }

    printf("Lunghezza = %d\n", i);
    return 0;
}
```

---
### Esercizio 27
Verificare se una stringa è palindroma (senza spazi, minuscole).

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    char s[100];
    int i = 0, j;
    bool pal = true;

    printf("Inserisci una parola (minuscole, senza spazi): ");
    scanf("%99s", s);

    while (s[i] != '\0') {
        i++;
    }
    j = i - 1;

    for (i = 0; i < j; i++, j--) {
        if (s[i] != s[j]) {
            pal = false;
            break;
        }
    }

    if (pal) printf("Palindroma\n");
    else     printf("Non palindroma\n");

    return 0;
}
```

---
### Esercizio 28
Contare le vocali presenti in una stringa.

```c
#include <stdio.h>

int main(void) {
    char s[100];
    int i = 0, count = 0;
    char c;

    printf("Inserisci una parola: ");
    scanf("%99s", s);

    while ((c = s[i]) != '\0') {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            count++;
        }
        i++;
    }

    printf("Numero di vocali = %d\n", count);
    return 0;
}
```

---
### Esercizio 29
Copiare una stringa in un'altra senza `strcpy`.

```c
#include <stdio.h>

int main(void) {
    char src[100], dst[100];
    int i = 0;

    printf("Inserisci una parola: ");
    scanf("%99s", src);

    while (src[i] != '\0') {
        dst[i] = src[i];
        i++;
    }
    dst[i] = '\0';

    printf("Copia: %s\n", dst);
    return 0;
}
```

---
### Esercizio 30
Concatenare due stringhe manualmente in una terza.

```c
#include <stdio.h>

int main(void) {
    char s1[50], s2[50], s3[100];
    int i = 0, j = 0;

    printf("Prima parola: ");
    scanf("%49s", s1);
    printf("Seconda parola: ");
    scanf("%49s", s2);

    while (s1[i] != '\0') {
        s3[i] = s1[i];
        i++;
    }
    while (s2[j] != '\0') {
        s3[i] = s2[j];
        i++; j++;
    }
    s3[i] = '\0';

    printf("Concatenazione: %s\n", s3);
    return 0;
}
```

---
## 7. Strutture

### Esercizio 31
Struttura `Studente` con 3 voti e calcolo media.

```c
#include <stdio.h>

struct Studente {
    char nome[50];
    char cognome[50];
    int voti[3];
};

int main(void) {
    struct Studente s;
    int i;
    int somma = 0;
    double media;

    printf("Nome: ");
    scanf("%49s", s.nome);
    printf("Cognome: ");
    scanf("%49s", s.cognome);

    for (i = 0; i < 3; i++) {
        printf("Voto %d: ", i + 1);
        scanf("%d", &s.voti[i]);
        somma += s.voti[i];
    }

    media = (double)somma / 3;
    printf("Studente %s %s, media = %.2f\n", s.nome, s.cognome, media);
    return 0;
}
```

---
### Esercizio 32
Array di 5 studenti; stampare lo studente con media più alta.

```c
#include <stdio.h>

struct Studente {
    char nome[50];
    char cognome[50];
    int voti[3];
};

int main(void) {
    struct Studente s[5];
    int i, j;
    double media, max_media = -1.0;
    int idx_max = 0;

    for (i = 0; i < 5; i++) {
        int somma = 0;
        printf("Studente %d\n", i + 1);
        printf("Nome: ");
        scanf("%49s", s[i].nome);
        printf("Cognome: ");
        scanf("%49s", s[i].cognome);

        for (j = 0; j < 3; j++) {
            printf("Voto %d: ", j + 1);
            scanf("%d", &s[i].voti[j]);
            somma += s[i].voti[j];
        }

        media = (double)somma / 3;
        if (media > max_media) {
            max_media = media;
            idx_max = i;
        }
    }

    printf("Migliore: %s %s con media %.2f\n",
           s[idx_max].nome, s[idx_max].cognome, max_media);
    return 0;
}
```

---
### Esercizio 33
Struttura `Punto` e funzione distanza tra due punti.

```c
#include <stdio.h>
#include <math.h>

struct Punto {
    double x;
    double y;
};

double distanza(struct Punto a, struct Punto b) {
    double dx = a.x - b.x;
    double dy = a.y - b.y;
    return sqrt(dx * dx + dy * dy);
}

int main(void) {
    struct Punto p1, p2;

    printf("Punto 1 (x y): ");
    scanf("%lf %lf", &p1.x, &p1.y);
    printf("Punto 2 (x y): ");
    scanf("%lf %lf", &p2.x, &p2.y);

    printf("Distanza = %.2f\n", distanza(p1, p2));
    return 0;
}
```

---
### Esercizio 34
Struttura `Rettangolo` con funzioni area e perimetro.

```c
#include <stdio.h>

struct Rettangolo {
    double base;
    double altezza;
};

double area(struct Rettangolo r) {
    return r.base * r.altezza;
}

double perimetro(struct Rettangolo r) {
    return 2 * (r.base + r.altezza);
}

int main(void) {
    struct Rettangolo r;

    printf("Base: ");
    scanf("%lf", &r.base);
    printf("Altezza: ");
    scanf("%lf", &r.altezza);

    printf("Area = %.2f\n", area(r));
    printf("Perimetro = %.2f\n", perimetro(r));
    return 0;
}
```

---
### Esercizio 35
Rubrica con 3 contatti (nome e telefono).

```c
#include <stdio.h>

struct Contatto {
    char nome[50];
    char telefono[20];
};

int main(void) {
    struct Contatto rubrica[3];
    int i;

    for (i = 0; i < 3; i++) {
        printf("Contatto %d\n", i + 1);
        printf("Nome: ");
        scanf("%49s", rubrica[i].nome);
        printf("Telefono: ");
        scanf("%19s", rubrica[i].telefono);
    }

    printf("\nRubrica:\n");
    for (i = 0; i < 3; i++) {
        printf("%s - %s\n", rubrica[i].nome, rubrica[i].telefono);
    }

    return 0;
}
```

---
## 8. File

Per semplicità, usiamo file di testo e controlli minimi sugli errori.

### Esercizio 36
Scrivere un file con il testo "ITS Programmazione C".

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("messaggio.txt", "w");
    if (f == NULL) {
        printf("Errore apertura file\n");
        return 1;
    }
    fprintf(f, "ITS Programmazione C\n");
    fclose(f);
    return 0;
}
```

---
### Esercizio 37
Leggere un file di testo e stamparlo.

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("messaggio.txt", "r");
    int c;

    if (f == NULL) {
        printf("Errore apertura file\n");
        return 1;
    }

    while ((c = fgetc(f)) != EOF) {
        putchar(c);
    }

    fclose(f);
    return 0;
}
```

---
### Esercizio 38
Scrivere 5 numeri in un file e rileggerli per calcolare la media.

```c
#include <stdio.h>

int main(void) {
    FILE *f;
    int i, x;
    int somma = 0;
    double media;

    f = fopen("numeri.txt", "w");
    if (f == NULL) {
        printf("Errore apertura file\n");
        return 1;
    }

    for (i = 0; i < 5; i++) {
        printf("Inserisci numero %d: ", i + 1);
        scanf("%d", &x);
        fprintf(f, "%d\n", x);
    }
    fclose(f);

    f = fopen("numeri.txt", "r");
    if (f == NULL) {
        printf("Errore riapertura file\n");
        return 1;
    }

    somma = 0;
    i = 0;
    while (fscanf(f, "%d", &x) == 1) {
        somma += x;
        i++;
    }
    fclose(f);

    if (i > 0) {
        media = (double)somma / i;
        printf("Media = %.2f\n", media);
    } else {
        printf("Nessun numero letto\n");
    }

    return 0;
}
```

---
### Esercizio 39
Salvare una struttura `Studente` in formato testo.

```c
#include <stdio.h>

struct Studente {
    char nome[50];
    char cognome[50];
    int eta;
};

int main(void) {
    struct Studente s;
    FILE *f;

    printf("Nome: ");
    scanf("%49s", s.nome);
    printf("Cognome: ");
    scanf("%49s", s.cognome);
    printf("Eta: ");
    scanf("%d", &s.eta);

    f = fopen("studente.txt", "w");
    if (f == NULL) {
        printf("Errore apertura file\n");
        return 1;
    }

    fprintf(f, "%s %s %d\n", s.nome, s.cognome, s.eta);
    fclose(f);

    return 0;
}
```

---
### Esercizio 40
Creare un file di log con data e ora a ogni esecuzione (versione semplice senza time.h dettagliata per studenti: si scrive solo un numero progressivo).

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("log.txt", "a");
    if (f == NULL) {
        printf("Errore apertura file\n");
        return 1;
    }

    fprintf(f, "Esecuzione del programma\n");
    fclose(f);
    return 0;
}
```

(Estensione possibile: usare `time.h` per data/ora reali.)

---
## 9. Problemi matematici

### Esercizio 41
Calcolare area del cerchio dato il raggio.

```c
#include <stdio.h>

int main(void) {
    double r, area;
    const double PI = 3.141592653589793;

    printf("Raggio: ");
    scanf("%lf", &r);

    area = PI * r * r;
    printf("Area = %.2f\n", area);
    return 0;
}
```

---
### Esercizio 42
Calcolare MCM di due numeri (metodo semplice via MCD).

```c
#include <stdio.h>

int mcd(int a, int b) {
    int r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main(void) {
    int a, b, g, mcm;

    printf("Inserisci due interi: ");
    scanf("%d %d", &a, &b);

    g = mcd(a, b);
    mcm = (a / g) * b;

    printf("MCM = %d\n", mcm);
    return 0;
}
```

---
### Esercizio 43
Calcolare MCD (Euclide).

```c
#include <stdio.h>

int mcd(int a, int b) {
    int r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main(void) {
    int a, b;

    printf("Inserisci due interi: ");
    scanf("%d %d", &a, &b);

    printf("MCD = %d\n", mcd(a, b));
    return 0;
}
```

---
### Esercizio 44
Generare i primi N numeri di Fibonacci.

```c
#include <stdio.h>

int main(void) {
    int N, i;
    int a = 0, b = 1, c;

    printf("Quanti numeri di Fibonacci? ");
    scanf("%d", &N);

    if (N <= 0) return 0;

    if (N >= 1) printf("%d ", a);
    if (N >= 2) printf("%d ", b);

    for (i = 3; i <= N; i++) {
        c = a + b;
        printf("%d ", c);
        a = b;
        b = c;
    }
    printf("\n");
    return 0;
}
```

---
### Esercizio 45
Verificare se un numero è perfetto.

```c
#include <stdio.h>

int main(void) {
    int n, i, somma = 0;

    printf("Inserisci un intero: ");
    scanf("%d", &n);

    for (i = 1; i < n; i++) {
        if (n % i == 0) {
            somma += i;
        }
    }

    if (somma == n) {
        printf("Numero perfetto\n");
    } else {
        printf("Non perfetto\n");
    }

    return 0;
}
```

---
## 10. Mini progetti

### Esercizio 46
Gioco "Indovina il numero" (versione con numero fisso per semplicità).

```c
#include <stdio.h>

int main(void) {
    int segreto = 42;  /* per ora fisso */
    int tentativo;

    do {
        printf("Indovina il numero: ");
        scanf("%d", &tentativo);

        if (tentativo < segreto) {
            printf("Troppo piccolo\n");
        } else if (tentativo > segreto) {
            printf("Troppo grande\n");
        } else {
            printf("Bravo, hai indovinato!\n");
        }
    } while (tentativo != segreto);

    return 0;
}
```

---
### Esercizio 47
Simulazione bancomat con saldo, deposito, prelievo.

```c
#include <stdio.h>

int main(void) {
    int scelta;
    double saldo = 0.0, importo;

    do {
        printf("1) Deposito\n");
        printf("2) Prelievo\n");
        printf("3) Mostra saldo\n");
        printf("4) Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);

        switch (scelta) {
            case 1:
                printf("Importo deposito: ");
                scanf("%lf", &importo);
                saldo += importo;
                break;
            case 2:
                printf("Importo prelievo: ");
                scanf("%lf", &importo);
                if (importo <= saldo) {
                    saldo -= importo;
                } else {
                    printf("Fondi insufficienti\n");
                }
                break;
            case 3:
                printf("Saldo = %.2f\n", saldo);
                break;
            case 4:
                printf("Fine operazioni\n");
                break;
            default:
                printf("Scelta non valida\n");
        }
    } while (scelta != 4);

    return 0;
}
```

---
### Esercizio 48
Mini-calcolatrice con funzioni separate.

```c
#include <stdio.h>

int somma(int a, int b) { return a + b; }
int diff(int a, int b)  { return a - b; }
int prod(int a, int b)  { return a * b; }
int quot(int a, int b)  { return b != 0 ? a / b : 0; }

int main(void) {
    int scelta, a, b;

    do {
        printf("1) Somma\n2) Differenza\n3) Prodotto\n4) Quoziente\n5) Esci\nScelta: ");
        scanf("%d", &scelta);

        if (scelta >= 1 && scelta <= 4) {
            printf("Inserisci due interi: ");
            scanf("%d %d", &a, &b);
        }

        switch (scelta) {
            case 1: printf("Risultato = %d\n", somma(a, b)); break;
            case 2: printf("Risultato = %d\n", diff(a, b));  break;
            case 3: printf("Risultato = %d\n", prod(a, b));  break;
            case 4:
                if (b != 0) printf("Risultato = %d\n", quot(a, b));
                else        printf("Divisione per zero\n");
                break;
            case 5: printf("Uscita\n"); break;
            default: printf("Scelta non valida\n");
        }
    } while (scelta != 5);

    return 0;
}
```

---
### Esercizio 49
Sistema votazione studenti con minimo, massimo, media.

```c
#include <stdio.h>

int main(void) {
    int n, i, voto;
    int somma = 0;
    int min, max;

    printf("Quanti voti? ");
    scanf("%d", &n);

    if (n <= 0) return 0;

    printf("Voto 1: ");
    scanf("%d", &voto);
    somma = voto;
    min = max = voto;

    for (i = 2; i <= n; i++) {
        printf("Voto %d: ", i);
        scanf("%d", &voto);
        somma += voto;
        if (voto < min) min = voto;
        if (voto > max) max = voto;
    }

    printf("Media = %.2f\n", (double)somma / n);
    printf("Minimo = %d, Massimo = %d\n", min, max);
    return 0;
}
```

---
### Esercizio 50
Lista della spesa con menu testuale (versione molto semplice, max 10 elementi).

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char elenco[10][50];
    int count = 0;
    int scelta, i;

    do {
        printf("1) Aggiungi elemento\n");
        printf("2) Mostra lista\n");
        printf("3) Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);

        if (scelta == 1) {
            if (count < 10) {
                printf("Elemento: ");
                scanf("%49s", elenco[count]);
                count++;
            } else {
                printf("Lista piena\n");
            }
        } else if (scelta == 2) {
            printf("Lista della spesa:\n");
            for (i = 0; i < count; i++) {
                printf("- %s\n", elenco[i]);
            }
        } else if (scelta == 3) {
            printf("Fine programma\n");
        } else {
            printf("Scelta non valida\n");
        }
    } while (scelta != 3);

    return 0;
}
```

