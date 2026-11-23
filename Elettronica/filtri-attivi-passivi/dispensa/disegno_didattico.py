"""Diagrammi didattici della dispensa: fasori, piano s, schemi di misura, aliasing, flussi di lavoro.

Ogni funzione restituisce la tripla (larghezza, altezza, contenuto SVG) accettata da `figura()`.
Le curve sono calcolate con src/filtri_core.py; gli schemi sono disegnati a coordinate fisse.
"""
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
from disegno import _cap_h, _cap_v, _gnd, _res_h, grafico_bode, serie_db, svgt
from formati import it, sig  # noqa: E402
from parametri import RC_C, RC_R, RLC_C, RLC_L, SK_C2, SK_FC

MENO = "−"


# ---------------------------------------------------------------------------------------------
# Primitive
# ---------------------------------------------------------------------------------------------

def _testa(x1, y1, x2, y2, lung=9, apertura=0.45):
    """Punta di freccia in (x2, y2) per un segmento che arriva da (x1, y1)."""
    ang = math.atan2(y2 - y1, x2 - x1)
    a = (x2 - lung * math.cos(ang - apertura), y2 - lung * math.sin(ang - apertura))
    b = (x2 - lung * math.cos(ang + apertura), y2 - lung * math.sin(ang + apertura))
    return f'M{a[0]:.1f} {a[1]:.1f} L{x2:.1f} {y2:.1f} L{b[0]:.1f} {b[1]:.1f}'


def freccia(x1, y1, x2, y2, cls="", doppia=False):
    s = f'<path class="arw {cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} {_testa(x1, y1, x2, y2)}'
    if doppia:
        s += f' {_testa(x2, y2, x1, y1)}'
    return s + '"/>'


def testo(x, y, s, cls="", ancora="start"):
    c = f' class="{cls}"' if cls else ""
    return f'<text{c} x="{x:.1f}" y="{y:.1f}" text-anchor="{ancora}">{svgt(s)}</text>'


def riquadro(x, y, w, h, s, cls="", righe=None):
    """Riquadro con testo centrato (una o più righe)."""
    righe = righe or [s]
    out = [f'<rect class="box {cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>']
    n = len(righe)
    for i, r in enumerate(righe):
        yy = y + h / 2 + (i - (n - 1) / 2) * 15 + 4
        out.append(f'<text class="{"bd" if i == 0 else "sm"}" x="{x + w / 2:.1f}" y="{yy:.1f}" text-anchor="middle">{svgt(r)}</text>')
    return "".join(out)


def _opamp(x, y, w=70, h=84):
    """Triangolo dell'operazionale con vertice di uscita a destra; ritorna (svg, pin+, pin-, uscita)."""
    svg = f'<path class="r" d="M{x} {y} L{x} {y + h} L{x + w} {y + h / 2} Z"/>'
    svg += f'<text class="pin" x="{x + 6}" y="{y + h * 0.3 + 4:.0f}">+</text><text class="pin" x="{x + 6}" y="{y + h * 0.7 + 4:.0f}">{MENO}</text>'
    return svg, (x, y + h * 0.3), (x, y + h * 0.7), (x + w, y + h / 2)


def _sorgente(x, y, r=14):
    """Generatore di tensione sinusoidale (cerchio con onda)."""
    return (f'<circle class="r" cx="{x}" cy="{y}" r="{r}"/>'
            f'<path class="w" d="M{x - 8} {y} q4 -8 8 0 t8 0"/>')


def _giunzione(x, y):
    return f'<circle class="dot" cx="{x}" cy="{y}" r="3"/>'


def _mappa(xmin, xmax, ymin, ymax, altezza, x_lin=True):
    """Stessa mappatura dati -> pixel di grafico_bode (per sovrapporre annotazioni)."""
    ml, mr, mt, mb = 58, 18, 40, 46
    pw, ph = 680 - ml - mr, altezza - mt - mb

    def px(x):
        if x_lin:
            return ml + (x - xmin) / (xmax - xmin) * pw
        return ml + (math.log10(x) - math.log10(xmin)) / (math.log10(xmax) - math.log10(xmin)) * pw

    def py(y):
        return mt + (ymax - y) / (ymax - ymin) * ph
    return px, py


# ---------------------------------------------------------------------------------------------
# Fondamenti
# ---------------------------------------------------------------------------------------------

def fig_luogo_rc():
    """Piano complesso: luogo di H(jω), con ω = 2πf, del passa-basso RC."""
    ox, oy, s = 100, 130, 250  # origine e pixel per unità
    sub = lambda t: f"<sub>{t}</sub>"  # noqa: E731

    def P(re_, im):
        return ox + s * re_, oy - s * im

    p = []
    p.append(f'<line class="ax" x1="{ox - 50}" y1="{oy}" x2="{ox + s + 50}" y2="{oy}"/>')
    p.append(f'<line class="ax" x1="{ox}" y1="{oy - 70}" x2="{ox}" y2="{oy + s * 0.5 + 60}"/>')
    p.append(testo(ox + s + 50, oy + 14, "Re", "tick", "end"))
    p.append(testo(ox + 8, oy - 58, "Im", "tick"))
    pts = []
    for i in range(0, 201):
        x = 10 ** (-2 + 4 * i / 200)
        h = fc.h_rc_lp(x, 1.0)
        pts.append(P(h.real, h.imag))
    p.append('<path class="sl sa" d="M' + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + '"/>')
    posizioni = {0.25: (12, 4, "start"), 0.5: (12, 18, "start"), 1.0: (0, 34, "middle"), 2.0: (-12, 20, "end"), 4.0: (-12, 4, "end")}
    for x, (dx, dy, anc) in posizioni.items():
        h = fc.h_rc_lp(x, 1.0)
        a, b = P(h.real, h.imag)
        p.append(f'<circle class="mrk" cx="{a:.1f}" cy="{b:.1f}" r="3.5"/>')
        p.append(testo(a + dx, b + dy, f"f/f{sub('c')} = {sig(x, 3).replace('.', ',')}", "tick", anc))
    h1 = fc.h_rc_lp(1.0, 1.0)
    ax, ay = P(1.0, 0)
    bx, by = P(h1.real, h1.imag)
    p.append(freccia(ox, oy, ax, ay, "a"))
    p.append(freccia(ox, oy, bx, by, "b"))
    p.append(freccia(bx, by, ax, ay, "c"))
    p.append(testo(ax + 4, ay - 10, f"V{sub('in')} = 1", "pin", "end"))
    p.append(testo((ox + bx) / 2 + 12, (oy + by) / 2 - 8, f"V{sub('C')} = V{sub('out')}", "pin"))
    p.append(testo((bx + ax) / 2 + 10, (by + ay) / 2 - 6, f"V{sub('R')}", "pin"))
    r = 46
    p.append(f'<path class="arw" d="M{ox + r} {oy} A{r} {r} 0 0 1 {ox + r * math.cos(math.radians(45)):.1f} {oy + r * math.sin(math.radians(45)):.1f}"/>')
    p.append(testo(ox + r + 6, oy + 24, f"\u03c6 = {MENO}45\u00b0", "pin"))
    tx = 440
    p.append(testo(tx, 36, "Come leggere il diagramma", "bd"))
    righe = ["Ogni punto del semicerchio è H(jω), ω = 2πf",
             "per una frequenza diversa:",
             "f = 0 \u2192 punto 1: nessuna attenuazione;",
             "f \u2192 \u221e \u2192 punto 0: uscita nulla.",
             "",
             f"A f = f{sub('c')}:",
             f"|V{sub('C')}| = |V{sub('R')}| = 0,707 V{sub('in')}",
             f"V{sub('C')} e V{sub('R')} sono a 90\u00b0, quindi",
             f"V{sub('in')} è l'ipotenusa di un triangolo",
             "rettangolo isoscele: la fase di V" + sub("out"),
             f"rispetto a V{sub('in')} è {MENO}45\u00b0."]
    for i, r_ in enumerate(righe):
        p.append(testo(tx, 58 + 17 * i, r_, "sm"))
    return 680, 320, "\n".join(p)


