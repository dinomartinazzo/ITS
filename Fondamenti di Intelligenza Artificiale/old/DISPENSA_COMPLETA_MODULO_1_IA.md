# 📘 DISPENSA COMPLETA - MODULO 1
# Fondamenti di Intelligenza Artificiale
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 2 ore | Livello: Introduttivo

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Cos'è l'Intelligenza Artificiale](#2-cosè-lintelligenza-artificiale)
3. [Storia e Evoluzione dell'IA](#3-storia-e-evoluzione-dellia)
4. [Categorie dell'IA](#4-categorie-dellia)
5. [Modelli Linguistici (LLM)](#5-modelli-linguistici-llm)
6. [Limiti e Rischi dell'IA](#6-limiti-e-rischi-dellia)
7. [Applicazioni in Ambito ITS](#7-applicazioni-in-ambito-its)
8. [Casi Studio Pratici](#8-casi-studio-pratici)
9. [Esercizi e Autovalutazione](#9-esercizi-e-autovalutazione)
10. [Glossario Tecnico](#10-glossario-tecnico)

---

## 1. Introduzione e Obiettivi

### 1.1 Benvenuti al Corso

Benvenuti al **Modulo 1** del corso di Intelligenza Artificiale e Programmazione Assistita. Questo modulo rappresenta la base teorica su cui costruiremo tutte le competenze pratiche dei moduli successivi.

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo sarai in grado di:

✅ **Comprendere** cos'è l'intelligenza artificiale e come funziona  
✅ **Distinguere** tra diverse categorie di IA (simbolica, ML, DL, LLM)  
✅ **Identificare** i limiti tecnici e i rischi dei sistemi IA  
✅ **Riconoscere** applicazioni reali in contesti industriali e embedded  
✅ **Valutare criticamente** output generati da sistemi IA  

### 1.3 Prerequisiti

- Nessun prerequisito specifico
- Conoscenze informatiche di base
- Curiosità e spirito critico

### 1.4 Materiali Necessari

- Questa dispensa
- Accesso a un sistema IA (ChatGPT, Claude, ecc.)
- Quaderno per appunti
- Computer per esercizi pratici

---

## 2. Cos'è l'Intelligenza Artificiale

### 2.1 Definizione

> **Intelligenza Artificiale (IA)**: insieme di tecniche computazionali progettate per permettere a un sistema di svolgere compiti che normalmente richiederebbero intelligenza umana.

L'IA non è una tecnologia singola, ma una **famiglia di approcci** che include:
- Riconoscimento di pattern
- Decision making
- Predizione
- Classificazione
- Generazione di contenuti

### 2.2 IA vs Algoritmi Tradizionali

#### **Approccio Algoritmico Classico**

```
SE temperatura > 30 ALLORA
    accendi_ventilatore()
ALTRIMENTI
    spegni_ventilatore()
FINE
```

**Caratteristiche:**
- ✅ Regole deterministiche chiare
- ✅ Comportamento prevedibile al 100%
- ✅ Facile debugging
- ❌ Rigido, non si adatta
- ❌ Richiede regole esplicite per ogni caso

#### **Approccio IA/Machine Learning**

```
Modello addestrato su:
- 10.000 esempi di temperature e azioni corrette
- Pattern complessi di comfort termico
- Preferenze utenti

Risultato:
- Predice azione ottimale anche per situazioni mai viste
- Si adatta a nuovi pattern
- Può gestire incertezza
```

**Caratteristiche:**
- ✅ Generalizza da esempi
- ✅ Gestisce complessità
- ✅ Si adatta a nuovi scenari
- ❌ Possibile errore intrinseco
- ❌ Meno prevedibile
- ❌ Richiede dati di addestramento

### 2.3 Quando Usare IA vs Algoritmi Classici

| **Usa Algoritmo Classico** | **Usa IA** |
|---|---|
| Regole chiare e stabili | Pattern complessi e nascosti |
| Comportamento predicibile richiesto | Adattamento necessario |
| Pochi casi da gestire | Migliaia di varianti possibili |
| Esempio: Calcolo IVA | Esempio: Riconoscimento vocale |

### 2.4 Esempio Pratico Comparativo

**Problema:** Classificare email come spam o non-spam

**Soluzione Algoritmica:**
```
IF contiene("viagra") OR contiene("vinto") THEN spam
```
- Pro: veloce, chiaro
- Contro: facilmente aggirabile, incompleto

**Soluzione IA:**
```
Addestramento su 100.000 email etichettate
Modello impara:
- Pattern linguistici dello spam
- Strutture sintattiche sospette
- Combinazioni di parole
- Metadati (mittente, orario, ecc.)
```
- Pro: molto più accurato, robusto
- Contro: richiede dati, meno trasparente

---

## 3. Storia e Evoluzione dell'IA

### 3.1 Timeline Essenziale

```
1950  | Test di Turing - "Can machines think?"
1956  | Conferenza di Dartmouth - nasce il termine "AI"
1980s | Sistemi esperti e IA simbolica
1990s | Machine Learning prende piede
2012  | Deep Learning vince ImageNet
2017  | Transformer architecture (base dei LLM)
2022  | ChatGPT - IA mainstream
2024  | IA integrata in sviluppo software
```

### 3.2 Le Tre Ondate dell'IA

#### **Prima Ondata (1950-1980): IA Simbolica**
- Basata su logica e regole
- Sistemi esperti
- Limitata a domini ristretti

#### **Seconda Ondata (1980-2010): Machine Learning**
- Apprendimento da dati
- Algoritmi statistici
- Applicazioni specifiche

#### **Terza Ondata (2010-oggi): Deep Learning e LLM**
- Reti neurali profonde
- Capacità generative
- Applicazioni generaliste

### 3.3 Perché Ora?

L'IA moderna è possibile grazie a tre fattori:

1. **Big Data**: miliardi di esempi disponibili
2. **Computing Power**: GPU e cloud computing
3. **Algoritmi Migliorati**: transformer, attention mechanism

---

## 4. Categorie dell'IA

### 4.1 Panoramica

```
Intelligenza Artificiale
│
├── IA Simbolica (rule-based)
│   └── Sistemi esperti, logica
│
├── Machine Learning (statistico)
│   ├── Supervisionato
│   ├── Non supervisionato
│   └── Reinforcement Learning
│
├── Deep Learning (reti neurali)
│   ├── Computer Vision
│   ├── NLP
│   └── Audio/Speech
│
└── IA Generativa (LLM, diffusion models)
    ├── Modelli linguistici
    ├── Generazione immagini
    └── Generazione codice
```

### 4.2 IA Simbolica

#### **Cos'è**
Sistema basato su regole logiche esplicite programmate dall'uomo.

#### **Esempio: Sistema Esperto Medico**
```
REGOLA 1: SE febbre > 38 E mal_di_gola ALLORA possibile_influenza
REGOLA 2: SE possibile_influenza E tosse ALLORA consiglia_riposo
REGOLA 3: SE febbre > 39 ALLORA allerta_medico
```

#### **Vantaggi**
- ✅ Trasparente (si capisce perché decide così)
- ✅ Verificabile
- ✅ Non richiede dati di addestramento

#### **Svantaggi**
- ❌ Rigido
- ❌ Non scala a problemi complessi
- ❌ Richiede codifica manuale di tutte le regole

### 4.3 Machine Learning

#### **4.3.1 Supervised Learning (Apprendimento Supervisionato)**

**Principio:** Impara da esempi etichettati

**Processo:**
```
INPUT (dati) + LABEL (etichetta corretta)
        ↓
   [ADDESTRAMENTO]
        ↓
    MODELLO ADDESTRATO
        ↓
   Predice label per nuovi dati
```

**Esempio Pratico: Classificazione Frutti**

Dataset di addestramento:
```
Immagine_1: mela rossa, rotonda, 200g → MELA
Immagine_2: banana gialla, lunga, 150g → BANANA
Immagine_3: mela verde, rotonda, 180g → MELA
... (1000 esempi)
```

Dopo addestramento:
```
Nuova_immagine: oggetto rosso, rotondo, 190g
Modello predice: MELA (98% confidenza)
```

**Applicazioni:**
- Classificazione email spam
- Diagnosi mediche
- Previsione prezzi
- Riconoscimento immagini

#### **4.3.2 Unsupervised Learning (Non Supervisionato)**

**Principio:** Trova pattern senza etichette

**Esempio: Clustering Clienti**
```
Dataset: 10.000 clienti con abitudini d'acquisto
Algoritmo trova automaticamente gruppi:

Gruppo A: Giovani, tech, acquisti online
Gruppo B: Famiglie, spesa settimanale, negozi fisici
Gruppo C: Senior, prodotti salute, acquisti sporadici
```

**Applicazioni:**
- Segmentazione mercato
- Rilevamento anomalie
- Compressione dati

#### **4.3.3 Reinforcement Learning**

**Principio:** Impara per tentativi ed errori con rinforzi

**Esempio: Robot che Impara a Camminare**
```
Tentativo 1: Cade subito → Ricompensa: -10
Tentativo 2: 2 passi poi cade → Ricompensa: +5
Tentativo 3: 10 passi → Ricompensa: +50
...
Dopo 1000 tentativi: Cammina stabilmente
```

**Applicazioni:**
- Giochi (AlphaGo, scacchi)
- Robotica
- Auto autonome
- Ottimizzazione processi

### 4.4 Deep Learning

#### **Cos'è**
Sottocategoria del ML che usa reti neurali "profonde" (molti strati).

#### **Architettura Base**
```
INPUT (es. immagine)
    ↓
[Layer 1: rileva bordi]
    ↓
[Layer 2: rileva forme semplici]
    ↓
[Layer 3: rileva parti (occhi, naso)]
    ↓
[Layer 4: rileva oggetti completi]
    ↓
OUTPUT (es. "gatto" 95%)
```

#### **Perché "Deep"?**
- Molti strati di elaborazione
- Ogni strato apprende rappresentazioni sempre più astratte
- Capacità di gestire problemi molto complessi

#### **Applicazioni Famose**
- **Computer Vision**: riconoscimento facciale, auto autonome
- **NLP**: traduzione, assistenti vocali
- **Giochi**: AlphaGo, OpenAI Five

### 4.5 IA Generativa e LLM

**Novità:** Non solo classifica/predice, ma **genera** nuovi contenuti.

#### **Tipi:**
- **LLM** (Large Language Models): generano testo
- **Diffusion Models**: generano immagini (DALL-E, Midjourney)
- **Audio/Video**: generano voce, musica, video

Approfondiremo gli LLM nella prossima sezione.

---

## 5. Modelli Linguistici (LLM)

### 5.1 Cos'è un LLM

> **LLM (Large Language Model)**: Modello di IA addestrato su enormi quantità di testo per comprendere e generare linguaggio naturale.

**Esempi:**
- GPT-4 (OpenAI)
- Claude (Anthropic)
- Gemini (Google)
- LLaMA (Meta)

### 5.2 Come Funziona un LLM

#### **Processo di Addestramento**

**Fase 1: Pre-training**
```
Dataset: Miliardi di pagine web, libri, codice
Compito: Predire la prossima parola

Esempio:
Input: "Il gatto è salito sul..."
Modello impara: probabilmente "tetto" o "divano" o "albero"

Ripetuto trilioni di volte su vari testi
```

**Fase 2: Fine-tuning**
```
Addestramento specifico su:
- Conversazioni di qualità
- Istruzioni e risposte
- Feedback umano

Risultato: Modello che segue istruzioni
```

#### **Generazione di Testo**

```
Input utente: "Spiega cos'è un array"

Processo interno:
Token 1: "Un" (probabilità 0.85)
Token 2: "array" (probabilità 0.92)
Token 3: "è" (probabilità 0.98)
Token 4: "una" (probabilità 0.88)
Token 5: "struttura" (probabilità 0.75)
... continua token per token

Output: "Un array è una struttura dati che..."
```

**Caratteristica chiave:** Generazione **probabilistica**, non deterministica.

### 5.3 Architettura Transformer

Gli LLM moderni usano l'architettura **Transformer** (2017).

#### **Componenti Chiave:**

**1. Attention Mechanism**
```
Permette al modello di "prestare attenzione" a parole rilevanti:

Frase: "Il gatto, che era molto affamato, mangiò"
Predizione prossima parola:
- Alta attenzione a: "gatto", "affamato"
- Bassa attenzione a: "che", "era"
→ Predice: "tutto" o "velocemente"
```

**2. Positional Encoding**
- Codifica la posizione delle parole
- Permette di capire l'ordine

**3. Multi-Head Attention**
- Analizza il testo da molteplici prospettive simultaneamente

### 5.4 Capacità e Limiti

#### **Capacità Sorprendenti**

✅ **Comprensione Contestuale**
```
"Banco" in:
- "Vado in banco" → istituzione finanziaria
- "Banco di scuola" → mobile
- "Banco di pesci" → gruppo
```

✅ **Ragionamento Base**
```
Q: "Se ho 3 mele e ne mangio 2, quante ne rimangono?"
A: "Rimane 1 mela"
```

✅ **Generazione Creativa**
- Scrittura articoli
- Poesie
- Codice

✅ **Traduzione**
- Multi-lingua
- Mantiene contesto e stile

#### **Limiti Critici**

❌ **Conoscenza Limitata**
- Taglio temporale (knowledge cutoff)
- Non accede a dati in tempo reale

❌ **No Ragionamento Logico Perfetto**
```
Problema:
"Se tutti i gatti sono animali e tutti gli animali respirano,
allora i gatti respirano?"

LLM: Spesso corretto (ha visto pattern simili)
Ma: Non fa deduzione logica formale
```

❌ **No Comprensione Vera**
- Manipola pattern statistici
- Non "capisce" davvero il significato

❌ **Allucinazioni** (vedi sezione successiva)

### 5.5 Tokenizzazione

Prima di essere elaborato, il testo viene spezzato in **token**.

#### **Esempio di Tokenizzazione**
```
Input: "Ciao, come stai?"

Tokenizzazione:
["Ciao", ",", " come", " stai", "?"]

O più granulare:
["Ci", "ao", ",", " co", "me", " st", "ai", "?"]
```

**Perché è importante:**
- LLM lavora sui token, non su parole
- Parole rare possono essere spezzate male
- Lingue diverse hanno tokenizzazione diversa

#### **Limiti di Token**
```
GPT-4: ~8.000 token di contesto
Claude: ~100.000 token di contesto

Token ≈ 0.75 parole in inglese
Token ≈ 0.6 parole in italiano
```

### 5.6 Temperatura e Parametri di Generazione

#### **Temperatura**

Controlla la "creatività" del modello:

```
Temperatura = 0:
Input: "Il cielo è"
Output: "blu" (sempre la risposta più probabile)

Temperatura = 0.5:
Output: "blu" o "azzurro" o "sereno" (variazione moderata)

Temperatura = 1.5:
Output: "costellato" o "infinito" o "rosso al tramonto"
(alta creatività, ma può essere meno accurato)
```

**Quando usare:**
- **Bassa (0-0.3)**: Codice, risposte fattuali, precisione
- **Media (0.5-0.8)**: Scrittura creativa con controllo
- **Alta (1.0+)**: Brainstorming, creatività massima

---

## 6. Limiti e Rischi dell'IA

### 6.1 Le "Allucinazioni"

> **Allucinazione**: Quando l'IA genera informazioni plausibili ma **completamente inventate**.

#### **Perché Accade**

L'IA predice la "parola successiva più probabile", non verifica la verità:

```
Prompt: "Chi ha vinto il premio Nobel per la fisica nel 2087?"

Output possibile (ERRATO):
"Nel 2087 il premio Nobel per la fisica è stato assegnato a 
Maria Rossi per la sua ricerca sulla fusione fredda."

Perché: Struttura plausibile, ma anno futuro → inventato
```

#### **Esempi Reali di Allucinazioni**

**Caso 1: Citazioni Inventate**
```
Prompt: "Cita una frase famosa di Einstein sulla programmazione"
Output: "Come disse Einstein: 'Il codice è la lingua dell'universo'"

Verità: Einstein non ha mai detto questo
```

**Caso 2: Funzioni Inesistenti**
```
Prompt: "Scrivi codice C per invertire una stringa"
Output include: strreverse(str);

Problema: strreverse() non esiste nella libreria standard C
```

**Caso 3: Dati Statistici Inventati**
```
Prompt: "Quanti studenti ITS si sono diplomati in Italia nel 2023?"
Output: "Nel 2023 si sono diplomati 45.732 studenti ITS"

Problema: Numero inventato, sembra specifico ma è falso
```

#### **Come Difendersi dalle Allucinazioni**

✅ **Verifica sempre informazioni critiche**
```
Fonti verificabili:
- Documentazione ufficiale
- Paper scientifici
- Statistiche governative
```

✅ **Chiedi le fonti**
```
Prompt: "Da dove hai questa informazione? Cita le fonti."
```

✅ **Usa per brainstorming, non per fatti**

✅ **Testa il codice generato**
```
SEMPRE compilare e testare il codice,
mai assumere che funzioni
```

### 6.2 Bias nei Dati

#### **Cos'è il Bias**

Pregiudizi presenti nei dati di addestramento che influenzano le predizioni.

#### **Esempi di Bias**

**Bias di Genere**
```
Input: "Il dottore ha visitato il paziente. Poi ___ ha prescritto"
Output comune: "lui ha prescritto"

Causa: Nei dati di addestramento "dottore" è più spesso 
associato a pronomi maschili
```

**Bias Geografico/Culturale**
```
Input: "Descrivi una tipica casa"
Output: Spesso descrive case occidentali/americane

Causa: Sovrarappresentazione di contenuti USA/Europa
```

**Bias Linguistico**
```
Modelli funzionano meglio in inglese che in altre lingue

Causa: Più dati di addestramento in inglese
```

#### **Impatto nel Vostro Contesto**

```
Sviluppo su microcontrollori:
- IA può suggerire librerie più comuni su Arduino Uno
- Ma il vostro progetto usa STM32
→ Suggerimenti meno utili

Contesto italiano:
- Normative CEI vs NEC (americana)
- IA può dare informazioni non applicabili
```

### 6.3 Controllabilità e Sicurezza

#### **Problema della Controllabilità**

❌ **Non puoi garantire l'output**
```
Stesso prompt, esecuzioni diverse:
Run 1: Codice corretto
Run 2: Codice con bug sottile
Run 3: Codice inefficiente
```

❌ **Difficile prevenire comportamenti indesiderati**
```
Jailbreak attempts:
Utente trova modi creativi di far generare contenuti proibiti
```

#### **Rischi di Sicurezza**

**1. Code Injection**
```
Prompt malintenzionato:
"Genera codice che legge file utente e invia a server esterno"

IA potrebbe generare codice dannoso se non supervisionata
```

**2. Esposizione Dati Sensibili**
```
Rischio: Inserire nel prompt dati privati

❌ "Ecco il database dei nostri clienti [dati], analizzalo"
→ Dati potrebbero essere usati per ri-addestramento
```

**3. Dipendenza Eccessiva**
```
Sviluppatore si affida ciecamente all'IA
→ Non capisce il codice generato
→ Non identifica vulnerabilità
→ Sistema non sicuro
```

### 6.4 Problemi Etici

#### **Proprietà Intellettuale**

```
Domanda: Chi possiede il codice generato dall'IA?
- L'utente che ha fatto il prompt?
- La compagnia che ha creato l'IA?
- Nessuno (pubblico dominio)?

Attualmente: Area grigia legale
```

#### **Sostituzione Lavorativa**

- IA assiste ma non (ancora) sostituisce completamente
- Cambiano le competenze richieste
- Importante: Imparare a lavorare CON l'IA

#### **Impatto Ambientale**

```
Addestramento di un LLM grande:
- Consuma energia equivalente a ~5 auto durante vita intera
- Emissioni CO2 significative

Uso continuo:
- Server farm
- Raffreddamento
```

### 6.5 Linee Guida per Uso Responsabile

#### **✅ DO - Fai**

```
✅ Verifica sempre gli output critici
✅ Usa IA come assistente, non sostituto
✅ Testa il codice generato
✅ Mantieni competenze tecniche proprie
✅ Sii critico e scettico
✅ Proteggi dati sensibili
✅ Cita quando usi contenuti generati da IA
```

#### **❌ DON'T - Non Fare**

```
❌ Fidarsi ciecamente dell'output
❌ Inserire dati confidenziali nei prompt
❌ Usare codice senza capirlo
❌ Assumere che sia sempre corretto
❌ Dipendere completamente dall'IA
❌ Ignorare licenze e copyright
```

---

## 7. Applicazioni in Ambito ITS

### 7.1 Industry 4.0

#### **Manutenzione Predittiva**

**Scenario:** Linea produzione con macchinari industriali

**Senza IA:**
```
Manutenzione programmata ogni X ore
→ Possibili fermi imprevisti
→ Manutenzione prematura (spreco)
```

**Con IA:**
```
Sensori raccolgono:
- Vibrazioni
- Temperature
- Consumi energetici
- Audio (rumore macchinario)

Modello ML addestrato su:
- Dati storici di guasti
- Segnali pre-guasto

Output:
"Cuscinetto motore 3 degradato, previsto guasto in 48-72h"
→ Manutenzione pianificata
→ Evitato fermo produzione
```

**Vantaggi Reali:**
- Riduzione downtime: 30-50%
- Costi manutenzione: -20-30%
- Vita utile macchinari: +20%

#### **Controllo Qualità Automatizzato**

**Applicazione: Computer Vision per Difetti**

```
Sistema di ispezione visiva:

Camera ad alta risoluzione → Immagine prodotto
                ↓
    [Modello Deep Learning]
                ↓
Classificazione: OK / DIFETTO

Tipi di difetti rilevabili:
- Graffi superficiali
- Cricche
- Dimensioni non conformi
- Colori sbagliati
- Assemblaggi mancanti
```

**Prestazioni:**
- Velocità: 1000+ pezzi/ora
- Accuratezza: >99.5%
- Costo: Ridotto dopo ammortamento iniziale

### 7.2 Automotive e ADAS

#### **ADAS (Advanced Driver Assistance Systems)**

**Sistemi Attivi nei Veicoli Moderni:**

```
1. Lane Keeping Assist
   Camera → CV → Detect lane lines → Steering correction

2. Adaptive Cruise Control
   Radar → Detect vehicle ahead → Adjust speed

3. Automatic Emergency Braking
   Camera + Radar → Detect obstacle → Brake

4. Traffic Sign Recognition
   Camera → CV + LLM → Read signs → Display info
```

#### **Sensori e Fusione Dati**

```
Auto moderna tipica:

- 8-12 telecamere
- 4-6 radar
- 2-4 LiDAR
- Sensori ultrasuoni (12+)
- GPS/IMU

IA fonde tutti i dati per:
- Mappa 3D ambiente
- Predizione traiettorie altri veicoli
- Decisioni guida
```

#### **Sfide Tecniche**

```
Real-time processing:
- Decisioni in <100ms
- Affidabilità >99.9999%
- Funzionamento in condizioni difficili (pioggia, notte)

Safety-critical:
- Certificazioni rigorose
- Fallback systems
- Testing estensivo
```

### 7.3 Sistemi Embedded

#### **Inferenza su Microcontrollori**

**Trend:** Portare IA direttamente su MCU

**Esempio: Keyword Spotting**

```
Microcontrollore: STM32H7 (ARM Cortex-M7)
Task: Riconoscere parola "Arduino"

1. Microfono cattura audio
2. Pre-processing (FFT)
3. Rete neurale tiny (50KB)
4. Output: "Arduino detected" o "No"

Tutto su chip, no cloud!
```

**Vantaggi:**
- Latenza: <50ms
- Privacy: dati non escono dal device
- Costi: no connettività necessaria
- Energia: basso consumo

#### **TinyML - Machine Learning su Embedded**

**Frameworks Popolari:**
```
- TensorFlow Lite Micro
- Edge Impulse
- STM32Cube.AI
- Arduino ML

Permettono di:
1. Addestrare modello su PC
2. Ottimizzare per MCU
3. Deployare su hardware embedded
```

**Casi D'Uso Reali:**

```
1. Predictive Maintenance IoT
   - Sensore vibrazioni
   - Modello tiny su MCU
   - Alert quando pattern anomalo

2. Gesture Recognition
   - Accelerometro
   - Rileva gesti utente
   - Controllo dispositivi

3. Audio Event Detection
   - Microfono
   - Riconosce suoni (vetro rotto, allarmi)
   - Sistema sicurezza
```

#### **Vincoli e Ottimizzazioni**

```
Tipico MCU embedded:
- RAM: 256KB - 2MB
- Flash: 512KB - 2MB
- Clock: 80-400 MHz
- No FPU in alcuni casi

Tecniche di ottimizzazione:
- Quantizzazione (float32 → int8)
- Pruning (rimozione neuroni poco utili)
- Knowledge distillation
- Architetture efficienti (MobileNet)

Risultato:
Modello da 50MB → 50KB (1000x più piccolo!)
Con perdita accuratezza < 2%
```

### 7.4 Programmazione Assistita (Preview Moduli 2-4)

#### **Code Generation**

```
Prompt: "Scrivi funzione C per media mobile su 10 campioni"

IA genera:
- Struttura dati (array circolare)
- Funzione di inserimento
- Calcolo media
- Gestione edge cases

Programmatore:
- Verifica correttezza
- Adatta a specifiche di progetto
- Testa
```

**Benefici:**
- Velocità: +30-50% produttività
- Qualità: meno errori sintattici
- Learning: vedi esempi di codice buono

**Attenzione:**
- Sempre validare
- IA non conosce il tuo hardware specifico
- Possibili funzioni non standard

### 7.5 IoT e Smart Devices

#### **Natural Language Interface**

```
Dispositivo IoT smart:

Utente: "Accendi la luce in cucina"
    ↓
[LLM cloud o edge] → Parse intent
    ↓
{
  action: "turn_on",
  device: "light",
  location: "kitchen"
}
    ↓
API call → Luce accesa
```

#### **Analisi Dati Sensori**

```
Smart Building:
- 1000 sensori (temp, umidità, CO2, presenza)
- Stream dati continuo

IA:
- Pattern detection: Anomalie
- Optimization: HVAC efficiente
- Prediction: Necessità manutenzione

Risultato:
- Energia: -30%
- Comfort: +20%
- Costi: -25%
```

---

## 8. Casi Studio Pratici

### 8.1 Caso Studio: Classificazione Anomalie Motori

#### **Contesto**
Azienda manifatturiera con 50 motori elettrici in produzione. Obiettivo: prevenire guasti costosi.

#### **Soluzione Tradizionale**
```
Manutenzione ogni 1000h di funzionamento
Costo annuo: €50.000
Downtime imprevisti: 3-5 all'anno (€20k cad)
```

#### **Soluzione con IA**

**Step 1: Raccolta Dati**
```
Sensori installati:
- Accelerometro 3-assi
- Microfono
- Temperatura cuscinetti
- Corrente assorbita

Frequenza campionamento: 10kHz (vibrazioni), 1Hz (altri)
Durata raccolta: 6 mesi (fase normale + alcuni guasti)
```

**Step 2: Labeling**
```
Dati etichettati da esperti:
- 85% funzionamento normale
- 10% stato degradato
- 5% pre-guasto

Feature engineering:
- FFT dello spettro vibrazioni
- RMS vibrazioni
- Picchi spettrali
- Temperatura trend
```

**Step 3: Training**
```
Modello: Random Forest Classifier
Split: 70% training, 15% validation, 15% test

Accuracy: 94%
False Negative Rate: 2% (accettabile)
False Positive Rate: 5%
```

**Step 4: Deployment**
```
Edge device: Raspberry Pi per ogni motore
Inferenza: Ogni 30 secondi
Output: 
- Verde: OK
- Giallo: Monitorare
- Rosso: Manutenzione urgente

Dashboard centrale con alert
```

#### **Risultati Dopo 1 Anno**

```
✅ Downtime imprevisti: 0
✅ Costo manutenzione: -40%
✅ Vita utile motori: +15%
✅ ROI: 8 mesi

❌ False alarm: 1-2 al mese (gestibili)
❌ Costo iniziale: €80k (sensori + software + training)
```

#### **Lezioni Apprese**

```
1. Dati di qualità fondamentali
   - 6 mesi di raccolta necessari
   - Importante avere esempi di guasti

2. Domain expertise essenziale
   - Ingegneri meccanici + data scientists
   - Feature engineering guidata da fisica

3. Edge computing preferibile
   - Latenza bassa
   - Privacy
   - Funziona anche senza rete

4. Manutenzione del modello
   - Re-training trimestrale
   - Drift detection (performance decade)
```

### 8.2 Caso Studio: IA su Microcontrollore per Wake Word

#### **Contesto**
Sviluppare dispositivo IoT che si attiva alla parola "Ciao Arduino".

#### **Requisiti**
```
- MCU: STM32F746 (ARM Cortex-M7, 216MHz)
- RAM disponibile: 256KB
- Flash disponibile: 512KB per modello
- Latenza max: 200ms
- Consumo: <50mW in listening mode
- Accuracy: >95%
```

#### **Approccio Tradizionale (Impossibile)**
```
Modello speech recognition standard:
- Size: 500MB+
- Richiede GPU
- Latenza: ~100ms su desktop

→ Non applicabile su MCU
```

#### **Soluzione TinyML**

**Step 1: Dataset**
```
Raccolta:
- 5000 clip "Ciao Arduino" (varie voci, accenti)
- 10000 clip altre parole/rumori
- Durata clip: 1 secondo cad

Augmentation:
- Variazione velocità
- Background noise
- Riverbero

Dataset finale: 30k esempi
```

**Step 2: Feature Extraction**
```
Audio raw (16kHz) → MFCC (Mel-Frequency Cepstral Coefficients)

Vantaggi MFCC:
- Riduce dimensionalità (16kHz → 13 coefficienti)
- Robusto a variazioni speaker
- Compatibile con ML

Window: 30ms, overlap 10ms
Output: Matrice 13x40 per ogni secondo
```

**Step 3: Model Architecture**
```
Tiny CNN:

Input: 13x40 MFCC
  ↓
Conv2D (8 filters, 3x3) + ReLU
  ↓
MaxPool (2x2)
  ↓
Conv2D (16 filters, 3x3) + ReLU
  ↓
MaxPool (2x2)
  ↓
Flatten
  ↓
Dense (32) + ReLU
  ↓
Dense (2) + Softmax
  ↓
Output: [P(target), P(non-target)]

Totale parametri: ~8.500
```

**Step 4: Training**
```
Framework: TensorFlow/Keras
Epochs: 50
Batch size: 32
Optimizer: Adam

Validation accuracy: 96.5%
```

**Step 5: Quantization**
```
Post-training quantization:
Float32 → Int8

Dimensione modello:
Prima: 34KB (float32)
Dopo: 9KB (int8)

Accuracy loss: 0.5% (accettabile)
```

**Step 6: Deployment su STM32**
```
Tool: STM32Cube.AI

Conversione Keras → C code
Integrazione in firmware

Memory footprint:
- Modello: 9KB Flash
- Working buffers: 45KB RAM
- Totale: ben dentro limiti

Inference time: 85ms
Power: 42mW (ottimo!)
```

#### **Testing sul Campo**

```
Test su 100 utenti diversi:
- True Positive Rate: 94%
- False Positive Rate: 2/hour
- Funziona con accenti regionali
- Resiliente a rumore moderato

Criticità identificate:
- Performance degrada in ambienti molto rumorosi
- Alcuni accenti stranieri problematici
→ Raccolti più dati per re-training
```

#### **Conclusioni Tecniche**

```
✅ IA su MCU è fattibile per task mirati
✅ Ottimizzazione cruciale (quantization, pruning)
✅ Trade-off accuracy vs. size gestibile
✅ Consumo energetico molto basso

❌ Limiti:
  - Solo task semplici
  - Richiede expertise ML + embedded
  - Dataset quality fondamentale
```

### 8.3 Caso Studio: Code Generation Assistita

#### **Scenario**
Studente ITS deve implementare algoritmo PID per controllo motore.

#### **Approccio Manuale (Tradizionale)**
```
Tempo stimato: 4-6 ore

Step:
1. Ricerca teoria PID (1h)
2. Comprensione equazioni (1h)
3. Scrittura codice C (2h)
4. Debug (1-2h)
5. Tuning parametri (variabile)

Problemi comuni:
- Errori implementazione integrale (wind-up)
- Discrete vs continuous
- Overflow variabili
```

#### **Approccio con IA Assistita**

**Iterazione 1: Prompt Base**
```
Prompt: "Scrivi funzione PID in C"

Output IA:
float pid_controller(float setpoint, float measurement) {
    float error = setpoint - measurement;
    integral += error;
    float derivative = error - previous_error;
    previous_error = error;
    return Kp * error + Ki * integral + Kd * derivative;
}
```

**Analisi Output:**
```
❌ Variabili globali non dichiarate
❌ No anti-windup per integrale
❌ No limite output
❌ No gestione tempo di campionamento
❌ Coefficienti hardcoded

Voto: 4/10 - Non usabile in produzione
```

**Iterazione 2: Prompt Migliorato**
```
Prompt:
"Scrivi in standard C99 una funzione PID controller con:
- Struttura dati per stato interno
- Anti-windup per integrale
- Saturazione output tra min e max
- Gestione corretta del tempo di campionamento dt
- Commenti esplicativi
- Funzione di inizializzazione separata"

Output IA: [codice significativamente migliore]

typedef struct {
    float Kp, Ki, Kd;
    float integral;
    float prev_error;
    float out_min, out_max;
} PIDController;

void pid_init(PIDController *pid, float kp, float ki, float kd, 
              float out_min, float out_max) {
    pid->Kp = kp;
    pid->Ki = ki;
    pid->Kd = kd;
    pid->integral = 0.0f;
    pid->prev_error = 0.0f;
    pid->out_min = out_min;
    pid->out_max = out_max;
}

float pid_compute(PIDController *pid, float setpoint, 
                  float measurement, float dt) {
    float error = setpoint - measurement;
    
    // Termine proporzionale
    float P = pid->Kp * error;
    
    // Termine integrale con anti-windup
    pid->integral += error * dt;
    float I = pid->Ki * pid->integral;
    
    // Termine derivativo
    float derivative = (error - pid->prev_error) / dt;
    float D = pid->Kd * derivative;
    
    // Output totale
    float output = P + I + D;
    
    // Saturazione
    if (output > pid->out_max) {
        output = pid->out_max;
        // Anti-windup: non accumulare se saturo
        pid->integral -= error * dt;
    } else if (output < pid->out_min) {
        output = pid->out_min;
        pid->integral -= error * dt;
    }
    
    pid->prev_error = error;
    return output;
}
```

**Analisi Output 2:**
```
✅ Struttura dati appropriata
✅ Separazione inizializzazione/compute
✅ Anti-windup implementato
✅ Saturazione output
✅ Gestione dt corretta
✅ Codice commentato

⚠️ Da verificare:
- Comportamento su reset (prev_error)
- Gestione dt = 0
- Test su valori reali

Voto: 8/10 - Buona base, richiede validazione
```

**Iterazione 3: Testing**
```
Prompt: "Genera funzione di test per questo PID controller 
con vari scenari: step response, rampa, disturbi"

Output IA: [genera test cases]

Test identificano:
- Bug: derivative kick su cambio setpoint
  (risolto salvando measurement invece di error)
- Performance buona su step
- Overshoot da parametri da tunare

Totale tempo con IA: 1.5 ore
- 30min prompt + iterazioni
- 45min comprensione codice generato
- 15min testing e fix
```

#### **Confronto Finale**

| Metodo | Tempo | Qualità | Apprendimento |
|--------|-------|---------|---------------|
| Manuale | 4-6h | Alta (se esperti) | Alto |
| IA Assistita | 1.5h | Alta (dopo validazione) | Medio-Alto |

**Conclusioni:**
```
✅ IA accelera significativamente
✅ Permette focus su comprensione vs. sintassi
✅ Output richiede sempre validazione critica
❌ Non sostituisce competenza tecnica
```

---

## 9. Esercizi e Autovalutazione

### 9.1 Quiz Teorico

#### **Domanda 1: Definizioni Base**
Quale delle seguenti affermazioni è corretta?

A) L'IA può risolvere solo problemi per cui esistono regole esplicite  
B) L'IA apprende pattern da dati e può generalizzare a nuove situazioni  
C) L'IA ha sempre ragione perché basata su matematica  
D) L'IA può funzionare senza dati di addestramento  

<details>
<summary>Risposta</summary>
B) Corretta. L'IA apprende da dati e generalizza.
</details>

#### **Domanda 2: Categorie IA**
Quale tecnica useresti per raggruppare clienti con comportamenti simili senza etichette predefinite?

A) Supervised Learning  
B) Reinforcement Learning  
C) Unsupervised Learning (Clustering)  
D) Rule-based system  

