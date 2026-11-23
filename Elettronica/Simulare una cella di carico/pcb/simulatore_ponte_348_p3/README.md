# Simulatore a ponte 348 Ω — revisione elettrica P3.1, PCB P3

La revisione P3.1 aumenta il margine di azzeramento usando **R6 = 56 kΩ 1%** e **R7/R8 = 909 Ω 0,1%**. Il multigiri RV1 resta da 200 Ω. Il PCB conserva piste, fori, dimensioni e serigrafia della P3: i nomi dei file terminano ancora in `_p3`, e sulla scheda resta scritto `REV P3`.

La [dispensa di laboratorio](../../dispensa_simulatore_ponte_348.html) contiene schema, calcoli aggiornati, procedure e limiti. La versione precedente, compreso il PDF dello schema con R6 = 71,5 kΩ, è in [archivio](../../archivio-2026-10-11/prima-miglioria-P3.1/). Non usare quel PDF per la distinta P3.1.

## Dati nominali

| Grandezza | Valore |
|---|---|
| Fondo scala, RV2 al centro | ±1,989 mV/V, circa ±4,27 milioni di conteggi HX711 a gain 128 |
| Impedenza d'uscita A+/A− | circa 340,53 Ω |
| Carico sull'eccitazione, entrambi i cursori al centro | 288,26 Ω, includendo RV2 |
| Corrente a 3,2 V / 5 V | 11,10 mA / 17,35 mA |
| Campo nominale dello zero | ±1,487 mV/V |
| Scheda | 51,5 × 36,5 mm, 2 strati, 1,6 mm |
| Piste / distanza minima impostata | 0,30 mm / 0,20 mm |

Valori calcolati, non misurati. Non linearità elettrica nominale: 0,044% del fondo scala positivo, oppure 0,022% dell'escursione totale. La linearità rispetto ai giri dipende anche da RV1, la cui sigla non è ancora disponibile.

## Componenti a foro acquistabili

| Rif. | Valore | Codice fabbricante |
|---|---|---|
| R1–R4 | 348 Ω 0,1%, 0,25 W | TE YR1B348RCC |
| R5 | 3,65 kΩ 0,1%, 0,25 W | TE YR1B3K65CC |
| R6 | 56 kΩ 1%, 0,25 W | Yageo MFR-25FRF52-56K |
| R7, R8 | 909 Ω 0,1%, 0,25 W | TE YR1B909RCC |
| R9, R10 | 0 Ω | Ponticelli a filo, passo 5,08 mm |
| RV1 | 200 Ω, 10 giri, lineare | Componente dell'utente; sigla e tolleranza da verificare |
| RV2 | 10 kΩ, 25 giri nominali | Bourns 3296W-1-103LF come riferimento |
| J1 | Connettore 1×6 | Passo 2,54 mm |

I valori 348 Ω, 3,65 kΩ e 909 Ω sono standard E96; 56 kΩ è E24. [Lista di acquisto con link](componenti_acquisto.csv) e [BOM di montaggio](simulatore_ponte_348_p3-bom.csv). Stock e consegna vanno ricontrollati all'ordine. I corpi dei resistori proposti sono compatibili con il passo di montaggio di 10,16 mm di R1–R8; i resistori sono adagiati sulla scheda, alcuni ruotati di 90° nel piano.

RV1 e RV2 hanno entrambi l'impronta **PinHeader_1x03_P2.54mm_Vertical**. Per RV1 usare tre fili; per RV2 controllare l'ingombro completo e l'orientamento del componente prima di saldarlo direttamente, oppure usare tre fili. Il rettangolo di serigrafia rappresenta il connettore, non il corpo del Bourns.

## Collegamenti

| Pin J1 | Segnale |
|---|---|
| 1 | EXC+ dal modulo, prima di R9 |
| 2 | SENSE+, nodo E+ del ponte dopo R9 |
| 3 | A+ |
| 4 | A− |
| 5 | SENSE−, nodo E− del ponte dopo R10 |
| 6 | EXC− dal modulo, prima di R10 |

RV1: 1 lato R7, 2 cursore, 3 lato R8. RV2: 1 E+, 2 cursore, 3 E−. Con HX711 lasciare i sense scollegati: collegarli ai morsetti di eccitazione può bypassare R9/R10 e falsare la prova del cavo. Con 1 Ω per filo l'errore di span è circa −0,689%; durante la prova conservare la stessa calibrazione.

## Verifiche e riproducibilità

Dalla cartella principale del progetto:

```sh
python3 verifiche/verifica_calcoli.py
python3 verifiche/verifica_pcb.py
python3 pcb/prepara_pacchetti.py
```

Il controllo statico confronta i file reali: 32 pin, 15 componenti inclusi i due fori, 23 segmenti e 2 vie. Connettività, valori e footprint di schema/PCB/legacy sono confrontati; i controlli geometrici Python sul modello coincidono con la geometria del PCB. Le verifiche ripetibili e i risultati sono nella cartella `verifiche/`.

La simulazione di 1024 combinazioni estreme delle tolleranze della P3.1 trova zero raggiungibile in tutti i casi esaminati, con almeno circa 0,440 mV/V di margine. Sono considerati anche corsa 1–99% e 110 Ω nel ramo di contatto di RV2; RV1 ±5% resta un'ipotesi. Questo campionamento non è una certificazione di tutti i componenti e condizioni operative.

**Controlli storici:** il README precedente riporta DRC KiCad 7.0.11 senza violazioni ed esportazione nativa di Gerber, fori, stampe e anteprime. **In questa revisione** KiCad non è disponibile: ERC/DRC nativi non sono stati rieseguiti. Non sono stati provati importazione EasyEDA, montaggio o funzionamento hardware.

I Gerber, i fori, le stampe 1:1 e le anteprime P3 restano applicabili: la revisione cambia soltanto valori e tolleranze dei componenti, non i livelli di fabbricazione. I file Gerber sono confrontati byte per byte con quelli archiviati. Prima della produzione restano da eseguire il controllo in KiCad e la revisione dell'anteprima del produttore.

## Modifica in KiCad ed esportazione

Aprire `simulatore_ponte_348_p3.kicad_pro`. La libreria locale `Simulatore.pretty` è registrata in `fp-lib-table`; simboli e footprint hanno UUID associati. Dopo modifiche allo schema aggiornare il PCB dallo schema e controllare reti e valori.

Lo script `../esporta_con_kicad.sh` esporta Gerber, fori, posizioni, stampe 1:1 e PDF dello schema quando KiCad è disponibile. Il PDF P3 precedente è stato archiviato: per la P3.1 usare lo schema KiCad e la figura 1 della dispensa finché non viene rigenerato e verificato il PDF.

Gli script `build_pcb_ponte_p3.py`, `build_sch_ponte_p3.py` e `build_easyeda_p3.py` ricreano i file dal modello Python: **sovrascrivono eventuali modifiche manuali**. Non usarli per esportare una scheda modificata nell'editor. `prepara_pacchetti.py` controlla la corrispondenza prima di aggiornare gli ZIP dai file già presenti.
