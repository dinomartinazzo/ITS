# Modulo 8: File e Input/Output
## ITS Informatica - Livello Base

---

## Obiettivi del Modulo
Al termine di questo modulo sarai in grado di:
- Capire cosa sono i file e perché sono utili
- Aprire, leggere e scrivere file di testo
- Salvare e caricare dati dai programmi
- Gestire errori nell'apertura dei file
- Creare sistemi di archiviazione semplici
- Lavorare con file CSV per dati strutturati

---

## 8.1 Perché i File?

Fino ad ora i tuoi programmi "dimenticavano" tutto quando finivano. I **file** permettono di:

### 💾 **Salvare Dati Permanenti**
```
Senza file:          Con file:
Programma inizia  →  Programma inizia
Inserisci dati    →  Carica dati dal file
Lavora sui dati   →  Lavora sui dati  
Programma finisce →  Salva dati nel file
TUTTO PERSO! ❌     TUTTO SALVATO! ✅
```

### Esempi di Utilizzo:
- 📝 Salvare la lista della spesa
- 🎓 Memorizzare i voti degli studenti
- 💰 Tenere traccia delle spese
- 🎮 Salvare i progressi di un gioco
- 📊 Esportare dati per Excel

---

## 8.2 Il Primo File: Scrittura

### Esempio Semplicissimo:
```c
#include <stdio.h>

int main() {
    FILE *file;  // "Maniglia" per il file
    
    // Apre file in scrittura ("w" = write)
    file = fopen("saluto.txt", "w");
    
    if (file == NULL) {
        printf("Errore: impossibile creare il file!\n");
        return 1;
    }
    
    // Scrive nel file (come printf, ma nel file)
    fprintf(file, "Ciao mondo!\n");
    fprintf(file, "Questo è il mio primo file.\n");
    fprintf(file, "Oggi ho imparato a scrivere file in C!\n");
    
    // IMPORTANTE: Chiude sempre il file!
    fclose(file);
    
    printf("File 'saluto.txt' creato con successo!\n");
    return 0;
}
```

**Dopo aver eseguito il programma, troverai un file `saluto.txt` con:**
```
Ciao mondo!
Questo è il mio primo file.
Oggi ho imparato a scrivere file in C!
```

---

## 8.3 Leggere da un File

### Leggere Riga per Riga:
```c
#include <stdio.h>

int main() {
    FILE *file;
    char riga[100];  // Buffer per leggere le righe
    
    // Apre file in lettura ("r" = read)
    file = fopen("saluto.txt", "r");
    
    if (file == NULL) {
        printf("Errore: file non trovato!\n");
        return 1;
    }
    
    printf("Contenuto del file:\n");
    printf("===================\n");
    
    // Legge riga per riga finché non finisce il file
    while (fgets(riga, sizeof(riga), file) != NULL) {
        printf("%s", riga);  // Stampa la riga (già ha \n)
    }
    
    fclose(file);
    return 0;
}
```

### Contare le Righe di un File:
```c
#include <stdio.h>

int main() {
    FILE *file;
    char riga[100];
    int numero_righe = 0;
    
    file = fopen("saluto.txt", "r");
    
    if (file == NULL) {
        printf("File non trovato!\n");
        return 1;
    }
    
    // Conta le righe
    while (fgets(riga, sizeof(riga), file) != NULL) {
        numero_righe++;
    }
    
    fclose(file);
    
    printf("Il file ha %d righe.\n", numero_righe);
    return 0;
}
```

---

## 8.4 Modi di Apertura dei File

| Modo | Significato | Cosa fa |
|------|-------------|---------|
| `"r"` | Read (lettura) | Legge file esistente |
| `"w"` | Write (scrittura) | Crea nuovo file (sovrascrive) |
| `"a"` | Append (aggiungi) | Aggiunge alla fine |
| `"r+"` | Read+Write | Legge e scrive file esistente |

### Esempio con Append:
```c
#include <stdio.h>

int main() {
    FILE *file;
    char messaggio[100];
    
    printf("Scrivi un messaggio da aggiungere al file: ");
    fgets(messaggio, sizeof(messaggio), stdin);
    
    // Apre in modalità "append" - aggiunge alla fine
    file = fopen("diario.txt", "a");
    
    if (file == NULL) {
        printf("Errore nell'apertura del file!\n");
        return 1;
    }
    
    fprintf(file, "Data: oggi - %s", messaggio);
    
    fclose(file);
    
    printf("Messaggio aggiunto al diario!\n");
    return 0;
}
```

---

## 8.5 Salvare e Caricare Dati Strutturati

