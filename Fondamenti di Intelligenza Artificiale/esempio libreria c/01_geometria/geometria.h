/*
 * =====================================================
 * FILE: geometria.h
 * LIBRERIA: Geometria - Calcoli su figure geometriche
 * LIVELLO: Principiante
 * =====================================================
 *
 * Questa libreria fornisce funzioni per calcolare
 * area e perimetro di figure geometriche comuni
 */

#ifndef GEOMETRIA_H
#define GEOMETRIA_H

/* ========== COSTANTI ========== */
#define PI 3.14159265359

/* ========== CODICI DI RITORNO ========== */
/* 0 = OK, -1 = Errore (parametri invalidi) */

/* ========== FUNZIONI CERCHIO ========== */

/**
 * Calcola l'area di un cerchio
 * Formula: A = π * r²
 *
 * Pre-condizioni:  raggio > 0, out != NULL
 * Post-condizioni: *out contiene l'area se OK
 *
 * @param raggio: il raggio del cerchio
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int area_cerchio(double raggio, double *out);

/**
 * Calcola il perimetro (circonferenza) di un cerchio
 * Formula: P = 2 * π * r
 *
 * Pre-condizioni:  raggio > 0, out != NULL
 * Post-condizioni: *out contiene il perimetro se OK
 *
 * @param raggio: il raggio del cerchio
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int perimetro_cerchio(double raggio, double *out);

/* ========== FUNZIONI RETTANGOLO ========== */

/**
 * Calcola l'area di un rettangolo
 * Formula: A = base * altezza
 *
 * Pre-condizioni:  base > 0, altezza > 0, out != NULL
 * Post-condizioni: *out contiene l'area se OK
 *
 * @param base: la base del rettangolo
 * @param altezza: l'altezza del rettangolo
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int area_rettangolo(double base, double altezza, double *out);

/**
 * Calcola il perimetro di un rettangolo
 * Formula: P = 2 * (base + altezza)
 *
 * Pre-condizioni:  base > 0, altezza > 0, out != NULL
 * Post-condizioni: *out contiene il perimetro se OK
 *
 * @param base: la base del rettangolo
 * @param altezza: l'altezza del rettangolo
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int perimetro_rettangolo(double base, double altezza, double *out);

/* ========== FUNZIONI TRIANGOLO ========== */

/**
 * Calcola l'area di un triangolo
 * Formula: A = (base * altezza) / 2
 *
 * Pre-condizioni:  base > 0, altezza > 0, out != NULL
 * Post-condizioni: *out contiene l'area se OK
 *
 * @param base: la base del triangolo
 * @param altezza: l'altezza del triangolo
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int area_triangolo(double base, double altezza, double *out);

/**
 * Calcola il perimetro di un triangolo
 * Formula: P = lato1 + lato2 + lato3
 *
 * Pre-condizioni:  lato1 > 0, lato2 > 0, lato3 > 0, out != NULL
 *                  Deve rispettare disuguaglianza triangolare
 * Post-condizioni: *out contiene il perimetro se OK
 *
 * @param lato1: primo lato del triangolo
 * @param lato2: secondo lato del triangolo
 * @param lato3: terzo lato del triangolo
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int perimetro_triangolo(double lato1, double lato2, double lato3, double *out);

/* ========== FUNZIONI QUADRATO ========== */

/**
 * Calcola l'area di un quadrato
 * Formula: A = lato²
 *
 * Pre-condizioni:  lato > 0, out != NULL
 * Post-condizioni: *out contiene l'area se OK
 *
 * @param lato: il lato del quadrato
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int area_quadrato(double lato, double *out);

/**
 * Calcola il perimetro di un quadrato
 * Formula: P = 4 * lato
 *
 * Pre-condizioni:  lato > 0, out != NULL
 * Post-condizioni: *out contiene il perimetro se OK
 *
 * @param lato: il lato del quadrato
 * @param out: puntatore dove scrivere il risultato
 * @return 0 se OK, -1 se errore
 */
int perimetro_quadrato(double lato, double *out);

#endif
