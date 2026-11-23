"""Primitive SVG: grafici di Bode, schemi elettrici e figure della dispensa."""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
from formati import sig  # noqa: E402


# ---------------------------------------------------------------------------------------------

def svgt(s):
    """Converte <sub>..</sub> in pedici SVG: un tag HTML dentro un <text> farebbe uscire il parser dall'SVG."""
    return re.sub(r"<sub>(.*?)</sub>", r"<tspan baseline-shift='sub' font-size='75%'>\1</tspan>", s)


def _fmt_tick(v):
    if abs(v) >= 1000 and float(v).is_integer():
        return f"{int(v / 1000)}k"
    if float(v).is_integer():
        return str(int(v))
    return sig(v, 3)


def grafico_bode(curve, xmin, xmax, ymin, ymax, xticks, yticks, ylabel, xlabel, altezza=300,
                 legenda_pos="alto-destra", id_clip="c", x_lin=False, ref_y=None,
                 ylab=None, xlab=None, aree=None, marcatori=None, annot=None, linee_v=None, legenda=True):
    """Grafico X (log o lineare) - Y con curve [(etichetta, classe, [(x, y), ...]), ...].

    ylab/xlab: dizionario valore -> etichetta (sostituisce la formattazione automatica dei tick).
    aree: [(x1, x2, y1, y2)] rettangoli vietati (maschera di specifica).
    marcatori: [(x, y, testo, dx, dy)] cerchi con etichetta spostata di (dx, dy) pixel.
    annot: [(x, y, testo, ancora)] testi liberi in coordinate dati.
    linee_v: [(x, testo)] linee verticali tratteggiate con etichetta in alto.
    """
    w, h = 680, altezza
    ml, mr, mt, mb = 58, 18, 40, 46
    pw, ph = w - ml - mr, h - mt - mb

    def px(x):
        if x_lin:
            return ml + (x - xmin) / (xmax - xmin) * pw
        return ml + (math.log10(x) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * pw

    def py(y):
        return mt + (ymax - y) / (ymax - ymin) * ph

    def etichetta(v, dizionario):
        if dizionario and v in dizionario:
            return dizionario[v]
        return _fmt_tick(v).replace("-", chr(0x2212))

    p = [f'<defs><clipPath id="{id_clip}"><rect x="{ml}" y="{mt}" width="{pw}" height="{ph}"/></clipPath></defs>']
    ultima = None
    for yv in yticks:
        p.append(f'<line class="grid" x1="{ml}" y1="{py(yv):.1f}" x2="{ml + pw}" y2="{py(yv):.1f}"/>')
        if ultima is None or abs(py(yv) - ultima) >= 13:
            p.append(f'<text class="tick" x="{ml - 8}" y="{py(yv) + 4:.1f}" text-anchor="end">{etichetta(yv, ylab)}</text>')
            ultima = py(yv)
    for xv in xticks:
        p.append(f'<line class="grid" x1="{px(xv):.1f}" y1="{mt}" x2="{px(xv):.1f}" y2="{mt + ph}"/>')
        p.append(f'<text class="tick" x="{px(xv):.1f}" y="{mt + ph + 16}" text-anchor="middle">{etichetta(xv, xlab)}</text>')
    p.append(f'<rect class="ax" x="{ml}" y="{mt}" width="{pw}" height="{ph}"/>')
    for ar in (aree or []):
        x1, x2, y1, y2 = ar[:4]
        cls_ar = ar[4] if len(ar) > 4 else "area"
        xa, xb = px(max(x1, xmin)), px(min(x2, xmax))
        ya, yb = py(min(y2, ymax)), py(max(y1, ymin))
        p.append(f'<rect class="{cls_ar}" clip-path="url(#{id_clip})" x="{xa:.1f}" y="{ya:.1f}" width="{xb - xa:.1f}" height="{yb - ya:.1f}"/>')
    if ref_y is not None:
        for r in ref_y:
            p.append(f'<line class="ref" x1="{ml}" y1="{py(r):.1f}" x2="{ml + pw}" y2="{py(r):.1f}"/>')
    for (xv, testo) in (linee_v or []):
        p.append(f'<line class="ref" x1="{px(xv):.1f}" y1="{mt}" x2="{px(xv):.1f}" y2="{mt + ph}"/>')
        p.append(f'<text class="tick" x="{px(xv) + 4:.1f}" y="{mt + 12}">{svgt(testo)}</text>')
    for _, cls, pts in curve:
        d = " ".join(("M" if i == 0 else "L") + f"{px(x):.1f} {py(max(min(y, ymax + 5), ymin - 5)):.1f}"
                     for i, (x, y) in enumerate(pts))
        p.append(f'<path class="sl {cls}" clip-path="url(#{id_clip})" d="{d}"/>')
    for m in (marcatori or []):
        xv, yv, testo, dx, dy = m[:5]
        ancora = m[5] if len(m) > 5 else "start"
        p.append(f'<circle class="mrk" cx="{px(xv):.1f}" cy="{py(yv):.1f}" r="4"/>')
        if testo:
            p.append(f'<text class="leg" x="{px(xv) + dx:.1f}" y="{py(yv) + dy:.1f}" text-anchor="{ancora}">{svgt(testo)}</text>')
    for (xv, yv, testo, ancora) in (annot or []):
        p.append(f'<text class="leg" x="{px(xv):.1f}" y="{py(yv):.1f}" text-anchor="{ancora}">{svgt(testo)}</text>')
    p.append(f'<text class="axl" x="{ml + pw / 2:.0f}" y="{h - 8}" text-anchor="middle">{svgt(xlabel)}</text>')
    p.append(f'<text class="axl" transform="translate(14 {mt + ph / 2:.0f}) rotate(-90)" text-anchor="middle">{svgt(ylabel)}</text>')
    if legenda:
        lx = ml
        for et, cls, _ in curve:
            p.append(f'<line class="sl {cls}" x1="{lx}" y1="{mt - 18}" x2="{lx + 22}" y2="{mt - 18}"/>')
            p.append(f'<text class="leg" x="{lx + 28}" y="{mt - 14}">{svgt(et)}</text>')
            lx += 28 + 7 * len(re.sub(r"<[^>]+>", "", et)) + 22
    return w, h, "\n".join(p)


def figura(num, titolo, desc, svg, vb, caption, cfg=""):
    w, h, inner = svg if isinstance(svg, tuple) else (vb[0], vb[1], svg)
    n = f"\u00a7{num}\u00a7"  # segnaposto: la numerazione definitiva segue l'ordine nella pagina
    return (f'<figure class="schema {cfg}"><div class="sheet"><span class="stamp">Fig. {n}</span>'
            f'<svg class="sch" viewBox="0 0 {w} {h}" role="img" aria-labelledby="f{n}-t f{n}-d">'
            f'<title id="f{n}-t">{re.sub(r"<[^>]+>", "", titolo)}</title><desc id="f{n}-d">{re.sub(r"<[^>]+>", "", desc)}</desc>\n{inner}\n</svg></div>'
            f'<figcaption><b>Fig. {n} \u2014 {titolo}.</b> {caption}</figcaption></figure>')


def serie_db(h_fun, fmin, fmax, n=240):
    return [(f, fc.db(h_fun(f))) for f in fc.griglia_log(fmin, fmax, n)]


def serie_fase(h_fun, fmin, fmax, n=240):
    return [(f, fc.fase_gradi(h_fun(f))) for f in fc.griglia_log(fmin, fmax, n)]


# ---------------------------------------------------------------------------------------------
# Schemi elettrici
# ---------------------------------------------------------------------------------------------

def _res_h(x, y, lung=56, alt=16):
    return f'<rect class="r" x="{x}" y="{y - alt // 2}" width="{lung}" height="{alt}" rx="2"/>'


def _gnd(x, y):
    return (f'<line class="w" x1="{x}" y1="{y}" x2="{x}" y2="{y + 6}"/>'
            f'<line class="w" x1="{x - 12}" y1="{y + 6}" x2="{x + 12}" y2="{y + 6}"/>'
            f'<line class="w" x1="{x - 8}" y1="{y + 11}" x2="{x + 8}" y2="{y + 11}"/>'
            f'<line class="w" x1="{x - 4}" y1="{y + 16}" x2="{x + 4}" y2="{y + 16}"/>')


def _cap_v(x, y1, y2):
    ym = (y1 + y2) // 2
    return (f'<line class="w" x1="{x}" y1="{y1}" x2="{x}" y2="{ym - 4}"/>'
            f'<line class="cap" x1="{x - 12}" y1="{ym - 4}" x2="{x + 12}" y2="{ym - 4}"/>'
            f'<line class="cap" x1="{x - 12}" y1="{ym + 4}" x2="{x + 12}" y2="{ym + 4}"/>'
            f'<line class="w" x1="{x}" y1="{ym + 4}" x2="{x}" y2="{y2}"/>')


def _cap_h(x1, x2, y):
    xm = (x1 + x2) // 2
    return (f'<line class="w" x1="{x1}" y1="{y}" x2="{xm - 4}" y2="{y}"/>'
            f'<line class="cap" x1="{xm - 4}" y1="{y - 12}" x2="{xm - 4}" y2="{y + 12}"/>'
            f'<line class="cap" x1="{xm + 4}" y1="{y - 12}" x2="{xm + 4}" y2="{y + 12}"/>'
            f'<line class="w" x1="{xm + 4}" y1="{y}" x2="{x2}" y2="{y}"/>')


def schema_rc():
    p = []
    # passa-basso: R in serie, C a massa
    p.append('<text class="ttl" x="20" y="28">Passa-basso</text>')
    p.append('<circle class="dot" cx="30" cy="80" r="3"/><text class="pin" x="22" y="68">V<tspan dy="3" font-size="9">in</tspan></text>')
    p.append('<line class="w" x1="30" y1="80" x2="80" y2="80"/>' + _res_h(80, 80))
    p.append('<line class="w" x1="136" y1="80" x2="250" y2="80"/>')
    p.append('<circle class="dot" cx="200" cy="80" r="3"/>' + _cap_v(200, 80, 130) + _gnd(200, 130))
    p.append('<circle class="dot" cx="250" cy="80" r="3"/><text class="pin" x="226" y="68">V<tspan dy="3" font-size="9">out</tspan></text>')
    p.append('<text x="108" y="64" text-anchor="middle">R</text><text x="224" y="110">C</text>')
    # passa-alto: C in serie, R a massa
    p.append('<text class="ttl" x="360" y="28">Passa-alto</text>')
    p.append('<circle class="dot" cx="370" cy="80" r="3"/><text class="pin" x="362" y="68">V<tspan dy="3" font-size="9">in</tspan></text>')
    p.append(_cap_h(370, 460, 80))
    p.append('<line class="w" x1="460" y1="80" x2="590" y2="80"/>')
    p.append('<circle class="dot" cx="540" cy="80" r="3"/><line class="w" x1="540" y1="80" x2="540" y2="100"/>'
             '<rect class="r" x="532" y="100" width="16" height="40" rx="2"/><line class="w" x1="540" y1="140" x2="540" y2="150"/>' + _gnd(540, 150))
    p.append('<circle class="dot" cx="590" cy="80" r="3"/><text class="pin" x="566" y="68">V<tspan dy="3" font-size="9">out</tspan></text>')
    p.append('<text x="415" y="64" text-anchor="middle">C</text><text x="564" y="124">R</text>')
    return 680, 200, "\n".join(p)


def schema_rlc():
    p = []
    p.append('<circle class="dot" cx="40" cy="70" r="3"/><text class="pin" x="26" y="58">V<tspan dy="3" font-size="9">in</tspan></text>')
    # induttore: quattro archi
    p.append('<line class="w" x1="40" y1="70" x2="100" y2="70"/>')
    p.append('<path class="w" d="M100 70 a14 14 0 0 1 28 0 a14 14 0 0 1 28 0 a14 14 0 0 1 28 0 a14 14 0 0 1 28 0"/>')
    p.append('<line class="w" x1="212" y1="70" x2="250" y2="70"/>')
    p.append(_cap_h(250, 330, 70))
    p.append('<line class="w" x1="330" y1="70" x2="390" y2="70"/>')
    p.append(_res_h(390, 70))
    p.append('<circle class="dot" cx="470" cy="70" r="3"/><line class="w" x1="446" y1="70" x2="470" y2="70"/>')
    p.append('<line class="w" x1="470" y1="70" x2="530" y2="70"/><circle class="dot" cx="530" cy="70" r="3"/>')
    p.append('<text class="pin" x="506" y="58">V<tspan dy="3" font-size="9">out</tspan></text>')
    p.append('<line class="w" x1="470" y1="70" x2="470" y2="130"/>' + _gnd(470, 130))
    p.append('<text x="156" y="48" text-anchor="middle">L</text><text x="290" y="46" text-anchor="middle">C</text>'
             '<text x="418" y="52" text-anchor="middle">R</text>')
    p.append('<text x="40" y="170">Uscita ai capi di R: passa-banda centrato su f₀ = 1/(2π√LC)</text>')
    return 680, 190, "\n".join(p)


def schema_sk_lp():
    p = []
    p.append('<circle class="dot" cx="30" cy="110" r="3"/><text class="pin" x="22" y="98">V<tspan dy="3" font-size="9">in</tspan></text>')
    p.append('<line class="w" x1="30" y1="110" x2="80" y2="110"/>' + _res_h(80, 110))
    p.append('<line class="w" x1="136" y1="110" x2="190" y2="110"/><circle class="dot" cx="190" cy="110" r="3"/>')
    p.append('<line class="w" x1="190" y1="110" x2="220" y2="110"/>' + _res_h(220, 110))
    p.append('<line class="w" x1="276" y1="110" x2="330" y2="110"/><circle class="dot" cx="330" cy="110" r="3"/>')
    p.append('<path class="w" d="M330 110 L330 90 L400 90"/>')
    # C2 a massa dal nodo B
    p.append('<line class="w" x1="330" y1="110" x2="330" y2="170"/>' + _cap_v(330, 170, 230) + _gnd(330, 230))
    # amplificatore operazionale (buffer)
    p.append('<path class="r" d="M400 60 L400 160 L500 110 Z"/>')
    p.append('<text class="pin" x="406" y="94">+</text><text class="pin" x="406" y="144">−</text>')
    p.append('<line class="w" x1="500" y1="110" x2="570" y2="110"/><circle class="dot" cx="540" cy="110" r="3"/>')
    p.append('<circle class="dot" cx="570" cy="110" r="3"/><text class="pin" x="546" y="98">V<tspan dy="3" font-size="9">out</tspan></text>')
    # reazione unitaria: uscita -> ingresso invertente
    p.append('<path class="w" d="M540 110 L540 270 L380 270 L380 140 L400 140"/>')
    # C1 dal nodo A all'uscita
    p.append('<path class="w" d="M190 110 L190 40 L340 40"/>' + _cap_h(340, 380, 40))
    p.append('<path class="w" d="M380 40 L540 40 L540 110"/>')
    p.append('<text x="108" y="94" text-anchor="middle">R1</text><text x="248" y="94" text-anchor="middle">R2</text>')
    p.append('<text x="360" y="26" text-anchor="middle">C1 (reazione)</text><text x="354" y="204">C2</text>')
    p.append('<text x="180" y="130" text-anchor="end">A</text><text x="322" y="130" text-anchor="end">B</text>')
    p.append('<text class="ttl" x="450" y="200" text-anchor="middle">K = 1</text>')
    return 680, 300, "\n".join(p)


def schema_sk_k(passa="lp"):
    """Sallen-Key a componenti uguali, guadagno K = 1 + Rf/Rg."""
    p = []
    p.append('<circle class="dot" cx="30" cy="110" r="3"/><text class="pin" x="22" y="98">V<tspan dy="3" font-size="9">in</tspan></text>')
    if passa == "lp":
        p.append('<line class="w" x1="30" y1="110" x2="80" y2="110"/>' + _res_h(80, 110))
        p.append('<line class="w" x1="136" y1="110" x2="190" y2="110"/><circle class="dot" cx="190" cy="110" r="3"/>')
        p.append('<line class="w" x1="190" y1="110" x2="220" y2="110"/>' + _res_h(220, 110))
        p.append('<line class="w" x1="276" y1="110" x2="330" y2="110"/><circle class="dot" cx="330" cy="110" r="3"/>')
        p.append('<line class="w" x1="330" y1="110" x2="330" y2="170"/>' + _cap_v(330, 170, 230) + _gnd(330, 230))
        p.append('<path class="w" d="M190 110 L190 40 L340 40"/>' + _cap_h(340, 380, 40))
        p.append('<path class="w" d="M380 40 L540 40 L540 110"/>')
        p.append('<text x="108" y="94" text-anchor="middle">R</text><text x="248" y="94" text-anchor="middle">R</text>')
        p.append('<text x="360" y="26" text-anchor="middle">C</text><text x="354" y="204">C</text>')
    else:
        p.append(_cap_h(30, 120, 110))
        p.append('<line class="w" x1="120" y1="110" x2="190" y2="110"/><circle class="dot" cx="190" cy="110" r="3"/>')
        p.append(_cap_h(190, 280, 110))
        p.append('<line class="w" x1="280" y1="110" x2="330" y2="110"/><circle class="dot" cx="330" cy="110" r="3"/>')
        p.append('<line class="w" x1="330" y1="110" x2="330" y2="130"/><rect class="r" x="322" y="130" width="16" height="40" rx="2"/>'
                 '<line class="w" x1="330" y1="170" x2="330" y2="180"/>' + _gnd(330, 180))
        p.append('<path class="w" d="M190 110 L190 40 L340 40"/>' + _res_h(340, 40))
        p.append('<path class="w" d="M396 40 L540 40 L540 110"/>')
        p.append('<text x="75" y="94" text-anchor="middle">C</text><text x="235" y="94" text-anchor="middle">C</text>')
        p.append('<text x="368" y="26" text-anchor="middle">R</text><text x="354" y="158">R</text>')
    p.append('<path class="w" d="M330 110 L330 90 L400 90"/>')
    p.append('<path class="r" d="M400 60 L400 160 L500 110 Z"/>')
    p.append('<text class="pin" x="406" y="94">+</text><text class="pin" x="406" y="144">−</text>')
    p.append('<line class="w" x1="500" y1="110" x2="610" y2="110"/><circle class="dot" cx="540" cy="110" r="3"/>')
    p.append('<circle class="dot" cx="610" cy="110" r="3"/><text class="pin" x="588" y="98">V<tspan dy="3" font-size="9">out</tspan></text>')
    # rete di guadagno Rg-Rf sull'ingresso invertente
    p.append('<path class="w" d="M540 110 L540 200"/><rect class="r" x="532" y="200" width="16" height="40" rx="2"/>'
             '<line class="w" x1="540" y1="240" x2="540" y2="262" />')
    p.append('<path class="w" d="M540 262 L380 262 L380 140 L400 140"/><circle class="dot" cx="440" cy="262" r="3"/>')
    p.append('<line class="w" x1="440" y1="262" x2="440" y2="276"/><rect class="r" x="432" y="276" width="16" height="30" rx="2"/>'
             '<line class="w" x1="440" y1="306" x2="440" y2="312"/>' + _gnd(440, 312))
    p.append('<text x="560" y="224">R<tspan dy="3" font-size="9">f</tspan></text>')
    p.append('<text x="458" y="296">R<tspan dy="3" font-size="9">g</tspan></text>')
    return 680, 340, "\n".join(p)


def hero_art():
    """Curve di Butterworth 1..4 per la testata (puramente decorativa)."""
    w, h, ml, mt, pw, ph = 520, 300, 30, 20, 430, 230

    def px(f):
        return ml + (math.log10(f) + 1.0) / 2.0 * pw

    def py(d):
        return mt + (3.0 - d) / 83.0 * ph

    p = []
    for n, cls in ((1, "hw"), (2, "hw"), (3, "hw"), (4, "hwp")):
        sez = fc.butterworth(n, 1.0)
        pts = [(f, fc.db(fc.risposta_cascata(sez, f))) for f in fc.griglia_log(0.1, 10.0, 90)]
        d = " ".join(("M" if i == 0 else "L") + f"{px(f):.1f} {py(max(v, -80)):.1f}" for i, (f, v) in enumerate(pts))
        p.append(f'<path class="{cls}" d="{d}"/>')
        y_fine = py(max(fc.db(fc.risposta_cascata(sez, 10.0)), -80))
        p.append(f'<text class="{"hl" if n == 4 else ""}" x="{px(10.0) + 8:.0f}" y="{y_fine + 4:.0f}">n = {n}</text>')
    p.append(f'<path class="hw" d="M{px(1.0):.1f} {mt} V{mt + ph}" stroke-dasharray="3 5"/>')
    p.append(f'<text x="{px(1.0) + 6:.0f}" y="{mt + 14}">f<tspan dy="3" font-size="10">c</tspan></text>')
    p.append(f'<text x="{ml}" y="{mt + ph + 26}">0,1 f<tspan dy="3" font-size="10">c</tspan></text>'
             f'<text x="{ml + pw}" y="{mt + ph + 26}" text-anchor="end">10 f<tspan dy="3" font-size="10">c</tspan></text>')
    return f'<svg class="hero-art" viewBox="0 0 {w} {h}" role="img" aria-label="Risposta in ampiezza di filtri Butterworth passa-basso dal primo al quarto ordine">' + "\n".join(p) + "</svg>"


