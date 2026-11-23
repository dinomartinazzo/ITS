# Ordine su JLCPCB — simulatore cella di carico a ponte 348 Ω, rev P3

**Montaggio P3.1:** usare la distinta aggiornata con R6 = 56 kΩ 1% e R7/R8 = 909 Ω 0,1%. Il PCB e i Gerber P3 sono invariati; il precedente DRC KiCad è un controllo storico e non è stato rieseguito nella revisione corrente. I controlli geometrici Python sono stati ripetuti.

File da caricare su jlcpcb.com (Order now → Add gerber file): **`simulatore_ponte_348_p3_gerber_JLCPCB.zip`**
(Gerber di rame, maschera, serigrafia e bordo, più fori `PTH` e `NPTH` separati; esportati da KiCad 7.0.11 con `esporta_con_kicad.sh`).

## Parametri consigliati

| Campo | Valore | Note |
|---|---|---|
| Base material | FR-4 | |
| Layers | 2 | |
| Dimensions | 51,5 × 36,5 mm | Il sito la legge dal bordo; controllare che coincida |
| PCB qty | 5 (minimo del sito) | |
| Thickness | 1,6 mm | |
| PCB color | Verde (o a scelta) | Disponibili anche viola, rosso, giallo, blu, bianco, nero |
| Silkscreen | Bianco | |
| Surface finish | HASL senza piombo | In alternativa HASL con piombo (più economico) o ENIG: per saldare a mano a foro va bene l'HASL |
| Outer copper weight | 1 oz | |
| Via covering | Tenting (predefinito) | Le due vie sono da 0,9/0,4 mm |
| Impedance, castellated holes, edge plating | No | |

I nomi esatti dei campi possono cambiare: sono indicativi.

## Confronto con le capacità di JLCPCB (2 strati, 1 oz)

Valori JLCPCB letti il 11/10/2026 su https://jlcpcb.com/capabilities/pcb-capabilities; valori della scheda misurati sul progetto.

| Grandezza | JLCPCB | Scheda | Esito |
|---|---|---|---|
| Larghezza pista | min 0,10 mm | 0,30 mm | ok |
| Distanza rame-rame | min 0,10 mm | min 0,84 mm | ok |
| Distanza rame-bordo | min 0,20 mm | min 2,15 mm | ok |
| Foro PTH | min 0,15 mm | 0,4 (vie), 0,8 e 1,0 mm | ok |
| Foro NPTH | min 0,50 mm | 2,7 mm (due fori M2,5) | ok |
| Anello anulare PTH | raccomandato 0,25 mm (minimo 0,18) | pad ≥ 0,35 mm, vie 0,25 mm | ok |
| Via | diametro > foro di almeno 0,1 mm | 0,9 / 0,4 mm | ok |
| Serigrafia: linea | min 0,15 mm | 0,15 mm | ok |
| Serigrafia: altezza testo | min 1,0 mm | 1,0 mm | ok al limite |
| Serigrafia: distanza dai pad | min 0,15 mm | controllata dal DRC di KiCad | ok |
| Dimensione scheda | min 3 × 3 mm | 51,5 × 36,5 mm | ok |

## Verifiche eseguite

- DRC di KiCad 7.0.11 sulla scheda, con le regole di serigrafia e fori di JLCPCB impostate nel progetto: 0 violazioni.
- Bordo letto dal Gerber `Edge_Cuts`: 51,50 × 36,50 mm.
- Fori: `PTH.drl` con utensili 0,4 / 0,8 / 1,0 mm; `NPTH.drl` con 2,7 mm.

## Da controllare prima di pagare

1. Nell'anteprima Gerber di JLCPCB: sagoma 51,5 × 36,5 mm, due fori grandi agli angoli superiore e inferiore sinistro, serigrafia leggibile (J1, R1…R10, SPAN, ZERO).
2. Dopo l'ordine, controllare il numero d'ordine che JLCPCB stampa sulla scheda (di norma sulla serigrafia o sul rame, in zona libera).

## Non verificato

- I Gerber non sono stati controllati da JLCPCB né in un visualizzatore diverso da KiCad.
- Nessuna scheda è stata prodotta; prezzi e tempi non verificati.
- I componenti sono tutti a foro e vanno saldati a mano: l'assemblaggio SMD di JLCPCB non è applicabile.
