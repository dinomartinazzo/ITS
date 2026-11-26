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