### Salvare Array di Numeri:
```c
#include <stdio.h>

int main() {
    int voti[] = {8, 7, 9, 6, 8, 7, 10};
    int dimensione = 7;
    FILE *file;
    
    // Salva i voti nel file
    file = fopen("voti.txt", "w");
    if (file == NULL) {
        printf("Errore nella creazione del file!\n");
        return 1;
    }
    
    fprintf(file, "%d\n", dimensione);  // Prima riga: quanti voti
    
    for (int i = 0; i < dimensione; i++) {
        fprintf(file, "%d\n", voti[i]);  // Un voto per riga
    }
    
    fclose(file);
    printf("Voti salvati nel file 'voti.txt'\n");
    
    return 0;
}
```

### Caricare Array di Numeri:
```c
#include <stdio.h>

int main() {
    int voti[20];  // Array per contenere i voti
    int dimensione;
    FILE *file;
    
    file = fopen("voti.txt", "r");
    if (file == NULL) {
        printf("File voti.txt non trovato!\n");
        return 1;
    }
    
    // Legge prima la dimensione
    fscanf(file, "%d", &dimensione);
    
    // Legge tutti i voti
    for (int i = 0; i < dimensione; i++) {
        fscanf(file, "%d", &voti[i]);
    }
    
    fclose(file);
    
    // Mostra i voti caricati
    printf("Voti caricati dal file:\n");
    for (int i = 0; i < dimensione; i++) {
        printf("Voto %d: %d\n", i + 1, voti[i]);
    }
    
    // Calcola media
    int somma = 0;
    for (int i = 0; i < dimensione; i++) {
        somma += voti[i];
    }
    float media = (float)somma / dimensione;
    
    printf("Media: %.2f\n", media);
    
    return 0;
}
```

---

## 8.6 Sistema Semplice di Database

### Salvare Informazioni Studente:
```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[30];
    char cognome[30];
    int eta;
    float media;
} Studente;

void salva_studente(Studente s) {
    FILE *file = fopen("studenti.txt", "a");  // Append mode
    
    if (file == NULL) {
        printf("Errore nell'apertura del file!\n");
        return;
    }
    
    fprintf(file, "%s,%s,%d,%.2f\n", s.nome, s.cognome, s.eta, s.media);
    fclose(file);
    
    printf("Studente %s %s salvato!\n", s.nome, s.cognome);
}

int main() {
    Studente nuovo_studente;
    
    printf("=== REGISTRAZIONE STUDENTE ===\n");
    
    printf("Nome: ");
    scanf("%29s", nuovo_studente.nome);
    
    printf("Cognome: ");
    scanf("%29s", nuovo_studente.cognome);
    
    printf("Età: ");
    scanf("%d", &nuovo_studente.eta);
    
    printf("Media voti: ");
    scanf("%f", &nuovo_studente.media);
    
    salva_studente(nuovo_studente);
    
    return 0;
}
```

### Leggere Database Studenti:
```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char nome[30];
    char cognome[30];
    int eta;
    float media;
} Studente;

void mostra_tutti_studenti() {
    FILE *file = fopen("studenti.txt", "r");
    Studente s;
    int numero = 1;
    
    if (file == NULL) {
        printf("Nessun file di studenti trovato!\n");
        return;
    }
    
    printf("\n=== ELENCO STUDENTI ===\n");
    printf("%-20s %-20s Età  Media\n", "Nome", "Cognome");
    printf("================================================\n");
    
    // Legge ogni riga del file CSV
    while (fscanf(file, "%29[^,],%29[^,],%d,%f\n", 
                  s.nome, s.cognome, &s.eta, &s.media) == 4) {
        
        printf("%-20s %-20s %3d  %.2f\n", 
               s.nome, s.cognome, s.eta, s.media);
        numero++;
    }
    
    fclose(file);
}

int main() {
    mostra_tutti_studenti();
    return 0;
}
```

---

## 8.7 Esercizi Pratici

