# Soluzione guidata (ITS Meccatronico) – Esame fine modulo Verona

Riferimento: fileciteturn4file0


## 1) Sistema di acquisizione multisensore (3 sensori)

Schema generale:

```
S1 ─┐
    ├─> [Condizionamento 1] ─┐
S2 ─┤                         ├─> [MUX] ─> [ADC] ─> [Elaborazione P]
    ├─> [Condizionamento 2] ─┘
S3 ─┘
        [Condizionamento 3]
```

Funzione dei blocchi:
- **Sensori (S1, S2, S3)**: trasformano grandezze fisiche in segnali elettrici.
- **Condizionamento**: amplificazione, filtraggio, adattamento di impedenza, offset.
- **MUX (multiplexer)**: seleziona quale segnale inviare all’ADC.
- **ADC**: converte il segnale analogico in digitale.
- **Elaborazione P**: calcola le grandezze fisiche e gestisce i dati.


## 2) Sensore non lineare e incertezza

### Trans-caratteristica non lineare (concettuale)

```
 uscita
   ^        *
   |     *
   |   *
   | *
   +----------------> ingresso
```

La relazione ingresso–uscita non è una retta ma una curva.


### Incertezza del sensore

L’incertezza è l’intervallo entro cui si trova il valore vero della misura:

- x = x_misurato ± U

Dipende da:
- rumore
- ripetibilità
- risoluzione
- errori sistematici


## 3) Sistema di acquisizione (condizionamento + ADC + sensore di tilt)

### Dati

- ADC: 8 bit
- Range ADC: [−12 , +12] V
- Uscita sensore: sinusoide con:
  - valore medio = −4 V
  - ampiezza (picco) = 8 V
- Blocco c: v = k·y + V0
- Sensore tilt: sensibilità = 5 mV/deg = 0.005 V/deg


### 3.1 Intervallo del segnale y

- valore minimo: y_min = −4 − 8 = −12 V
- valore massimo: y_max = −4 + 8 = +4 V

Intervallo: [−12 , +4] V


### 3.2 Progetto del blocco di condizionamento

Obiettivo: mappare [−12 , +4] V → [−12 , +12] V

Imponiamo:

- y = −12 → v = −12
- y = +4 → v = +12

Sistema:

- −12 = k(−12) + V0
- +12 = k(4) + V0

Sottrazione:

- 24 = 16k → k = 1.5

Calcolo V0:

- −12 = −18 + V0 → V0 = 6 V

Risultato:

- **v = 1.5·y + 6**


### 3.3 Risoluzione ADC

- N = 2^8 = 256 livelli
- Full-scale = 24 V

Passo di quantizzazione:

- q = 24 / 256 = 0.09375 V


### 3.4 Risoluzione complessiva con sensore di tilt

Sensibilità sensore:

- 0.005 V/deg

Relazione complessiva:

- v = 1.5·y + 6

Sensibilità complessiva:

- dv/dθ = 1.5 · 0.005 = 0.0075 V/deg

Risoluzione angolare:

- Δθ = q / (dv/dθ) = 0.09375 / 0.0075 = 12.5 deg

Risultato:

- **Δθ = 12.5°**


## 4) Sensore a scelta: accelerometro MEMS

### Principio di funzionamento

Un accelerometro MEMS misura l’accelerazione tramite una massa sospesa su micro-molle:

```
  massa mobile
    |
 [====]
  |  |
 molla molla
```

Lo spostamento della massa varia una capacità elettrica che viene convertita in tensione.


### Applicazione: airbag automobilistico

Aspetti di interesse:
- misura rapida delle decelerazioni
- affidabilità elevata
- integrazione con microcontrollore

Attenzioni:
- filtraggio del rumore
- calibrazione
- saturazione in urti violenti

Vantaggi:
- piccolo
- economico
- robusto
- facilmente integrabile


## Riepilogo numerico

- Blocco c: v = 1.5·y + 6
- Risoluzione ADC: q = 0.09375 V
- Risoluzione sistema tilt: Δθ = 12.5°

