"""Crea il PDF della dispensa: HTML con CSS di stampa -> Chrome headless -> copertina + corpo + segnalibri.

Uso (dalla radice del progetto, dopo `python3 dispensa/build_dispensa.py`):

    python3 dispensa/crea_pdf.py

Metodo:
 1. dall'HTML finale si ricava una variante per il PDF: soluzioni e risposte aperte, indice con numeri
    di pagina, un marcatore invisibile all'inizio di ogni parte e capitolo;
 2. prima passata: Chrome produce il PDF e dai marcatori si leggono le pagine di ogni capitolo;
 3. seconda passata: l'indice viene riempito con i numeri di pagina e il PDF è rigenerato (la pagina di
    ogni capitolo deve restare invariata);
 4. la copertina è un PDF separato a pagina piena (Chrome ignora @page :first con margine zero);
 5. copertina e corpo sono uniti con pikepdf, che aggiunge segnalibri e metadati.
"""
import html as html_lib
import os
import re
import shutil
import subprocess
import sys
import tempfile

import pikepdf

AQUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

HTML_IN = os.path.join(RADICE, "dispensa_filtri_attivi_passivi.html")
PDF_OUT = os.path.join(RADICE, "dispensa_filtri_attivi_passivi.pdf")
CHROME = shutil.which("google-chrome") or "/usr/bin/google-chrome"

TITOLO = "Filtri elettronici passivi e attivi — dalle basi al progetto"
SOTTOTITOLO = "RC, RLC e Sallen-Key"
AUTORE = "Dino Martinazzo"
OGGETTO = "Dispensa di laboratorio per ITS: teoria di base, filtri passivi e attivi, progetto e verifica"
PAROLE_CHIAVE = "filtri, RC, RLC, Sallen-Key, Butterworth, Chebyshev, Bessel, anti-aliasing, elettronica analogica"


# ---------------------------------------------------------------------------------------------
# HTML per il PDF
# ---------------------------------------------------------------------------------------------

def struttura(html):
    """Elenco di (id, tipo, etichetta, titolo) per parti e capitoli, nell'ordine del documento."""
    voci = []
    schema = re.compile(
        r'<div class="part[^"]*" id="([^"]+)"><span>([^<]*)</span><h2 class="part-title">(.*?)</h2>'
        r'|<section id="([^"]+)"[^>]*>\s*<h2><span class="num">([^<]+)</span>(.*?)</h2>', re.S)
    for m in schema.finditer(html):
        if m.group(1):
            voci.append((m.group(1), "parte", m.group(2), _testo(m.group(3))))
        else:
            voci.append((m.group(4), "capitolo", m.group(5), _testo(m.group(6))))
    return voci


def _testo(frammento):
    return html_lib.unescape(re.sub(r"<[^>]+>", "", frammento)).strip()


def indice_html(voci, pagine):
    righe = []
    for ident, tipo, etichetta, titolo in voci:
        pg = pagine.get(ident, 0)
        if tipo == "parte":
            righe.append(f'<li class="p"><span class="t">{html_lib.escape(etichetta)} — {html_lib.escape(titolo)}</span>'
                         f'<span class="d"></span><span class="pg"><a href="#{ident}">{pg}</a></span></li>')
        else:
            righe.append(f'<li><span class="n0">{html_lib.escape(etichetta)}</span><span class="t"><a href="#{ident}">{html_lib.escape(titolo)}</a></span>'
                         f'<span class="d"></span><span class="pg">{pg}</span></li>')
    return '<section id="indice-pdf" class="toc-pdf"><h2>Indice</h2><ul>' + "".join(righe) + "</ul></section>"


def prepara_html(html, voci, pagine, marcatori=True):
    """Variante per il PDF: risposte aperte, indice con numeri, marcatori di pagina (facoltativi)."""
    html = html.replace('<details class="sv">', '<details class="sv" open>')
    for ident, _, _, _ in voci if marcatori else []:
        marcatore = f'<span class="pdfmark">@@{ident}@@</span>'
        html = re.sub(rf'(<section id="{re.escape(ident)}"[^>]*>)', r"\1" + marcatore, html, count=1)
        html = re.sub(rf'(<div class="part[^"]*" id="{re.escape(ident)}">)', r"\1" + marcatore, html, count=1)
    html = html.replace("<main>", "<main>\n" + indice_html(voci, pagine), 1)
    return html


# ---------------------------------------------------------------------------------------------
# Chrome e lettura delle pagine
# ---------------------------------------------------------------------------------------------

