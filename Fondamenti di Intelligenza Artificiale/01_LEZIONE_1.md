# 📘 LEZIONE 1: INTRODUZIONE ALL'IA E PRIMI PROMPT
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita

**Durata:** 2 ore
**Struttura:** 1 ora teoria + 1 ora pratica
**Livello:** Base
**Prerequisiti:** Nessuno (conoscenze informatiche di base)

---

## 🎯 Obiettivi della Lezione

Al termine di questa lezione sarai in grado di:

✅ **Comprendere** il contesto storico che ha portato all'IA moderna
✅ **Spiegare** cosa sono i Large Language Models e come funzionano
✅ **Identificare** i principali strumenti IA disponibili nel 2025
✅ **Riconoscere** i limiti critici dell'IA (allucinazioni, bias, knowledge cutoff)
✅ **Utilizzare** ChatGPT e altri LLM per i primi esperimenti pratici
✅ **Applicare** principi etici nell'uso dell'IA
✅ **Formulare** domande e prompt efficaci
✅ **Confrontare** l'output di diversi modelli IA

---

## 📋 Struttura della Lezione

### **PARTE 1: TEORIA (60 minuti)**

1. **Introduzione e Contesto** (10 min)
   - Benvenuto e presentazione del corso
   - Perché l'IA è importante nel 2025
   - Il ruolo dell'IA nella programmazione moderna

2. **Storia dell'Intelligenza Artificiale** (15 min)
   - Da Alan Turing (1950) ai LLM moderni
   - I momenti chiave: dagli "inverni IA" alla rivoluzione ChatGPT
   - Timeline essenziale: 1950-2025

3. **Cos'è un Large Language Model** (15 min)
   - Architettura e funzionamento
   - Come i LLM "apprendono"
   - Cosa sanno fare (e cosa NON sanno fare)

4. **Panoramica Strumenti 2025** (10 min)
   - ChatGPT (OpenAI)
   - Claude (Anthropic)
   - Gemini (Google)
   - GitHub Copilot e altri strumenti

5. **Limiti Critici e Uso Etico** (10 min)
   - Allucinazioni: quando l'IA "inventa"
   - Bias e knowledge cutoff
   - Responsabilità e etica professionale

### **PARTE 2: PRATICA (60 minuti)**

6. **Setup e Configurazione** (15 min)
   - Creazione account ChatGPT/Claude/Gemini
   - Interfaccia e prime esplorazioni
   - Configurazioni base

7. **Primi Esperimenti Guidati** (20 min)
   - Dalla domanda semplice al prompt strutturato
   - Esempi pratici step-by-step
   - Analisi degli output

8. **Riconoscere e Gestire Allucinazioni** (15 min)
   - Esercizi di identificazione
   - Tecniche di verifica
   - Cosa fare quando l'IA sbaglia

9. **Confronto tra LLM Diversi** (10 min)
   - Stessa domanda a ChatGPT, Claude e Gemini
   - Analisi delle differenze
   - Quando usare quale strumento

---

---

# PARTE 1: TEORIA (60 MINUTI)

---

## 1. INTRODUZIONE E CONTESTO (10 minuti)

### 1.1 Benvenuto al Corso

Benvenuto al corso **"Intelligenza Artificiale e Programmazione Assistita"** per studenti ITS!

Questo non è un corso tradizionale di programmazione, né un corso teorico sull'intelligenza artificiale. È qualcosa di completamente nuovo: un corso che ti insegna a **collaborare efficacemente con l'IA** per diventare un programmatore più produttivo, creativo e professionale.

### 1.2 Perché l'IA è Importante nel 2025?

Nel 2025, l'intelligenza artificiale non è più fantascienza o tecnologia futuristica. È una **realtà quotidiana** che sta trasformando radicalmente il modo in cui lavoriamo, programmiamo e risolviamo problemi.

**Alcuni dati che dimostrano questa rivoluzione:**

