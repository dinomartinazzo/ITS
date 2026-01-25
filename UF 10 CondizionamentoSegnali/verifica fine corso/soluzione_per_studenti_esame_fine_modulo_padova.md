# Soluzione guidata (ITS Meccatronico) – Esame fine modulo (Padova)

Riferimento: fileciteturn3file0

## 1) Sistema di controllo retroazionato: schema, posizione e ruolo del sensing

### Schema a blocchi (feedback negativo)

```
        r(t)                 e(t)               u(t)                 y(t)
Set-point ---> [ Σ ] ----------------> [ Controllore ] ---> [ Impianto/Attuatore ] ---> Uscita
               +  -
               |  ^
               |  |
               |  +-------------------- [ Sensing: sensore + condizionamento + ADC ]
               |                        (misura y_m(t))
               +--------------------------------------------------------------
```

- **Posizione**: il sensing sta **nel ramo di retroazione** (feedback) e misura l’uscita (o una grandezza correlata).
- **Ruolo**: genera la misura y_m(t) che viene confrontata con il riferimento r(t) per ottenere l’errore e(t)=r(t)−y_m(t).
- **Importanza**:
  - accuratezza della misura → accuratezza del controllo;
  - ritardi/filtri/rumore in feedback influenzano stabilità e prestazioni;
  - saturazioni o errori di scala in sensing possono portare a controllo scorretto.


## 2) Sensore di prossimità a scelta: sensore induttivo (principio e disegno)

### Principio di funzionamento
Un sensore **induttivo** rileva oggetti **metallici** mediante un campo elettromagnetico generato da un oscillatore ad alta frequenza:
- una bobina alimentata genera un campo;
- quando un metallo entra nel campo, si generano **correnti parassite** (eddy currents);
- queste dissipano energia e smorzano l’oscillazione;
- l’elettronica interna rileva la variazione e commuta l’uscita (ON/OFF o analogica).

### Disegno concettuale

```
[Oscillatore]-->[Bobina] ))))))  campo  ))))))   | oggetto metallico |
                     |--------------------------->|  (target)        |
                     |   correnti parassite <----|
                     v
              [Rilevatore ampiezza] -> [Comparatore] -> OUT
```

### Note tipiche
- Pro: robusto, insensibile a sporco non metallico, veloce.
- Contro: rileva solo metalli, distanza di intervento limitata.


## 3) Non linearità di un sensore: definizione

La **non linearità** quantifica quanto la caratteristica reale del sensore si discosta dalla retta ideale.

Definizione tipica (metodo “best-fit line” o “end-point”, a seconda del contesto):

- Non linearità (%) = (errore massimo rispetto alla retta di riferimento / fondo scala) · 100

Dove:
- errore massimo = max |v_reale(x) − v_retta(x)|
- fondo scala = variazione totale dell’uscita sul range (V_FS)

Quindi:

- **NL% = (max|Δv| / V_FS)·100**


## 4) Sistema di misura: sensore ultrasuoni + condizionamento + ADC

Dati:
- Sensore lineare:
  - sensibilità: 2 mV/cm = 0.002 V/cm
  - offset: −2.4 V
  - range: x ∈ [0 , 200] cm
- ADC:
  - input range: [0 , 10) V
  - bit: B = 6


### 4.1 Trans-caratteristica del sensore

- **vS(x) = 0.002·x − 2.4   [V]**

Valori agli estremi:
- x = 0 cm → vS = −2.4 V
- x = 200 cm → vS = 0.002·200 − 2.4 = 0.4 − 2.4 = −2.0 V

Range sensore: [−2.4 , −2.0] V (ampiezza 0.4 V)

Disegno qualitativo:

```
 vS [V]
 -2.0 |                      * (200 cm)
      |
 -2.2 |             *
      |
 -2.4 |* (0 cm)
      +----------------------------- x [cm]
        0                      200
```


### 4.2 Progetto del blocco di condizionamento c (ottimale per ADC)

Obiettivo: mappare il range sensore [−2.4 , −2.0] V su [0 , 10] V.

Usiamo:
- vADC = a·vS + d

Vincoli:
- vS = −2.4 → vADC = 0
- vS = −2.0 → vADC = 10

Calcolo:
- 10 = a(−2.0 + 2.4) = a(0.4) → a = 25
- 0 = 25(−2.4) + d → d = 60

Quindi:

- **vADC = 25·vS + 60**

Forma equivalente:

- **vADC = 25·(vS + 2.4)**


### 4.3 Risoluzione dell’ADC (B=6, range 0–10 V)

- N = 2^6 = 64 livelli
- q = 10 / 64 = 0.15625 V

Quindi:

- **q = 156.25 mV per LSB**


### 4.4 Risoluzione complessiva del sistema in termini di Δx

Ricaviamo la sensibilità complessiva vADC(x):

- vS(x) = 0.002x − 2.4
- vADC = 25(vS + 2.4)

Sostituzione:

- vADC(x) = 25(0.002x) = 0.05x

Quindi:
- dvADC/dx = 0.05 V/cm

Risoluzione spaziale:

- Δx = q / (dvADC/dx) = 0.15625 / 0.05 = 3.125 cm

Risultato:

- **Δx = 3.125 cm**


## Riepilogo finale (numeri chiave)

- Sensore: vS(x) = 0.002x − 2.4 [V]
- Condizionamento ottimale: vADC = 25(vS + 2.4)
- Risoluzione ADC: q = 0.15625 V
- Sensibilità complessiva: vADC(x) = 0.05x [V] (x in cm)
- Risoluzione complessiva: Δx = 3.125 cm