<details>
<summary>Risposta</summary>
C) Unsupervised Learning - perfetto per clustering senza etichette.
</details>

#### **Domanda 3: LLM**
Come genera testo un Large Language Model?

A) Cerca nel database e copia frasi esistenti  
B) Ragiona logicamente come un umano  
C) Predice token successivi basandosi su probabilità  
D) Usa regole grammaticali programmate  

<details>
<summary>Risposta</summary>
C) Corretta. LLM predice token per token probabilisticamente.
</details>

#### **Domanda 4: Allucinazioni**
Cos'è un'allucinazione in un LLM?

A) Un errore di connessione  
B) Informazione plausibile ma inventata  
C) Risposta troppo lunga  
D) Errore di sintassi  

<details>
<summary>Risposta</summary>
B) L'LLM genera contenuti che sembrano veri ma sono inventati.
</details>

#### **Domanda 5: Applicazioni**
Quale NON è un'applicazione tipica di Deep Learning?

A) Riconoscimento immagini  
B) Calcolo di radice quadrata  
C) Traduzione automatica  
D) Riconoscimento vocale  

<details>
<summary>Risposta</summary>
B) La radice quadrata si calcola con algoritmi classici, non serve DL.
</details>

### 9.2 Esercizio Pratico 1: Classificazione Applicazioni

