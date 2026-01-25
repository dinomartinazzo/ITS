# Soluzione guidata (ITS Meccatronico) – Prova C

Riferimento: fileciteturn2file0

## Dati del problema

- Intervallo di misura: x ∈ [0 , 2] m = [0 , 2000] mm
- Sensore lineare assoluto S:
  - offset: Vofs = 2 V
  - sensibilità: s = −2 mV/mm = −0.002 V/mm
  - incertezza: Ux = ±0.4 mm
- Blocco di condizionamento c: offset V0 e guadagno k0
- ADC:
  - input range: [0 , 8] V
  - numero di bit: B


## 1) Trans-caratteristica del sensore (con incertezza)

Legge lineare del sensore:

- vS(x) = Vofs + s·x

Sostituendo i dati:

- **vS(x) = 2 − 0.002·x   [V]**   (con x in mm)

Valori agli estremi:
- x = 0 mm → vS = 2 V
- x = 2000 mm → vS = 2 − 0.002·2000 = −2 V

Range del sensore: [−2 , +2] V

Tenendo conto dell’incertezza:

- vS(x) ∈ [2 − 0.002·(x ± 0.4)]

Graficamente (banda di incertezza):

```
 vS [V]
  2 |*-----------------
    | \   banda di
    |  \  incertezza
  0 |   \
    |    \
 -2 |-----*------------
    +------------------- x [mm]
      0             2000
```


## 2) Progetto del blocco di condizionamento c (ottimale)

Obiettivo: sfruttare tutto il range dell’ADC [0 , 8] V.

Range sensore:
- vS,min = −2 V
- vS,max = +2 V

Trasformazione affine:

- vADC = k0·vS + V0

Vincoli:
- vS = −2 V → vADC = 0 V
- vS = +2 V → vADC = 8 V

Sistema:

- 0 = k0(−2) + V0
- 8 = k0(2) + V0

Sottrazione:

- 8 = 4k0  →  k0 = 2

Calcolo V0:

- 0 = −4 + V0  →  V0 = 4 V

Quindi:

- **vADC = 2·vS + 4**


## 3) Numero di bit B per risoluzione complessiva < 0.4 mm

Relazione tra vADC e x:

- vS(x) = 2 − 0.002x
- vADC = 2vS + 4 = 2(2 − 0.002x) + 4 = 8 − 0.004x

Sensibilità complessiva:

- dvADC/dx = −0.004 V/mm

Risoluzione spaziale:

- Δx = q / |dvADC/dx|

con:

- q = 8 / 2^B

Richiesta:

- Δx < 0.4 mm

Sostituzione:

- (8 / 2^B) / 0.004 < 0.4
- 8 / (0.004 · 2^B) < 0.4
- 2000 / 2^B < 0.4
- 2^B > 5000

Poiché:
- 2^12 = 4096
- 2^13 = 8192

Risulta:

- **B = 13 bit** (minimo valore accettabile)


## 4) Risoluzione ADC e del sistema (con B = 13)

Passo ADC:

- q = 8 / 2^13 = 8 / 8192 = 0.0009766 V ≈ 0.977 mV

Risoluzione spaziale:

- Δx = q / 0.004 = 0.0009766 / 0.004 = 0.244 mm

Risultato:

- Risoluzione ADC: 0.977 mV
- Risoluzione sistema: **Δx ≈ 0.244 mm**


## 5) Operazione del blocco P (Processing)

Il blocco P deve invertire la relazione vADC(x).

Da:

- vADC = 8 − 0.004x

Si ricava:

- 0.004x = 8 − vADC
- x = (8 − vADC) / 0.004

Quindi l’operazione svolta da P è:

- **xD = (8 − vD) / 0.004**   (con vD campione ADC)


## 6) Risultato della misura per vD = 1.75 V (con incertezza)

Stima nominale:

- xD = (8 − 1.75) / 0.004 = 6.25 / 0.004 = 1562.5 mm = 1.5625 m

Tenendo conto dell’incertezza del sensore:

- Ux = ±0.4 mm

Risultato finale:

- **x = (1562.5 ± 0.4) mm**

Oppure:

- **x = (1.5625 ± 0.0004) m**


## Domande di rinforzo

1) Se l’ADC fosse a 12 bit, la specifica di risoluzione sarebbe soddisfatta?
2) Qual è il ruolo dell’offset V0 nel blocco di condizionamento?
3) Perché la risoluzione deve essere migliore dell’incertezza del sensore?

