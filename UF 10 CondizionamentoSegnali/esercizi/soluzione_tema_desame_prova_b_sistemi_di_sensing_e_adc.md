# Soluzione guidata (ITS Meccatronico) – Prova B

Riferimento: fileciteturn1file0

## 1) Schema del sistema di sensing e funzione dei blocchi

Schema generale:

```
Grandezza fisica x(t)
        |
        v
     [ Sensore S ]  -> segnale elettrico analogico v_S(t)
        |
        v
[ Condizionamento c ] -> v_c(t)
        |
        v
     [ ADC ] -> codice digitale
```

Funzione dei blocchi:
- **Sensore (S)**: converte la grandezza fisica (distanza) in un segnale elettrico proporzionale.
- **Condizionamento (c)**: adatta il segnale al range e alle caratteristiche dell’ADC (amplificazione, offset, filtraggio, adattamento d’impedenza).
- **ADC**: campiona e quantizza il segnale analogico producendo un valore numerico digitale.


## 2) Adattamento di impedenza: definizione e importanza

### Definizione

L’adattamento di impedenza è la funzione del blocco di condizionamento che garantisce:
- impedenza di ingresso elevata verso il sensore;
- impedenza di uscita bassa verso l’ADC.

Formalmente:
- Z_ingresso(c) >> Z_uscita(S)
- Z_uscita(c) << Z_ingresso(ADC)


### Importanza

Serve a:
- non caricare il sensore;
- evitare attenuazioni del segnale;
- preservare la linearità della misura;
- ridurre l’errore sistematico.

### Problema principale che previene

Previene il **partitore resistivo involontario** tra sensore e ADC che causerebbe:
- riduzione dell’ampiezza del segnale;
- errore di scala (gain error);
- perdita di accuratezza.


## 3) Circuito T&H (Track and Hold) dell’ADC

### Funzionamento

Il circuito Track & Hold:
- in fase di **Track** segue il segnale analogico in ingresso;
- in fase di **Hold** mantiene costante il valore istantaneo del segnale durante il tempo di conversione dell’ADC.

Serve a garantire che l’ADC converta un valore stabile.


### Esempio grafico concettuale

Ingresso analogico:

```
   v(t)
    /\    /\    /\
   /  \  /  \  /  \
```

Uscita T&H:

```
   ____      ____      ____
  |    |    |    |    |    |
__|    |____|    |____|    |____
```

Il segnale diventa a gradini costanti durante la conversione.


## 4) Sistema di misura con sensore IR, condizionamento e ADC

Dati:
- distanza: x ∈ [0, 120] cm
- range sensore: 600 mV = 0.6 V
- offset sensore: −4.8 V
- ADC: range [−12, +12] V
- bit ADC: B = 7


### 4.1 Trans-caratteristica del sensore S

La distanza varia di 120 cm con variazione di tensione di 0.6 V.

Pendenza:
- m = 0.6 V / 120 cm = 0.005 V/cm

Offset:
- v_S(0) = −4.8 V

Equazione:

- **v_S(x) = 0.005·x − 4.8   [V]**

Verifica ai bordi:
- x = 0 cm → v_S = −4.8 V
- x = 120 cm → v_S = 0.005·120 − 4.8 = 0.6 − 4.8 = −4.2 V

Range sensore: [−4.8 , −4.2] V


### 4.2 Progetto del blocco di condizionamento c (ottimizzazione ADC)

Obiettivo: sfruttare tutto il range dell’ADC [−12, +12] V.

Trasformazione affine:

- v_ADC = a·v_S + d

Imponiamo:
- v_S = −4.8 V → v_ADC = −12 V
- v_S = −4.2 V → v_ADC = +12 V

Sistema:

- −12 = a(−4.8) + d
- +12 = a(−4.2) + d

Sottrazione:

- 24 = a(0.6)
- a = 40

Calcolo d:

- −12 = 40(−4.8) + d
- d = 180

Quindi:

- **v_ADC = 40·v_S + 180**

Forma equivalente:

- v_ADC = 40·(v_S + 4.5)



### 4.3 Risoluzione dell’ADC

Numero livelli:

- N = 2^7 = 128

Ampiezza full-scale:

- 24 V (da −12 a +12)

Passo di quantizzazione:

- q = 24 / 128 = 0.1875 V

Quindi:

- **q = 187.5 mV per LSB**


### 4.4 Valore di x per v_ADC = 2 V

Invertiamo il condizionamento:

- v_ADC = 40·v_S + 180
- v_S = (v_ADC − 180) / 40

Con v_ADC = 2 V:

- v_S = (2 − 180) / 40 = −178 / 40 = −4.45 V

Invertiamo la legge del sensore:

- v_S = 0.005 x − 4.8
- 0.005 x = v_S + 4.8
- x = (v_S + 4.8) / 0.005

Sostituzione:

- x = (−4.45 + 4.8) / 0.005 = 0.35 / 0.005 = 70 cm

Risultato:

- **x stimato = 70 cm**


### 4.5 Risoluzione complessiva del sistema (Δx)

Ricaviamo v_ADC(x):

- v_S(x) = 0.005 x − 4.8
- v_ADC = 40·v_S + 180

Sostituiamo:

- v_ADC(x) = 40(0.005 x − 4.8) + 180
- v_ADC(x) = 0.2 x − 192 + 180
- v_ADC(x) = 0.2 x − 12

Sensibilità:

- dv_ADC/dx = 0.2 V/cm

Risoluzione spaziale:

- Δx = q / (dv_ADC/dx)
- Δx = 0.1875 / 0.2 = 0.9375 cm

Risultato:

- **Δx ≈ 0.94 cm (circa 9.4 mm)**


## Domande di rinforzo per lo studio

1) Se l’ADC fosse a 10 bit mantenendo lo stesso range, quanto varrebbe Δx?
2) Se non si ottimizzasse il condizionamento e si usasse solo una parte del range ADC, cosa succederebbe alla risoluzione?
3) Qual è il legame tra adattamento di impedenza e circuito T&H?

