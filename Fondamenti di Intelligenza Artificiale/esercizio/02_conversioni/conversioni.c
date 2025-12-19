/*
 * =====================================================
 * FILE: conversioni.c
 * IMPLEMENTAZIONE: Libreria Conversioni
 * =====================================================
 */

#include "conversioni.h"

/* ========== COSTANTI ========== */
#define ZERO_ASSOLUTO_CELSIUS -273.15
#define ZERO_ASSOLUTO_FAHRENHEIT -459.67
#define ZERO_ASSOLUTO_KELVIN 0.0

/* ========== IMPLEMENTAZIONI TEMPERATURE ========== */

int celsius_to_fahrenheit(double celsius, double *out) {
    /* Validazione: temperatura sopra zero assoluto e out non NULL */
    if (celsius < ZERO_ASSOLUTO_CELSIUS || out == ((void*)0)) {
        return -1;
    }

    /* Formula: F = (C * 9/5) + 32 */
    *out = (celsius * 9.0 / 5.0) + 32.0;
    return 0;
}

int fahrenheit_to_celsius(double fahrenheit, double *out) {
    /* Validazione */
    if (fahrenheit < ZERO_ASSOLUTO_FAHRENHEIT || out == ((void*)0)) {
        return -1;
    }

    /* Formula: C = (F - 32) * 5/9 */
    *out = (fahrenheit - 32.0) * 5.0 / 9.0;
    return 0;
}

int celsius_to_kelvin(double celsius, double *out) {
    /* Validazione */
    if (celsius < ZERO_ASSOLUTO_CELSIUS || out == ((void*)0)) {
        return -1;
    }

    /* Formula: K = C + 273.15 */
    *out = celsius + 273.15;
    return 0;
}

int kelvin_to_celsius(double kelvin, double *out) {
    /* Validazione */
    if (kelvin < ZERO_ASSOLUTO_KELVIN || out == ((void*)0)) {
        return -1;
    }

    /* Formula: C = K - 273.15 */
    *out = kelvin - 273.15;
    return 0;
}

int fahrenheit_to_kelvin(double fahrenheit, double *out) {
    /* Validazione */
    if (fahrenheit < ZERO_ASSOLUTO_FAHRENHEIT || out == ((void*)0)) {
        return -1;
    }

    /* Formula: K = (F - 32) * 5/9 + 273.15 */
    *out = (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15;
    return 0;
}

int kelvin_to_fahrenheit(double kelvin, double *out) {
    /* Validazione */
    if (kelvin < ZERO_ASSOLUTO_KELVIN || out == ((void*)0)) {
        return -1;
    }

    /* Formula: F = (K - 273.15) * 9/5 + 32 */
    *out = (kelvin - 273.15) * 9.0 / 5.0 + 32.0;
    return 0;
}

/* ========== IMPLEMENTAZIONI DISTANZE ========== */

int metri_to_km(double metri, double *out) {
    /* Validazione: distanza non negativa */
    if (metri < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Formula: km = m / 1000 */
    *out = metri / 1000.0;
    return 0;
}

int km_to_metri(double km, double *out) {
    /* Validazione */
    if (km < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Formula: m = km * 1000 */
    *out = km * 1000.0;
    return 0;
}

int km_to_miglia(double km, double *out) {
    /* Validazione */
    if (km < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Formula: miglia = km * 0.621371 */
    *out = km * 0.621371;
    return 0;
}

int miglia_to_km(double miglia, double *out) {
    /* Validazione */
    if (miglia < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Formula: km = miglia * 1.60934 */
    *out = miglia * 1.60934;
    return 0;
}

int metri_to_miglia(double metri, double *out) {
    /* Validazione */
    if (metri < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Formula: miglia = metri * 0.000621371 */
    *out = metri * 0.000621371;
    return 0;
}

/* ========== IMPLEMENTAZIONI VALUTE ========== */

int euro_to_usd(double euro, double *out) {
    /* Validazione: importo non negativo */
    if (euro < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Tasso: 1 EUR = 1.10 USD (esempio) */
    *out = euro * 1.10;
    return 0;
}

int usd_to_euro(double usd, double *out) {
    /* Validazione */
    if (usd < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Tasso: 1 USD = 0.91 EUR (esempio) */
    *out = usd * 0.91;
    return 0;
}

int euro_to_gbp(double euro, double *out) {
    /* Validazione */
    if (euro < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Tasso: 1 EUR = 0.86 GBP (esempio) */
    *out = euro * 0.86;
    return 0;
}

int gbp_to_euro(double gbp, double *out) {
    /* Validazione */
    if (gbp < 0.0 || out == ((void*)0)) {
        return -1;
    }

    /* Tasso: 1 GBP = 1.16 EUR (esempio) */
    *out = gbp * 1.16;
    return 0;
}
