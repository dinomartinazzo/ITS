# DISPENSA ITS
## Esperimento sul Ponte di Wheatstone con Arduino (Simulazione)

---

# 1. OBIETTIVI DIDATTICI

Al termine dell’attività lo studente sarà in grado di:

- Comprendere la struttura e il principio di funzionamento del ponte di Wheatstone.
- Calcolare la tensione di sbilanciamento del ponte.
- Utilizzare l’ADC di Arduino per misure analogiche.
- Effettuare misure differenziali in software.
- Analizzare la sensibilità del sistema rispetto a variazioni resistive.
- Comprendere il concetto di bilanciamento del ponte.

---

# 2. RICHIAMI TEORICI

## 2.1 Struttura del ponte

Il ponte di Wheatstone è costituito da quattro resistenze disposte in due rami paralleli:

- R1 e R2 nel ramo sinistro
- R3 e Rx nel ramo destro (Rx = resistenza incognita o sensore)

L’alimentazione è applicata tra il nodo superiore (+Vcc) e il nodo inferiore (GND).

I nodi centrali dei due rami generano due tensioni:

VL = tensione tra R1 e R2
VR = tensione tra R3 e Rx

L’uscita del ponte è:

Vout = VL − VR

---

## 2.2 Calcolo delle tensioni

Ogni ramo è un partitore resistivo.

VL = Vcc · (R2 / (R1 + R2))

VR = Vcc · (Rx / (R3 + Rx))

Quindi:

Vout = Vcc · [ R2/(R1+R2) − Rx/(R3+Rx) ]

---

## 2.3 Condizione di bilanciamento

Il ponte è bilanciato quando:

R1 / R2 = R3 / Rx

In questa condizione:

Vout = 0 V

---

# 3. CONFIGURAZIONE SPERIMENTALE (SIMULAZIONE)

## 3.1 Componenti

- Arduino UNO (simulato)
- 3 resistenze da 10 kΩ
- 1 potenziometro da 10 kΩ (simula Rx)
- Alimentazione 5 V (Arduino)

## 3.2 Collegamenti

Nodo superiore del ponte → 5V
Nodo inferiore del ponte → GND

Nodo VL → A0
Nodo VR → A1

Non si collega direttamente Vout perché potrebbe assumere valori negativi rispetto a GND. La differenza viene calcolata via software.

---

# 4. CARATTERISTICHE ADC ARDUINO UNO

- Risoluzione: 10 bit
- Intervallo digitale: 0–1023
- Tensione di riferimento tipica: 5 V

Conversione ADC → Volt:

V = (ADC · Vref) / 1023

Risoluzione teorica (LSB):

LSB ≈ 5 V / 1023 ≈ 4.88 mV

---

# 5. CODICE ARDUINO COMPLETO

```cpp
/*
  Esperimento ITS: Ponte di Wheatstone
  Lettura differenziale in software
*/

const int PIN_VL = A0;
const int PIN_VR = A1;

const float VREF = 5.0;
const int ADC_MAX = 1023;

const int N_SAMPLES = 20;

int readAvg(int pin) {
  long sum = 0;
  for (int i = 0; i < N_SAMPLES; i++) {
    sum += analogRead(pin);
    delay(2);
  }
  return (int)(sum / N_SAMPLES);
}

float adcToVolt(int adc) {
  return (adc * VREF) / ADC_MAX;
}

void setup() {
  Serial.begin(115200);
  while (!Serial) { ; }
}

void loop() {
  int adcVL = readAvg(PIN_VL);
  int adcVR = readAvg(PIN_VR);

  float VL = adcToVolt(adcVL);
  float VR = adcToVolt(adcVR);

  float Vout = VL - VR;

  Serial.print("VL: "); Serial.print(VL,4);
  Serial.print("  VR: "); Serial.print(VR,4);
  Serial.print("  Vout: "); Serial.println(Vout,4);

  delay(200);
}
```

---

# 6. PROCEDURA DI LABORATORIO

