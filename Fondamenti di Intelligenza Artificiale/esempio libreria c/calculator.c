/*
 * FILE: calculator.c
 * SCOPO: Implementazione della libreria calculator
 *
 * Questo file contiene il CODICE VERO delle funzioni
 * Qui c'è la logica che fa funzionare le operazioni
 */

#include "calculator.h"

/* Implementazione della somma */
int somma(int a, int b) {
    return a + b;
}

/* Implementazione della sottrazione */
int sottrazione(int a, int b) {
    return a - b;
}

/* Implementazione della moltiplicazione */
int moltiplica(int a, int b) {
    return a * b;
}

/* Implementazione della divisione */
int dividi(int a, int b) {
    /* Controllo: non posso dividere per zero! */
    if (b == 0) {
        return 0;  /* Ritorno 0 come valore di errore */
    }
    return a / b;
}
