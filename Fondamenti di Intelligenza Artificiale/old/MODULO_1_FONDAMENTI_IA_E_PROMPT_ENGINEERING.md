# 📘 MODULO 1
# Fondamenti di Intelligenza Artificiale e Prompt Engineering
## Corso ITS - Intelligenza Artificiale e Programmazione Assistita 2025
### Durata: 3 ore | Livello: Base-Intermedio

---

## 📑 Indice del Modulo

1. [Introduzione e Obiettivi](#1-introduzione-e-obiettivi)
2. [Fondamenti di Intelligenza Artificiale](#2-fondamenti-di-intelligenza-artificiale)
3. [Large Language Models (LLM)](#3-large-language-models-llm)
4. [Limiti, Rischi e Uso Responsabile](#4-limiti-rischi-e-uso-responsabile)
5. [Prompt Engineering Professionale](#5-prompt-engineering-professionale)
6. [Framework e Metodologie](#6-framework-e-metodologie)
7. [Applicazioni in Ambito ITS](#7-applicazioni-in-ambito-its)
8. [Esercitazioni Pratiche](#8-esercitazioni-pratiche)

---

## 1. Introduzione e Obiettivi

### 1.1 Benvenuti al Corso 2025

Benvenuti! Questo corso vi insegnerà a utilizzare l'**Intelligenza Artificiale come strumento professionale** per la programmazione, con focus particolare su sistemi embedded e applicazioni ITS (Istituto Tecnico Superiore).

**Perché questo corso è importante per voi?**

Nel 2025, l'IA non è più fantascienza o una tecnologia per pochi esperti. È diventata uno **strumento di lavoro quotidiano** per programmatori, ingegneri e tecnici. Immaginate di avere un collega esperto sempre disponibile 24/7, che può:
- Scrivere codice al vostro posto
- Spiegare concetti complessi in modo semplice
- Trovare bug nel vostro codice
- Suggerire soluzioni a problemi tecnici

Ma attenzione: come ogni strumento potente, l'IA va usata **con intelligenza**. Non è magia, ha limiti precisi, e può sbagliare. Questo corso vi insegnerà **quando, come e perché** usare l'IA, e soprattutto **come riconoscere quando sbaglia**.

**Novità 2025:**
- **Claude 3.5 Sonnet**: il migliore per seguire istruzioni precise
- **GPT-4 Turbo**: eccellente per codice e ragionamento complesso
- **Gemini 1.5 Pro**: può "leggere" documenti lunghissimi (2 milioni di parole!)
- **GitHub Copilot**: scrive codice mentre digitate nell'IDE
- **TinyML**: intelligenza artificiale che gira su Arduino!

### 1.2 Obiettivi di Apprendimento

Al termine di questo modulo (3 ore) sarai in grado di:

✅ **Comprendere** cos'è l'IA e come funzionano gli LLM moderni
   → Saprai spiegare a un amico cosa fa ChatGPT "sotto il cofano"

✅ **Riconoscere** limiti, bias e allucinazioni
   → Non ti farai ingannare quando l'IA inventa fatti falsi

✅ **Formulare** prompt tecnici efficaci
   → Otterrai codice utilizzabile al primo colpo invece di perdere ore

✅ **Applicare** framework professionali (CLEAR, Chain-of-Thought)
   → Userai tecniche da professionista, non da principiante

✅ **Valutare criticamente** output generati da IA
   → Saprai dire se un codice è buono o pericoloso

✅ **Integrare** IA nel workflow di sviluppo
   → L'IA diventerà parte naturale del tuo lavoro

### 1.3 Strumenti 2025

**Cosa vi serve per iniziare?**

Niente di costoso! La maggior parte degli strumenti sono gratuiti o gratis per studenti.

**LLM Raccomandati (almeno 1 obbligatorio):**

```
GRATUITI AL 100%:
┌────────────────────────────────────────┐
│ ChatGPT 3.5 (OpenAI)                   │
│ ├─ Gratis forever                      │
│ ├─ Molto buono per iniziare            │
│ └─ Limite: qualità inferiore a GPT-4   │
│                                        │
│ Claude 3.5 Sonnet (Anthropic)          │
│ ├─ Gratis con limiti                   │
│ ├─ Eccellente per istruzioni precise   │
│ └─ Limite: ~50 messaggi/giorno free    │
│                                        │
│ Gemini 1.5 (Google)                    │
│ ├─ Gratis con account Google           │
│ ├─ Context window ENORME               │
│ └─ Limite: più lento dei concorrenti   │
└────────────────────────────────────────┘

STUDENTI (GRATIS CON VERIFICA):
┌────────────────────────────────────────┐
│ GitHub Copilot                         │
│ ├─ Gratis con GitHub Student Pack      │
│ ├─ Si integra nell'IDE (VSCode, etc)   │
│ ├─ Scrive codice mentre digiti         │
│ └─ FORTEMENTE RACCOMANDATO              │
│                                        │
│ ChatGPT Plus                           │
│ ├─ Normalmente $20/mese                │
│ ├─ Gratis per studenti verificati      │
│ └─ Accesso a GPT-4 (migliore qualità)  │
└────────────────────────────────────────┘

PRO (A PAGAMENTO - OPZIONALE):
- ChatGPT Plus: $20/mese
- Claude Pro: $20/mese
- Cursor IDE: $20/mese (editor con IA integrata)
```

**Come ottenere GitHub Student Pack (IMPORTANTE!):**

Il GitHub Student Pack è un regalo incredibile per studenti: oltre 100 tool professionali gratis, incluso GitHub Copilot che normalmente costa $10/mese!

```
PASSI:
1. Vai su: https://education.github.com/pack
2. Clicca "Get Student Benefits"
3. Verifica identità studente con:
   ├─ Email istituzionale ITS (@its...)
   ├─ Foto documento studente
   └─ Prova iscrizione
4. Attendi approvazione (1-7 giorni)
5. Attiva Copilot su VSCode

COSA OTTIENI:
✓ GitHub Copilot (valore $120/anno)
✓ Domini .me gratis
✓ Cloud credits AWS/Azure
✓ + altri 100+ tool professionali
```

**Configurazione Ambiente Base:**

```bash
# 1. EDITOR RACCOMANDATO
Visual Studio Code (gratuito)
→ https://code.visualstudio.com/

# 2. ESTENSIONI VSCODE ESSENZIALI
- GitHub Copilot (se hai Student Pack)
- C/C++ (Microsoft)
- Arduino (Microsoft)
- ChatGPT (extension ufficiale)

# 3. ACCOUNT DA CREARE
□ Account OpenAI (ChatGPT)
□ Account Anthropic (Claude)
□ Account Google (Gemini)
□ GitHub account (per Student Pack)
```

---

## 2. Fondamenti di Intelligenza Artificiale

### 2.1 Cos'è l'IA nel 2025

**Definizione Semplice:**

> **Intelligenza Artificiale**: programmi che imparano a fare cose intelligenti guardando esempi, invece di seguire istruzioni scritte da programmatori.

**Pensate alla differenza:**

**Programmazione Tradizionale:**
```python
# Il programmatore scrive OGNI regola
def è_spam(email):
    if "viagra" in email:
        return True
    if "gratis" in email and "vinci" in email:
        return True
    # ...devi scrivere 1000 regole...
    return False
```
→ Serve il programmatore per ogni nuova regola
→ Non si adatta a nuovi trucchi degli spammer

**Intelligenza Artificiale:**
```python
# L'IA impara DA SOLA dai dati
modello = train_spam_detector(
    esempi_spam=10000,     # email spam
    esempi_normali=10000   # email normali
)

# Ora riconosce spam MAI VISTO PRIMA
print(modello.è_spam("...nuova email..."))
```
→ Impara pattern complessi dai dati
→ Si adatta a nuovi tipi di spam

**Evoluzione Storica (Timeline per capire dove siamo):**

```
1950s: NASCITA
├─ Test di Turing (1950)
├─ "Può una macchina pensare?"
└─ Solo teoria, nessun risultato pratico

1980s-1990s: INVERNO IA
├─ Computer troppo lenti
├─ Dati insufficienti
└─ Poche applicazioni reali

2010s: RINASCITA
├─ 2012: Deep Learning funziona (ImageNet)
├─ GPU potenti + Big Data
├─ Google, Facebook investono miliardi
└─ Assistenti vocali (Siri, Alexa)

2020s: RIVOLUZIONE
├─ 2022: ChatGPT (175 miliardi parametri!)
│        → 100 milioni utenti in 2 mesi
├─ 2023: GPT-4 (multimodale: testo+immagini)
│        → Supera esami professionali
├─ 2024: Claude 3.5, Gemini 1.5 Pro
│        → Context window 2 milioni token
└─ 2025: IA in OGNI strumento
         → IDE, browser, sistemi operativi
```

**Perché PROPRIO ORA è il momento della rivoluzione?**

Tre fattori si sono allineati:

1. **DATI**: Internet ha creato oceani di testo/immagini/video
2. **COMPUTING**: GPU moderne 1000x più potenti di 10 anni fa
3. **ALGORITMI**: Transformer (2017) ha sbloccato tutto

È come avere benzina (dati) + motore (GPU) + chiave per accenderlo (algoritmi).

### 2.2 Categorie IA Essenziali

L'IA è un termine generico. Sotto questo ombrello ci sono TANTI tipi diversi di tecnologie. Ecco le principali che dovete conoscere:

```
┌─────────────────────────────────────────┐
│    CATEGORIE IA (Focus 2025)            │
├─────────────────────────────────────────┤
│                                         │
│ 1. MACHINE LEARNING (ML)                │
│    Apprendimento da dati con algoritmi  │
│    statistici                           │
│    │                                    │
│    ├─ Supervised Learning               │
│    │  (impara da esempi etichettati)    │
│    │  Es: Spam detector, diagnosi       │
│    │                                    │
│    ├─ Unsupervised Learning             │
│    │  (trova pattern da solo)           │
│    │  Es: Clustering clienti            │
│    │                                    │
│    └─ Reinforcement Learning            │
│       (impara per tentativi/errori)     │
│       Es: AlphaGo, robot                │
│                                         │
│ 2. DEEP LEARNING                        │
│    Reti neurali "profonde" (tanti       │
│    layer) che imparano automaticamente  │
│    │                                    │
│    ├─ Computer Vision                   │
│    │  (riconoscimento immagini)         │
│    │  Es: Face ID, auto autonome        │
│    │                                    │
│    ├─ NLP (Natural Language)            │
│    │  (comprensione linguaggio)         │
│    │  Es: ChatGPT, traduttori           │
│    │                                    │
│    └─ Speech Recognition                │
│       (riconoscimento vocale)           │
│       Es: Alexa, Siri                   │
│                                         │
│ 3. IA GENERATIVA ⭐ (FOCUS 2025)       │
│    IA che CREA contenuti nuovi          │
│    │                                    │
│    ├─ LLM (Large Language Models)       │
│    │  Generano TESTO e CODICE           │
│    │  Es: ChatGPT, Claude, Gemini       │
│    │  → QUESTO È IL NOSTRO FOCUS!       │
│    │                                    │
│    ├─ Image Generation                  │
│    │  Generano IMMAGINI                 │
│    │  Es: DALL-E 3, Midjourney, Stable  │
│    │                                    │
│    └─ Multi-Modal                       │
│       Capiscono/generano testo+immagini │
│       Es: GPT-4V, Gemini 1.5           │
│                                         │
│ 4. EDGE AI / TinyML ⭐                 │
│    IA che gira su microcontrollori!     │
│    Es: Keyword spotting su Arduino      │
│                                         │
└─────────────────────────────────────────┘
```

**Spiegazione Categorie con Esempi Pratici:**

#### **1. Machine Learning (ML)**

Il ML è la base di tutto. L'idea: invece di programmare regole, dai esempi e l'algoritmo impara le regole da solo.

**Esempio Supervised Learning:**
```
PROBLEMA: Riconoscere se un'email è spam

DATI TRAINING:
Email 1: "Vinci iPhone gratis!" → SPAM ✓
Email 2: "Riunione domani ore 10" → OK ✓
Email 3: "Viagra sconto 90%" → SPAM ✓
...10.000 esempi...

ALGORITMO IMPARA:
- Parole spam: "gratis", "vinci", "viagra"
- Pattern spam: molti CAPS, link strani
- Mittenti spam: domini sospetti

RISULTATO:
Input: nuova email mai vista
Output: SPAM (85% sicuro) o OK (98% sicuro)
```

**Esempio Unsupervised Learning:**
```
PROBLEMA: Raggruppa clienti simili

DATI:
Cliente A: Compra [pasta, pomodori, basilico]
Cliente B: Compra [birra, patatine, pizza]
Cliente C: Compra [pasta, olio, aglio]
...

ALGORITMO TROVA GRUPPI DA SOLO:
Cluster 1: "Cucinatori italiani" (A, C)
Cluster 2: "Party people" (B)

USO: Marketing mirato per ogni cluster
```

#### **2. Deep Learning**

Deep Learning = Machine Learning con reti neurali molto "profonde" (tanti layer). Può imparare concetti sempre più astratti.

**Analogia:**
```
Layer 1: Rileva linee/bordi in immagine
   ↓
Layer 2: Combina linee in forme (occhi, naso)
   ↓
Layer 3: Combina forme in oggetti (volto)
   ↓
Layer 4: Riconosce CHI è la persona
```

**Applicazione ITS:**
```
COMPUTER VISION su produzione:
Camera → Deep Learning Model → Difetto rilevato!

Es: Controllo qualità PCB (circuit board)
- Input: Foto PCB
- Model: CNN (Convolutional Neural Network)
- Output: "Saldatura difettosa sulla resistenza R7"
- Accuratezza: >99.5%
```

#### **3. IA Generativa (FOCUS CORSO)**

Questa è la rivoluzione 2022-2025. IA che non solo riconosce, ma **CREA** contenuti nuovi.

**Large Language Models (LLM):**

Immaginate un modello che ha "letto" quasi tutto internet:
- Wikipedia completa
- Milioni di libri
- Codice GitHub (miliardi di righe)
- Forum, blog, paper scientifici

Ora può:
- Rispondere a domande
- Scrivere articoli
- **Generare codice** ← QUESTO CI INTERESSA!
- Tradurre linguaggi
- Riassumere documenti

**Come è possibile?**

Il modello ha imparato **pattern statistici** del linguaggio. Non "capisce" veramente, ma è bravissimo a prevedere "quale parola viene dopo".

```
Input: "La capitale d'Italia è"
Model pensa:
  "Roma" → 92% probabilità ✓
  "Milano" → 3%
  "Parigi" → 0.001%
Output: "Roma"
```

Ma con miliardi di parametri e addestramento sofisticato, questi pattern diventano sorprendentemente intelligenti!

#### **4. Edge AI / TinyML**

Questa è la frontiera per embedded! IA che gira su microcontrollori con pochi KB di RAM.

**Caso d'uso reale:**
```
KEYWORD SPOTTING su Arduino Nano 33 BLE:

Hardware:
- MCU: ARM Cortex-M4 (64 MHz)
- RAM: 256 KB
- Flash: 1 MB

Model:
- Tipo: CNN
- Dimensione: 30 KB (!)
- Accuratezza: 94%

Funzionalità:
Microfono → Model → Riconosce "Arduino"
                  → Attiva azione

Consumi:
- Idle: 50 µA
- Active: 8 mA
- Batteria dura MESI
```

**Perché è importante?**
- Privacy: dati restano locali
- Latenza: risposta istantanea
- Affidabilità: no dipendenza cloud
- Costo: no connettività necessaria

### 2.3 IA vs Algoritmi Tradizionali

**Quando usare cosa?**

Questa è una domanda FONDAMENTALE per ingegneri. Non tutto va risolto con IA!

| Scenario | Algoritmo Classico | IA/ML | Vincitore |
|----------|-------------------|-------|-----------|
| **Calcolare IVA su vendita** | `prezzo * 0.22` | Rete neurale addestrata su esempi | ❌ Algoritmo! (IA è overkill) |
| **Classificare email spam** | Regole if/then manuali | Modello ML addestrato | ✅ IA! (troppi pattern) |
| **Riconoscimento vocale** | Pattern matching acustico | Deep Learning CNN/RNN | ✅ IA! (impossibile altrimenti) |
| **PID controller** | Formula PID classica | Reinforcement Learning | ⚖️ Dipende! (PID ok per casi semplici) |
| **Generare codice da descrizione** | Template + regex | LLM (GPT-4) | ✅ IA! (unica opzione) |
| **Ordinare array** | Quicksort | Neural Sort | ❌ Algoritmo! (più veloce, deterministico) |
| **Predire guasto motore** | Soglie fisse | ML + sensori | ✅ IA! (pattern complessi) |

**Regole Pratiche 2025:**

```
USA ALGORITMI CLASSICI quando:
✓ Le regole sono chiare e stabili
  Es: calcolo IVA non cambierà domani

✓ Precisione matematica è CRITICA
  Es: sistemi safety-critical (avionica)

✓ Spiegabilità è obbligatoria
  Es: "perché il controllo ha fatto X?"

✓ Dati insufficienti
  Es: 10 esempi non bastano per ML

✓ Risorse limitate
  Es: Arduino Uno (2KB RAM!)

USA IA/ML quando:
✓ Pattern troppo complessi per regole
  Es: "questa immagine contiene un gatto?"

✓ Hai TANTI dati
  Es: 10.000+ esempi etichettati

✓ Task creativi/generativi
  Es: scrivere codice, testi, immagini

✓ Ambiente cambia nel tempo
  Es: nuovi tipi di spam ogni giorno

✓ Approssimazione accettabile
  Es: 95% accuratezza è ok
```

**Esempio Reale ITS: Sistema Rilevamento Difetti**

```
SCENARIO: Controllo qualità saldature PCB

APPROCCIO CLASSICO:
```c
bool saldatura_ok(Image img, Point p) {
    // Controlla dimensione
    if (area(p) < MIN_AREA) return false;
    if (area(p) > MAX_AREA) return false;

    // Controlla colore
    if (brightness(p) < MIN_BRIGHT) return false;

    // Controlla forma
    if (circolarità(p) < 0.8) return false;

    return true;
}
```
**Problemi:**
- Devi definire TUTTE le regole manualmente
- Non funziona su nuovi tipi di difetti
- Falsi positivi/negativi alti

**APPROCCIO IA:**
```python
# Training
model = train_cnn(
    immagini_ok = 5000,
    immagini_difetto = 5000
)

# Inference
difetto = model.predict(nuova_immagine)
# → 98.2% accuratezza!
```
**Vantaggi:**
- Impara automaticamente i pattern
- Si adatta a nuovi difetti con re-training
- Accuratezza superiore

**Conclusione per questo caso: IA vince!**

---

## 3. Large Language Models (LLM)

### 3.1 Cosa Sono gli LLM

Gli **LLM (Large Language Models)** sono il cuore di ChatGPT, Claude, e Gemini. Sono quello che useremo per programmare con l'IA.

**Definizione Semplice:**

> **LLM**: Un programma di intelligenza artificiale addestrato su MILIARDI di pagine di testo da internet, libri e codice. Può capire cosa scrivi e generare risposte sensate, incluso codice funzionante.

**Ma come funziona veramente?**

Pensate a un gioco dove dovete indovinare la parola successiva:

```
"Il gatto dorme sul ___"

Voi probabilmente direste:
- "divano" (molto probabile)
- "letto" (probabile)
- "tetto" (possibile)
- "aeroplano" (wtf? no!)
```

Un LLM fa la STESSA cosa, ma:
1. Ha visto MILIARDI di frasi simili
2. Ha imparato pattern statistici
3. Può farlo per QUALSIASI contesto

**LLM Principali 2025 (Comparison):**

```
┌────────────────────────────────────────────────────────┐
│ GPT-4 Turbo (OpenAI)                                   │
├────────────────────────────────────────────────────────┤
│ Parametri: ~1.7 trilioni (1,700,000,000,000!)         │
│ Context: 128,000 token (~100k parole, ~400 pagine)    │
│ Costo: $0.01 per 1k token input                       │
│                                                        │
│ ✅ PUNTI DI FORZA:                                     │
│   - Eccellente per codice                             │
│   - Ragionamento matematico                           │
│   - Multimodale (vede immagini!)                      │
│   - Function calling preciso                          │
│                                                        │
│ ❌ PUNTI DEBOLI:                                       │
│   - Più costoso dei concorrenti                       │
│   - A volte troppo verboso                            │
│   - Censura eccessiva su alcuni topic                 │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ Claude 3.5 Sonnet (Anthropic)                          │
├────────────────────────────────────────────────────────┤
│ Parametri: Non dichiarati (segreto!)                  │
│ Context: 200,000 token (~150k parole)                 │
│ Costo: $0.003 per 1k token (3x cheaper!)              │
│                                                        │
│ ✅ PUNTI DI FORZA:                                     │
│   - MIGLIORE per seguire istruzioni                   │
│   - Analisi codice accurata                           │
│   - Meno allucinazioni di GPT                         │
│   - Stile di scrittura naturale                       │
│                                                        │
│ ❌ PUNTI DEBOLI:                                       │
│   - Meno bravo su matematica complessa                │
│   - Meno conosciuto = meno esempi online              │
│   - Rate limits più stretti (free tier)               │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ Gemini 1.5 Pro (Google)                                │
├────────────────────────────────────────────────────────┤
│ Parametri: Non dichiarati                             │
│ Context: 2,000,000 token (!!!) = ~1 milione parole!   │
│ Costo: $0.00125 per 1k token (cheapest!)              │
│                                                        │
│ ✅ PUNTI DI FORZA:                                     │
│   - Context ENORME (può leggere interi libri)         │
│   - Gratis con limiti generosi                        │
│   - Multimodale avanzato                              │
│   - Integrazione Google Workspace                     │
│                                                        │
│ ❌ PUNTI DEBOLI:                                       │
│   - Più lento dei concorrenti                         │
│   - Qualità codice inferiore a GPT-4                  │
│   - Meno adatto a task specifici                      │
└────────────────────────────────────────────────────────┘
```

**Quale usare?**

```
Per CODICE COMPLESSO:
→ GPT-4 Turbo
  Esempio: "Implementa Red-Black Tree in C"

Per SEGUIRE ISTRUZIONI PRECISE:
→ Claude 3.5 Sonnet
  Esempio: "Genera sketch Arduino con ESATTAMENTE
            questi 15 requisiti..."

Per ANALIZZARE DOCUMENTI LUNGHI:
→ Gemini 1.5 Pro
  Esempio: "Leggi questo datasheet 500 pagine e
            trova i pin per I2C"

Per IMPARARE/SPERIMENTARE GRATIS:
→ ChatGPT 3.5 o Claude Free
  Funzionano benissimo per il 90% dei casi!
```

### 3.2 Come Funzionano (Spiegazione Semplificata)

**Il Viaggio di un Prompt (Step-by-Step):**

Quando scrivi "Scrivi funzione C per sommare array" e premi invio, cosa succede?

```
STEP 1: TOKENIZZAZIONE
──────────────────────────────────────────
Il tuo testo viene spezzato in "token"
(pezzi di parole)

Input: "Scrivi funzione C"
↓
Token: ["Scr", "ivi", " funzione", " C"]

Perché non parole intere?
→ Gestisce meglio parole nuove/rare
→ Funziona su TUTTE le lingue
→ Più efficiente per il modello

Un token ≈ 4 caratteri in italiano
"Ciao come stai?" = ~4 token
```

```
STEP 2: EMBEDDING
──────────────────────────────────────────
Ogni token → Vettore di numeri
(rappresentazione matematica)

"Scrivi" → [0.2, -0.5, 0.8, ..., 0.3]
           (4096 numeri!)

Cosa rappresentano questi numeri?
→ SIGNIFICATO SEMANTICO

Token simili hanno vettori simili:
"Scrivi" ≈ "Genera" ≈ "Crea"
"C" ≈ "C++" ≈ "codice"

Questo permette al modello di "capire"
relazioni tra concetti!
```

```
STEP 3: ATTENTION MECHANISM
──────────────────────────────────────────
Il cuore del Transformer!

Il modello "presta attenzione" a token
rilevanti per predire il prossimo

Esempio:
Input: "Scrivi funzione C per invertire stringa"

Quando genera codice, presta attenzione a:
- "funzione" → genererà `tipo nome()`
- "C" → userà sintassi C, non Python
- "invertire" → algoritmo reverse
- "stringa" → tipo `char*`

È come sottolineare le parti importanti
di un testo mentre studi!
```

```
STEP 4: PREDIZIONE PROBABILISTICA
──────────────────────────────────────────
Il modello genera UN token alla volta
scegliendo il più probabile

Dopo "Scrivi funzione C per sommare array",
il modello calcola:

Prossimo token:
"void" → 45% prob
"int" → 40% prob
"\n" → 10% prob (inizia su nuova riga)
"float" → 4% prob
"class" → 0.001% (sbagliato, C non ha class!)

Sceglie: "int" (in questo caso)

Poi ripete:
"int" → Prossimo token:
"sum" → 30%
"add" → 25%
"array" → 20%
...
```

```
STEP 5: ITERAZIONE FINO A COMPLETAMENTO
──────────────────────────────────────────
Ripete step 4 finché:
- Genera token di STOP
- Raggiunge limite token
- Tu fermi generazione

Genera così 100, 1000, 10000 token...
e costruisce risposta completa!
```

**Esempio Concreto Completo:**

```
PROMPT:
"Scrivi funzione C che calcola fattoriale"

GENERAZIONE (semplificato):
Token 1: "int" (45% prob)
Token 2: " fattoriale" (52% prob)
Token 3: "(" (98% prob - deve aprire parentesi!)
Token 4: "int" (78% prob)
Token 5: " n" (65% prob - nome parametro comune)
Token 6: ")" (99% prob)
Token 7: " {" (99% prob)
Token 8: "\n" (95% prob - new line)
Token 9: "    if" (70% prob - case base ricorsione)
...continua...

RISULTATO:
int fattoriale(int n) {
    if (n <= 1) return 1;
    return n * fattoriale(n - 1);
}
```

**Ma come fa a "sapere" la formula del fattoriale?**

**Non "sa" nulla!** Ha solo visto MILIONI di esempi di codice durante training:

```
Training data (semplificato):
- Visto 10,000 implementazioni fattoriale su GitHub
- Visto spiegazioni su Wikipedia/StackOverflow
- Visto esami/esercizi di programmazione

Ha imparato il PATTERN:
"fattoriale" + "ricorsione" →
   if (n <= 1) return 1;
   return n * fattoriale(n-1);
```

È come uno studente che ha fatto 10,000 esercizi: non "capisce" matematicamente, ma ha visto il pattern così tante volte che lo riproduce perfettamente!

### 3.3 Capacità e Limiti

**✅ Cosa Fanno BENISSIMO**

#### **1. Generazione Codice**

```
ECCELLENTI PER:

✓ Funzioni standard (sorting, searching, etc)
✓ Boilerplate code (setup Arduino, init struct)
✓ Implementazione algoritmi noti
✓ Conversione tra linguaggi
✓ Wrapper per API

ESEMPIO REALE:
Prompt: "Implementa merge sort in C"
→ Genera implementazione corretta 95% volte
→ Spesso più pulita di quella di studente medio!
```

#### **2. Debugging**

```
✓ Spiega errori compilatore in linguaggio semplice
✓ Trova bug evidenti (null pointer, off-by-one)
✓ Suggerisce fix
✓ Propone test case che fallirebbero

ESEMPIO:
Input: "error: invalid conversion from 'const char*' to 'char*'"
→ LLM spiega: "Stai passando stringa costante a
   funzione che si aspetta puntatore modificabile.
   Soluzione: cambia parametro in const char*"
```

#### **3. Documentazione**

```
✓ Genera commenti Doxygen
✓ Scrive README.md professionali
✓ Crea docstring Python
✓ Spiega codice complesso

ESEMPIO:
Input: [funzione complessa senza commenti]
Prompt: "Aggiungi commenti Doxygen"
→ Output: documentazione completa, parametri, return, esempi
```

#### **4. Refactoring**

```
✓ Migliora naming variabili
✓ Estrae funzioni da codice duplicato
✓ Semplifica logica complessa
✓ Applica design pattern

ESEMPIO:
Input: codice con 500 righe in un'unica funzione
Prompt: "Refactora in funzioni più piccole"
→ Output: 10 funzioni ben nominate, ognuna <50 righe
```

#### **5. Learning Assistant**

```
✓ Spiega concetti in modo semplice
✓ Genera esercizi personalizzati
✓ Confronta approcci diversi
✓ Risponde a "perché?" infinite volte senza irritarsi!

ESEMPIO STUDENTE:
"Perché usare malloc invece di array fisso?"
→ Spiegazione con pro/cons, esempi, casi d'uso
"Ok ma quando DEVO usare malloc?"
→ Scenari specifici con codice
"E se malloc fallisce?"
→ Error handling patterns
[...puoi continuare all'infinito...]
```

**❌ Limiti CRITICI (IMPORTANTE!)**

#### **1. Allucinazioni**

```
PROBLEMA #1: Inventa fatti/funzioni inesistenti

ESEMPIO REALE (successo davvero!):
Prompt: "Copia stringa in C"
Output IA:
  char* copy = strdup(original);

PROBLEMA: strdup() NON è standard C!
→ Non compila su embedded
→ Non compila con -std=c99
→ Ma SEMBRA corretto!

COME DIFENDERSI:
✓ Compila sempre il codice
✓ Leggi documentazione ufficiale
✓ Se non conosci una funzione, cercala!
✓ Usa -Wall -Wextra -Wpedantic
```

#### **2. Knowledge Cutoff**

```
PROBLEMA #2: Dati limitati a data di training

GPT-4: Training fino aprile 2023
→ Non conosce librerie/tool usciti dopo
→ Non conosce nuove versioni Arduino
→ Non sa eventi recenti

ESEMPIO:
"Usa nuova libreria XYZ del 2024"
→ "Non conosco questa libreria"
→ Potrebbe inventare API inesistente!

SOLUZIONE:
✓ Fornisci documentazione nel prompt
✓ Specifica versioni esatte
✓ Verifica online esistenza librerie
```

#### **3. No Vera Comprensione**

```
PROBLEMA #3: Pattern matching, non ragionamento

L'IA non "capisce" cosa fa il codice.
Riproduce pattern visti, come pappagallo intelligente.

ESEMPIO PROBLEMA:
Prompt: "Scrivi funzione che trova numero primo
         più grande di N"

Potrebbe generare:
bool isPrime(int n) { ... }  // ✓ corretto
int nextPrime(int n) {
    for (int i = n+1; ; i++) {
        if (isPrime(i)) return i;
    }
}
// ❌ LOOP INFINITO se n molto grande!
// Non ha "capito" che serve limite

LEZIONE:
✓ Testa sempre edge cases
✓ Non fidarti ciecamente
✓ Verifica logica, non solo sintassi
```

#### **4. Matematica Complessa Fallisce**

```
PROBLEMA #4: Calcoli complessi inaffidabili

ESEMPIO:
"Qual è 127 * 843?"

IA potrebbe dire: 107,061

Risposta corretta: 107,061 ✓
Ma se chiedi: "E 127 * 844?"
Potrebbe dire: 107,188 ❌ (giusto: 107,188)

Piccolo errore! Ma su calcoli complessi peggiora.

SOLUZIONE:
✓ Non usare LLM per matematica precisa
✓ Usa calcolatrice/codice per calcoli
✓ LLM va bene per LOGICA, non aritmetica
```

#### **5. Sicurezza Non Garantita**

```
PROBLEMA #5: Può generare codice vulnerabile

ESEMPIO:
Prompt: "Leggi password da input"
Output potenziale:
  char password[20];
  scanf("%s", password);  // ❌ BUFFER OVERFLOW!

È sintatticamente corretto ma PERICOLOSO!

COME DIFENDERSI:
✓ Code review sempre
✓ Static analysis (cppcheck)
✓ Fuzzing/testing
✓ Non usare in sistemi safety-critical
   senza validazione esperta
```

**TABELLA RIASSUNTIVA - Quando Fidarsi**

| Task | Affidabilità | Note |
|------|-------------|------|
| **Genera funzione semplice** | 90% | Verifica sempre compilazione |
| **Spiega errore compilatore** | 95% | Ottime spiegazioni |
| **Matematica semplice** | 70% | Meglio usare calcolatrice |
| **Matematica complessa** | 30% | ❌ Non affidabile |
| **Trova bug evidenti** | 85% | Buono ma non perfetto |
| **Trova bug sottili** | 40% | Serve umano esperto |
| **Genera documentazione** | 95% | Eccellente |
| **Code sicuro security-critical** | 50% | ❌ Serve review esperto |
| **Spiega concetti** | 90% | Ottimo teacher |
| **Genera test case** | 80% | Buono, ma aggiungi edge cases tu |

---

## 4. Limiti, Rischi e Uso Responsabile

### 4.1 Allucinazioni - Il Problema #1

**Cos'è un'allucinazione?**

> **Allucinazione IA**: Quando il modello genera informazioni che sembrano vere e plausibili, ma sono completamente inventate.

È come uno studente che invece di dire "non lo so", inventa una risposta che SEMBRA giusta ma è falsa.

**Perché succede?**

L'LLM è addestrato a generare testo che "suona bene", non necessariamente testo VERO. Se non sa qualcosa, potrebbe inventare per completare il pattern!

**Esempi Reali di Allucinazioni:**

#### **Esempio 1: Funzioni Inesistenti (MOLTO COMUNE)**

```c
// ❌ ALLUCINAZIONE TIPICA

Prompt: "Duplica stringa in C"

Output IA:
char *duplicate = strdup(original);

PROBLEMA:
strdup() NON esiste in C standard!
- È una estensione POSIX
- Non compila con -std=c99
- Non funziona su molti embedded
- Ma SEMBRA perfetto!

✅ VERSIONE CORRETTA:
char *duplicate = malloc(strlen(original) + 1);
if (duplicate != NULL) {
    strcpy(duplicate, original);
}
```

#### **Esempio 2: Librerie Inventate**

```cpp
// ❌ ALLUCINAZIONE

Prompt: "Usa sensore XYZ con Arduino"

Output IA:
#include <XYZ_Sensor.h>  // ❌ NON ESISTE!

XYZ_Sensor sensor(A0);
sensor.begin();
float value = sensor.read();

PROBLEMA:
- Libreria inventata
- Metodi plausibili ma falsi
- Compila solo se NON provi davvero

COME RILEVARE:
✓ Cerca libreria su Library Manager Arduino
✓ Controlla su GitHub
✓ Verifica documentazione ufficiale
```

#### **Esempio 3: "Fatti" Inventati**

```
Prompt: "Quanti studenti ITS in Italia 2024?"

Output possibile:
"Ci sono 47.532 studenti iscritti a ITS in Italia
nel 2024, con un aumento del 12.3% rispetto al 2023."

PROBLEMA:
- Numeri TROPPO specifici (sospetto!)
- Nessuna fonte citata
- Potrebbe essere inventato

COME VERIFICARE:
✓ Chiedi: "Qual è la fonte?"
✓ Cerca su siti ufficiali (MIUR, Indire)
✓ Numeri troppo precisi = red flag
```

**Come Difendersi dalle Allucinazioni:**

```
REGOLA D'ORO:
"Fidarsi è bene, NON fidarsi è meglio!"

✅ CHECKLIST ANTI-ALLUCINAZIONE:

1. COMPILA SEMPRE IL CODICE
   [ ] gcc compila senza errori?
   [ ] Zero warning con -Wall -Wextra?

2. VERIFICA FUNZIONI/LIBRERIE
   [ ] Cerchi documentazione ufficiale
   [ ] Esiste su cppreference.com (C/C++)?
   [ ] Esiste su Arduino Library Manager?

3. TESTA L'OUTPUT
   [ ] Unit test passano?
   [ ] Edge cases gestiti?
   [ ] Valgrind pulito (no leak)?

4. CONTROLLA "FATTI"
   [ ] Numeri troppo specifici?
   [ ] Fonte citata verificabile?
   [ ] Cerca su Google per conferma

5. USA STRUMENTI
   [ ] Static analysis (cppcheck)
   [ ] Linter
   [ ] Compiler warning TUTTI abilitati
```

**Segnali di Allarme (Red Flags):**

```
🚩 RED FLAGS - Probabile Allucinazione:

⚠️ "Secondo recenti studi..."
   → Senza citare fonte = inventato

⚠️ Funzione che non hai mai visto
   → Cerca SEMPRE se non conosci

⚠️ Numeri troppo specifici
   → "45.732 studenti" vs "~46.000"

⚠️ "La libreria XYZ fornisce..."
   → Verifica che esista!

⚠️ Codice compila ma non funziona
   → Logica inventata, sintassi ok

⚠️ "Questa funzione è stata introdotta in C99"
   → Verifica su standard ufficiale
```

### 4.2 Bias nei Dati di Training

**Cos'è il Bias?**

> **Bias**: Pregiudizi o distorsioni nei dati di training che si riflettono nelle risposte del modello.

**Esempi di Bias in Programmazione:**

#### **1. Bias Linguistico**

```
PROBLEMA:
L'IA è molto più brava in INGLESE che italiano

ESEMPIO:
Prompt INGLESE:
"Implement binary search in C"
→ Output: Perfetto, ottimizzato, 95% corretto

Prompt ITALIANO:
"Implementa ricerca binaria in C"
→ Output: Funziona ma meno ottimizzato, 80% corretto

SOLUZIONE:
✓ Usa prompts in inglese per codice
✓ Commenti possono essere in italiano
✓ Nomi funzioni in inglese (best practice comunque)
```

#### **2. Bias Platform/Hardware**

```
PROBLEMA:
Più esempi per hardware popolari

BIAS EVIDENTI:
- Arduino Uno >> Arduino Mega >> STM32 >> PIC
- Raspberry Pi >> ESP32 >> Arduino
- x86/Linux >> ARM/Windows >> RISC-V

ESEMPIO:
"Configura I2C su Arduino"
→ Esempi per Uno (Wire.h)

"Configura I2C su PIC18F"
→ Risposta generica, meno precisa

SOLUZIONE:
✓ Specifica ESATTAMENTE il modello hardware
✓ Fornisci datasheet se possibile
✓ Chiedi alternative se primo tentativo vago
```

#### **3. Bias Temporale**

```
PROBLEMA:
Preferisce soluzioni vecchie/deprecate

ESEMPIO:
Prompt: "Temporizza Arduino"

Output potenziale:
delay(1000);  // ❌ Vecchio stile, bloccante

Invece di:
unsigned long previousMillis = 0;
if (millis() - previousMillis >= 1000) {
    // ✅ Moderno, non-bloccante
}

SOLUZIONE:
✓ Specifica anno/versione target
✓ Chiedi esplicitamente "metodo moderno 2025"
✓ Menziona "non-blocking" se rilevante
```

**Mitigare i Bias:**

```
PROMPT DESIGN ANTI-BIAS:

❌ VAGO:
"Scrivi programma Arduino sensore"

✅ SPECIFICO:
"Scrivi sketch Arduino Uno R4 (2024) con sensore
 DHT22, usando libreria DHT sensor library v1.4.6,
 pattern millis() non-bloccante moderno"

ELEMENTI CHIAVE:
✓ Hardware esatto con anno/revisione
✓ Versione libreria
✓ Anno/standard ("moderno 2025", "C99 standard")
✓ Best practices esplicite
```

### 4.3 Sicurezza e Privacy

**⚠️ REGOLA FONDAMENTALE:**

> **MAI inserire dati sensibili in LLM!**

**Perché?**

Quando scrivi qualcosa a ChatGPT/Claude:
1. Viene salvato nei loro server
2. Potrebbe essere usato per training futuro
3. Potrebbe essere visto da revisori umani (quality check)
4. Se c'è breach, potrebbe trapelare

**❌ NON INSERIRE MAI:**

```
ASSOLUTAMENTE VIETATO:

❌ Password (anche vecchie!)
❌ API keys / Token autenticazione
❌ Dati personali:
   - Numeri telefono
   - Indirizzi email/casa
   - Codici fiscali
   - Carte credito (ovvio!)

❌ Codice proprietario aziendale
   - Segreti commerciali
   - Algoritmi protetti
   - Configurazioni interne

❌ Informazioni riservate ITS/scuola
   - Voti altri studenti
   - Dati sensibili progetti
```

**✅ SAFE PRACTICES:**

```
COME USARE IN SICUREZZA:

✅ GENERALIZZA il problema
Invece di:
  "Debug questo codice del server aziendale SuperSecretCorp..."

Usa:
  "Debug questo pattern di server web generico..."

✅ USA DATI MOCK/ESEMPIO
Invece di:
  users = ["mario.rossi@email.com", "giuseppe.verdi@email.com"]

Usa:
  users = ["user1@example.com", "user2@example.com"]

✅ RIMUOVI INFO IDENTIFICATIVE
Codice vero:
  #define SERVER_IP "192.168.1.100"
  #define API_KEY "sk_live_51H3..."

Codice per IA:
  #define SERVER_IP "XXX.XXX.XXX.XXX"
  #define API_KEY "YOUR_API_KEY_HERE"

✅ USA VARIABILI PLACEHOLDER
Invece di nomi reali, usa:
  COMPANY_NAME, PROJECT_X, SECRET_KEY, etc.
```

**Esempio Pratico - Richiesta Sicura:**

```
❌ NON SICURO:

"Debug questo codice del nostro sistema di allarme
presso cliente ACME Corp, IP 10.50.23.15,
password admin: Acme2024!
[codice con logica proprietaria]"

✅ SICURO:

"Debug questo pattern per sistema embedded di
allarme generico. Hardware: Arduino Mega.
Problema: Timeout su connessione server.

[codice con IP/password rimossi, logica sanitizzata]
```

**Tool/Setting Privacy:**

```
OPZIONI PRIVACY (varia per provider):

ChatGPT:
Settings → Data Controls
□ Disable "Improve model for everyone"
  → I tuoi chat NON usati per training

Claude:
Settings → Privacy
□ Conversations private by default

Copilot (GitHub):
Settings → telemetry
□ Disable se non vuoi condividere snippet
```

### 4.4 Linee Guida Uso Responsabile

**Principi Fondamentali:**

```
┌────────────────────────────────────────┐
│  REGOLE D'ORO USO IA 2025              │
├────────────────────────────────────────┤
│                                        │
│  1. IA = ASSISTENTE, non SOSTITUTO    │
│     Tu sei il programmatore,           │
│     IA è il tuo aiutante junior        │
│                                        │
│  2. VERIFICA SEMPRE output critici     │
│     Test, compila, valida              │
│                                        │
│  3. COMPRENDI il codice generato       │
│     Se non capisci, non usare!         │
│     Chiedi spiegazione all'IA stessa   │
│                                        │
│  4. MANTIENI competenze tecniche       │
│     Non diventare dipendente           │
│     Studia i fondamentali              │
│                                        │
│  5. USA ETICA in contesti accademici   │
│     Chiedi al prof se è permesso       │
│     Cita uso IA se richiesto           │
│                                        │
└────────────────────────────────────────┘
```

**✅ Usi Corretti:**

```
DO - Esempi Concreti:

✓ LEARNING:
  "Spiega come funziona malloc() in C"
  → Ottimo per capire concetti!

✓ DEBUGGING:
  "Perché questo codice ha memory leak?"
  [codice di un tuo progetto personale]
  → Aiuto nel trovare bug

✓ BOILERPLATE:
  "Genera setup base Arduino con serial + LED"
  → Accelera tasks ripetitivi

✓ REFACTORING:
  "Come posso migliorare questo codice?"
  → Impari best practices

✓ IDEAZIONE:
  "Suggerisci architettura per sistema IoT"
  → Brainstorming tecnico

✓ DOCUMENTAZIONE:
  "Genera README per questo progetto"
  → Task tedioso automatizzato
```

**❌ Usi Scorretti:**

```
DON'T - Esempi da EVITARE:

❌ COPIA-INCOLLA CIECO:
   Prompt: "Fai esercizio 5 del compito"
   → Copi senza capire
   → Non impari niente
   → Problematico eticamente

❌ ESAMI SENZA PERMESSO:
   Usare IA durante test/esame
   → Se non esplicitamente permesso = CHEATING

❌ DIPENDENZA TOTALE:
   Non sai più fare niente senza IA
   → Perdi competenze base
   → Problema in colloqui/emergenze

❌ CODICE PRODUCTION SENZA REVIEW:
   Deploy diretto codice IA
   → Bug/vulnerabilità
   → Irresponsabile

❌ IGNORA WARNING:
   IA genera codice, compili con -Wall
   → 10 warning
   → Li ignori "tanto funziona"
   → ❌ PESSIMA PRATICA

❌ SOSTITUISCI RAGIONAMENTO:
   "IA non posso pensare per te"
   → Diventi passivo
   → Non sviluppi problem solving
```

**Uso Etico in Contesto Accademico:**

```
GUIDELINES ITS/UNIVERSITÀ:

SEMPRE PERMESSO:
✓ Studiare concetti con IA
✓ Chiedere spiegazioni teoria
✓ Praticare con esercizi extra generati da IA
✓ Debug progetti personali

PERMESSO SE ESPLICITAMENTE AUTORIZZATO:
⚠️ Usare IA per compiti/progetti
⚠️ Generare parti di codice per assignment
⚠️ Refactoring progetti graded

MAI PERMESSO (salvo eccezioni):
❌ Esami/test scritti
❌ Valutazioni individuali
❌ Certificazioni

REGOLA:
"Se in dubbio, CHIEDI al docente!"

CITAZIONE:
Se usi IA per progetto e permesso:
"""
Parti di questo codice sono state generate con
assistenza di [ChatGPT/Claude/Copilot], poi
validate e testate dallo studente.
Specificamente: [funzione X, algoritmo Y]
"""
```

**Auto-Valutazione Uso Responsabile:**

```
DOMANDE DA FARTI:

□ Capisco al 100% il codice generato?
  NO → Studia finché capisci

□ Ho testato tutti i casi edge?
  NO → Scrivi più test

□ So spiegare ogni riga a un collega?
  NO → Non sei pronto a usarlo

□ Sarei in grado di riscriverlo da zero?
  NO → Stai imparando o solo copiando?

□ È permesso usare IA per questo task?
  DUBBIO → Chiedi al docente/responsabile

□ Ho verificato non ci sono vulnerabilità?
  NO → Code review + static analysis

Se rispondi NO a qualcuna:
→ Fermati e correggi prima di procedere!
```

