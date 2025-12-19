/*
 * =====================================================
 * FILE: geometria.c
 * IMPLEMENTAZIONE: Libreria Geometria
 * =====================================================
 */

#include "geometria.h"

/* ========== IMPLEMENTAZIONI CERCHIO ========== */

int area_cerchio(double raggio, double *out) {
    /* Validazione: raggio deve essere positivo e out non NULL */
    if (raggio <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola area: A = π * r² */
    *out = PI * raggio * raggio;
    return 0;
}

int perimetro_cerchio(double raggio, double *out) {
    /* Validazione */
    if (raggio <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola perimetro: P = 2 * π * r */
    *out = 2.0 * PI * raggio;
    return 0;
}

/* ========== IMPLEMENTAZIONI RETTANGOLO ========== */

int area_rettangolo(double base, double altezza, double *out) {
    /* Validazione */
    if (base <= 0.0 || altezza <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola area: A = base * altezza */
    *out = base * altezza;
    return 0;
}

int perimetro_rettangolo(double base, double altezza, double *out) {
    /* Validazione */
    if (base <= 0.0 || altezza <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola perimetro: P = 2 * (base + altezza) */
    *out = 2.0 * (base + altezza);
    return 0;
}

/* ========== IMPLEMENTAZIONI TRIANGOLO ========== */

int area_triangolo(double base, double altezza, double *out) {
    /* Validazione */
    if (base <= 0.0 || altezza <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola area: A = (base * altezza) / 2 */
    *out = (base * altezza) / 2.0;
    return 0;
}

int perimetro_triangolo(double lato1, double lato2, double lato3, double *out) {
    /* Validazione: lati positivi */
    if (lato1 <= 0.0 || lato2 <= 0.0 || lato3 <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Validazione: disuguaglianza triangolare */
    /* Un lato deve essere minore della somma degli altri due */
    if (lato1 >= (lato2 + lato3) ||
        lato2 >= (lato1 + lato3) ||
        lato3 >= (lato1 + lato2)) {
        return -1;  /* Non è un triangolo valido */
    }

    /* Calcola perimetro: P = lato1 + lato2 + lato3 */
    *out = lato1 + lato2 + lato3;
    return 0;
}

/* ========== IMPLEMENTAZIONI QUADRATO ========== */

int area_quadrato(double lato, double *out) {
    /* Validazione */
    if (lato <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola area: A = lato² */
    *out = lato * lato;
    return 0;
}

int perimetro_quadrato(double lato, double *out) {
    /* Validazione */
    if (lato <= 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Calcola perimetro: P = 4 * lato */
    *out = 4.0 * lato;
    return 0;
}