**Istruzioni:** Per ogni scenario, indica quale tipo di IA è più appropriato.

| Scenario | IA Simbolica | ML Supervisionato | ML Non Super. | Reinforcement | Deep Learning |
|----------|--------------|-------------------|---------------|---------------|---------------|
| 1. Diagnosi medica da sintomi predefiniti | ? | ? | ? | ? | ? |
| 2. Riconoscimento facciale da foto | ? | ? | ? | ? | ? |
| 3. Robot che impara a camminare | ? | ? | ? | ? | ? |
| 4. Segmentazione clienti senza categorie note | ? | ? | ? | ? | ? |
| 5. Previsione prezzi case da caratteristiche | ? | ? | ? | ? | ? |

<details>
<summary>Soluzioni</summary>

1. **IA Simbolica** o ML Supervisionato (dipende dalla complessità)
2. **Deep Learning** (Computer Vision)
3. **Reinforcement Learning**
4. **ML Non Supervisionato** (Clustering)
5. **ML Supervisionato** (Regressione)

</details>

### 9.3 Esercizio Pratico 2: Analisi Critica Output IA

**Scenario:** Hai chiesto a un LLM di spiegarti cos'è un microcontrollore. Ecco la risposta:

```
"Un microcontrollore è un chip che contiene CPU, RAM e periferiche.
Il più famoso è l'Arduino Mega2560 che ha una CPU a 32-bit e 512MB di RAM.
Viene usato principalmente nei supercomputer per calcoli complessi.
La sua invenzione nel 2015 da parte di Steve Jobs ha rivoluzionato l'IoT."
```

