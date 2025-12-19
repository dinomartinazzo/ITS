#ifndef STATS_H
#define STATS_H

/**
 * Mini-libreria stats per statistiche su array di interi
 * Standard: C99
 * Convenzioni:
 * - Ritorno: 0 se OK, -1 se errore
 * - Errori gestiti: v==NULL, out==NULL, n<=0
 * - Le funzioni non stampano nulla
 */

/**
 * stats_min: Trova il valore minimo nell'array
 * Pre-condizioni: v != NULL, out != NULL, n > 0
 * Post-condizioni: *out contiene il minimo se ritorno == 0
 * Complessità: O(n)
 * @param v: puntatore all'array di interi (const)
 * @param n: numero di elementi nell'array
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int stats_min(const int *v, int n, int *out);

/**
 * stats_max: Trova il valore massimo nell'array
 * Pre-condizioni: v != NULL, out != NULL, n > 0
 * Post-condizioni: *out contiene il massimo se ritorno == 0
 * Complessità: O(n)
 * @param v: puntatore all'array di interi (const)
 * @param n: numero di elementi nell'array
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int stats_max(const int *v, int n, int *out);

/**
 * stats_sum_ll: Calcola la somma degli elementi usando long long
 * Pre-condizioni: v != NULL, out != NULL, n > 0
 * Post-condizioni: *out contiene la somma se ritorno == 0
 * Complessità: O(n)
 * Nota overflow: usa long long per evitare overflow con valori grandi
 * @param v: puntatore all'array di interi (const)
 * @param n: numero di elementi nell'array
 * @param out: puntatore dove scrivere il risultato (long long)
 * @return 0 se OK, -1 se errore
 */
int stats_sum_ll(const int *v, int n, long long *out);

/**
 * stats_mean: Calcola la media aritmetica degli elementi
 * Pre-condizioni: v != NULL, out != NULL, n > 0
 * Post-condizioni: *out contiene la media se ritorno == 0
 * Complessità: O(n)
 * Nota precisione: usa double per precisione decimale
 * @param v: puntatore all'array di interi (const)
 * @param n: numero di elementi nell'array
 * @param out: puntatore dove scrivere il risultato (double)
 * @return 0 se OK, -1 se errore
 */
int stats_mean(const int *v, int n, double *out);

/**
 * stats_variance_population: Calcola la varianza di popolazione
 * Pre-condizioni: v != NULL, out != NULL, n > 0
 * Post-condizioni: *out contiene la varianza se ritorno == 0
 * Complessità: O(n) - due passate (media + varianza)
 * Formula: (1/n) * somma((xi - mean)^2)
 * Nota: varianza di popolazione usa divisore n (non n-1)
 * @param v: puntatore all'array di interi (const)
 * @param n: numero di elementi nell'array
 * @param out: puntatore dove scrivere il risultato (double)
 * @return 0 se OK, -1 se errore
 */
int stats_variance_population(const int *v, int n, double *out);

#endif
