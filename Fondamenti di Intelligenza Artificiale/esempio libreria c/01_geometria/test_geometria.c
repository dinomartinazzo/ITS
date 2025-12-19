/*
 * =====================================================
 * FILE: test_geometria.c
 * SCOPO: Test della libreria geometria
 * =====================================================
 */

#include <stdio.h>
#include "geometria.h"

void stampa_separatore(void) {
    printf("=============================================\n");
}

void test_cerchio(void) {
    printf("\n=== TEST CERCHIO ===\n");

    double raggio = 5.0;
    double area, perimetro;

    printf("Cerchio con raggio = %.2f\n", raggio);

    /* Test area */
    int rc_area = area_cerchio(raggio, &area);
    if (rc_area == 0) {
        printf("  Area = %.2f (atteso ~78.54)\n", area);
    } else {
        printf("  ERRORE nel calcolo area!\n");
    }

    /* Test perimetro */
    int rc_perim = perimetro_cerchio(raggio, &perimetro);
    if (rc_perim == 0) {
        printf("  Perimetro = %.2f (atteso ~31.42)\n", perimetro);
    } else {
        printf("  ERRORE nel calcolo perimetro!\n");
    }

    /* Test errore: raggio negativo */
    printf("\nTest errore (raggio negativo = -3):\n");
    rc_area = area_cerchio(-3.0, &area);
    if (rc_area != 0) {
        printf("  PASS: Errore correttamente rilevato (rc=%d)\n", rc_area);
    } else {
        printf("  FAIL: Errore non rilevato!\n");
    }
}

void test_rettangolo(void) {
    printf("\n=== TEST RETTANGOLO ===\n");

    double base = 8.0;
    double altezza = 5.0;
    double area, perimetro;

    printf("Rettangolo con base = %.2f, altezza = %.2f\n", base, altezza);

    /* Test area */
    int rc_area = area_rettangolo(base, altezza, &area);
    if (rc_area == 0) {
        printf("  Area = %.2f (atteso 40.00)\n", area);
    } else {
        printf("  ERRORE nel calcolo area!\n");
    }

    /* Test perimetro */
    int rc_perim = perimetro_rettangolo(base, altezza, &perimetro);
    if (rc_perim == 0) {
        printf("  Perimetro = %.2f (atteso 26.00)\n", perimetro);
    } else {
        printf("  ERRORE nel calcolo perimetro!\n");
    }
}

void test_triangolo(void) {
    printf("\n=== TEST TRIANGOLO ===\n");

    /* Test area con base e altezza */
    double base = 6.0;
    double altezza = 4.0;
    double area;

    printf("Triangolo con base = %.2f, altezza = %.2f\n", base, altezza);

    int rc_area = area_triangolo(base, altezza, &area);
    if (rc_area == 0) {
        printf("  Area = %.2f (atteso 12.00)\n", area);
    } else {
        printf("  ERRORE nel calcolo area!\n");
    }

    /* Test perimetro con lati validi */
    double lato1 = 3.0, lato2 = 4.0, lato3 = 5.0;  /* Triangolo rettangolo */
    double perimetro;

    printf("\nTriangolo con lati = %.2f, %.2f, %.2f\n", lato1, lato2, lato3);

    int rc_perim = perimetro_triangolo(lato1, lato2, lato3, &perimetro);
    if (rc_perim == 0) {
        printf("  Perimetro = %.2f (atteso 12.00)\n", perimetro);
    } else {
        printf("  ERRORE nel calcolo perimetro!\n");
    }

    /* Test errore: triangolo non valido (disuguaglianza non rispettata) */
    printf("\nTest errore (triangolo invalido: lati 1, 2, 10):\n");
    rc_perim = perimetro_triangolo(1.0, 2.0, 10.0, &perimetro);
    if (rc_perim != 0) {
        printf("  PASS: Triangolo invalido rilevato (rc=%d)\n", rc_perim);
    } else {
        printf("  FAIL: Triangolo invalido non rilevato!\n");
    }
}

void test_quadrato(void) {
    printf("\n=== TEST QUADRATO ===\n");

    double lato = 7.0;
    double area, perimetro;

    printf("Quadrato con lato = %.2f\n", lato);

    /* Test area */
    int rc_area = area_quadrato(lato, &area);
    if (rc_area == 0) {
        printf("  Area = %.2f (atteso 49.00)\n", area);
    } else {
        printf("  ERRORE nel calcolo area!\n");
    }

    /* Test perimetro */
    int rc_perim = perimetro_quadrato(lato, &perimetro);
    if (rc_perim == 0) {
        printf("  Perimetro = %.2f (atteso 28.00)\n", perimetro);
    } else {
        printf("  ERRORE nel calcolo perimetro!\n");
    }
}

void test_errori_out_null(void) {
    printf("\n=== TEST ERRORI OUT=NULL ===\n");

    /* Test con puntatore out NULL */
    int rc = area_cerchio(5.0, ((void*)0));

    if (rc != 0) {
        printf("PASS: Errore out=NULL correttamente rilevato (rc=%d)\n", rc);
    } else {
        printf("FAIL: Errore out=NULL non rilevato!\n");
    }
}

void test_casi_limite(void) {
    printf("\n=== TEST CASI LIMITE ===\n");

    /* Cerchio con raggio molto piccolo */
    double area_piccola;
    area_cerchio(0.1, &area_piccola);
    printf("Cerchio raggio 0.1: area = %.6f\n", area_piccola);

    /* Rettangolo con lati uguali (diventa quadrato) */
    double area_quadrato_spec;
    area_rettangolo(5.0, 5.0, &area_quadrato_spec);
    printf("Rettangolo 5x5: area = %.2f (come un quadrato)\n", area_quadrato_spec);

    /* Triangolo equilatero */
    double perim_equilatero;
    perimetro_triangolo(5.0, 5.0, 5.0, &perim_equilatero);
    printf("Triangolo equilatero lato 5: perimetro = %.2f\n", perim_equilatero);
}

int main(void) {
    printf("=============================================\n");
    printf("   TEST LIBRERIA GEOMETRIA\n");
    printf("=============================================\n");

    test_cerchio();
    stampa_separatore();

    test_rettangolo();
    stampa_separatore();

    test_triangolo();
    stampa_separatore();

    test_quadrato();
    stampa_separatore();

    test_errori_out_null();
    stampa_separatore();

    test_casi_limite();
    stampa_separatore();

    printf("\n=== TUTTI I TEST COMPLETATI ===\n\n");

    return 0;
}