**Compito:**
1. Identifica tutte le affermazioni errate
2. Spiega perché sono errate
3. Fornisci le informazioni corrette

<details>
<summary>Soluzione</summary>

**Errori identificati:**

1. **"Arduino Mega2560 ha CPU a 32-bit"**
   - FALSO: Ha CPU 8-bit (ATmega2560)
   
2. **"512MB di RAM"**
   - FALSO: Ha solo 8KB di SRAM
   
3. **"Usato nei supercomputer"**
   - FALSO: Usati in sistemi embedded, non supercomputer
   
4. **"Invenzione nel 2015 da Steve Jobs"**
   - FALSO: Microcontrollori esistono dagli anni '70; Jobs non li ha inventati; Arduino nasce nel 2005

**Tipo di errori:** Allucinazioni tipiche (numeri plausibili ma sbagliati, associazioni errate)

</details>

### 9.4 Esercizio Pratico 3: Progettazione Sistema IA

**Scenario:** Sei stato incaricato di progettare un sistema per rilevare difetti su pannelli solari in una fabbrica.

**Dati disponibili:**
- 10.000 immagini di pannelli OK
- 500 immagini di pannelli con difetti (vari tipi)
- Camera industriale 12MP
- Server on-premise con GPU

**Compiti:**
1. Scegli la categoria di IA più appropriata
2. Giustifica la scelta
3. Descrivi il pipeline di lavoro
4. Identifica almeno 3 sfide potenziali