def chrome_pdf(percorso_html, percorso_pdf):
    comando = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
               "--virtual-time-budget=30000", f"--print-to-pdf={percorso_pdf}", "file://" + percorso_html]
    subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    if not os.path.exists(percorso_pdf) or os.path.getsize(percorso_pdf) < 10000:
        raise RuntimeError("Chrome non ha prodotto un PDF valido")


def pagine_marcatori(percorso_pdf, voci):
    """Pagina (1-based) di ciascun marcatore, letta dal testo del PDF."""
    testo = subprocess.run(["pdftotext", percorso_pdf, "-"], check=True, capture_output=True, text=True).stdout
    pagine, risultato = testo.split("\f"), {}
    for ident, _, _, _ in voci:
        chiave = f"@@{ident}@@"
        for numero, contenuto in enumerate(pagine, 1):
            if chiave in contenuto:
                risultato[ident] = numero
                break
        else:
            raise RuntimeError(f"Marcatore non trovato nel PDF: {ident}")
    return risultato


def verifica_titoli(percorso_pdf, voci, pagine):
    """Controlla che il titolo di ogni parte/capitolo compaia nella pagina registrata (PDF senza marcatori)."""
    testo = subprocess.run(["pdftotext", percorso_pdf, "-"], check=True, capture_output=True, text=True).stdout.split("\f")
    norm = lambda s: re.sub(r"\s+", " ", s).lower()  # noqa: E731
    errori = []
    for ident, _, _, titolo in voci:
        if norm(titolo) not in norm(testo[pagine[ident] - 1]):
            errori.append((ident, pagine[ident]))
    if errori:
        raise RuntimeError(f"Titoli non trovati nella pagina attesa: {errori}")


# ---------------------------------------------------------------------------------------------
# Copertina
# ---------------------------------------------------------------------------------------------

def copertina_html():
    from disegno import hero_art
    with open(os.path.join(AQUI, "stile.css"), encoding="utf-8") as fh:
        stile = fh.read()
    arte = hero_art()
    return f"""<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"><title>Copertina</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500&display=swap" rel="stylesheet">
<style>{stile}
@page{{size:A4;margin:0}}
html,body{{margin:0;padding:0;background:#0f1318;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.copertina{{box-sizing:border-box;width:210mm;height:296.5mm;padding:30mm 22mm 24mm;color:#f1ede4;display:flex;flex-direction:column;justify-content:space-between;background:#0f1318}}
.copertina .kicker{{font:500 12pt var(--mono);color:#e3a33b;margin:0 0 10mm;letter-spacing:.02em}}
.copertina h1{{font:500 46pt/1.04 var(--serif);font-variation-settings:"opsz" 144;letter-spacing:-.015em;margin:0 0 8mm;color:#f1ede4}}
.copertina .sotto{{font:400 17pt/1.5 var(--sans);color:#a5a9b0;margin:0;max-width:130mm}}
.copertina .arte{{margin:6mm 0}}
.copertina .arte svg{{width:100%;height:auto;max-height:90mm}}
.copertina .piede{{border-top:1px solid #2a3038;padding-top:6mm;display:flex;justify-content:space-between;font:400 10.5pt var(--sans);color:#a5a9b0}}
.copertina .piede b{{display:block;font:500 11pt var(--mono);color:#f1ede4;margin-top:1mm}}
</style></head><body><div class="copertina">
<div><p class="kicker">Dispensa di laboratorio — elettronica analogica</p><h1>Filtri elettronici<br>passivi e attivi</h1><p class="sotto">Dalle basi al progetto: corrente, condensatore, sinusoide, numeri complessi e decibel; poi filtri RC, RLC e Sallen-Key, fino al filtro anti-aliasing.</p></div>
<div class="arte">{arte}</div>
<div class="piede"><div>Autore<b>{AUTORE}</b></div><div>Livello<b>dal primo anno ITS</b></div><div>Circuiti<b>{SOTTOTITOLO}</b></div><div>Edizione<b>ottobre 2026</b></div></div>
</div></body></html>"""


# ---------------------------------------------------------------------------------------------
# Unione, segnalibri, metadati
# ---------------------------------------------------------------------------------------------

