# Importazione in EasyEDA — simulatore cella di carico a ponte 348 Ω, revisione elettrica P3.1 su PCB P3

**Aggiornamento P3.1:** R6 = 56 kΩ 1%, R7/R8 = 909 Ω 0,1%; piste e fori P3 invariati. Schema, valori dei componenti e pacchetti sono aggiornati. I nomi dei file restano `_p3`. I controlli KiCad descritti sotto sono storici; nella revisione corrente sono stati ripetuti i controlli statici Python, non il DRC nativo.

Cartella con gli ZIP per l'importazione in EasyEDA (Standard, versione web, ed EasyEDA Pro). **Non sono stati provati in EasyEDA**: non ho accesso all'editor.

## Perché due formati KiCad

La documentazione ufficiale di EasyEDA dichiara l'importazione di KiCad fino alla serie 5: EasyEDA Standard «dalla 4.06», con l'avviso che dalla 5.1.3 il formato dei documenti è cambiato e l'importazione può fallire ([Import KiCAD](https://docs.easyeda.com/en/Import/Import-KiCAD)); EasyEDA Pro indica KiCad 5.1 e 5.9 ([Import KiCad](https://prodocs.easyeda.com/en/import-export/import-kicad/)). Il progetto è in KiCad 7, quindi ho preparato anche scheda e schema nel vecchio formato 5.1.

| ZIP | Contenuto | Uso |
|---|---|---|
| `easyeda_solo_pcb_kicad51.zip` | scheda in formato KiCad 5.1 (`.kicad_pcb`) | **Prima scelta** per EasyEDA Standard: la guida dice di comprimere solo il file PCB |
| `easyeda_progetto_kicad51.zip` | schema `.sch` (v4) + `-cache.lib` + scheda `.kicad_pcb` + `.pro` | Per importare anche lo schema |
| `easyeda_gerber.zip` | Gerber e fori (gli stessi di JLCPCB) | Ripiego: importazione dei Gerber, senza reti né componenti |
| `easyeda_progetto_kicad7_non_dichiarato.zip` | progetto KiCad 7 completo con la libreria `Simulatore.pretty` | Solo se la tua versione di EasyEDA accetta KiCad 6/7 (non dichiarato dalla documentazione) |

I file sciolti (`.kicad_pcb`, `.sch`, `-cache.lib`, `.pro`) sono quelli contenuti negli ZIP.

## Procedura

1. Aprire EasyEDA Standard (web) o EasyEDA Pro e scegliere l'importazione di KiCad (nella guida: sezione «Import», voce «Import KiCAD»; per Pro dalla pagina iniziale). I nomi dei menu possono variare con la versione: la guida non li riporta.
2. Selezionare uno ZIP dalla tabella, in quest'ordine: `easyeda_solo_pcb_kicad51.zip`, poi `easyeda_progetto_kicad51.zip`, poi `easyeda_gerber.zip`.
3. Dopo l'importazione controllare: sagoma 51,5 × 36,5 mm; 15 componenti (R1–R10, RV1, RV2, J1, due fori); le reti E+, E−, EXC+, EXC−, A+, A−, W1, W2, N1, N2; le due vie; la serigrafia.
4. Le regole di progetto (design rules) non vengono importate ([guida](https://docs.easyeda.com/en/Import/Import-KiCAD)): impostare a mano distanza minima 0,2 mm e pista 0,3 mm.
5. Per ordinare, il percorso più sicuro resta caricare su JLCPCB i Gerber di `../jlcpcb/`, già controllati con il DRC di KiCad (vedi `../jlcpcb/ORDINE_JLCPCB.md`), invece di esportarli di nuovo da EasyEDA.

## Verifiche eseguite

- Scheda 5.1: ricaricata con `pcbnew` 7.0.11; pad, reti, posizioni, piste e vie coincidono con la scheda KiCad 7; DRC senza violazioni (a parte l'avviso sulla libreria `Simulatore`, assente nell'ambiente di prova).
- Schema 5.1: connettività ricostruita con un controllo indipendente (parser dei file `.sch` e `-cache.lib`) e confrontata con le reti della scheda: 32 pin su 32 uguali. KiCad 7 non legge più il formato legacy da riga di comando: il file non è stato aperto né in KiCad né in EasyEDA.

## Non verificato

- Qualunque importazione in EasyEDA (Standard o Pro).
- Il rendering dei simboli dello schema legacy e l'apertura in KiCad 5.
- Il comportamento di EasyEDA con i footprint personalizzati (`Simulatore:*`) e con le etichette globali.

Per aggiornare gli ZIP dopo una modifica coerente dei file: dalla cartella principale eseguire `python3 pcb/prepara_pacchetti.py`. Lo script controlla schema, PCB e legacy prima di creare i pacchetti. `build_easyeda_p3.py` genera invece dal modello Python e può perdere modifiche fatte manualmente in KiCad.