<details>
<summary>Soluzione Esempio</summary>

**1. Categoria:** Deep Learning (Computer Vision) - Supervised Learning

**2. Giustificazione:**
- Problema di classificazione immagini
- Dataset etichettato disponibile
- Pattern visivi complessi
- Deep Learning eccelle in questo tipo di task

**3. Pipeline:**
```
1. Pre-processing:
   - Resize immagini a 512x512
   - Normalizzazione pixel values
   - Data augmentation (rotazioni, flip, variazioni luce)

2. Model Architecture:
   - CNN (es. ResNet-50 modificato)
   - Output: OK / DIFETTO + confidence

3. Training:
   - Split: 70% train, 15% validation, 15% test
   - Gestione imbalance dataset (più OK che difetti)
   - Transfer learning da modello pre-trained

4. Deployment:
   - Edge inference su server locale
   - Integrazione con linea produzione
   - Alert automatici

5. Monitoring:
   - Tracking accuracy nel tempo
   - Re-training periodico con nuovi esempi
```

**4. Sfide:**
```
1. Imbalance dataset (10k OK vs 500 difetti)
   - Soluzione: Oversampling minoranza, class weights

2. Variabilità illuminazione in fabbrica
   - Soluzione: Augmentation, illuminazione controllata

3. Nuovi tipi di difetti nel tempo
   - Soluzione: Sistema di labeling continuo, re-training

4. False negative critici (difetto non rilevato)
   - Soluzione: Threshold ottimizzato per recall alto
```

