"""Disegni della teoria di base: circuiti elementari, sinusoide, numeri complessi, logaritmi, filtri.

Ogni funzione restituisce (larghezza, altezza, contenuto SVG) per `figura()`. Le curve sono calcolate;
gli schemi sono disegnati a coordinate fisse.
"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
from disegno import _cap_h, _cap_v, _gnd, _res_h, grafico_bode, serie_db, svgt  # noqa: E402
from disegno_didattico import _giunzione, _mappa, _opamp, _sorgente, _testa, freccia, riquadro, testo  # noqa: E402
from formati import it, sig, si  # noqa: E402

MENO = "−"
OHM = "Ω"


# ---------------------------------------------------------------------------------------------
# Primitive di pannello (grafici compatti dentro un'unica figura)
# ---------------------------------------------------------------------------------------------

def _pannello(x0, y0, w, h, pts, xmin, xmax, ymin, ymax, cls="sa", xlog=False, assi=True, tratteggio=False):
    def X(x):
        if xlog:
            return x0 + (math.log10(x) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * w
        return x0 + (x - xmin) / (xmax - xmin) * w

    def Y(y):
        return y0 + h - (y - ymin) / (ymax - ymin) * h

    out = []
    if assi:
        out.append(f'<rect class="ax" x="{x0}" y="{y0}" width="{w}" height="{h}"/>')
        if ymin < 0 < ymax:
            out.append(f'<line class="ax" x1="{x0}" y1="{Y(0):.1f}" x2="{x0 + w}" y2="{Y(0):.1f}"/>')
    d = " ".join(("M" if i == 0 else "L") + f"{X(x):.1f} {Y(max(min(y, ymax), ymin)):.1f}" for i, (x, y) in enumerate(pts))
    extra = ' stroke-dasharray="5 4"' if tratteggio else ""
    out.append(f'<path class="sl {cls}"{extra} d="{d}"/>')
    return "".join(out), X, Y


def _seno(f, fase_gradi=0.0, ampiezza=1.0, t_max=1.0, n=240, coseno=False):
    fase = math.radians(fase_gradi)
    fun = math.cos if coseno else math.sin
    return [(t_max * i / n, ampiezza * fun(2 * math.pi * f * t_max * i / n + fase)) for i in range(n + 1)]


# ---------------------------------------------------------------------------------------------
# Mappa del percorso
# ---------------------------------------------------------------------------------------------

def schema_percorso():
    p = []
    parti = [("Teoria di base", "corrente, partitore, condensatore, sinusoide, numeri complessi, decibel", "d"),
             ("Filtri passivi", "RC e RLC: formule, esempi, misure", "a"),
             ("Filtri attivi", "operazionale e Sallen-Key", "b"),
             ("Progetto e verifica", "anti-aliasing, diagnostica, esercizi", "c")]
    for i, (t, s, cls) in enumerate(parti):
        x = 20 + i * 165
        p.append(riquadro(x, 40, 150, 100, "", cls, [t] + _spezza(s, 20)))
        if i < 3:
            p.append(freccia(x + 150, 90, x + 165, 90, ""))
    p.append(testo(20, 175, "In ogni capitolo: 1) l'idea in parole semplici  2) il disegno  3) la formula  4) un esempio con i numeri  5) il riepilogo e qualche domanda.", "sm"))
    p.append(testo(20, 196, "Si può leggere in ordine; chi conosce già la teoria di base può partire dalla parte sui filtri passivi.", "sm"))
    return 680, 215, "\n".join(p)


def _spezza(s, n):
    parole, riga, righe = s.split(), "", []
    for w in parole:
        if len(riga) + len(w) + 1 > n:
            righe.append(riga)
            riga = w
        else:
            riga = (riga + " " + w).strip()
    righe.append(riga)
    return righe


# ---------------------------------------------------------------------------------------------
# Elettricità di base
# ---------------------------------------------------------------------------------------------

def fig_idraulica():
    p = []
    p.append(testo(20, 24, "Circuito elettrico", "ttl") + testo(380, 24, "Analogia con l'acqua", "ttl"))
    # circuito elettrico: batteria a sinistra, resistenza in alto
    p.append('<path class="w" d="M60 70 L60 100"/><line class="cap" x1="45" y1="100" x2="75" y2="100"/><line class="w" x1="52" y1="109" x2="68" y2="109"/>'
             '<path class="w" d="M60 109 L60 150"/>')
    p.append('<path class="w" d="M60 70 L110 70"/>' + _res_h(110, 70) + '<path class="w" d="M166 70 L250 70 L250 150 L60 150"/>')
    p.append(testo(84, 98, "+", "pin") + testo(84, 124, MENO, "pin") + testo(36, 108, "batteria", "sm", "end"))
    p.append(testo(138, 54, "R", "", "middle") + testo(138, 90, "resistenza", "sm", "middle"))
    p.append(freccia(180, 70, 215, 70, "w") + testo(198, 58, "corrente I", "sm", "middle"))
    p.append(testo(60, 190, "tensione V: la «spinta» della batteria", "sm") + testo(60, 207, "corrente I: quante cariche passano al secondo", "sm")
             + testo(60, 224, "resistenza R: quanto il componente «frena»", "sm"))
    # analogia idraulica: pompa e tubo con restringimento
    p.append('<circle class="r" cx="420" cy="110" r="22"/>' + testo(420, 114, "pompa", "sm", "middle"))
    p.append('<path class="w" d="M420 88 L420 70 L480 70"/><path class="w" d="M420 132 L420 150 L600 150 L600 70"/>')
    p.append('<path class="w" d="M480 60 L540 60 L540 80 L480 80 Z" fill="none"/>')
    p.append('<path class="w" d="M480 70 L480 62 M540 70 L540 62"/>')
    p.append('<rect class="r" x="495" y="64" width="30" height="12" rx="2"/>')
    p.append('<path class="w" d="M540 70 L600 70"/>')
    p.append(freccia(555, 52, 595, 52, "b") + testo(575, 44, "portata", "sm", "middle"))
    p.append(testo(510, 96, "restringimento", "sm", "middle"))
    p.append(testo(380, 190, "pressione della pompa ↔ tensione V", "sm") + testo(380, 207, "portata d'acqua ↔ corrente I", "sm")
             + testo(380, 224, "restringimento del tubo ↔ resistenza R", "sm"))
    return 680, 245, "\n".join(p)


def fig_ohm():
    xs = [0, 25]
    curve = [("R = 100 \u03a9", "sa", [(i, 0.1 * i) for i in xs]), ("R = 200 \u03a9", "sb", [(i, 0.2 * i) for i in xs]),
             ("R = 400 \u03a9", "sc", [(i, 0.4 * i) for i in xs])]
    return grafico_bode(curve, 0, 25, 0, 12, [0, 5, 10, 15, 20, 25], [0, 2, 4, 6, 8, 10, 12],
                        "tensione V [V]", "corrente I [mA]", id_clip="clip-ohm", x_lin=True,
                        marcatori=[(10, 2.0, "", 0, 0), (10, 4.0, "", 0, 0), (10, 1.0, "", 0, 0)],
                        annot=[(0.8, 11.0, "Con 10 mA: R = 100 \u03a9 \u2192 1 V, R = 200 \u03a9 \u2192 2 V, R = 400 \u03a9 \u2192 4 V.", "start"),
                               (0.8, 10.0, "La retta è più ripida quando la resistenza è maggiore: V = R \u00b7 I.", "start")])


def schema_serie_parallelo():
    p = []
    p.append(testo(20, 24, "Resistenze in serie", "ttl") + testo(360, 24, "Resistenze in parallelo", "ttl"))
    # serie
    p.append('<line class="w" x1="30" y1="80" x2="60" y2="80"/>' + _res_h(60, 80) + '<line class="w" x1="116" y1="80" x2="150" y2="80"/>' + _res_h(150, 80) + '<line class="w" x1="206" y1="80" x2="236" y2="80"/>')
    p.append(testo(88, 62, "R<sub>1</sub> = 1 kΩ", "", "middle") + testo(178, 62, "R<sub>2</sub> = 2 kΩ", "", "middle"))
    p.append(testo(30, 130, "R<sub>eq</sub> = R<sub>1</sub> + R<sub>2</sub> = 3 kΩ", "it"))
    p.append(testo(30, 154, "Le correnti sono uguali, le tensioni si sommano.", "sm"))
    p.append(testo(30, 172, "La resistenza totale è sempre più grande della maggiore.", "sm"))
    # parallelo
    o = 22
    p.append(f'<line class="w" x1="360" y1="{80 + o}" x2="400" y2="{80 + o}"/><line class="w" x1="400" y1="{50 + o}" x2="400" y2="{120 + o}"/><line class="w" x1="400" y1="{50 + o}" x2="430" y2="{50 + o}"/>' + _res_h(430, 50 + o)
             + f'<line class="w" x1="486" y1="{50 + o}" x2="520" y2="{50 + o}"/><line class="w" x1="520" y1="{50 + o}" x2="520" y2="{120 + o}"/><line class="w" x1="400" y1="{120 + o}" x2="430" y2="{120 + o}"/>' + _res_h(430, 120 + o)
             + f'<line class="w" x1="486" y1="{120 + o}" x2="520" y2="{120 + o}"/><line class="w" x1="520" y1="{80 + o}" x2="560" y2="{80 + o}"/>' + _giunzione(400, 80 + o) + _giunzione(520, 80 + o))
    p.append(testo(458, 36 + o, "R<sub>1</sub> = 1 k\u03a9", "", "middle") + testo(458, 106 + o + 12, "R<sub>2</sub> = 2 k\u03a9", "", "middle"))
    p.append(testo(360, 178, "R<sub>eq</sub> = R<sub>1</sub>R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>) = 667 \u03a9", "it"))
    p.append(testo(360, 202, "La tensione è la stessa, le correnti si sommano.", "sm"))
    p.append(testo(360, 220, "La resistenza totale è sempre più piccola della minore.", "sm"))
    return 680, 240, "\n".join(p)


def fig_partitore():
    """Partitore di tensione con barra proporzionale (R1 = 3 kOhm, R2 = 1 kOhm, Vin = 12 V)."""
    p = []
    r1, r2, vin = 3000.0, 1000.0, 12.0
    vout = vin * r2 / (r1 + r2)
    p.append(_giunzione(60, 40) + testo(40, 30, "V<sub>in</sub>", "pin"))
    p.append('<line class="w" x1="60" y1="40" x2="60" y2="62"/><rect class="r" x="52" y="62" width="16" height="50" rx="2"/><line class="w" x1="60" y1="112" x2="60" y2="130"/>' + _giunzione(60, 130))
    p.append('<line class="w" x1="60" y1="130" x2="60" y2="148"/><rect class="r" x="52" y="148" width="16" height="50" rx="2"/><line class="w" x1="60" y1="198" x2="60" y2="215"/>' + _gnd(60, 215))
    p.append('<line class="w" x1="60" y1="130" x2="140" y2="130"/>' + _giunzione(140, 130) + testo(150, 134, "V<sub>out</sub>", "pin"))
    p.append(testo(82, 92, "R<sub>1</sub> = 3 kΩ", "sm") + testo(82, 178, "R<sub>2</sub> = 1 kΩ", "sm"))
    # barra proporzionale
    x0, larg = 300, 340
    w1 = larg * r1 / (r1 + r2)
    p.append(testo(x0, 40, "La tensione V<sub>in</sub> si divide in proporzione alle resistenze", "bd"))
    p.append(f'<rect class="fill-a" x="{x0}" y="62" width="{w1:.1f}" height="44"/><rect class="fill-b" x="{x0 + w1:.1f}" y="62" width="{larg - w1:.1f}" height="44"/>')
    p.append(f'<rect class="ax" x="{x0}" y="62" width="{larg}" height="44"/><line class="ax" x1="{x0 + w1:.1f}" y1="62" x2="{x0 + w1:.1f}" y2="106"/>')
    p.append(testo(x0 + w1 / 2, 88, f"su R<sub>1</sub>: {it(vin - vout, 0)} V", "bd", "middle") + testo(x0 + w1 + (larg - w1) / 2, 88, f"su R<sub>2</sub>: {it(vout, 0)} V", "bd", "middle"))
    p.append(testo(x0, 130, f"Totale: {it(vin, 0)} V = {it(vin - vout, 0)} V + {it(vout, 0)} V", "sm"))
    p.append(testo(x0, 160, "V<sub>out</sub> = V<sub>in</sub> · R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>)", "it"))
    p.append(testo(x0, 184, f"= {it(vin, 0)} V · 1000/(3000 + 1000) = {it(vout, 0)} V", "it"))
    p.append(testo(x0, 208, "R<sub>2</sub> è un quarto del totale, quindi prende un quarto della tensione.", "sm"))
    return 680, 235, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Condensatore e induttore
# ---------------------------------------------------------------------------------------------

def fig_condensatore():
    p = []
    p.append(testo(20, 24, "Che cos'è un condensatore", "ttl") + testo(380, 24, "Analogia: una membrana elastica nel tubo", "ttl"))
    # armature
    p.append('<line class="cap" x1="90" y1="70" x2="90" y2="150"/><line class="cap" x1="150" y1="70" x2="150" y2="150"/>')
    p.append('<path class="w" d="M90 110 L40 110"/><path class="w" d="M150 110 L200 110"/>')
    for yy in (85, 110, 135):
        p.append(freccia(94, yy, 146, yy, "b"))
    p.append(testo(120, 62, "isolante", "sm", "middle") + testo(84, 100, "+ + +", "pin", "end") + testo(158, 100, MENO + " " + MENO + " " + MENO, "pin"))
    p.append(testo(20, 190, "Due piastre di metallo separate da un isolante.", "sm") + testo(20, 207, "Applicando una tensione si accumulano cariche + e −:", "sm")
             + testo(20, 224, "il condensatore «immagazzina» carica, cioè energia.", "sm"))
    # analogia idraulica
    p.append('<path class="w" d="M400 80 L560 80 M400 140 L560 140"/><rect class="r" x="478" y="80" width="8" height="60"/>')
    p.append(freccia(410, 110, 470, 110, "b") + testo(440, 100, "acqua", "sm", "middle"))
    p.append('<path class="arw a" d="M486 90 Q502 110 486 130"/>')
    p.append(testo(380, 190, "L'acqua spinge la membrana, che si tende e la ferma:", "sm") + testo(380, 207, "all'inizio l'acqua scorre molto, poi sempre meno.", "sm")
             + testo(380, 224, "Così è la corrente: grande all'inizio, poi si annulla.", "sm"))
    return 680, 245, "\n".join(p)


def fig_carica_condensatore():
    xs = [i * 6 / 240 for i in range(241)]
    carica = [(x, 1 - math.exp(-x)) for x in xs]
    corr = [(x, math.exp(-x)) for x in xs]
    marc = [(1.0, 1 - math.exp(-1), "dopo τ: V al 63 %", 8, 20), (1.0, math.exp(-1), "dopo τ: I al 37 %", 8, -8)]
    return grafico_bode([("tensione sul condensatore V/V<sub>s</sub>", "sa", carica), ("corrente I/I<sub>0</sub>", "sb", corr)],
                        0, 6, 0, 1.08, [0, 1, 2, 3, 4, 5, 6], [0, 0.25, 0.5, 0.75, 1], "valore relativo",
                        "tempo t / τ", id_clip="car", x_lin=True, marcatori=marc, ylab={0: "0", 0.25: "0,25", 0.5: "0,5", 0.75: "0,75", 1: "1"})


def schema_cond_dc_ac():
    p = []
    p.append(testo(20, 24, "In continua (frequenza zero)", "ttl") + testo(360, 24, "In alternata ad alta frequenza", "ttl"))
    # DC
    p.append(_sorgente(50, 100) + '<path class="w" d="M50 86 L50 60 L100 60"/><path class="w" d="M50 114 L50 150 L260 150 L260 60 L200 60"/>')
    p.append('<line class="w" x1="100" y1="60" x2="140" y2="60"/><line class="cap" x1="140" y1="45" x2="140" y2="75"/><line class="cap" x1="156" y1="45" x2="156" y2="75"/><line class="w" x1="156" y1="60" x2="200" y2="60"/>')
    p.append(testo(20, 190, "Dopo la carica iniziale non passa più corrente:", "sm") + testo(20, 207, "il condensatore si comporta come un interruttore aperto.", "sm"))
    # AC
    p.append(_sorgente(390, 100) + '<path class="w" d="M390 86 L390 60 L440 60"/><path class="w" d="M390 114 L390 150 L600 150 L600 60 L540 60"/>')
    p.append('<line class="w" x1="440" y1="60" x2="480" y2="60"/><line class="cap" x1="480" y1="45" x2="480" y2="75"/><line class="cap" x1="496" y1="45" x2="496" y2="75"/><line class="w" x1="496" y1="60" x2="540" y2="60"/>')
    p.append(freccia(440, 36, 470, 36, "b") + freccia(510, 36, 540, 36, "b") + freccia(540, 84, 510, 84, "w") + freccia(470, 84, 440, 84, "w"))
    p.append(testo(360, 190, "La corrente va avanti e indietro e il condensatore", "sm") + testo(360, 207, "si carica e si scarica di continuo: lascia passare", "sm")
             + testo(360, 224, "il segnale. Più la frequenza è alta, più passa.", "sm"))
    return 680, 245, "\n".join(p)


def fig_induttore():
    p = []
    p.append(testo(20, 24, "L'induttore: una bobina di filo", "ttl"))
    p.append('<path class="w" d="M40 85 L90 85"/>')
    p.append('<path class="w" d="M90 85 a14 18 0 0 1 28 0 a14 18 0 0 1 28 0 a14 18 0 0 1 28 0 a14 18 0 0 1 28 0"/>')
    p.append('<path class="w" d="M202 85 L250 85"/>')
    p.append('<path class="arw a" stroke-dasharray="4 3" d="M146 58 Q146 28 240 40"/><path class="arw a" stroke-dasharray="4 3" d="M146 112 Q146 142 240 130"/>')
    p.append(testo(250, 44, "campo magnetico", "sm"))
    p.append(testo(340, 70, "La corrente nella bobina crea un campo magnetico, che ha energia.", "sm") + testo(340, 88, "Per cambiare la corrente bisogna cambiare il campo, e questo", "sm")
             + testo(340, 106, "richiede tempo: l'induttore si oppone alle variazioni di corrente.", "sm"))
    p.append(testo(20, 170, "Condensatore e induttore a confronto", "bd"))
    righe = [("", "Condensatore", "Induttore"),
             ("Si oppone ai cambi di", "tensione", "corrente"),
             ("In continua", "circuito aperto", "filo (cortocircuito)"),
             ("Ad alta frequenza", "quasi un filo", "quasi un circuito aperto"),
             ("Reattanza X", "1/(2\u03c0fC): scende con f", "2\u03c0fL: sale con f")]
    for i, (a_, b_, c_) in enumerate(righe):
        y = 196 + i * 24
        cl = "bd" if i == 0 else "sm"
        p.append(testo(20, y, a_, cl) + testo(200, y, b_, cl) + testo(440, y, c_, cl))
        p.append(f'<line class="ax" x1="20" y1="{y + 7}" x2="660" y2="{y + 7}"/>')
    return 680, 320, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Segnali sinusoidali
# ---------------------------------------------------------------------------------------------

def fig_sinusoide_cerchio():
    p = []
    cx, cy, r = 110, 150, 80
    theta = math.radians(50)
    p.append(f'<circle class="ref" cx="{cx}" cy="{cy}" r="{r}"/><line class="ax" x1="{cx - 100}" y1="{cy}" x2="{cx + 100}" y2="{cy}"/><line class="ax" x1="{cx}" y1="{cy - 100}" x2="{cx}" y2="{cy + 100}"/>')
    px, py = cx + r * math.cos(theta), cy - r * math.sin(theta)
    p.append(freccia(cx, cy, px, py, "a"))
    p.append(f'<path class="arw" d="M{cx + 28} {cy} A28 28 0 0 0 {cx + 28 * math.cos(theta):.1f} {cy - 28 * math.sin(theta):.1f}"/>' + testo(cx + 34, cy - 10, "θ", "pin"))
    p.append(f'<line class="ref" x1="{px:.1f}" y1="{py:.1f}" x2="{cx}" y2="{py:.1f}"/><circle class="mrk" cx="{px:.1f}" cy="{py:.1f}" r="4"/>')
    p.append(testo(cx, 262, "Il vettore di lunghezza V<sub>p</sub> ruota", "sm", "middle") + testo(cx, 278, "alla velocità di f giri al secondo.", "sm", "middle"))
    # sinusoide a destra
    x0, w, h = 280, 370, 140
    pts = [(math.radians(a), math.sin(math.radians(a))) for a in range(0, 361, 4)]
    svg, X, Y = _pannello(x0, cy - h / 2, w, h, pts, 0, 2 * math.pi, -1.1, 1.1, "sa")
    p.append(svg)
    p.append(f'<line class="ref" x1="{X(theta):.1f}" y1="{Y(0):.1f}" x2="{X(theta):.1f}" y2="{Y(math.sin(theta)):.1f}"/><circle class="mrk" cx="{X(theta):.1f}" cy="{Y(math.sin(theta)):.1f}" r="4"/>')
    p.append(f'<line class="ref" x1="{x0 - 40}" y1="{py:.1f}" x2="{X(theta):.1f}" y2="{Y(math.sin(theta)):.1f}"/>')
    p.append(testo(x0 + w / 2, cy + h / 2 + 22, "La tensione è l'altezza del vettore: v = V<sub>p</sub> sen θ", "sm", "middle"))
    p.append(testo(x0, cy - h / 2 - 8, "un giro completo = un periodo T", "sm"))
    p.append(testo(X(math.pi / 2), Y(1) - 6, "V<sub>p</sub>", "tick", "middle") + testo(x0 + w + 4, Y(0) + 4, "θ", "tick"))
    return 680, 320, "\n".join(p)


def fig_parametri_sinusoide():
    p = []
    w, h, y0 = 190, 100, 50
    titoli = ["Ampiezza", "Frequenza", "Fase"]
    descr = [["La curva grande ha ampiezza doppia", "(V<sub>p</sub> = 2 contro V<sub>p</sub> = 1)."],
             ["La curva veloce ha frequenza doppia:", "il periodo si dimezza."],
             ["Con fase 90° la curva parte da un massimo:", "è spostata (anticipata) di un quarto di periodo."]]
    for k in range(3):
        x0 = 20 + k * 215
        p.append(testo(x0, 30, titoli[k], "bd"))
        if k == 0:
            a, _, _ = _pannello(x0, y0, w, h, _seno(1, 0, 1.0), 0, 1, -2.2, 2.2, "sa"); b, _, _ = _pannello(x0, y0, w, h, _seno(1, 0, 2.0), 0, 1, -2.2, 2.2, "sb", assi=False)
        elif k == 1:
            a, _, _ = _pannello(x0, y0, w, h, _seno(1, 0), 0, 1, -1.2, 1.2, "sa"); b, _, _ = _pannello(x0, y0, w, h, _seno(2, 0), 0, 1, -1.2, 1.2, "sb", assi=False)
        else:
            a, _, _ = _pannello(x0, y0, w, h, _seno(1, 0), 0, 1, -1.2, 1.2, "sa"); b, _, _ = _pannello(x0, y0, w, h, _seno(1, 90), 0, 1, -1.2, 1.2, "sb", assi=False)
        p.append(a + b)
        for i, r in enumerate(descr[k]):
            p.append(testo(x0, y0 + h + 22 + 15 * i, r, "sm"))
    p.append(testo(20, 232, "Tre numeri bastano a descrivere una sinusoide: quanto è grande (ampiezza), quanto è veloce (frequenza), da dove parte (fase).", "sm"))
    return 680, 250, "\n".join(p)


def fig_picco_rms():
    pts = _seno(1, 0, 1.0, 1.0, 300)
    ymin, ymax, h = -1.5, 1.5, 300
    w_, h_, inner = grafico_bode([("tensione v(t)", "sa", pts)], 0, 1, ymin, ymax, [0, 0.25, 0.5, 0.75, 1], [-1, 0, 1], "tensione [V]", "tempo [periodi T]",
                                 altezza=h, id_clip="pr", x_lin=True, ylab={-1: MENO + "1", 0: "0", 1: "1"}, xlab={0: "0", 0.25: "T/4", 0.5: "T/2", 0.75: "3T/4", 1: "T"})
    px, py = _mappa(0, 1, ymin, ymax, h)
    ex = []
    ex.append(freccia(px(0.88), py(0), px(0.88), py(1), "b", doppia=True) + testo(px(0.88) - 8, py(0.5) + 4, "V<sub>p</sub> (picco)", "sm", "end"))
    ex.append(freccia(px(0.1), py(-1), px(0.1), py(1), "w", doppia=True) + testo(px(0.1) + 8, py(-0.7), "V<sub>pp</sub> = 2 V<sub>p</sub>", "sm"))
    ex.append(f'<line class="ref" x1="{px(0)}" y1="{py(0.707):.1f}" x2="{px(1)}" y2="{py(0.707):.1f}"/>')
    ex.append(testo(px(0.52), py(0.55), "V<sub>rms</sub> = 0,707 V<sub>p</sub>", "sm") + testo(px(0.52), py(0.33), "(effetto in potenza uguale a una continua)", "sm"))
    return w_, h_, inner + "\n" + "\n".join(ex)


def fig_fasori_ritardo():
    p = []
    cx, cy, r = 100, 150, 70
    p.append(f'<circle class="ref" cx="{cx}" cy="{cy}" r="{r}"/><line class="ax" x1="{cx - 90}" y1="{cy}" x2="{cx + 90}" y2="{cy}"/><line class="ax" x1="{cx}" y1="{cy - 90}" x2="{cx}" y2="{cy + 90}"/>')
    p.append(freccia(cx, cy, cx + r, cy, "a") + testo(cx + r + 6, cy - 4, "ingresso", "sm"))
    a = math.radians(-45)
    p.append(freccia(cx, cy, cx + r * math.cos(a), cy - r * math.sin(a), "b") + testo(cx + r * math.cos(a) + 4, cy - r * math.sin(a) + 14, "uscita", "sm"))
    p.append(f'<path class="arw" d="M{cx + 30} {cy} A30 30 0 0 1 {cx + 30 * math.cos(a):.1f} {cy - 30 * math.sin(a):.1f}"/>' + testo(cx + 34, cy + 22, "45°", "pin"))
    p.append(testo(cx, 250, "Due fasori: il secondo è «in ritardo»", "sm", "middle") + testo(cx, 266, "di 45° rispetto al primo.", "sm", "middle"))
    x0, w, h = 280, 380, 120
    svg1, X, Y = _pannello(x0, cy - h / 2, w, h, _seno(2, 0, 1.0, 1.0, 300), 0, 1, -1.3, 1.3, "sa")
    svg2, _, _ = _pannello(x0, cy - h / 2, w, h, _seno(2, -45, 0.707, 1.0, 300), 0, 1, -1.3, 1.3, "sb", assi=False)
    p.append(svg1 + svg2)
    dt = 1 / 16  # 45 gradi di 2 periodi nel riquadro => 1/8 di periodo = 1/16 dell'asse
    p.append(freccia(X(0.0), Y(-1.12), X(dt), Y(-1.12), "w", doppia=True) + testo(X(dt) + 6, Y(-1.12) + 4, "Δt = T/8", "sm"))
    p.append(testo(x0 + w / 2, cy + h / 2 + 22, "Ritardo di fase ↔ ritardo nel tempo: φ = 360° · Δt/T", "sm", "middle"))
    return 680, 290, "\n".join(p)


def fig_fase_rcl():
    p = []
    w, h, y0 = 190, 90, 56
    casi = [("Resistenza", 0, 0, "tensione e corrente in fase"), ("Condensatore", 0, 90, "la corrente anticipa la tensione di 90°"),
            ("Induttore", 0, -90, "la corrente è in ritardo di 90° sulla tensione")]
    for k, (nome, fv, fi, descr) in enumerate(casi):
        x0 = 20 + k * 215
        p.append(testo(x0, 32, nome, "bd"))
        s1, _, _ = _pannello(x0, y0, w, h, _seno(2, fv, 1.0, 1.0, 300), 0, 1, -1.3, 1.3, "sa")
        s2, _, _ = _pannello(x0, y0, w, h, _seno(2, fi, 0.7, 1.0, 300), 0, 1, -1.3, 1.3, "sb", assi=False)
        p.append(s1 + s2)
        for i, r in enumerate(_spezza(descr, 30)):
            p.append(testo(x0, y0 + h + 20 + 15 * i, r, "sm"))
    p.append(f'<line class="sl sa" x1="20" y1="214" x2="46" y2="214"/>' + testo(52, 218, "tensione", "sm") + f'<line class="sl sb" x1="120" y1="214" x2="146" y2="214"/>' + testo(152, 218, "corrente (ridotta nel disegno)", "sm"))
    return 680, 235, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Numeri complessi
# ---------------------------------------------------------------------------------------------

def fig_numero_complesso():
    p = []
    ox, oy, s = 100, 200, 28
    p.append(f'<line class="ax" x1="{ox - 40}" y1="{oy}" x2="{ox + 6 * s}" y2="{oy}"/><line class="ax" x1="{ox}" y1="{oy + 20}" x2="{ox}" y2="{oy - 5 * s - 20}"/>')
    p.append(testo(ox + 6 * s, oy + 34, "parte reale", "tick", "end") + testo(ox + 8, oy - 5 * s - 12, "parte immaginaria (j)", "tick"))
    zx, zy = ox + 3 * s, oy - 4 * s
    p.append(f'<line class="ref" x1="{zx}" y1="{oy}" x2="{zx}" y2="{zy}"/><line class="ref" x1="{ox}" y1="{zy}" x2="{zx}" y2="{zy}"/>')
    p.append(freccia(ox, oy, zx, zy, "a") + f'<circle class="mrk" cx="{zx}" cy="{zy}" r="4"/>')
    p.append(testo(zx + 8, zy - 4, "z = 3 + j4", "bd"))
    p.append(testo(zx - 10, oy + 16, "3", "tick", "middle") + testo(ox - 8, zy + 4, "4", "tick", "end"))
    mod, ang = math.hypot(3, 4), math.degrees(math.atan2(4, 3))
    p.append(f'<path class="arw" d="M{ox + 32} {oy} A32 32 0 0 0 {ox + 32 * math.cos(math.radians(ang)):.1f} {oy - 32 * math.sin(math.radians(ang)):.1f}"/>' + testo(ox + 38, oy - 8, f"{it(ang, 1)}°", "pin"))
    p.append(testo(ox - 36, oy + 56, f"modulo |z| = √(3² + 4²) = {it(mod, 0)}", "sm"))
    # moltiplicazione per j
    jx, jy = ox + (-4) * s * 0, 0
    tx = 380
    p.append(testo(tx, 40, "Moltiplicare per j significa ruotare di 90°", "bd"))
    cx, cy, rr = 480, 170, 60
    p.append(f'<line class="ax" x1="{cx - 90}" y1="{cy}" x2="{cx + 90}" y2="{cy}"/><line class="ax" x1="{cx}" y1="{cy + 90}" x2="{cx}" y2="{cy - 100}"/>')
    k = rr / 5.0
    p.append(freccia(cx, cy, cx + 3 * k, cy - 4 * k, "a") + testo(cx + 3 * k + 6, cy - 4 * k, "z = 3 + j4", "sm"))
    p.append(freccia(cx, cy, cx - 4 * k, cy - 3 * k, "b") + testo(cx - 4 * k - 6, cy - 3 * k - 6, "j·z = −4 + j3", "sm", "end"))
    p.append(f'<path class="arw" d="M{cx + 22 * math.cos(math.radians(ang)):.1f} {cy - 22 * math.sin(math.radians(ang)):.1f} A22 22 0 0 0 {cx + 22 * math.cos(math.radians(ang + 90)):.1f} {cy - 22 * math.sin(math.radians(ang + 90)):.1f}"/>' + testo(cx - 6, cy - 34, "+90°", "pin", "end"))
    p.append(testo(tx, 250, "j · j = j² = −1: due rotazioni di 90°", "sm") + testo(tx, 267, "fanno 180°, cioè cambiano il segno.", "sm"))
    return 680, 285, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Funzione di trasferimento, logaritmi, decibel
# ---------------------------------------------------------------------------------------------

def schema_scatola_nera():
    p = []
    f0 = fc.rc_fc(1600.0, 100e-9)
    p.append(riquadro(250, 50, 170, 70, "", "b", ["Circuito (filtro)", "scatola nera"]))
    p.append(freccia(130, 85, 250, 85, "") + freccia(420, 85, 540, 85, ""))
    p.append(testo(30, 78, "ingresso", "sm") + testo(30, 94, "V<sub>in</sub> (f)", "bd") + testo(550, 78, "uscita", "sm") + testo(550, 94, "V<sub>out</sub> (f)", "bd"))
    p.append(testo(20, 160, "Esempio: il filtro RC con R = 1,6 kΩ e C = 100 nF, con 1 V all'ingresso", "bd"))
    righe = [(100.0, "una frequenza bassa"), (995.0, "la frequenza di taglio"), (9950.0, "una frequenza alta")]
    for i, (f, nome) in enumerate(righe):
        y = 188 + i * 30
        h = fc.h_rc_lp(f, f0)
        p.append(testo(20, y, f"a {sig(f, 4)} Hz ({nome}):", "sm"))
        p.append(f'<rect class="fill-a" x="270" y="{y - 12}" width="{abs(h) * 260:.1f}" height="14"/><rect class="ax" x="270" y="{y - 12}" width="260" height="14"/>')
        p.append(testo(540, y, f"V<sub>out</sub> = {it(abs(h), 3)} V   ({it(math.degrees(math.atan2(h.imag, h.real)), 1)}°)", "sm"))
    p.append(testo(20, 292, "La funzione di trasferimento H(f) è la tabella completa di questi rapporti, per tutte le frequenze.", "sm"))
    return 680, 308, "\n".join(p)


def fig_scala_log():
    p = []
    ml, pw = 40, 600
    p.append(testo(ml, 24, "Scala lineare: i numeri piccoli sono schiacciati", "bd"))
    y1 = 70
    p.append(f'<line class="ax" x1="{ml}" y1="{y1}" x2="{ml + pw}" y2="{y1}"/>')
    for v in (1, 10, 100, 1000):
        x = ml + pw * v / 1000
        extra = {1: 22, 10: 38, 100: 22, 1000: 22}[v]
        p.append(f'<line class="ax" x1="{x:.1f}" y1="{y1 - 6}" x2="{x:.1f}" y2="{y1 + 6}"/>' + testo(x, y1 + extra, str(v), "tick", "middle"))
    p.append(testo(ml + 4, y1 - 14, "1, 10 e 100 stanno quasi tutti nello stesso punto", "sm"))
    p.append(testo(ml, 130, "Scala logaritmica: ogni ×10 occupa lo stesso spazio", "bd"))
    y2 = 176
    p.append(f'<line class="ax" x1="{ml}" y1="{y2}" x2="{ml + pw}" y2="{y2}"/>')
    for i, v in enumerate((1, 10, 100, 1000)):
        x = ml + pw * i / 3
        p.append(f'<line class="ax" x1="{x:.1f}" y1="{y2 - 6}" x2="{x:.1f}" y2="{y2 + 6}"/>' + testo(x, y2 + 22, str(v), "tick", "middle"))
    for i in range(3):
        x = ml + pw * (i + 0.5) / 3
        p.append(freccia(ml + pw * i / 3 + 8, y2 - 20, ml + pw * (i + 1) / 3 - 8, y2 - 20, "b") + testo(x, y2 - 28, "× 10", "sm", "middle"))
    p.append(testo(ml, 226, "I filtri si studiano su scala logaritmica perché frequenze e ampiezze variano di molti ordini di grandezza.", "sm"))
    return 680, 245, "\n".join(p)


def fig_scala_db():
    p = []
    ml, pw = 50, 580
    p.append(testo(ml, 24, "Scala dei decibel: ogni ×10 in tensione sono 20 dB", "bd"))
    y = 110
    p.append(f'<line class="ax" x1="{ml}" y1="{y}" x2="{ml + pw}" y2="{y}"/>')

    def X(db):
        return ml + (db + 40) / 60 * pw
    voci = [(-40, "0,01"), (-20, "0,1"), (-6.02, "0,5"), (-3.01, "0,707"), (0, "1"), (3.01, "1,41"), (6.02, "2"), (20, "10")]
    for i, (db_, r) in enumerate(voci):
        x = X(db_)
        alt = (i % 2) * 15
        p.append(f'<line class="ax" x1="{x:.1f}" y1="{y - 8}" x2="{x:.1f}" y2="{y + 8}"/>')
        p.append(testo(x, y + 26 + alt, f"{it(round(db_), 0)} dB", "tick", "middle"))
        p.append(testo(x, y - 14 - alt, f"× {r}", "sm", "middle"))
    p.append(testo(ml, 190, "Da ricordare: ×1 = 0 dB  ·  ×2 = +6 dB  ·  ×0,5 = −6 dB  ·  ×0,707 = −3 dB  ·  ×10 = +20 dB  ·  ×0,1 = −20 dB", "sm"))
    p.append(testo(ml, 212, "Due filtri in cascata moltiplicano le ampiezze, ma i decibel si sommano: −20 dB e −20 dB fanno −40 dB.", "sm"))
    return 680, 232, "\n".join(p)


def fig_lineare_vs_log():
    p = []
    f0 = 1.0
    # pannello lineare
    p.append(testo(20, 24, "Scala di frequenza lineare", "bd") + testo(360, 24, "Scala di frequenza logaritmica", "bd"))
    pts1 = [(x, fc.db(fc.h_rc_lp(x, f0))) for x in [0.01 + i * 10 / 300 for i in range(301)]]
    s1, X1, Y1 = _pannello(20, 40, 300, 160, pts1, 0, 10, -40, 3, "sa")
    pts2 = [(x, fc.db(fc.h_rc_lp(x, f0))) for x in fc.griglia_log(0.01, 100, 300)]
    s2, X2, Y2 = _pannello(360, 40, 300, 160, pts2, 0.01, 100, -40, 3, "sa", xlog=True)
    p.append(s1 + s2)
    p.append(testo(20, 218, "0", "tick") + testo(320, 218, "10 f<sub>c</sub>", "tick", "end") + testo(360, 218, "0,01", "tick") + testo(660, 218, "100 f<sub>c</sub>", "tick", "end"))
    for x in (0.1, 1, 10):
        p.append(f'<line class="ref" x1="{X2(x):.1f}" y1="40" x2="{X2(x):.1f}" y2="200"/>' + testo(X2(x), 218, str(x).replace(".", ","), "tick", "middle"))
    p.append(testo(20, 244, "Quasi tutta la curva sta nello spazio di una sola decade:", "sm") + testo(20, 260, "la parte sotto f<sub>c</sub> è schiacciata.", "sm"))
    p.append(testo(360, 244, "Ogni decade ha lo stesso spazio: si vedono bene il", "sm") + testo(360, 260, "ginocchio e la discesa a pendenza costante.", "sm"))
    return 680, 280, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Che cos'è un filtro
# ---------------------------------------------------------------------------------------------

def fig_filtro_setaccio():
    p = []
    ml, pw = 60, 560
    fcut = 500.0

    def X(f):
        return ml + (math.log10(f) - math.log10(30)) / (math.log10(30000) - math.log10(30)) * pw
    voci = [(100.0, 1.0, "segnale utile (100 Hz)", "a"), (3000.0, 0.45, "disturbo (3 kHz)", "w"), (12000.0, 0.55, "disturbo (12 kHz)", "w")]
    for k, (titolo, y0) in enumerate((("Prima del filtro", 30), ("Dopo il filtro (RC con f<sub>c</sub> = 500 Hz)", 200))):
        base = y0 + 120
        p.append(testo(ml, y0 - 6, titolo, "bd"))
        p.append(f'<line class="ax" x1="{ml}" y1="{base}" x2="{ml + pw}" y2="{base}"/>')
        for f in (100, 1000, 10000):
            p.append(f'<line class="ax" x1="{X(f):.1f}" y1="{base}" x2="{X(f):.1f}" y2="{base + 4}"/>' + testo(X(f), base + 16, f"{f} Hz" if f < 1000 else f"{f // 1000} kHz", "tick", "middle"))
        if k == 1:
            pts = [(f, abs(fc.h_rc_lp(f, fcut)) * 100) for f in fc.griglia_log(30, 30000, 120)]
            d = " ".join(("M" if i == 0 else "L") + f"{X(f):.1f} {base - v:.1f}" for i, (f, v) in enumerate(pts))
            p.append(f'<path class="sl sd dash" d="{d}"/>' + testo(ml + pw, base - 108, "risposta del filtro", "sm", "end"))
        for f, amp, nome, cls in voci:
            a = amp * (abs(fc.h_rc_lp(f, fcut)) if k == 1 else 1.0)
            p.append(freccia(X(f), base, X(f), base - 100 * a, "b" if cls == "a" else "w"))
            if k == 0:
                p.append(testo(X(f) + 6, base - 100 * a + 8, nome, "sm"))
            else:
                p.append(testo(X(f) + 8, base - 34, f"resta il {it(a * 100 / amp, 0)} %", "sm"))
    return 680, 370, "\n".join(p)


def fig_tipi_filtro():
    p = []
    xs = fc.griglia_log(0.05, 20, 300)
    q = 3.0

    def notch(x):
        return abs((1 - x * x) / (1 - x * x + 1j * x / q))
    reali = {
        "Passa-basso": [(x, abs(fc.h2_lp(x, 1.0, 1 / math.sqrt(2)))) for x in xs],
        "Passa-alto": [(x, abs(fc.h2_hp(x, 1.0, 1 / math.sqrt(2)))) for x in xs],
        "Passa-banda": [(x, abs(fc.h2_bp(x, 1.0, q))) for x in xs],
        "Elimina-banda (notch)": [(x, notch(x)) for x in xs],
    }
    ideali = {"Passa-basso": [(0.05, 1), (1, 1), (1, 0), (20, 0)], "Passa-alto": [(0.05, 0), (1, 0), (1, 1), (20, 1)],
              "Passa-banda": [(0.05, 0), (0.7, 0), (0.7, 1), (1.4, 1), (1.4, 0), (20, 0)], "Elimina-banda (notch)": [(0.05, 1), (0.7, 1), (0.7, 0), (1.4, 0), (1.4, 1), (20, 1)]}
    spiega = {"Passa-basso": "lascia passare il lento", "Passa-alto": "lascia passare il veloce", "Passa-banda": "lascia passare una fascia", "Elimina-banda (notch)": "toglie una fascia stretta"}
    pos = [(30, 30), (360, 30), (30, 190), (360, 190)]
    for (nome, rp), (x0, y0) in zip(reali.items(), pos):
        w, h = 290, 110
        p.append(testo(x0, y0 - 8, nome, "bd"))
        s, X, Y = _pannello(x0, y0, w, h, rp, 0.05, 20, 0, 1.15, "sa", xlog=True)
        idl = " ".join(("M" if i == 0 else "L") + f"{X(a):.1f} {Y(b):.1f}" for i, (a, b) in enumerate(ideali[nome]))
        p.append(s + f'<path class="sl sd dash" d="{idl}"/>')
        p.append(testo(x0 + w, y0 + h + 16, spiega[nome], "sm", "end"))
    p.append(testo(30, 346, "Tratteggio = filtro ideale (passa o blocca di netto). Linea piena = filtro reale: il passaggio è graduale.", "sm"))
    return 680, 362, "\n".join(p)


def fig_specifiche():
    xs = fc.griglia_log(100, 20000, 300)
    sez = fc.butterworth(3, 1000.0)
    curve = [("filtro reale (Butterworth, n = 3)", "sa", [(x, fc.db(fc.risposta_cascata(sez, x))) for x in xs])]
    aree = [(100, 1000, -100, 3, "fill-b"), (1000, 4000, -100, 3, "fill-c"), (4000, 20000, -100, 3, "fill-a")]
    w_, h_, inner = grafico_bode(curve, 100, 20000, -70, 6, [100, 200, 500, 1000, 2000, 5000, 10000, 20000], [-60, -40, -20, -3, 0],
                                 "ampiezza [dB]", "frequenza [Hz]", altezza=330, id_clip="spc", aree=aree, ref_y=[-3],
                                 annot=[(270, -62, "banda passante", "middle"), (1900, -62, "banda di transizione", "middle"), (9000, -62, "banda oscura (da bloccare)", "middle"),
                                        (130, -8, "qui il segnale", "start"), (130, -17, "passa quasi intatto", "start")])
    px, py = _mappa(100, 20000, -70, 6, 330, x_lin=False)
    ex = [f'<circle class="mrk" cx="{px(1000):.1f}" cy="{py(-3):.1f}" r="4"/>' + testo(px(1000) + 8, py(-3) - 8, "f<sub>c</sub>: −3 dB", "sm"),
          freccia(px(2000), py(-10), px(5000), py(-34), "w") + testo(px(5000) + 8, py(-34) + 4, "pendenza ≈ −60 dB/decade", "sm", "start")]
    return w_, h_, inner + "\n" + "\n".join(ex)


def fig_poli_pendenza():
    xs = fc.griglia_log(0.05, 50, 300)
    curve = [("1 polo: −20 dB/decade", "sa", [(x, fc.db(fc.h_rc_lp(x, 1.0) ** 1)) for x in xs]),
             ("2 poli uguali: −40 dB/decade", "sb", [(x, fc.db(fc.h_rc_lp(x, 1.0) ** 2)) for x in xs]),
             ("3 poli uguali: −60 dB/decade", "sc", [(x, fc.db(fc.h_rc_lp(x, 1.0) ** 3)) for x in xs])]
    return grafico_bode(curve, 0.05, 50, -80, 6, [0.1, 1, 10], [-60, -40, -20, 0], "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>",
                        id_clip="pp", altezza=300, legenda=True, annot=[(0.06, -50, "ogni polo in più", "start"), (0.06, -62, "aggiunge 20 dB/decade", "start")],
                        marcatori=[(10, -20, "", 0, 0), (10, -40, "", 0, 0), (10, -60, "", 0, 0)])


# ---------------------------------------------------------------------------------------------
# Esempi numerici annotati e operazionale
# ---------------------------------------------------------------------------------------------

def schema_rc_esempio():
    p = []
    f0 = fc.rc_fc(1600.0, 100e-9)
    p.append(_giunzione(40, 90) + testo(30, 78, "V<sub>in</sub>", "pin"))
    p.append('<line class="w" x1="40" y1="90" x2="80" y2="90"/>' + _res_h(80, 90) + '<line class="w" x1="136" y1="90" x2="260" y2="90"/>' + _giunzione(220, 90))
    p.append('<line class="w" x1="220" y1="90" x2="220" y2="115"/>' + _cap_v(220, 115, 180) + _gnd(220, 180) + _giunzione(260, 90) + testo(266, 84, "V<sub>out</sub>", "pin"))
    p.append(testo(108, 74, "R = 1,6 kΩ", "bd", "middle") + testo(206, 156, "C = 100 nF", "bd", "end"))
    passi = [("1", "Costante di tempo", f"τ = R · C = 1600 · 100·10⁻⁹ = {si(1600 * 100e-9, 's')}"),
             ("2", "Frequenza di taglio", f"f<sub>c</sub> = 1/(2πτ) = 1/(2π · 160·10⁻⁶) = {sig(f0, 4)} Hz"),
             ("3", "Attenuazione a 5 kHz", f"|H| = 1/√(1 + (5000/{sig(f0, 4)})²) = {it(abs(fc.h_rc_lp(5000.0, f0)), 3)}  →  {it(fc.db(fc.h_rc_lp(5000.0, f0)), 1)} dB"),
             ("4", "Fase a 5 kHz", f"φ = −arctan(5000/{sig(f0, 4)}) = {it(fc.fase_gradi(fc.h_rc_lp(5000.0, f0)), 1)}°")]
    for i, (n, t, f) in enumerate(passi):
        y = 36 + i * 52
        p.append(f'<circle class="r" cx="320" cy="{y + 8}" r="12"/>' + testo(320, y + 12, n, "bd", "middle"))
        p.append(testo(342, y + 4, t, "bd") + testo(342, y + 22, f, "sm"))
    return 680, 250, "\n".join(p)


def fig_barre_impedenza():
    p = []
    f0 = 1.0
    p.append(testo(20, 24, "R e condensatore in serie: chi «pesa» di più prende più tensione", "bd"))
    for i, x in enumerate((0.1, 1.0, 10.0)):
        y = 56 + i * 92
        xc = 1.0 / x
        h = fc.h_rc_lp(x, f0)
        esc = 18.0
        wr, wc = esc * 1.0, min(esc * xc, 190)
        p.append(testo(20, y + 24, f"f = {sig(x, 2).replace('.', ',')} f<sub>c</sub>", "bd"))
        p.append(f'<rect class="fill-a" x="130" y="{y}" width="{wr:.1f}" height="16"/><rect class="ax" x="130" y="{y}" width="{wr:.1f}" height="16"/>' + testo(130 + wr + 6, y + 12, "R = 1", "sm"))
        p.append(f'<rect class="fill-b" x="130" y="{y + 24}" width="{wc:.1f}" height="16"/><rect class="ax" x="130" y="{y + 24}" width="{wc:.1f}" height="16"/>' + testo(130 + wc + 6, y + 36, f"X<sub>C</sub> = {sig(xc, 3).replace('.', ',')}", "sm"))
        p.append(testo(400, y + 12, f"V<sub>out</sub>/V<sub>in</sub> = {it(abs(h) * 100, 1)} %", "bd"))
        comm = ["Il condensatore pesa molto: l'uscita segue l'ingresso.", "R e condensatore pesano uguale: l'uscita scende a 71 %.", "Il condensatore pesa poco: l'uscita è quasi cortocircuitata."][i]
        for j, r in enumerate(_spezza(comm, 40)):
            p.append(testo(400, y + 32 + 15 * j, r, "sm"))
    return 680, 330, "\n".join(p)


def schema_retroazione():
    p = []
    A, beta = 100000.0, 0.1
    g = A / (1 + A * beta)
    p.append(testo(20, 24, "Il segreto della reazione negativa", "ttl"))
    p.append(f'<circle class="r" cx="130" cy="110" r="16"/><text class="pin" x="123" y="115">+</text>' + testo(112, 97, MENO, "pin"))
    p.append(freccia(40, 110, 114, 110, "") + testo(40, 98, "V<sub>in</sub>", "pin"))
    p.append(freccia(146, 110, 230, 110, "") + riquadro(230, 80, 110, 60, "", "b", ["Amplificatore", "guadagno A"]))
    p.append(freccia(340, 110, 520, 110, "") + _giunzione(450, 110) + testo(520, 98, "V<sub>out</sub>", "pin"))
    p.append('<path class="w" d="M450 110 L450 190 L400 190"/>' + riquadro(250, 165, 150, 50, "", "w", ["Rete di reazione", "frazione β di V<sub>out</sub>"]))
    p.append('<path class="arw" d="M250 190 L130 190 L130 130"/>' + f'<path class="arw" d="{_testa(130, 150, 130, 127)}"/>')
    p.append(testo(20, 250, "L'amplificatore amplifica la differenza tra V<sub>in</sub> e la parte β V<sub>out</sub> riportata all'ingresso:", "sm"))
    p.append(testo(20, 268, "V<sub>out</sub> = A (V<sub>in</sub> − β V<sub>out</sub>)  →  V<sub>out</sub>/V<sub>in</sub> = A/(1 + Aβ)  ≈  1/β   se Aβ ≫ 1", "it"))
    p.append(testo(20, 292, f"Esempio: A = 100 000 e β = 0,1: guadagno = {it(g, 4)} ≈ 10. Il valore di A (quasi) non conta: conta solo β, cioè le resistenze.", "sm"))
    return 680, 312, "\n".join(p)


def schema_buffer_traduttore():
    p = []
    vs, rout, rin = 1.0, 10e3, 1e3
    v1 = vs * rin / (rout + rin)
    p.append(testo(20, 24, "Senza buffer", "ttl"))
    p.append(_sorgente(50, 85) + '<path class="w" d="M50 71 L50 55 L90 55"/><path class="w" d="M50 99 L50 120 L330 120"/>')
    p.append(_res_h(90, 55) + testo(118, 40, "R<sub>out</sub> = 10 kΩ", "sm", "middle") + '<line class="w" x1="146" y1="55" x2="300" y2="55"/><line class="w" x1="300" y1="55" x2="300" y2="75"/><rect class="r" x="292" y="75" width="16" height="30" rx="2"/><line class="w" x1="300" y1="105" x2="300" y2="120"/>')
    p.append(testo(318, 94, "carico 1 kΩ", "sm") + _giunzione(300, 55) + testo(260, 46, f"V = {it(v1 * 1000, 0)} mV", "bd", "end"))
    p.append(testo(360, 50, "Il carico «vede» la resistenza interna della sorgente", "sm") + testo(360, 68, f"e la tensione cala a {it(v1 * 100, 1)} % (partitore 1 kΩ su 11 kΩ).", "sm"))
    p.append(testo(20, 168, "Con buffer", "ttl"))
    p.append(_sorgente(50, 229) + '<path class="w" d="M50 215 L50 199 L90 199"/><path class="w" d="M50 243 L50 262 L460 262"/>')
    p.append(_res_h(90, 199) + testo(118, 184, "10 kΩ", "sm", "middle") + '<line class="w" x1="146" y1="199" x2="178" y2="199"/>')
    p.append(f'<path class="r" d="M178 179 L178 219 L218 199 Z"/><line class="w" x1="218" y1="199" x2="300" y2="199"/>' + testo(198, 232, "buffer", "sm", "middle"))
    p.append('<line class="w" x1="300" y1="199" x2="440" y2="199"/><line class="w" x1="440" y1="199" x2="440" y2="219"/><rect class="r" x="432" y="219" width="16" height="30" rx="2"/><line class="w" x1="440" y1="249" x2="440" y2="262"/>')
    p.append(testo(458, 238, "carico 1 kΩ", "sm") + testo(360, 190, f"V ≈ {it(vs * 1000 * 0.99, 0)} mV", "bd", "end"))
    p.append(testo(20, 292, "Il buffer ha ingresso ad alta impedenza (non carica la sorgente) e uscita a bassa impedenza (non risente del carico).", "sm"))
    return 680, 310, "\n".join(p)


def schema_sk_esempio():
    from disegno import schema_sk_lp
    w, h, inner = schema_sk_lp()
    s = fc.progetta_sezione_sk(1000.0, 1 / math.sqrt(2), 10e-9)
    p = [inner]
    p.append(testo(20, 318, f"R<sub>1</sub> = {si(s.r1, OHM)}   R<sub>2</sub> = {si(s.r2, OHM)}   C<sub>1</sub> = {si(s.c1, 'F')}   C<sub>2</sub> = {si(s.c2, 'F')}", "bd"))
    p.append(testo(20, 340, f"risultato: f<sub>0</sub> = {sig(s.f0, 4)} Hz   Q = {sig(s.q, 4)}  (obiettivo: 1000 Hz e 0,7071)", "sm"))
    return 680, 360, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Campionamento e oscilloscopio
# ---------------------------------------------------------------------------------------------

def fig_campionamento_alias():
    w_, h_, inner = 680, 300, ""
    ts = [i / 400 * 1.0 for i in range(401)]  # ms da 0 a 1
    f1, f2, fs = 1.0, 9.0, 10.0  # kHz
    c1 = [(t, math.cos(2 * math.pi * f1 * t)) for t in ts]
    c2 = [(t, math.cos(2 * math.pi * f2 * t)) for t in ts]
    w_, h_, inner = grafico_bode([("1 kHz", "sa", c1), ("9 kHz", "se dash", c2)], 0, 1, -1.3, 1.3, [0, 0.2, 0.4, 0.6, 0.8, 1.0], [-1, 0, 1],
                                 "tensione", "tempo [ms]", altezza=300, id_clip="cam", x_lin=True, ylab={-1: MENO + "1", 0: "0", 1: "1"},
                                 xlab={0: "0", 0.2: "0,2", 0.4: "0,4", 0.6: "0,6", 0.8: "0,8", 1.0: "1"})
    px, py = _mappa(0, 1, -1.3, 1.3, 300)
    pts = "".join(f'<circle class="mrk" cx="{px(n / fs):.1f}" cy="{py(math.cos(2 * math.pi * f1 * n / fs)):.1f}" r="4.5"/>' for n in range(0, 11))
    nota = [testo(px(0.5), py(1.22), "campioni ogni 0,1 ms (f<sub>s</sub> = 10 kHz): le due onde passano per gli stessi punti", "sm", "middle")]
    return w_, h_, inner + pts + "\n".join(nota)


def schermo_oscilloscopio():
    """Schermo 10 x 8 divisioni: V/div = 0,2 V, base tempi 0,2 ms/div, f = 1 kHz, passa-basso RC (fc = 995 Hz)."""
    p = []
    x0, y0, dv = 40, 20, 40
    larg, alt = 10 * dv, 8 * dv
    p.append(f'<rect class="box" x="{x0}" y="{y0}" width="{larg}" height="{alt}" rx="4"/>')
    for i in range(1, 10):
        p.append(f'<line class="grid" x1="{x0 + i * dv}" y1="{y0}" x2="{x0 + i * dv}" y2="{y0 + alt}"/>')
    for j in range(1, 8):
        p.append(f'<line class="grid" x1="{x0}" y1="{y0 + j * dv}" x2="{x0 + larg}" y2="{y0 + j * dv}"/>')
    cy = y0 + alt / 2
    h = fc.h_rc_lp(1000.0, fc.rc_fc(1600.0, 100e-9))
    amp_in, amp_out = 0.5 / 0.2 * dv, 0.5 * abs(h) / 0.2 * dv  # 1 Vpp = 5 div; picco 0,5 V
    fase = math.atan2(h.imag, h.real)

    def traccia(a, ph, cls):
        pts = []
        for i in range(0, 401):
            x = i / 400 * 10  # divisioni
            t_ms = x * 0.2
            pts.append((x0 + x * dv, cy - a * math.sin(2 * math.pi * 1.0 * t_ms + ph)))
        return f'<path class="sl {cls}" d="M' + " L".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in pts) + '"/>'
    p.append(traccia(amp_in, 0.0, "sa") + traccia(amp_out, fase, "sb"))
    # annotazioni
    pic_in = cy - amp_in
    p.append(f'<line class="ref" x1="{x0 + 2.25 * dv:.1f}" y1="{cy - amp_in:.1f}" x2="{x0 + 2.25 * dv:.1f}" y2="{cy + amp_in:.1f}"/>')
    p.append(freccia(x0 + 2.0 * dv, cy - amp_in, x0 + 2.0 * dv, cy + amp_in, "w", doppia=True))
    p.append(testo(x0 + 2.0 * dv - 6, cy - 6, "5 div", "sm", "end"))
    # ritardo
    xr = x0 + 5 * dv
    p.append(freccia(xr, cy, xr + 0.625 * dv, cy, "w", doppia=True))
    p.append(f'<line class="ref" x1="{xr}" y1="{cy - 1.0 * dv:.1f}" x2="{xr}" y2="{cy + 1.0 * dv:.1f}"/><line class="ref" x1="{xr + 0.625 * dv:.1f}" y1="{cy - 1.0 * dv:.1f}" x2="{xr + 0.625 * dv:.1f}" y2="{cy + 1.0 * dv:.1f}"/>')
    p.append(testo(xr + 0.625 * dv + 8, cy + 1.0 * dv + 4, "Δt ≈ 0,6 div", "sm"))
    # legenda e calcoli a destra
    lx = x0 + larg + 20
    p.append(testo(lx, 36, "Impostazioni", "bd") + testo(lx, 54, "CH1 (ingresso): 0,2 V/div", "sm") + testo(lx, 70, "CH2 (uscita): 0,2 V/div", "sm") + testo(lx, 86, "base tempi: 0,2 ms/div", "sm"))
    p.append(f'<line class="sl sa" x1="{lx}" y1="104" x2="{lx + 22}" y2="104"/>' + testo(lx + 28, 108, "ingresso", "sm") + f'<line class="sl sb" x1="{lx + 90}" y1="104" x2="{lx + 112}" y2="104"/>' + testo(lx + 118, 108, "uscita", "sm"))
    dt_ms = 0.625 * 0.2
    p.append(testo(lx, 140, "Come si legge", "bd"))
    p.append(testo(lx, 158, f"V<sub>pp</sub> ingresso = 5 div × 0,2 V = 1,0 V", "sm"))
    p.append(testo(lx, 174, f"V<sub>pp</sub> uscita ≈ 3,5 div × 0,2 V = {it(3.54 * 0.2, 2)} V", "sm"))
    p.append(testo(lx, 190, f"rapporto = {it(abs(h), 3)}  →  {it(fc.db(h), 2)} dB", "sm"))
    p.append(testo(lx, 214, f"periodo T = 5 div × 0,2 ms = 1 ms", "sm"))
    p.append(testo(lx, 230, f"Δt = {it(dt_ms, 3)} ms", "sm"))
    p.append(testo(lx, 246, f"φ = 360° × Δt/T = {it(360 * dt_ms / 1.0, 1)}° di ritardo", "sm"))
    return 680, 355, "\n".join(p)
