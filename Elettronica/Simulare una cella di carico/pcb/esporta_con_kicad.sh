#!/usr/bin/env bash
# esporta_con_kicad.sh — esporta con kicad-cli (KiCad 7 o superiore) i file di fabbricazione e di consultazione
# del simulatore a ponte 348 ohm: Gerber, fori Excellon, posizioni, stampe 1:1 e PDF dello schema.
# Uso (Su questo PC, dopo aver modificato il progetto in KiCad):  ./esporta_con_kicad.sh [cartella_progetto]
set -uo pipefail

# Se lanciato con un doppio click da file manager, il terminale si chiuderebbe
# subito alla fine dello script: questo trap lo tiene aperto fino a un invio,
# qualunque sia il punto di uscita (successo, errore, annullamento).
if [[ -t 0 && -t 1 ]]; then
  trap 'read -rp "Premi INVIO per chiudere..." _' EXIT
fi

NOME="simulatore_ponte_348_p3"
DIR="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$NOME}"
PCB="$DIR/$NOME.kicad_pcb"
SCH="$DIR/$NOME.kicad_sch"
ok=0; err=0

if ! command -v kicad-cli >/dev/null 2>&1; then
  echo "kicad-cli non trovato: installare KiCad (sudo apt install kicad) e riprovare." >&2
  exit 1
fi
[[ -f "$PCB" ]] || { echo "File non trovato: $PCB" >&2; exit 1; }

passo() {   # passo "descrizione" comando...
  local d="$1"; shift
  if "$@" >/dev/null 2>&1; then echo "  ok   $d"; ok=$((ok + 1)); else echo "  ERRORE  $d" >&2; err=$((err + 1)); fi
}

echo "Esportazione di $NOME in $DIR"
rm -rf "$DIR/gerber" "$DIR/stampa_1a1"; mkdir -p "$DIR/gerber" "$DIR/stampa_1a1"
# Gerber: rame, maschera, serigrafia, bordo (nomi canonici dei layer)
passo "Gerber"        kicad-cli pcb export gerbers --layers "F.Cu,B.Cu,F.Mask,B.Mask,F.SilkS,B.SilkS,Edge.Cuts" -o "$DIR/gerber/" "$PCB"
passo "Fori Excellon" kicad-cli pcb export drill --format excellon --drill-origin absolute --excellon-units mm --excellon-separate-th -o "$DIR/gerber/" "$PCB"
passo "Posizioni"     kicad-cli pcb export pos --format csv --units mm -o "$DIR/$NOME-pos.csv" "$PCB"
# Stampe 1:1 su A4 (stampare al 100%, senza adattare alla pagina)
passo "Rame lato componenti"          kicad-cli pcb export pdf --layers "F.Cu,Edge.Cuts" --black-and-white -o "$DIR/stampa_1a1/rame_F_Cu.pdf" "$PCB"
passo "Rame lato saldature"           kicad-cli pcb export pdf --layers "B.Cu,Edge.Cuts" --black-and-white -o "$DIR/stampa_1a1/rame_B_Cu.pdf" "$PCB"
passo "Rame lato saldature specchiato" kicad-cli pcb export pdf --layers "B.Cu,Edge.Cuts" --black-and-white --mirror -o "$DIR/stampa_1a1/rame_B_Cu_SPECCHIATO.pdf" "$PCB"
passo "Serigrafia lato componenti"    kicad-cli pcb export pdf --layers "F.SilkS,Edge.Cuts" --black-and-white -o "$DIR/stampa_1a1/serigrafia_lato_componenti.pdf" "$PCB"
if [[ -f "$SCH" ]]; then
  passo "PDF dello schema"  kicad-cli sch export pdf -o "$DIR/schema_elettrico.pdf" "$SCH"
fi

echo
echo "Riepilogo: $ok esportazioni riuscite, $err fallite."
echo "File scritti in: $DIR/gerber, $DIR/stampa_1a1, $DIR/$NOME-pos.csv"
echo "Da verificare: controllo regole di progetto (DRC) in KiCad prima di ordinare, e i Gerber in un visualizzatore."
[[ $err -eq 0 ]]