</details>

### 9.5 Esercizio Pratico 4: Prompt Engineering

**Scenario:** Devi chiedere a un LLM di generare codice per un filtro passa-basso digitale.

**Compito:** Scrivi due versioni del prompt:
1. **Versione base** (probabilmente insufficiente)
2. **Versione professionale** (specifica e completa)

Poi spiega le differenze.

<details>
<summary>Soluzione Esempio</summary>

**Versione Base (❌ Insufficiente):**
```
"Scrivi codice per un filtro passa-basso"
```

**Problemi:**
- Linguaggio non specificato
- Tipo di filtro non chiaro
- Parametri mancanti
- Contesto d'uso assente

---

**Versione Professionale (✅ Completa):**
```
"Scrivi in standard C99 una funzione per implementare un filtro 
passa-basso digitale del primo ordine (RC filter discretizzato).

Requisiti:
- Funzione: float lpf_update(LPF_State *state, float input)
- Struttura per mantenere stato interno
- Parametro alpha (costante di smoothing) configurabile
- Alpha calcolato da frequenza di taglio e sample rate
- Includi funzione di inizializzazione
- Aggiungi commenti esplicativi
- Fornisci esempio di uso con sample rate 1kHz e fc 50Hz

Vincoli:
- No librerie esterne
- Efficiente per sistemi embedded
- Float precision (32-bit)

Output richiesto:
- Header file (.h) con dichiarazioni
- Implementation (.c)
- Esempio di uso nel main()
"
```