📊 **GitHub Copilot:** Oltre 1.5 milioni di sviluppatori paganti lo usano quotidianamente (2024)
📊 **ChatGPT:** Ha raggiunto 100 milioni di utenti in soli 2 mesi dal lancio (record assoluto)
📊 **Stack Overflow:** Il traffico è calato del 35% dopo ChatGPT (gli sviluppatori chiedono all'IA)
📊 **Studi di produttività:** Gli sviluppatori che usano IA completano task il 55% più velocemente

**Cosa significa per te come studente ITS?**

1. **Nuove competenze richieste:** Le aziende non cercano più solo programmatori che sanno scrivere codice, ma professionisti che sanno **collaborare con l'IA** per produrre software di qualità.

2. **Democratizzazione della programmazione:** L'IA abbassa la barriera d'ingresso. Puoi realizzare progetti complessi anche se sei alle prime armi, **purché tu sappia guidare l'IA correttamente**.

3. **Focus sulle competenze di alto livello:** Meno tempo su sintassi e boilerplate, più tempo su architettura, design, problem solving e validazione critica.

### 1.3 Il Ruolo dell'IA nella Programmazione Moderna

**L'IA NON sostituisce il programmatore.** Questa è una credenza errata che va subito chiarita.

**Analogia del pilota e del copilota:**

Immagina un aereo moderno. Il pilota automatico può gestire gran parte del volo, ma:
- ❌ **NON** può decollare in sicurezza senza supervisione
- ❌ **NON** può gestire situazioni impreviste
- ❌ **NON** può prendere decisioni strategiche
- ❌ **NON** può validare che tutto funzioni correttamente

Il pilota umano:
- ✅ **Decide** la rotta e la strategia
- ✅ **Supervisiona** il pilota automatico
- ✅ **Interviene** quando necessario
- ✅ **Valida** che tutto sia corretto

**Lo stesso vale per l'IA nella programmazione:**

```
TU (Programmatore)                  IA (Assistente)
├─ Definisci il problema           ├─ Suggerisce soluzioni
├─ Scegli l'architettura           ├─ Genera codice boilerplate
├─ Validi la correttezza           ├─ Propone alternative
├─ Testi e debuggi                 ├─ Aiuta a trovare bug
├─ Prendi decisioni finali         ├─ Fornisce informazioni
└─ SEI RESPONSABILE                └─ È UNO STRUMENTO
```

**Il mindset corretto:**

> **"L'IA è un collega junior super veloce ma che commette errori. Tu sei il senior che supervisiona."**

Questa metafora è fondamentale: un collega junior può essere estremamente utile se lo guidi bene, ma devi sempre verificare il suo lavoro.

### 1.4 Cosa Imparerai in Questo Corso

Questo corso è strutturato per darti competenze **immediatamente spendibili** nel mondo del lavoro:

**Settimana 1-2: Fondamenti**
- Come funzionano i LLM
- Come scrivere prompt efficaci
- Come riconoscere e correggere allucinazioni

**Settimana 3-4: Programmazione Assistita**
- Generare codice C sicuro con l'IA
- Debug e testing con supporto IA
- Best practices e pattern comuni

**Settimana 5: Progetto Completo**
- Implementare un sistema reale end-to-end
- Documentazione professionale
- Portfolio per colloqui di lavoro

---

## 2. STORIA DELL'INTELLIGENZA ARTIFICIALE (15 minuti)

### 2.1 Perché Studiare la Storia?

Prima di immergerci nell'uso pratico dell'IA, è importante comprendere **da dove veniamo**. La storia dell'IA è una storia di:

- 🎢 **Cicli di hype e delusione** ("inverni IA")
- 💡 **Scoperte rivoluzionarie** che hanno cambiato tutto
- 🤔 **Limiti fondamentali** che ancora oggi influenzano i sistemi
- 🚀 **Progressi esponenziali** negli ultimi anni

Capire questa storia ti aiuterà a:
- **Contestualizzare** le capacità attuali dell'IA
- **Riconoscere** i pattern storici (cosa funziona, cosa fallisce)
- **Anticipare** dove stiamo andando
- **Evitare** errori del passato

### 2.2 Timeline Essenziale: 1950-2025

#### **📅 1950: Il Test di Turing - Nasce la Domanda**

**Alan Turing**, matematico britannico, pubblica il paper **"Computing Machinery and Intelligence"** dove propone una domanda rivoluzionaria:

> **"Possono le macchine pensare?"**

Invece di definire filosoficamente "pensiero", Turing propone un test pragmatico:

**Il Test di Turing (Imitation Game):**
- Un umano conversa in chat con due interlocutori anonimi
- Uno è umano, l'altro è una macchina
- Se l'umano non riesce a distinguere chi è la macchina, allora la macchina "pensa"

**Perché è importante oggi:** ChatGPT e Claude hanno essenzialmente **superato** il Test di Turing in molte conversazioni. Ma questo non significa che "pensino" davvero!

#### **📅 1956: La Conferenza di Dartmouth - Nasce l'IA come Disciplina**

**Estate 1956, Dartmouth College (USA)**

Un gruppo di ricercatori (John McCarthy, Marvin Minsky, Claude Shannon, Nathaniel Rochester) organizza un workshop di 2 mesi dove coniarono per la prima volta il termine **"Artificial Intelligence"**.

**La proposta originale diceva:**

> "Lo studio sarà condotto sulla base della congettura che ogni aspetto dell'apprendimento o qualsiasi altra caratteristica dell'intelligenza possa in linea di principio essere descritto con tale precisione da poter costruire una macchina per simularlo."

**Ottimismo iniziale (eccessivo):** Pensavano di risolvere l'IA in pochi anni. Ci sono voluti 70 anni per ChatGPT.

#### **📅 1957-1969: I Primi Successi**

**Perceptron (1957):**
- Frank Rosenblatt crea il primo "neurone artificiale"
- Può imparare a classificare pattern semplici
- Venne dimostrato su hardware fisico, non solo teoria

**ELIZA (1961-1963):**
- Primo "chatbot" della storia (MIT, Joseph Weizenbaum)
- Simulava uno psicoterapeuta rogersiano
- **Trucco:** Usava pattern matching semplice, NON comprensione vera
- **Rivelazione scioccante:** Anche sapendo che era un trucco, le persone si affezionavano e confidavano segreti

```
Utente: "Ho problemi con mio padre"
ELIZA: "Raccontami di più sulla tua famiglia"
Utente: "Mio padre non mi capisce"
ELIZA: "Perché pensi che tuo padre non ti capisca?"
```

**Lezione per oggi:** L'effetto ELIZA persiste. Gli utenti tendono a **antropomorfizzare** l'IA, attribuendole comprensione che non ha.

#### **📅 1974-1980: Il Primo "Inverno dell'IA"**

**Cosa successe:**
- I finanziamenti pubblici vengono drasticamente tagliati
- I risultati pratici non corrispondono alle promesse
- **Lighthill Report (UK, 1973):** Report governativo devastante che conclude che l'IA è sopravvalutata

**Problemi principali:**
1. **Computational Limits:** I computer erano troppo lenti e con poca memoria
2. **Limiti teorici:** Alcune cose che sembravano semplici (riconoscere una sedia) erano impossibili
3. **Overhype:** Erano state fatte promesse irrealistiche

**Perceptrons Book (Minsky & Papert, 1969):**
- Dimostrazione matematica che i perceptron non possono risolvere problemi non-linearmente separabili (es: XOR)
- Questo **uccise la ricerca sulle reti neurali per 20 anni**

**Lezione per oggi:** L'hype eccessivo seguito da delusione è un pattern ricorrente. Oggi siamo in un momento di hype (ChatGPT), ma dobbiamo rimanere critici.

#### **📅 1980-1987: Il Boom dei Sistemi Esperti**

**Cosa sono i sistemi esperti:**
Programmi che codificano la conoscenza di esperti umani in **regole IF-THEN**.

**Esempio di sistema esperto:**
```
IF paziente ha febbre > 38°C
   AND paziente ha tosse
   AND paziente ha mal di gola
THEN probabile diagnosi: influenza
     raccomandazione: riposo e paracetamolo
```

**Sistemi famosi:**
- **MYCIN (1972-1980):** Diagnosi di infezioni batteriche del sangue
- **XCON (1980):** Configurazione di sistemi computer VAX (risparmiò milioni a Digital Equipment Corporation)
- **DENDRAL:** Analisi struttura molecolare

**Successo commerciale:** Aziende investirono miliardi. Boom di "LISP Machines" (computer specializzati per IA).

#### **📅 1987-1993: Il Secondo "Inverno dell'IA"**

**Il crollo:**
- Le aziende si rendono conto che i sistemi esperti sono **fragili**
- Ogni regola deve essere codificata manualmente
- Impossibile gestire incertezza e casi non previsti
- Il mercato delle LISP Machines crolla: troppo costose, tecnologia obsoleta

**Lezione per oggi:** L'IA basata su regole manuali non scala. I LLM moderni "apprendono" da dati, non da regole scritte a mano.

#### **📅 1997: Deep Blue Batte Kasparov**

**11 maggio 1997:** Il computer Deep Blue (IBM) batte Garry Kasparov, campione mondiale di scacchi.

**Significato storico:**
- Prima volta che una macchina batte un umano al top level in un dominio considerato di "alta intelligenza"
- **Ma:** Deep Blue usava forza bruta (calcolo di milioni di posizioni), NON comprensione strategica

**Quote di Kasparov dopo la sconfitta:**
> "Potevo sentire... una nuova forma di intelligenza dall'altra parte del tavolo"

**Reality check:** Deep Blue era specializzato SOLO negli scacchi. Non sapeva giocare a dama.

#### **📅 2006-2011: Il Risveglio - Deep Learning**

**Cosa cambia:**
1. **Hardware più potente:** GPU (schede grafiche) si rivelano perfette per addestrare reti neurali
2. **Big Data:** Internet fornisce quantità immense di dati
3. **Algoritmi migliorati:** Backpropagation, ReLU, Dropout

**Geoffrey Hinton** e il suo team dimostrano che reti neurali PROFONDE (molti layer) possono apprendere rappresentazioni complesse.

**ImageNet (2009):**
Dataset di 14 milioni di immagini etichettate. Diventerà il benchmark per la computer vision.

#### **📅 2012: AlexNet - La Rivoluzione Deep Learning**

**ImageNet Competition 2012:**

AlexNet (rete neurale profonda) **DISTRUGGE** la competizione:
- **Errore di AlexNet:** 15.3%
- **Secondo classificato (metodi tradizionali):** 26.2%
- **Miglioramento:** ~11% in UN ANNO (prima ci volevano decenni)

**Impatto:**
- Tutte le aziende tech si gettano sul deep learning
- Google, Facebook, Microsoft assumono ricercatori in massa
- Boom di investimenti

#### **📅 2014-2016: Applicazioni Pratiche**

**GANs - Generative Adversarial Networks (2014):**
- Ian Goodfellow inventa le reti generative avversarie
- Fondamentali per generare immagini realistiche (DALL-E, Midjourney, Stable Diffusion verranno dopo)

**AlphaGo (2016):**
- DeepMind (Google) crea AlphaGo
- **Marzo 2016:** Batte Lee Sedol (campione mondiale di Go) 4-1
- **Significato:** Go ha 10^170 posizioni possibili (più atomi nell'universo)
- Forza bruta è impossibile: AlphaGo usa **intuizione** appresa con reti neurali

**Quote di Lee Sedol:**
> "Ho pensato che AlphaGo fosse basato su probabilità e statistica. Ma quando ho visto questa mossa, ho cambiato idea. Sicuramente AlphaGo è creativo."

#### **📅 2017: L'Architettura Transformer - Punto di Svolta**

**Giugno 2017:** Ricercatori Google pubblicano paper **"Attention is All You Need"**

**Introduzione del Transformer:**
Un nuovo tipo di architettura neurale basata su **"attention mechanism"** (meccanismo di attenzione).

**Perché è rivoluzionario:**
- Prima: le reti neurali processavano testo parola per parola sequenzialmente (lento)
- Transformer: processa tutto il testo in parallelo guardando relazioni tra TUTTE le parole (veloce)

**Meccanismo di attenzione - Esempio:**

Frase: "Il gatto ha bevuto il latte perché aveva sete"

Domanda: A cosa si riferisce "aveva"?

**Transformer calcola "attenzione":**
- "aveva" → "gatto" (alta attenzione)
- "aveva" → "latte" (bassa attenzione)

Quindi comprende che è il **gatto** che aveva sete, non il latte.

**Conseguenza:** TUTTI i LLM moderni (GPT, BERT, Claude, Gemini) usano architettura Transformer o sue varianti.

#### **📅 2018-2020: L'Era dei LLM Pre-ChatGPT**

**BERT (2018 - Google):**
- Bidirectional Encoder Representations from Transformers
- Addestrato su 3.3 miliardi di parole (Wikipedia + libri)
- Rivoluziona la comprensione del linguaggio naturale

**GPT-2 (2019 - OpenAI):**
- 1.5 miliardi di parametri
- OpenAI inizialmente NON lo rilascia pubblicamente per paura di abusi
- Può generare testo coerente paragrafo dopo paragrafo

**GPT-3 (2020 - OpenAI):**
- **175 miliardi di parametri** (100x più grande di GPT-2)
- Addestrato su ~500 miliardi di token
- Costo addestramento: stimato 4-12 milioni di dollari
- **Capacità emergenti:** Può fare task mai visti prima senza training specifico (few-shot learning)

**Accesso API:** OpenAI rilascia GPT-3 via API (a pagamento). Migliaia di startup costruiscono prodotti sopra.

#### **📅 30 Novembre 2022: ChatGPT - Il Momento Spartiacque**

**OpenAI rilascia ChatGPT gratuitamente al pubblico.**

**Cosa lo rende speciale:**
- Interfaccia chat conversazionale (non API tecnica)
- Gratuito per tutti
- Incredibilmente capace: scrive codice, saggi, poesie, risponde domande complesse

**Crescita esplosiva:**
- **5 giorni:** 1 milione di utenti
- **2 mesi:** 100 milioni di utenti (record assoluto di qualsiasi app)
- Per confronto: TikTok ci mise 9 mesi, Instagram 2.5 anni

**Impatto culturale:**
- Copertine di tutti i giornali mondiali
- Governi iniziano a discutere regolamentazione
- Scuole e università vietano (poi cambiano idea)
- Milioni di persone usano IA per la prima volta

**Conseguenza:** Microsoft investe $10 miliardi in OpenAI. Google lancia Bard (ora Gemini) in tutta fretta. La corsa all'IA si intensifica.

#### **📅 2023-2025: La Rivoluzione dei LLM**

**Marzo 2023: GPT-4**
- Multimodale (capisce immagini e testo)
- Superato test SAT, esame avvocati, esami medici
- Ragionamento molto più avanzato

**Aprile 2023: Claude (Anthropic)**
- Competitor di ChatGPT focalizzato su sicurezza
- Finestra di contesto enorme (100k+ token)
- Particolarmente bravo in ragionamento e programmazione

**Maggio 2023: Google Bard (ora Gemini)**
- Risposta di Google a ChatGPT
- Integrato con Google Search
- Accesso a informazioni real-time

**Luglio 2023: Llama 2 (Meta)**
- **Open source** e gratuito
- Chiunque può scaricarlo ed eseguirlo localmente
- Democratizzazione dell'accesso all'IA

**Fine 2023-2025: Esplosione di Applicazioni**
- GitHub Copilot X: programmazione assistita avanzata
- GPT-4o: multimodale ultra-veloce
- Gemini Pro 1.5: finestra di contesto da 2 milioni di token
- Claude Sonnet 3.5: eccellenza in coding
- DALL-E 3, Midjourney v6, Stable Diffusion 3: generazione immagini fotorealistica
- Sora (OpenAI): generazione video da testo

**Stato attuale (2025):**
- L'IA è mainstream: centinaia di milioni di utenti
- Quasi ogni professione sta sperimentando integrazione IA
- Dibattito intenso su regolamentazione, etica, futuro del lavoro

### 2.3 Lezioni dalla Storia

**Cosa ci insegna questa storia:**

1. **I cicli di hype sono normali:** Siamo probabilmente al picco di un ciclo di hype. Aspettiamoci una correzione (ma i LLM sono qui per restare).

2. **L'IA non è "intelligente" come sembra:** Ogni era ha avuto il suo "trucco" (ELIZA: pattern matching, Deep Blue: forza bruta, LLM: completamento statistico di pattern). Non è vera comprensione.

3. **Le breakthrough arrivano da combinazioni:** Hardware + dati + algoritmi. Transformer ha funzionato perché c'erano GPU potenti e Internet forniva dati.

4. **L'applicazione pratica richiede tempo:** Dal Transformer (2017) a ChatGPT (2022) sono passati 5 anni di ingegnerizzazione.

5. **L'open source accelera il progresso:** Transformer paper era pubblico. Llama 2 open source ha generato migliaia di progetti.

**Implicazioni per te:**
- Usa l'IA ora, ma preparati ad adattarti quando cambierà
- Focalizzati su competenze trasferibili (problem solving, critical thinking)
- Non affezionarti troppo a uno strumento specifico

---

## 3. COS'È UN LARGE LANGUAGE MODEL (15 minuti)

### 3.1 Definizione e Concetti Base

**Large Language Model (LLM):**

Un modello di intelligenza artificiale addestrato su quantità enormi di testo per **predire la prossima parola** in una sequenza.

**Esempio banale:**

Input: "Il gatto è salito sul..."
LLM predice: "tetto" (alta probabilità), "tavolo" (media probabilità), "elefante" (bassa probabilità)

**Ma se fosse solo questo, non sarebbe impressionante.** La magia sta in cosa emerge da questa semplice capacità quando applicata a **scala massiva**.

### 3.2 Come Funziona un LLM (Spiegazione Semplificata)

**Step 1: Training (Addestramento)**

Immagina di leggere l'intera Internet (semplificando):

```
Testi di input:
- Wikipedia intera (tutte le lingue)
- Milioni di libri
- Codice sorgente da GitHub
- Siti web, forum, discussioni
- Paper scientifici
```

**Dimensioni tipiche (GPT-4):**
- ~13 trilioni di token (parole/pezzi di parole)
- ~45 TB di testo compresso
- Costo: ~$100 milioni di compute

**Cosa fa il modello:**

Per ogni frase vista, il modello prova a predire la prossima parola. Se sbaglia, aggiusta i suoi parametri interni (pesi) per migliorare la predizione.

**Esempio di training:**

```
Testo: "La capitale della Francia è Parigi"

Il modello vede:
"La capitale della Francia è ___"

Predice: "Berlino" (SBAGLIATO)
Sistema: "No, era Parigi. Aggiusto i pesi."

Dopo milioni di esempi simili:
"La capitale della Francia è ___"
Predice: "Parigi" ✅
```

**Step 2: Cosa Emerge**

Dopo aver visto miliardi di esempi di:
- Codice Python funzionante
- Spiegazioni matematiche
- Conversazioni domanda-risposta
- Traduzioni
- Ragionamento logico

Il modello sviluppa **capacità emergenti**:
- ✅ Può scrivere codice in linguaggi che segue schemi simili
- ✅ Può ragionare su problemi nuovi
- ✅ Può tradurre lingue mai viste esplicitamente associate
- ✅ Può spiegare concetti complessi

**Nota cruciale:** Nessuna di queste capacità è stata "programmata". Sono emerse dal training su testi.

### 3.3 Architettura Interna (Concetti Semplificati)

**Transformer Architecture:**

Un LLM moderno (come GPT-4) è composto da:

```
┌─────────────────────────────────┐
│  INPUT: "Scrivi una funzione"   │
└────────────┬────────────────────┘
             │
             ▼
      ┌─────────────┐
      │ Tokenization│ (divide in pezzi)
      └──────┬──────┘
             │
             ▼
      ┌────────────────┐
      │ Embeddings     │ (trasforma in numeri)
      └───────┬────────┘
             │
             ▼
   ┌────────────────────┐
   │ Transformer Layers │ (centinaia di layer)
   │ Layer 1            │
   │ Layer 2            │
   │   ...              │
   │ Layer 96           │
   └────────┬───────────┘
             │
             ▼
      ┌─────────────┐
      │ Prediction  │ (prossima parola)
      └──────┬──────┘
             │
             ▼
┌────────────────────────────────────┐
│ OUTPUT: "def my_function():"      │
└────────────────────────────────────┘
```

**Attention Mechanism (la parte magica):**

Ogni layer "presta attenzione" a tutte le altre parole per capire il contesto.

**Esempio:**

```
Input: "La torre Eiffel è a Parigi. È molto alta."

Quando processa "È molto alta", il modello:
1. Presta attenzione a "torre Eiffel" (alto score)
2. Ignora "Parigi" (basso score per "alta")
3. Capisce che "alta" si riferisce alla torre

Senza attention, non capirebbe a cosa si riferisce "È".
```

**Parametri:**

Un "parametro" è un numero che il modello aggiusta durante il training.

**Dimensioni:**
- GPT-3: 175 miliardi di parametri
- GPT-4: stimato ~1.7 trilioni di parametri (OpenAI non ha confermato)
- Claude 3 Opus: ~100-500 miliardi (stimato)

**Analogia:** Se il cervello umano avesse ~100 trilioni di sinapsi, i parametri sono come le "forze" delle connessioni sinaptiche.

### 3.4 Cosa Sanno Fare i LLM

**Capacità Principali:**

1. **Completamento di testo**
   ```
   Input: "C'era una volta un re che..."
   Output: "...regnava su un regno lontano e misterioso..."
   ```

2. **Risposta a domande**
   ```
   Input: "Cos'è il polimorfismo in C++?"
   Output: [Spiegazione dettagliata]
   ```

3. **Generazione di codice**
   ```
   Input: "Scrivi una funzione C che inverta una stringa"
   Output: [Codice C funzionante]
   ```

4. **Traduzione**
   ```
   Input: "Translate to English: 'Ciao, come stai?'"
   Output: "Hello, how are you?"
   ```

5. **Riassunto**
   ```
   Input: [Testo di 10 pagine] + "Riassumi in 3 punti"
   Output: [3 bullet points]
   ```

6. **Ragionamento (limitato)**
   ```
   Input: "Se tutti i gatti hanno la coda, e Felix è un gatto, Felix ha la coda?"
   Output: "Sì, Felix ha la coda perché [ragionamento]"
   ```

7. **Creatività**
   ```
   Input: "Scrivi una poesia sul debugging"
   Output: [Poesia originale e divertente]
   ```

8. **Analisi e debugging di codice**
   ```
   Input: [Codice con bug] + "Trova l'errore"
   Output: "Il bug è alla linea 12: [spiegazione]"
   ```

### 3.5 Cosa NON Sanno Fare (Limiti Fondamentali)

**❌ NON hanno vera comprensione**

L'LLM manipola simboli statisticamente, non "capisce" nel senso umano.

**Esempio rivelatore:**

```
Prompt: "Quante lettere 'r' ci sono nella parola 'strawberry'?"

ChatGPT (GPT-3.5): "Ci sono 2 lettere 'r' in 'strawberry'"

SBAGLIATO! Ce ne sono 3: st-r-awber-r-y
```

Perché sbaglia? Perché il modello lavora su **token**, non lettere individuali. Non "vede" la parola come la vediamo noi.

**❌ NON hanno accesso al mondo reale**

Un LLM puro (senza estensioni) non può:
- Accedere a Internet in tempo reale
- Eseguire codice
- Vedere immagini (a meno che non sia multimodale)
- Interagire con API

**❌ NON hanno memoria persistente tra sessioni**

Ogni conversazione ricomincia da zero (a meno che non usi servizi con "memory" artificiale).

**❌ NON possono ragionare su matematica complessa in modo affidabile**

```
Prompt: "Calcola 12847 × 8293"

LLM può dare: "106,547,871" (SBAGLIATO)
Risposta corretta: 106,508,071
```

Perché? Perché ha imparato pattern di calcoli, ma non ha una calcolatrice interna affidabile.

**Soluzione:** Usa tool esterni (Python, calculator API).

**❌ NON possono garantire correttezza**

Anche quando il codice "sembra" giusto, potrebbe avere bug sottili.

### 3.6 Il Modello Statistico: Perché "Allucinano"

**Cosa succede internamente:**

Quando un LLM genera una risposta, sta campionando da una **distribuzione di probabilità** su tutte le possibili prossime parole.

**Esempio:**

```
Input: "La capitale dell'Italia è"

Distribuzione di probabilità (semplificata):
- "Roma" → 95%
- "Milano" → 2%
- "Firenze" → 1%
- "Napoli" → 1%
- [altre parole] → 1%
```

**Sampling con temperature:**

Il parametro "temperature" controlla la casualità:
- **Temperature bassa (0.1):** Sempre la risposta più probabile → "Roma" (deterministico)
- **Temperature alta (1.5):** Più variabilità → Potrebbe scegliere "Milano" qualche volta

**Problema delle allucinazioni:**

Se il modello non "sa" la risposta con certezza, distribuisce probabilità su più opzioni. A volte sceglie quella sbagliata, ma la presenta con **tono sicuro e assertivo**.

**Esempio di allucinazione:**

```
Prompt: "Chi ha vinto il premio Nobel per la fisica nel 2087?"

LLM: "Il premio Nobel per la fisica nel 2087 è stato vinto
      dal Dr. Marco Santini per i suoi studi sulla fusione fredda."
```

**Tutto inventato!** Il 2087 è nel futuro, ma l'LLM genera comunque una risposta plausibile seguendo il pattern di altre risposte su Nobel.

---

## 4. PANORAMICA STRUMENTI 2025 (10 minuti)

### 4.1 Il Panorama dei LLM nel 2025

Nel 2025, abbiamo un ecosistema ricco e competitivo di LLM. Ogni strumento ha punti di forza specifici.

### 4.2 ChatGPT (OpenAI)

**Modelli principali:**
- **GPT-4o** (Omni): Multimodale, velocissimo
- **GPT-4 Turbo**: Versione migliorata di GPT-4
- **GPT-3.5 Turbo**: Gratuito, veloce ma meno capace

**Punti di forza:**
- ✅ Interfaccia più user-friendly
- ✅ Enorme conoscenza generale
- ✅ Ottimo per brainstorming e ideazione
- ✅ Integrazione con DALL-E (generazione immagini)
- ✅ Browsing web (nelle versioni Plus/Team)
- ✅ Code Interpreter (esegue codice Python)

**Limiti:**
- ❌ Knowledge cutoff (dati fino a una certa data)
- ❌ Versione gratuita più limitata
- ❌ A volte "inventa" dettagli tecnici

**Quando usarlo:**
- Spiegazioni generali
- Brainstorming di idee
- Scrittura creativa
- Prototipazione rapida di codice

**Costi:**
- **Gratuito:** GPT-3.5 Turbo con limiti
- **Plus ($20/mese):** GPT-4, GPT-4o, più messaggi, browsing, DALL-E
- **API:** Pay-per-use (economico per uso occasionale)

### 4.3 Claude (Anthropic)

**Modelli principali:**
- **Claude 3 Opus**: Top di gamma (ragionamento complesso)
- **Claude 3 Sonnet**: Bilanciato (ottimo per codice)
- **Claude 3 Haiku**: Veloce ed economico

**Punti di forza:**
- ✅ **Eccellente per programmazione** (specialmente Sonnet)
- ✅ Finestra di contesto enorme (100k-200k token = ~150-300 pagine)
- ✅ Molto attento a sicurezza ed etica
- ✅ Ragionamento lungo e strutturato
- ✅ Ottimo per analisi di codice complesso

**Limiti:**
- ❌ Più "cauto" (a volte rifiuta richieste legittime)
- ❌ Interfaccia meno rifinita di ChatGPT
- ❌ Limiti di messaggio più stringenti nel piano gratuito

**Quando usarlo:**
- **Programmazione complessa** (è spesso migliore di GPT-4)
- Analisi di codebase grandi
- Ragionamento su testi lunghi
- Review di codice

**Costi:**
- **Gratuito:** Accesso limitato a Claude 3 Sonnet
- **Pro ($20/mese):** 5x più messaggi, accesso a Opus
- **API:** Pay-per-use

### 4.4 Gemini (Google)

**Modelli principali:**
- **Gemini Ultra 1.5**: Top di gamma
- **Gemini Pro 1.5**: Bilanciato
- **Gemini Flash**: Veloce

**Punti di forza:**
- ✅ Integrazione con Google Search (informazioni real-time)
- ✅ Finestra di contesto record (fino a 2 milioni di token)
- ✅ Multimodale avanzato
- ✅ Gratuito per la maggior parte degli usi
- ✅ Ottimo per ricerca e fact-checking

**Limiti:**
- ❌ Meno consistente di GPT-4/Claude
- ❌ A volte eccessivamente verboso
- ❌ Disponibilità regionale variabile

**Quando usarlo:**
- Ricerca con informazioni aggiornate
- Analisi di documenti enormi (grazie alla finestra massiva)
- Quando serve accesso a Google Search

**Costi:**
- **Gratuito:** Ampio accesso
- **Gemini Advanced ($20/mese):** Accesso a Ultra, più quota
- **API:** Pay-per-use

### 4.5 GitHub Copilot (Microsoft/OpenAI)

**Cos'è:** Assistente IA integrato nell'editor di codice (VSCode, JetBrains, ecc.)

**Come funziona:**
Mentre scrivi codice, Copilot suggerisce completamenti in tempo reale.

**Esempio:**
```c
// Tu scrivi:
// Funzione che calcola il fattoriale

// Copilot suggerisce automaticamente:
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

**Punti di forza:**
- ✅ **Massima produttività** per coding
- ✅ Integrato direttamente nell'editor
- ✅ Completamento inline istantaneo
- ✅ Suggerisce funzioni intere da commenti
- ✅ Chat integrata per domande contestuali

**Limiti:**
- ❌ Richiede subscription
- ❌ Funziona meglio su linguaggi popolari (Python, JS, Java)
- ❌ Può suggestionare verso codice non ottimale

**Quando usarlo:**
- **Sempre** quando scrivi codice!
- Boilerplate e codice ripetitivo
- Implementazione veloce di algoritmi standard

**Costi:**
- **$10/mese** per individui
- **GRATUITO per studenti** con GitHub Student Pack (https://education.github.com/pack)

### 4.6 Confronto Rapido

| Strumento | Migliore per | Costo | Livello Studente |
|-----------|--------------|-------|------------------|
| **ChatGPT** | Uso generale, brainstorming | Gratis/€20 | Ottimo inizio |
| **Claude** | Programmazione, analisi codice | Gratis/€20 | Eccellente per codice |
| **Gemini** | Ricerca, info aggiornate | Gratis | Buono per ricerca |
| **Copilot** | Produttività coding | Gratis studenti | ESSENZIALE |

**Consiglio per studenti ITS:**

1. **Inizia con:** ChatGPT o Claude gratuito per imparare prompting
2. **Procurati:** GitHub Student Pack per Copilot gratuito
3. **Sperimenta:** Usa tutti e 3 (ChatGPT, Claude, Gemini) per confrontare
4. **Specializzati:** Dopo 2-3 settimane, scegli quello che preferisci come principale

### 4.7 Altri Strumenti Utili

**Cursor** (https://cursor.sh/)
- Editor di codice con IA integrata
- Alternative a VSCode + Copilot
- Gratuito per uso base

**Perplexity AI** (https://perplexity.ai/)
- Motore di ricerca con IA
- Fornisce fonti per ogni affermazione
- Ottimo per ricerca tecnica

**Phind** (https://phind.com/)
- Motore di ricerca specializzato per sviluppatori
- Risponde con codice e spiegazioni
- Gratuito

**Stack Overflow + OverflowAI**
- Stack Overflow tradizionale ora ha integrazione IA
- Combina domande umane + risposte IA

---

## 5. LIMITI CRITICI E USO ETICO (10 minuti)

### 5.1 Allucinazioni: Quando l'IA "Inventa"

**Definizione:**
Un'**allucinazione** è quando l'IA genera informazioni false o inventate presentandole con sicurezza come se fossero vere.

**Perché accade:**
Come spiegato prima, l'LLM è un modello statistico. Quando non "sa" la risposta, completa comunque il pattern in modo plausibile.

**Esempi reali di allucinazioni:**

**Esempio 1: Funzioni inesistenti**
```c
// Chiedi a ChatGPT: "Come leggere un file binario in C?"

// Potrebbe suggerire:
#include <stdio.h>

int main() {
    FILE *fp = fopen("file.bin", "rb");
    read_binary(fp);  // ← QUESTA FUNZIONE NON ESISTE!
    fclose(fp);
}
```

**Esempio 2: Librerie inventate**
```
Prompt: "Come fare HTTP requests in C?"

Risposta: "Usa la libreria libhttpeasy:
           #include <httpeasy.h>
           http_get('https://example.com');"

PROBLEMA: libhttpeasy NON ESISTE!
```

**Esempio 3: Riferimenti accademici falsi**
```
Prompt: "Quali studi supportano che X causa Y?"

Risposta: "Lo studio di Smith et al. (2019) pubblicato
           su Nature dimostra che X causa Y."

PROBLEMA: Lo studio non esiste! Nome autore, anno e
          rivista sembrano realistici ma sono inventati.
```

**Come riconoscere allucinazioni:**

1. **Diffida di nomi specifici che non conosci**
   - Funzioni di libreria mai sentite
   - Autori di studi
   - Tool o comandi OS strani

2. **Controlla documentazione ufficiale**
   - Se l'IA suggerisce una funzione, cerca la documentazione online

3. **Compila e testa SEMPRE il codice**
   - Un errore di compilazione rivela subito allucinazioni

4. **Chiedi fonti**
   - "Puoi darmi il link alla documentazione ufficiale?"
   - Se l'IA non può, probabilmente ha inventato

5. **Fai cross-check con più LLM**
   - Chiedi la stessa cosa a ChatGPT, Claude e Gemini
   - Se danno risposte diverse, approfondir

### 5.2 Bias (Pregiudizi)

**Definizione:**
I LLM riflettono i bias presenti nei dati di training (Internet, libri, ecc.).

**Esempi di bias:**

**Bias di genere:**
```
Prompt: "Il dottore è entrato nella stanza. ___ ha detto..."

LLM potrebbe preferire: "Lui ha detto" (assumendo dottore = uomo)
Anche se: "Lei ha detto" è ugualmente valido
```

**Bias culturale:**
```
Prompt: "Genera un nome casuale per un CEO"

LLM potrebbe generare: "John Smith", "Michael Johnson"
Meno frequente: "Jamal Washington", "Wei Zhang"
```

**Bias nel codice:**
L'IA potrebbe suggerire pratiche di coding che riflettono pattern popolari ma non ottimali.

**Come mitigare bias:**

1. **Sii esplicito:** Specifica requisiti inclusivi
   - "Genera una lista di 10 nomi casuali di varie etnie e generi"

2. **Revisiona criticamente:** Non accettare ciecamente output stereotipati

3. **Diversifica input:** Prova prompt da prospettive diverse

### 5.3 Knowledge Cutoff

**Definizione:**
I LLM sono addestrati su dati fino a una certa data. Non conoscono eventi successivi.

**Knowledge cutoff comuni (2025):**
- GPT-4: Ottobre 2023
- Claude 3: Inizio 2024
- Gemini: Dati più recenti grazie a Google Search

**Problema pratico:**

```
Prompt (nel 2025): "Qual è l'ultima versione di Python?"

GPT-4 potrebbe dire: "Python 3.11" (se il cutoff è 2023)
Realtà nel 2025: Python 3.13 è uscito
```

**Soluzioni:**

1. **Usa LLM con browsing:** ChatGPT Plus, Gemini
2. **Specifica data:** "Secondo dati fino a gennaio 2025, qual è...?"
3. **Verifica informazioni time-sensitive:** Sempre cross-check online

### 5.4 Limiti di Ragionamento

**I LLM NON sono perfetti in:**

**1. Matematica complessa**
```
Prompt: "Risolvi: ∫(x² + 3x + 2)dx da 0 a 5"

LLM potrebbe sbagliare calcoli numerici specifici
Soluzione: Usa tool matematici (WolframAlpha, SymPy)
```

**2. Logica multi-step complessa**
```
Prompt: "Ho 3 scatole. Scatola A contiene B e C.
         B contiene D. D contiene una chiave.
         In quale scatola devo guardare per la chiave?"

LLM può confondersi su ragionamenti annidati
```

**3. Programmazione con state complesso**
```c
// L'IA può generare codice con race conditions,
// memory leak sottili, o logic error non ovvi
```

**Soluzione: TESTA SEMPRE**

### 5.5 Uso Etico e Responsabile

**Principi fondamentali:**

**1. Trasparenza**
- ✅ **Dichiara** quando usi IA per generare codice/contenuti (nei contesti appropriati)
- ❌ NON spacciare lavoro generato da IA come completamente tuo senza verifica

**2. Verifica e responsabilità**
- ✅ **Tu sei responsabile** del codice che consegni, anche se generato da IA
- ✅ **Testa, comprendi, valida** tutto prima di usarlo

**3. Privacy e dati sensibili**
- ❌ **NON inviare:** Dati personali, password, segreti aziendali, codice proprietario
- ⚠️ **OpenAI, Anthropic, Google** potrebbero usare i tuoi input per training (controlla privacy policy)

**Esempio di cosa NON fare:**
```
Prompt SBAGLIATO: "Ecco il database password della mia azienda [dati],
                   aiutami a scrivere script di migrazione"

PROBLEMA: Hai appena esposto dati sensibili!
```

**Cosa fare invece:**
```
Prompt CORRETTO: "Aiutami a scrivere script di migrazione per un
                  database. Schema: users(id, username, hashed_password).
                  Usa dati di esempio fittizi."
```

**4. Plagio e originalità**
- ✅ Usa IA come **strumento di supporto**, non sostituto del pensiero
- ✅ L'IA suggerisce, TU decidi e adatti
- ❌ NON copiare e incollare senza comprendere

**5. Fair use in ambito educativo**
- ✅ **Accettabile:** Usare IA per imparare, comprendere concetti, generare esempi
- ❌ **NON accettabile:** Usare IA per fare compiti/esami senza comprensione
- ⚠️ **Chiedi al docente:** Ogni corso ha regole diverse

**6. Impatto ambientale e sociale**
- ⚠️ **Consapevolezza:** Addestrare GPT-4 ha emissioni di CO₂ significative
- ⚠️ **Labor concerns:** I dati di training includono contenuti umani (spesso non compensati)

### 5.6 Regolamentazioni e Futuro

**Situazione normativa (2025):**

**Unione Europea: AI Act**
- Regolamentazione basata su livelli di rischio
- LLM considerati "high-risk" in certi contesti
- Requisiti di trasparenza

**USA:**
- Regolamentazione a livello statale (California, New York)
- Nessuna legge federale comprensiva ancora

**Italia:**
- Garante Privacy attivo (ha bloccato ChatGPT temporaneamente nel 2023)
- Linee guida per uso in ambito pubblico e educativo

**Implicazioni per te:**
- Rimani aggiornato su normative
- Usa IA in modo responsabile anticipando future regole
- Documenta l'uso di IA nei tuoi progetti

---

---

# PARTE 2: PRATICA (60 MINUTI)

---

## 6. SETUP E CONFIGURAZIONE (15 minuti)

### 6.1 Obiettivi di questa Sezione

- ✅ Creare account su almeno 2 LLM (ChatGPT, Claude, o Gemini)
- ✅ Familiarizzare con l'interfaccia
- ✅ Configurare impostazioni base
- ✅ Fare i primi esperimenti

### 6.2 Creazione Account ChatGPT

**Step 1: Registrazione**

1. Vai su https://chat.openai.com
2. Clicca "Sign up"
3. Opzioni di registrazione:
   - Email + password
   - Google account
   - Microsoft account
   - Apple ID

**Consiglio:** Usa email universitaria se disponibile (potrebbe dare accesso a benefit educativi).

4. Verifica email
5. Completa profilo base

**Step 2: Interfaccia**

```
┌─────────────────────────────────────────────┐
│  [☰ Menu]  New Chat                [⚙️ Settings]│
├─────────────────────────────────────────────┤
│  Chat History:                              │
│  □ My first conversation                    │
│  □ Help with Python code                    │
│  □ ...                                      │
├─────────────────────────────────────────────┤
│                                             │
│         [Area conversazione]                │
│                                             │
│  ChatGPT:                                   │
│  Ciao! Come posso aiutarti oggi?            │
│                                             │
├─────────────────────────────────────────────┤
│  [Message ChatGPT...]              [Send ↑] │
└─────────────────────────────────────────────┘
```

**Step 3: Primo messaggio di test**

Scrivi:
```
Ciao! Sono uno studente ITS e sto imparando a usare l'IA
per la programmazione. Puoi darmi un esempio di codice
C che stampa "Hello World"?
```

**Analizza la risposta:**
- ✅ Ha generato codice C corretto?
- ✅ Ha incluso spiegazioni?
- ✅ Ha compilato (`#include <stdio.h>`, `int main()`, ecc.)?

**Step 4: Configurazioni utili**

Clicca ⚙️ Settings:

- **Theme:** Light/Dark (scegli preferenza)
- **Chat history:** Abilita per salvare conversazioni
- **Data controls:** Decide se OpenAI può usare i tuoi dati per training
  - ⚠️ Se disabiliti, più privacy ma nessun miglioramento del modello
- **Custom instructions:** (disponibile in Plus) Istruzioni permanenti per tutte le chat

### 6.3 Creazione Account Claude

**Step 1: Registrazione**

1. Vai su https://claude.ai
2. Clicca "Try Claude"
3. Registra con:
   - Email + verifica
   - Google account

4. Completa onboarding

**Step 2: Interfaccia**

Simile a ChatGPT ma con alcune differenze:

- **Chats:** Lista conversazioni sulla sinistra
- **Artifacts:** Claude può generare "artifacts" (documenti standalone che puoi esportare)
- **Upload files:** Puoi caricare file per analisi (PDF, immagini, codice)

**Step 3: Primo messaggio di test**

```
Analizza questo codice C e dimmi se ci sono problemi:

#include <stdio.h>

int main() {
    char buffer[10];
    gets(buffer);  // legge input
    printf("Hai scritto: %s\n", buffer);
    return 0;
}
```

**Claude dovrebbe identificare il problema:** `gets()` è pericoloso (buffer overflow)! Dovrebbe suggerirti `fgets()`.

**Osservazione:** Claude è spesso più attento a problemi di sicurezza nel codice.

### 6.4 Creazione Account Gemini

**Step 1: Accesso**

1. Vai su https://gemini.google.com
2. Accedi con account Google (non serve registrazione separata)

**Step 2: Interfaccia**

- Simile a ChatGPT
- Pulsante "Google it" per cercare info aggiornate
- Può generare immagini (nelle versioni avanzate)

**Step 3: Test con informazione aggiornata**

```
Qual è l'ultima versione stabile di GCC (compilatore C)
rilasciata nel 2025?
```

Gemini dovrebbe poter trovare info aggiornate tramite Google Search.

### 6.5 Confronto Iniziale delle Interfacce

**Prova questo esperimento:**

Chiedi LA STESSA domanda a tutti e 3:

```
Scrivi una funzione C che conta quante volte compare
una lettera in una stringa. Include gestione errori.
```

**Confronta:**
1. **Qualità codice:** Quale genera codice più pulito?
2. **Gestione errori:** Chi aggiunge controlli?
3. **Commenti:** Chi commenta meglio?
4. **Spiegazioni:** Chi spiega più chiaramente?

**Non c'è risposta "giusta":** Dipende dalle tue preferenze!

### 6.6 Configurazioni Avanzate (Opzionale)

**ChatGPT Plus (se hai abbonamento):**

- **Browse with Bing:** Abilita ricerca web
- **DALL-E:** Genera immagini
- **Code Interpreter:** Esegue Python (utile per calcoli)

**Claude Pro:**
- Più messaggi al giorno (5x)
- Accesso a Claude 3 Opus (più potente)

---

## 7. PRIMI ESPERIMENTI GUIDATI (20 minuti)

### 7.1 Esperimento 1: Dalla Domanda Semplice al Prompt Complesso

**Obiettivo:** Capire come prompt progressivamente più dettagliati producono output migliori.

**Step 1: Domanda semplice (vaga)**

```
Scrivi codice per ordinare array
```

**Analisi dell'output:**
- ❓ In che linguaggio? (Probabilmente Python o C, ma non specificato)
- ❓ Che tipo di array? (int, float, stringhe?)
- ❓ Che algoritmo? (bubble sort, quicksort, merge sort?)
- ❓ Ordine crescente o decrescente?

**L'IA farà assunzioni.** Probabilmente genererà qualcosa di generico.

**Step 2: Domanda più specifica**

```
Scrivi una funzione C che ordina un array di interi in ordine crescente
```

**Meglio!** Ora l'IA sa:
- Linguaggio: C
- Tipo: int
- Ordine: crescente

Ma ancora:
- ❓ Che algoritmo?
- ❓ Ordinamento in-place o nuovo array?
- ❓ Dimensione array?

**Step 3: Prompt dettagliato (ottimo)**

```
Scrivi una funzione C con le seguenti specifiche:

- Nome: sort_array
- Input: array di int, dimensione array
- Output: void (ordina in-place)
- Algoritmo: quicksort
- Gestione errori: controlla se array è NULL
- Includi: commenti esplicativi e esempio d'uso
```

**Ora l'IA ha tutte le informazioni!** Output sarà molto più preciso.

**Esercizio per te:**

Prova entrambe le versioni (vaga vs dettagliata) e confronta gli output.

### 7.2 Esperimento 2: Iterazione e Raffinamento

**Obiettivo:** Capire che puoi "dialogare" con l'IA per migliorare il codice.

**Step 1: Richiesta iniziale**

```
Scrivi una funzione C che legge un file di testo riga per riga
```

**Step 2: Analizza l'output**

L'IA probabilmente genererà qualcosa come:

```c
#include <stdio.h>

void read_file(const char *filename) {
    FILE *fp = fopen(filename, "r");
    char line[256];

    while (fgets(line, sizeof(line), fp) != NULL) {
        printf("%s", line);
    }

    fclose(fp);
}
```

**Problemi potenziali:**
- ❌ Non controlla se `fopen` ha fallito
- ❌ Buffer fisso (256 caratteri)
- ❌ Non gestisce linee più lunghe

**Step 3: Richieste di miglioramento**

```
Ottimo! Ora modifica la funzione per:
1. Controllare se fopen ha successo
2. Gestire linee di lunghezza arbitraria
3. Ritornare un codice di errore
```

**L'IA migliorerà il codice** aggiungendo:
- `if (fp == NULL) return -1;`
- Allocazione dinamica per linee lunghe
- `return 0;` per successo

**Step 4: Ulteriori raffinamenti**

```
Perfetto! Ultima cosa: aggiungi documentazione in stile Doxygen
```

L'IA aggiungerà commenti:

```c
/**
 * @brief Legge un file di testo riga per riga
 * @param filename Percorso del file da leggere
 * @return 0 se successo, -1 se errore
 */
```

**Lezione chiave:**
> **"Non devi ottenere tutto perfetto al primo prompt. Itera e raffina!"**

### 7.3 Esperimento 3: Spiegazione di Codice Esistente

**Obiettivo:** Usare l'IA per capire codice complesso.

**Scenario:** Hai trovato questo codice su Stack Overflow ma non capisci come funziona.

```c
int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}
```

**Prompt:**

```
Spiega riga per riga cosa fa questa funzione C.
Usa esempi concreti con numeri.

[incolla codice]
```

**L'IA dovrebbe spiegare:**

- `n & (n - 1)` rimuove il bit meno significativo impostato
- Loop conta quanti bit sono impostati (bit counting)
- Esempio con n=13 (binario: 1101) → 3 bit impostati

**Prova anche:**

```
Ci sono modi più efficienti? Mostra alternative
```

L'IA potrebbe suggerire lookup table o `__builtin_popcount()` (GCC).

### 7.4 Esperimento 4: Generazione di Test

**Obiettivo:** Far generare test cases all'IA.

**Hai scritto questa funzione:**

```c
int is_palindrome(const char *str) {
    if (str == NULL) return 0;

    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            return 0;
        }
    }
    return 1;
}
```

**Prompt:**

```
Genera 10 test cases per questa funzione che controlla
se una stringa è palindroma. Include:
- Casi normali (palindromi e non)
- Edge cases (stringa vuota, singolo carattere, NULL)
- Casi con spazi e punteggiatura

[incolla codice funzione]
```

**L'IA dovrebbe generare:**

```c
// Test cases
assert(is_palindrome("radar") == 1);      // palindromo semplice
assert(is_palindrome("hello") == 0);      // non palindromo
assert(is_palindrome("") == 1);           // stringa vuota
assert(is_palindrome("a") == 1);          // singolo char
assert(is_palindrome(NULL) == 0);         // NULL
assert(is_palindrome("A man a plan a canal Panama") == ?); // con spazi
// ... ecc
```

**Problema rivelato:** La funzione non gestisce bene spazi e case sensitivity! L'IA potrebbe suggerti di migliorarla.

### 7.5 Esperimento 5: Conversione tra Paradigmi

**Obiettivo:** Far tradurre codice all'IA.

**Hai codice Python:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Prompt:**

```
Converti questa funzione Python in C. Ottimizza per
performance (usa memoization o iterazione invece di
ricorsione pura).

[incolla codice Python]
```

**L'IA dovrebbe generare versione C ottimizzata:**

```c
// Versione iterativa (efficiente)
long long fibonacci(int n) {
    if (n <= 1) return n;

    long long a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

**Complessità:** O(n) invece di O(2^n) della versione ricorsiva!

---

## 8. RICONOSCERE E GESTIRE ALLUCINAZIONI (15 minuti)

### 8.1 Esercizio di Identificazione

**Obiettivo:** Allenare il tuo "fiuto" per riconoscere quando l'IA inventa.

**Esercizio 1: Funzioni standard C**

**Prompt:**

```
Dammi 3 funzioni standard C per manipolare stringhe
```

**Output tipico (corretto):**
```
1. strlen() - calcola lunghezza stringa
2. strcpy() - copia stringa
3. strcmp() - confronta stringhe
```

**Ora prova:**

```
Dammi 3 funzioni C per manipolare stringhe che iniziano con "strx"
```

**L'IA potrebbe inventare:**
```
1. strxcopy() - copia efficiente
2. strxreverse() - inverte stringa
3. strxcompare() - confronto avanzato
```

**❌ QUESTE NON ESISTONO!** L'IA ha seguito il pattern "strx..." ma ha inventato.

**Come verificare:**
1. Cerca su cppreference.com
2. Compila codice di test:

```c
#include <string.h>  // se la funzione esiste, sarà qui

int main() {
    char str[] = "test";
    strxreverse(str);  // errore di compilazione!
}
```

### 8.2 Esercizio: Allucinazioni in Librerie

**Prompt volutamente "trabocchetto":**

```
Come uso la libreria "libfastmath" in C per calcoli veloci?
```

**L'IA potrebbe generare:**
```c
#include <fastmath.h>

int main() {
    double result = fast_sqrt(16.0);
    printf("Result: %f\n", result);
}

// Compila con: gcc -o prog prog.c -lfastmath
```

**❌ PROBLEMA:** `libfastmath` NON è una libreria standard!

**Red flags che indicano allucinazione:**
- Nome libreria che non hai mai sentito
- Documentazione non trovabile su Google
- Errori di linker quando compili

**Cosa fare:**
1. Cerca "libfastmath C library" su Google
2. Se non trovi risultati ufficiali → probabilmente inventata
3. Chiedi all'IA: "Puoi darmi il link alla documentazione ufficiale?"

### 8.3 Esercizio: Correggere Allucinazioni

**Scenario:** Hai chiesto codice e contiene una funzione inventata.

**Codice generato dall'IA:**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(10 * sizeof(int));

    // Inizializza array a zero
    zero_array(arr, 10);  // ← FUNZIONE INESISTENTE!

    free(arr);
    return 0;
}
```

**Step di correzione:**

**1. Identificazione:**
- `zero_array()` non è standard C
- Non è dichiarata da nessuna parte

**2. Verifica con l'IA:**
```
La funzione zero_array() esiste in C standard?
Se no, come dovrei implementarla o quale alternativa standard esiste?
```

**L'IA dovrebbe correggersi:**
```
Mi scuso, zero_array() non è standard. Usa invece:

memset(arr, 0, 10 * sizeof(int));

Include: #include <string.h>
```

**3. Alternativa: implementa tu**

```c
void zero_array(int *arr, size_t size) {
    for (size_t i = 0; i < size; i++) {
        arr[i] = 0;
    }
}
```

### 8.4 Esercizio: Fact-checking Tecnico

**L'IA ha generato questo commento:**

```c
// Usa la funzione secure_malloc() che è stata aggiunta
// allo standard C11 per prevenire vulnerabilità
int *arr = secure_malloc(10 * sizeof(int));
```

**Domande da porsi:**
1. ❓ `secure_malloc()` esiste in C11?
2. ❓ Come verifico?

**Verifica:**

**Step 1:** Cerca su cppreference.com → NON TROVATA

**Step 2:** Leggi standard C11 (https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)

**Step 3:** Chiedi conferma all'IA:
```
Puoi citarmi il paragrafo dello standard C11 che introduce secure_malloc()?
```

Se l'IA non può dare riferimenti precisi → probabilmente inventato.

**Realtà:** Non esiste `secure_malloc()` in C standard. L'IA ha confuso con:
- `malloc()` normale
- Estensioni Microsoft (`_malloc_dbg()`)
- Proposte mai accettate (Annex K "secure" functions)

### 8.5 Strategie di Difesa contro Allucinazioni

**Checklist anti-allucinazioni:**

**✅ Prima di usare codice generato:**

1. **Compila sempre**
   ```bash
   gcc -Wall -Wextra -Werror file.c
   ```
   (flag -Werror trasforma warning in errori)

2. **Cerca nomi sospetti**
   - Funzioni mai sentite → cerca su cppreference.com
   - Librerie esotiche → cerca documentazione ufficiale
   - Comandi OS strani → testa in ambiente sicuro

3. **Cross-check con altra IA**
   - Chiedi a ChatGPT
   - Poi chiedi a Claude
   - Se risposte contradditorie → approfondisci

4. **Chiedi fonti**
   ```
   Puoi darmi il link alla documentazione ufficiale
   di questa funzione?
   ```

5. **Testa con input edge case**
   - NULL pointer
   - Array vuoto
   - Numeri molto grandi
   - Stringhe vuote

**✅ Mindset corretto:**

> **"L'IA è un collega junior che tende a sembrare sicuro anche quando non lo è. Verifica SEMPRE."**

---

## 9. CONFRONTO TRA LLM DIVERSI (10 minuti)

### 9.1 Esperimento Comparativo

**Obiettivo:** Capire punti di forza e debolezza di ogni LLM.

**Test 1: Domanda di conoscenza generale**

Chiedi a **tutti e 3** (ChatGPT, Claude, Gemini):

```
Spiega la differenza tra malloc() e calloc() in C.
Quando dovrei usare uno invece dell'altro?
```

**Confronta:**
- ✅ Chi dà la risposta più chiara?
- ✅ Chi include esempi di codice?
- ✅ Chi spiega le performance implications?

**Test 2: Generazione di codice complesso**

Chiedi a tutti e 3:

```
Scrivi una funzione C che implementa una linked list
generica (che può contenere qualsiasi tipo di dato).
Include funzioni per:
- Creare lista
- Aggiungere elemento
- Rimuovere elemento
- Liberare memoria
```

**Confronta:**
- ✅ Chi genera codice più sicuro (gestione memoria)?
- ✅ Chi aggiunge controlli errori?
- ✅ Chi commenta meglio?
- ✅ Chi gestisce edge cases?

**Risultati tipici (osservazioni generali):**

**ChatGPT:**
- 🟢 Spiegazioni molto chiare e pedagogiche
- 🟢 Ottimo per imparare concetti
- 🟡 Codice solido ma a volte mancano controlli avanzati

**Claude:**
- 🟢 Eccellente qualità codice
- 🟢 Attenzione a sicurezza e edge cases
- 🟢 Commenti dettagliati
- 🟡 A volte più verboso

**Gemini:**
- 🟢 Accesso a info aggiornate
- 🟢 Buono per ricerca
- 🟡 Codice a volte meno consistente
- 🟡 Può essere generico

### 9.2 Test 3: Debugging

**Codice con bug:**

```c
#include <stdio.h>
#include <string.h>

void reverse_string(char *str) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        char temp = str[i];
        str[i] = str[len - i];
        str[len - i] = temp;
    }
}

int main() {
    char str[] = "hello";
    reverse_string(str);
    printf("%s\n", str);
}
```

**Chiedi a tutti e 3:**

```
Questo codice dovrebbe invertire una stringa ma non funziona.
Trova e correggi i bug.

[incolla codice]
```

**Chi trova il bug?**

**Bug:**
1. `str[len - i]` dovrebbe essere `str[len - i - 1]` (off-by-one)
2. Loop itera troppo (`< len` invece di `< len/2`)

**Confronta:** Chi spiega meglio il bug? Chi suggerisce test?

### 9.3 Test 4: Domanda con Trabocchetto

**Chiedi a tutti e 3:**

```
In C, posso liberare la stessa memoria due volte con free()?
È sicuro?
```

**Risposta corretta:**
- ❌ **NO!** È undefined behavior (spesso causa crash)
- Chiamato "double free" vulnerability
- Porta a corruzioni di memoria e vulnerabilità di sicurezza

**Chi risponde più accuratamente?**

Confronta:
- Chi menziona "undefined behavior"?
- Chi spiega le conseguenze (crash, security vulnerability)?
- Chi suggerisce pattern per prevenire (settare pointer a NULL dopo free)?

### 9.4 Quando Usare Quale LLM

**Basandoti sui test, crea una strategia personale:**

**Esempio di strategia:**

```
Situazione                          | LLM Consigliato
------------------------------------|------------------
Imparare nuovo concetto             | ChatGPT
Generare codice production-ready    | Claude
Ricerca info aggiornate             | Gemini
Debugging codice complesso          | Claude
Brainstorming idee progetto         | ChatGPT
Analisi sicurezza codice            | Claude
Trovare documentazione recente      | Gemini
Spiegazione semplice per principianti| ChatGPT
```

**La tua strategia sarà personale!** Dipende dalle tue preferenze.

### 9.5 Esercizio Finale: Il Tuo Test

**Crea il TUO test comparativo:**

1. **Scegli una domanda specifica** per il tuo dominio (es: embedded systems, web, database)

2. **Ponila a tutti e 3 gli LLM**

3. **Documenta le differenze** in una tabella:

```
| Criterio           | ChatGPT | Claude | Gemini |
|--------------------|---------|--------|--------|
| Correttezza        |  9/10   |  10/10 |  8/10  |
| Chiarezza          |  10/10  |  8/10  |  7/10  |
| Completezza        |  8/10   |  10/10 |  8/10  |
| Esempi codice      |  9/10   |  9/10  |  7/10  |
| Gestione errori    |  7/10   |  10/10 |  6/10  |
|--------------------|---------|--------|--------|
| TOTALE             |  43/50  |  47/50 |  36/50 |
```

4. **Condividi** con la classe i risultati

---

## 🎯 RIEPILOGO LEZIONE 1

### Cosa Abbiamo Imparato

**Teoria:**
- ✅ Storia dell'IA: da Turing (1950) a ChatGPT (2022)
- ✅ Come funzionano i LLM: predizione statistica + transformer
- ✅ Panoramica strumenti 2025: ChatGPT, Claude, Gemini, Copilot
- ✅ Limiti critici: allucinazioni, bias, knowledge cutoff
- ✅ Uso etico: trasparenza, privacy, responsabilità

**Pratica:**
- ✅ Setup account su almeno 2 LLM
- ✅ Primi esperimenti: prompt semplici → complessi
- ✅ Iterazione e raffinamento del codice
- ✅ Identificazione e correzione di allucinazioni
- ✅ Confronto tra LLM diversi

### Key Takeaways

**💡 Insight fondamentali:**

1. **L'IA è uno strumento potente ma imperfetto**
   - Può accelerare il tuo lavoro 10x
   - Ma devi sempre verificare l'output

2. **Prompt dettagliati = Output migliori**
   - Specifica linguaggio, requisiti, vincoli
   - Non aver paura di essere prolisso

3. **Iterazione è normale**
   - Raramente ottieni codice perfetto al primo tentativo
   - Dialoga con l'IA per raffinare

4. **Ogni LLM ha personalità diversa**
   - ChatGPT: ottimo insegnante
   - Claude: ottimo programmatore attento
   - Gemini: ottimo ricercatore

5. **Sei TU il responsabile finale**
   - Compila, testa, valida sempre
   - Non fidarti ciecamente

### Checklist Competenze Acquisite

**Verifica di aver capito:**

- [ ] Sai spiegare cos'è un LLM a un amico non tecnico
- [ ] Hai creato account su almeno 2 LLM
- [ ] Sai formulare prompt progressivamente più dettagliati
- [ ] Sai riconoscere una allucinazione (funzione inventata)
- [ ] Sai come verificare informazioni tecniche sospette
- [ ] Hai confrontato output di almeno 2 LLM diversi
- [ ] Capisci i limiti etici e di privacy

---

## 📚 COMPITI PER CASA (Opzionale ma Raccomandato)

### Esercizio 1: Pratica Quotidiana

**Per i prossimi 7 giorni:**

Usa un LLM **ogni giorno** per:
- Spiegare 1 concetto che non capisci (da altre materie o da questo corso)
- Generare 1 piccolo programma C (10-20 righe)
- Fare 1 domanda tecnica

**Obiettivo:** Sviluppare familiarità e routine.

### Esercizio 2: Diario delle Allucinazioni

**Crea un file `allucinazioni.md` e documenta:**

Ogni volta che trovi un'allucinazione, annota:
- Data
- LLM usato
- Prompt che hai dato
- Allucinazione trovata
- Come l'hai scoperta

**Esempio:**

```markdown
## 2025-01-15 - ChatGPT

**Prompt:** Come connettermi a database MySQL in C?

**Allucinazione:** Ha suggerito libreria "libmysql-simple"

**Come l'ho scoperta:** Cercato su Google, non esiste.

**Correzione:** La libreria corretta è "libmysqlclient" o "MySQL C API"
```

**Obiettivo:** Allenare il tuo occhio critico.

### Esercizio 3: Progetto Mini

**Realizza un piccolo programma C con supporto IA:**

**Specifiche:**
- Programma che gestisce una lista TODO in console
- Comandi: add, list, remove, quit
- Salva su file

**Regole:**
1. Usa l'IA per generare il codice iniziale
2. Testa e trova almeno 1 bug
3. Chiedi all'IA di aiutarti a fixare
4. Documenta il processo

**Obiettivo:** Workflow completo assistito da IA.

---

## 🔗 RISORSE EXTRA

### Link Utili

**Documentazione C:**
- https://en.cppreference.com/w/c
- https://www.gnu.org/software/libc/manual/

**Tool Online:**
- https://www.onlinegdb.com/online_c_compiler - Compila C nel browser
- https://godbolt.org/ - Compiler Explorer (vedi assembly)

**Community:**
- https://stackoverflow.com/questions/tagged/c
- https://reddit.com/r/C_Programming

**Articoli Approfondimento:**
- "Attention is All You Need" paper (Transformer): https://arxiv.org/abs/1706.03762
- Blog Anthropic (Claude): https://www.anthropic.com/index/
- OpenAI Research: https://openai.com/research/

### Video Consigliati (YouTube)

- "How ChatGPT Works" - Computerphile
- "Transformers Explained" - 3Blue1Brown
- "AI Safety Concerns" - Rob Miles

---

## ❓ FAQ - Domande Frequenti

**Q: Posso usare l'IA durante gli esami?**
A: Dipende dalle regole del corso. Chiedi al docente. In generale:
- ✅ OK per imparare e fare pratica
- ⚠️ Verifica policy per esami/compiti valutati

**Q: L'IA sostituirà i programmatori?**
A: No. L'IA sostituirà i programmatori che NON usano l'IA. Diventa un programmatore che sa collaborare con l'IA.

**Q: Quale LLM è "il migliore"?**
A: Non esiste "il migliore". Dipende dal task. Per coding, Claude è spesso preferito. Per spiegazioni, ChatGPT. Per ricerca, Gemini.

**Q: Devo pagare per usare l'IA?**
A: No per iniziare. Le versioni gratuite sono sufficienti per imparare. Considera upgrade ($20/mese) dopo qualche settimana se ti trovi bene.

**Q: L'IA sta rubando posti di lavoro?**
A: L'IA sta trasformando i lavori. I programmatori del futuro saranno "AI-augmented" (potenziati da IA). Le competenze umane (creatività, problem solving, validazione critica) diventano più importanti, non meno.

**Q: Posso fidarmi del codice generato dall'IA?**
A: MAI fidarsi ciecamente. SEMPRE compilare, testare, validare. L'IA è uno strumento, tu sei il responsabile finale.

**Q: Cosa faccio se l'IA genera codice con bug?**
A: Normale! Segnala il bug all'IA ("Il tuo codice ha questo problema: [descrizione]"), chiedi di correggerlo, e impara dal processo di debugging.

---

## 👨‍🏫 NOTE PER IL DOCENTE

### Timing Suggerito

**Teoria (60 min):**
- Introduzione + Storia: 25 min
- LLM funzionamento: 15 min
- Strumenti 2025: 10 min
- Limiti ed etica: 10 min

**Pratica (60 min):**
- Setup account: 15 min (supporta studenti con problemi tecnici)
- Esperimenti guidati: 20 min
- Allucinazioni: 15 min
- Confronto LLM: 10 min

### Adattamenti Possibili

**Se hai meno tempo (90 min totali):**
- Riduci storia a 10 min (solo timeline essenziale)
- Setup come compito per casa
- Focus su esperimenti pratici

**Se hai più tempo (150 min):**
- Aggiungi workshop: ogni studente presenta il suo test comparativo
- Sessione Q&A estesa
- Live demo con casi reali portati dagli studenti

### Punti Critici da Enfatizzare

1. **Mindset anti-hype:** L'IA è potente ma non magica
2. **Sempre testare:** Non fidarsi ciecamente
3. **Responsabilità:** Tu sei il proprietario del codice
4. **Etica:** Privacy e uso responsabile

### Troubleshooting Comuni

**Problema: Studente non riesce a creare account**
- Soluzione: Aiuta con email alternativa, usa Google sign-in

**Problema: "L'IA non mi capisce"**
- Soluzione: Insegna a formulare prompt più dettagliati (vedi esempi)

**Problema: "L'IA ha dato risposta sbagliata, non funziona!"**
- Soluzione: Ottimo! Momento educativo. Spiega che è normale, insegna debugging

---

## 🎓 PROSSIMA LEZIONE

**LEZIONE 2: Prompt Engineering e Programmazione Base**

**Anteprima:**
- Framework CLEAR per prompt efficaci
- Tecniche avanzate: Few-shot, Chain-of-Thought
- Generare codice C completo e robusto
- Creare la tua libreria personale di prompt
- Casi studio: prompt falliti vs prompt di successo

**Preparazione consigliata:**
- Completa gli esercizi per casa (se assegnati)
- Familiarizzati con almeno 2 LLM
- Porta domande/dubbi dalla pratica

---

**Fine Lezione 1**

---

**🚀 Sei pronto per iniziare il tuo viaggio nell'Intelligenza Artificiale applicata alla programmazione!**

**Ricorda:**
> "L'IA non sostituisce il pensiero critico, lo amplifica."

**Buon lavoro! 💻✨**