1. Costruire il ponte in simulazione.
2. Impostare Rx = 10 kΩ.
3. Verificare che VL ≈ VR ≈ 2.5 V.
4. Registrare i valori letti da Arduino.
5. Variare Rx in almeno 5 punti.
6. Compilare la tabella dati.

---

# 7. ESEMPIO DI CALCOLO

Dati:

Vcc = 5 V
R1 = R2 = R3 = 10 kΩ
Rx = 12 kΩ

VL = 5 · (10 / 20) = 2.5 V

VR = 5 · (12 / 22) = 2.727 V

Vout = 2.5 − 2.727 = −0.227 V

Confrontare con misura simulata.

---

# 8. ANALISI DATI

Gli studenti devono:

- Confrontare teoria e misura.
- Stimare l’errore percentuale.
- Valutare la sensibilità locale:

Sensibilità ≈ ΔVout / ΔRx

- Discutere la quasi-linearità vicino al punto di bilanciamento.

---

# 9. ESTENSIONI AVANZATE

1. Ricavare Rx dalla misura di VR:

   Rx = R3 · VR / (Vcc − VR)

2. Simulare un sensore (estensimetro) come Rx = R(1 + ε).

3. Discutere perché nei sistemi reali si utilizza un amplificatore strumentale.

---

# 10. CONCLUSIONI

Il ponte di Wheatstone è uno strumento fondamentale per la misura di piccole variazioni resistive.

La simulazione con Arduino consente di comprendere:

- Il comportamento dei partitori.
- Il concetto di misura differenziale.
- I limiti dell’ADC.
- La sensibilità del sistema.

Questa esperienza costituisce base per applicazioni con estensimetri, sensori di pressione, celle di carico e trasduttori resistivi.

---

# 11. ESERCIZI PROPOSTI

## Esercizio 1 – Bilanciamento del ponte

Dati:
R1 = 10 kΩ
R2 = 15 kΩ
R3 = 12 kΩ

Determinare il valore di Rx affinché il ponte sia bilanciato.

---

## Esercizio 2 – Calcolo tensione di sbilanciamento

Dati:
Vcc = 5 V
R1 = R2 = R3 = 10 kΩ
Rx = 8 kΩ

Calcolare:
1) VL
2) VR
3) Vout

---

## Esercizio 3 – Conversione ADC

Supponendo che Arduino legga:
adcVL = 512
adcVR = 558

Con Vref = 5 V:

1) Convertire i valori in Volt.
2) Calcolare Vout.

---

## Esercizio 4 – Sensibilità locale

Vicino al punto di bilanciamento (10 kΩ), Rx varia da 10 kΩ a 10.5 kΩ.

Calcolare numericamente la variazione di Vout e stimare la sensibilità:

Sensibilità ≈ ΔVout / ΔRx

---

# 12. SOLUZIONI

## Soluzione Esercizio 1

Condizione di bilanciamento:

R1 / R2 = R3 / Rx

10 / 15 = 12 / Rx

Rx = (15 · 12) / 10

Rx = 18 kΩ

---

## Soluzione Esercizio 2

VL = 5 · (10 / 20) = 2.5 V

VR = 5 · (8 / 18)

VR = 5 · 0.4444 = 2.222 V

Vout = 2.5 − 2.222 = 0.278 V

---

## Soluzione Esercizio 3

Conversione in Volt:

VL = (512 · 5) / 1023 = 2.502 V

VR = (558 · 5) / 1023 = 2.728 V

Vout = 2.502 − 2.728 = −0.226 V

---

## Soluzione Esercizio 4

Calcolo per Rx = 10 kΩ:

VL = 2.5 V
VR = 2.5 V
Vout = 0 V

Calcolo per Rx = 10.5 kΩ:

VR = 5 · (10.5 / 20.5)

VR = 5 · 0.5122 = 2.561 V

Vout = 2.5 − 2.561 = −0.061 V

ΔVout ≈ −0.061 V
ΔRx = 0.5 kΩ

Sensibilità ≈ −0.061 / 0.5 = −0.122 V/kΩ

---

FINE DISPENSA


