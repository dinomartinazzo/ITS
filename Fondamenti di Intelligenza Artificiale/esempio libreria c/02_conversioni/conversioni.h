/*
 * =====================================================
 * FILE: conversioni.h
 * LIBRERIA: Conversioni - Conversione unità di misura
 * LIVELLO: Principiante
 * =====================================================
 *
 * Questa libreria fornisce funzioni per convertire
 * temperature, distanze e valute
 */

#ifndef CONVERSIONI_H
#define CONVERSIONI_H

/* ========== CODICI DI RITORNO ========== */
/* 0 = OK, -1 = Errore (parametri invalidi) */

/* ========== CONVERSIONI TEMPERATURE ========== */

/**
 * Converte da Celsius a Fahrenheit
 * Formula: F = (C * 9/5) + 32
 *
 * Pre-condizioni:  celsius >= -273.15 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Fahrenheit se OK
 *
 * @param celsius: temperatura in gradi Celsius
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int celsius_to_fahrenheit(double celsius, double *out);

/**
 * Converte da Fahrenheit a Celsius
 * Formula: C = (F - 32) * 5/9
 *
 * Pre-condizioni:  fahrenheit >= -459.67 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Celsius se OK
 *
 * @param fahrenheit: temperatura in gradi Fahrenheit
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int fahrenheit_to_celsius(double fahrenheit, double *out);

/**
 * Converte da Celsius a Kelvin
 * Formula: K = C + 273.15
 *
 * Pre-condizioni:  celsius >= -273.15 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Kelvin se OK
 *
 * @param celsius: temperatura in gradi Celsius
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int celsius_to_kelvin(double celsius, double *out);

/**
 * Converte da Kelvin a Celsius
 * Formula: C = K - 273.15
 *
 * Pre-condizioni:  kelvin >= 0 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Celsius se OK
 *
 * @param kelvin: temperatura in gradi Kelvin
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int kelvin_to_celsius(double kelvin, double *out);

/**
 * Converte da Fahrenheit a Kelvin
 * Formula: K = (F - 32) * 5/9 + 273.15
 *
 * Pre-condizioni:  fahrenheit >= -459.67 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Kelvin se OK
 *
 * @param fahrenheit: temperatura in gradi Fahrenheit
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int fahrenheit_to_kelvin(double fahrenheit, double *out);

/**
 * Converte da Kelvin a Fahrenheit
 * Formula: F = (K - 273.15) * 9/5 + 32
 *
 * Pre-condizioni:  kelvin >= 0 (zero assoluto), out != NULL
 * Post-condizioni: *out contiene temperatura in Fahrenheit se OK
 *
 * @param kelvin: temperatura in gradi Kelvin
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int kelvin_to_fahrenheit(double kelvin, double *out);

/* ========== CONVERSIONI DISTANZE ========== */

/**
 * Converte da metri a chilometri
 * Formula: km = m / 1000
 *
 * Pre-condizioni:  metri >= 0, out != NULL
 * Post-condizioni: *out contiene distanza in km se OK
 *
 * @param metri: distanza in metri
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int metri_to_km(double metri, double *out);

/**
 * Converte da chilometri a metri
 * Formula: m = km * 1000
 *
 * Pre-condizioni:  km >= 0, out != NULL
 * Post-condizioni: *out contiene distanza in metri se OK
 *
 * @param km: distanza in chilometri
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int km_to_metri(double km, double *out);

/**
 * Converte da chilometri a miglia
 * Formula: miglia = km * 0.621371
 *
 * Pre-condizioni:  km >= 0, out != NULL
 * Post-condizioni: *out contiene distanza in miglia se OK
 *
 * @param km: distanza in chilometri
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int km_to_miglia(double km, double *out);

/**
 * Converte da miglia a chilometri
 * Formula: km = miglia * 1.60934
 *
 * Pre-condizioni:  miglia >= 0, out != NULL
 * Post-condizioni: *out contiene distanza in km se OK
 *
 * @param miglia: distanza in miglia
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int miglia_to_km(double miglia, double *out);

/**
 * Converte da metri a miglia
 * Formula: miglia = metri * 0.000621371
 *
 * Pre-condizioni:  metri >= 0, out != NULL
 * Post-condizioni: *out contiene distanza in miglia se OK
 *
 * @param metri: distanza in metri
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int metri_to_miglia(double metri, double *out);

/* ========== CONVERSIONI VALUTE (tassi esempio) ========== */

/**
 * Converte da Euro a Dollari USA
 * Tasso: 1 EUR = 1.10 USD (esempio, tasso variabile nella realtà)
 *
 * Pre-condizioni:  euro >= 0, out != NULL
 * Post-condizioni: *out contiene importo in USD se OK
 *
 * @param euro: importo in Euro
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int euro_to_usd(double euro, double *out);

/**
 * Converte da Dollari USA a Euro
 * Tasso: 1 USD = 0.91 EUR (esempio, tasso variabile nella realtà)
 *
 * Pre-condizioni:  usd >= 0, out != NULL
 * Post-condizioni: *out contiene importo in EUR se OK
 *
 * @param usd: importo in Dollari USA
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int usd_to_euro(double usd, double *out);

/**
 * Converte da Euro a Sterline Inglesi
 * Tasso: 1 EUR = 0.86 GBP (esempio, tasso variabile nella realtà)
 *
 * Pre-condizioni:  euro >= 0, out != NULL
 * Post-condizioni: *out contiene importo in GBP se OK
 *
 * @param euro: importo in Euro
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int euro_to_gbp(double euro, double *out);

/**
 * Converte da Sterline Inglesi a Euro
 * Tasso: 1 GBP = 1.16 EUR (esempio, tasso variabile nella realtà)
 *
 * Pre-condizioni:  gbp >= 0, out != NULL
 * Post-condizioni: *out contiene importo in EUR se OK
 *
 * @param gbp: importo in Sterline
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int gbp_to_euro(double gbp, double *out);

#endif
