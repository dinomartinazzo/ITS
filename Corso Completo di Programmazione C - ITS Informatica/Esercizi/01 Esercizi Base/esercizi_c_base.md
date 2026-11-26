# PROGRAMMAZIONE IN C – PRIMO ANNO

## SEZIONE 1 – INPUT / OUTPUT DI BASE

### Esempio 1.1 – Somma di due interi
```c
#include <stdio.h>
int main(void) {
    int a, b;
    printf("Inserisci due interi: ");
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Input non valido.\n");
        return 1;
    }
    printf("Somma = %d\n", a + b);
    return 0;
}
```

### Esempio 1.2 – Media di tre numeri reali
```c
#include <stdio.h>
int main(void) {
    double x, y, z;
    printf("Inserisci tre numeri reali: ");
    if (scanf("%lf %lf %lf", &x, &y, &z) != 3) {
        printf("Input non valido.\n");
        return 1;
    }
    double media = (x + y + z) / 3.0;
    printf("Media = %.3f\n", media);
    return 0;
}
```

### Esercizio 1.3 – Converti minuti in ore e minuti
```c
#include <stdio.h>
int main(void) {
    int minuti;
    printf("Minuti totali: ");
    if (scanf("%d", &minuti) != 1 || minuti < 0) {
        printf("Input non valido.\n");
        return 1;
    }
    int ore = minuti / 60;
    int restanti = minuti % 60;
    printf("%d ore e %d minuti\n", ore, restanti);
    return 0;
}
```

---

## SEZIONE 2 – CONDIZIONALI `if / else`

### Esempio 2.1 – Pari o dispari
```c
#include <stdio.h>
int main(void) {
    int n;
    printf("Inserisci un intero: ");
    if (scanf("%d", &n) != 1) {
        printf("Input non valido.\n");
        return 1;
    }
    if (n % 2 == 0)
        printf("Pari\n");
    else
        printf("Dispari\n");
    return 0;
}
```

### Esempio 2.2 – Massimo di due numeri
```c
#include <stdio.h>
int main(void) {
    int a, b;
    printf("Due interi: ");
    if (scanf("%d %d", &a, &b) != 2) { printf("Input non valido.\n"); return 1; }
    int max = (a > b) ? a : b;
    printf("Massimo = %d\n", max);
    return 0;
}
```

### Esercizio 2.3 – Voto sufficiente o insufficiente
```c
#include <stdio.h>
int main(void) {
    int voto;
    printf("Voto (0-30): ");
    if (scanf("%d", &voto) != 1) { printf("Input non valido.\n"); return 1; }
    if (voto < 0 || voto > 30) {
        printf("Valore fuori intervallo.\n");
        return 1;
    }
    if (voto >= 18) printf("Sufficiente\n");
    else            printf("Insufficiente\n");
    return 0;
}
```

### Esercizio 2.4 – Anno bisestile
```c
#include <stdio.h>
int main(void) {
    int anno;
    printf("Anno: ");
    if (scanf("%d", &anno) != 1) { printf("Input non valido.\n"); return 1; }
    int bis = ( (anno % 4 == 0 && anno % 100 != 0) || (anno % 400 == 0) );
    if (bis) printf("Bisestile\n");
    else     printf("Non bisestile\n");
    return 0;
}
```

---

## SEZIONE 3 – CICLO `while`

### Esempio 3.1 – Conta da 1 a N
```c
#include <stdio.h>
int main(void) {
    int N, i = 1;
    printf("N: ");
    if (scanf("%d", &N) != 1 || N < 1) { printf("Input non valido.\n"); return 1; }
    while (i <= N) {
        printf("%d ", i);
        i++;
    }
    printf("\n");
    return 0;
}
```

### Esempio 3.2 – Somma da 1 a N
```c
#include <stdio.h>
int main(void) {
    int N, i = 1, somma = 0;
    printf("N: ");
    if (scanf("%d", &N) != 1 || N < 0) { printf("Input non valido.\n"); return 1; }
    while (i <= N) {
        somma += i;
        i++;
    }
    printf("Somma = %d\n", somma);
    return 0;
}
```

### Esercizio 3.3 – Fattoriale
```c
#include <stdio.h>
int main(void) {
    int n;
    printf("n (0-12): ");
    if (scanf("%d", &n) != 1 || n < 0 || n > 12) {
        printf("Input non valido (0-12).\n");
        return 1;
    }
    int i = 1;
    long long fatt = 1;
    while (i <= n) {
        fatt *= i;
        i++;
    }
    printf("%d! = %lld\n", n, fatt);
    return 0;
}
```

