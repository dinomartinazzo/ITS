# Simulatore di cella di carico — ponte 348 Ω, PCB rev P3 (resistenze a foro)

Scheda a due strati, 51,5 × 36,5 mm, solo componenti a foro, disposta come lo schema su una griglia di 2,54 mm: due file di resistenze verticali tra le dorsali E+ (in alto) ed E− (in basso), J1 a sinistra, potenziometri a destra, tracce solo ortogonali e un unico attraversamento sul lato rame (A+ sotto il ramo A−, con due vie). Schema e calcoli: `../../dispensa_simulatore_ponte_348.html`.
Rigenerazione da zero: `python3 ../build_pcb_ponte_p3.py && python3 ../build_sch_ponte_p3.py` (nessuna dipendenza).

## Dati di progetto

| Grandezza | Valore |
|---|---|
| Fondo scala (RV1 agli estremi) | ±1,994 mV/V |
| Impedenza d'uscita A+/A− | ≈ 341 Ω |
| Carico sull'eccitazione | ≈ 297 Ω: ≈ 10,8 mA a 3,2 V, ≈ 16,8 mA a 5 V |
| Campo di regolazione dello zero (RV2) | ±1,21 mV/V |
| Offset iniziale, caso peggiore, R1–R4 allo 0,1% | ±1,0 mV/V |
| Dimensioni, strati, spessore | 51,5 × 36,5 mm, 2 strati, 1,6 mm |
| Piste, distanza minima | 0,3 mm, 0,2 mm |

## Componenti

| Rif. | Valore | Footprint |
|---|---|---|
| R1–R4 | 348 Ω 0,1%, stesso lotto | `R_Axial_DIN0207_P10.16mm_Rot90` (assiale in verticale) |
| R5 | 3,65 kΩ 0,1% | `R_Axial_DIN0207_P10.16mm_Horizontal` |
| R6 | 71,5 kΩ 1% | idem |
| R7, R8 | 909 Ω 1% | `R_Axial_DIN0207_P10.16mm_Rot90` |
| R9, R10 | ponticello a filo (0 Ω), da montare sempre | `R_Axial_DIN0207_P5.08mm_Horizontal` |
| RV1 | multigiri 200 Ω 10 giri (SPAN) | `PinHeader_1x03_P2.54mm_Vertical` |
| RV2 | 10 kΩ 25 giri (ZERO) | `Trimmer_1x03_P2.54mm_Vertical` |
| J1 | header 1×6 | `PinHeader_1x06_P2.54mm_Vertical` |

## Connessioni

| J1 | Segnale | RV1 | RV2 |
|---|---|---|---|
| 1 | EXC+ (verso il modulo, tramite R9) | 1 = lato R7 | 1 = E+ |
| 2 | SENSE+ (nodo E+ del ponte) | 2 = cursore | 2 = cursore |
| 3 | A+ | 3 = lato R8 | 3 = E− |
| 4 | A− | | |
| 5 | SENSE− (nodo E− del ponte) | | |
| 6 | EXC− (verso il modulo, tramite R10) | | |

Con l'HX711 si collegano EXC+, EXC−, A+, A−; SENSE+ e SENSE− restano liberi. Per simulare la resistenza del cavo sostituire R9 e R10 con 0,5–2 Ω (errore di span ≈ −2R/(297 + 2R)).

## Come modificarlo in KiCad

Aprire `simulatore_ponte_348_p3.kicad_pro` con KiCad 7 o superiore (progetto completo: schema `.kicad_sch` e scheda `.kicad_pcb`). I simboli sono quelli standard di KiCad (`Device:R`, `Device:R_Potentiometer`, `Connector_Generic:Conn_01x06`, `Mechanical:MountingHole`); i footprint sono nella libreria di progetto `Simulatore` (`Simulatore.pretty`, registrata in `fp-lib-table`). Lo schema usa etichette globali con gli stessi nomi di rete della scheda (E+, E−, EXC+, EXC−, A+, A−, W1, W2, N1, N2) e ogni simbolo è legato al proprio footprint (stesso UUID nel campo `path`): dopo una modifica allo schema usare *Strumenti → Aggiorna PCB dallo schema* (F8). Dopo le modifiche alla scheda eseguire `../esporta_con_kicad.sh` per rigenerare Gerber, fori, posizioni, stampe 1:1 e PDF dello schema.

## Verifiche eseguite

- Controllo regole di progetto (DRC) di KiCad 7.0.11 sul file definitivo: 0 violazioni, 0 pad non collegati, 0 errori sui footprint.
- Netlist esportata dallo schema con `kicad-cli` e confrontata con le reti della scheda: 32 pin su 32 uguali, stessi footprint assegnati, nessuna differenza.
- Gerber, fori, posizioni, stampe 1:1 e PDF dello schema esportati da `kicad-cli` 7.0.11 (script `../esporta_con_kicad.sh`, provato); anteprime renderizzate da KiCad e riviste.
- Il file `.kicad_pcb` è stato caricato e riscritto da `pcbnew` 7.0.11 (formato nativo).
- Regole di serigrafia (testo 1,0 mm, tratto 0,15 mm, distanza dai pad 0,15 mm) e fori di JLCPCB impostate nel progetto: DRC senza violazioni.

## Verifiche NON eseguite

- Il progetto non è stato aperto nell'interfaccia grafica di KiCad (ambiente senza schermo): solo `kicad-cli` e il modulo Python `pcbnew`.
- Controllo regole elettriche (ERC) dello schema non eseguito (non disponibile in `kicad-cli` 7): aprire lo schema, eseguire l'ERC e valutare eventuali avvisi sulle etichette globali.
- Nessuna scheda è stata costruita né misurata; i Gerber non sono stati verificati da un produttore.

## File

| File | Contenuto |
|---|---|
| `simulatore_ponte_348_p3.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, `.kicad_prl` | Progetto KiCad 7: schema e scheda |
| `fp-lib-table`, `Simulatore.pretty/` | Libreria dei footprint del progetto |
| `schema_elettrico.pdf` | Schema elettrico (A4) |
| `gerber/` | Gerber (rame, maschera, serigrafia, bordo), fori Excellon `.drl` e file di job |
| `stampa_1a1/` | Maschere in bianco e nero su A4 a scala 1:1 (rame lato componenti, lato saldature, lato saldature specchiato, serigrafia) |
| `anteprima_lato_componenti.png`, `anteprima_lato_saldature.png` | Anteprime |
| `simulatore_ponte_348_p3-bom.csv`, `-pos.csv` | Distinta componenti e posizioni |
| `../build_pcb_ponte_p3.py`, `../build_sch_ponte_p3.py`, `../simboli_kicad7.json` | Script che generano scheda e schema (simboli estratti da kicad-symbols 7.0.11, licenza CC-BY-SA 4.0 con eccezione per le librerie KiCad) |
| `../esporta_con_kicad.sh` | Esportazione con `kicad-cli` |
| `../jlcpcb/` | Gerber in ZIP per JLCPCB e checklist d'ordine (`ORDINE_JLCPCB.md`) |
| `../easyeda/` | ZIP per l'importazione in EasyEDA (formato KiCad 5.1 e altri) e istruzioni (`LEGGIMI_EASYEDA.md`); script `../build_easyeda_p3.py` |

Rigenerare con gli script riporta il progetto allo stato iniziale e cancella le modifiche fatte in KiCad: usarli solo per ripartire da zero.
