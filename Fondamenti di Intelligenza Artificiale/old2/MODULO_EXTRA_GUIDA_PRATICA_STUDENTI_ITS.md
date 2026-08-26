# 📘 MODULO EXTRA
# Guida Pratica all'Uso dell'IA per Studenti ITS
## Come Sfruttare l'IA per Studio, Progetti e Lavoro
### Manuale Operativo Completo

---

## 📑 Indice del Modulo

1. [Introduzione per Studenti ITS](#1-introduzione-per-studenti-its)
2. [Strumenti IA Disponibili](#2-strumenti-ia-disponibili)
3. [Organizzazione dei Prompt](#3-organizzazione-dei-prompt)
4. [Prompt per Apprendimento e Studio](#4-prompt-per-apprendimento-e-studio)
5. [Prompt per Generazione Codice](#5-prompt-per-generazione-codice)
6. [Prompt per Testi e Documentazione](#6-prompt-per-testi-e-documentazione)
7. [Prompt per Presentazioni](#7-prompt-per-presentazioni)
8. [Workflow Completi per Progetti ITS](#8-workflow-completi-per-progetti-its)
9. [Biblioteca Prompt Pronti all'Uso](#9-biblioteca-prompt-pronti-alluso)
10. [Errori da Evitare](#10-errori-da-evitare)
11. [Casi d'Uso Reali ITS](#11-casi-duso-reali-its)
12. [Sistema di Organizzazione Personale](#12-sistema-di-organizzazione-personale)

---

## 1. Introduzione per Studenti ITS

### 1.1 Perché Questa Guida

Come studente ITS in ambito informatico, embedded o sistemi, l'IA può essere il tuo **assistente personale 24/7** per:

- ✅ **Studiare** concetti difficili con spiegazioni personalizzate
- ✅ **Programmare** più velocemente con supporto su codice
- ✅ **Documentare** progetti in modo professionale
- ✅ **Creare** presentazioni efficaci per esami/stage
- ✅ **Risolvere** problemi tecnici complessi
- ✅ **Prepararsi** per colloqui di lavoro

**Ma attenzione**: L'IA è uno **strumento**, non una **scorciatoia**. Usala per imparare meglio, non per evitare di imparare!

### 1.2 Mentalità Corretta

```
❌ MENTALITÀ SBAGLIATA:
"Chiedo all'IA di fare tutto, io copio"
→ Risultato: Non impari nulla, non sai validare

✅ MENTALITÀ CORRETTA:
"Uso l'IA per capire meglio, accelerare, migliorare"
→ Risultato: Impari di più, più velocemente
```

### 1.3 La Regola d'Oro

> **Usa l'IA come un TUTOR esperto, non come un GHOSTWRITER.**
> 
> Fai domande, chiedi spiegazioni, richiedi esempi.
> Poi STUDIA l'output, COMPRENDI, VALIDA, INTEGRA.

### 1.4 Competenze che Svilupperai

Usando questa guida imparerai a:

1. **Formulare domande precise** → Ottieni risposte utili
2. **Organizzare conoscenza** → Sistema di prompt riutilizzabili
3. **Validare criticamente** → Riconosci errori IA
4. **Produrre contenuti professionali** → Codice, docs, slide
5. **Lavorare efficacemente** → Velocità + Qualità

---

## 2. Strumenti IA Disponibili

### 2.1 LLM Generici (Conversazionali)

#### **ChatGPT (OpenAI)**
```
URL: https://chat.openai.com
Costo: Gratuito (limitato) / Plus $20/mese
Punti di forza:
- Interfaccia semplice
- Ottimo per codice Python, JavaScript
- Buone spiegazioni didattiche
- Plugin (con Plus)

Punti deboli:
- A volte genera codice obsoleto
- Limiti giornalieri versione free
```

#### **Claude (Anthropic)**
```
URL: https://claude.ai
Costo: Gratuito (limitato) / Pro $20/mese
Punti di forza:
- Contesto molto lungo (200k token)
- Eccellente con C, embedded
- Analisi documenti complessi
- Risposte strutturate

Punti deboli:
- Meno plugin di ChatGPT
```

#### **Gemini (Google)**
```
URL: https://gemini.google.com
Costo: Gratuito
Punti di forza:
- Integrato con Google Suite
- Cerca web in tempo reale
- Analizza immagini

Punti deboli:
- A volte meno tecnico degli altri
```

### 2.2 Tool Specializzati per Codice

#### **GitHub Copilot**
```
Tipo: Plugin IDE (VSCode, JetBrains)
Costo: $10/mese (GRATIS per studenti!)
Come: https://education.github.com/pack

Uso:
- Autocomplete intelligente
- Genera funzioni da commenti
- Suggerisce fix

Ideale per: Coding quotidiano
```

#### **Cursor**
```
Tipo: IDE con IA integrata
Costo: Gratuito / Pro $20/mese
URL: https://cursor.sh

Uso:
- Editor stile VSCode + IA nativa
- Ctrl+K per prompt nel codice
- Refactoring assistito

Ideale per: Progetti complessi
```

### 2.3 Tool per Presentazioni

#### **Gamma.app**
```
URL: https://gamma.app
Costo: Gratuito (limitato) / Pro $10/mese

Genera slide da:
- Prompt testo
- Documenti
- Outline

Output: Presentazioni professionali pronte
```

#### **Beautiful.ai**
```
URL: https://www.beautiful.ai
Costo: Trial gratuito / $12/mese

Design automatico slide
Template professionali
```

### 2.4 Tool per Documentazione

#### **Notion AI**
```
Integrato in Notion
Costo: $10/mese (add-on)

Genera/migliora:
- Note di studio
- Documentazione progetti
- Wiki personali
```

### 2.5 Raccomandazione per Studente ITS

**Setup Consigliato (Gratuito):**
```
1. ChatGPT free → Domande generali, spiegazioni
2. Claude free → Codice C, embedded, analisi tecnica
3. GitHub Copilot (studente) → Coding quotidiano
4. Gamma.app free → Presentazioni esami

Costo totale: €0 (con email studente!)
```

**Setup Avanzato (con budget):**
```
1. ChatGPT Plus ($20) O Claude Pro ($20)
2. GitHub Copilot ($10 → gratis studenti)
3. Gamma Pro ($10)

Costo: ~$20-30/mese
Risparmio tempo: 10-15 ore/mese
ROI: Eccellente!
```

---

## 3. Organizzazione dei Prompt

### 3.1 Perché Organizzare i Prompt

Come organizzeresti i tuoi **appunti di studio**? Probabilmente per materia, argomento, progetto.

Lo stesso vale per i prompt IA:

**Senza organizzazione:**
- "Cosa avevo chiesto settimana scorsa?"
- "Com'era quel prompt per generare test?"
- "Devo riscrivere tutto da capo..."

**Con organizzazione:**
- Biblioteca prompt riutilizzabili
- Modelli per task ricorrenti
- Evoluzione progressiva
- Risparmio tempo enorme

### 3.2 Sistema di Organizzazione Prompt

#### **Metodo 1: File di Testo (Base)**

```
📁 Prompt_ITS/
├── 📁 Studio/
│   ├── 📄 spiega_concetto.txt
│   ├── 📄 riassunto_argomento.txt
│   └── 📄 esercizi_pratica.txt
├── 📁 Codice/
│   ├── 📄 funzione_C_template.txt
│   ├── 📄 sketch_arduino_template.txt
│   ├── 📄 debug_codice.txt
│   └── 📄 refactoring.txt
├── 📁 Documentazione/
│   ├── 📄 README_progetto.txt
│   ├── 📄 relazione_tecnica.txt
│   └── 📄 commenti_codice.txt
└── 📁 Presentazioni/
    ├── 📄 slide_progetto.txt
    └── 📄 pitch_idea.txt
```

**Esempio file `funzione_C_template.txt`:**
```
TEMPLATE PROMPT: Funzione C Professionale

---
Scrivi in standard C99 una funzione:

[FIRMA FUNZIONE]

SPECIFICHE:
- [Cosa deve fare]
- [Gestione errori]
- [Valori ritorno]

VINCOLI:
- Solo C99 standard
- No VLA
- Gestione NULL esplicita

OUTPUT RICHIESTO:
- Header (.h) con Doxygen
- Implementation (.c)
- 3+ test cases

ESEMPIO USO:
[Codice esempio]
---

USO:
Copia questo template, compila [CAMPI], invia all'IA.
```

#### **Metodo 2: Notion (Intermedio)**

Crea database Notion:

```
Database: "Prompt Library"
├── Proprietà:
│   ├── Nome (Titolo)
│   ├── Categoria (Select: Studio/Codice/Docs/Slides)
│   ├── Tool (Select: ChatGPT/Claude/Copilot)
│   ├── Qualità (Rating 1-5)
│   ├── Ultima modifica (Data)
│   └── Tag (Multi-select)
└── Views:
    ├── Per Categoria
    ├── Per Tool
    └── Preferiti (5 stelle)
```

**Vantaggio:** Ricerca veloce, template riutilizzabili, collaborazione.

#### **Metodo 3: GitHub Repo (Avanzato)**

```bash
# Crea repo privato
gh repo create my-prompts --private

# Struttura
my-prompts/
├── README.md (indice)
├── templates/
│   ├── coding/
│   ├── docs/
│   └── study/
├── examples/
│   └── real_usage/
└── CHANGELOG.md
```

**Vantaggio:** Versioning, backup automatico, condivisibile.

### 3.3 Sistema di Nomenclatura

**Convenzione consigliata:**
```
[CATEGORIA]_[TASK]_[DETTAGLIO].txt

Esempi:
CODE_function_C_mathematical.txt
CODE_arduino_sensor_analog.txt
STUDY_explain_concept_simple.txt
STUDY_quiz_generation.txt
DOC_readme_project.txt
DOC_comments_inline.txt
SLIDE_project_presentation.txt
```

### 3.4 Template Base Universale

Ogni prompt ben fatto contiene questi elementi:

```markdown
# [NOME PROMPT]

## Contesto
[Chi sei, cosa stai facendo, perché serve]

## Obiettivo
[Cosa vuoi ottenere - chiaro e misurabile]

## Input
[Cosa fornisci all'IA]

## Vincoli
[Limitazioni, standard, formati]

## Output Desiderato
[Come deve essere la risposta]

## Esempi (opzionale)
[Input/output di esempio]

---
CHANGELOG:
v1.0 - 2024-12-05 - Versione iniziale
v1.1 - 2024-12-10 - Aggiunto esempio
```

### 3.5 Sistema di Evoluzione Prompt

I tuoi prompt MIGLIORERANNO nel tempo:

```
ITERAZIONE 1: Prompt base
→ Output OK ma generico

ITERAZIONE 2: Aggiungi vincoli specifici
→ Output migliore, più mirato

ITERAZIONE 3: Aggiungi esempi
→ Output quasi perfetto

ITERAZIONE 4: Fine-tune dettagli
→ Output professionale

SALVA VERSIONE FINALE!
```

**Best Practice:** Quando trovi un prompt che funziona bene, **salvalo immediatamente** con note su cosa lo rende efficace.

---

## 4. Prompt per Apprendimento e Studio

### 4.1 Spiegazione Concetti

#### **Template: Spiega Concetto Semplice**

```
Sono uno studente ITS al [ANNO] anno di [INDIRIZZO].

Devo capire il concetto di [CONCETTO] nel contesto di [MATERIA].

Spiegamelo in modo:
1. Semplice ma preciso (livello universitario tecnico)
2. Con un'analogia pratica
3. Con un esempio di codice/applicazione se pertinente
4. Evidenziando errori comuni da evitare

Poi dammi 3 domande di autoverifica per testare se ho capito.
```

**Esempio Reale:**

```
Sono uno studente ITS al primo anno di Informatica.

Devo capire il concetto di PUNTATORI in C nel contesto di 
Programmazione di Sistema.

Spiegamelo in modo:
1. Semplice ma preciso (livello universitario tecnico)
2. Con un'analogia pratica
3. Con un esempio di codice
4. Evidenziando errori comuni da evitare

Poi dammi 3 domande di autoverifica per testare se ho capito.
```

#### **Template: Confronto Concetti**

```
Sono uno studente ITS che studia [MATERIA].

Qual è la differenza tra [CONCETTO A] e [CONCETTO B]?

Fornisci:
1. Definizioni tecniche di entrambi
2. Tabella comparativa con 5 criteri
3. Quando usare uno vs l'altro
4. Esempio pratico di ciascuno
5. Errori comuni nel confonderli
```

**Esempio:**
```
Qual è la differenza tra malloc() e calloc() in C?
[Usa template sopra]
```

#### **Template: Approfondimento Tecnico**

```
Sto studiando [ARGOMENTO] per [MATERIA/PROGETTO].

Ho capito le basi, ma voglio approfondire [ASPETTO SPECIFICO].

Fornisci:
1. Spiegazione tecnica dettagliata
2. Come funziona internamente (se rilevante)
3. Casi d'uso avanzati
4. Pitfalls e best practices
5. Risorse per approfondire ulteriormente

Il mio livello attuale: [principiante/intermedio/avanzato]
```

### 4.2 Generazione Quiz e Test

#### **Template: Quiz Autovalutazione**

```
Genera un quiz di autovalutazione su [ARGOMENTO].

Formato:
- 10 domande a scelta multipla
- 5 domande vero/falso
- 3 domande aperte brevi

Livello: [base/intermedio/avanzato]
Focus su: [aspetti specifici]

Fornisci le domande senza risposte. Poi, separatamente, 
fornisci tutte le risposte con spiegazioni.
```

#### **Template: Esercizi Pratici**

```
Crea 5 esercizi pratici su [ARGOMENTO] per studente ITS.

Per ogni esercizio fornisci:
1. Testo esercizio (cosa fare)
2. Input/output attesi
3. Suggerimenti (hints) se bloccato
4. Soluzione completa commentata
5. Varianti più difficili (opzionali)

Difficoltà: crescente (da facile a difficile)
Tempo stimato: ~15 minuti ciascuno
```

**Esempio:**
```
Crea 5 esercizi pratici su ARRAY E PUNTATORI IN C per studente ITS.
[Usa template]
```

### 4.3 Riassunti e Sintesi

#### **Template: Riassunto Capitolo/Argomento**

```
Ho studiato [ARGOMENTO/CAPITOLO] da [FONTE].

Ecco i concetti chiave che ho identificato:
[Lista punti principali]

Crea un riassunto strutturato che:
1. Organizzi i concetti in modo logico
2. Evidenzi collegamenti tra concetti
3. Aggiunga esempi pratici per ogni punto
4. Includa una "mappa mentale" testuale
5. Concluda con 3 takeaway principali

Formato: Markdown con titoli chiari
Lunghezza: 1-2 pagine A4
```

#### **Template: Preparazione Esame**

```
Devo preparare l'esame di [MATERIA] che copre:
[Lista argomenti]

Crea un piano di studio strutturato che:
1. Organizzi gli argomenti per priorità
2. Suggerisca ordine di studio ottimale
3. Indichi tempo stimato per argomento
4. Includa metodi di memorizzazione/comprensione
5. Proponga sessioni di ripasso

Ho [N] giorni disponibili e studio [X] ore/giorno.
```

### 4.4 Chiarimento Dubbi

#### **Template: "Non Ho Capito..."**

```
Sto studiando [ARGOMENTO] e non ho capito [PUNTO SPECIFICO].

Ho capito fino a qui:
[Cosa hai capito]

Ma non capisco:
[Cosa non ti è chiaro]

Ho provato:
[Cosa hai tentato per capire]

Spiegami [PUNTO SPECIFICO] in modo diverso, magari con:
- Un'analogia pratica
- Un esempio passo-passo
- Un disegno/schema descritto a parole
```

---

## 5. Prompt per Generazione Codice

### 5.1 Template Funzione Singola

#### **Template Base Funzione C**

```
Scrivi in standard C99 una funzione:

FIRMA:
[tipo_ritorno] nome_funzione([parametri]);

COMPORTAMENTO:
- [Cosa fa]
- [Come gestisce input invalidi]
- [Cosa ritorna]

VINCOLI:
- Solo C99 standard (no POSIX, no GNU)
- No VLA
- Gestione esplicita NULL/errori
- Complessità massima: O([...])

OUTPUT RICHIESTO:
1. Header file (.h) con:
   - Dichiarazione
   - Documentazione Doxygen completa
2. Implementation (.c) con:
   - Codice commentato
   - Gestione edge cases
3. Test file con 5 test cases:
   - Caso normale
   - Edge cases (minimo 3)
   - Caso errore

ESEMPIO USO:
[Mostra chiamata tipica]
```

**Esempio Compilato:**

```
Scrivi in standard C99 una funzione:

FIRMA:
int find_max(const int arr[], int n, int *max_value);

COMPORTAMENTO:
- Trova valore massimo in array
- Salva massimo in *max_value
- Ritorna 0 se successo, -1 se errore

VINCOLI:
- Solo C99 standard
- Gestione esplicita NULL
- Complessità: O(n)

OUTPUT RICHIESTO:
[come template]

ESEMPIO USO:
int arr[] = {3, 7, 2, 9, 1};
int max;
if (find_max(arr, 5, &max) == 0) {
    printf("Max: %d\n", max);
}
```

#### **Template Sketch Arduino**

```
Scrivi sketch Arduino per board [BOARD_TYPE]:

HARDWARE:
- [Componente 1] su pin [X]
- [Componente 2] su pin [Y]
- [...]

FUNZIONALITÀ:
1. [Funzione principale]
2. [Funzione secondaria]
3. [Gestione eventi/sensori]

VINCOLI TECNICI:
- Usa millis() (NO delay() lunghi)
- Logica completamente non-bloccante
- Comunicazione seriale [BAUD] per debug
- Gestisci debouncing se pulsanti
- Definisci pin con const int

OUTPUT RICHIESTO:
1. Sketch completo (.ino)
2. Commenti esplicativi
3. Schema collegamenti testuale/ASCII art
4. Istruzioni setup iniziale

COMPORTAMENTO ATTESO:
[Descrivi scenario d'uso]
```

### 5.2 Debugging e Fixing

#### **Template Debug Codice**

```
Ho questo codice [LINGUAGGIO] che non funziona come previsto:

```[linguaggio]
[IL TUO CODICE]
```

PROBLEMA OSSERVATO:
[Descrizione comportamento errato o errore]

COMPORTAMENTO ATTESO:
[Cosa dovrebbe fare]

COSA HO PROVATO:
[Tentativi di fix]

COMPITI:
1. Identifica TUTTI i bug (sintattici, logici, sicurezza)
2. Spiega PERCHÉ ogni bug causa il problema
3. Fornisci versione corretta e funzionante
4. Aggiungi commenti che evidenziano le correzioni
5. Suggerisci test per validare il fix
```

#### **Template Ottimizzazione**

```
Ho questo codice funzionante ma voglio ottimizzarlo:

```[linguaggio]
[CODICE]
```

OBIETTIVI OTTIMIZZAZIONE:
- [ ] Velocità (performance)
- [ ] Memoria (footprint)
- [ ] Leggibilità
- [ ] Sicurezza

VINCOLI:
- [Vincoli specifici]

COMPITI:
1. Analizza complessità attuale
2. Identifica bottleneck
3. Proponi ottimizzazioni specifiche
4. Fornisci versione ottimizzata
5. Benchmarking: confronta prima/dopo
```

### 5.3 Refactoring

#### **Template Refactoring Completo**

```
Questo codice funziona ma è poco manutenibile:

```[linguaggio]
[CODICE]
```

OBIETTIVI REFACTORING:
1. Migliorare leggibilità
2. Ridurre duplicazione
3. Separare responsabilità (SRP)
4. Migliorare nomi variabili/funzioni
5. Aggiungere documentazione

VINCOLI:
- Mantieni comportamento identico
- No cambi di algoritmo
- [Linguaggio] standard [versione]

OUTPUT:
1. Codice refactorato completo
2. Lista modifiche applicate
3. Confronto prima/dopo (evidenzia differenze)
4. Test che dimostrano equivalenza comportamentale
```

### 5.4 Generazione Test

#### **Template Test Suite**

```
Ho questa funzione [LINGUAGGIO]:

```[linguaggio]
[FUNZIONE]
```

Genera test suite completa che copra:
1. Casi normali (happy path)
2. Edge cases (limiti, valori estremi)
3. Casi errore (input invalidi)
4. Corner cases (combinazioni rare)

Per ogni test fornisci:
- Nome test descrittivo
- Input
- Output atteso
- Asserzione
- Commento su cosa testa

Framework: [es. assert.h per C, unittest per Python]
Copertura target: >90%
```

### 5.5 Documentazione Codice

#### **Template Commenti Inline**

```
Aggiungi commenti inline al seguente codice:

```[linguaggio]
[CODICE]
```

STILE COMMENTI:
- Spiega PERCHÉ, non COSA (il cosa si vede dal codice)
- Evidenzia algoritmi non ovvi
- Documenta assunzioni
- Nota edge cases gestiti

FORMATO:
- [Formato commenti del linguaggio]
- Concisi ma informativi
```

#### **Template README Progetto**

```
Ho sviluppato questo progetto [NOME]:

DESCRIZIONE BREVE:
[1 frase cosa fa]

COMPONENTI:
- [File 1]: [scopo]
- [File 2]: [scopo]
- [...]

DIPENDENZE:
- [Libreria 1]
- [Libreria 2]

Genera README.md professionale che includa:
1. Titolo e descrizione
2. Features principali
3. Requisiti di sistema
4. Istruzioni installazione (passo-passo)
5. Esempi d'uso
6. Struttura progetto
7. Licenza
8. Contatti/Contributi

Tono: Professionale ma accessibile
Formato: Markdown con emoji appropriati
```

---

## 6. Prompt per Testi e Documentazione

### 6.1 Relazioni Tecniche

#### **Template Relazione Progetto ITS**

```
Devo scrivere relazione tecnica per progetto ITS su [ARGOMENTO].

INFORMAZIONI PROGETTO:
- Titolo: [...]
- Durata: [...]
- Obiettivi: [...]
- Tecnologie: [...]
- Risultati: [...]

STRUTTURA RICHIESTA:
1. Introduzione (problema affrontato)
2. Analisi requisiti
3. Progettazione (architettura, scelte tecniche)
4. Implementazione (dettagli tecnici)
5. Testing e validazione
6. Risultati e discussione
7. Conclusioni e sviluppi futuri

VINCOLI:
- Lunghezza: [N] pagine
- Tono: Tecnico-professionale
- Pubblico: Docenti ITS + potenziali datori lavoro
- Formato: [Word/LaTeX/Markdown]

Genera outline dettagliato con punti chiave per ogni sezione.
Poi, su richiesta, espandi sezione per sezione.
```

#### **Template Documentazione API**

```
Ho sviluppato [LIBRERIA/MODULO] con queste funzioni:

[LISTA FUNZIONI CON FIRME]

Genera documentazione API stile professionale che includa:

PER OGNI FUNZIONE:
1. Descrizione scopo
2. Parametri (tipo, descrizione, vincoli)
3. Valore ritorno
4. Esempi d'uso (minimo 2)
5. Note su edge cases
6. Possibili errori
7. Vedere anche (funzioni correlate)

STILE:
- Formato: [Doxygen/JSDoc/Sphinx]
- Esempi funzionanti
- Chiaro per utente esterno
```

### 6.2 Report e Analisi

#### **Template Report Tecnico**

```
Ho raccolto questi dati da [ESPERIMENTO/PROGETTO]:

[DATI O DESCRIZIONE]

Genera report tecnico che:
1. Introduca brevemente contesto
2. Descriva metodologia
3. Presenti dati (tabelle/grafici descritti)
4. Analizzi risultati
5. Tragga conclusioni
6. Suggerisca miglioramenti

Formato: [Word/PDF]
Lunghezza: [N] pagine
Grafici: Descrivi che tipo serve, genererò io
```

### 6.3 Email e Comunicazioni

#### **Template Email Professionale**

```
Devo scrivere email a [DESTINATARIO: docente/azienda/collega] per [SCOPO].

CONTESTO:
[Breve descrizione situazione]

OBIETTIVO EMAIL:
[Cosa vuoi ottenere]

INFORMAZIONI DA INCLUDERE:
- [Info 1]
- [Info 2]

TONO: [Formale/Semi-formale/Cordiale]

Genera email completa con:
- Oggetto efficace
- Saluto appropriato
- Corpo chiaro e conciso
- Chiusura e firma
```

**Esempio:**
```
Destinatario: Professor Rossi (docente Sistemi Embedded)
Scopo: Chiarimento su specifiche progetto finale

CONTESTO:
Sto sviluppando progetto su sistema IoT con Arduino 
e non sono sicuro se posso usare librerie esterne.

OBIETTIVO:
Ottenere chiarimento e eventuale approvazione.

TONO: Formale ma cordiale
```

### 6.4 CV e Lettere Motivazionali

#### **Template Miglioramento CV**

```
Ecco il mio CV attuale:

[PASTE CV O DESCRIZIONE SEZIONI]

CONTESTO:
- Studente ITS [anno/indirizzo]
- Candidatura per: [Stage/Lavoro/Progetto]
- Azienda target: [Tipo/settore]

COMPITI:
1. Analizza punti forti e deboli
2. Suggerisci miglioramenti struttura
3. Riscrivi sezioni chiave enfatizzando:
   - Competenze tecniche
   - Progetti rilevanti
   - Soft skills
4. Suggerisci cosa aggiungere/rimuovere
5. Ottimizza per ATS (Applicant Tracking System)

Output: CV migliorato in formato [richiesto]
```

#### **Template Lettera Motivazionale**

```
Sto candidando per [POSIZIONE] presso [AZIENDA].

MIO BACKGROUND:
- [Percorso studi]
- [Competenze chiave]
- [Progetti rilevanti]

PERCHÉ QUESTA POSIZIONE:
- [Motivazione 1]
- [Motivazione 2]

COSA PORTO:
- [Valore che aggiungi]

Genera lettera motivazionale che:
1. Catturi attenzione nelle prime righe
2. Dimostri conoscenza azienda/ruolo
3. Colleghi mie competenze a loro bisogni
4. Mostri entusiasmo genuino
5. Call to action chiara

Lunghezza: ~300-400 parole
Tono: Professionale, entusiasta, non retorico
```

---

## 7. Prompt per Presentazioni

### 7.1 Struttura Presentazione

#### **Template Outline Presentazione**

```
Devo creare presentazione su [ARGOMENTO] per [CONTESTO].

INFORMAZIONI:
- Pubblico: [Chi ascolta]
- Durata: [Minuti]
- Scopo: [Informare/Persuadere/Insegnare]
- Formato: [Esame/Pitch/Conferenza]

CONTENUTI DA COPRIRE:
- [Punto 1]
- [Punto 2]
- [...]

Genera:
1. Outline completo con numero slide stimato
2. Contenuto chiave per ogni slide
3. Suggerimenti visual per ogni sezione
4. Script note relatore per slide complesse
5. Timing suggerito per sezione

STRUTTURA:
- Introduzione (impatto)
- Corpo (3-5 punti principali)
- Conclusione (call to action/takeaway)
```

### 7.2 Contenuto Slide Specifiche

#### **Template Slide Tecnica**

```
Slide su [ARGOMENTO TECNICO].

OBIETTIVO SLIDE:
[Cosa deve capire lo spettatore]

CONTENUTO DA INCLUDERE:
- [Info 1]
- [Info 2]

VINCOLI:
- Massimo [N] bullet points
- 1 visual (descrivi che tipo)
- Leggibile da 5 metri

Genera:
1. Titolo slide efficace
2. Bullet points (max 6 parole cad)
3. Descrizione visual suggerito
4. Note relatore (cosa dire, non cosa scrivere)
```

**Esempio:**
```
Slide su "Architettura Sistema Arduino"

OBIETTIVO:
Far capire componenti principali e loro relazione

CONTENUTO:
- Microcontrollore ATmega328P
- Pin I/O (digitali/analogici)
- Alimentazione
- Comunicazione seriale

VINCOLI:
- Max 5 bullet points
- Schema a blocchi
- Leggibile

[IA genera contenuto ottimizzato]
```

### 7.3 Pitch e Demo

#### **Template Elevator Pitch**

```
Ho sviluppato [PROGETTO/IDEA].

DESCRIZIONE TECNICA:
[Cosa fa, come funziona]

PROBLEMA RISOLTO:
[Pain point]

PUBBLICO:
[A chi mi rivolgo]

Genera elevator pitch di 60 secondi (~150 parole) che:
1. Catturi attenzione con problema/hook
2. Presenti soluzione in modo chiaro
3. Evidenzi valore unico
4. Chiuda con call to action

Stile: Chiaro, entusiasta, non tecnico (se pubblico misto)
```

#### **Template Demo Script**

```
Devo fare demo live di [PROGETTO].

SETUP:
[Hardware/software necessari]

FUNZIONALITÀ DA MOSTRARE:
1. [Feature 1]
2. [Feature 2]
3. [...]

DURATA: [Minuti]

Genera script demo che:
1. Introduca contesto (30 sec)
2. Mostri features in sequenza logica
3. Gestisca transizioni fluide
4. Anticipi possibili domande
5. Includa piano B se qualcosa non funziona

FORMATO:
- Timing preciso per ogni parte
- Cosa dire E cosa fare
- Note su cosa evidenziare
```

### 7.4 Slide di Codice

#### **Template Slide con Codice**

```
Devo mostrare questo codice in slide:

```[linguaggio]
[CODICE]
```

OBIETTIVO:
[Cosa deve capire l'audience]

VINCOLI:
- Slide PowerPoint/Google Slides
- Leggibile da lontano
- Massimo [N] righe visibili

Genera:
1. Versione codice semplificata (solo essenziale)
2. Annotazioni/evidenziazioni chiave
3. Titolo slide
4. Spiegazione concisa (sotto il codice)
5. Note relatore per spiegare dettagli

Formato syntax highlighting: [linguaggio]
```

---

## 8. Workflow Completi per Progetti ITS

### 8.1 Workflow: Progetto da Zero

#### **Fase 1: Ideazione e Planning**

```
PROMPT 1 - Brainstorming:
"Sono studente ITS [indirizzo]. Devo sviluppare progetto 
finale su tema [AREA: es. IoT/Embedded/Automazione].

Suggeriscimi 10 idee di progetto che:
- Siano fattibili in [N] settimane
- Dimostrino competenze tecniche
- Abbiano applicazione pratica
- Usino tecnologie [elenca]

Per ogni idea:
- Descrizione breve
- Difficoltà (1-5)
- Tecnologie necessarie
- Originalità (1-5)"

↓

PROMPT 2 - Analisi Fattibilità:
"Ho scelto idea: [DESCRIZIONE]

Analizza fattibilità considerando:
- Componenti hardware necessari (con costi stimati)
- Software/librerie richieste
- Competenze da acquisire
- Tempo stimato per milestone
- Rischi e mitigation

Genera:
1. Bill of Materials (BOM)
2. Timeline progetto
3. Analisi SWOT
4. Piano di apprendimento per skill mancanti"
```

#### **Fase 2: Design e Architettura**

```
PROMPT 3 - Architettura Sistema:
"Progetto: [NOME E DESCRIZIONE]

Requisiti funzionali:
- [Req 1]
- [Req 2]

Requisiti non funzionali:
- [Performance]
- [Affidabilità]

Genera:
1. Architettura sistema (descrivi diagramma a blocchi)
2. Scelte tecnologiche giustificate
3. Interfacce tra componenti
4. Struttura software (moduli)
5. Schema elettrico/collegamenti (se hardware)

Formato: Descrittivo + pseudocodice dove utile"

↓

PROMPT 4 - Specifica Dettagliata:
"Basandoti sull'architettura, genera specifica tecnica 
dettagliata per modulo [NOME_MODULO]:

- Input/Output
- Algoritmi utilizzati
- Gestione errori
- API esposte
- Dipendenze
- Test cases previsti"
```

#### **Fase 3: Implementazione**

```
PROMPT 5 - Generazione Codice Base:
[Usa template sezione 5 per ogni modulo]

↓

PROMPT 6 - Integrazione:
"Ho questi moduli sviluppati:
[Lista moduli con breve descrizione]

Genera:
1. Main/entry point che integra tutto
2. Gestione dipendenze
3. Inizializzazione sistema
4. Shutdown pulito
5. Logging/debugging"

↓

PROMPT 7 - Testing:
[Usa template generazione test sezione 5.4]
```

#### **Fase 4: Documentazione**

```
PROMPT 8 - Documentazione Tecnica:
[Usa template sezione 6.1]

↓

PROMPT 9 - README e Guide:
[Usa template sezione 5.5]

↓

PROMPT 10 - Presentazione:
[Usa template sezione 7]
```

### 8.2 Workflow: Debugging Complesso

```
STEP 1 - Isolamento Problema:
"Ho questo bug nel progetto [NOME]:

SINTOMO:
[Cosa non funziona]

QUANDO SUCCEDE:
[Condizioni]

COSA HO PROVATO:
[Tentativi]

Aiutami a isolare il problema:
1. Genera checklist debug
2. Suggerisci test per riprodurre
3. Identifica aree probabili del bug
4. Proponi strategia di isolamento"

↓

STEP 2 - Analisi Specifica:
[Paste codice sospetto]
[Usa template debug sezione 5.2]

↓

STEP 3 - Fix e Validazione:
"Applicato questo fix:
[Mostra modifiche]

Genera:
1. Test di regressione
2. Test che valida il fix
3. Checklist per verificare no effetti collaterali"
```

### 8.3 Workflow: Preparazione Esame/Colloquio

```
FASE 1 - Studio:
[Usa template sezione 4.1-4.3]

↓

FASE 2 - Ripasso Attivo:
"Argomenti esame: [LISTA]

Per ogni argomento genera:
1. Domanda probabile esame
2. Risposta modello (concisa)
3. Domanda di approfondimento
4. Concetti da collegare

Poi simula 10 domande random da tutto il materiale"

↓

FASE 3 - Presentazione Progetti:
[Usa template sezione 7.3 per pitch progetti]

↓

FASE 4 - Simulazione:
"Simula colloquio tecnico per posizione [RUOLO].

Fai 5 domande tecniche progressive:
1. Base (valuta conoscenze fondamentali)
2-3. Intermedie (problem solving)
4-5. Avanzate (pensiero critico)

Per ogni mia risposta:
- Valuta (1-10)
- Indica miglioramenti
- Fai follow-up se necessario"
```

---

## 9. Biblioteca Prompt Pronti all'Uso

### 9.1 Prompt Copy-Paste per Studenti ITS

#### **Studio: Spiegazione ELI5 (Explain Like I'm 5)**

```
Spiega [CONCETTO COMPLESSO] come se avessi 5 anni, 
poi spiega lo stesso concetto al mio livello (studente ITS).

Cosa voglio capire: PERCHÉ funziona così, non solo COME.
```

#### **Codice: Quick Function**

```
Funzione [LINGUAGGIO] che fa: [1 RIGA DESCRIZIONE]
Parametri: [LISTA]
Ritorna: [TIPO]
Standard: [C99/Python3/etc]
Test: includi 2 esempi
```

#### **Debug: Fix Veloce**

```
Questo codice:
```[linguaggio]
[PASTE CODICE]
```
Errore: [COPIA ERRORE COMPILATORE/RUNTIME]

Fix + spiega il problema in 2 righe.
```

#### **Docs: README Express**

```
Progetto: [NOME]
Fa: [1 RIGA]
Tech: [LISTA]
Come run: [COMANDO]

Genera README.md minimale ma completo.
```

#### **Presentazione: Slide in 5 Minuti**

```
Presentazione [DURATA]min su [TOPIC]
Pubblico: [CHI]
3 punti chiave: [P1, P2, P3]

Outline + contenuto slide chiave.
```

### 9.2 Prompt Avanzati

#### **Code Review Automatico**

```
Fai code review di questo codice come se fossi senior developer:

```[linguaggio]
[CODICE]
```

Valuta (1-10) e commenta:
1. Correttezza
2. Leggibilità
3. Performance
4. Sicurezza
5. Manutenibilità

Per ogni problema trovato:
- Severity (Critical/Major/Minor)
- Suggerimento fix
- Best practice violata
```

#### **Progettazione Sistema**

```
Devo progettare sistema [TIPO] con requisiti:

FUNZIONALI:
- [Req 1]
- [Req 2]

NON-FUNZIONALI:
- Performance: [spec]
- Affidabilità: [spec]
- Scalabilità: [spec]

Proponi 3 architetture alternative con:
- Diagramma (descritto)
- Pro/Contro
- Costo stimato
- Complessità implementazione

Poi raccomanda la migliore per caso d'uso [CONTESTO].
```

#### **Analisi Comparativa**

```
Devo scegliere tra [OPZIONE A] e [OPZIONE B] per [CONTESTO].

Criteri decisione:
- [Criterio 1]
- [Criterio 2]
- [...]

Genera:
1. Tabella comparativa dettagliata
2. Analisi punti critici
3. Raccomandazione giustificata
4. Scenario dove l'altra opzione sarebbe migliore
```

### 9.3 Prompt Creativi

#### **Analogia su Misura**

```
Spiega [CONCETTO TECNICO COMPLESSO] usando un'analogia 
tratta dal mondo [DOMINIO FAMILIARE: sport/cucina/musica/etc].

Mantieni analogia coerente su tutti gli aspetti del concetto.
```

**Esempio:**
```
Spiega STACK (struttura dati) usando analogia con una pila di piatti.
```

#### **Storytelling Tecnico**

```
Racconta come [TECNOLOGIA/CONCETTO] è nata e si è evoluta,
come se fosse una storia avvincente.

Include:
- Problema originale
- Soluzioni tentate
- Breakthrough
- Evoluzione
- Stato attuale
- Futuro possibile

Stile: Divulgativo ma accurato tecnicamente.
```

#### **Debugging Narrativo**

```
Ho questo bug frustrante: [DESCRIZIONE]

Raccontami una "detective story" del debug:
1. Indizi (sintomi osservati)
2. Sospetti (possibili cause)
3. Investigazione (come procedere)
4. Rivelazione (causa vera)
5. Risoluzione (fix)

Rendila didattica e memorabile!
```

---

## 10. Errori da Evitare

### 10.1 Errori Comuni con IA

#### ❌ **Errore 1: Prompt Troppo Vago**

```
SBAGLIATO:
"Scrivi codice Arduino"

PROBLEMA: Troppo generico, output inutile

CORRETTO:
"Scrivi sketch Arduino Uno che legge temperatura 
da TMP36 su A0 e accende LED su pin 13 se >25°C.
Usa millis(), no delay. Seriale 9600 per debug."
```

#### ❌ **Errore 2: Copiare Senza Capire**

```
COMPORTAMENTO SBAGLIATO:
1. Chiedi codice all'IA
2. Copia-incolla direttamente
3. Compili
4. "Funziona!" → Consegni

PROBLEMA: 
- Non hai imparato nulla
- Non sai se è corretto
- Non sai fixare se rompe
- Non puoi spiegarlo

COMPORTAMENTO CORRETTO:
1. Chiedi codice
2. LEGGI e COMPRENDI ogni riga
3. Identifica possibili problemi
4. TESTA con vari input
5. VALIDA con tool (compiler, valgrind)
6. MODIFICA se necessario
7. ORA puoi usarlo
```

#### ❌ **Errore 3: Non Validare Output**

```
CASO REALE:
Student: "IA, scrivi funzione C per duplicare stringa"
IA: [Genera codice con strdup()]
Student: [Copia, compila su embedded]
Compilatore: "error: strdup undefined"

PROBLEMA: strdup() non è C standard!

LEZIONE: SEMPRE validare suggerimenti IA
- Controlla standard/librerie
- Testa su target reale
- Usa documentation ufficiale
```

#### ❌ **Errore 4: Prompt Monolitico**

```
SBAGLIATO:
"Scrivi intero sistema di gestione libreria con database,
interfaccia utente, gestione utenti, prestiti, ricerche,
statistiche, backup automatico, in C++ con Qt."

PROBLEMA: Troppo grande, output superficiale

CORRETTO: Approccio iterativo
1. "Progetta architettura sistema libreria"
2. "Specifica modulo database"
3. "Implementa classe Book"
4. "Genera test per Book"
[... passo dopo passo]
```

#### ❌ **Errore 5: Ignorare Contesto**

```
SBAGLIATO:
"Scrivi codice per gestire 1000 connessioni simultanee"
[Su Arduino con 2KB RAM!]

PROBLEMA: IA non conosce il TUO contesto specifico

CORRETTO:
"Sistema: Arduino Uno (2KB RAM, 32KB Flash)
Task: Gestire max 5 sensori con polling ogni 100ms
Vincoli: Memoria minimale, no allocazione dinamica

Scrivi codice adatto a QUESTI vincoli."
```

### 10.2 Red Flags nell'Output IA

Impara a riconoscere segnali di allarme:

#### 🚩 **Red Flag 1: Funzioni "Strane"**

```c
// IA genera:
char *str = strdup(input);  // 🚩 strdup in C99?
result = itoa(number);      // 🚩 itoa standard?

AZIONE: Verifica SEMPRE su cppreference.com
```

#### 🚩 **Red Flag 2: "Sembra Troppo Facile"**

```
Prompt: "Sistema operativo real-time da zero"
IA: "Ecco il codice completo in 50 righe!"

🚩 Se sembra troppo semplice per problema complesso,
   probabilmente è TROPPO semplificato o incompleto.
```

#### 🚩 **Red Flag 3: Commenti Generici**

```c
// IA genera:
int x = 5;  // Initialize x to 5
int y = 10; // Initialize y to 10

🚩 Commenti che ripetono il codice = output low-quality
   Buoni commenti spiegano PERCHÉ, non COSA.
```

#### 🚩 **Red Flag 4: Nessuna Gestione Errori**

```c
// IA genera:
void process(int *data) {
    for (int i = 0; i < 100; i++) {
        data[i] = i * 2;  // 🚩 No check data!=NULL!
    }
}

🚩 Codice senza error handling = codice fragile
```

#### 🚩 **Red Flag 5: Hardcoded Magic Numbers**

```c
// IA genera:
if (sensor > 1023) {  // 🚩 Perché 1023?
    delay(5000);      // 🚩 Perché 5000?
}

🚩 Numeri senza spiegazione/costanti = codice oscuro
```

### 10.3 Quando NON Usare IA

Situazioni dove IA **non è appropriata**:

#### ❌ **Durante Esami Senza Permesso**

Ovvio, ma va detto: se l'esame vieta strumenti esterni, rispetta le regole.

#### ❌ **Per Copiare Progetti Altrui**

```
SBAGLIATO:
"IA, ricrea il progetto X che ho visto online"
→ Plagio, anche se tramite IA

CORRETTO:
"IA, spiega come funziona progetto X"
"IA, aiutami a implementare concetto simile MA originale"
```

#### ❌ **Per Evitare di Imparare Basi**

```
Se non sai cos'è un ciclo for, NON chiedere:
"IA, scrivi for loop"

Prima STUDIA le basi, poi usa IA per:
- Approfondimenti
- Applicazioni complesse
- Ottimizzazioni
```

#### ❌ **Per Decisioni Critiche Senza Verifica**

```
SCENARIO: Sistema medicale embedded

❌ "IA, scrivi algoritmo controllo dosaggio insulina"
   → Copia diretto in produzione

Dati sensibili, vite umane → Serve:
- Revisione esperto
- Testing rigoroso
- Certificazioni
- Validazione multipla
```

---

## 11. Casi d'Uso Reali ITS

### 11.1 Scenario: Progetto Stage Azienda

**Contesto:** Stage in azienda automazione, ti chiedono di sviluppare prototipo sistema monitoraggio macchine.

**Workflow con IA:**

```
GIORNO 1 - Comprensione Requisiti:
"Analizza questi requisiti aziendali e aiutami a:
1. Identificare ambiguità
2. Generare domande chiarificatrici
3. Creare checklist validazione requisiti"

↓

GIORNO 2-3 - Ricerca e Studio:
"Non conosco protocollo Modbus RTU richiesto.
Spiegami:
- Come funziona
- Come implementarlo su Arduino/ESP32
- Librerie disponibili
- Esempi pratici"

"Genera piano studio 2 giorni per padroneggiare Modbus"

↓

GIORNO 4-7 - Prototipazione:
[Usa workflow progetto sezione 8.1]
"Genera architettura sistema"
"Implementa modulo comunicazione Modbus"
"Crea interface HMI basilare"

↓

GIORNO 8-9 - Testing:
"Genera piano testing per sistema Modbus:
- Unit test moduli
- Integration test
- Stress test comunicazione
- Edge cases (disconnessioni, errori)"

↓

GIORNO 10 - Documentazione:
"Genera documentazione tecnica per consegna:
- Architettura sistema
- Manuale installazione
- Troubleshooting comune
- API documentation"

↓

GIORNO 11-12 - Presentazione:
"Prepara presentazione 15min per team aziendale:
- Problema e soluzione
- Demo funzionalità
- Architettura tecnica
- Prossimi step sviluppo"
```

**Risultato:** Progetto completato con qualità professionale, hai imparato Modbus, impressionato azienda.

### 11.2 Scenario: Recupero Esame

**Contesto:** Hai fallito esame Sistemi Embedded, devi recuperare in 2 settimane.

**Piano con IA:**

```
SETTIMANA 1 - Fondamenti:

GIORNO 1-2: Architetture Embedded
"Crea piano studio architetture embedded (ARM, AVR).
Include:
- Concetti chiave per giorno
- Esercizi pratici
- Quiz autovalutazione"

"Per ogni argomento studiato, genera:
1. Riassunto 1 pagina
2. Mappa concettuale (descritta)
3. 5 domande esame probabili"

GIORNO 3-4: Gestione Interrupts
[Stesso approccio]

GIORNO 5-6: Comunicazione (UART, SPI, I2C)
[Stesso approccio]

GIORNO 7: Ripasso e Simulazione
"Simula esame completo con 20 domande miste.
Valuta risposte, indica lacune, genera materiale ripasso."

↓

SETTIMANA 2 - Pratica e Consolidamento:

GIORNO 8-10: Progetti Pratici
"3 mini-progetti embedded che coprano tutti gli argomenti:
1. [Progetto 1]
2. [Progetto 2]  
3. [Progetto 3]
Con test e documentazione."

GIORNO 11-12: Esercizi Esame Precedenti
"Analizza questi testi esami passati.
Genera soluzioni commentate + spiegazioni concettuali."

GIORNO 13: Mock Exam
"Simula esame reale condizioni.
Timer 2 ore, ambiente silenzioso."

GIORNO 14: Revisione Finale
"Basandoti sui miei errori mock exam, genera:
- Checklist ultimi ripasso
- Formule/concetti chiave da memorizzare
- Tips strategici per esame"
```

**Risultato:** Esame passato con buon voto, basi solide acquisite.

### 11.3 Scenario: Tesi ITS

**Contesto:** Tesi finale su "Sistema IoT per Smart Agriculture"

**Mesi 1-2: Ricerca e Progettazione**

```
"Analisi stato dell'arte Smart Agriculture IoT.
Genera:
1. Survey tecnologie attuali
2. Gap nel mercato
3. Opportunità innovazione
4. Bibliografia paper rilevanti"

↓

"Proponi 5 architetture per sistema IoT agricolo con:
- Sensori (suolo, meteo, ecc)
- Edge processing
- Cloud platform
- User interface
Confronta e raccomanda."

↓

"Genera documento progettazione dettagliato:
- Requisiti funzionali/non-funzionali
- Architettura HW/SW
- Diagrammi UML
- Piano implementazione
Stile: Tesi accademica formale"
```

**Mesi 3-4: Implementazione**

```
[Workflow progetto sezione 8.1, applicato a ogni componente]

"Implementa modulo acquisizione sensori"
"Implementa algoritmo irrigazione intelligente"  
"Sviluppa dashboard visualizzazione dati"
"Integra comunicazione MQTT"
```

**Mese 5: Testing e Validazione**

```
"Piano testing completo sistema IoT:
- Unit test componenti
- Integration test
- Field test (agricoltura reale)
- Performance benchmarks
- Reliability testing"

"Analizza dati raccolti durante field test.
Genera grafici prestazioni, statistiche affidabilità."
```

**Mese 6: Scrittura Tesi**

```
"Genera struttura tesi su sistema Smart Agriculture:
- Capitoli principali
- Sezioni per capitolo
- Figura/tabella per sezione
- Bibliografia organizzata"

[Per ogni capitolo:]
"Scrivi bozza capitolo [N]: [Titolo]
Basandoti su materiale raccolto: [paste note/dati]
Stile: Accademico formale, terza persona"

"Revise e migliora capitolo considerando:
- Chiarezza espositiva
- Coerenza tecnica
- Formalismo accademico"
```

**Risultato:** Tesi completa, progetto funzionante, ottima valutazione.

### 11.4 Scenario: Primo Colloquio Tecnico

**Contesto:** Colloquio per posizione Junior Embedded Developer.

**Preparazione:**

```
FASE 1 - Analisi Posizione:
"Analizza job description:
[paste descrizione lavoro]

Identifica:
- Competenze tecniche richieste
- Soft skills ricercate
- Tecnologie/tool citati
- Tipo progetti probabili

Genera piano preparazione mirato."

↓

FASE 2 - Studio Mirato:
"Per ogni tecnologia richiesta [es. FreeRTOS], genera:
- Concetti essenziali da sapere
- Domande colloquio probabili
- Progetti dimostrativi semplici
- Terminologia chiave"

↓

FASE 3 - Mock Interview:
"Simula colloquio tecnico per [posizione].
Fai domande progressive:
- Warm-up (basi)
- Tecniche (problem solving)
- Behavioral (soft skills)
- Case study (progetto reale)

Valuta risposte, da feedback."

↓

FASE 4 - Preparazione Presentazione Portfolio:
"Ho questi 3 progetti da presentare:
[Lista progetti]

Per ciascuno, prepara:
- Elevator pitch (30 sec)
- Demo script (2 min)
- Risposte a domande tecniche probabili
- Slide supporto (1-2 slide)"

↓

FASE 5 - Q&A Preparation:
"Genera 20 domande intelligenti da fare al recruiter/tech lead,
organizzate per categoria:
- Tecnica (tech stack, metodologie)
- Team (struttura, collaboration)
- Crescita (learning, mentorship)
- Progetto (roadmap, challenges)"
```

**Durante Colloquio:**
- Sicurezza acquisita da preparazione
- Risposte strutturate e competenti
- Domande intelligenti dimostrano interesse

**Risultato:** Offerta ricevuta!

---

## 12. Sistema di Organizzazione Personale

### 12.1 Setup Workspace Digitale

#### **Struttura Cartelle Raccomandata**

```
📁 ITS_AI_Workspace/
├── 📁 01_Prompts_Library/
│   ├── 📁 Study/
│   ├── 📁 Code/
│   ├── 📁 Docs/
│   └── 📁 Presentations/
├── 📁 02_Projects/
│   ├── 📁 [Nome_Progetto_1]/
│   │   ├── 📄 README.md
│   │   ├── 📁 code/
│   │   ├── 📁 docs/
│   │   ├── 📁 prompts_used/
│   │   └── 📄 CHANGELOG.md
│   └── 📁 [Nome_Progetto_2]/
├── 📁 03_Study_Notes/
│   ├── 📁 [Materia_1]/
│   └── 📁 [Materia_2]/
├── 📁 04_Code_Snippets/
│   ├── 📁 C/
│   ├── 📁 Arduino/
│   └── 📁 Python/
└── 📁 05_Career/
    ├── 📄 CV.md
    ├── 📄 Cover_Letter_Template.md
    └── 📁 Interview_Prep/
```

### 12.2 Template Tracker Progresso

**File: `PROGRESS_TRACKER.md`**

```markdown
# Progress Tracker - [Anno Accademico]

## Obiettivi Generali
- [ ] Completare corso [Nome]
- [ ] Sviluppare [N] progetti personali
- [ ] Imparare [Tecnologia X]
- [ ] Ottenere stage presso [Tipo Azienda]

## Progetti in Corso

### [Nome Progetto 1]
**Status:** 🟡 In Progress (60%)
**Deadline:** 2024-XX-XX
**Ultima sessione:** 2024-XX-XX

**Tasks:**
- [x] Setup ambiente
- [x] Architettura sistema
- [ ] Implementazione modulo A
- [ ] Testing
- [ ] Documentazione

**Prompts Utili:**
- `prompts/project1_architecture.txt`
- `prompts/project1_testing.txt`

**Note:** [Problemi incontrati, decisioni prese]

---

### [Nome Progetto 2]
[...]

## Materie/Esami

### Sistemi Embedded
**Esame:** 2024-XX-XX
**Status:** 🟢 Preparato

**Argomenti:**
- [x] Architetture
- [x] Interrupts
- [ ] DMA
- [ ] Power Management

**Risorse IA:**
- `prompts/embedded_study_plan.txt`
- `prompts/embedded_quiz.txt`

---

## Skills Development

### Nuove Competenze 2024
- [x] FreeRTOS basics
- [ ] Machine Learning embedded
- [ ] PCB Design

**Per ognuna:**
- Risorse usate
- Progetti pratici
- Certificazioni (se applicable)

---

## Retrospettive Mensili

### Dicembre 2024
**Cosa ha funzionato:**
- [...]

**Cosa migliorare:**
- [...]

**Lezioni apprese:**
- [...]

**Next month focus:**
- [...]
```

### 12.3 Journal Giornaliero

**File: `DAILY_LOG_YYYY-MM.md`**

```markdown
# Daily Log - December 2024

## 2024-12-05
**Time spent:** 4 hours
**Main focus:** Progetto Arduino IoT

### What I did:
- Implementato modulo sensori
- Debuggato problema I2C
- Generato documentazione

### IA Usage:
**Prompts efficaci oggi:**
1. "Debug I2C communication Arduino..."
   → Risolto in 10min invece di ore

**Prompts da migliorare:**
1. "Genera test..." troppo vago
   → Next time: specificare criteri

### Learning:
- Scoperto [nuovo concetto]
- Capito perché [problema] accadeva

### Tomorrow:
- [ ] Continuare testing
- [ ] Scrivere README

---

## 2024-12-06
[...]
```

### 12.4 Checklist Workflow Quotidiano

**All'inizio della sessione studio/lavoro:**

```
□ Apri workspace organizzato
□ Review obiettivi giornata
□ Check deadline imminenti
□ Prepara prompt library (apri file utili)
□ Setup ambiente (IDE, seriale, hardware)
```

**Durante il lavoro:**

```
□ Usa IA per blocchi >15min
□ Salva prompt efficaci subito
□ Documenta decisioni importanti
□ Testa output IA sempre
□ Commit codice frequentemente
```

**A fine sessione:**

```
□ Aggiorna progress tracker
□ Scrivi daily log (5min)
□ Salva prompts nuovi/migliorati
□ Backup lavoro
□ Prepara TODO domani
```

### 12.5 Template Revisione Settimanale

**File: `WEEKLY_REVIEW_YYYY-WXX.md`**

```markdown
# Weekly Review - Week XX, Month YYYY

## Accomplishments
**Projects:**
- [Progetto A]: [milestone raggiunto]
- [Progetto B]: [progresso]

**Study:**
- [Materia X]: [argomenti coperti]
- [Skill Y]: [pratica fatta]

**Code written:** XXX lines
**Prompts created/refined:** XX

## Challenges
**Technical:**
- [Problema 1]: [Come risolto o in progress]

**Learning:**
- [Difficoltà concept]: [Strategia adottata]

## IA Effectiveness
**Best prompts this week:**
1. [Prompt name]: [Perché efficace]

**Improvements needed:**
- [Area da migliorare]

## Metrics
- Hours studied: XX
- Projects progress: [percentuali]
- IA time saved: ~XX hours

## Next Week Goals
- [ ] [Goal 1]
- [ ] [Goal 2]
- [ ] [Goal 3]

## Notes
[Riflessioni libere, idee, spunti futuri]
```

### 12.6 Dashboard Notion (Opzionale)

Se usi Notion, crea dashboard con:

```
┌─────────────────────────────────────┐
│        ITS AI WORKSPACE             │
├─────────────────────────────────────┤
│                                     │
│  📊 PROGRESS OVERVIEW               │
│  ├ Projects: [X/Y completed]       │
│  ├ Exams: [next: Nome - date]      │
│  └ Skills: [learning X, Y, Z]      │
│                                     │
│  🎯 WEEKLY GOALS                    │
│  □ [Goal 1]                         │
│  □ [Goal 2]                         │
│                                     │
│  ⚡ QUICK ACTIONS                   │
│  → New Prompt                       │
│  → New Project                      │
│  → Daily Log                        │
│                                     │
│  📚 DATABASES                       │
│  → Prompts Library                  │
│  → Projects                         │
│  → Study Notes                      │
│  → Code Snippets                    │
│                                     │
└─────────────────────────────────────┘
```

**Vantaggio:** Vista unificata, quick access, mobile-friendly.

---

## 📚 Risorse Supplementari

### Link Utili

**Tool IA:**
- ChatGPT: https://chat.openai.com
- Claude: https://claude.ai
- GitHub Copilot: https://copilot.github.com
- GitHub Student Pack: https://education.github.com/pack

**Prompt Engineering:**
- Learn Prompting: https://learnprompting.org
- Prompt Engineering Guide: https://www.promptingguide.ai

**Community:**
- r/learnprogramming
- r/embedded
- Stack Overflow

### Libri Consigliati

1. **"The Pragmatic Programmer"** - Thomas & Hunt
2. **"Code Complete"** - McConnell
3. **"Making Embedded Systems"** - White

### Canali YouTube

- **Ben Eater** - Computer architecture
- **Andreas Spiess** - Arduino/ESP32 projects
- **Low Level Learning** - C e sistemi embedded

---

## ✅ Checklist Finale

**Prima di iniziare il tuo percorso:**

- [ ] Ho scelto i tool IA da usare
- [ ] Ho creato account necessari
- [ ] Ho ottenuto GitHub Student Pack (Copilot gratis!)
- [ ] Ho setup workspace organizzato
- [ ] Ho scaricato template prompt dalla dispensa
- [ ] Ho creato sistema di tracking progresso
- [ ] Ho letto sezione "Errori da Evitare"
- [ ] Ho capito mentalità corretta (IA = strumento, non scorciatoia)

**Durante il percorso, ricorda di:**

- [ ] Salvare prompt efficaci appena li trovi
- [ ] Validare SEMPRE output IA
- [ ] Documentare progetti mentre lavori
- [ ] Fare retrospettive regolari
- [ ] Condividere conoscenze con colleghi
- [ ] Chiedere aiuto quando bloccato (anche all'IA!)

---

## 🎓 Conclusione

Questa guida ti ha fornito:

✅ **Strumenti** per usare IA efficacemente  
✅ **Template** prompt per ogni situazione  
✅ **Workflow** completi per progetti reali  
✅ **Sistema** di organizzazione personale  
✅ **Best practices** validate  

**Ora dipende da te!**

L'IA è potente, ma sei **TU** che:
- Formuli le domande giuste
- Validi le risposte
- Integri le conoscenze
- Costruisci competenze reali

> **Usa l'IA per diventare uno sviluppatore MIGLIORE,**  
> **non per evitare di diventare uno sviluppatore.**

**Buon lavoro e... buon prompt! 🚀**

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Corso ITS:** IA e Programmazione Assistita  
**Modulo:** Extra - Guida Pratica Studenti

