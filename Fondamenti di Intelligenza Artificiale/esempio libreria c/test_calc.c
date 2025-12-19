/*
 * FILE: test_calc.c
 * SCOPO: Programma principale che USA la libreria calculator
 *
 * Questo file contiene il main() che testa le funzioni
 * della nostra libreria calculator
 */

#include <stdio.h>
#include "calculator.h"  /* Includo l'header della mia libreria */

int main(void) {
    printf("=== ESEMPIO SEMPLICE: LIBRERIA CALCULATOR ===\n\n");

    /* TEST 1: Somma */
    int risultato1 = somma(5, 3);
    printf("5 + 3 = %d\n", risultato1);

    /* TEST 2: Sottrazione */
    int risultato2 = sottrazione(10, 4);
    printf("10 - 4 = %d\n", risultato2);

    /* TEST 3: Moltiplicazione */
    int risultato3 = moltiplica(6, 7);
    printf("6 * 7 = %d\n", risultato3);

    /* TEST 4: Divisione */
    int risultato4 = dividi(20, 5);
    printf("20 / 5 = %d\n", risultato4);

    /* TEST 5: Divisione per zero */
    printf("\n--- Test divisione per zero ---\n");
    int risultato5 = dividi(10, 0);
    printf("10 / 0 = %d (ritorna 0 per indicare errore)\n", risultato5);

    printf("\n=== FINE TEST ===\n");

    return 0;
}
