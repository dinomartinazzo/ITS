# Soluzione guidata (ITS Meccatronico) – Prova A

Riferimento: fileciteturn0file0

## 1) Schema di un sistema di controllo retroazionato e ruolo del blocco di sensing

### 1.1 Schema a blocchi (feedback negativo)

```
        r(t)                 e(t)              u(t)                 y(t)
Set-point ---> [ Σ ] ----------------> [ Controllore ] ---> [ Attuatore/Impianto ] ---> Uscita
               +  -
               |  ^
               |  |
               |  +-------------------- [ Sensing: sensore + condizionamento + ADC ]
               |                        (misura y_m(t))
               +--------------------------------------------------------------
```

- r(t): riferimento (set-point)
- y(t): uscita reale dell’impianto
- y_m(t): uscita misurata (versione “osservata” di y(t))
- e(t) = r(t) − y_m(t): errore

### 1.2 Posizione e funzione del sensing

Il blocco di sensing si trova **nel ramo di retroazione** e ha lo scopo di:
- misurare la grandezza d’uscita (o una grandezza correlata);
- convertire la misura in un segnale utilizzabile dal controllore (spesso digitale).

**Composizione tipica del sensing**:
- sensore (trasduttore) che trasforma la grandezza fisica in segnale elettrico;
- condizionamento (amplificazione, offset, filtraggio, adattamento d’impedenza);
- conversione A/D (campionamento e quantizzazione).

### 1.3 Importanza del sensing

Il sensing impatta direttamente:
- **stabilità**: un errore di misura o un ritardo può ridurre margine di fase e portare a instabilità;
- **accuratezza**: offset, non linearità e rumore degradano la qualità della retroazione;
- **banda passante complessiva**: un sensing lento “taglia” le dinamiche veloci, limitando le prestazioni;
- **robustezza**: rumore elevato in feedback aumenta l’azione di controllo, con rischio di saturazioni.


## 2) Larghezza di banda del blocco di condizionamento: definizione e importanza (tempo di salita e rumore)

### 2.1 Definizione

Per un blocco di condizionamento (tipicamente un filtro/amplificatore) si definisce **larghezza di banda** l’intervallo di frequenze in cui il modulo della risposta in frequenza resta entro un certo limite rispetto al valore a bassa frequenza.

Caso tipico: filtro passa-basso del 1° ordine.
- Frequenza di taglio (−3 dB): f_c
- Banda utile (in prima approssimazione): 0 → f_c

### 2.2 Collegamento con la prontezza (tempo di salita)

Per un passa-basso del 1° ordine:
- Costante di tempo: τ
- Relazione: f_c = 1 / (2π τ)
- Tempo di salita (10–90%): t_r ≈ 2.2 τ

Quindi:
- **banda maggiore** (f_c più alta) → τ più piccola → **tempo di salita più breve** (sistema più pronto);
- **banda minore** (f_c più bassa) → τ più grande → **tempo di salita più lungo** (sistema più lento).

### 2.3 Collegamento con la riduzione del rumore

Il rumore (specialmente ad alta frequenza) viene attenuato da un passa-basso:
- riducendo la banda, si attenuano più componenti rumorose;
- aumentando la banda, si lascia passare più rumore.

Trade-off tipico:
- **banda alta**: migliore dinamica (misure “rapide”) ma più rumore;
- **banda bassa**: misura più “pulita” ma più lenta.

Regola pratica in acquisizione:
- impostare la banda del condizionamento appena sopra la massima frequenza utile del segnale misurato, evitando di lasciare banda inutile che contiene solo rumore.


## 3) Ruolo dell’ADC nel sensing: quantizzazione e risoluzione

### 3.1 Ruolo dell’ADC

L’ADC (Analog-to-Digital Converter) trasforma una tensione analogica v(t) in un numero digitale (codice). Le operazioni fondamentali sono:
- **campionamento** nel tempo (sampling) → discreto nel tempo;
- **quantizzazione** in ampiezza → discreto nei livelli.

### 3.2 Quantizzazione

La quantizzazione assegna a ogni valore di ingresso un livello tra N livelli disponibili.
- Ingresso continuo → insieme di “gradini” discreti.
- L’errore di quantizzazione e_q è tipicamente compreso in:
  - e_q ∈ [−q/2, +q/2]
  dove q è il passo di quantizzazione (LSB).

### 3.3 Risoluzione

La risoluzione di un ADC ideale è il minimo incremento di tensione distinguibile, pari al passo:
- N = 2^B (numero livelli)
- Se il range è [V_min, V_max], allora:
  - q = (V_max − V_min) / 2^B

Nota pratica: in alcuni datasheet si usa 2^B − 1 nel denominatore per l’ampiezza full-scale codificabile. In ambito didattico e per stime si usa spesso 2^B.


## 4) Sistema di misura: sensore S + condizionamento c + ADC (B=8, range ADC [0,10] V)

Dati:
- Intervallo distanza: x ∈ [−50, 150] cm
- Sensore lineare con:
  - range di uscita: 400 mV (variazione totale sul range di x)
  - offset: −2.4 V
- ADC:
  - input range: [0, 10] V
  - bit: B = 8

### 4.1 Trans-caratteristica del sensore S (grafico e formula)

