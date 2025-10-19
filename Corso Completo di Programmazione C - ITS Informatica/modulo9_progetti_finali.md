# Modulo 9: Progetti Finali
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Integrare tutte le competenze apprese nei moduli precedenti
- Sviluppare progetti completi e funzionali
- Pianificare e strutturare un programma complesso
- Applicare le buone pratiche di programmazione
- Creare software utilizzabile nella vita reale

---

## 9.1 Come Affrontare un Progetto

### 📋 **Metodologia di Sviluppo**

1. **ANALISI**: Capire cosa deve fare il programma
2. **PROGETTAZIONE**: Pianificare la struttura
3. **IMPLEMENTAZIONE**: Scrivere il codice
4. **TEST**: Verificare che funzioni
5. **MIGLIORAMENTO**: Ottimizzare e aggiungere funzioni

### 🎯 **Esempio di Analisi**
**Progetto**: Sistema di gestione magazzino

**Cosa deve fare?**
- Aggiungere prodotti
- Visualizzare inventario  
- Cercare prodotti
- Aggiornare quantità
- Salvare dati su file
- Calcolare valore totale

**Strutture dati necessarie:**
- Struct Prodotto (nome, codice, prezzo, quantità)
- Array di prodotti
- File per persistenza

**Funzioni necessarie:**
- Menu principale
- Aggiungi/rimuovi prodotto
- Cerca prodotto
- Salva/carica da file
- Calcoli statistici

---

## 9.2 Progetto 1: Gestione Studenti Completa

### Sistema completo per gestire una classe con tutte le funzionalità:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTI 50
#define MAX_NOME 30
#define MAX_VOTI 10
#define FILE_STUDENTI "studenti.dat"

typedef struct {
    int id;
    char nome[MAX_NOME];
    char cognome[MAX_NOME];
    int eta;
    float voti[MAX_VOTI];
    int numero_voti;
    float media;
    char stato[20];  // "Promosso", "Bocciato", "In corso"
} Studente;

typedef struct {
    Studente studenti[MAX_STUDENTI];
    int numero_studenti;
    int prossimo_id;
} SistemaStudenti;

// Prototipi funzioni
void inizializza_sistema(SistemaStudenti *sistema);
void menu_principale(void);
void aggiungi_studente(SistemaStudenti *sistema);
void mostra_tutti_studenti(SistemaStudenti *sistema);
void cerca_studente(SistemaStudenti *sistema);
void aggiungi_voto(SistemaStudenti *sistema);
void calcola_statistiche_classe(SistemaStudenti *sistema);
void salva_sistema(SistemaStudenti *sistema);
int carica_sistema(SistemaStudenti *sistema);
void aggiorna_stato_studente(Studente *studente);
void stampa_pagella(SistemaStudenti *sistema);
void elimina_studente(SistemaStudenti *sistema);

int main() {
    SistemaStudenti sistema;
    int scelta;
    
    printf("🎓 === SISTEMA GESTIONE STUDENTI ITS === 🎓\n\n");
    
    inizializza_sistema(&sistema);
    
    if (carica_sistema(&sistema)) {
        printf("✅ Dati caricati dal file (%d studenti)\n", sistema.numero_studenti);
    } else {
        printf("📄 Iniziando con database vuoto\n");
    }
    
    do {
        menu_principale();
        printf("➤ Scegli opzione (1-9): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                aggiungi_studente(&sistema);
                break;
            case 2:
                mostra_tutti_studenti(&sistema);
                break;
            case 3:
                cerca_studente(&sistema);
                break;
            case 4:
                aggiungi_voto(&sistema);
                break;
            case 5:
                stampa_pagella(&sistema);
                break;
            case 6:
                calcola_statistiche_classe(&sistema);
                break;
            case 7:
                elimina_studente(&sistema);
                break;
            case 8:
                salva_sistema(&sistema);
                printf("✅ Sistema salvato con successo!\n");
                break;
            case 9:
                salva_sistema(&sistema);
                printf("💾 Dati salvati. Arrivederci!\n");
                break;
            default:
                printf("❌ Opzione non valida!\n");
        }
        
        if (scelta != 9) {
            printf("\n🔄 Premi INVIO per continuare...");
            getchar();
            getchar();
        }
        
    } while (scelta != 9);
    
    return 0;
}

void inizializza_sistema(SistemaStudenti *sistema) {
    sistema->numero_studenti = 0;
    sistema->prossimo_id = 1;
}

void menu_principale(void) {
    printf("\n" "═══════════════════════════════════════════════\n");
    printf("📋 MENU PRINCIPALE\n");
    printf("═══════════════════════════════════════════════\n");
    printf("1️⃣  Aggiungi nuovo studente\n");
    printf("2️⃣  Mostra tutti gli studenti\n");  
    printf("3️⃣  Cerca studente\n");
    printf("4️⃣  Aggiungi voto\n");
    printf("5️⃣  Stampa pagella\n");
    printf("6️⃣  Statistiche classe\n");
    printf("7️⃣  Elimina studente\n");
    printf("8️⃣  Salva dati\n");
    printf("9️⃣  Esci\n");
    printf("═══════════════════════════════════════════════\n");
}