### 🎯 Esercizio 8.1: Diario Personale
```c
#include <stdio.h>
#include <time.h>

void aggiungi_al_diario() {
    FILE *file = fopen("diario.txt", "a");
    char messaggio[200];
    time_t now;
    char *data;
    
    if (file == NULL) {
        printf("Errore nell'apertura del diario!\n");
        return;
    }
    
    // Ottiene data corrente
    time(&now);
    data = ctime(&now);
    data[strlen(data)-1] = '\0';  // Rimuove \n dalla fine
    
    printf("Cosa è successo oggi? ");
    getchar();  // Consuma il newline precedente
    fgets(messaggio, sizeof(messaggio), stdin);
    
    fprintf(file, "[%s] %s\n", data, messaggio);
    fclose(file);
    
    printf("Aggiunto al diario!\n");
}

void leggi_diario() {
    FILE *file = fopen("diario.txt", "r");
    char riga[300];
    
    if (file == NULL) {
        printf("Diario vuoto o non esistente.\n");
        return;
    }
    
    printf("\n=== IL TUO DIARIO ===\n");
    while (fgets(riga, sizeof(riga), file) != NULL) {
        printf("%s", riga);
    }
    
    fclose(file);
}

int main() {
    int scelta;
    
    do {
        printf("\n=== DIARIO PERSONALE ===\n");
        printf("1. Aggiungi entry\n");
        printf("2. Leggi diario\n");
        printf("3. Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                aggiungi_al_diario();
                break;
            case 2:
                leggi_diario();
                break;
            case 3:
                printf("Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 3);
    
    return 0;
}
```

### 🎯 Esercizio 8.2: Contabilità Semplice
```c
#include <stdio.h>

typedef struct {
    char descrizione[50];
    float importo;
    char tipo;  // 'E' = entrata, 'U' = uscita
} Movimento;

void aggiungi_movimento() {
    FILE *file = fopen("contabilita.txt", "a");
    Movimento m;
    
    if (file == NULL) {
        printf("Errore nell'apertura del file!\n");
        return;
    }
    
    printf("Descrizione: ");
    getchar();
    fgets(m.descrizione, sizeof(m.descrizione), stdin);
    m.descrizione[strcspn(m.descrizione, "\n")] = 0;  // Rimuove \n
    
    printf("Importo: ");
    scanf("%f", &m.importo);
    
    do {
        printf("Tipo (E=entrata, U=uscita): ");
        scanf(" %c", &m.tipo);
    } while (m.tipo != 'E' && m.tipo != 'U');
    
    fprintf(file, "%s,%.2f,%c\n", m.descrizione, m.importo, m.tipo);
    fclose(file);
    
    printf("Movimento registrato!\n");
}

void mostra_bilancio() {
    FILE *file = fopen("contabilita.txt", "r");
    Movimento m;
    float entrate = 0, uscite = 0;
    
    if (file == NULL) {
        printf("Nessun movimento registrato.\n");
        return;
    }
    
    printf("\n=== TUTTI I MOVIMENTI ===\n");
    printf("%-30s %10s %4s\n", "Descrizione", "Importo", "Tipo");
    printf("-----------------------------------------------\n");
    
    while (fscanf(file, "%49[^,],%f,%c\n", 
                  m.descrizione, &m.importo, &m.tipo) == 3) {
        
        printf("%-30s %10.2f    %c\n", 
               m.descrizione, m.importo, m.tipo);
        
        if (m.tipo == 'E') {
            entrate += m.importo;
        } else {
            uscite += m.importo;
        }
    ៉
    
    fclose(file);
    
    printf("-----------------------------------------------\n");
    printf("Totale entrate:  %10.2f\n", entrate);
    printf("Totale uscite:   %10.2f\n", uscite);
    printf("SALDO:           %10.2f\n", entrate - uscite);
}

int main() {
    int scelta;
    
    do {
        printf("\n=== CONTABILITÀ PERSONALE ===\n");
        printf("1. Aggiungi movimento\n");
        printf("2. Mostra bilancio\n");
        printf("3. Esci\n");
        printf("Scelta: ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                aggiungi_movimento();
                break;
            case 2:
                mostra_bilancio();
                break;
            case 3:
                printf("Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 3);
    
    return 0;
}
```

---

## 8.8 Gestione Errori con i File

