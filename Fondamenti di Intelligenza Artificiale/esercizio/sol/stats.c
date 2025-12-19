#include "stats.h"

/**
 * Codici di errore:
 * -1: parametri invalidi (v==NULL, out==NULL, n<=0)
 */

int stats_min(const int *v, int n, int *out) {
    /* Validazione input */
    if (v == ((void*)0) || out == ((void*)0) || n <= 0) {
        return -1;
    }

    /* Trova il minimo */
    int min = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < min) {
            min = v[i];
        }
    }

    /* Scrivi output solo se tutto OK */
    *out = min;
    return 0;
}

int stats_max(const int *v, int n, int *out) {
    /* Validazione input */
    if (v == ((void*)0) || out == ((void*)0) || n <= 0) {
        return -1;
    }

    /* Trova il massimo */
    int max = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] > max) {
            max = v[i];
        }
    }

    /* Scrivi output solo se tutto OK */
    *out = max;
    return 0;
}

int stats_sum_ll(const int *v, int n, long long *out) {
    /* Validazione input */
    if (v == ((void*)0) || out == ((void*)0) || n <= 0) {
        return -1;
    }

    /* Calcola somma con long long per evitare overflow */
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += v[i];
    }

    /* Scrivi output solo se tutto OK */
    *out = sum;
    return 0;
}

int stats_mean(const int *v, int n, double *out) {
    /* Validazione input */
    if (v == ((void*)0) || out == ((void*)0) || n <= 0) {
        return -1;
    }

    /* Calcola somma */
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += v[i];
    }

    /* Calcola media con divisione double */
    double mean = (double)sum / (double)n;

    /* Scrivi output solo se tutto OK */
    *out = mean;
    return 0;
}

int stats_variance_population(const int *v, int n, double *out) {
    /* Validazione input */
    if (v == ((void*)0) || out == ((void*)0) || n <= 0) {
        return -1;
    }

    /* Prima passata: calcola la media */
    double mean;
    int rc = stats_mean(v, n, &mean);
    if (rc != 0) {
        return rc;  /* Errore nella chiamata a stats_mean */
    }

    /* Seconda passata: calcola somma dei quadrati degli scarti */
    double sum_squared_deviations = 0.0;
    for (int i = 0; i < n; i++) {
        double deviation = v[i] - mean;
        sum_squared_deviations += deviation * deviation;
    }

    /* Varianza di popolazione: divisore n (non n-1) */
    double variance = sum_squared_deviations / (double)n;

    /* Scrivi output solo se tutto OK */
    *out = variance;
    return 0;
}