void aggiungi_studente(SistemaStudenti *sistema) {
    if (sistema->numero_studenti >= MAX_STUDENTI) {
        printf("❌ Errore: Classe piena! (Max %d studenti)\n", MAX_STUDENTI);
        return;
    }
    
    Studente *nuovo = &sistema->studenti[sistema->numero_studenti];
    
    printf("\n📝 === REGISTRAZIONE NUOVO STUDENTE ===\n");
    
    nuovo->id = sistema->prossimo_id++;
    
    printf("👤 Nome: ");
    scanf("%29s", nuovo->nome);
    
    printf("👤 Cognome: ");
    scanf("%29s", nuovo->cognome);
    
    do {
        printf("🎂 Età: ");
        scanf("%d", &nuovo->eta);
        if (nuovo->eta < 14 || nuovo->eta > 25) {
            printf("❌ Età non valida per studente ITS (14-25 anni)\n");
        }
    } while (nuovo->eta < 14 || nuovo->eta > 25);
    
    nuovo->numero_voti = 0;
    nuovo->media = 0.0;
    strcpy(nuovo->stato, "In corso");
    
    sistema->numero_studenti++;
    
    printf("✅ Studente %s %s aggiunto con ID %d!\n", 
           nuovo->nome, nuovo->cognome, nuovo->id);
}

void mostra_tutti_studenti(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente registrato.\n");
        return;
    }
    
    printf("\n📊 === ELENCO COMPLETO STUDENTI ===\n");
    printf("ID  %-15s %-15s Età Voti Media  Stato\n", "Nome", "Cognome");
    printf("─────────────────────────────────────────────────────────\n");
    
    for (int i = 0; i < sistema->numero_studenti; i++) {
        Studente *s = &sistema->studenti[i];
        printf("%-3d %-15s %-15s %-3d %-4d %-6.2f %s\n",
               s->id, s->nome, s->cognome, s->eta,
               s->numero_voti, s->media, s->stato);
    }
    
    printf("─────────────────────────────────────────────────────────\n");
    printf("Totale studenti: %d\n", sistema->numero_studenti);
}

void cerca_studente(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente da cercare.\n");
        return;
    }
    
    char termine[50];
    printf("🔍 Cerca per nome o cognome: ");
    scanf("%49s", termine);
    
    printf("\n🔍 === RISULTATI RICERCA ===\n");
    int trovati = 0;
    
    for (int i = 0; i < sistema->numero_studenti; i++) {
        Studente *s = &sistema->studenti[i];
        if (strstr(s->nome, termine) || strstr(s->cognome, termine)) {
            printf("👤 ID %d: %s %s (età %d) - Media: %.2f - %s\n",
                   s->id, s->nome, s->cognome, s->eta, s->media, s->stato);
            
            if (s->numero_voti > 0) {
                printf("   📚 Voti: ");
                for (int j = 0; j < s->numero_voti; j++) {
                    printf("%.1f ", s->voti[j]);
                }
                printf("\n");
            }
            printf("\n");
            trovati++;
        }
    }
    
    if (trovati == 0) {
        printf("❌ Nessuno studente trovato con '%s'\n", termine);
    } else {
        printf("✅ Trovati %d studenti\n", trovati);
    }
}

void aggiungi_voto(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente registrato.\n");
        return;
    }
    
    int id;
    printf("🆔 Inserisci ID studente: ");
    scanf("%d", &id);
    
    // Cerca studente per ID
    Studente *studente = NULL;
    for (int i = 0; i < sistema->numero_studenti; i++) {
        if (sistema->studenti[i].id == id) {
            studente = &sistema->studenti[i];
            break;
        }
    }
    
    if (studente == NULL) {
        printf("❌ Studente con ID %d non trovato!\n", id);
        return;
    }
    
    if (studente->numero_voti >= MAX_VOTI) {
        printf("❌ Lo studente ha già il numero massimo di voti (%d)\n", MAX_VOTI);
        return;
    }
    
    float voto;
    do {
        printf("📊 Inserisci voto per %s %s (0.0-10.0): ", 
               studente->nome, studente->cognome);
        scanf("%f", &voto);
        
        if (voto < 0.0 || voto > 10.0) {
            printf("❌ Voto non valido! Deve essere tra 0.0 e 10.0\n");
        }
    } while (voto < 0.0 || voto > 10.0);
    
    studente->voti[studente->numero_voti] = voto;
    studente->numero_voti++;
    
    // Ricalcola media
    float somma = 0;
    for (int i = 0; i < studente->numero_voti; i++) {
        somma += studente->voti[i];
    }
    studente->media = somma / studente->numero_voti;
    
    // Aggiorna stato
    aggiorna_stato_studente(studente);
    
    printf("✅ Voto %.1f aggiunto! Nuova media: %.2f (%s)\n", 
           voto, studente->media, studente->stato);
}

void aggiorna_stato_studente(Studente *studente) {
    if (studente->numero_voti == 0) {
        strcpy(studente->stato, "In corso");
    } else if (studente->numero_voti >= 5) {  // Almeno 5 voti per decidere
        if (studente->media >= 6.0) {
            strcpy(studente->stato, "Promosso");
        } else {
            strcpy(studente->stato, "Bocciato");
        }
    } else {
        strcpy(studente->stato, "In corso");
    }
}

void stampa_pagella(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente registrato.\n");
        return;
    }
    
    int id;
    printf("🆔 ID studente per pagella: ");
    scanf("%d", &id);
    
    Studente *s = NULL;
    for (int i = 0; i < sistema->numero_studenti; i++) {
        if (sistema->studenti[i].id == id) {
            s = &sistema->studenti[i];
            break;
        }
    }
    
    if (s == NULL) {
        printf("❌ Studente non trovato!\n");
        return;
    }
    
    printf("\n" "╔══════════════════════════════════════════════════════════════╗\n");
    printf("║                           PAGELLA                            ║\n");
    printf("║                        ITS INFORMATICA                      ║\n");
    printf("╠══════════════════════════════════════════════════════════════╣\n");
    printf("║ Studente: %-20s %-20s        ║\n", s->nome, s->cognome);
    printf("║ ID: %-3d                           Età: %-3d anni         ║\n", s->id, s->eta);
    printf("╠══════════════════════════════════════════════════════════════╣\n");
    printf("║ VOTI:                                                        ║\n");
    
    if (s->numero_voti == 0) {
        printf("║ Nessun voto registrato                                      ║\n");
    } else {
        printf("║ ");
        for (int i = 0; i < s->numero_voti; i++) {
            printf("%.1f  ", s->voti[i]);
        }
        for (int i = s->numero_voti; i < 10; i++) {
            printf("     ");
        }
        printf("║\n");
        printf("║                                                              ║\n");
        printf("║ MEDIA GENERALE: %-6.2f                                    ║\n", s->media);
    }
    
    printf("║                                                              ║\n");
    printf("║ STATO: %-20s                                ║\n", s->stato);
    printf("╚══════════════════════════════════════════════════════════════╝\n");
}

