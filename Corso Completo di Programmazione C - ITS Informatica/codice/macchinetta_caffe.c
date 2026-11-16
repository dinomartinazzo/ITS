/*
 * macchinetta_caffe.c
 * Simulazione didattica di un distributore di bevande calde
 * realizzato come macchina a stati finiti.
 *
 * Costrutti di controllo usati: if, for, do-while, switch.
 * Tutti gli importi sono espressi in centesimi (interi).
 *
 * Compilazione:  gcc -std=c99 -Wall -Wextra -o macchinetta macchinetta_caffe.c
 */

#include <stdio.h>
#include <stdlib.h>

/* ------------------------------------------------------------------ */
/* CONFIGURAZIONE                                                      */
/* ------------------------------------------------------------------ */

#define NUM_BEVANDE         4
#define NUM_TAGLI           6
#define PASSI_PREPARAZIONE  5

/* Se si cambia NUM_BEVANDE aggiornare anche i case dello stato SELEZIONE */
const char *NOMI_BEVANDE[NUM_BEVANDE]   = { "Caffe'", "Cappuccino", "Te'", "Cioccolata" };
const int   PREZZI_BEVANDE[NUM_BEVANDE] = { 60, 90, 75, 110 };

/* Tagli accettati, in ordine decrescente (serve per il calcolo del resto) */
const int TAGLI_MONETE[NUM_TAGLI] = { 200, 100, 50, 20, 10, 5 };

/* Stati dell'automa */
typedef enum {
    SELEZIONE,      /* menu e scelta della bevanda          */
    INSERIMENTO,    /* accumulo del credito                 */
    RESTO,          /* erogazione del resto o del rimborso  */
    PREPARAZIONE,   /* preparazione della bevanda           */
    SPENTA          /* stato finale: uscita dal programma   */
} Stato;

/* ------------------------------------------------------------------ */
/* FUNZIONI DI INGRESSO / USCITA                                       */
/* ------------------------------------------------------------------ */

/* Legge un intero da tastiera. Restituisce -1 se l'input non e' un numero. */
int leggi_intero(void)
{
    int valore = -1;
    int c;
    int letti;

    letti = scanf("%d", &valore);
    if (letti == EOF) {         /* ingresso chiuso: si termina */
        printf("\nIngresso terminato.\n");
        exit(0);
    }
    if (letti != 1) {           /* testo non numerico */
        valore = -1;
    }

    /* Scarta il resto della riga */
    do {
        c = getchar();
    } while (c != '\n' && c != EOF);

    return valore;
}

/* Stampa un importo in centesimi nel formato euro (es. 110 -> 1.10) */
void stampa_euro(int centesimi)
{
    printf("%d.%02d EUR", centesimi / 100, centesimi % 100);
}

void stampa_menu(void)
{
    int i;

    printf("\n=============================\n");
    printf("   DISTRIBUTORE AUTOMATICO\n");
    printf("=============================\n");
    for (i = 0; i < NUM_BEVANDE; i++) {
        printf(" %d) %-12s ", i + 1, NOMI_BEVANDE[i]);
        stampa_euro(PREZZI_BEVANDE[i]);
        printf("\n");
    }
    printf(" 0) Spegni la macchina\n");
    printf("Scelta: ");
}

/* ------------------------------------------------------------------ */
/* LOGICA                                                              */
/* ------------------------------------------------------------------ */

/* Eroga l'importo indicato usando il minor numero di monete */
void eroga_resto(int importo)
{
    int i;
    int quante;

    if (importo == 0) {
        printf("Nessun resto da erogare.\n");
    } else {
        printf("Resto: ");
        stampa_euro(importo);
        printf("\n");
        for (i = 0; i < NUM_TAGLI; i++) {
            quante  = importo / TAGLI_MONETE[i];
            importo = importo % TAGLI_MONETE[i];
            if (quante > 0) {   /* si stampano solo i tagli usati */
                printf("  %d x ", quante);
                stampa_euro(TAGLI_MONETE[i]);
                printf("\n");
            }
        }
    }
}

/* Simula la preparazione con una barra di avanzamento */
void prepara_bevanda(const char *nome)
{
    int passo;

    printf("Preparazione di %s in corso\n", nome);
    for (passo = 1; passo <= PASSI_PREPARAZIONE; passo++) {
        printf("  [%d/%d] %d%%\n", passo, PASSI_PREPARAZIONE,
               passo * 100 / PASSI_PREPARAZIONE);
    }
    printf("%s pronto. Ritirare la bevanda.\n", nome);
}

/* ------------------------------------------------------------------ */
/* PROGRAMMA PRINCIPALE: ciclo dell'automa                             */
/* ------------------------------------------------------------------ */

int main(void)
{
    Stato stato = SELEZIONE;
    int bevanda   = 0;   /* indice della bevanda scelta          */
    int credito   = 0;   /* centesimi inseriti                   */
    int annullato = 0;   /* 1 se l'utente ha annullato l'acquisto */
    int scelta;
    int moneta;
    int resto;

    do {
        switch (stato) {

            case SELEZIONE:
                stampa_menu();
                scelta = leggi_intero();
                switch (scelta) {
                    case 0:
                        stato = SPENTA;
                        break;
                    /* Case vuoti voluti (fall-through): senza break
                       l'esecuzione prosegue fino al blocco comune sotto */
                    case 1:
                    case 2:
                    case 3:
                    case 4:
                        bevanda   = scelta - 1;
                        credito   = 0;
                        annullato = 0;
                        stato     = INSERIMENTO;
                        break;
                    default:
                        printf("Scelta non valida.\n");
                }
                break;

            case INSERIMENTO:
                printf("\n%s - prezzo ", NOMI_BEVANDE[bevanda]);
                stampa_euro(PREZZI_BEVANDE[bevanda]);
                printf(" - credito ");
                stampa_euro(credito);
                printf("\nInserire moneta in centesimi (5 10 20 50 100 200, 0 = annulla): ");
                moneta = leggi_intero();
                switch (moneta) {
                    /* Fall-through voluto: tutte le monete valide
                       eseguono la stessa istruzione */
                    case 5:
                    case 10:
                    case 20:
                    case 50:
                    case 100:
                    case 200:
                        credito += moneta;
                        break;
                    case 0:
                        annullato = 1;
                        printf("Acquisto annullato.\n");
                        break;
                    default:
                        printf("Moneta non accettata.\n");
                }
                /* Transizione: credito sufficiente oppure annullamento */
                if (annullato || credito >= PREZZI_BEVANDE[bevanda]) {
                    stato = RESTO;
                }
                break;

            case RESTO:
                if (annullato) {    /* rimborso completo, niente bevanda */
                    resto = credito;
                    stato = SELEZIONE;
                } else {
                    resto = credito - PREZZI_BEVANDE[bevanda];
                    stato = PREPARAZIONE;
                }
                eroga_resto(resto);
                credito = 0;
                break;

            case PREPARAZIONE:
                prepara_bevanda(NOMI_BEVANDE[bevanda]);
                stato = SELEZIONE;
                break;

            default:
                stato = SPENTA;
        }
    } while (stato != SPENTA);

    printf("Macchina spenta.\n");
    return 0;
}
