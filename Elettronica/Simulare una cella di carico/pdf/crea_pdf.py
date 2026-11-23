"""Crea il PDF della dispensa: HTML con CSS di stampa -> Chrome headless -> copertina + corpo + segnalibri.

Uso (da qualunque cartella):

    uv run --with pikepdf python "pdf/crea_pdf.py"

Il sorgente `dispensa_simulatore_ponte_348.html` non viene modificato. Metodo:
 1. dall'HTML si ricava una variante per la stampa: tema chiaro, senza intestazione, indice laterale e script;
    soluzioni aperte; indice con numeri di pagina; un marcatore invisibile all'inizio di ogni parte e capitolo;
 2. prima passata: Chrome produce il PDF e dai marcatori si leggono le pagine di ogni capitolo;
 3. seconda passata: l'indice viene riempito e il PDF rigenerato (la paginazione deve restare identica);
 4. passata finale senza marcatori; si verifica che ogni titolo stia nella pagina registrata;
 5. la copertina (l'intestazione scura dell'HTML) è un PDF separato a pagina piena a margine zero, perché
    Chrome ignora `@page :first` con margine zero;
 6. copertina e corpo sono uniti con pikepdf, che aggiunge segnalibri e metadati.
"""
import html as html_lib
import os
import re
import subprocess
import sys
import tempfile

import pikepdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import configurazione as cfg  # noqa: E402


# ---------------------------------------------------------------------------------------------
# Struttura del documento
# ---------------------------------------------------------------------------------------------

def struttura(html):
    """Elenco di (id, tipo, etichetta, titolo) per parti e capitoli, nell'ordine del documento."""
    voci = []
    schema = re.compile(
        r'<div class="part[^"]*" id="([^"]+)"[^>]*><span[^>]*>([^<]*)</span><h2 class="part-title">(.*?)</h2>'
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
    """Sezione dell'indice con i numeri di pagina fisici (la copertina è la pagina 1)."""
    righe = []
    for ident, tipo, etichetta, titolo in voci:
        pg = pagine.get(ident, 0) + (cfg.PAGINE_COPERTINA if ident in pagine else 0)
        if tipo == "parte":
            righe.append(f'<li class="p"><span class="t"><a href="#{ident}">{html_lib.escape(etichetta)} — '
                         f'{html_lib.escape(titolo)}</a></span><span class="d"></span><span class="pg">{pg}</span></li>')
        else:
            righe.append(f'<li><span class="n0">{html_lib.escape(etichetta)}</span><span class="t">'
                         f'<a href="#{ident}">{html_lib.escape(titolo)}</a></span>'
                         f'<span class="d"></span><span class="pg">{pg}</span></li>')
    return '<section id="indice-pdf" class="toc-pdf"><h2>Indice</h2><ul>' + "".join(righe) + "</ul></section>"


def prepara_html(html, voci, pagine, css_stampa, marcatori=True):
    """Variante per il PDF: tema chiaro, senza hero/indice laterale/script, risposte aperte, indice, marcatori."""
    html = html.replace('<html lang="it">', '<html lang="it" data-theme="light">', 1)
    html = re.sub(r'<header class="hero">.*?</header>', "", html, count=1, flags=re.S)
    html = re.sub(r'<aside class="toc">.*?</aside>', "", html, count=1, flags=re.S)
    html = re.sub(r"<script>.*?</script>", "", html, flags=re.S)
    html = html.replace('<details class="file"', '<details class="file" open')
    html = html.replace("</head>", f"<style>\n{css_stampa}\n</style>\n</head>", 1)
    for ident, _, _, _ in voci if marcatori else []:
        marcatore = f'<span class="pdfmark">@@{ident}@@</span>'
        html = re.sub(rf'(<section id="{re.escape(ident)}"[^>]*>)', r"\1" + marcatore, html, count=1)
        html = re.sub(rf'(<div class="part[^"]*" id="{re.escape(ident)}"[^>]*>)', r"\1" + marcatore, html, count=1)
    return html.replace("<main>", "<main>\n" + indice_html(voci, pagine), 1)


# ---------------------------------------------------------------------------------------------
# Chrome e lettura delle pagine
# ---------------------------------------------------------------------------------------------

def chrome_pdf(percorso_html, percorso_pdf):
    comando = [cfg.CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
               "--virtual-time-budget=30000", f"--print-to-pdf={percorso_pdf}", "file://" + percorso_html]
    subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   timeout=cfg.TIMEOUT_CHROME)
    if not os.path.exists(percorso_pdf) or os.path.getsize(percorso_pdf) < 10000:
        raise RuntimeError("Chrome non ha prodotto un PDF valido")