**Differenze Chiave:**
```
✅ Linguaggio e standard specificati
✅ Dettagli tecnici (tipo filtro, ordine)
✅ Struttura dati richiesta
✅ Parametri e vincoli chiari
✅ Formato output definito
✅ Esempio concreto richiesto
✅ Contesto (embedded) specificato

Risultato: Output molto più utilizzabile e professionale
```

</details>

### 9.6 Progetto Finale del Modulo

**Titolo:** Analisi Critica di Sistema IA Industriale

**Obiettivo:** Applicare tutte le conoscenze del modulo in un caso reale.

**Consegna:**
1. Scegli un'applicazione industriale di IA (es. manutenzione predittiva, quality control, robotica)
2. Ricerca un caso reale (paper, articolo tecnico, case study aziendale)
3. Produci un report (2-3 pagine) che include:

**Struttura Report:**

```
1. INTRODUZIONE (1/2 pagina)
   - Descrizione applicazione
   - Contesto industriale
   - Problema da risolvere

2. SOLUZIONE IA (1 pagina)
   - Tipo di IA utilizzata (categoria)
   - Architettura (se disponibile)
   - Dati utilizzati
   - Processo di training

3. ANALISI CRITICA (1/2 pagina)
   - Punti di forza della soluzione
   - Limiti identificati
   - Possibili bias o rischi
   - Validazione risultati

4. VALUTAZIONE (1/2 pagina)
   - Risultati quantitativi (accuracy, ROI, ecc.)
   - Applicabilità al vostro contesto ITS
   - Lezioni apprese

5. CONCLUSIONI (1/4 pagina)
   - Sintesi
   - Raccomandazioni
```

**Criteri di Valutazione:**
- Completezza analisi: 30%
- Capacità critica: 30%
- Comprensione tecnica: 25%
- Chiarezza esposizione: 15%

**Fonti Suggerite:**
- IEEE Xplore
- ArXiv (sezione CS)
- Blog tecnici aziendali (NVIDIA, Google AI, ecc.)
- Case study pubblici

---

## 10. Glossario Tecnico

### A

**Accuracy (Accuratezza)**
Percentuale di predizioni corrette su totale predizioni.
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

**Activation Function**
Funzione non-lineare in una rete neurale (es. ReLU, Sigmoid, Tanh).

**ADAS (Advanced Driver Assistance Systems)**
Sistemi di assistenza alla guida avanzati.

**Algorithm**
Sequenza finita di istruzioni per risolvere un problema.

**Allucinazione**
Output di un LLM che è plausibile ma inventato/errato.

**API (Application Programming Interface)**
Interfaccia per interagire con un software/servizio.

**Attention Mechanism**
Tecnica che permette al modello di "focalizzarsi" su parti rilevanti dell'input.

### B

**Backpropagation**
Algoritmo per calcolare gradienti in una rete neurale durante training.

**Batch**
Sottoinsieme di dati usato in un'iterazione di training.

**Bias (Machine Learning)**
1. Parametro in neuroni (intercetta)
2. Pregiudizio nei dati o modello

**Big Data**
Dataset molto grandi (terabytes+) che richiedono elaborazione distribuita.

### C

**Classification**
Task di assegnare categorie a input (es. spam/non-spam).

**Clustering**
Raggruppamento automatico di dati simili senza etichette.

**CNN (Convolutional Neural Network)**
Architettura di rete neurale efficace per immagini.

**Computer Vision**
Branca dell'IA che elabora e comprende immagini.

**Corpus**
Grande raccolta di testi usata per training di modelli linguistici.

### D

**Data Augmentation**
Tecniche per aumentare varietà dataset (rotazioni, flip, noise, ecc.).

**Dataset**
Collezione di dati usata per training/validation/test.

**Deep Learning**
Sottocategoria ML con reti neurali "profonde" (molti layer).

**Deployment**
Processo di messa in produzione di un modello.

### E

**Edge Computing**
Elaborazione dati direttamente su dispositivo (vs cloud).

**Embedding**
Rappresentazione vettoriale densa di dati (es. word embeddings).

**Epoch**
Passata completa attraverso tutto il training dataset.

**Evaluation Metrics**
Metriche per valutare performance (accuracy, precision, recall, F1).