void calcola_statistiche_classe(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente per le statistiche.\n");
        return;
    }
    
    int promossi = 0, bocciati = 0, in_corso = 0;
    float somma_medie = 0;
    int studenti_con_voti = 0;
    float media_piu_alta = 0, media_piu_bassa = 11;
    char nome_migliore[MAX_NOME], nome_peggiore[MAX_NOME];
    
    for (int i = 0; i < sistema->numero_studenti; i++) {
        Studente *s = &sistema->studenti[i];
        
        if (strcmp(s->stato, "Promosso") == 0) promossi++;
        else if (strcmp(s->stato, "Bocciato") == 0) bocciati++;
        else in_corso++;
        
        if (s->numero_voti > 0) {
            somma_medie += s->media;
            studenti_con_voti++;
            
            if (s->media > media_piu_alta) {
                media_piu_alta = s->media;
                strcpy(nome_migliore, s->nome);
                strcat(nome_migliore, " ");
                strcat(nome_migliore, s->cognome);
            }
            
            if (s->media < media_piu_bassa) {
                media_piu_bassa = s->media;
                strcpy(nome_peggiore, s->nome);
                strcat(nome_peggiore, " ");
                strcat(nome_peggiore, s->cognome);
            }
        }
    }
    
    printf("\n📈 === STATISTICHE CLASSE ===\n");
    printf("👥 Totale studenti: %d\n", sistema->numero_studenti);
    printf("✅ Promossi: %d (%.1f%%)\n", promossi, 
           (float)promossi / sistema->numero_studenti * 100);
    printf("❌ Bocciati: %d (%.1f%%)\n", bocciati,
           (float)bocciati / sistema->numero_studenti * 100);
    printf("⏳ In corso: %d (%.1f%%)\n", in_corso,
           (float)in_corso / sistema->numero_studenti * 100);
    
    if (studenti_con_voti > 0) {
        float media_classe = somma_medie / studenti_con_voti;
        printf("\n📊 MEDIE:\n");
        printf("📈 Media classe: %.2f\n", media_classe);
        printf("🏆 Media più alta: %.2f (%s)\n", media_piu_alta, nome_migliore);
        printf("📉 Media più bassa: %.2f (%s)\n", media_piu_bassa, nome_peggiore);
    }
}

void elimina_studente(SistemaStudenti *sistema) {
    if (sistema->numero_studenti == 0) {
        printf("📭 Nessuno studente da eliminare.\n");
        return;
    }
    
    int id;
    printf("🆔 ID studente da eliminare: ");
    scanf("%d", &id);
    
    int indice = -1;
    for (int i = 0; i < sistema->numero_studenti; i++) {
        if (sistema->studenti[i].id == id) {
            indice = i;
            break;
        }
    }
    
    if (indice == -1) {
        printf("❌ Studente con ID %d non trovato!\n", id);
        return;
    }
    
    Studente *s = &sistema->studenti[indice];
    printf("⚠️  Sei sicuro di voler eliminare %s %s? (s/n): ", s->nome, s->cognome);
    
    char conferma;
    scanf(" %c", &conferma);
    
    if (conferma == 's' || conferma == 'S') {
        // Sposta tutti gli studenti successivi indietro di una posizione
        for (int i = indice; i < sistema->numero_studenti - 1; i++) {
            sistema->studenti[i] = sistema->studenti[i + 1];
        }
        
        sistema->numero_studenti--;
        printf("✅ Studente eliminato con successo!\n");
    } else {
        printf("❌ Eliminazione annullata.\n");
    }
}

void salva_sistema(SistemaStudenti *sistema) {
    FILE *file = fopen(FILE_STUDENTI, "wb");
    
    if (file == NULL) {
        printf("❌ Errore nell'apertura del file per il salvataggio!\n");
        return;
    }
    
    // Salva prima i metadati del sistema
    fwrite(&sistema->numero_studenti, sizeof(int), 1, file);
    fwrite(&sistema->prossimo_id, sizeof(int), 1, file);
    
    // Salva tutti gli studenti
    fwrite(sistema->studenti, sizeof(Studente), sistema->numero_studenti, file);
    
    fclose(file);
}