def testo_pagine(percorso_pdf):
    uscita = subprocess.run(["pdftotext", percorso_pdf, "-"], check=True, capture_output=True, text=True).stdout
    return uscita.split("\f")


def pagine_marcatori(percorso_pdf, voci):
    """Pagina (1-based, del solo corpo) di ciascun marcatore, letta dal testo del PDF."""
    pagine, risultato = testo_pagine(percorso_pdf), {}
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
    testo = testo_pagine(percorso_pdf)
    norm = lambda s: re.sub(r"\s+", " ", s).lower()  # noqa: E731
    errori = [(i, pagine[i]) for i, _, _, titolo in voci if norm(titolo) not in norm(testo[pagine[i] - 1])]
    if errori:
        raise RuntimeError(f"Titoli non trovati nella pagina attesa: {errori}")


# ---------------------------------------------------------------------------------------------
# Copertina: l'intestazione scura dell'HTML a pagina piena
# ---------------------------------------------------------------------------------------------

CSS_COPERTINA = """
@page{size:A4;margin:0}
html,body{margin:0;padding:0;background:#0f1318;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.hero{box-sizing:border-box;width:210mm;height:296.5mm;display:flex;align-items:center}
.hero-in{box-sizing:border-box;width:100%;max-width:none;margin:0;display:flex;flex-direction:column;
  align-items:stretch;gap:14mm;padding:24mm 20mm}
.kicker{font-size:11pt;margin:0 0 8mm}
.hero h1{font-size:38pt;margin:0 0 8mm}
.hero .lead{font-size:12.5pt;max-width:none;margin:0 0 9mm}
.meta{gap:6mm 12mm;padding-top:6mm}
.meta dt{font-size:9pt}
.meta dd{font-size:10.5pt}
.hero-art{width:140mm;margin:0 auto}
"""


def copertina_html(html):
    stile = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    hero = re.search(r'<header class="hero">.*?</header>', html, re.S).group(0)
    anteprima = re.search(r'<link href="https://fonts.googleapis.com[^>]*>', html).group(0)
    return (f'<!DOCTYPE html><html lang="it" data-theme="light"><head><meta charset="utf-8">'
            f"<title>Copertina</title>{anteprima}<style>{stile}\n{CSS_COPERTINA}</style></head>"
            f"<body>{hero}</body></html>")


# ---------------------------------------------------------------------------------------------
# Unione, segnalibri, metadati
# ---------------------------------------------------------------------------------------------

def risolvi_collegamenti(pdf, pagine, offset):
    """Chrome lascia nei collegamenti interni il solo nome della destinazione (`/obiettivi`) senza tabella
    dei nomi: si sostituisce con una destinazione esplicita (pagina, in alto) ricavata dai marcatori.
    Se un collegamento punta a un'ancora sconosciuta, si segnala l'errore."""
    sconosciuti = set()
    for pagina in pdf.pages:
        for annotazione in pagina.get("/Annots") or []:
            if annotazione.get("/Subtype") != "/Link" or "/Dest" not in annotazione:
                continue
            ident = str(annotazione.Dest).lstrip("/")
            if ident not in pagine:
                sconosciuti.add(ident)
                continue
            destinazione = pdf.pages[pagine[ident] - 1 + offset]
            annotazione.Dest = pikepdf.Array([destinazione.obj, pikepdf.Name.XYZ, 0, 842, pikepdf.Object.parse(b"null")])
    if sconosciuti:
        raise RuntimeError(f"Collegamenti interni verso ancore non registrate: {sorted(sconosciuti)}")