def fig_oscillogramma():
    """Ingresso e uscita del passa-basso RC a f = fc: ampiezza 0,707 e ritardo T/8."""
    n = 400
    ymin, ymax, h = -1.45, 1.45, 300
    ing = [(2 * i / n, math.sin(2 * math.pi * 2 * i / n)) for i in range(n + 1)]
    h1 = fc.h_rc_lp(1.0, 1.0)
    usc = [(2 * i / n, abs(h1) * math.sin(2 * math.pi * 2 * i / n + math.atan2(h1.imag, h1.real))) for i in range(n + 1)]
    w_, h_, inner = grafico_bode([("V<sub>in</sub>", "sa", ing), ("V<sub>out</sub>", "sb", usc)], 0, 2, ymin, ymax,
                                 [0, 0.5, 1, 1.5, 2], [-1, 0, 1], "tensione [V]", "tempo [periodi T]", altezza=h,
                                 id_clip="osc", x_lin=True, ylab={-1: MENO + "1", 0: "0", 1: "1"},
                                 xlab={0: "0", 0.5: "T/2", 1: "T", 1.5: "3T/2", 2: "2T"})
    px, py = _mappa(0, 2, ymin, ymax, h)
    ex = []
    dt = 1 / 8
    ex.append(freccia(px(0), py(-1.25), px(dt), py(-1.25), "w", doppia=True))
    ex.append(f'<line class="ref" x1="{px(0):.1f}" y1="{py(0):.1f}" x2="{px(0):.1f}" y2="{py(-1.3):.1f}"/>')
    ex.append(f'<line class="ref" x1="{px(dt):.1f}" y1="{py(0):.1f}" x2="{px(dt):.1f}" y2="{py(-1.3):.1f}"/>')
    ex.append(testo(px(dt) + 6, py(-1.25) + 4, "Δt = T/8 → φ = 360° · Δt/T = 45° di ritardo", "sm"))
    ex.append(testo(px(1.75), py(abs(h1)) - 6, "0,707", "tick", "middle"))
    ex.append(testo(px(1.25), py(1) - 6, "1", "tick", "middle"))
    return w_, h_, inner + "\n" + "\n".join(ex)


def fig_bode_asintotico():
    xs = fc.griglia_log(0.01, 100, 240)
    reale = [(x, fc.db(fc.h_rc_lp(x, 1.0))) for x in xs]
    asint = [(x, 0.0 if x <= 1 else -20 * math.log10(x)) for x in xs]
    d05, d2 = fc.db(fc.h_rc_lp(0.5, 1.0)), fc.db(fc.h_rc_lp(2.0, 1.0))
    marc = [(1.0, fc.db(fc.h_rc_lp(1.0, 1.0)), f"in f/f<sub>c</sub> = 1: {it(fc.db(fc.h_rc_lp(1.0, 1.0)))} dB, scarto di 3 dB dagli asintoti", -14, 22, "end"),
            (0.5, d05, "", 0, 0), (2.0, d2, "", 0, 0)]
    return grafico_bode([("risposta reale", "sa", reale), ("asintoti: 0 dB e \u221220 dB/decade", "sd dash", asint)],
                        0.01, 100, -42, 4, [0.01, 0.1, 1, 10, 100], [-40, -30, -20, -10, 0],
                        "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", id_clip="asi", marcatori=marc)


# ---------------------------------------------------------------------------------------------
# Parte I: passivi
# ---------------------------------------------------------------------------------------------

def fig_reattanza_rc():
    """XC(f) e R sullo stesso grafico log-log: si incontrano alla frequenza di taglio."""
    xs = fc.griglia_log(30, 30000, 200)
    xc = [(f, math.log10(1 / (2 * math.pi * f * RC_C))) for f in xs]
    r = [(f, math.log10(RC_R)) for f in (30, 30000)]
    fcut = fc.rc_fc(RC_R, RC_C)
    ticks = {1: "10 Ω", 2: "100 Ω", 3: "1 kΩ", 4: "10 kΩ", 5: "100 kΩ"}
    return grafico_bode([("X<sub>C</sub> = 1/(2πfC), C = 100 nF", "sb", xc), ("R = 1,6 kΩ", "sa dash", r)],
                        30, 30000, 1.5, 4.5, [100, 1000, 10000], [2, 3, 4], "impedenza |Z|", "frequenza [Hz]",
                        id_clip="rea", ylab=ticks, x_lin=False,
                        marcatori=[(fcut, math.log10(RC_R), f"X<sub>C</sub> = R a {sig(fcut, 4)} Hz = f<sub>c</sub>", 10, -10)],
                        annot=[(34, 2.0, "X<sub>C</sub> \u226b R: V<sub>out</sub> \u2248 V<sub>in</sub>", "start"),
                               (28000, 3.85, "X<sub>C</sub> \u226a R: C cortocircuita l'uscita", "end")])


def fig_gradino_rc():
    xs = [i * 6 / 240 for i in range(241)]
    y = [(x, 1 - math.exp(-x)) for x in xs]
    tang = [(0, 0), (1, 1)]
    marc = []
    for k in (1, 2, 3, 4, 5):
        v = 1 - math.exp(-k)
        marc.append((k, v, f"{k}τ: {it(v * 100, 1)} %", 6, 22 if k == 1 else 20))
    return grafico_bode([("V<sub>out</sub>/V<sub>in</sub> dopo un gradino", "sa", y), ("tangente in t = 0", "sd dash", tang)],
                        0, 6, 0, 1.08, [0, 1, 2, 3, 4, 5, 6], [0, 0.25, 0.5, 0.75, 1], "V<sub>out</sub> / V<sub>in</sub>",
                        "tempo t / τ, τ = RC", id_clip="grd", x_lin=True, marcatori=marc,
                        ylab={0: "0", 0.25: "0,25", 0.5: "0,5", 0.75: "0,75", 1: "1"})