### Controllo Completo degli Errori:
```c
#include <stdio.h>

int salva_numero_sicuro(int numero, const char* nome_file) {
    FILE *file = fopen(nome_file, "w");
    
    if (file == NULL) {
        printf("❌ Errore: impossibile creare il file '%s'\n", nome_file);
        return 0;  // Fallimento
    }
    
    if (fprintf(file, "%d\n", numero) < 0) {
        printf("❌ Errore durante la scrittura nel file\n");
        fclose(file);
        return 0;  // Fallimento
    }
    
    if (fclose(file) != 0) {
        printf("❌ Errore nella chiusura del file\n");
        return 0;  // Fallimento
    }
    
    printf("✅ Numero %d salvato con successo in '%s'\n", numero, nome_file);
    return 1;  // Successo
}

int carica_numero_sicuro(int *numero, const char* nome_file) {
    FILE *file = fopen(nome_file, "r");
    
    if (file == NULL) {
        printf("❌ Errore: file '%s' non trovato\n", nome_file);
        return 0;  // Fallimento
    }
    
    if (fscanf(file, "%d", numero) != 1) {
        printf("❌ Errore: formato file non valido\n");
        fclose(file);
        return 0;  // Fallimento
    }
    
    fclose(file);
    printf("✅ Numero %d caricato da '%s'\n", *numero, nome_file);
    return 1;  // Successo
}

int main() {
    int numero;
    const char* nome_file = "numero.txt";
    
    // Test salvataggio
    printf("Inserisci un numero: ");
    scanf("%d", &numero);
    
    if (salva_numero_sicuro(numero, nome_file)) {
        // Test caricamento
        int numero_caricato;
        if (carica_numero_sicuro(&numero_caricato, nome_file)) {
            printf("Verifica: numero salvato=%d, caricato=%d\n", 
                   numero, numero_caricato);
        }
    }
    
    return 0;
}
```

---

## 🎯 Progetto del Modulo: "Sistema di Gestione Biblioteca"

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TITOLO 50
#define MAX_AUTORE 30
#define NOME_FILE "biblioteca.txt"

typedef struct {
    int id;
    char titolo[MAX_TITOLO];
    char autore[MAX_AUTORE];
    int disponibile;  // 1 = disponibile, 0 = prestato
} Libro;

// Funzioni
void stampa_menu(void);
int carica_libri(Libro libri[], int max_libri);
void salva_libri(Libro libri[], int numero_libri);
void aggiungi_libro(Libro libri[], int *numero_libri);
void mostra_libri(Libro libri[], int numero_libri);
void presta_libro(Libro libri[], int numero_libri);
void restituisci_libro(Libro libri[], int numero_libri);
void cerca_libro(Libro libri[], int numero_libri);
int prossimo_id(Libro libri[], int numero_libri);

int main() {
    Libro biblioteca[100];
    int numero_libri;
    int scelta;
    
    printf("=== SISTEMA GESTIONE BIBLIOTECA ===\n");
    
    // Carica libri esistenti
    numero_libri = carica_libri(biblioteca, 100);
    printf("Caricati %d libri dal file.\n", numero_libri);
    
    do {
        stampa_menu();
        printf("Scegli (1-7): ");
        scanf("%d", &scelta);
        
        switch (scelta) {
            case 1:
                aggiungi_libro(biblioteca, &numero_libri);
                break;
            case 2:
                mostra_libri(biblioteca, numero_libri);
                break;
            case 3:
                cerca_libro(biblioteca, numero_libri);
                break;
            case 4:
                presta_libro(biblioteca, numero_libri);
                break;
            case 5:
                restituisci_libro(biblioteca, numero_libri);
                break;
            case 6:
                salva_libri(biblioteca, numero_libri);
                printf("Biblioteca salvata!\n");
                break;
            case 7:
                salva_libri(biblioteca, numero_libri);
                printf("Biblioteca salvata. Arrivederci!\n");
                break;
            default:
                printf("Scelta non valida!\n");
        }
    } while (scelta != 7);
    
    return 0;
}

void stampa_menu(void) {
    printf("\n--- MENU BIBLIOTECA ---\n");
    printf("1. Aggiungi libro\n");
    printf("2. Mostra tutti i libri\n");
    printf("3. Cerca libro\n");
    printf("4. Presta libro\n");
    printf("5. Restituisci libro\n");
    printf("6. Salva biblioteca\n");
    printf("7. Esci\n");
}

int carica_libri(Libro libri[], int max_libri) {
    FILE *file = fopen(NOME_FILE, "r");
    int count = 0;
    
    if (file == NULL) {
        printf("Nessun file biblioteca esistente. Iniziando da zero.\n");
        return 0;
    }
    
    while (count < max_libri && 
           fscanf(file, "%d,%49[^,],%29[^,],%d\n",
                  &libri[count].id,
                  libri[count].titolo,
                  libri[count].autore,
                  &libri[count].disponibile) == 4) {
        count++;
    }
    
    fclose(file);
    return count;
}

void salva_libri(Libro libri[], int numero_libri) {
    FILE *file = fopen(NOME_FILE, "w");
    
    if (file == NULL) {
        printf("❌ Errore nel salvataggio!\n");
        return;
    }
    
    for (int i = 0; i < numero_libri; i++) {
        fprintf(file, "%d,%s,%s,%d\n",
                libri[i].id,
                libri[i].titolo,
                libri[i].autore,
                libri[i].disponibile);
    }
    
    fclose(file);
}

