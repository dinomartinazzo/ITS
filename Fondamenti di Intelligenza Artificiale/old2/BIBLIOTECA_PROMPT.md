# 📚 BIBLIOTECA PROMPT 2025
## Collezione Prompt Professionali per Programmazione con IA
### Corso ITS - Intelligenza Artificiale e Programmazione Assistita

---

## 📑 Indice

1. [Introduzione](#introduzione)
2. [Prompt Generazione Codice C](#prompt-generazione-codice-c)
3. [Prompt Arduino/Embedded](#prompt-arduinoembedded)
4. [Prompt Debugging](#prompt-debugging)
5. [Prompt Testing](#prompt-testing)
6. [Prompt Documentazione](#prompt-documentazione)
7. [Prompt Ottimizzazione](#prompt-ottimizzazione)
8. [Prompt Analisi e Review](#prompt-analisi-e-review)
9. [Prompt Apprendimento](#prompt-apprendimento)
10. [Best Practices Prompting](#best-practices-prompting)

---

## Introduzione

Questa biblioteca contiene **prompt testati e ottimizzati** per uso con LLM moderni (GPT-4, Claude 3.5, Gemini 1.5) nel contesto di programmazione C e Arduino.

**Come usare:**
1. Copia il template prompt
2. Sostituisci `[PARAMETRI]` con valori specifici
3. Aggiungi contesto se necessario
4. Invia all'LLM
5. Valida output con checklist

**Convenzioni:**
- `[MAIUSCOLO]` = parametro da sostituire
- `VINCOLI:` = requisiti tecnici obbligatori
- `OUTPUT:` = formato risposta atteso

---

## Prompt Generazione Codice C

### Template 1: Funzione C Standard

```
# GENERAZIONE FUNZIONE C 2025

Scrivi in **C99 standard** una funzione:

## Firma
```c
[TIPO_RITORNO] [NOME_FUNZIONE]([PARAMETRI]);
```

## Comportamento
[Descrizione dettagliata cosa deve fare la funzione]

## Vincoli Tecnici
- Standard: C99
- NO estensioni POSIX/GNU (NO strdup, strndup, asprintf)
- Usa SOLO librerie standard: stdio.h, stdlib.h, string.h, stdbool.h
- Compilazione: gcc -std=c99 -Wall -Wextra -Wpedantic -Werror

## Gestione Errori
- Controlla puntatori NULL prima dell'uso
- Controlla bounds array
- Ritorna [CODICE_ERRORE] in caso di errore
- Usa defensive programming

## Gestione Memoria
- Se alloca memoria: documenta chi deve chiamare free()
- NO memory leak
- NO double free
- Inizializza puntatori a NULL dopo free()

## Input/Output
- Input: [specifica parametri e pre-condizioni]
- Output: [specifica return value e post-condizioni]
- Side effects: [modifica parametri? I/O? globali?]

## Testing
Genera anche suite test con assert.h:
- Caso normale
- Edge cases (NULL, 0, vuoti, negativi)
- Boundary conditions

## Output Richiesto
1. Header comment Doxygen
2. Implementazione funzione commentata
3. Suite test completa
4. Note su limitazioni/miglioramenti possibili
```

### Template 2: Struttura Dati C

```
# GENERAZIONE STRUTTURA DATI C

Implementa in **C99 standard**:

## Tipo Dati
[es: Lista linkata / Stack / Coda / Hash table]

## Strutture
```c
typedef struct [NOME] {
    [CAMPI]
} [NOME];
```

## Operazioni Richieste
- [ ] Creazione/Inizializzazione
- [ ] Inserimento
- [ ] Ricerca
- [ ] Eliminazione
- [ ] Attraversamento
- [ ] Distruzione completa

## Vincoli
- C99 standard puro
- Gestione memoria esplicita (malloc/free)
- Controlli NULL su tutti puntatori
- Documentazione Doxygen ogni funzione

## Performance
- Complessità temporale target: [O(n), O(1), etc]
- Ottimizza per: [memoria / velocità / entrambe]

## Testing
Test per ogni operazione:
- Caso normale
- Sequenze operazioni
- Edge cases (vuoto, singolo elemento)
- Memory leak (valgrind clean)

## Output
1. Header file (.h) con dichiarazioni
2. Implementation file (.c)
3. Test suite completa
4. Esempio uso
```

### Template 3: Algoritmo Specifico

```
# IMPLEMENTAZIONE ALGORITMO C

Implementa algoritmo **[NOME_ALGORITMO]** in C99:

## Specifica
[Descrizione algoritmo e cosa deve fare]

## Firma Funzione
```c
[TIPO] [nome]([parametri]);
```

## Vincoli
- Standard: C99
- Complessità: [O(n log n) / O(n) / etc]
- Spazio: [O(1) / O(n) / etc]
- NO ricorsione se stack limitato

## Input
- Formato: [array / lista / etc]
- Range valori: [0-100 / negativi ammessi / etc]
- Dimensione: [fissa / variabile]

## Output
- Formato: [modificato in-place / nuovo array / etc]
- Return value: [successo/errore / risultato]

## Casi Speciali
- Array vuoto: [comportamento]
- Singolo elemento: [comportamento]
- Duplicati: [come gestiti]

## Testing
- Dataset piccolo (verifica manuale)
- Dataset grande (performance)
- Edge cases completi

## Output
1. Implementazione ottimizzata
2. Analisi complessità
3. Test con benchmark
```

---

## Prompt Arduino/Embedded

### Template 4: Sketch Arduino Base

```
# SKETCH ARDUINO 2025

Crea sketch Arduino [BOARD] per:

## Hardware
Board: [Arduino Uno / Nano ESP32 / Mega]
Componenti:
- [COMPONENTE_1]: [PIN] ([NOTE])
- [COMPONENTE_2]: [PIN] ([NOTE])
- [...]

## Connessioni Pin
```
[COMPONENTE] → Arduino
  [PIN1] → [ARDUINO_PIN1]
  [PIN2] → [ARDUINO_PIN2]
  ...
```

## Funzionalità
[Descrizione dettagliata comportamento sistema]

Requisiti specifici:
1. [REQUISITO_1]
2. [REQUISITO_2]
3. [...]

## Vincoli Tecnici
- Logica NON-BLOCCANTE: usa millis(), NO delay() lunghi
- Comunicazione seriale: [BAUD_RATE] baud per debug
- Gestione errori: [sensori / hardware]
- Commenti esplicativi per ogni sezione

## Librerie
[Lista librerie Arduino da usare]
- [LIBRERIA_1] versione [X.Y]
- [LIBRERIA_2]

## Timing
- [TASK_1]: ogni [X] millisecondi
- [TASK_2]: ogni [Y] secondi
- [TASK_3]: continuo (polling)

## Gestione Errori
- [ERRORE_1]: [COMPORTAMENTO]
- [ERRORE_2]: [COMPORTAMENTO]

## Output Richiesto
1. Sketch completo con setup() e loop()
2. Tabella pin connections
3. Lista librerie da installare (con versioni)
4. Istruzioni test rapido
5. Note configurazione/calibrazione
```

### Template 5: Integrazione Sensore

```
# INTEGRAZIONE SENSORE ARDUINO

Integra sensore **[NOME_SENSORE]** in sketch Arduino:

## Sensore
Modello: [es: DHT22 / BMP280 / HC-SR04]
Protocollo: [I2C / SPI / Analogico / Digitale]
Datasheet: [link o note chiave]

## Connessioni
```
[SENSORE] → Arduino
  [PIN_1] → [ARDUINO_PIN]
  [PIN_2] → [ARDUINO_PIN]
  ...
```

## Libreria
Nome: [nome libreria ufficiale]
Installazione: [Arduino IDE / PlatformIO]
Versione: [X.Y.Z]

## Funzioni Richieste
```cpp
// Inizializzazione
void setupSensor();

// Lettura dati
[STRUCT_TYPE] readSensor();

// Validazione lettura
bool isValidReading([STRUCT_TYPE] data);
```

## Struct Dati
```cpp
typedef struct {
    [CAMPI_DATI]
    bool valid;  // flag validazione
} SensorData;
```

## Gestione Errori
- Timeout lettura: [TIMEOUT_MS] ms
- Valori fuori range: [MIN]-[MAX]
- Sensore disconnesso: [COMPORTAMENTO]

## Timing
- Frequenza lettura: [X] secondi
- Tempo warm-up: [Y] secondi
- Delay minimo tra letture: [Z] ms

## Calibrazione
[Procedure calibrazione se necessaria]

## Testing
- Test connessione setup
- Test lettura valori noti
- Test gestione errori
- Stress test (1000+ letture)

## Output
1. Codice integrazione completo
2. Esempio uso nel loop()
3. Debug output seriale
4. Note troubleshooting comuni
```

### Template 6: Sistema Multi-Task Arduino

```
# SISTEMA MULTI-TASK ARDUINO

Implementa sistema Arduino con task multipli non-bloccanti:

## Tasks
[Lista task con priorità e timing]

Task 1: [NOME]
- Frequenza: [ogni X ms]
- Priorità: [alta/media/bassa]
- Funzione: [cosa fa]

Task 2: [NOME]
- Frequenza: [ogni Y ms]
- Priorità: [alta/media/bassa]
- Funzione: [cosa fa]

[... altri task]

## Architettura
Pattern: [Simple millis / State Machine / RTOS]

Se State Machine:
```cpp
enum SystemState {
    STATE_[NOME1],
    STATE_[NOME2],
    // ...
};
```

Stati e transizioni:
- [STATO1] → [STATO2]: quando [CONDIZIONE]
- [...]

## Timer Non-Bloccanti
```cpp
unsigned long [task1]PrevMillis = 0;
unsigned long [task2]PrevMillis = 0;
const long [TASK1]_INTERVAL = [X];
const long [TASK2]_INTERVAL = [Y];
```

## Priorità
Se conflitto:
1. [TASK_PRIORITA_1]
2. [TASK_PRIORITA_2]
3. [...]

## Gestione Overflow millis()
Gestisci correttamente rollover 49 giorni

## Sincronizzazione
[Come task comunicano tra loro]
- Variabili globali: [quali]
- Flag: [quali]

## Output
1. Sketch con architettura multi-task
2. Diagramma stati (se State Machine)
3. Timing analysis (worst-case)
4. Note ottimizzazione
```

---

## Prompt Debugging

### Template 7: Debug Errore Compilatore

```
# DEBUG ERRORE COMPILATORE C

Ho questo codice C che genera errore di compilazione:

## Codice
```c
[INCOLLA CODICE COMPLETO]
```

## Errore Compilatore
```
[INCOLLA OUTPUT ERRORE COMPLETO]
```

## Contesto
- Compilatore: [gcc / clang] versione [X.Y]
- Flag compilazione: [es: -std=c99 -Wall -Wextra]
- OS: [Windows / Linux / Mac]
- Cosa dovrebbe fare: [descrizione funzionalità]

## Analizza e Fornisci

1. **Root Cause**
   - Causa esatta dell'errore
   - Riga/e problematiche
   - Perché il compilatore si lamenta

2. **Spiegazione Tecnica**
   - Cosa viola lo standard C
   - Regole linguaggio coinvolte
   - Esempi simili

3. **Fix Completo**
   - Codice corretto commentato
   - Evidenzia modifiche
   - Spiega ogni cambio

4. **Prevenzione Futura**
   - Come evitare in futuro
   - Best practice correlate
   - Tool/warning da usare

5. **Test di Validazione**
   - Come verificare fix
   - Test case da provare
```

### Template 8: Debug Runtime Arduino

```
# DEBUG COMPORTAMENTO RUNTIME ARDUINO

Sketch Arduino con comportamento anomalo:

## Codice
```cpp
[INCOLLA SKETCH]
```

## Problema
Comportamento atteso:
[DESCRIZIONE]

Comportamento attuale:
[DESCRIZIONE]

## Sintomi
- [SINTOMO_1]
- [SINTOMO_2]
- [...]

## Setup Hardware
- Board: [Arduino Uno / etc]
- Componenti: [lista]
- Alimentazione: [USB / esterna XVolt]

## Osservazioni
- Serial monitor output: [se disponibile]
- LED/indicatori: [comportamento]
- Quando si manifesta: [sempre / random / dopo X min]

## Tentativi Fatti
- [TENTATIVO_1]: [risultato]
- [TENTATIVO_2]: [risultato]

## Debug Richiesto

1. **Analisi Codice**
   - Identifica possibili cause
   - Bug logica / timing / hardware

2. **Ipotesi Problemi**
   - Problema più probabile
   - Problemi secondari possibili

3. **Debug Steps**
   - Aggiungi debug print strategici
   - Test da fare per isolare
   - Measurements con multimetro

4. **Fix Proposto**
   - Codice corretto
   - Spiegazione modifiche
   - Perché dovrebbe funzionare

5. **Verifica**
   - Come testare il fix
   - Cosa monitorare
```

### Template 9: Debug Memory Leak C

```
# DEBUG MEMORY LEAK C

Programma C con sospetto memory leak:

## Codice
```c
[INCOLLA CODICE]
```

## Evidenza Leak
- Valgrind output: [se disponibile]
- Comportamento: [memoria cresce / crash dopo X minuti]
- Contesto: [quando si manifesta]

## Analizza

1. **Leak Detection**
   - Identifica malloc senza free corrispondente
   - Puntatori persi
   - Realloc problematici

2. **Leak Paths**
   - Percorsi esecuzione che causano leak
   - Condizioni specifiche

3. **Fix Completo**
   - Codice corretto
   - Aggiungi free() mancanti
   - Pattern ownership chiaro

4. **Validazione**
   - Comando valgrind da usare
   - Output atteso (0 bytes leaked)

5. **Best Practices**
   - Pattern safe da usare sempre
   - Tool automatici (sanitizers)
```

---

## Prompt Testing

### Template 10: Generazione Suite Test

```
# GENERAZIONE TEST SUITE C

Genera test completi per questa funzione C:

## Funzione da Testare
```c
[INCOLLA FIRMA E IMPLEMENTAZIONE]
```

## Test Richiesti

1. **Unit Tests**
   - Casi normali (happy path)
   - Edge cases: NULL, 0, vuoti, negativi
   - Boundary conditions (min, max, overflow)
   - Invalid input

2. **Framework**
   Usa assert.h (C standard):
   ```c
   #include <assert.h>
   ```

3. **Struttura**
   ```c
   void test_[funzione]_[scenario]() {
       // Setup
       // Execute
       // Assert
       // Cleanup
   }
   ```

4. **Coverage**
   - Tutti branch if/else
   - Tutti casi switch
   - Loop: 0, 1, many iterations
   - Errori gestiti

5. **Main Test**
   ```c
   int main() {
       test_caso1();
       test_caso2();
       // ...
       printf("✅ All tests passed!\n");
       return 0;
   }
   ```

## Output
1. File test completo compilabile
2. Commenti su cosa testa ogni assert
3. Note su coverage raggiunta
4. Comando compilazione ed esecuzione
```

### Template 11: Test Hardware Arduino

```
# TEST PLAN HARDWARE ARDUINO

Genera piano test per progetto Arduino:

## Sistema
[Descrizione setup hardware e funzionalità]

## Test Checklist

### Unit Tests (Componenti Singoli)
- [ ] Test sensore 1: [NOME]
  - Lettura valori corretti
  - Gestione disconnessione
  - Timing rispettato

- [ ] Test attuatore 1: [NOME]
  - Risponde a comandi
  - Range operativo corretto

- [ ] Test display: [NOME]
  - Testo leggibile
  - Update senza flicker

[... altri componenti]

### Integration Tests
- [ ] Test comunicazione moduli
- [ ] Test timing multi-task
- [ ] Test gestione errori

### System Tests
- [ ] Test scenario normale
- [ ] Test condizioni estreme
- [ ] Test lungo periodo (8+ ore)

### Stress Tests
- [ ] Test sotto carico
- [ ] Test memory usage
- [ ] Test overflow/rollover

## Procedure Test

Per ogni test:
1. **Setup**: [cosa preparare]
2. **Esecuzione**: [steps]
3. **Verifica**: [cosa controllare]
4. **Criteri pass/fail**: [valori attesi]

## Test Automation

Funzioni test automatiche dove possibile:
```cpp
bool testSensor() {
    // return true se pass
}
```

## Output
1. Checklist stampabile
2. Codice test automatici
3. Test log template
4. Criteri accettazione
```

---

## Prompt Documentazione

### Template 12: README.md Progetto

```
# GENERAZIONE README.MD PROFESSIONALE

Genera README.md completo per:

## Progetto
Nome: [NOME_PROGETTO]
Tipo: [Arduino / C library / Tool]
Scopo: [descrizione breve]

## Informazioni
- Linguaggio: [C / C++ / Arduino]
- Board: [se applicabile]
- Licenza: [MIT / GPL / Apache]

## Sezioni README

### 1. Header
- Titolo con emoji appropriata
- Badge: ![Arduino](shields.io badge)
- Badge: ![License](license badge)
- Tagline breve (1 frase)

### 2. Features
Lista bullet delle funzionalità principali con emoji:
- 🎯 [feature 1]
- ⚡ [feature 2]
[...]

### 3. Hardware (se Arduino)
Tabella BOM (Bill of Materials):
| Componente | Qty | Note |
|---|---|---|

### 4. Wiring/Collegamenti
Schema connessioni in formato code block:
```
[Component] → Arduino
  Pin1 → PinX
  ...
```

### 5. Installazione
Steps numerati:
1. Installa [tool]
2. Clona repository
3. [...]

### 6. Configurazione
Parametri configurabili

### 7. Uso
Esempi pratici

### 8. Documentazione API
(se libreria)

### 9. Testing
Come testare

### 10. Troubleshooting
FAQ problemi comuni

### 11. Sviluppi Futuri
Roadmap

### 12. Contributi
Come contribuire

### 13. Licenza
Dettagli licenza

### 14. Autore
Info contatti

## Stile
- Markdown professionale
- Emoji moderate
- Code blocks evidenziati
- Immagini/diagrammi (descrizione)
- Beginner-friendly

## Output
README.md completo pronto per GitHub
```

### Template 13: Commenti Codice Doxygen

```
# DOCUMENTAZIONE CODICE DOXYGEN

Genera commenti Doxygen professionali per:

## Codice
```c
[INCOLLA FUNZIONE/STRUCT/FILE]
```

## Formato Doxygen

### Per Funzioni
```c
/**
 * @brief [Descrizione breve 1 riga]
 *
 * [Descrizione dettagliata multi-riga se necessario]
 *
 * @param [nome_param] [descrizione]
 * @param [nome_param2] [descrizione]
 * @return [descrizione return value]
 * @retval [valore_speciale] [quando ritorna questo]
 *
 * @note [Note importanti]
 * @warning [Warning critici]
 *
 * @pre [Pre-condizioni]
 * @post [Post-condizioni]
 *
 * @see [riferimenti altre funzioni]
 *
 * @example
 * [esempio uso]
 */
```

### Per Struct
```c
/**
 * @brief [Descrizione struct]
 * @struct [nome]
 *
 * [Dettagli uso]
 */
typedef struct {
    int campo1;  /**< descrizione campo */
    int campo2;  /**< descrizione campo */
} Nome;
```

### Per File
```c
/**
 * @file [nome_file.c]
 * @brief [Scopo file]
 * @author [Nome Autore]
 * @date [Data]
 * @version [X.Y.Z]
 *
 * [Descrizione contenuto]
 */
```

## Output
Codice con commenti Doxygen completi
```

---

## Prompt Ottimizzazione

### Template 14: Ottimizzazione Performance

```
# OTTIMIZZAZIONE PERFORMANCE C/ARDUINO

Ottimizza questo codice per performance:

## Codice Attuale
```c
[INCOLLA CODICE]
```

## Profiling Info
[Se disponibile]
- Funzione più lenta: [nome] ([X]ms)
- Memoria usata: [Y] bytes
- Bottleneck identificato: [descrizione]

## Obiettivi Ottimizzazione
- [ ] Ridurre tempo esecuzione: target [X]ms
- [ ] Ridurre uso RAM: target [Y] bytes
- [ ] Ridurre consumo energia (se embedded)
- [ ] Altro: [specifica]

## Vincoli
- Mantenere leggibilità: [alta/media]
- Compatibilità: [C99 / Arduino]
- NO assembly inline
- NO inline assembly

## Tecniche da Applicare
- Loop unrolling
- Strength reduction
- Eliminazione calcoli ridondanti
- Cache-friendly data structures
- Uso PROGMEM (Arduino)
- Integer al posto float dove possibile

## Output Richiesto
1. **Codice Ottimizzato**
   - Con commenti su ottimizzazioni
   - Before/After per ogni cambio

2. **Analisi Performance**
   - Speedup atteso
   - Trade-off (memoria vs velocità)

3. **Benchmark**
   - Come misurare miglioramento
   - Test da fare

4. **Note**
   - Optimizations applicate
   - Limitazioni
   - Ulteriori miglioramenti possibili
```

### Template 15: Ottimizzazione Memoria Arduino

```
# OTTIMIZZAZIONE MEMORIA ARDUINO

Riduci uso RAM di questo sketch Arduino:

## Sketch Attuale
```cpp
[INCOLLA CODICE]
```

## Situazione Memoria
- Board: [Arduino Uno / Mega / etc]
- RAM totale: [X] bytes
- RAM usata: [Y] bytes ([Z]%)
- Target: < [W]%

## RAM Usage Report
[Da Arduino IDE: Sketch → Verify/Compile]
```
Global variables use X bytes (Y%) of dynamic memory
```

## Tecniche Ottimizzazione

1. **Stringhe in PROGMEM**
   ```cpp
   const char str[] PROGMEM = "...";
   ```

2. **F() Macro per Seriale**
   ```cpp
   Serial.println(F("testo"));
   ```

3. **Eliminare String class**
   Usare char[] statici

4. **Ottimizzare struct**
   - Padding aware
   - Bitfields dove appropriato

5. **Buffer statici riusabili**

6. **Const/static dove possibile**

## Output
1. Sketch ottimizzato
2. Prima/dopo ogni cambio
3. Nuovo RAM usage
4. Checklist applicata
```

---

## Prompt Analisi e Review

### Template 16: Code Review

```
# CODE REVIEW C/ARDUINO

Fai review professionale di questo codice:

## Codice
```c
[INCOLLA CODICE]
```

## Contesto
- Linguaggio: [C99 / Arduino]
- Scopo: [descrizione funzionalità]
- Target: [embedded / desktop / etc]

## Aspetti da Revieware

### 1. Correttezza
- [ ] Implementazione corretta
- [ ] Edge cases gestiti
- [ ] Nessun bug ovvio

### 2. Sicurezza
- [ ] Buffer overflow check
- [ ] Null pointer check
- [ ] Integer overflow
- [ ] Memory leak

### 3. Performance
- [ ] Algoritmi efficienti
- [ ] Uso memoria ottimale
- [ ] NO operazioni ridondanti

### 4. Maintainability
- [ ] Codice leggibile
- [ ] Naming chiaro
- [ ] Commenti utili
- [ ] Struttura modulare

### 5. Best Practices
- [ ] Coding standard rispettato
- [ ] Gestione errori completa
- [ ] Resource cleanup (RAII pattern)

### 6. Portabilità
- [ ] C99 standard compliance
- [ ] NO dipendenze platform-specific

## Output Review

### Issues Trovati
Per ogni issue:
**[SEVERITY: CRITICAL/HIGH/MEDIUM/LOW]**
- Riga: [X]
- Problema: [descrizione]
- Fix suggerito: [codice]

### Suggestions
- [miglioramenti non critici]

### Positives
- [cosa è fatto bene]

### Overall Rating
[1-10] con motivazione
```

### Template 17: Analisi Sicurezza

```
# SECURITY ANALYSIS C CODE

Analizza sicurezza di questo codice C:

## Codice
```c
[INCOLLA CODICE]
```

## Scope
- Tipo applicazione: [embedded / server / etc]
- Input source: [user / network / sensor]
- Privilegi: [user / system]

## Vulnerabilità da Cercare

### Memory Safety
- [ ] Buffer overflow (strcpy, strcat, gets)
- [ ] Heap overflow
- [ ] Stack overflow
- [ ] Use after free
- [ ] Double free
- [ ] Memory leak (DoS)

### Integer Issues
- [ ] Integer overflow/underflow
- [ ] Signedness issues
- [ ] Type confusion

### Input Validation
- [ ] Unvalidated input
- [ ] Format string bugs
- [ ] Injection flaws

### Race Conditions
- [ ] TOCTOU (Time of Check Time of Use)
- [ ] Unsafe globals

### Crypto
- [ ] Weak RNG
- [ ] Hardcoded secrets

## Report

### Vulnerabilities Found
Per ogni vulnerabilità:
**CVE Reference (se applicabile)**
- Severity: [CRITICAL/HIGH/MEDIUM/LOW]
- Type: [buffer overflow/etc]
- Location: Line [X]
- Exploit scenario: [descrizione]
- Fix: [codice sicuro]

### Mitigations
- Compiler flags: [-fstack-protector, -D_FORTIFY_SOURCE=2]
- Static analysis: [tool da usare]

### Security Score
[0-10] con giustificazione
```

---

## Prompt Apprendimento

### Template 18: Spiegazione Codice

```
# SPIEGAZIONE CODICE

Spiega questo codice C/Arduino in dettaglio:

## Codice
```c
[INCOLLA CODICE]
```

## Livello Target
[Beginner / Intermediate / Advanced]

## Spiegazione Richiesta

### 1. Overview
- Cosa fa il codice (high-level)
- Perché è strutturato così

### 2. Step-by-Step
Spiega riga per riga o blocco per blocco:
- Cosa fa
- Perché è necessario
- Come funziona

### 3. Concetti Chiave
Approfondisci:
- [Concetto_1]: [spiegazione]
- [Concetto_2]: [spiegazione]
- Pattern usati

### 4. Variazioni
- Come modificare per [caso_uso_diverso]
- Approcci alternativi

### 5. Pitfalls
- Errori comuni da evitare
- Cosa NON fare

## Formato Output
- Spiegazione chiara per livello target
- Esempi concreti
- Analogie se utili
- Codice annotato inline
```

### Template 19: Tutorial Step-by-Step

```
# TUTORIAL PROGRAMMAZIONE

Crea tutorial step-by-step per:

## Obiettivo
[es: "Imparare a usare I2C su Arduino"]

## Target Audience
Livello: [Beginner / Intermediate]
Prerequisiti: [cosa devono già sapere]

## Struttura Tutorial

### Introduzione (10%)
- Cosa impareranno
- Perché è utile
- Cosa serve (HW/SW)

### Teoria (20%)
- Concetti fondamentali
- Come funziona sotto il cofano
- Terminologia chiave

### Pratica (60%)
Esercizi progressivi:

#### Esercizio 1: [Nome]
Difficoltà: ⭐
- Obiettivo: [cosa si impara]
- Codice starter
- Steps guidati
- Soluzione completa
- Cosa abbiamo imparato

#### Esercizio 2: [Nome]
Difficoltà: ⭐⭐
[...]

#### Progetto Finale
Difficoltà: ⭐⭐⭐
- Combina tutti concetti
- Specifiche
- Hints (no soluzione completa)

### Troubleshooting (10%)
- Problemi comuni
- Soluzioni

### Next Steps
- Cosa studiare dopo
- Risorse aggiuntive

## Stile
- Linguaggio chiaro e friendly
- Tanti esempi
- Diagrammi (descrizione verbale)
- Checkpoint verifica comprensione

## Output
Tutorial markdown completo pronto per pubblicazione
```

---

## Best Practices Prompting

### Regole d'Oro

1. **Sii Specifico**
   ❌ "Scrivi codice Arduino"
   ✅ "Scrivi sketch Arduino Uno per LED RGB su pin 9,10,11 con fade effect"

2. **Specifica Standard**
   ❌ "Usa C"
   ✅ "Usa C99 standard, NO estensioni POSIX"

3. **Chiedi Validazione**
   ✅ "Includi anche test con assert.h"

4. **Contesto Completo**
   ✅ Include: hardware, vincoli, obiettivi

5. **Output Strutturato**
   ✅ "Output: 1. Codice 2. Test 3. Note"

6. **Esempi Input/Output**
   ✅ Mostra esempi concreti quando possibile

### Checklist Prompt Efficace

```
[ ] Obiettivo chiaro?
[ ] Standard/versione specificata?
[ ] Vincoli tecnici elencati?
[ ] Formato output definito?
[ ] Contesto sufficiente?
[ ] Esempi inclusi (se utili)?
[ ] Criteri validazione chiari?
```

### Prompt Engineering Patterns

#### Pattern 1: Chain of Thought
Chiedi ragionamento esplicito:
```
"Prima analizza il problema, poi proponi architettura,
poi implementa con spiegazioni per ogni scelta."
```

#### Pattern 2: Few-Shot
Fornisci esempi:
```
"Esempio 1: [input] → [output]
 Esempio 2: [input] → [output]
 Ora fai per: [nuovo input]"
```

#### Pattern 3: Role Playing
Assegna ruolo:
```
"Sei un senior embedded engineer.
Rivedi questo codice come faresti in code review professionale."
```

#### Pattern 4: Iterative Refinement
Migliora in passi:
```
"Step 1: Implementa versione base funzionante
 Step 2: Aggiungi gestione errori
 Step 3: Ottimizza performance"
```

---

## 🎯 Quick Reference

### Prompt Veloce Generazione Codice
```
"Scrivi in C99 funzione [NOME]([PARAMETRI]) che [COSA_FA].
Vincoli: NO POSIX, gestione errori completa, test inclusi."
```

### Prompt Veloce Debug
```
"Debug questo codice C:
[CODICE]
Errore: [MESSAGGIO]
Spiega causa e fornisci fix."
```

### Prompt Veloce Arduino
```
"Sketch Arduino [BOARD] con [SENSORE] su pin [X].
Funzionalità: [COSA_FA].
Usa millis(), NO delay lunghi."
```

### Prompt Veloce Documentazione
```
"Genera README.md per [PROGETTO]:
- Features
- BOM
- Wiring
- Setup
- Uso
Stile: professionale, markdown."
```

---

## 📊 Metriche Qualità Prompt

**Prompt di Qualità Alta:**
- Specificità: 9/10
- Vincoli chiari: Sì
- Output definito: Sì
- Validazione: Test inclusi
- Risultato: Codice production-ready al primo colpo

**Prompt di Qualità Bassa:**
- Specificità: 3/10
- Vincoli: Vaghi
- Output: Generico
- Validazione: Assente
- Risultato: Richiede 5+ iterazioni

---

## 🚀 Workflow Ottimale

```
1. DEFINISCI obiettivo preciso
   ↓
2. SCEGLI template appropriato
   ↓
3. PERSONALIZZA con specifiche
   ↓
4. INVIA a LLM (GPT-4/Claude 3.5/Gemini)
   ↓
5. VALIDA output con checklist
   ↓
6. TESTA codice generato
   ↓
7. ITERA se necessario (max 2-3 volte)
   ↓
8. DOCUMENTA prompt efficaci per riuso
```

---

## 📝 Note Finali

Questa biblioteca è **viva** e va **aggiornata**:
- Aggiungi prompt che funzionano bene per te
- Annota LLM e versione usata
- Condividi con team/classe
- Fai versioning (Git)

**Last Updated:** Gennaio 2025
**Tested with:** GPT-4 Turbo, Claude 3.5 Sonnet, Gemini 1.5 Pro

---

**Fine Biblioteca Prompt** 📚✨

*Usa saggiamente, valida sempre, codifica sicuro!*
