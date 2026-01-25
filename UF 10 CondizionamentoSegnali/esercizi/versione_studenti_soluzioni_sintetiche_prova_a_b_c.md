# VERSIONE STUDENTI – Soluzioni sintetiche (Prova A + Prova B + Prova C)

Documento con **solo risultati finali e formule chiave**. Nessuno svolgimento intermedio.

---

# PROVA A – Sistema di sensing e ADC

## 1) Schema concettuale sensing

Sensore → Condizionamento (gain + offset + filtro + adattamento impedenza) → ADC → Controllore

Errore: e(t) = r(t) − y_m(t)

---

## 2) Larghezza di banda (formule chiave)

- f_c = 1 / (2π τ)
- Tempo di salita: t_r ≈ 2.2 τ

Trade-off:
- banda alta → risposta rapida, più rumore
- banda bassa → risposta lenta, meno rumore

---

## 3) ADC

- Livelli: N = 2^B
- Passo di quantizzazione: q = (Vmax − Vmin) / 2^B

---

## 4) Sistema di misura (dati Prova A)

Range: x ∈ [−50 , 150] cm

### Trans-caratteristica sensore

vS(x) = 0.002·x − 2.4   [V]

Range sensore: [−2.5 , −2.1] V

---

### Blocco di condizionamento ottimale

vADC = 25·(vS + 2.5)

---

### Risoluzione ADC (B = 8, range 0–10 V)

q = 10 / 256 = 0.03906 V

---

### Stima distanza per vADC = 2 V

x = −10 cm

---

### Risoluzione complessiva

vADC(x) = 0.05·x + 2.5

dvADC/dx = 0.05 V/cm

Δx = q / (dvADC/dx) = 0.78 cm


---
---

# PROVA B – Sensore IR e ADC

Dati:
- x ∈ [0 , 120] cm
- range sensore = 0.6 V
- offset = −4.8 V
- ADC range = [−12 , +12] V
- B = 7

---

## Trans-caratteristica sensore

vS(x) = 0.005·x − 4.8   [V]

Range: [−4.8 , −4.2] V

---

## Blocco di condizionamento ottimale

vADC = 40·vS + 180

---

## Risoluzione ADC

q = 24 / 128 = 0.1875 V

---

## Stima distanza per vADC = 2 V

x = 70 cm

---

## Risoluzione complessiva

vADC(x) = 0.2·x − 12

dvADC/dx = 0.2 V/cm

Δx = 0.94 cm


---
---

# PROVA C – Sistema di misura posizione assoluta

Dati:
- x ∈ [0 , 2000] mm
- Vofs = 2 V
- s = −0.002 V/mm
- ADC range = [0 , 8] V
- incertezza sensore: Ux = ±0.4 mm

---

## Trans-caratteristica sensore

vS(x) = 2 − 0.002·x   [V]

Range: [−2 , +2] V

---

## Blocco di condizionamento ottimale

vADC = 2·vS + 4

---

## Numero minimo di bit

Condizione:

Δx < 0.4 mm

Risultato:

B = 13 bit

---

## Risoluzione (B = 13)

q = 8 / 8192 = 0.0009766 V

Δx = 0.244 mm

---

## Operazione del blocco Processing P

xD = (8 − vD) / 0.004

---

## Stima per vD = 1.75 V

x = 1562.5 mm ± 0.4 mm

x = 1.5625 m ± 0.0004 m


---

# FORMULE RIASSUNTIVE GENERALI

- q = (Vmax − Vmin) / 2^B
- Δx = q / (dvADC/dx)
- vADC = k·vS + V0
- x = funzione inversa di vADC(x)

---

Documento per studio e verifica rapida dei risultati.

