# Filtri elettronici attivi e passivi

Dispensa di laboratorio (stile «Dispensa di laboratorio», livello ITS, dalle basi) su filtri RC, RLC e
Sallen-Key: 25 capitoli e 4 appendici, circa 24 000 parole, 87 figure, esempi svolti, riepiloghi, domande di
controllo, 31 esercizi con svolgimento, valori attesi calcolati e procedure di misura. La dispensa non
contiene codice né simulazioni.

## Contenuto

| Percorso | Ruolo |
|---|---|
| `dispensa_filtri_attivi_passivi.html` | Dispensa finale, HTML autosufficiente con tema chiaro/scuro |
| `src/filtri_core.py` | Calcolo: funzioni di trasferimento, modello nodale Sallen-Key, Butterworth/Chebyshev/Bessel (poli e polinomi), gradino e impulso, ritardo di gruppo, ordine minimo, progetto a cascata |
| `src/serie.py` | Configurazione: serie E12, E24, E96 |
| `src/filtri_cli.py` | Interfaccia a riga di comando (`rc`, `sk`, `butter`) |
| `tests/test_filtri.py` | 55 test (`unittest`) |
| `dispensa/template.html` | Struttura della pagina e indice; include i capitoli |
| `dispensa/capitoli/*.html` | Testo: `00-intro`, `01a/01b-base` (teoria di base), `02-passivi`, `03-attivi` (+ `03b-famiglie`), `04-progetto`, `05-appendici` |
| `dispensa/build_dispensa.py` | Generatore: unisce template, capitoli, figure, tabelle ed esercizi; numera capitoli, equazioni e figure |
| `dispensa/parametri.py` | Valori degli esempi (R, C, L, frequenze) |
| `dispensa/formati.py`, `disegno.py`, `disegno_didattico.py`, `disegno_base.py`, `disegno_famiglie.py` | Formattazione, grafici di Bode, schemi e diagrammi didattici (SVG) |
| `dispensa/contenuti_base.py`, `contenuti_nuovi.py`, `contenuti_teoria.py`, `contenuti_famiglie.py`, `esercizi.py` | Tabelle, didascalie ed esercizi calcolati dal motore |
| `dispensa/stile.css`, `extra.css`, `script.js` | Stile e comportamento (da riferimento «celle di carico» + aggiunte) |
| `dispensa/stampa.css`, `crea_pdf.py` | CSS di stampa (A4) e produzione del PDF |
| `dispensa_filtri_attivi_passivi.pdf` | PDF finale: copertina, indice con numeri di pagina, segnalibri, metadati |

## Uso

Solo libreria standard di Python 3, nessuna dipendenza. Dalla radice del progetto:

```bash
python3 -m unittest discover -s tests -v
python3 dispensa/build_dispensa.py       # rigenera la dispensa HTML
python3 dispensa/crea_pdf.py             # produce il PDF (richiede Google Chrome, pdftotext e pikepdf)
python3 src/filtri_cli.py butter --n 4 --fc 1k --c 10n
```

## Note per chi modifica

- Ogni numero nelle tabelle, nelle figure e negli esercizi viene da `filtri_core.py`; per cambiare un
  esempio modificare `dispensa/parametri.py` e rigenerare. Il builder si ferma se resta un segnaposto.
- Nei capitoli i caratteri speciali si scrivono come `\uXXXX` oppure direttamente; titoli di capitolo
  `<span class="num">#</span>` (appendici `@`) e equazioni `(@nome)` sono numerati dal builder; i rimandi
  si scrivono `{{cap:id}}`, `{{eq:nome}}`: nessun numero a mano. Le figure sono numerate in ordine di apparizione. Nelle etichette SVG usare `<sub>…</sub>`, che `svgt()` converte in pedici SVG: un tag HTML
  dentro un `<text>` farebbe uscire il parser dall'SVG.
- Font (Google Fonts) caricati dalla rete; offline la pagina usa i font di sistema.
- Nessuna misura di laboratorio è riportata: i valori attesi sono calcolati con componenti nominali.
- Riferimenti: TI SLOA049B, SLOA024B, SLOD006B (appendice D della dispensa).