def unisci(cop, corpo, voci, pagine, destinazione):
    with pikepdf.open(cop) as pdf_cop, pikepdf.open(corpo) as finale:
        if len(pdf_cop.pages) != cfg.PAGINE_COPERTINA:
            raise RuntimeError(f"La copertina ha {len(pdf_cop.pages)} pagine invece di {cfg.PAGINE_COPERTINA}")
        for posizione, pagina in enumerate(pdf_cop.pages):
            finale.pages.insert(posizione, pagina)
        offset = len(pdf_cop.pages)
        risolvi_collegamenti(finale, pagine, offset)
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
            meta["dc:title"] = cfg.TITOLO
            meta["dc:creator"] = [cfg.AUTORE]
            meta["dc:description"] = cfg.OGGETTO
            meta["dc:language"] = ["it"]
            meta["pdf:Keywords"] = cfg.PAROLE_CHIAVE
        finale.docinfo["/Title"] = cfg.TITOLO
        finale.docinfo["/Author"] = cfg.AUTORE
        finale.docinfo["/Subject"] = cfg.OGGETTO
        finale.docinfo["/Keywords"] = cfg.PAROLE_CHIAVE
        finale.docinfo["/Creator"] = "HTML con CSS di stampa, resa con Google Chrome"
        finale.Root.PageMode = pikepdf.Name.UseOutlines
        finale.Root.Lang = pikepdf.String("it")
        finale.save(destinazione)
        return len(finale.pages)


# ---------------------------------------------------------------------------------------------
# Programma principale
# ---------------------------------------------------------------------------------------------

def main():
    if not os.path.exists(cfg.HTML_IN):
        sys.exit(f"Manca la dispensa HTML: {cfg.HTML_IN}")
    with open(cfg.HTML_IN, encoding="utf-8") as fh:
        html = fh.read()
    with open(cfg.CSS_STAMPA, encoding="utf-8") as fh:
        css = fh.read()
    voci = struttura(html)
    print(f"Struttura: {len(voci)} voci (parti e capitoli)")
    if len(voci) < 10:
        sys.exit("Struttura incompleta: controllare le espressioni regolari")

    with tempfile.TemporaryDirectory(prefix="pdf-ponte348-") as tmp:
        html_corpo = os.path.join(tmp, "corpo.html")
        pdf_corpo = os.path.join(tmp, "corpo.pdf")

        def scrivi(pagine, marcatori=True):
            with open(html_corpo, "w", encoding="utf-8") as fh:
                fh.write(prepara_html(html, voci, pagine, css, marcatori))

        scrivi({})  # passata 1: numeri provvisori
        chrome_pdf(html_corpo, pdf_corpo)
        pagine1 = pagine_marcatori(pdf_corpo, voci)

        scrivi(pagine1)  # passata 2: indice definitivo, la paginazione non deve cambiare
        chrome_pdf(html_corpo, pdf_corpo)
        pagine2 = pagine_marcatori(pdf_corpo, voci)
        if pagine1 != pagine2:
            diff = {k: (pagine1[k], pagine2[k]) for k in pagine1 if pagine1[k] != pagine2[k]}
            raise RuntimeError(f"La paginazione è cambiata tra le due passate: {diff}")
        print(f"Corpo: {len(pagine2)} marcatori, paginazione stabile")

        scrivi(pagine2, marcatori=False)  # passata finale: il testo nascosto inquinerebbe ricerca e copia
        chrome_pdf(html_corpo, pdf_corpo)
        verifica_titoli(pdf_corpo, voci, pagine2)
        print("Corpo finale senza marcatori: titoli verificati nelle pagine registrate")

        html_cop, pdf_cop = os.path.join(tmp, "copertina.html"), os.path.join(tmp, "copertina.pdf")
        with open(html_cop, "w", encoding="utf-8") as fh:
            fh.write(copertina_html(html))
        chrome_pdf(html_cop, pdf_cop)

        n = unisci(pdf_cop, pdf_corpo, voci, pagine2, cfg.PDF_OUT)
        os.chmod(cfg.PDF_OUT, 0o664)
    print(f"Scritto {cfg.PDF_OUT}: {n} pagine, {os.path.getsize(cfg.PDF_OUT) / 1024 / 1024:.1f} MiB")


if __name__ == "__main__":
    main()