Interpretazione coerente con i dati:
- La variazione complessiva di uscita sul range di x è 0.4 V.
- La distanza varia di 200 cm (da −50 a 150).
- Pendenza:
  - m = 0.4 V / 200 cm = 0.002 V/cm = 2 mV/cm

Definiamo il vincolo sull’offset come valore a x = 0 cm:
- v_S(0) = −2.4 V

Allora la trans-caratteristica è:
- v_S(x) = m x + b
- b = −2.4 V
- m = 0.002 V/cm

Quindi:
- **v_S(x) = 0.002·x − 2.4   [V]**, con x in cm.

Verifica ai bordi:
- x = −50 cm → v_S = 0.002·(−50) − 2.4 = −0.1 − 2.4 = −2.5 V
- x = 150 cm → v_S = 0.002·150 − 2.4 = 0.3 − 2.4 = −2.1 V

Il range in uscita del sensore è quindi [−2.5, −2.1] V (ampiezza 0.4 V), coerente.

Rappresentazione qualitativa:

```
 v_S [V]
  -2.1 |                         * (150 cm)
       |
       |
  -2.3 |               * (50 cm)
       |
  -2.4 |        * (0 cm)
       |
  -2.5 | * (-50 cm)
       +----------------------------------- x [cm]
         -50          0                150
```


### 4.2 Progetto del blocco di condizionamento c per ottimizzare l’ADC

Obiettivo: usare tutto il range [0,10] V dell’ADC per massimizzare la risoluzione effettiva sulla misura di x.

Range sensore:
- v_S,min = −2.5 V
- v_S,max = −2.1 V

Progettiamo una trasformazione affine:
- v_ADC = a·v_S + d

Imponiamo:
- v_S = −2.5 V  -> v_ADC = 0 V
- v_S = −2.1 V  -> v_ADC = 10 V

Sistema:
- 0 = a(−2.5) + d
- 10 = a(−2.1) + d

Sottrazione:
- 10 = a(−2.1 + 2.5) = a(0.4)
- a = 10 / 0.4 = 25

Poi:
- 0 = 25(−2.5) + d  => d = 62.5

Quindi:
- **v_ADC = 25·v_S + 62.5**

Forma equivalente più “circuitale” (shift + gain):
- v_ADC = 25 · (v_S + 2.5)

perché:
- 25(v_S + 2.5) = 25 v_S + 62.5

Implementazione tipica (concettuale):
- somma di offset (+2.5 V) tramite riferimento e stadio sommatore;
- amplificazione con guadagno 25 (op-amp non invertente o stadio dedicato);
- eventuale filtro passa-basso per limitare rumore e anti-aliasing.

Nota operativa:
- è necessario che l’op-amp e l’alimentazione consentano l’escursione in uscita 0–10 V (rail-to-rail o alimentazioni adeguate) e che le tensioni di riferimento siano stabili.


### 4.3 Risoluzione dell’ADC

Per ADC ideale con range 0–10 V e B=8:
- N = 2^8 = 256 livelli
- q = (10 − 0) / 256 = 10 / 256 V

Calcolo:
- 10 / 256 = 0.0390625 V

Quindi:
- **q = 39.0625 mV per LSB**


### 4.4 Stima della distanza x corrispondente a v_ADC = 2 V

Usiamo la catena:
1) invertiamo il condizionamento per risalire a v_S
- v_ADC = 25(v_S + 2.5)
- v_S + 2.5 = v_ADC / 25
- v_S = (v_ADC / 25) − 2.5

Con v_ADC = 2 V:
- v_S = (2/25) − 2.5 = 0.08 − 2.5 = −2.42 V

2) invertiamo la trans-caratteristica del sensore
- v_S = 0.002 x − 2.4
- 0.002 x = v_S + 2.4
- x = (v_S + 2.4) / 0.002

Sostituzione:
- x = (−2.42 + 2.4) / 0.002 = (−0.02) / 0.002 = −10 cm

Risultato:
- **x stimato = −10 cm**


### 4.5 Risoluzione complessiva in termini di Δx

Vogliamo il minimo incremento di distanza distinguibile dato un LSB dell’ADC.

Relazione tra x e v_ADC.
Partiamo da:
- v_S(x) = 0.002 x − 2.4
- v_ADC = 25(v_S + 2.5)

Sostituiamo v_S:
- v_ADC(x) = 25[(0.002 x − 2.4) + 2.5]
- v_ADC(x) = 25(0.002 x + 0.1)
- v_ADC(x) = 0.05 x + 2.5

Quindi la sensibilità complessiva è:
- dv_ADC/dx = 0.05 V/cm

Un LSB vale q = 0.0390625 V.
Allora:
- Δx = q / (dv_ADC/dx)
- Δx = 0.0390625 / 0.05 cm

Calcolo:
- 0.0390625 / 0.05 = 0.78125 cm

Risultato:
- **risoluzione complessiva Δx ≈ 0.78125 cm (circa 7.8 mm)**

Interpretazione:
- ogni incremento di 1 LSB dell’ADC corrisponde a circa 0.78 cm di variazione di distanza.


## Esercizio di controllo rapido (per autovalutazione)

1) Se il range ADC fosse [0, 5] V con B=8, quale sarebbe Δx (con lo stesso condizionamento ridisegnato per usare tutto il range)?
2) Se si aumentasse B a 10 bit mantenendo [0,10] V, quale sarebbe la nuova Δx?

Suggerimento: rifare solo i passaggi 4.3 e 4.5.

