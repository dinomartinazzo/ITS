/*
 * =====================================================
 * FILE: test_conversioni.c
 * SCOPO: Test della libreria conversioni
 * =====================================================
 */

#include <stdio.h>
#include "conversioni.h"

void stampa_separatore(void) {
    printf("=============================================\n");
}

void test_temperature(void) {
    printf("\n=== TEST CONVERSIONI TEMPERATURE ===\n");

    double risultato;
    int rc;

    /* Test 1: Celsius → Fahrenheit */
    printf("\n1. Celsius → Fahrenheit:\n");
    rc = celsius_to_fahrenheit(0.0, &risultato);
    if (rc == 0) {
        printf("   0°C = %.2f°F (atteso 32.00)\n", risultato);
    }

    rc = celsius_to_fahrenheit(100.0, &risultato);
    if (rc == 0) {
        printf("   100°C = %.2f°F (atteso 212.00)\n", risultato);
    }

    /* Test 2: Fahrenheit → Celsius */
    printf("\n2. Fahrenheit → Celsius:\n");
    rc = fahrenheit_to_celsius(32.0, &risultato);
    if (rc == 0) {
        printf("   32°F = %.2f°C (atteso 0.00)\n", risultato);
    }

    rc = fahrenheit_to_celsius(212.0, &risultato);
    if (rc == 0) {
        printf("   212°F = %.2f°C (atteso 100.00)\n", risultato);
    }

    /* Test 3: Celsius → Kelvin */
    printf("\n3. Celsius → Kelvin:\n");
    rc = celsius_to_kelvin(0.0, &risultato);
    if (rc == 0) {
        printf("   0°C = %.2fK (atteso 273.15)\n", risultato);
    }

    rc = celsius_to_kelvin(-273.15, &risultato);
    if (rc == 0) {
        printf("   -273.15°C = %.2fK (atteso 0.00 - zero assoluto)\n", risultato);
    }

    /* Test 4: Kelvin → Celsius */
    printf("\n4. Kelvin → Celsius:\n");
    rc = kelvin_to_celsius(273.15, &risultato);
    if (rc == 0) {
        printf("   273.15K = %.2f°C (atteso 0.00)\n", risultato);
    }

    /* Test 5: Errore temperatura sotto zero assoluto */
    printf("\n5. Test errore (temperatura impossibile):\n");
    rc = celsius_to_fahrenheit(-300.0, &risultato);
    if (rc != 0) {
        printf("   PASS: Temperatura -300°C correttamente rifiutata (rc=%d)\n", rc);
    } else {
        printf("   FAIL: Temperatura impossibile non rilevata!\n");
    }
}

void test_distanze(void) {
    printf("\n=== TEST CONVERSIONI DISTANZE ===\n");

    double risultato;
    int rc;

    /* Test 1: Metri → Km */
    printf("\n1. Metri → Chilometri:\n");
    rc = metri_to_km(1000.0, &risultato);
    if (rc == 0) {
        printf("   1000 m = %.2f km (atteso 1.00)\n", risultato);
    }

    rc = metri_to_km(5000.0, &risultato);
    if (rc == 0) {
        printf("   5000 m = %.2f km (atteso 5.00)\n", risultato);
    }

    /* Test 2: Km → Metri */
    printf("\n2. Chilometri → Metri:\n");
    rc = km_to_metri(1.0, &risultato);
    if (rc == 0) {
        printf("   1 km = %.0f m (atteso 1000)\n", risultato);
    }

    rc = km_to_metri(2.5, &risultato);
    if (rc == 0) {
        printf("   2.5 km = %.0f m (atteso 2500)\n", risultato);
    }

    /* Test 3: Km → Miglia */
    printf("\n3. Chilometri → Miglia:\n");
    rc = km_to_miglia(10.0, &risultato);
    if (rc == 0) {
        printf("   10 km = %.2f miglia (atteso ~6.21)\n", risultato);
    }

    /* Test 4: Miglia → Km */
    printf("\n4. Miglia → Chilometri:\n");
    rc = miglia_to_km(5.0, &risultato);
    if (rc == 0) {
        printf("   5 miglia = %.2f km (atteso ~8.05)\n", risultato);
    }

    /* Test 5: Metri → Miglia */
    printf("\n5. Metri → Miglia:\n");
    rc = metri_to_miglia(1609.34, &risultato);
    if (rc == 0) {
        printf("   1609.34 m = %.2f miglia (atteso ~1.00)\n", risultato);
    }

    /* Test 6: Errore distanza negativa */
    printf("\n6. Test errore (distanza negativa):\n");
    rc = metri_to_km(-100.0, &risultato);
    if (rc != 0) {
        printf("   PASS: Distanza negativa correttamente rifiutata (rc=%d)\n", rc);
    } else {
        printf("   FAIL: Distanza negativa non rilevata!\n");
    }
}