### Esercizio 3.4 – Validazione input
```c
#include <stdio.h>
int main(void) {
    int x;
    while (1) {
        printf("Inserisci un intero tra 1 e 10: ");
        if (scanf("%d", &x) != 1) {
            printf("Input non valido.\n");
            return 1;
        }
        if (x >= 1 && x <= 10) break;
        printf("Fuori intervallo, riprova.\n");
    }
    printf("Hai inserito: %d\n", x);
    return 0;
}
```

---

## SEZIONE 4 – CICLO `for`

### Esempio 4.1 – Tabellina
```c
#include <stdio.h>
int main(void) {
    int n;
    printf("Numero: ");
    if (scanf("%d", &n) != 1) { printf("Input non valido.\n"); return 1; }
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }
    return 0;
}
```

### Esercizio 4.3 – Somma dei multipli di 3 fino a N
```c
#include <stdio.h>
int main(void) {
    int N;
    printf("N: ");
    if (scanf("%d", &N) != 1 || N < 0) { printf("Input non valido.\n"); return 1; }
    int somma = 0;
    for (int i = 0; i <= N; i += 3) {
        somma += i;
    }
    printf("Somma multipli di 3 = %d\n", somma);
    return 0;
}
```

---

## SEZIONE 5 – OPERATORI LOGICI

### Esempio 5.1 – Controllo intervallo con `&&`
```c
#include <stdio.h>
int main(void) {
    int x;
    printf("Inserisci un numero tra 10 e 20: ");
    scanf("%d", &x);
    if (x >= 10 && x <= 20)
        printf("Nel range.\n");
    else
        printf("Fuori range.\n");
    return 0;
}
```

### Esempio 5.2 – Negazione logica `!`
```c
#include <stdio.h>
int main(void) {
    int n;
    printf("Inserisci un intero non nullo: ");
    scanf("%d", &n);
    if (!n)
        printf("Hai inserito zero.\n");
    else
        printf("Valore valido.\n");
    return 0;
}
```

---

## SEZIONE 6 – SWITCH / CASE

### Esempio 6.1 – Giorno della settimana
```c
#include <stdio.h>
int main(void) {
    int g;
    printf("Numero giorno (1-7): ");
    if (scanf("%d", &g) != 1) return 1;
    switch (g) {
        case 1: printf("Lunedi\n"); break;
        case 2: printf("Martedi\n"); break;
        case 3: printf("Mercoledi\n"); break;
        case 4: printf("Giovedi\n"); break;
        case 5: printf("Venerdi\n"); break;
        case 6: printf("Sabato\n"); break;
        case 7: printf("Domenica\n"); break;
        default: printf("Valore non valido.\n"); break;
    }
    return 0;
}
```

### Esercizio 6.2 – Menu con scelte numeriche
```c
#include <stdio.h>
int main(void) {
    int scelta;
    printf("1) Somma\n2) Differenza\n3) Prodotto\nScelta: ");
    if (scanf("%d", &scelta) != 1) return 1;
    int a, b;
    printf("Due numeri: ");
    scanf("%d %d", &a, &b);
    switch (scelta) {
        case 1: printf("%d\n", a + b); break;
        case 2: printf("%d\n", a - b); break;
        case 3: printf("%d\n", a * b); break;
        default: printf("Scelta errata.\n"); break;
    }
    return 0;
}
```

---

## SEZIONE 7 – FUNZIONI

### Esempio 7.1 – Funzione somma
```c
#include <stdio.h>
int somma(int a, int b) {
    return a + b;
}
int main(void) {
    int x, y;
    printf("Inserisci due numeri: ");
    scanf("%d %d", &x, &y);
    printf("Somma = %d\n", somma(x, y));
    return 0;
}
```

### Esempio 7.2 – Funzione che verifica pari/dispari
```c
#include <stdio.h>
int pari(int n) {
    return (n % 2 == 0);
}
int main(void) {
    int n;
    printf("Numero: ");
    scanf("%d", &n);
    if (pari(n)) printf("Pari\n");
    else printf("Dispari\n");
    return 0;
}
```

### Esercizio 7.3 – Funzione fattoriale
```c
#include <stdio.h>
long long fattoriale(int n) {
    long long f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    return f;
}
int main(void) {
    int n;
    printf("n: ");
    scanf("%d", &n);
    printf("%d! = %lld\n", n, fattoriale(n));
    return 0;
}
```

---

## Suggerimenti finali
- Scrivere sempre l’intestazione `#include <stdio.h>`.
- Controllare sempre il valore restituito da `scanf`.
- Testare tutti i casi limite (0, numeri negativi, input errati).
- Inserire commenti chiari e coerenti.
- Salvare i file con estensione `.c` e compilarli con GCC o Clang.

