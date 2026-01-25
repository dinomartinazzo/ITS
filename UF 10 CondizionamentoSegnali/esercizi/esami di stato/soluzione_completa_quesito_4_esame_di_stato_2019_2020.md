# Soluzione completa (ITS Meccatronico) – Quesito 4: acquisizione posizione angolare

Riferimenti:
- Esame di Stato 2019 (testo): fileciteturn5file2; (materiale 2019): fileciteturn5file0
- Esame di Stato 2020 (testo): fileciteturn5file3; (materiale 2020): fileciteturn5file1

Nota: si risolvono i punti richiesti nei due temi (2019 e 2020). Nomenclatura: tensioni in volt, angoli in gradi.

---

# A) ESAME DI STATO 2019 – Quesito 4 (sensore angolare, MUX, ADC B=6)

## Dati
- Angolo: ξ ∈ [180°, 360°]
- Uscita sensore: Vs ∈ [−90, +90] mV = [−0.09, +0.09] V
- Primo condizionamento: V1 = k1·Vs + Y1
- MUX accetta: V1 ∈ [0, 3] V
- Secondo condizionamento: V0 = k0·V1 + Y0
- ADC: input range [−9, +9] V, B = 6 bit
- Richiesta campionamento: 3 ingressi; MUX commuta ogni 20 ms; almeno 10 campioni per ogni ingresso per scansione.

---

## 1) Sensibilità del sensore

ΔVs = 0.09 − (−0.09) = 0.18 V

Δξ = 360 − 180 = 180°

Sensibilità:

S = ΔVs/Δξ = 0.18/180 = 0.001 V/° = 1 mV/°

Risultato:
- **S = 1 mV/°**

---

## 2) k1 e Y1 ottimali (mappatura [−0.09, +0.09] → [0, 3])

Condizioni:
- Vs = −0.09 → V1 = 0
- Vs = +0.09 → V1 = 3

Soluzione:
- k1 = 3/0.18 = 16.6667
- Y1 = 1.5 V

Risultato:
- **k1 = 16.6667**
- **Y1 = 1.5 V**

---

## 3) k0 e Y0 ottimali (mappatura [0, 3] → [−9, +9])

Condizioni:
- V1 = 0 → V0 = −9
- V1 = 3 → V0 = +9

Soluzione:
- k0 = 6
- Y0 = −9 V

Risultato:
- **k0 = 6**
- **Y0 = −9 V**

---

## 4) Risoluzione dell’ADC

- Full-scale = 18 V
- N = 2^6 = 64

q_ADC = 18/64 = 0.28125 V

Risultato:
- **q_ADC = 0.28125 V/LSB**

---

## 5) Risoluzione angolare equivalente del sistema

Il progetto usa l’intero range ADC per coprire l’intero intervallo angolare 180°.

Δξ = 180°/64 = 2.8125°

Risultato:
- **Risoluzione angolare = 2.8125°**

---

## 6) Numero di bit per risoluzione < 1°

Serve:

180/2^B < 1  →  2^B > 180  →  B > log2(180) ≈ 7.49

Risultato:
- **B_min = 8 bit**

---

## 7) Formula per ottenere ξD dai campioni V0 (Processing)

Catena diretta:
- V1 = k1·Vs + Y1
- V0 = k0·V1 + Y0

Inversione:
- V1 = (V0 − Y0)/k0
- Vs = (V1 − Y1)/k1

Legge del sensore (da sensibilità e riferimento ξ=180° a Vs=−0.09 V):
- Vs = 0.001·(ξ − 180) − 0.09

Equivalentemente:
- ξ = 180 + (Vs + 0.09)/0.001

Composizione (forma generale):

ξD = 180 + (1/0.001)·( (1/k1)·( (V0 − Y0)/k0 − Y1 ) + 0.09 )

Sostituendo i valori ottimali (k1=16.6667, Y1=1.5, k0=6, Y0=−9):

- **ξD = 180 + 1000·( ( (V0 + 9)/6 − 1.5 )/16.6667 + 0.09 )**

Forma semplificata (numerica):

- (1/(0.001·k1)) = 60
- **ξD = 60·( (V0 + 9)/6 − 1.5 ) + 180**

---

## 8) Frequenza minima di campionamento RS

- 3 ingressi
- 20 ms per ingresso → scansione completa = 3·20 ms = 60 ms
- minimo 10 campioni per ingresso → 30 campioni in 60 ms

RS_min = 30/0.06 = 500 S/s

Risultato:
- **RS_min = 500 S/s**

---

