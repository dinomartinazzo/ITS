# PROGRAMMAZIONE IN C – ESERCIZI DI MATEMATICA DI BASE

## SEZIONE 1 – OPERAZIONI ARITMETICHE

### Esercizio 1.1 – Quadrato e cubo di un numero
Scrivere un programma che legge un numero intero e ne calcola quadrato e cubo.
```c
#include <stdio.h>
int main(void) {
    int n;
    printf("Numero intero: ");
    scanf("%d", &n);
    int q = n * n;
    int c = n * n * n;
    printf("Quadrato = %d, Cubo = %d\n", q, c);
    return 0;
}
```

### Esercizio 1.2 – Area e perimetro di un rettangolo
```c
#include <stdio.h>
int main(void) {
    double base, altezza;
    printf("Base e altezza: ");
    scanf("%lf %lf", &base, &altezza);
    double area = base * altezza;
    double perimetro = 2 * (base + altezza);
    printf("Area = %.2f, Perimetro = %.2f\n", area, perimetro);
    return 0;
}
```

### Esercizio 1.3 – Conversione gradi Celsius in Fahrenheit
```c
#include <stdio.h>
int main(void) {
    double C;
    printf("Gradi Celsius: ");
    scanf("%lf", &C);
    double F = (C * 9.0 / 5.0) + 32.0;
    printf("Fahrenheit = %.2f\n", F);
    return 0;
}
```

---

## SEZIONE 2 – CICLI CON CALCOLI

### Esercizio 2.1 – Somma dei primi N numeri pari
```c
#include <stdio.h>
int main(void) {
    int N, somma = 0;
    printf("N: ");
    scanf("%d", &N);
    for (int i = 2; i <= N * 2; i += 2) {
        somma += i;
    }
    printf("Somma dei primi %d numeri pari = %d\n", N, somma);
    return 0;
}
```

### Esercizio 2.2 – Tabella dei quadrati
```c
#include <stdio.h>
int main(void) {
    int N;
    printf("N: ");
    scanf("%d", &N);
    for (int i = 1; i <= N; i++) {
        printf("%d^2 = %d\n", i, i * i);
    }
    return 0;
}
```

### Esercizio 2.3 – Somma dei numeri divisibili per 5 tra 1 e 100
```c
#include <stdio.h>
int main(void) {
    int somma = 0;
    for (int i = 1; i <= 100; i++) {
        if (i % 5 == 0) somma += i;
    }
    printf("Somma = %d\n", somma);
    return 0;
}
```

---

## SEZIONE 3 – FORMULE GEOMETRICHE

### Esercizio 3.1 – Circonferenza e area del cerchio
```c
#include <stdio.h>
#define PI 3.141592653589793
int main(void) {
    double r;
    printf("Raggio: ");
    scanf("%lf", &r);
    double circ = 2 * PI * r;
    double area = PI * r * r;
    printf("Circonferenza = %.3f, Area = %.3f\n", circ, area);
    return 0;
}
```

### Esercizio 3.2 – Teorema di Pitagora
```c
#include <stdio.h>
#include <math.h>
int main(void) {
    double a, b;
    printf("Cateti a e b: ");
    scanf("%lf %lf", &a, &b);
    double c = sqrt(a*a + b*b);
    printf("Ipotenusa = %.3f\n", c);
    return 0;
}
```

### Esercizio 3.3 – Distanza tra due punti nel piano
```c
#include <stdio.h>
#include <math.h>
int main(void) {
    double x1, y1, x2, y2;
    printf("Punto1 (x1 y1): ");
    scanf("%lf %lf", &x1, &y1);
    printf("Punto2 (x2 y2): ");
    scanf("%lf %lf", &x2, &y2);
    double dx = x2 - x1;
    double dy = y2 - y1;
    double dist = sqrt(dx*dx + dy*dy);
    printf("Distanza = %.3f\n", dist);
    return 0;
}
```

---

## SEZIONE 4 – PICCOLI PROBLEMI DI MATEMATICA APPLICATA

### Esercizio 4.1 – Interessi semplici
```c
#include <stdio.h>
int main(void) {
    double capitale, tasso, anni;
    printf("Capitale, tasso%%, anni: ");
    scanf("%lf %lf %lf", &capitale, &tasso, &anni);
    double interesse = capitale * tasso / 100.0 * anni;
    double montante = capitale + interesse;
    printf("Interesse = %.2f, Montante = %.2f\n", interesse, montante);
    return 0;
}
```

### Esercizio 4.2 – Serie aritmetica
Calcolare la somma di una serie aritmetica di `N` termini, con primo termine `a1` e differenza `d`.
```c
#include <stdio.h>
int main(void) {
    double a1, d;
    int N;
    printf("Primo termine, differenza, N: ");
    scanf("%lf %lf %d", &a1, &d, &N);
    double somma = N * (2 * a1 + (N - 1) * d) / 2.0;
    printf("Somma serie = %.3f\n", somma);
    return 0;
}
```

### Esercizio 4.3 – Conversione da radianti a gradi
```c
#include <stdio.h>
#define PI 3.141592653589793
int main(void) {
    double rad;
    printf("Radianti: ");
    scanf("%lf", &rad);
    double gradi = rad * 180.0 / PI;
    printf("Gradi = %.2f\n", gradi);
    return 0;
}
```

---

## SEZIONE 5 – FUNZIONI MATEMATICHE

### Esempio 5.1 – Calcolo del minimo comune multiplo (MCM)
```c
#include <stdio.h>
int mcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}
int main(void) {
    int a, b;
    printf("Due numeri: ");
    scanf("%d %d", &a, &b);
    int MCM = (a * b) / mcd(a, b);
    printf("MCM = %d\n", MCM);
    return 0;
}
```

### Esempio 5.2 – Funzione potenza intera positiva
```c
#include <stdio.h>
long long potenza(int base, int esp) {
    long long p = 1;
    for (int i = 0; i < esp; i++) p *= base;
    return p;
}
int main(void) {
    int b, e;
    printf("Base ed esponente: ");
    scanf("%d %d", &b, &e);
    printf("%d^%d = %lld\n", b, e, potenza(b, e));
    return 0;
}
```

### Esercizio 5.3 – Equazione lineare ax + b = 0
```c
#include <stdio.h>
int main(void) {
    double a, b;
    printf("Coefficienti a e b: ");
    scanf("%lf %lf", &a, &b);
    if (a == 0) {
        if (b == 0) printf("Infiniti risultati.\n");
        else printf("Nessuna soluzione.\n");
    } else {
        double x = -b / a;
        printf("Soluzione: x = %.3f\n", x);
    }
    return 0;
}
```

---

## Suggerimenti
- Usare `math.h` per funzioni come `sqrt`, `pow`, `sin`, `cos`.
- Dichiarare costanti come `#define PI 3.14159` quando servono.
- Testare input negativi e casi limite.
- Organizzare il codice in funzioni per esercizi più lunghi.

