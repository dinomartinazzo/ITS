# 📘 MODULO 1
# Fondamenti di Intelligenza Artificiale
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita
### Durata: 4 ore | Livello: Introduttivo

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

### 4.2 Machine Learning

#### **Supervised Learning (Apprendimento Supervisionato)**

**Principio:** Impara da esempi etichettati

**Applicazioni:**
- Classificazione email spam
- Diagnosi mediche
- Previsione prezzi
- Riconoscimento immagini

#### **Unsupervised Learning (Non Supervisionato)**

**Principio:** Trova pattern senza etichette

**Applicazioni:**
- Segmentazione mercato
- Rilevamento anomalie
- Compressione dati

#### **Reinforcement Learning**

**Principio:** Impara per tentativi ed errori con rinforzi

**Applicazioni:**
- Giochi (AlphaGo, scacchi)
- Robotica
- Auto autonome
- Ottimizzazione processi

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

### 5.3 Capacità e Limiti

#### **Capacità Sorprendenti**

✅ **Comprensione Contestuale**
✅ **Ragionamento Base**
✅ **Generazione Creativa**
✅ **Traduzione**

#### **Limiti Critici**

❌ **Conoscenza Limitata** (knowledge cutoff)
❌ **No Ragionamento Logico Perfetto**
❌ **No Comprensione Vera**
❌ **Allucinazioni**

---

## 6. Limiti e Rischi dell'IA

### 6.1 Le "Allucinazioni"

> **Allucinazione**: Quando l'IA genera informazioni plausibili ma **completamente inventate**.

#### **Come Difendersi dalle Allucinazioni**

✅ **Verifica sempre informazioni critiche**
✅ **Chiedi le fonti**
✅ **Usa per brainstorming, non per fatti**
✅ **Testa il codice generato**

### 6.2 Bias nei Dati

**Bias di Genere**
- Associazioni stereotipate nei dati

**Bias Geografico/Culturale**
- Sovrarappresentazione contenuti occidentali

**Bias Linguistico**
- Modelli funzionano meglio in inglese

### 6.3 Linee Guida per Uso Responsabile

#### **✅ DO - Fai**

```
✅ Verifica sempre gli output critici
✅ Usa IA come assistente, non sostituto
✅ Testa il codice generato
✅ Mantieni competenze tecniche proprie
✅ Sii critico e scettico
✅ Proteggi dati sensibili
```

#### **❌ DON'T - Non Fare**

```
❌ Fidarsi ciecamente dell'output
❌ Inserire dati confidenziali nei prompt
❌ Usare codice senza capirlo
❌ Assumere che sia sempre corretto
❌ Dipendere completamente dall'IA
```

---

## 7. Applicazioni in Ambito ITS

### 7.1 Industry 4.0

#### **Manutenzione Predittiva**

**Con IA:**
```
Sensori raccolgono:
- Vibrazioni
- Temperature
- Consumi energetici

Output:
"Cuscinetto motore 3 degradato, previsto guasto in 48-72h"
→ Manutenzione pianificata
```

**Vantaggi Reali:**
- Riduzione downtime: 30-50%
- Costi manutenzione: -20-30%
- Vita utile macchinari: +20%

### 7.2 Sistemi Embedded

#### **TinyML - Machine Learning su Embedded**

**Frameworks Popolari:**
- TensorFlow Lite Micro
- Edge Impulse
- STM32Cube.AI
- Arduino ML

**Casi D'Uso:**
1. Predictive Maintenance IoT
2. Gesture Recognition
3. Audio Event Detection

### 7.3 Programmazione Assistita

**Benefici:**
- Velocità: +30-50% produttività
- Qualità: meno errori sintattici
- Learning: esempi di codice buono

**Attenzione:**
- Sempre validare
- IA non conosce hardware specifico
- Possibili funzioni non standard

---

## 8. Casi Studio Pratici

### 8.1 Caso Studio: Classificazione Anomalie Motori

**Risultati Dopo 1 Anno:**
```
✅ Downtime imprevisti: 0
✅ Costo manutenzione: -40%
✅ Vita utile motori: +15%
✅ ROI: 8 mesi
```

### 8.2 Caso Studio: IA su Microcontrollore

**Conclusioni:**
```
✅ IA su MCU è fattibile per task mirati
✅ Ottimizzazione cruciale
✅ Trade-off accuracy vs. size gestibile
✅ Consumo energetico molto basso
```

---

## 9. Esercizi e Autovalutazione

### 9.1 Quiz Teorico

**Domanda 1:** Quale affermazione è corretta sull'IA?
A) Può risolvere solo problemi con regole esplicite
B) Apprende pattern da dati e generalizza
C) Ha sempre ragione
D) Funziona senza dati

<details>
<summary>Risposta</summary>
B) Corretta - L'IA apprende da dati e generalizza
</details>

**Domanda 2:** Cos'è un'allucinazione in un LLM?
A) Errore di connessione
B) Informazione plausibile ma inventata
C) Risposta troppo lunga
D) Errore di sintassi

<details>
<summary>Risposta</summary>
B) L'LLM genera contenuti che sembrano veri ma sono inventati
</details>

---

## 10. Glossario Tecnico

**Accuracy**: Percentuale di predizioni corrette

**Allucinazione**: Output LLM plausibile ma inventato

**Bias**: Pregiudizio nei dati o modello

**Deep Learning**: ML con reti neurali profonde

**Feature**: Attributo misurabile dell'input

**LLM**: Large Language Model

**Machine Learning**: Algoritmi che apprendono da dati

**Overfitting**: Modello troppo adattato al training set

**Token**: Unità base di testo per LLM

**Training Set**: Dati usati per addestrare il modello

---

## ✅ Checklist Completamento Modulo

- [ ] So definire cos'è l'IA
- [ ] Conosco le categorie principali di IA
- [ ] Capisco come funzionano gli LLM
- [ ] So cos'è un'allucinazione
- [ ] Riconosco bias e limiti
- [ ] Conosco applicazioni ITS/embedded
- [ ] So valutare criticamente output IA
- [ ] Mi sento pronto per il Modulo 2

---

**Fine Modulo 1**

*Prossimo: Modulo 2 - Prompt Engineering*

---

**Versione:** 2.0 | **Aggiornamento:** Dicembre 2024 | **Corso ITS**