def unisci(cop, corpo, voci, pagine, destinazione):
    with pikepdf.open(cop) as pdf_cop, pikepdf.open(corpo) as pdf_corpo:
        if len(pdf_cop.pages) != 1:
            raise RuntimeError(f"La copertina ha {len(pdf_cop.pages)} pagine invece di una")
        finale = pikepdf.Pdf.new()
        finale.pages.extend(pdf_cop.pages)
        finale.pages.extend(pdf_corpo.pages)
        offset = len(pdf_cop.pages)  # le pagine del corpo iniziano dopo la copertina
        with finale.open_outline() as outline:
            outline.root.append(pikepdf.OutlineItem("Copertina", 0))
            outline.root.append(pikepdf.OutlineItem("Indice", offset))
            corrente = None
            for ident, tipo, etichetta, titolo in voci:
                pagina = pagine[ident] - 1 + offset
                if tipo == "parte":
                    corrente = pikepdf.OutlineItem(f"{etichetta} — {titolo}", pagina)
                    outline.root.append(corrente)
                else:
                    voce = pikepdf.OutlineItem(f"{etichetta}  {titolo}", pagina)
                    (corrente.children if corrente is not None else outline.root).append(voce)
        with finale.open_metadata(set_pikepdf_as_editor=False) as meta:
            meta["dc:title"] = TITOLO
            meta["dc:creator"] = [AUTORE]
            meta["dc:description"] = OGGETTO
            meta["dc:language"] = ["it"]
            meta["pdf:Keywords"] = PAROLE_CHIAVE
        finale.docinfo["/Title"] = TITOLO
        finale.docinfo["/Author"] = AUTORE
        finale.docinfo["/Subject"] = OGGETTO
        finale.docinfo["/Keywords"] = PAROLE_CHIAVE
        finale.docinfo["/Creator"] = "HTML con CSS di stampa, resa con Google Chrome"
        finale.Root.PageMode = pikepdf.Name.UseOutlines
        finale.Root.Lang = pikepdf.String("it")
        finale.save(destinazione)
        return len(finale.pages)


# ---------------------------------------------------------------------------------------------
# Programma principale
# ---------------------------------------------------------------------------------------------

def main():
    if not os.path.exists(HTML_IN):
        sys.exit("Manca la dispensa HTML: eseguire prima dispensa/build_dispensa.py")
    with open(HTML_IN, encoding="utf-8") as fh:
        html = fh.read()
    voci = struttura(html)
    print(f"Struttura: {len(voci)} voci (parti e capitoli)")

    with tempfile.TemporaryDirectory(prefix="pdf-dispensa-") as tmp:
        html_corpo = os.path.join(tmp, "corpo.html")
        pdf_corpo = os.path.join(tmp, "corpo.pdf")

        # passata 1: numeri di pagina provvisori
        with open(html_corpo, "w", encoding="utf-8") as fh:
            fh.write(prepara_html(html, voci, {}))
        chrome_pdf(html_corpo, pdf_corpo)
        pagine1 = pagine_marcatori(pdf_corpo, voci)

        # passata 2: indice definitivo; la paginazione non deve cambiare
        with open(html_corpo, "w", encoding="utf-8") as fh:
            fh.write(prepara_html(html, voci, pagine1))
        chrome_pdf(html_corpo, pdf_corpo)
        pagine2 = pagine_marcatori(pdf_corpo, voci)
        if pagine1 != pagine2:
            diff = {k: (pagine1[k], pagine2[k]) for k in pagine1 if pagine1[k] != pagine2[k]}
            raise RuntimeError(f"La paginazione è cambiata tra le due passate: {diff}")
        print(f"Corpo: {len(pagine2)} marcatori, paginazione stabile")

        # passata finale senza marcatori (il testo nascosto inquinerebbe ricerca e copia); si verifica che
        # ogni titolo stia nella pagina registrata
        with open(html_corpo, "w", encoding="utf-8") as fh:
            fh.write(prepara_html(html, voci, pagine2, marcatori=False))
        chrome_pdf(html_corpo, pdf_corpo)
        verifica_titoli(pdf_corpo, voci, pagine2)
        print("Corpo finale senza marcatori: titoli verificati nelle pagine registrate")

        # copertina
        html_cop = os.path.join(tmp, "copertina.html")
        pdf_cop = os.path.join(tmp, "copertina.pdf")
        with open(html_cop, "w", encoding="utf-8") as fh:
            fh.write(copertina_html())
        chrome_pdf(html_cop, pdf_cop)

        n = unisci(pdf_cop, pdf_corpo, voci, pagine2, PDF_OUT)
        os.chmod(PDF_OUT, 0o664)
    print(f"Scritto {PDF_OUT}: {n} pagine, {os.path.getsize(PDF_OUT) / 1024 / 1024:.1f} MiB")


if __name__ == "__main__":
    main()