int carica_sistema(SistemaStudenti *sistema) {
    FILE *file = fopen(FILE_STUDENTI, "rb");
    
    if (file == NULL) {
        return 0;  // File non esiste
    }
    
    // Carica metadati
    if (fread(&sistema->numero_studenti, sizeof(int), 1, file) != 1) {
        fclose(file);
        return 0;
    }
    
    if (fread(&sistema->prossimo_id, sizeof(int), 1, file) != 1) {
        fclose(file);
        return 0;
    }
    
    // Carica studenti
    if (fread(sistema->studenti, sizeof(Studente), 
              sistema->numero_studenti, file) != sistema->numero_studenti) {
        fclose(file);
        return 0;
    }
    
    fclose(file);
    return 1;  // Successo
}
```

---

## 🎯 Progetto 2: Gioco "Indovina la Parola"

### Un gioco completo con livelli di difficoltà e punteggi:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

#define MAX_PAROLA 20
#define MAX_PAROLE 50
#define MAX_TENTATIVI 6
#define FILE_PUNTEGGI "punteggi.txt"
#define FILE_PAROLE "parole.txt"

typedef struct {
    char nome[30];
    int punteggio;
    char livello[15];
} Giocatore;

// Parole per i diversi livelli
char parole_facili[][MAX_PAROLA] = {
    "CASA", "CANE", "GATTO", "SOLE", "LUNA", "MARE", "NEVE", "FIORE"
};

char parole_medie[][MAX_PAROLA] = {
    "COMPUTER", "TELEFONO", "STUDIARE", "PROGRAMMA", "INTERNET", "SISTEMA"
};

char parole_difficili[][MAX_PAROLA] = {
    "PROGRAMMAZIONE", "INFORMATICA", "TECNOLOGIA", "INTELLIGENZA", "ALGORITMO"
};

// Prototipi
void menu_principale(void);
void nuova_partita(void);
void mostra_classifica(void);
void gioca_partita(char *parola, int livello);
void inizializza_parola_nascosta(char *parola, char *nascosta);
int aggiorna_parola_nascosta(char *parola, char *nascosta, char lettera);
void disegna_impiccato(int errori);
void salva_punteggio(char *nome, int punteggio, char *livello);
void carica_e_mostra_classifica(void);
int calcola_punteggio(int lunghezza_parola, int errori, int livello);

int main() {
    srand(time(NULL));
    
    printf("🎮 === GIOCO DELL'IMPICCATO === 🎮\n\n");
    
    int scelta;
    do {
        menu_principale();
        printf("➤ Scegli opzione: ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                nuova_partita();
                break;
            case 2:
                mostra_classifica();
                break;
            case 3:
                printf("👋 Grazie per aver giocato!\n");
                break;
            default:
                printf("❌ Opzione non valida!\n");
        }
        
        if (scelta != 3) {
            printf("\n🔄 Premi INVIO per continuare...");
            getchar();
            getchar();
        }
        
    } while (scelta != 3);
    
    return 0;
}

void menu_principale(void) {
    printf("\n" "════════════════════════════════════════════════\n");
    printf("🏠 MENU PRINCIPALE\n");
    printf("════════════════════════════════════════════════\n");
    printf("1️⃣  Nuova Partita\n");
    printf("2️⃣  Classifica\n");
    printf("3️⃣  Esci\n");
    printf("════════════════════════════════════════════════\n");
}

void nuova_partita(void) {
    int livello;
    char *parola;
    
    printf("\n🎯 === SCEGLI DIFFICOLTÀ ===\n");
    printf("1️⃣  Facile (4-5 lettere) - 100 punti base\n");
    printf("2️⃣  Medio (6-8 lettere) - 200 punti base\n");
    printf("3️⃣  Difficile (9+ lettere) - 300 punti base\n");
    
    do {
        printf("➤ Livello (1-3): ");
        scanf("%d", &livello);
        
        if (livello < 1 || livello > 3) {
            printf("❌ Livello non valido!\n");
        }
    } while (livello < 1 || livello > 3);
    
    // Seleziona parola casuale in base al livello
    switch (livello) {
        case 1:
            parola = parole_facili[rand() % 8];
            break;
        case 2:
            parola = parole_medie[rand() % 6];
            break;
        case 3:
            parola = parole_difficili[rand() % 5];
            break;
    }
    
    gioca_partita(parola, livello);
}

void gioca_partita(char *parola, int livello) {
    char nascosta[MAX_PAROLA];
    char lettere_provate[26] = {0};
    int errori = 0;
    int lettere_indovinate = 0;
    char lettera;
    int lunghezza = strlen(parola);
    
    inizializza_parola_nascosta(parola, nascosta);
    
    printf("\n🎮 === PARTITA INIZIATA ===\n");
    printf("📏 Parola di %d lettere\n", lunghezza);
    printf("❤️  Hai %d vite\n\n", MAX_TENTATIVI);
    
    while (errori < MAX_TENTATIVI && lettere_indovinate < lunghezza) {
        printf("Parola: %s\n", nascosta);
        printf("Errori: %d/%d\n", errori, MAX_TENTATIVI);
        
        if (errori > 0) {
            disegna_impiccato(errori);
        }
        
        printf("Lettere provate: ");
        for (int i = 0; i < 26; i++) {
            if (lettere_provate[i]) {
                printf("%c ", 'A' + i);
            }
        }
        printf("\n");
        
        do {
            printf("🔤 Inserisci una lettera: ");
            scanf(" %c", &lettera);
            lettera = toupper(lettera);
            
            if (lettera < 'A' || lettera > 'Z') {
                printf("❌ Inserisci solo lettere!\n");
                continue;
            }
            
            if (lettere_provate[lettera - 'A']) {
                printf("❌ Lettera già provata!\n");
                continue;
            }
            
            break;
        } while (1);
        
        lettere_provate[lettera - 'A'] = 1;
        
        if (aggiorna_parola_nascosta(parola, nascosta, lettera)) {
            printf("✅ Bravo! La lettera '%c' c'è!\n\n", lettera);
            
            // Conta lettere indovinate
            lettere_indovinate = 0;
            for (int i = 0; i < lunghezza; i++) {
                if (nascosta[i] != '_') {
                    lettere_indovinate++;
                }
            }
        } else {
            errori++;
            printf("❌ La lettera '%c' non c'è! (%d/%d)\n\n", 
                   lettera, errori, MAX_TENTATIVI);
        }
    }
    
    // Fine partita
    printf("════════════════════════════════════════════════\n");
    if (lettere_indovinate == lunghezza) {
        int punteggio = calcola_punteggio(lunghezza, errori, livello);
        printf("🎉 CONGRATULAZIONI! HAI VINTO! 🎉\n");
        printf("📝 La parola era: %s\n", parola);
        printf("🏆 Punteggio: %d punti\n", punteggio);
        
        // Salva punteggio
        char nome[30];
        printf("👤 Inserisci il tuo nome: ");
        scanf("%29s", nome);
        
        char livello_str[15];
        switch (livello) {
            case 1: strcpy(livello_str, "Facile"); break;
            case 2: strcpy(livello_str, "Medio"); break;
            case 3: strcpy(livello_str, "Difficile"); break;
        }
        
        salva_punteggio(nome, punteggio, livello_str);
        printf("💾 Punteggio salvato!\n");
        
    } else {
        printf("💀 HAI PERSO! 💀\n");
        printf("📝 La parola era: %s\n", parola);
        disegna_impiccato(MAX_TENTATIVI);
        printf("🔄 Ritenta! Puoi farcela!\n");
    }
    printf("════════════════════════════════════════════════\n");
}

void inizializza_parola_nascosta(char *parola, char *nascosta) {
    int lunghezza = strlen(parola);
    for (int i = 0; i < lunghezza; i++) {
        nascosta[i] = '_';
    }
    nascosta[lunghezza] = '\0';
}

int aggiorna_parola_nascosta(char *parola, char *nascosta, char lettera) {
    int trovata = 0;
    int lunghezza = strlen(parola);
    
    for (int i = 0; i < lunghezza; i++) {
        if (parola[i] == lettera) {
            nascosta[i] = lettera;
            trovata = 1;
        }
    }
    
    return trovata;
}

void disegna_impiccato(int errori) {
    printf("\n");
    printf("  +---+\n");
    printf("  |   |\n");
    
    switch (errori) {
        case 0:
            printf("      |\n");
            printf("      |\n");
            printf("      |\n");
            break;
        case 1:
            printf("  O   |\n");
            printf("      |\n");
            printf("      |\n");
            break;
        case 2:
            printf("  O   |\n");
            printf("  |   |\n");
            printf("      |\n");
            break;
        case 3:
            printf("  O   |\n");
            printf(" /|   |\n");
            printf("      |\n");
            break;
        case 4:
            printf("  O   |\n");
            printf(" /|\\  |\n");
            printf("      |\n");
            break;
        case 5:
            printf("  O   |\n");
            printf(" /|\\  |\n");
            printf(" /    |\n");
            break;
        case 6:
            printf("  O   |\n");
            printf(" /|\\  |\n");
            printf(" / \\  |\n");
            break;
    }
    
    printf("      |\n");
    printf("=========\n\n");
}

int calcola_punteggio(int lunghezza_parola, int errori, int livello) {
    int punteggio_base = livello * 100;  // 100, 200, o 300
    int bonus_lunghezza = lunghezza_parola * 10;
    int malus_errori = errori * 20;
    
    int punteggio_finale = punteggio_base + bonus_lunghezza - malus_errori;
    
    return (punteggio_finale > 0) ? punteggio_finale : 10;  // Minimo 10 punti
}

void salva_punteggio(char *nome, int punteggio, char *livello) {
    FILE *file = fopen(FILE_PUNTEGGI, "a");
    
    if (file == NULL) {
        printf("❌ Errore nel salvataggio del punteggio\n");
        return;
    }
    
    fprintf(file, "%s,%d,%s\n", nome, punteggio, livello);
    fclose(file);
}

void mostra_classifica(void) {
    FILE *file = fopen(FILE_PUNTEGGI, "r");
    Giocatore giocatori[100];
    int numero_giocatori = 0;
    
    if (file == NULL) {
        printf("📊 Nessun punteggio salvato ancora.\n");
        return;
    }
    
    // Carica tutti i punteggi
    while (numero_giocatori < 100 && 
           fscanf(file, "%29[^,],%d,%14s\n", 
                  giocatori[numero_giocatori].nome,
                  &giocatori[numero_giocatori].punteggio,
                  giocatori[numero_giocatori].livello) == 3) {
        numero_giocatori++;
    }
    fclose(file);
    
    if (numero_giocatori == 0) {
        printf("📊 Nessun punteggio trovato.\n");
        return;
    }
    
    // Ordina per punteggio (bubble sort semplice)
    for (int i = 0; i < numero_giocatori - 1; i++) {
        for (int j = 0; j < numero_giocatori - i - 1; j++) {
            if (giocatori[j].punteggio < giocatori[j + 1].punteggio) {
                Giocatore temp = giocatori[j];
                giocatori[j] = giocatori[j + 1];
                giocatori[j + 1] = temp;
            }
        }
    }
    
    printf("\n🏆 === CLASSIFICA === 🏆\n");
    printf("Pos %-20s %-10s %s\n", "Nome", "Punteggio", "Livello");
    printf("──────────────────────────────────────────────\n");
    
    int da_mostrare = (numero_giocatori > 10) ? 10 : numero_giocatori;
    
    for (int i = 0; i < da_mostrare; i++) {
        char medaglia[5] = "";
        if (i == 0) strcpy(medaglia, "🥇");
        else if (i == 1) strcpy(medaglia, "🥈");
        else if (i == 2) strcpy(medaglia, "🥉");
        
        printf("%-2d%s %-20s %-10d %s\n", 
               i + 1, medaglia, giocatori[i].nome, 
               giocatori[i].punteggio, giocatori[i].livello);
    }
    
    printf("──────────────────────────────────────────────\n");
    printf("Totale partite giocate: %d\n", numero_giocatori);
}
```

