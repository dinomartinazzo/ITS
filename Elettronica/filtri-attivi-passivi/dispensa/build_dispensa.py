"""Genera dispensa_filtri_attivi_passivi.html a partire da template.html.

Tutti i valori numerici, le tabelle e i grafici sono calcolati con src/filtri_core.py: la dispensa
non contiene numeri scritti a mano nelle tabelle. Uso (dalla radice del progetto):

    python3 dispensa/build_dispensa.py
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

from contenuti_base import blocchi_base  # noqa: E402
from contenuti_nuovi import blocchi_nuovi  # noqa: E402
from contenuti_teoria import blocchi_teoria_tutti  # noqa: E402
from contenuti_famiglie import blocchi_famiglie  # noqa: E402
from disegno import hero_art  # noqa: E402

USCITA = os.path.join(RADICE, "dispensa_filtri_attivi_passivi.html")


def leggi(nome):
    with open(os.path.join(AQUI, nome), encoding="utf-8") as fh:
        return fh.read()


def numera(pagina):
    """Numera capitoli, appendici ed equazioni in ordine di apparizione e risolve i rimandi.

    Nel template: <span class="num">#</span> (capitolo) o <span class="num">@</span> (appendice) dentro la
    prima h2 di una <section id="...">; <span class="eqn">(@nome)</span> per le equazioni.
    Rimandi: {{cap:id}} -> numero del capitolo, {{num:id}} -> numero a due cifre, {{eq:nome}} -> (n).
    """
    etichette = {}
    cap, app = 0, 0

    def sezione(m):
        nonlocal cap, app
        ident, simbolo = m.group(1), m.group(3)
        if simbolo == "#":
            cap += 1
            etichette[ident] = str(cap)
        else:
            app += 1
            etichette[ident] = chr(ord("A") + app - 1)
        lab = etichette[ident]
        return m.group(0).replace(f'<span class="num">{simbolo}</span>', f'<span class="num">{lab.zfill(2) if lab.isdigit() else lab}</span>')

    pagina = re.sub(r'<section id="([^"]+)"([^>]*)>\s*<h2><span class="num">([#@])</span>', sezione, pagina)
    equazioni = {}
    def equazione(m):
        nome = m.group(1)
        equazioni[nome] = len(equazioni) + 1
        return f'<span class="eqn">({equazioni[nome]})</span>'

    pagina = re.sub(r'<span class="eqn">\(@([a-z0-9_]+)\)</span>', equazione, pagina)
    pagina = pagina.replace("{{N_CAPITOLI}}", str(cap))
    pagina = re.sub(r"\{\{cap:([^}]+)\}\}", lambda m: etichette[m.group(1)], pagina)
    pagina = re.sub(r"\{\{num:([^}]+)\}\}", lambda m: etichette[m.group(1)].zfill(2) if etichette[m.group(1)].isdigit() else etichette[m.group(1)], pagina)
    pagina = re.sub(r"\{\{eq:([a-z0-9_]+)\}\}", lambda m: f"({equazioni[m.group(1)]})", pagina)
    return pagina


def main():
    pagina = leggi("template.html")
    # {{include:nome}} inserisce il file capitoli/nome.html (i capitoli sono scritti in file separati)
    for _ in range(3):  # le inclusioni possono essere annidate
        pagina = re.sub(r"\{\{include:([a-z0-9_-]+)\}\}", lambda m: leggi(os.path.join("capitoli", m.group(1) + ".html")), pagina)
    # nel template i caratteri speciali possono essere scritti come \uXXXX
    pagina = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), pagina)

    sost = blocchi_base()
    sost.update(blocchi_nuovi())
    sost.update(blocchi_teoria_tutti())
    sost.update(blocchi_famiglie())
    sost["CSS"] = leggi("stile.css") + leggi("extra.css") + leggi("stampa.css")
    sost["JS"] = leggi("script.js")
    sost["HERO_ART"] = hero_art()
    for chiave, valore in sost.items():
        pagina = pagina.replace("{{" + chiave + "}}", valore)

    pagina = numera(pagina)

    # numerazione delle figure in ordine di apparizione (figura() emette il segnaposto §N§)
    ordine = []
    for m in re.finditer("§([^§]+)§", pagina):
        if m.group(1) not in ordine:
            ordine.append(m.group(1))
    pagina = re.sub("§([^§]+)§", lambda m: str(ordine.index(m.group(1)) + 1), pagina)

    residui = sorted(set(re.findall(r"\{\{([A-Z0-9_]+)\}\}", pagina)))
    if residui:
        sys.exit("Segnaposto non risolti: " + ", ".join(residui))
    rimandi_residui = sorted(set(re.findall(r"\{+(?:cap|num|eq):[^}]+\}+", pagina)))
    if rimandi_residui:
        sys.exit("Rimandi non risolti: " + ", ".join(rimandi_residui))
    with open(USCITA, "w", encoding="utf-8") as fh:
        fh.write(pagina)
    print(f"Scritto {USCITA} ({len(pagina) / 1024:.0f} KiB, {len(ordine)} figure)")


if __name__ == "__main__":
    main()