### F

**Feature**
Attributo misurabile dell'input (es. pixel, frequenza audio).

**Feature Engineering**
Processo di creare feature rilevanti dai dati raw.

**Fine-tuning**
Adattamento di modello pre-trained a task specifico.

**FPU (Floating Point Unit)**
Unità hardware per calcoli in virgola mobile.

### G

**Generative AI**
IA che genera nuovi contenuti (testo, immagini, audio).

**GPU (Graphics Processing Unit)**
Hardware ottimizzato per calcoli paralleli, usato per training IA.

**Gradient Descent**
Algoritmo di ottimizzazione per minimizzare loss function.

### H

**Hyperparameter**
Parametro di configurazione del training (learning rate, batch size).

**Hallucination**
Vedi "Allucinazione".

### I

**Inference**
Processo di usare modello addestrato per fare predizioni.

**IoT (Internet of Things)**
Rete di dispositivi fisici connessi e intelligenti.

### K

**Knowledge Cutoff**
Data oltre la quale un LLM non ha dati di addestramento.

**K-Fold Cross Validation**
Tecnica per validare modello su più split del dataset.

### L

**Label**
Etichetta target in supervised learning (output corretto).

**Latency**
Tempo di risposta di un sistema.

**Learning Rate**
Hyperparameter che controlla velocità di apprendimento.

**LLM (Large Language Model)**
Modello di linguaggio molto grande (miliardi di parametri).

**Loss Function**
Funzione che misura errore del modello (da minimizzare).

### M

**Machine Learning**
Branca IA dove algoritmi apprendono da dati.

**MCU (Microcontroller Unit)**
Chip embedded con CPU, RAM, periferiche integrate.

**MFCC (Mel-Frequency Cepstral Coefficients)**
Feature per elaborazione audio/speech.

**Model**
Rappresentazione matematica addestrata per fare predizioni.

### N

**Neural Network**
Modello computazionale ispirato a neuroni biologici.

**NLP (Natural Language Processing)**
Elaborazione linguaggio naturale.

**Normalization**
Processo di scalare dati a range standard (es. 0-1).

### O

**Overfitting**
Modello troppo adattato al training set, performa male su nuovi dati.

**Optimizer**
Algoritmo che aggiorna pesi del modello (SGD, Adam, ecc.).

### P

**Parameter**
Peso o bias appreso dal modello durante training.

**Precision**
Percentuale di predizioni positive corrette.
```
Precision = TP / (TP + FP)
```

**Pre-training**
Fase iniziale di training su grandi dataset generali.

**Prompt**
Istruzione/input fornito a un LLM.

**Pruning**
Rimozione di parametri poco importanti per ridurre dimensione modello.

### Q

**Quantization**
Conversione di pesi da alta a bassa precisione (es. float32 → int8).

### R

**Recall**
Percentuale di casi positivi reali correttamente identificati.
```
Recall = TP / (TP + FN)
```

**Regression**
Predizione di valori continui (vs categorie discrete).

**Reinforcement Learning**
Apprendimento tramite reward/penalty per azioni.

**ReLU (Rectified Linear Unit)**
Activation function: f(x) = max(0, x)

### S

**Supervised Learning**
ML con dati etichettati (input + output corretto).

**Sample**
Singolo elemento di un dataset.

### T

**Test Set**
Porzione di dati usata per valutazione finale del modello.

**TinyML**
Machine Learning su dispositivi embedded con risorse limitate.

**Token**
Unità base di testo per LLM (spesso sub-parola).

**Training Set**
Porzione di dati usata per addestrare il modello.

**Transfer Learning**
Riuso di modello addestrato su un task per altro task simile.

**Transformer**
Architettura di rete neurale base dei moderni LLM.

### U

**Underfitting**
Modello troppo semplice, performa male sia su training che test.

**Unsupervised Learning**
ML senza etichette, trova pattern automaticamente.

### V

**Validation Set**
Porzione di dati usata per tuning hyperparameters durante training.

### W

**Weight**
Parametro di connessione in una rete neurale.

### Simboli

**α (Alpha)**
Comunemente: learning rate o coefficiente di smoothing.

**η (Eta)**
Comunemente: learning rate.

---

## 📚 Bibliografia e Risorse

### Libri Consigliati
1. **"Artificial Intelligence: A Modern Approach"** - Russell & Norvig
2. **"Deep Learning"** - Goodfellow, Bengio, Courville
3. **"Pattern Recognition and Machine Learning"** - Bishop

### Corsi Online Gratuiti
- **Coursera**: Machine Learning - Andrew Ng
- **Fast.ai**: Practical Deep Learning
- **MIT OpenCourseWare**: Introduction to Deep Learning

### Risorse Web
- **Papers with Code**: State-of-the-art ML papers con codice
- **ArXiv**: Repository paper scientifici
- **Kaggle**: Competizioni e dataset ML

### Tool e Framework
- **TensorFlow / Keras**: Framework deep learning
- **PyTorch**: Framework deep learning (research-friendly)
- **Scikit-learn**: Libreria ML Python
- **Edge Impulse**: TinyML per embedded

---

## 📝 Note per il Docente

### Suggerimenti Didattici

**Timing Raccomandato (2 ore totali):**
- Introduzione e motivazione: 15min
- Sezioni 2-4 (IA, categorie, LLM): 45min
- Sezione 6 (limiti e rischi): 20min
- Sezione 7 (applicazioni ITS): 25min
- Q&A e discussione: 15min

**Punti Chiave da Enfatizzare:**
1. IA come strumento, non magia
2. Importanza validazione critica
3. Limiti e rischi reali
4. Applicazioni pratiche nel loro futuro lavorativo

**Materiali Supplementari Utili:**
- Video demo di sistemi IA reali
- Code snippet da mostrare live
- Accesso a LLM per esempi in tempo reale

**Valutazione Apprendimento:**
- Quiz interattivo (Kahoot/Mentimeter)
- Discussione casi studio
- Esercizio pratico guidato con LLM

---

## ✅ Checklist Completamento Modulo

Per lo studente - verifica di aver compreso:

- [ ] So definire cos'è l'IA e distinguerla da algoritmi classici
- [ ] Conosco le 4 categorie principali di IA
- [ ] Capisco come funzionano gli LLM a livello concettuale
- [ ] So cos'è un'allucinazione e come identificarla
- [ ] Riconosco bias e limiti dei sistemi IA
- [ ] Posso citare 3 applicazioni IA in ambito ITS/embedded
- [ ] So valutare criticamente output generato da IA
- [ ] Ho completato almeno 3 esercizi della sezione 9
- [ ] Mi sento pronto per il Modulo 2 (Prompt Engineering)

---

**Fine Modulo 1**

*Prossimo passo: Modulo 2 - Tecniche di Programmazione Assistita*

---

**Versione documento:** 1.0  
**Ultimo aggiornamento:** Dicembre 2024  
**Autore:** Corso ITS - IA e Programmazione Assistita  
**Licenza:** Materiale didattico ad uso interno