---

## 🎯 Progetto 3: Calcolatrice Scientifica Avanzata

### Una calcolatrice completa con funzioni matematiche:

```c
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define PI 3.141592653589793

void menu_principale(void);
void operazioni_base(void);
void operazioni_avanzate(void);
void conversioni(void);
void calcolatrice_interattiva(void);

int main() {
    printf("🧮 === CALCOLATRICE SCIENTIFICA === 🧮\n\n");
    
    int scelta;
    do {
        menu_principale();
        printf("➤ Scegli categoria: ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                operazioni_base();
                break;
            case 2:
                operazioni_avanzate();
                break;
            case 3:
                conversioni();
                break;
            case 4:
                calcolatrice_interattiva();
                break;
            case 5:
                printf("👋 Calcolatrice chiusa!\n");
                break;
            default:
                printf("❌ Opzione non valida!\n");
        }
        
        if (scelta != 5) {
            printf("\n🔄 Premi INVIO per continuare...");
            getchar();
            getchar();
        }
        
    } while (scelta != 5);
    
    return 0;
}

void menu_principale(void) {
    printf("\n" "═══════════════════════════════════════════════\n");
    printf("📋 MENU CALCOLATRICE\n");
    printf("═══════════════════════════════════════════════\n");
    printf("1️⃣  Operazioni Base (+, -, ×, ÷)\n");
    printf("2️⃣  Operazioni Avanzate (potenze, radici, log)\n");
    printf("3️⃣  Conversioni (temperatura, distanza, peso)\n");
    printf("4️⃣  Modalità Interattiva\n");
    printf("5️⃣  Esci\n");
    printf("═══════════════════════════════════════════════\n");
}

void operazioni_base(void) {
    double num1, num2, risultato;
    int operazione;
    
    printf("\n➕ === OPERAZIONI BASE ===\n");
    printf("1. Addizione (+)\n");
    printf("2. Sottrazione (-)\n");
    printf("3. Moltiplicazione (×)\n");
    printf("4. Divisione (÷)\n");
    printf("5. Modulo (resto)\n");
    
    printf("➤ Scegli operazione: ");
    scanf("%d", &operazione);
    
    printf("Inserisci primo numero: ");
    scanf("%lf", &num1);
    printf("Inserisci secondo numero: ");
    scanf("%lf", &num2);
    
    switch (operazione) {
        case 1:
            risultato = num1 + num2;
            printf("📊 %.3f + %.3f = %.3f\n", num1, num2, risultato);
            break;
        case 2:
            risultato = num1 - num2;
            printf("📊 %.3f - %.3f = %.3f\n", num1, num2, risultato);
            break;
        case 3:
            risultato = num1 * num2;
            printf("📊 %.3f × %.3f = %.3f\n", num1, num2, risultato);
            break;
        case 4:
            if (num2 != 0) {
                risultato = num1 / num2;
                printf("📊 %.3f ÷ %.3f = %.3f\n", num1, num2, risultato);
            } else {
                printf("❌ Errore: Divisione per zero!\n");
            }
            break;
        case 5:
            if (num2 != 0) {
                risultato = fmod(num1, num2);
                printf("📊 %.3f mod %.3f = %.3f\n", num1, num2, risultato);
            } else {
                printf("❌ Errore: Modulo per zero!\n");
            }
            break;
        default:
            printf("❌ Operazione non valida!\n");
    }
}

void operazioni_avanzate(void) {
    double numero, risultato;
    int operazione;
    
    printf("\n🔬 === OPERAZIONI AVANZATE ===\n");
    printf("1. Potenza al quadrato (x²)\n");
    printf("2. Potenza al cubo (x³)\n");
    printf("3. Radice quadrata (√x)\n");
    printf("4. Potenza personalizzata (x^y)\n");
    printf("5. Logaritmo naturale (ln)\n");
    printf("6. Logaritmo base 10 (log₁₀)\n");
    printf("7. Seno (sin)\n");
    printf("8. Coseno (cos)\n");
    printf("9. Tangente (tan)\n");
    printf("10. Fattoriale (n!)\n");
    
    printf("➤ Scegli operazione: ");
    scanf("%d", &operazione);
    
    switch (operazione) {
        case 1:
            printf("Inserisci numero: ");
            scanf("%lf", &numero);
            risultato = numero * numero;
            printf("📊 %.3f² = %.3f\n", numero, risultato);
            break;
            
        case 2:
            printf("Inserisci numero: ");
            scanf("%lf", &numero);
            risultato = numero * numero * numero;
            printf("📊 %.3f³ = %.3f\n", numero, risultato);
            break;
            
        case 3:
            printf("Inserisci numero: ");
            scanf("%lf", &numero);
            if (numero >= 0) {
                risultato = sqrt(numero);
                printf("📊 √%.3f = %.3f\n", numero, risultato);
            } else {
                printf("❌ Impossibile calcolare radice di numero negativo!\n");
            }
            break;
            
        case 4: {
            double base, esponente;
            printf("Inserisci base: ");
            scanf("%lf", &base);
            printf("Inserisci esponente: ");
            scanf("%lf", &esponente);
            risultato = pow(base, esponente);
            printf("📊 %.3f^%.3f = %.3f\n", base, esponente, risultato);
            break;
        }
        
        case 5:
            printf("Inserisci numero: ");
            scanf("%lf", &numero);
            if (numero > 0) {
                risultato = log(numero);
                printf("📊 ln(%.3f) = %.3f\n", numero, risultato);
            } else {
                printf("❌ Logaritmo definito solo per numeri positivi!\n");
            }
            break;
            
        case 6:
            printf("Inserisci numero: ");
            scanf("%lf", &numero);
            if (numero > 0) {
                risultato = log10(numero);
                printf("📊 log₁₀(%.3f) = %.3f\n", numero, risultato);
            } else {
                printf("❌ Logaritmo definito solo per numeri positivi!\n");
            }
            break;
            
        case 7:
            printf("Inserisci angolo in gradi: ");
            scanf("%lf", &numero);
            risultato = sin(numero * PI / 180);  // Converte in radianti
            printf("📊 sin(%.1f°) = %.3f\n", numero, risultato);
            break;
            
        case 8:
            printf("Inserisci angolo in gradi: ");
            scanf("%lf", &numero);
            risultato = cos(numero * PI / 180);
            printf("📊 cos(%.1f°) = %.3f\n", numero, risultato);
            break;
            
        case 9:
            printf("Inserisci angolo in gradi: ");
            scanf("%lf", &numero);
            risultato = tan(numero * PI / 180);
            printf("📊 tan(%.1f°) = %.3f\n", numero, risultato);
            break;
            
        case 10:
            printf("Inserisci numero intero: ");
            int n;
            scanf("%d", &n);
            if (n >= 0 && n <= 20) {  // Limite per evitare overflow
                long long fattoriale = 1;
                for (int i = 1; i <= n; i++) {
                    fattoriale *= i;
                }
                printf("📊 %d! = %lld\n", n, fattoriale);
            } else {
                printf("❌ Fattoriale calcolabile solo per 0 ≤ n ≤ 20!\n");
            }
            break;
            
        default:
            printf("❌ Operazione non valida!\n");
    }
}

void conversioni(void) {
    int categoria, tipo;
    double valore, risultato;
    
    printf("\n🔄 === CONVERSIONI ===\n");
    printf("1. Temperature\n");
    printf("2. Distanze\n");
    printf("3. Pesi\n");
    printf("4. Valute (tassi fissi di esempio)\n");
    
    printf("➤ Scegli categoria: ");
    scanf("%d", &categoria);
    
    switch (categoria) {
        case 1:
            printf("\n🌡️ Temperature:\n");
            printf("1. Celsius → Fahrenheit\n");
            printf("2. Fahrenheit → Celsius\n");
            printf("3. Celsius → Kelvin\n");
            printf("4. Kelvin → Celsius\n");
            
            printf("➤ Conversione: ");
            scanf("%d", &tipo);
            printf("Inserisci valore: ");
            scanf("%lf", &valore);
            
            switch (tipo) {
                case 1:
                    risultato = (valore * 9.0 / 5.0) + 32;
                    printf("📊 %.1f°C = %.1f°F\n", valore, risultato);
                    break;
                case 2:
                    risultato = (valore - 32) * 5.0 / 9.0;
                    printf("📊 %.1f°F = %.1f°C\n", valore, risultato);
                    break;
                case 3:
                    risultato = valore + 273.15;
                    printf("📊 %.1f°C = %.1fK\n", valore, risultato);
                    break;
                case 4:
                    risultato = valore - 273.15;
                    printf("📊 %.1fK = %.1f°C\n", valore, risultato);
                    break;
                default:
                    printf("❌ Tipo non valido!\n");
            }
            break;
            
        case 2:
            printf("\n📏 Distanze:\n");
            printf("1. Metri → Chilometri\n");
            printf("2. Chilometri → Metri\n");
            printf("3. Metri → Miglia\n");
            printf("4. Miglia → Metri\n");
            printf("5. Centimetri → Pollici\n");
            printf("6. Pollici → Centimetri\n");
            
            printf("➤ Conversione: ");
            scanf("%d", &tipo);
            printf("Inserisci valore: ");
            scanf("%lf", &valore);
            
            switch (tipo) {
                case 1:
                    risultato = valore / 1000;
                    printf("📊 %.3f m = %.3f km\n", valore, risultato);
                    break;
                case 2:
                    risultato = valore * 1000;
                    printf("📊 %.3f km = %.3f m\n", valore, risultato);
                    break;
                case 3:
                    risultato = valore / 1609.34;
                    printf("📊 %.3f m = %.3f miglia\n", valore, risultato);
                    break;
                case 4:
                    risultato = valore * 1609.34;
                    printf("📊 %.3f miglia = %.3f m\n", valore, risultato);
                    break;
                case 5:
                    risultato = valore / 2.54;
                    printf("📊 %.3f cm = %.3f pollici\n", valore, risultato);
                    break;
                case 6:
                    risultato = valore * 2.54;
                    printf("📊 %.3f pollici = %.3f cm\n", valore, risultato);
                    break;
                default:
                    printf("❌ Tipo non valido!\n");
            }
            break;
            
        case 3:
            printf("\n⚖️ Pesi:\n");
            printf("1. Chilogrammi → Libbre\n");
            printf("2. Libbre → Chilogrammi\n");
            printf("3. Grammi → Once\n");
            printf("4. Once → Grammi\n");
            
            printf("➤ Conversione: ");
            scanf("%d", &tipo);
            printf("Inserisci valore: ");
            scanf("%lf", &valore);
            
            switch (tipo) {
                case 1:
                    risultato = valore * 2.20462;
                    printf("📊 %.3f kg = %.3f lbs\n", valore, risultato);
                    break;
                case 2:
                    risultato = valore / 2.20462;
                    printf("📊 %.3f lbs = %.3f kg\n", valore, risultato);
                    break;
                case 3:
                    risultato = valore / 28.3495;
                    printf("📊 %.3f g = %.3f oz\n", valore, risultato);
                    break;
                case 4:
                    risultato = valore * 28.3495;
                    printf("📊 %.3f oz = %.3f g\n", valore, risultato);
                    break;
                default:
                    printf("❌ Tipo non valido!\n");
            }
            break;
            
        case 4:
            printf("\n💰 Valute (tassi di esempio):\n");
            printf("1. Euro → Dollaro USA (1.10)\n");
            printf("2. Dollaro USA → Euro (0.91)\n");
            printf("3. Euro → Sterlina (0.85)\n");
            printf("4. Sterlina → Euro (1.18)\n");
            
            printf("➤ Conversione: ");
            scanf("%d", &tipo);
            printf("Inserisci valore: ");
            scanf("%lf", &valore);
            
            switch (tipo) {
                case 1:
                    risultato = valore * 1.10;
                    printf("📊 %.2f € = %.2f $\n", valore, risultato);
                    break;
                case 2:
                    risultato = valore * 0.91;
                    printf("📊 %.2f $ = %.2f €\n", valore, risultato);
                    break;
                case 3:
                    risultato = valore * 0.85;
                    printf("📊 %.2f € = %.2f £\n", valore, risultato);
                    break;
                case 4:
                    risultato = valore * 1.18;
                    printf("📊 %.2f £ = %.2f €\n", valore, risultato);
                    break;
                default:
                    printf("❌ Tipo non valido!\n");
            }
            break;
            
        default:
            printf("❌ Categoria non valida!\n");
    }
}

void calcolatrice_interattiva(void) {
    double risultato = 0;
    double numero;
    char operazione;
    int prima_operazione = 1;
    
    printf("\n🔢 === MODALITÀ INTERATTIVA ===\n");
    printf("💡 Comandi disponibili:\n");
    printf("   +, -, *, / : operazioni base\n");
    printf("   ^ : potenza\n");
    printf("   s : radice quadrata\n");
    printf("   c : clear (azzera)\n");
    printf("   q : quit (esci)\n\n");
    
    printf("Risultato: %.3f\n", risultato);
    
    while (1) {
        printf("➤ ");
        scanf(" %c", &operazione);
        
        if (operazione == 'q' || operazione == 'Q') {
            printf("👋 Modalità interattiva terminata!\n");
            break;
        }
        
        if (operazione == 'c' || operazione == 'C') {
            risultato = 0;
            prima_operazione = 1;
            printf("🗑️ Azzerato! Risultato: %.3f\n", risultato);
            continue;
        }
        
        if (operazione == 's' || operazione == 'S') {
            if (risultato >= 0) {
                risultato = sqrt(risultato);
                printf("√ Risultato: %.3f\n", risultato);
            } else {
                printf("❌ Impossibile calcolare radice di numero negativo!\n");
            }
            continue;
        }
        
        if (prima_operazione) {
            printf("Inserisci numero iniziale: ");
            scanf("%lf", &risultato);
            printf("Risultato: %.3f\n", risultato);
            prima_operazione = 0;
            continue;
        }
        
        printf("Inserisci numero: ");
        scanf("%lf", &numero);
        
        switch (operazione) {
            case '+':
                risultato += numero;
                printf("+ Risultato: %.3f\n", risultato);
                break;
            case '-':
                risultato -= numero;
                printf("- Risultato: %.3f\n", risultato);
                break;
            case '*':
                risultato *= numero;
                printf("× Risultato: %.3f\n", risultato);
                break;
            case '/':
                if (numero != 0) {
                    risultato /= numero;
                    printf("÷ Risultato: %.3f\n", risultato);
                } else {
                    printf("❌ Divisione per zero!\n");
                }
                break;
            case '^':
                risultato = pow(risultato, numero);
                printf("^ Risultato: %.3f\n", risultato);
                break;
            default:
                printf("❌ Operazione non riconosciuta!\n");
        }
    }
}
```