void test_valute(void) {
    printf("\n=== TEST CONVERSIONI VALUTE ===\n");
    printf("(NOTA: Tassi di cambio sono esempi, non reali!)\n");

    double risultato;
    int rc;

    /* Test 1: Euro → USD */
    printf("\n1. Euro → Dollari USA:\n");
    rc = euro_to_usd(100.0, &risultato);
    if (rc == 0) {
        printf("   100 EUR = %.2f USD (tasso 1.10)\n", risultato);
    }

    rc = euro_to_usd(50.0, &risultato);
    if (rc == 0) {
        printf("   50 EUR = %.2f USD\n", risultato);
    }

    /* Test 2: USD → Euro */
    printf("\n2. Dollari USA → Euro:\n");
    rc = usd_to_euro(110.0, &risultato);
    if (rc == 0) {
        printf("   110 USD = %.2f EUR (tasso 0.91)\n", risultato);
    }

    /* Test 3: Euro → GBP */
    printf("\n3. Euro → Sterline:\n");
    rc = euro_to_gbp(100.0, &risultato);
    if (rc == 0) {
        printf("   100 EUR = %.2f GBP (tasso 0.86)\n", risultato);
    }

    /* Test 4: GBP → Euro */
    printf("\n4. Sterline → Euro:\n");
    rc = gbp_to_euro(86.0, &risultato);
    if (rc == 0) {
        printf("   86 GBP = %.2f EUR (tasso 1.16)\n", risultato);
    }

    /* Test 5: Errore importo negativo */
    printf("\n5. Test errore (importo negativo):\n");
    rc = euro_to_usd(-50.0, &risultato);
    if (rc != 0) {
        printf("   PASS: Importo negativo correttamente rifiutato (rc=%d)\n", rc);
    } else {
        printf("   FAIL: Importo negativo non rilevato!\n");
    }
}

void test_conversioni_multiple(void) {
    printf("\n=== TEST CONVERSIONI A CATENA ===\n");

    double temp_f, temp_k;
    int rc1, rc2;

    printf("\nConversione a catena: 25°C → °F → K\n");

    /* 25°C → °F */
    rc1 = celsius_to_fahrenheit(25.0, &temp_f);
    if (rc1 == 0) {
        printf("  Passo 1: 25°C = %.2f°F\n", temp_f);
    }

    /* °F → K */
    rc2 = fahrenheit_to_kelvin(temp_f, &temp_k);
    if (rc2 == 0) {
        printf("  Passo 2: %.2f°F = %.2fK\n", temp_f, temp_k);
    }

    /* Verifica diretta: 25°C → K */
    double temp_k_diretto;
    celsius_to_kelvin(25.0, &temp_k_diretto);
    printf("  Verifica diretta: 25°C = %.2fK\n", temp_k_diretto);

    if (temp_k > temp_k_diretto - 0.01 && temp_k < temp_k_diretto + 0.01) {
        printf("  PASS: Conversioni a catena coerenti!\n");
    } else {
        printf("  FAIL: Differenza tra conversioni!\n");
    }
}

void test_casi_pratici(void) {
    printf("\n=== TEST CASI PRATICI ===\n");

    double risultato;

    /* Caso 1: Febbre */
    printf("\n1. Febbre 37.5°C in Fahrenheit:\n");
    celsius_to_fahrenheit(37.5, &risultato);
    printf("   37.5°C = %.1f°F\n", risultato);

    /* Caso 2: Maratona */
    printf("\n2. Maratona 42.195 km in miglia:\n");
    km_to_miglia(42.195, &risultato);
    printf("   42.195 km = %.2f miglia\n", risultato);

    /* Caso 3: Viaggio 100 km in miglia */
    printf("\n3. Viaggio di 100 km in miglia:\n");
    km_to_miglia(100.0, &risultato);
    printf("   100 km = %.2f miglia\n", risultato);

    /* Caso 4: Shopping online */
    printf("\n4. Acquisto online 50 EUR in USD:\n");
    euro_to_usd(50.0, &risultato);
    printf("   50 EUR = %.2f USD\n", risultato);

    /* Caso 5: Zero assoluto */
    printf("\n5. Zero assoluto in tutte le scale:\n");
    printf("   0 K = -273.15°C\n");
    kelvin_to_fahrenheit(0.0, &risultato);
    printf("   0 K = %.2f°F\n", risultato);
}

void test_errori_out_null(void) {
    printf("\n=== TEST ERRORE OUT=NULL ===\n");

    int rc = celsius_to_fahrenheit(100.0, ((void*)0));

    if (rc != 0) {
        printf("PASS: Errore out=NULL correttamente rilevato (rc=%d)\n", rc);
    } else {
        printf("FAIL: Errore out=NULL non rilevato!\n");
    }
}

int main(void) {
    printf("=============================================\n");
    printf("   TEST LIBRERIA CONVERSIONI\n");
    printf("=============================================\n");

    test_temperature();
    stampa_separatore();

    test_distanze();
    stampa_separatore();

    test_valute();
    stampa_separatore();

    test_conversioni_multiple();
    stampa_separatore();

    test_casi_pratici();
    stampa_separatore();

    test_errori_out_null();
    stampa_separatore();

    printf("\n=== TUTTI I TEST COMPLETATI ===\n\n");

    return 0;
}