# B) ESAME DI STATO 2020 – Quesito 4 (sensore angolare, c1, c2, ADC B=8)

## Dati
- Angolo: x ∈ [0°, 180°]
- Sensore: offset V0 = −0.2 V, sensibilità 4 mV/° = 0.004 V/°
- Uscita sensore: Vs = −0.2 + 0.004·x
- c1: V1 = k1·Vs + V10, con range richiesto V1 ∈ [0, 4] V
- c2: v = k2·V1 + V20
- ADC: input range [−8, +8] V, B = 8 bit
- Test/calibrazione: 30°→150°→30° con velocità costante ±40°/s; stop 1 s a 30°, 90°, 150°; ripetere 3 volte.
- Frequenza campionamento per punto 8: RS = 20 S/s

---

## 1) Output range del sensore

Per x=0°:
- Vs = −0.2 V

Per x=180°:
- Vs = −0.2 + 0.004·180 = −0.2 + 0.72 = 0.52 V

Risultato:
- **Vs ∈ [−0.2 , 0.52] V**

---

## 2) k1 e V10 ottimali (mappatura [−0.2, 0.52] → [0, 4])

Condizioni:
- Vs = −0.2 → V1 = 0
- Vs = 0.52 → V1 = 4

Soluzione:
- k1 = 4/0.72 = 5.5556
- V10 = 0.2·k1 = 1.1111 V

Risultato:
- **k1 = 5.5556**
- **V10 = 1.1111 V**

---

## 3) k2 e V20 ottimali (mappatura [0, 4] → [−8, +8])

Condizioni:
- V1 = 0 → v = −8
- V1 = 4 → v = +8

Soluzione:
- k2 = 4
- V20 = −8 V

Risultato:
- **k2 = 4**
- **V20 = −8 V**

---

## 4) Risoluzione dell’ADC

- Full-scale = 16 V
- N = 2^8 = 256

q_ADC = 16/256 = 0.0625 V

Risultato:
- **q_ADC = 62.5 mV/LSB**

---

## 5) Risoluzione angolare del sistema

Poiché l’intera catena usa l’intero ADC per coprire 180°:

Δx = 180/256 = 0.703125°

Risultato:
- **Risoluzione angolare = 0.703°**

---

## 6) Formula per ottenere xD dai campioni digitalizzati vD (Processing)

Inversione della catena:

- V1 = (vD − V20)/k2
- Vs = (V1 − V10)/k1

Legge sensore:
- Vs = −0.2 + 0.004·x  →  x = (Vs + 0.2)/0.004

Composizione:

- **xD = (  ( ( (vD − V20)/k2 ) − V10 )/k1  + 0.2 ) / 0.004**

Con valori ottimali (k1=5.5556, V10=1.1111, k2=4, V20=−8):

- **xD = ( ( ( (vD + 8)/4 ) − 1.1111 )/5.5556 + 0.2 ) / 0.004**

---

## 7) Diagramma angolo-tempo (descrizione per disegno)

- Rampa lineare 30°→150° a 40°/s:
  - Δ=120° → 120/40 = 3 s
- Rampa lineare 150°→30° a 40°/s:
  - 3 s
- Stop 1 s a 30°, 90°, 150° in andata e ritorno.

Sequenza tipica di un ciclo (andata+ritorno):
- soste complessive: 6 s (3 s in andata + 3 s in ritorno)
- rampe complessive: 6 s
- durata ciclo: **12 s**

Il grafico è un’onda trapezoidale “avanti e indietro” con tratti piatti a 30°, 90°, 150°.

Tre cicli: **36 s** totali.

---

## 8) Numero di campioni acquisiti in un ciclo (andata+ritorno)

- RS = 20 S/s
- T_ciclo = 12 s

N = RS·T = 20·12 = 240 campioni

Risultato:
- **N = 240 campioni per un ciclo completo**

---

# Checklist “metodo” (per studenti)

1) Calcola range del sensore agli estremi dell’ingresso.
2) Imposta una trasformazione affine per il condizionamento: v_out = k·v_in + Voff.
3) Risolvi k e Voff imponendo i due vincoli ai bordi (min→min, max→max).
4) Risoluzione ADC: q = (Vmax−Vmin)/2^B.
5) Risoluzione in grandezza fisica: Δx = range_x / 2^B (se la catena usa tutto l’ADC).
6) Processing: inverti in ordine inverso tutti i blocchi fino a tornare alla grandezza fisica.
7) Campionamento con MUX: conta quanti campioni servono per scansione e dividi per la durata scansione.

