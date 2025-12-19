#include <stdio.h>
#include "stats.h"

/* Funzione helper per stampare i risultati dei test */
void print_separator(void) {
    printf("========================================\n");
}

void test_case_1(void) {
    printf("TEST 1: v={1,2,3,4}\n");
    printf("Atteso: min=1, max=4, sum=10, mean=2.5, var_pop=1.25\n");

    int v[] = {1, 2, 3, 4};
    int n = 4;
    int min, max;
    long long sum;
    double mean, var_pop;

    int rc_min = stats_min(v, n, &min);
    int rc_max = stats_max(v, n, &max);
    int rc_sum = stats_sum_ll(v, n, &sum);
    int rc_mean = stats_mean(v, n, &mean);
    int rc_var = stats_variance_population(v, n, &var_pop);

    printf("Ottenuto: min=%d (rc=%d), max=%d (rc=%d), sum=%lld (rc=%d), mean=%.1f (rc=%d), var_pop=%.2f (rc=%d)\n",
           min, rc_min, max, rc_max, sum, rc_sum, mean, rc_mean, var_pop, rc_var);
    print_separator();
}

void test_case_2(void) {
    printf("TEST 2: v={-5,-1,-3}\n");
    printf("Atteso: min=-5, max=-1, sum=-9, mean=-3.0\n");

    int v[] = {-5, -1, -3};
    int n = 3;
    int min, max;
    long long sum;
    double mean;

    int rc_min = stats_min(v, n, &min);
    int rc_max = stats_max(v, n, &max);
    int rc_sum = stats_sum_ll(v, n, &sum);
    int rc_mean = stats_mean(v, n, &mean);

    printf("Ottenuto: min=%d (rc=%d), max=%d (rc=%d), sum=%lld (rc=%d), mean=%.1f (rc=%d)\n",
           min, rc_min, max, rc_max, sum, rc_sum, mean, rc_mean);
    print_separator();
}

void test_case_3(void) {
    printf("TEST 3: v={7} (array singolo)\n");
    printf("Atteso: mean=7.0, var_pop=0.0\n");

    int v[] = {7};
    int n = 1;
    double mean, var_pop;

    int rc_mean = stats_mean(v, n, &mean);
    int rc_var = stats_variance_population(v, n, &var_pop);

    printf("Ottenuto: mean=%.1f (rc=%d), var_pop=%.1f (rc=%d)\n",
           mean, rc_mean, var_pop, rc_var);
    print_separator();
}

void test_case_4(void) {
    printf("TEST 4: Errore v=NULL\n");
    printf("Atteso: rc != 0\n");

    int *v = ((void*)0);
    int n = 5;
    int result;

    int rc = stats_min(v, n, &result);

    printf("Ottenuto: rc=%d\n", rc);
    if (rc != 0) {
        printf("PASS: Errore correttamente rilevato\n");
    } else {
        printf("FAIL: Errore non rilevato!\n");
    }
    print_separator();
}

void test_case_5(void) {
    printf("TEST 5: Errore out=NULL\n");
    printf("Atteso: rc != 0\n");

    int v[] = {1, 2, 3};
    int n = 3;
    int *out = ((void*)0);

    int rc = stats_max(v, n, out);

    printf("Ottenuto: rc=%d\n", rc);
    if (rc != 0) {
        printf("PASS: Errore correttamente rilevato\n");
    } else {
        printf("FAIL: Errore non rilevato!\n");
    }
    print_separator();
}

void test_case_6(void) {
    printf("TEST 6: Errore n<=0\n");
    printf("Atteso: rc != 0\n");

    int v[] = {1, 2, 3};
    int n = 0;
    double result;

    int rc = stats_mean(v, n, &result);

    printf("Ottenuto: rc=%d\n", rc);
    if (rc != 0) {
        printf("PASS: Errore correttamente rilevato\n");
    } else {
        printf("FAIL: Errore non rilevato!\n");
    }
    print_separator();
}

void test_case_7(void) {
    printf("TEST 7: Somma grande (overflow int, necessario long long)\n");
    printf("v={1000000000, 1000000000, 1000000000}\n");
    printf("Atteso: sum=3000000000 (necessario long long)\n");

    int v[] = {1000000000, 1000000000, 1000000000};
    int n = 3;
    long long sum;

    int rc = stats_sum_ll(v, n, &sum);

    printf("Ottenuto: sum=%lld (rc=%d)\n", sum, rc);
    if (sum == 3000000000LL) {
        printf("PASS: Long long ha evitato l'overflow\n");
    } else {
        printf("FAIL: Valore non corretto!\n");
    }
    print_separator();
}

int main(void) {
    printf("========================================\n");
    printf("TEST MINI-LIBRERIA STATS\n");
    printf("========================================\n\n");

    test_case_1();
    test_case_2();
    test_case_3();
    test_case_4();
    test_case_5();
    test_case_6();
    test_case_7();

    printf("\nTutti i test completati.\n");

    return 0;
}