def schema_thevenin():
    p = []
    # circuito originale
    p.append(testo(20, 24, "Circuito reale", "ttl"))
    p.append(_sorgente(50, 110) + testo(24, 80, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append('<path class="w" d="M50 96 L50 70 L90 70"/><path class="w" d="M50 124 L50 190 L300 190"/>')
    p.append(_res_h(90, 70) + '<line class="w" x1="146" y1="70" x2="300" y2="70"/>' + testo(118, 54, "R", "", "middle"))
    p.append(_giunzione(190, 70) + '<line class="w" x1="190" y1="70" x2="190" y2="100"/>')
    p.append(_cap_v(190, 100, 190) + _giunzione(190, 190))
    p.append(_giunzione(260, 70) + '<line class="w" x1="260" y1="70" x2="260" y2="100"/>'
             '<rect class="r" x="252" y="100" width="16" height="50" rx="2"/><line class="w" x1="260" y1="150" x2="260" y2="190"/>' + _giunzione(260, 190))
    p.append(testo(170, 150, "C", "", "end") + testo(280, 130, "R<tspan dy='3' font-size='9'>L</tspan>"))
    p.append(f'<circle class="dot" cx="300" cy="70" r="3"/>' + testo(306, 62, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    # freccia
    p.append(freccia(340, 120, 380, 120, "a"))
    p.append(testo(360, 104, "Thevenin", "sm", "middle") + testo(360, 140, "visto da C", "sm", "middle"))
    # equivalente
    p.append(testo(400, 24, "Equivalente visto dal condensatore", "ttl"))
    p.append(_sorgente(430, 110) + testo(398, 80, "V<tspan dy='3' font-size='9'>th</tspan>", "pin"))
    p.append('<path class="w" d="M430 96 L430 70 L470 70"/><path class="w" d="M430 124 L430 190 L640 190"/>')
    p.append(_res_h(470, 70) + '<line class="w" x1="526" y1="70" x2="640" y2="70"/>' + testo(498, 54, "R<tspan dy='3' font-size='9'>th</tspan>", "", "middle"))
    p.append(_giunzione(590, 70) + '<line class="w" x1="590" y1="70" x2="590" y2="100"/>' + _cap_v(590, 100, 190) + _giunzione(590, 190))
    p.append(testo(570, 150, "C", "", "end"))
    p.append(f'<circle class="dot" cx="640" cy="70" r="3"/>' + testo(646, 62, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    p.append(testo(20, 232, "V<tspan dy='3' font-size='9'>th</tspan> = V<tspan dy='3' font-size='9'>in</tspan> · R<tspan dy='3' font-size='9'>L</tspan>/(R + R<tspan dy='3' font-size='9'>L</tspan>)", "it"))
    p.append(testo(280, 232, "R<tspan dy='3' font-size='9'>th</tspan> = R ∥ R<tspan dy='3' font-size='9'>L</tspan> = R R<tspan dy='3' font-size='9'>L</tspan>/(R + R<tspan dy='3' font-size='9'>L</tspan>)", "it"))
    p.append(testo(20, 258, "Il filtro è di nuovo un semplice RC: ha guadagno V<tspan dy='3' font-size='9'>th</tspan>/V<tspan dy='3' font-size='9'>in</tspan> in continua e f<tspan dy='3' font-size='9'>c</tspan><tspan dy='-3'>′ = 1/(2π R</tspan><tspan dy='3' font-size='9'>th</tspan><tspan dy='-3'> C).</tspan>", "sm"))
    return 680, 272, "\n".join(p)


def schema_cascata_rc():
    p = []
    # cascata diretta
    p.append(testo(20, 24, "Cascata diretta: la seconda cella carica la prima", "ttl"))
    y = 80
    p.append(_giunzione(30, y) + testo(22, y - 12, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(f'<line class="w" x1="30" y1="{y}" x2="70" y2="{y}"/>' + _res_h(70, y) + f'<line class="w" x1="126" y1="{y}" x2="320" y2="{y}"/>')
    p.append(_giunzione(180, y) + _cap_v(180, y, y + 70) + _gnd(180, y + 70))
    p.append(testo(98, y - 16, "R<tspan dy='3' font-size='9'>1</tspan>", "", "middle") + testo(166, y + 40, "C<tspan dy='3' font-size='9'>1</tspan>", "", "end"))
    p.append(f'<line class="w" x1="250" y1="{y}" x2="250" y2="{y}"/>' + _res_h(230, y))
    p.append(f'<line class="w" x1="286" y1="{y}" x2="400" y2="{y}"/>' + _giunzione(340, y) + _cap_v(340, y, y + 70) + _gnd(340, y + 70))
    p.append(testo(258, y - 16, "R<tspan dy='3' font-size='9'>2</tspan>", "", "middle") + testo(326, y + 40, "C<tspan dy='3' font-size='9'>2</tspan>", "", "end"))
    p.append(_giunzione(400, y) + testo(406, y - 8, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    p.append(freccia(196, y - 24, 220, y - 24, "w") + testo(208, y - 32, "I<tspan dy='3' font-size='9'>2</tspan>", "pin", "middle"))
    p.append(testo(440, y - 10, "La corrente I<tspan dy='3' font-size='9'>2</tspan><tspan dy='-3'> sottratta al nodo di C</tspan><tspan dy='3' font-size='9'>1</tspan>", "sm"))
    p.append(testo(440, y + 8, "cambia la tensione ai capi di C<tspan dy='3' font-size='9'>1</tspan><tspan dy='-3'>:</tspan>", "sm"))
    p.append(testo(440, y + 26, "le due celle non sono indipendenti.", "sm"))
    # cascata con buffer
    y2 = 262
    p.append(testo(20, 196, "Cascata con buffer: le celle sono indipendenti", "ttl"))
    p.append(_giunzione(30, y2) + testo(22, y2 - 12, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(f'<line class="w" x1="30" y1="{y2}" x2="60" y2="{y2}"/>' + _res_h(60, y2) + f'<line class="w" x1="116" y1="{y2}" x2="160" y2="{y2}"/>')
    p.append(_giunzione(140, y2) + _cap_v(140, y2, y2 + 56) + _gnd(140, y2 + 56))
    p.append(f'<path class="r" d="M160 {y2 - 20} L160 {y2 + 20} L200 {y2} Z"/><line class="w" x1="200" y1="{y2}" x2="230" y2="{y2}"/>')
    p.append(_res_h(230, y2) + f'<line class="w" x1="286" y1="{y2}" x2="400" y2="{y2}"/>' + _giunzione(340, y2) + _cap_v(340, y2, y2 + 56) + _gnd(340, y2 + 56))
    p.append(_giunzione(400, y2) + testo(406, y2 - 8, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    p.append(testo(440, y2 - 10, "Il buffer (guadagno 1, ingresso ad alta", "sm") + testo(440, y2 + 8, "impedenza, uscita a bassa) isola le celle:", "sm") + testo(440, y2 + 26, "H = H<sub>1</sub> \u00b7 H<sub>2</sub>", "sm"))
    p.append(testo(98, y2 - 16, "R<sub>1</sub>", "", "middle") + testo(258, y2 - 16, "R<sub>2</sub>", "", "middle")
             + testo(126, y2 + 40, "C<sub>1</sub>", "", "end") + testo(326, y2 + 40, "C<sub>2</sub>", "", "end"))
    return 680, 350, "\n".join(p)


def schema_zout_zin():
    p = []
    p.append(_sorgente(50, 100) + testo(30, 70, "V<tspan dy='3' font-size='9'>s</tspan>", "pin"))
    p.append('<path class="w" d="M50 86 L50 60 L100 60"/>' + _res_h(100, 60) + '<line class="w" x1="156" y1="60" x2="260" y2="60"/>')
    p.append(testo(128, 44, "Z<tspan dy='3' font-size='9'>out</tspan>", "", "middle"))
    p.append(_giunzione(230, 60) + '<line class="w" x1="230" y1="60" x2="230" y2="80"/><rect class="r" x="222" y="80" width="16" height="50" rx="2"/><line class="w" x1="230" y1="130" x2="230" y2="160"/>')
    p.append(testo(250, 112, "Z<tspan dy='3' font-size='9'>in</tspan>") + '<path class="w" d="M50 114 L50 160 L260 160"/>' + _giunzione(230, 160))
    p.append(f'<circle class="dot" cx="260" cy="60" r="3"/>' + testo(266, 54, "V<tspan dy='3' font-size='9'>x</tspan>", "pin"))
    p.append(testo(320, 54, "Partitore: V<tspan dy='3' font-size='9'>x</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>s</tspan><tspan dy='-3'> · Z</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>/(Z</tspan><tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> + Z</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>)</tspan>", "it"))
    p.append(testo(320, 82, "Se Z<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> ≥ 10 Z</tspan><tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>: l'errore è ≤ 9 %.</tspan>", "sm"))
    p.append(testo(320, 100, "Se Z<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> ≥ 100 Z</tspan><tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>: l'errore è ≤ 1 %.</tspan>", "sm"))
    p.append(testo(320, 124, "Nel filtro RC Z<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> è la resistenza R (più C in parallelo),</tspan>", "sm"))
    p.append(testo(320, 142, "Z<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> è l'impedenza del carico.</tspan>", "sm"))
    return 680, 190, "\n".join(p)


def fig_reattanze_lc():
    xs = fc.griglia_log(100, 100000, 200)
    xl = [(f, math.log10(2 * math.pi * f * RLC_L)) for f in xs]
    xc = [(f, math.log10(1 / (2 * math.pi * f * RLC_C))) for f in xs]
    r = fc.RlcSerie(100.0, RLC_L, RLC_C)
    z0 = math.sqrt(RLC_L / RLC_C)
    ticks = {0: "1 Ω", 1: "10 Ω", 2: "100 Ω", 3: "1 kΩ", 4: "10 kΩ"}
    return grafico_bode([("X<sub>L</sub> = 2πfL (10 mH)", "sa", xl), ("X<sub>C</sub> = 1/(2πfC) (100 nF)", "sb", xc),
                         ("R = 100 Ω", "sd dash", [(100, 2), (100000, 2)])],
                        100, 100000, 0.5, 4.3, [100, 1000, 10000, 100000], [1, 2, 3, 4], "reattanza |X|", "frequenza [Hz]",
                        id_clip="lc", ylab=ticks,
                        marcatori=[(r.f0, math.log10(z0), f"f<sub>0</sub> = {sig(r.f0, 4)} Hz: X<sub>L</sub> = X<sub>C</sub> = {sig(z0, 3)} Ω", 12, -10)],
                        annot=[(110, 3.0, "sotto f<sub>0</sub> prevale C", "start"),
                               (95000, 2.55, "sopra f<sub>0</sub> prevale L", "end")])


def fig_fasori_risonanza(q=None):
    q = q or fc.RlcSerie(100.0, RLC_L, RLC_C).q
    ox, oy, u = 90, 170, 52  # unità di pixel per V_in
    p = []
    p.append(f'<line class="ax" x1="{ox - 30}" y1="{oy}" x2="{ox + 280}" y2="{oy}"/><line class="ax" x1="{ox}" y1="{oy - 150}" x2="{ox}" y2="{oy + 150}"/>')
    p.append(freccia(ox, oy, ox + u, oy, "a") + testo(ox + u + 8, oy + 4, "V<tspan dy='3' font-size='9'>R</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(freccia(ox, oy, ox, oy - q * u, "b") + testo(ox + 8, oy - q * u + 10, f"V<tspan dy='3' font-size='9'>L</tspan><tspan dy='-3'> = +jQ V</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>   (Q = {it(q, 2)})</tspan>", "pin"))
    p.append(freccia(ox, oy, ox, oy + q * u, "c") + testo(ox + 8, oy + q * u - 4, "V<tspan dy='3' font-size='9'>C</tspan><tspan dy='-3'> = −jQ V</tspan><tspan dy='3' font-size='9'>in</tspan>", "pin"))
    tx = ox + 300
    p.append(testo(tx, 40, "Alla risonanza (f = f<tspan dy='3' font-size='9'>0</tspan><tspan dy='-3'>)</tspan>", "bd"))
    righe = ["X<tspan dy='3' font-size='9'>L</tspan><tspan dy='-3'> = X</tspan><tspan dy='3' font-size='9'>C</tspan><tspan dy='-3'> = √(L/C):</tspan>",
             "le due reattanze sono uguali e opposte,",
             "quindi V<tspan dy='3' font-size='9'>L</tspan><tspan dy='-3'> + V</tspan><tspan dy='3' font-size='9'>C</tspan><tspan dy='-3'> = 0 e la corrente</tspan>",
             "è limitata solo da R: I = V<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>/R.</tspan>",
             "",
             "Le tensioni su L e C valgono Q volte V<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>:</tspan>",
             f"con V<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> = 1 V e Q = {it(q, 2)}</tspan>",
             f"su L e su C ci sono {it(q, 2)} V.",
             "Con Q alti conta la tensione massima",
             "del condensatore e dell'induttore."]
    for i, r in enumerate(righe):
        p.append(testo(tx, 62 + 17 * i, r, "sm"))
    return 680, 340, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Laboratorio
# ---------------------------------------------------------------------------------------------

def schema_collegamento_lab():
    p = []
    y = 70
    p.append(testo(40, 30, "Generatore", "ttl"))
    p.append(_sorgente(60, 114) + '<path class="w" d="M60 128 L60 205"/><path class="w" d="M60 100 L60 70 L100 70"/>')
    p.append(_res_h(100, y) + testo(128, 54, "R<sub>s</sub> \u2248 50 \u03a9", "sm", "middle"))
    p.append('<line class="w" x1="156" y1="70" x2="250" y2="70"/>' + _giunzione(230, 70))
    p.append(riquadro(250, 40, 130, 60, "", "b", ["Circuito in prova", "(filtro)"]))
    p.append('<line class="w" x1="380" y1="70" x2="500" y2="70"/>' + _giunzione(430, 70))
    p.append('<line class="w" x1="315" y1="100" x2="315" y2="205"/>')
    p.append(testo(236, 62, "P", "pin") + testo(436, 62, "Q", "pin"))
    p.append(riquadro(500, 30, 150, 150, "", "", ["Oscilloscopio"]))
    p.append('<path class="w" d="M230 70 L230 140 L500 140"/>')
    p.append(testo(508, 66, "CH2", "pin") + testo(508, 136, "CH1", "pin"))
    p.append(testo(508, 156, "R<sub>in</sub> \u2248 1 M\u03a9 \u2225 C<sub>in</sub>", "sm") + testo(508, 171, "(decine di pF)", "sm"))
    p.append('<path class="w" d="M60 205 L575 205 L575 180"/>')
    p.append(testo(60, 224, "massa comune di generatore, circuito e oscilloscopio", "sm"))
    p.append(testo(60, 252, "CH1 su P misura l'ingresso a circuito collegato; CH2 su Q misura l'uscita. L'impedenza di uscita del generatore", "sm"))
    p.append(testo(60, 269, "forma con la resistenza d'ingresso del circuito un partitore: per questo V<sub>in</sub> va misurata in P, non letta dal generatore.", "sm"))
    return 680, 285, "\n".join(p)


def fig_lissajous():
    p = []
    pannelli = [(0, "φ = 0°", "retta inclinata a 45°"), (45, "φ = 45°", "ellisse inclinata"), (90, "φ = 90°", "cerchio (ampiezze uguali)")]
    r = 70
    for k, (phi, nome, descr) in enumerate(pannelli):
        cx, cy = 115 + 225 * k, 120
        p.append(f'<line class="ax" x1="{cx - 90}" y1="{cy}" x2="{cx + 90}" y2="{cy}"/><line class="ax" x1="{cx}" y1="{cy - 90}" x2="{cx}" y2="{cy + 90}"/>')
        pts = []
        for i in range(0, 361, 4):
            t = math.radians(i)
            pts.append((cx + r * math.sin(t), cy - r * math.sin(t - math.radians(phi))))
        p.append('<path class="sl sa" d="M' + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + 'Z"/>')
        p.append(testo(cx, 28, nome, "bd", "middle"))
        p.append(testo(cx, 224, descr, "sm", "middle"))
        if phi == 45:
            a = r * math.sin(math.radians(45))
            p.append(f'<line class="ref" x1="{cx}" y1="{cy - r}" x2="{cx + 25}" y2="{cy - r}"/>')
            p.append(freccia(cx + 10, cy, cx + 10, cy + a, "w", doppia=False))
            p.append(testo(cx + 16, cy + a / 2 + 4, "a", "pin"))
            p.append(freccia(cx - 14, cy, cx - 14, cy - r, "b", doppia=False))
            p.append(testo(cx - 22, cy - r / 2, "b", "pin", "end"))
    p.append(testo(20, 262, "Modo XY: X = V<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>, Y = V</tspan><tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>. Lo sfasamento si ricava da sen φ = a/b, con a = intercetta sull'asse Y e b = massimo di Y.</tspan>", "sm"))
    return 680, 280, "\n".join(p)


def tabella_misura_vuota(intest, righe_attese, colonne_vuote):
    """Tabella da compilare: valori attesi precompilati e colonne di misura vuote."""
    th = "".join(f"<th>{h}</th>" for h in intest + colonne_vuote)
    body = "".join("<tr>" + "".join(f'<td class="n">{c}</td>' for c in r) + "".join("<td></td>" for _ in colonne_vuote) + "</tr>" for r in righe_attese)
    return f'<div class="tbl"><table class="vuota"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


# ---------------------------------------------------------------------------------------------
# Parte II: attivi
# ---------------------------------------------------------------------------------------------

def schema_opamp_regole():
    p = []
    # (a) non invertente
    p.append(testo(20, 24, "Amplificatore non invertente", "ttl"))
    a, pp, pm, out = _opamp(150, 60)
    p.append(a)
    p.append(f'<line class="w" x1="40" y1="{pp[1]}" x2="{pp[0]}" y2="{pp[1]}"/>' + testo(30, pp[1] - 8, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(f'<line class="w" x1="{out[0]}" y1="{out[1]}" x2="330" y2="{out[1]}"/>' + _giunzione(290, out[1]) + testo(336, out[1] - 6, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    # reazione Rf e Rg
    p.append(f'<path class="w" d="M{pm[0]} {pm[1]} L120 {pm[1]} L120 175 L290 175 L290 {out[1]}"/>')
    p.append(_res_h(170, 175) + testo(198, 166, "R<tspan dy='3' font-size='9'>f</tspan>", "", "middle"))
    p.append(_giunzione(120, pm[1]) + _giunzione(120, 175) + f'<line class="w" x1="120" y1="{pm[1]}" x2="120" y2="196"/>')
    p.append('<rect class="r" x="112" y="196" width="16" height="44" rx="2"/><line class="w" x1="120" y1="240" x2="120" y2="256"/>' + _gnd(120, 256))
    p.append(testo(138, 222, "R<tspan dy='3' font-size='9'>g</tspan>"))
    p.append(testo(20, 300, "V<tspan dy='3' font-size='9'>+</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>−</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> → corrente in R</tspan><tspan dy='3' font-size='9'>g</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>/R</tspan><tspan dy='3' font-size='9'>g</tspan>", "it"))
    p.append(testo(20, 322, "la stessa corrente scorre in R<tspan dy='3' font-size='9'>f</tspan><tspan dy='-3'> → V</tspan><tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> (1 + R</tspan><tspan dy='3' font-size='9'>f</tspan><tspan dy='-3'>/R</tspan><tspan dy='3' font-size='9'>g</tspan><tspan dy='-3'>)</tspan>", "it"))
    # (b) buffer
    p.append(testo(400, 24, "Buffer (guadagno 1)", "ttl"))
    a2, pp2, pm2, out2 = _opamp(480, 60)
    p.append(a2)
    p.append(f'<line class="w" x1="410" y1="{pp2[1]}" x2="{pp2[0]}" y2="{pp2[1]}"/>' + testo(400, pp2[1] - 8, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(f'<line class="w" x1="{out2[0]}" y1="{out2[1]}" x2="640" y2="{out2[1]}"/>' + _giunzione(600, out2[1]) + testo(612, out2[1] - 8, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    p.append(f'<path class="w" d="M{pm2[0]} {pm2[1]} L455 {pm2[1]} L455 160 L600 160 L600 {out2[1]}"/>')
    p.append(testo(400, 200, "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>−</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>+</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan>", "it"))
    p.append(testo(400, 232, "Proprietà dell'operazionale ideale:", "bd"))
    for i, r in enumerate(["• corrente d'ingresso nulla (i<tspan dy='3' font-size='9'>+</tspan><tspan dy='-3'> = i</tspan><tspan dy='3' font-size='9'>−</tspan><tspan dy='-3'> = 0)</tspan>",
                           "• impedenza d'uscita nulla",
                           "• guadagno ad anello aperto infinito:",
                           "   con reazione negativa V<tspan dy='3' font-size='9'>+</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>−</tspan>"]):
        p.append(testo(400, 252 + 17 * i, r, "sm"))
    return 680, 335, "\n".join(p)


def _sk_mini(x0, y0, c1, c2, cls_fb):
    """Piccolo Sallen-Key (R1, R2, C1 di reazione, C2 a massa) con condensatori aperti, chiusi o normali."""
    p = []
    y = y0
    p.append(_giunzione(x0, y) + f'<line class="w" x1="{x0}" y1="{y}" x2="{x0 + 14}" y2="{y}"/>' + _res_h(x0 + 14, y, 36, 12))
    p.append(f'<line class="w" x1="{x0 + 50}" y1="{y}" x2="{x0 + 64}" y2="{y}"/>' + _giunzione(x0 + 64, y))
    p.append(f'<line class="w" x1="{x0 + 64}" y1="{y}" x2="{x0 + 78}" y2="{y}"/>' + _res_h(x0 + 78, y, 36, 12))
    p.append(f'<line class="w" x1="{x0 + 114}" y1="{y}" x2="{x0 + 128}" y2="{y}"/>' + _giunzione(x0 + 128, y))
    # buffer
    p.append(f'<line class="w" x1="{x0 + 128}" y1="{y}" x2="{x0 + 140}" y2="{y}"/><path class="r" d="M{x0 + 140} {y - 14} L{x0 + 140} {y + 14} L{x0 + 166} {y} Z"/>'
             f'<line class="w" x1="{x0 + 166}" y1="{y}" x2="{x0 + 190}" y2="{y}"/>' + _giunzione(x0 + 178, y))
    # C2 a massa dal nodo B
    xb = x0 + 128
    if c2 == "aperto":
        p.append(f'<line class="w" x1="{xb}" y1="{y}" x2="{xb}" y2="{y + 24}"/><line class="w" x1="{xb}" y1="{y + 46}" x2="{xb}" y2="{y + 56}"/>'
                 f'<circle class="r" cx="{xb}" cy="{y + 24}" r="2.5"/><circle class="r" cx="{xb}" cy="{y + 46}" r="2.5"/>')
        p.append(testo(xb + 8, y + 38, "C₂ aperto", "sm"))
    elif c2 == "chiuso":
        p.append(f'<path class="arw w" d="M{xb} {y} L{xb} {y + 56}"/>')
        p.append(testo(xb + 8, y + 32, "C₂ corto", "sm"))
    else:
        p.append(_cap_v(xb, y, y + 56))
        p.append(testo(xb + 16, y + 32, "C₂", "sm"))
    p.append(_gnd(xb, y + 56))
    # C1 dal nodo A all'uscita
    xa, xo = x0 + 64, x0 + 178
    top = y - 38
    if c1 == "aperto":
        p.append(f'<path class="w" d="M{xa} {y} L{xa} {top} L{x0 + 100} {top}"/><path class="w" d="M{x0 + 132} {top} L{xo} {top} L{xo} {y}"/>'
                 f'<circle class="r" cx="{x0 + 104}" cy="{top}" r="2.5"/><circle class="r" cx="{x0 + 128}" cy="{top}" r="2.5"/>')
        p.append(testo(x0 + 116, top - 8, "C₁ aperto", "sm", "middle"))
    elif c1 == "chiuso":
        p.append(f'<path class="arw w" d="M{xa} {y} L{xa} {top} L{xo} {top} L{xo} {y}"/>')
        p.append(testo(x0 + 116, top - 8, "C₁ corto", "sm", "middle"))
    else:
        p.append(f'<path class="w" d="M{xa} {y} L{xa} {top} L{x0 + 112} {top}"/><path class="w" d="M{x0 + 124} {top} L{xo} {top} L{xo} {y}"/>'
                 f'<line class="cap" x1="{x0 + 112}" y1="{top - 10}" x2="{x0 + 112}" y2="{top + 10}"/><line class="cap" x1="{x0 + 124}" y1="{top - 10}" x2="{x0 + 124}" y2="{top + 10}"/>')
        p.append(testo(x0 + 118, top - 14, "C₁", "sm", "middle"))
        if cls_fb:
            p.append(freccia(xo - 8, top + 12, xa + 8, top + 12, cls_fb))
    return "".join(p)


def schema_sk_stati():
    p = []
    stati = [("Bassa frequenza", "aperto", "aperto", "", ["I condensatori sono circuiti aperti:", "nelle resistenze non scorre corrente,", "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> = V</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> (guadagno 1).</tspan>"]),
             ("Intorno a f₀", "normale", "normale", "b", ["C₁ riporta sul nodo A una parte di V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>:</tspan>", "reazione positiva che solleva la risposta", "vicino a f₀ (picco se Q > 0,707)."]),
             ("Alta frequenza", "chiuso", "chiuso", "", ["C₂ cortocircuita il nodo B a massa:", "il segnale non arriva al buffer,", "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'> → 0.</tspan>"])]
    for k, (titolo, c1, c2, fb, righe) in enumerate(stati):
        x0 = 8 + 225 * k
        p.append(testo(x0 + 100, 22, titolo, "bd", "middle"))
        p.append(f'<g transform="scale(0.98)">{_sk_mini(x0 + 4, 90, c1, c2, fb)}</g>')
        for i, r in enumerate(righe):
            p.append(testo(x0 + 100, 190 + 16 * i, r, "sm", "middle"))
    return 680, 250, "\n".join(p)


def fig_q_vs_k():
    xs = [1 + i * (2.96 - 1) / 300 for i in range(301)]
    y = [(k, 1 / (3 - k)) for k in xs]
    marc = [(1.0, 0.5, "K = 1,0 \u2192 Q = 0,5", 10, -10, "start"),
            (2.0, 1.0, "K = 2,0 \u2192 Q = 1,0", -10, -14, "end"),
            (2.5, 2.0, "K = 2,5 \u2192 Q = 2,0", -10, -14, "end"),
            (2.9, 10.0, "K = 2,9 \u2192 Q = 10", -12, 4, "end"),
            (2.95, 20.0, "K = 2,95 \u2192 Q = 20", -12, 14, "end")]
    return grafico_bode([("Q = 1/(3 \u2212 K)", "sc", y)], 1.0, 3.0, 0, 21, [1, 1.5, 2, 2.5, 3], [0, 5, 10, 15, 20],
                        "fattore Q", "guadagno K = 1 + R<sub>f</sub>/R<sub>g</sub>",
                        id_clip="qk", x_lin=True, marcatori=marc, linee_v=[(3.0, "")],
                        annot=[(2.97, 12, "K = 3: oscillazione", "end")])


def fig_poli_s():
    p = []
    scala, ox_rel = 78, 1.55  # px per unità; posizione dello zero di sigma nel pannello
    pannelli = []
    bw = fc.butterworth(4, 1.0)
    cb = fc.chebyshev(4, 1.0, 1.0)
    be = [fc.bessel2(1.0)]
    eps = math.sqrt(10 ** 0.1 - 1)
    a = math.asinh(1 / eps) / 4
    pannelli.append(("Butterworth, n = 4", bw, ("cerchio", 1.0)))
    pannelli.append(("Chebyshev 1 dB, n = 4", cb, ("ellisse", (math.sinh(a), math.cosh(a)))))
    pannelli.append(("Bessel, n = 2", be, None))
    for k, (nome, sez, forma) in enumerate(pannelli):
        ox = 45 + 225 * k + scala * 1.15
        oy = 150
        p.append(f'<rect class="fill-a" x="{ox - scala * 1.15 - 4:.1f}" y="40" width="{scala * 1.15 + 4:.1f}" height="220"/>')
        p.append(f'<line class="ax" x1="{ox - scala * 1.3:.1f}" y1="{oy}" x2="{ox + scala * 0.5:.1f}" y2="{oy}"/><line class="ax" x1="{ox}" y1="40" x2="{ox}" y2="260"/>')
        p.append(testo(ox + scala * 0.5, oy + 14, "σ", "tick", "end") + testo(ox + 6, 52, "jω", "tick"))
        if forma:
            if forma[0] == "cerchio":
                p.append(f'<circle class="ref" cx="{ox:.1f}" cy="{oy}" r="{scala}"/>')
            else:
                p.append(f'<ellipse class="ref" cx="{ox:.1f}" cy="{oy}" rx="{forma[1][0] * scala:.1f}" ry="{forma[1][1] * scala:.1f}"/>')
        for s in sez:
            for sigma, omega in fc.poli_sezione(s):
                cx, cy = ox + sigma * scala, oy - omega * scala
                p.append(f'<path class="arw b" d="M{cx - 5:.1f} {cy - 5:.1f} L{cx + 5:.1f} {cy + 5:.1f} M{cx - 5:.1f} {cy + 5:.1f} L{cx + 5:.1f} {cy - 5:.1f}"/>')
        p.append(testo(ox - scala * 0.55, 24, nome, "bd", "middle"))
        p.append(testo(ox - scala * 0.55, 276, "semipiano sinistro: stabile", "sm", "middle"))
    return 680, 292, "\n".join(p)


def fig_gradino_q():
    t_max = 2.0  # in unità di 1/f0 (f0 = 1 Hz)
    curve = []
    for q, cls in ((0.5, "sm"), (1 / math.sqrt(2), "sa"), (1.0, "sb"), (2.0, "sc"), (5.0, "se")):
        r = fc.risposta_gradino([fc.Sezione(2, 1.0, q)], t_max, punti=300)
        curve.append((f"Q = {it(q, 3) if q < 1 else it(q, 1)}", cls, r))
    return grafico_bode(curve, 0, t_max, 0, 2.0, [0, 0.5, 1, 1.5, 2], [0, 0.5, 1, 1.5, 2],
                        "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>/V</tspan><tspan dy='3' font-size='9'>in</tspan>",
                        "tempo · f<tspan dy='3' font-size='9'>0</tspan>", id_clip="gq", x_lin=True, ref_y=[1],
                        ylab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2"}, xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2"})


def _famiglie_n2():
    return [("Bessel", "sm", [fc.bessel2(1.0)]), ("Butterworth", "sa", fc.butterworth(2, 1.0)), ("Chebyshev 1 dB", "sc", fc.chebyshev(2, 1.0, 1.0))]


def fig_gradino_famiglie():
    curve = [(nome, cls, fc.risposta_gradino(sez, 1.5, punti=300)) for nome, cls, sez in _famiglie_n2()]
    return grafico_bode(curve, 0, 1.5, 0, 1.4, [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5], [0, 0.5, 1, 1.4], "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>/V</tspan><tspan dy='3' font-size='9'>in</tspan>",
                        "tempo · f<tspan dy='3' font-size='9'>c</tspan>", id_clip="gf", x_lin=True, ref_y=[1],
                        ylab={0: "0", 0.5: "0,5", 1: "1", 1.4: "1,4"})


def fig_ritardo_gruppo():
    xs = [0.02 + i * (2.0 - 0.02) / 200 for i in range(201)]
    curve = []
    for nome, cls, sez in _famiglie_n2():
        curve.append((nome, cls, [(x, fc.ritardo_gruppo(sez, x) * 2 * math.pi) for x in xs]))
    return grafico_bode(curve, 0, 2.0, 0, 2.2, [0, 0.5, 1, 1.5, 2], [0, 0.5, 1, 1.5, 2],
                        "ritardo di gruppo · 2π f<tspan dy='3' font-size='9'>c</tspan>", "f / f<tspan dy='3' font-size='9'>c</tspan>",
                        id_clip="rg", x_lin=True, ylab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2"},
                        xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2"})


def fig_ripple():
    xs = [i * 1.5 / 300 for i in range(1, 301)]
    bw = fc.butterworth(4, 1.0)
    cb = fc.chebyshev(4, 1.0, 1.0)
    cb3 = fc.chebyshev(4, 3.0, 1.0)
    curve = [("Butterworth n = 4", "sa", [(x, fc.db(fc.risposta_cascata(bw, x))) for x in xs]),
             ("Chebyshev 1 dB", "sc", [(x, fc.db(fc.risposta_cascata(cb, x))) for x in xs]),
             ("Chebyshev 3 dB", "se", [(x, fc.db(fc.risposta_cascata(cb3, x))) for x in xs])]
    return grafico_bode(curve, 0, 1.5, -6, 4, [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5], [-6, -4, -3, -2, -1, 0, 1, 2, 3],
                        "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", id_clip="rip", x_lin=True, ref_y=[0],
                        ylab={-6: MENO + "6", -4: MENO + "4", -3: MENO + "3", -2: MENO + "2", -1: MENO + "1", 0: "0", 1: "1", 2: "2", 3: "3"})


def fig_cascata_somma():
    sk4 = fc.progetta_cascata_butterworth_lp(4, SK_FC, SK_C2)
    curve = [("sezione 1 (Q = 1,30)", "sa", serie_db(lambda f: sk4[0].h(f), 50, 20000)),
             ("sezione 2 (Q = 0,54)", "sb", serie_db(lambda f: sk4[1].h(f), 50, 20000)),
             ("totale = somma in dB", "sd", serie_db(lambda f: fc.risposta_cascata_reale(sk4, f), 50, 20000))]
    return grafico_bode(curve, 50, 20000, -90, 8, [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000], [-80, -60, -40, -20, 0],
                        "ampiezza [dB]", "frequenza [Hz]", altezza=320, id_clip="cs", ref_y=[-3])


def schema_cascata_blocchi():
    p = []
    y = 60
    p.append(testo(20, 24, "Quarto ordine Butterworth = due sezioni del secondo ordine", "ttl"))
    p.append(f'<line class="w" x1="20" y1="{y + 30}" x2="70" y2="{y + 30}"/>' + testo(24, y + 20, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(freccia(20, y + 30, 70, y + 30, ""))
    p.append(riquadro(70, y, 200, 60, "", "b", ["Sezione 1 Sallen-Key", "f₀ = 1 kHz, Q = 1,307"]))
    p.append(freccia(270, y + 30, 330, y + 30, ""))
    p.append(riquadro(330, y, 200, 60, "", "b", ["Sezione 2 Sallen-Key", "f₀ = 1 kHz, Q = 0,541"]))
    p.append(freccia(530, y + 30, 600, y + 30, "") + testo(604, y + 34, "V<tspan dy='3' font-size='9'>out</tspan>", "pin"))
    p.append(testo(300, y + 90, "H = H₁ · H₂", "it", "middle"))
    p.append(testo(300, y + 112, "in decibel le curve si sommano: |H|<tspan dy='3' font-size='9'>dB</tspan><tspan dy='-3'> = |H</tspan><tspan dy='3' font-size='9'>1</tspan><tspan dy='-3'>|</tspan><tspan dy='3' font-size='9'>dB</tspan><tspan dy='-3'> + |H</tspan><tspan dy='3' font-size='9'>2</tspan><tspan dy='-3'>|</tspan><tspan dy='3' font-size='9'>dB</tspan>", "sm", "middle"))
    p.append(testo(300, y + 132, "(il buffer di ogni sezione impedisce che una carichi l'altra)", "sm", "middle"))
    return 680, 210, "\n".join(p)


def fig_guadagno_ao():
    a0_db, gbw = 100.0, 1e6
    a0 = 10 ** (a0_db / 20)
    fp = gbw / a0

    def aperto(f):
        return a0 / (1 + 1j * f / fp)

    xs = fc.griglia_log(1, 1e7, 240)
    curve = [("A(f) ad anello aperto", "sd", [(f, fc.db(aperto(f))) for f in xs])]
    for k, cls in ((1, "sa"), (10, "sb"), (100, "sc")):
        curve.append((f"K = {k}", cls, [(f, fc.db(k / (1 + k / aperto(f)))) for f in xs]))
    marc = [(gbw / k, 20 * math.log10(k) - 3.0, "", 0, 0) for k in (1, 10, 100)]
    return grafico_bode(curve, 1, 1e7, -20, 110, [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000], [-20, 0, 20, 40, 60, 80, 100],
                        "guadagno [dB]", "frequenza [Hz]", altezza=320, id_clip="ao", marcatori=marc,
                        xlab={1000: "1k", 10000: "10k", 100000: "100k", 1000000: "1M", 10000000: "10M"},
                        linee_v=[(1e6, "GBW = 1 MHz")])


def fig_slew():
    f, vp, sr = 100e3, 1.0, 0.3  # Hz, V, V/us
    dt = 0.01  # us
    ts = [i * dt for i in range(0, 2001)]
    ideale = [(t, vp * math.sin(2 * math.pi * f * 1e-6 * t)) for t in ts]
    y = 0.0
    lim = []
    for t, x in ideale:
        step = max(-sr * dt, min(sr * dt, x - y))
        y += step
        lim.append((t, y))
    pend = 2 * math.pi * f * 1e-6 * vp
    return grafico_bode([("uscita ideale", "sd dash", ideale), (f"uscita con SR = {it(sr, 1)} V/µs", "se", lim)],
                        0, 20, -1.3, 1.3, [0, 5, 10, 15, 20], [-1, 0, 1], "tensione [V]", "tempo [µs]", id_clip="sl", x_lin=True,
                        ylab={-1: MENO + "1", 0: "0", 1: "1"},
                        annot=[(10, 1.18, f"pendenza massima richiesta 2πfV<sub>p</sub> = {it(pend, 2)} V/µs > SR", "middle")])


def fig_tolleranze():
    s = fc.progetta_cascata_butterworth_lp(2, SK_FC, SK_C2)[0]
    curve = []
    for nome, cls, k1, k2 in (("nominale", "sd", 1.0, 1.0), ("C₁ +10 %", "sa", 1.1, 1.0), ("C₁ −10 %", "sb", 0.9, 1.0), ("C₁ e C₂ +10 %", "se", 1.1, 1.1)):
        curve.append((nome, cls, [(f, fc.db(fc.h_sk_lp(f, s.r1, s.r2, s.c1 * k1, s.c2 * k2))) for f in fc.griglia_log(300, 3000, 200)]))
    return grafico_bode(curve, 300, 3000, -20, 4, [300, 500, 1000, 2000, 3000], [-20, -15, -10, -5, -3, 0],
                        "ampiezza [dB]", "frequenza [Hz]", id_clip="tol", ref_y=[-3])


def schema_sk_monoalim():
    p = []
    # rete di polarizzazione
    p.append(testo(20, 24, "Riferimento V<tspan dy='3' font-size='9'>cc</tspan><tspan dy='-3'>/2</tspan>", "ttl"))
    p.append('<line class="w" x1="40" y1="50" x2="150" y2="50"/>' + testo(40, 42, "V<tspan dy='3' font-size='9'>cc</tspan>", "pin"))
    p.append('<line class="w" x1="70" y1="50" x2="70" y2="70"/><rect class="r" x="62" y="70" width="16" height="40" rx="2"/><line class="w" x1="70" y1="110" x2="70" y2="130"/>' + _giunzione(70, 130))
    p.append('<line class="w" x1="70" y1="130" x2="70" y2="150"/><rect class="r" x="62" y="150" width="16" height="40" rx="2"/><line class="w" x1="70" y1="190" x2="70" y2="200"/>' + _gnd(70, 200))
    p.append('<line class="w" x1="70" y1="130" x2="110" y2="130"/>' + _giunzione(95, 130) + '<line class="w" x1="95" y1="130" x2="95" y2="150"/>' + _cap_v(95, 150, 200) + _gnd(95, 200))
    p.append(testo(36, 94, "R") + testo(36, 174, "R") + testo(112, 174, "C", "sm"))
    p.append('<circle class="r" cx="110" cy="130" r="4"/>' + testo(120, 134, "V<tspan dy='3' font-size='9'>ref</tspan>", "pin"))
    # Sallen-Key unitario con ritorno a Vref
    y = 120
    p.append(testo(260, 24, "Sallen-Key con alimentazione singola", "ttl"))
    p.append(_giunzione(230, y) + testo(222, y - 12, "V<tspan dy='3' font-size='9'>in</tspan>", "pin"))
    p.append(f'<line class="w" x1="230" y1="{y}" x2="250" y2="{y}"/>' + _cap_h(250, 290, y) + f'<line class="w" x1="290" y1="{y}" x2="320" y2="{y}"/>' + _giunzione(310, y))
    p.append(testo(262, y - 16, "C<tspan dy='3' font-size='9'>in</tspan>", "sm", "middle"))
    p.append(f'<line class="w" x1="310" y1="{y}" x2="310" y2="{y + 24}"/><rect class="r" x="302" y="{y + 24}" width="16" height="30" rx="2"/><line class="w" x1="310" y1="{y + 54}" x2="310" y2="{y + 66}"/>' + '<circle class="r" cx="310" cy="%d" r="4"/>' % (y + 70) + testo(324, y + 74, "V<tspan dy='3' font-size='9'>ref</tspan>", "pin"))
    p.append(testo(326, y + 44, "R<tspan dy='3' font-size='9'>b</tspan>", "sm"))
    p.append(f'<line class="w" x1="310" y1="{y}" x2="340" y2="{y}"/>' + _res_h(340, y, 40, 14) + f'<line class="w" x1="380" y1="{y}" x2="410" y2="{y}"/>' + _giunzione(410, y))
    p.append(f'<line class="w" x1="410" y1="{y}" x2="430" y2="{y}"/>' + _res_h(430, y, 40, 14) + f'<line class="w" x1="470" y1="{y}" x2="500" y2="{y}"/>' + _giunzione(500, y))
    p.append(testo(360, y - 14, "R<tspan dy='3' font-size='9'>1</tspan>", "sm", "middle") + testo(450, y - 14, "R<tspan dy='3' font-size='9'>2</tspan>", "sm", "middle"))
    # C2 verso Vref
    p.append(f'<line class="w" x1="500" y1="{y}" x2="500" y2="{y + 30}"/>' + _cap_v(500, y + 30, y + 80) + '<circle class="r" cx="500" cy="%d" r="4"/>' % (y + 84) + testo(510, y + 90, "V<tspan dy='3' font-size='9'>ref</tspan>", "pin"))
    p.append(testo(486, y + 60, "C₂", "sm", "end"))
    # buffer
    p.append(f'<line class="w" x1="500" y1="{y}" x2="520" y2="{y}"/><path class="r" d="M520 {y - 18} L520 {y + 18} L556 {y} Z"/><line class="w" x1="556" y1="{y}" x2="590" y2="{y}"/>' + _giunzione(575, y))
    p.append(f'<path class="w" d="M575 {y} L575 {y + 54} L508 {y + 54} L508 {y + 14} L520 {y + 14}"/>')
    p.append(f'<line class="w" x1="590" y1="{y}" x2="610" y2="{y}"/>' + _cap_h(610, 650, y) + f'<line class="w" x1="650" y1="{y}" x2="670" y2="{y}"/>' + testo(660, y - 14, "V<tspan dy='3' font-size='9'>out</tspan>", "pin", "middle"))
    # C1 dal nodo A all'uscita
    p.append(f'<path class="w" d="M410 {y} L410 {y - 56} L480 {y - 56}"/>' + _cap_h(480, 520, y - 56) + f'<path class="w" d="M520 {y - 56} L575 {y - 56} L575 {y}"/>')
    p.append(testo(500, y - 74, "C₁", "sm", "middle"))
    p.append(testo(20, 262, "Il segnale oscilla attorno a V<tspan dy='3' font-size='9'>cc</tspan><tspan dy='-3'>/2: l'ingresso è accoppiato in alternata (C</tspan><tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'>) e polarizzato da R</tspan><tspan dy='3' font-size='9'>b</tspan><tspan dy='-3'>;</tspan>", "sm"))
    p.append(testo(20, 280, "C₂ ritorna a V<tspan dy='3' font-size='9'>ref</tspan><tspan dy='-3'> e non a massa. Il partitore va disaccoppiato con un condensatore verso massa; l'operazionale deve avere</tspan>", "sm"))
    p.append(testo(20, 298, "ingressi e uscita compatibili con la tensione di alimentazione (rail-to-rail).", "sm"))
    return 680, 318, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Parte III
# ---------------------------------------------------------------------------------------------

def fig_aliasing(fs=10000.0, fb=1000.0, f_int=9000.0):
    p = []
    ml, pw = 70, 560
    fmax = 12000.0

    def X(f):
        return ml + f / fmax * pw
    att4 = -fc.db(fc.risposta_cascata(fc.butterworth(4, fb), f_int))
    pannelli = [("1. Prima del campionamento", 36),
                ("2. Dopo il campionamento a f<sub>s</sub> = 10 kHz, senza filtro", 176),
                ("3. Dopo il campionamento, con filtro del 4\u00b0 ordine (f<sub>c</sub> = 1 kHz)", 316)]
    for k, (titolo, y0) in enumerate(pannelli):
        base = y0 + 90
        p.append(testo(ml, y0 - 6, titolo, "bd"))
        p.append(f'<line class="ax" x1="{ml}" y1="{base}" x2="{ml + pw}" y2="{base}"/>')
        for f in (0, 2000, 4000, 6000, 8000, 10000, 12000):
            p.append(f'<line class="ax" x1="{X(f)}" y1="{base}" x2="{X(f)}" y2="{base + 4}"/>' + testo(X(f), base + 16, f"{int(f / 1000)}", "tick", "middle"))
        p.append(testo(ml + pw + 6, base + 16, "kHz", "tick"))
        p.append(f'<rect class="fill-b" x="{X(0):.1f}" y="{base - 52}" width="{X(fb) - X(0):.1f}" height="52"/>')
        p.append(testo((X(0) + X(fb)) / 2, base - 20, "segnale", "sm", "middle"))
        p.append(f'<line class="ref" x1="{X(fs / 2):.1f}" y1="{base - 74}" x2="{X(fs / 2):.1f}" y2="{base}"/>' + testo(X(fs / 2) + 4, base - 66, "f<sub>s</sub>/2", "tick"))
        if k == 0:
            p.append(freccia(X(f_int), base, X(f_int), base - 60, "w") + testo(X(f_int) + 6, base - 46, "interferente a 9 kHz", "sm"))
        elif k == 1:
            p.append(freccia(X(fb), base, X(fb), base - 60, "w") + testo(X(fb) + 8, base - 40, "alias a 1 kHz (10 \u2212 9):", "sm") + testo(X(fb) + 8, base - 26, "cade nella banda utile", "sm"))
            p.append(f'<line class="arw w" stroke-dasharray="3 3" x1="{X(f_int):.1f}" y1="{base}" x2="{X(f_int):.1f}" y2="{base - 60}"/>')
            p.append(f'<path class="arw" stroke-dasharray="4 3" d="M{X(f_int):.1f} {base - 64} Q{X(fs / 2):.1f} {base - 110} {X(fb) + 4:.1f} {base - 66}"/>')
            p.append(testo(X(f_int) + 6, base - 46, "9 kHz si ripiega attorno a f<sub>s</sub>/2", "sm"))
        else:
            p.append(freccia(X(fb), base, X(fb), base - 3, "w") + testo(X(fb) + 8, base - 30, f"alias attenuato di {it(att4, 1)} dB:", "sm") + testo(X(fb) + 8, base - 16, "trascurabile", "sm"))
    return 680, 440, "\n".join(p)


def fig_maschera():
    xs = fc.griglia_log(100, 20000, 260)
    n4 = fc.butterworth(4, 1500.0)
    n5 = fc.butterworth(5, 1500.0)
    n4b = fc.butterworth(4, 1000.0)
    curve = [("n = 4, f<sub>c</sub> = 1 kHz", "sm dash", [(x, fc.db(fc.risposta_cascata(n4b, x))) for x in xs]),
             ("n = 4, f<sub>c</sub> = 1,5 kHz", "sa", [(x, fc.db(fc.risposta_cascata(n4, x))) for x in xs]),
             ("n = 5, f<sub>c</sub> = 1,5 kHz", "sb", [(x, fc.db(fc.risposta_cascata(n5, x))) for x in xs])]
    aree = [(100, 1000, -100, -0.5), (9000, 20000, -72, 10)]
    return grafico_bode(curve, 100, 20000, -100, 6, [100, 200, 500, 1000, 2000, 5000, 10000, 20000], [-100, -80, -72, -60, -40, -20, -0.5, 0],
                        "ampiezza [dB]", "frequenza [Hz]", altezza=340, id_clip="mas", aree=aree,
                        ylab={-72: MENO + "72", -0.5: "", -100: MENO + "100", -80: MENO + "80", -60: MENO + "60", -40: MENO + "40", -20: MENO + "20", 0: "0"},
                        annot=[(300, -50, "zona vietata: attenuazione > 0,5 dB", "start"), (8700, -92, "zona vietata (attenuazione < 72 dB) \u2192", "end")])


def schema_flusso_progetto():
    p = []
    passi = [("1. Specifica", "banda, attenuazioni, ampiezza", "b"), ("2. Famiglia e ordine", "Butterworth, Chebyshev, Bessel", "b"),
             ("3. Sezioni", "f₀ e Q di ciascuna", "b"), ("4. Componenti", "C, poi R; serie E", "a"),
             ("5. Limiti reali", "GBW, slew rate, rumore, C", "a"), ("6. Misura", "confronto con i valori attesi", "c")]
    pos = [(30, 40), (250, 40), (470, 40), (470, 170), (250, 170), (30, 170)]
    for (titolo, sotto, cls), (x, y) in zip(passi, pos):
        p.append(riquadro(x, y, 180, 70, "", cls, [titolo, sotto]))
    p.append(freccia(210, 75, 250, 75, ""))
    p.append(freccia(430, 75, 470, 75, ""))
    p.append(freccia(560, 110, 560, 170, ""))
    p.append(freccia(470, 205, 430, 205, ""))
    p.append(freccia(250, 205, 210, 205, ""))
    p.append(f'<path class="arw w" stroke-dasharray="5 4" d="M30 205 L12 205 L12 75 L30 75"/>')
    p.append(testo(8, 140, "se fuori specifica: rivedere", "sm", "middle").replace('<text', '<text transform="rotate(-90 8 140)"'))
    return 680, 270, "\n".join(p)


def schema_flusso_diagnostica():
    p = []
    p.append(riquadro(20, 110, 150, 70, "", "w", ["La risposta misurata", "differisce dal calcolo"]))
    casi = [("Guadagno in banda passante errato", "Misurare V<tspan dy='3' font-size='9'>in</tspan><tspan dy='-3'> sul nodo P con il circuito collegato; verificare impedenza del generatore e carico dello strumento</tspan>"),
            ("fᶜ o f₀ spostata", "Misurare R e C reali; verificare tolleranza e tipo di condensatore (X7R)"),
            ("Picco diverso dal previsto", "Ricalcolare Q con i valori misurati; controllare C₁ e C₂; verificare GBW dell'operazionale"),
            ("Oscillazione o taglio del segnale", "Disaccoppiare l'alimentazione; ridurre l'ampiezza; controllare i nodi intermedi con l'oscilloscopio")]
    for i, (a, b) in enumerate(casi):
        y = 20 + i * 90
        p.append(riquadro(205, y, 225, 60, "", "b", [a]))
        p.append(freccia(170, 145, 205, y + 30, ""))
        p.append(freccia(430, y + 30, 450, y + 30, ""))
        p.append(f'<rect class="box" x="450" y="{y}" width="215" height="60" rx="6"/>')
        # testo a capo
        parole = re.sub(r"<[^>]+>", "", b).split()
        riga, righe = "", []
        for w in parole:
            if len(riga) + len(w) > 32:
                righe.append(riga)
                riga = w
            else:
                riga = (riga + " " + w).strip()
        righe.append(riga)
        for j, r in enumerate(righe[:4]):
            p.append(testo(458, y + 16 + 13 * j, r, "sm"))
    return 680, 385, "\n".join(p)