int prossimo_id(Libro libri[], int numero_libri) {
    int max_id = 0;
    for (int i = 0; i < numero_libri; i++) {
        if (libri[i].id > max_id) {
            max_id = libri[i].id;
        }
    }
    return max_id + 1;
}

void aggiungi_libro(Libro libri[], int *numero_libri) {
    if (*numero_libri >= 100) {
        printf("❌ Biblioteca piena!\n");
        return;
    }
    
    Libro *nuovo = &libri[*numero_libri];
    
    nuovo->id = prossimo_id(libri, *numero_libri);
    
    printf("Titolo: ");
    getchar();  // Consuma newline
    fgets(nuovo->titolo, sizeof(nuovo->titolo), stdin);
    nuovo->titolo[strcspn(nuovo->titolo, "\n")] = 0;  // Rimuove \n
    
    printf("Autore: ");
    fgets(nuovo->autore, sizeof(nuovo->autore), stdin);
    nuovo->autore[strcspn(nuovo->autore, "\n")] = 0;
    
    nuovo->disponibile = 1;  // Disponibile di default
    
    (*numero_libri)++;
    printf("✅ Libro aggiunto con ID %d\n", nuovo->id);
}

void mostra_libri(Libro libri[], int numero_libri) {
    if (numero_libri == 0) {
        printf("📚 Nessun libro nella biblioteca.\n");
        return;
    }
    
    printf("\n=== CATALOGO BIBLIOTECA ===\n");
    printf("ID  %-30s %-20s Stato\n", "Titolo", "Autore");
    printf("--------------------------------------------------------\n");
    
    for (int i = 0; i < numero_libri; i++) {
        printf("%-3d %-30s %-20s %s\n",
               libri[i].id,
               libri[i].titolo,
               libri[i].autore,
               libri[i].disponibile ? "Disponibile" : "Prestato");
    }
}

void cerca_libro(Libro libri[], int numero_libri) {
    char termine[50];
    int trovati = 0;
    
    printf("Cerca per titolo o autore: ");
    getchar();
    fgets(termine, sizeof(termine), stdin);
    termine[strcspn(termine, "\n")] = 0;
    
    printf("\n=== RISULTATI RICERCA ===\n");
    
    for (int i = 0; i < numero_libri; i++) {
        if (strstr(libri[i].titolo, termine) || 
            strstr(libri[i].autore, termine)) {
            
            printf("ID %d: %s di %s (%s)\n",
                   libri[i].id,
                   libri[i].titolo,
                   libri[i].autore,
                   libri[i].disponibile ? "Disponibile" : "Prestato");
            trovati++;
        }
    }
    
    if (trovati == 0) {
        printf("🔍 Nessun libro trovato.\n");
    } else {
        printf("Trovati %d libri.\n", trovati);
    }
}

void presta_libro(Libro libri[], int numero_libri) {
    int id;
    
    printf("ID del libro da prestare: ");
    scanf("%d", &id);
    
    for (int i = 0; i < numero_libri; i++) {
        if (libri[i].id == id) {
            if (libri[i].disponibile) {
                libri[i].disponibile = 0;
                printf("✅ Libro '%s' prestato!\n", libri[i].titolo);
            } else {
                printf("❌ Libro già prestato!\n");
            }
            return;
        }
    }
    
    printf("❌ Libro con ID %d non trovato!\n", id);
}

void restituisci_libro(Libro libri[], int numero_libri) {
    int id;
    
    printf("ID del libro da restituire: ");
    scanf("%d", &id);
    
    for (int i = 0; i < numero_libri; i++) {
        if (libri[i].id == id) {
            if (!libri[i].disponibile) {
                libri[i].disponibile = 1;
                printf("✅ Libro '%s' restituito!\n", libri[i].titolo);
            } else {
                printf("❌ Libro non era prestato!\n");
            }
            return;
        }
    }
    
    printf("❌ Libro con ID %d non trovato!\n", id);
}
```

---

## 8.9 Riepilogo

✅ **Cosa hai imparato:**
- Come aprire, leggere e scrivere file
- Modi di apertura: "r", "w", "a", "r+"
- Salvare e caricare dati strutturati
- Gestire errori nell'accesso ai file
- Creare semplici database con file CSV
- Implementare sistemi di persistenza

✅ **Cosa sai fare ora:**
- Creare programmi che "ricordano" i dati
- Salvare configurazioni e preferenze
- Implementare sistemi di archiviazione
- Lavorare con file CSV per dati tabulari
- Gestire errori di I/O in modo professionale

---

**Prossimo modulo:** Metteremo tutto insieme con **progetti finali completi**!