---

## 9.3 Congratulazioni! 🎉

### Hai Completato il Corso!

🏆 **Competenze Acquisite:**
- Programmazione strutturata in C
- Gestione di variabili, array e stringhe
- Controllo del flusso (if, cicli)
- Funzioni e modularità
- Puntatori e gestione memoria
- Input/Output e file
- Sviluppo di progetti completi

🚀 **Cosa Puoi Fare Ora:**
- Sviluppare applicazioni desktop semplici
- Creare sistemi di gestione dati
- Implementare algoritmi matematici
- Lavorare con file e database
- Progettare giochi testuali
- Preparare la base per linguaggi avanzati

📚 **Prossimi Passi Consigliati:**
1. **C++**: Programmazione orientata agli oggetti
2. **Python**: Sviluppo rapido e data science
3. **Java**: Applicazioni enterprise
4. **JavaScript**: Sviluppo web
5. **SQL**: Database e gestione dati
6. **Git**: Controllo versione del codice

### 🎯 Sfide Bonus

**Sfida 1**: Migliora uno dei progetti con nuove funzionalità
**Sfida 2**: Crea un progetto completamente nuovo
**Sfida 3**: Ottimizza il codice per prestazioni migliori
**Sfida 4**: Aggiungi interfacce grafiche semplici

### 📋 Portfolio Progetti

Hai ora un portfolio di progetti che puoi mostrare:
- ✅ Sistema gestione studenti
- ✅ Gioco dell'impiccato
- ✅ Calcolatrice scientifica
- ✅ Sistema biblioteca
- ✅ Gestione magazzino
- ✅ E molti altri mini-progetti!

---

**🎓 Complimenti per aver completato il Corso di Programmazione C per ITS Informatica!**

*Continua a programmare, sperimentare e imparare. Il mondo della programmazione è infinito e pieno di opportunità!*
