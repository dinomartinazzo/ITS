"""Diagrammi del capitolo su Butterworth, Chebyshev e Bessel (SVG, curve calcolate con src/filtri_core.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
from disegno import grafico_bode  # noqa: E402
from disegno_base import _pannello  # noqa: E402
from disegno_didattico import _mappa, freccia, riquadro, testo  # noqa: E402
from formati import it, sig  # noqa: E402

MENO = "−"
CH05, CH10, CH30 = 0.5, 1.0, 3.0
N4 = 4


def _famiglie_n4():
    """Elenco (etichetta, classe, sezioni) dei cinque filtri del quarto ordine confrontati."""
    return [("Bessel", "sm", fc.bessel(N4, 1.0)),
            ("Butterworth", "sa", fc.butterworth(N4, 1.0)),
            ("Cheb. 0,5 dB", "sb", fc.chebyshev(N4, CH05, 1.0)),
            ("Cheb. 1 dB", "sc", fc.chebyshev(N4, CH10, 1.0)),
            ("Cheb. 3 dB", "se", fc.chebyshev(N4, CH30, 1.0))]


def _tre_n4():
    return [("Bessel", "sm", fc.bessel(N4, 1.0)), ("Butterworth", "sa", fc.butterworth(N4, 1.0)),
            ("Chebyshev 1 dB", "sc", fc.chebyshev(N4, CH10, 1.0))]


# ---------------------------------------------------------------------------------------------
# Tre idee di ottimalità
# ---------------------------------------------------------------------------------------------

def fig_tre_idee():
    """Che cosa ottimizza ciascuna famiglia, visto su tre piccoli grafici."""
    p = []
    w, h, y0 = 190, 120, 56
    xs = [i * 1.4 / 200 for i in range(1, 201)]
    bw, ch, be = fc.butterworth(N4, 1.0), fc.chebyshev(N4, CH10, 1.0), fc.bessel(N4, 1.0)
    titoli = ["Butterworth: la più piatta", "Chebyshev: errore uguale ovunque", "Bessel: ritardo quasi costante in banda"]
    sotto = [["Il modulo resta piatto il più a lungo", "possibile, poi scende."], ["Il modulo oscilla entro un ripple", "fisso e poi scende molto in fretta."],
             ["Ritardo quasi costante nella banda", "utile: forma meglio conservata."]]
    for k in range(3):
        x0 = 20 + k * 215
        p.append(testo(x0, 28, titoli[k], "bd"))
        if k == 0:
            pts = [(x, fc.db(fc.risposta_cascata(bw, x))) for x in xs]
            s, X, Y = _pannello(x0, y0, w, h, pts, 0, 1.4, -12, 2, "sa")
            p.append(s + testo(x0, y0 + h + 14, "ampiezza [dB], f/fc da 0 a 1,4", "tick"))
        elif k == 1:
            pts = [(x, fc.db(fc.risposta_cascata(ch, x))) for x in xs]
            s, X, Y = _pannello(x0, y0, w, h, pts, 0, 1.4, -12, 2, "sc")
            p.append(s + testo(x0, y0 + h + 14, "ampiezza [dB], f/fc da 0 a 1,4", "tick"))
        else:
            xs2 = [i * 1.4 / 200 for i in range(2, 201)]
            pts = [(x, fc.ritardo_gruppo(be, x) * 2 * math.pi) for x in xs2]
            s, X, Y = _pannello(x0, y0, w, h, pts, 0, 1.4, 0, 3.0, "sm")
            p.append(s + testo(x0, y0 + h + 14, "ritardo di gruppo, f/fc da 0 a 1,4", "tick"))
        for i, r in enumerate(sotto[k]):
            p.append(testo(x0, y0 + h + 34 + 15 * i, r, "sm"))
    return 680, 270, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Chebyshev: polinomi ed equiripple
# ---------------------------------------------------------------------------------------------

def fig_polinomi_chebyshev():
    xs = [-1.3 + i * 2.6 / 400 for i in range(401)]
    curve = [(f"T<sub>{n}</sub>(x)", cls, [(x, fc.polinomio_chebyshev(n, x)) for x in xs])
             for n, cls in ((1, "sm"), (2, "sa"), (3, "sb"), (4, "sc"), (5, "se"))]
    w_, h_, inner = grafico_bode(curve, -1.3, 1.3, -2.2, 2.2, [-1, -0.5, 0, 0.5, 1], [-2, -1, 0, 1, 2], "T<sub>n</sub>(x)", "x",
                                 altezza=320, id_clip="pch", x_lin=True, ref_y=[-1, 1],
                                 aree=[(-1, 1, -2.2, 2.2, "fill-b")], ylab={-2: MENO + "2", -1: MENO + "1", 0: "0", 1: "1", 2: "2"},
                                 xlab={-1: MENO + "1", -0.5: MENO + "0,5", 0: "0", 0.5: "0,5", 1: "1"},
                                 annot=[(0, 2.0, "dentro |x| ≤ 1 ogni polinomio oscilla tra −1 e +1", "middle"),
                                        (-1.28, 1.2, "fuori cresce", "start")])
    return w_, h_, inner


def fig_equiripple_cheb():
    xs = [i * 1.15 / 400 for i in range(401)]
    curve = []
    for n, cls in ((2, "sa"), (3, "sb"), (4, "sc"), (5, "se")):
        sez = fc.chebyshev(n, CH10, 1.0)
        vals = [(x, fc.db(fc.risposta_cascata(sez, x))) for x in xs]
        massimo = max(v for _, v in vals if _ <= 1.0)
        curve.append((f"n = {n}", cls, [(x, v - massimo) for x, v in vals]))
    return grafico_bode(curve, 0, 1.15, -4, 0.4, [0, 0.25, 0.5, 0.75, 1], [-4, -3, -2, -1, 0], "ampiezza [dB] rispetto al massimo", "f / f<tspan dy='3' font-size='9'>c</tspan>",
                        altezza=320, id_clip="eqr", x_lin=True, ref_y=[-1], aree=[(0, 1, -4, 0.4, "fill-b")],
                        ylab={-4: MENO + "4", -3: MENO + "3", -2: MENO + "2", -1: MENO + "1", 0: "0"},
                        xlab={0: "0", 0.25: "0,25", 0.5: "0,5", 0.75: "0,75", 1: "1"},
                        annot=[(0.5, -3.6, "ripple di 1 dB: n + 1 estremi alternati", "middle")])


# ---------------------------------------------------------------------------------------------
# Poli
# ---------------------------------------------------------------------------------------------

def _piano_s(p, x0, y0, w, h, scala, sezioni, titolo, riferimento=None, etichette=None, ellisse=None):
    """Piano s in un riquadro: semipiano sinistro ombreggiato, poli come croci, cerchio/ellisse di riferimento."""
    ox, oy = x0 + w * 0.68, y0 + h / 2
    p.append(f'<rect class="fill-a" x="{x0}" y="{y0}" width="{ox - x0:.1f}" height="{h}"/>')
    p.append(f'<line class="ax" x1="{x0}" y1="{oy}" x2="{x0 + w}" y2="{oy}"/><line class="ax" x1="{ox:.1f}" y1="{y0}" x2="{ox:.1f}" y2="{y0 + h}"/>')
    p.append(testo(x0 + w, oy + 13, "σ", "tick", "end") + testo(ox + 5, y0 + 11, "jω", "tick"))
    if riferimento:
        p.append(f'<circle class="ref" cx="{ox:.1f}" cy="{oy}" r="{riferimento * scala:.1f}"/>')
    if ellisse:
        p.append(f'<ellipse class="sl sc dash" cx="{ox:.1f}" cy="{oy}" rx="{ellisse[0] * scala:.1f}" ry="{ellisse[1] * scala:.1f}"/>')
    for k, s in enumerate(sezioni):
        for sigma, omega in fc.poli_sezione(s):
            cx, cy = ox + sigma * scala, oy - omega * scala
            p.append(f'<path class="arw b" d="M{cx - 4.5:.1f} {cy - 4.5:.1f} L{cx + 4.5:.1f} {cy + 4.5:.1f} M{cx - 4.5:.1f} {cy + 4.5:.1f} L{cx + 4.5:.1f} {cy - 4.5:.1f}"/>')
        if etichette and s.ordine == 2:
            sg, om = fc.poli_sezione(s)[0]
            p.append(testo(ox + sg * scala - 7, oy - om * scala - 6, f"Q {it(s.q, 2)}", "tick", "end"))
    p.append(testo(x0, y0 - 8, titolo, "bd"))


def fig_poli_butterworth_n():
    p = []
    w, h, y0 = 150, 190, 46
    for k, n in enumerate((3, 4, 5, 6)):
        x0 = 20 + k * 165
        _piano_s(p, x0, y0, w, h, 52, fc.butterworth(n, 1.0), f"Butterworth n = {n}", riferimento=1.0, etichette=True)
    p.append(testo(20, 262, "I poli stanno sulla stessa circonferenza di raggio f<sub>c</sub>, a intervalli di 180°/n.", "sm"))
    p.append(testo(20, 280, "Più ordine = più poli vicini all'asse jω = sezioni con Q più alto (picco più marcato).", "sm"))
    return 680, 296, "\n".join(p)


def fig_poli_chebyshev_ripple():
    p = []
    w, h, y0 = 190, 190, 46
    for k, r in enumerate((CH05, CH10, CH30)):
        x0 = 20 + k * 215
        eps = math.sqrt(10 ** (r / 10) - 1)
        a = math.asinh(1 / eps) / N4
        _piano_s(p, x0, y0, w, h, 56, fc.chebyshev(N4, r, 1.0), f"Chebyshev n = 4, ripple {sig(r, 2).replace('.', ',')} dB",
                 riferimento=1.0, etichette=True, ellisse=(math.sinh(a), math.cosh(a)))
    p.append(testo(20, 262, "Più ripple = ellisse più stretta (semiasse sinh a più piccolo) = poli più vicini all'asse jω:", "sm"))
    p.append(testo(20, 280, "discesa più ripida, ma sezioni con Q più alto. Cerchio puntinato = Butterworth, ellisse viola = Chebyshev.", "sm"))
    return 680, 296, "\n".join(p)


def fig_poli_bessel_n():
    p = []
    w, h, y0 = 190, 190, 46
    for k, n in enumerate((2, 3, 4)):
        x0 = 20 + k * 215
        _piano_s(p, x0, y0, w, h, 56, fc.bessel(n, 1.0), f"Bessel n = {n}", riferimento=1.0, etichette=True)
    p.append(testo(20, 262, "I poli del Bessel stanno più lontani dall'asse jω di quelli del Butterworth (cerchio tratteggiato):", "sm"))
    p.append(testo(20, 280, "Q basso, nessun picco e ritardo di gruppo quasi costante nella banda utile.", "sm"))
    return 680, 296, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Confronti a ordine 4
# ---------------------------------------------------------------------------------------------

def fig_confronto_n4_modulo():
    xs = fc.griglia_log(0.1, 10, 260)
    curve = [(n, c, [(x, fc.db(fc.risposta_cascata(s, x))) for x in xs]) for n, c, s in _famiglie_n4()]
    return grafico_bode(curve, 0.1, 10, -100, 4, [0.1, 0.2, 0.5, 1, 2, 5, 10], [-100, -80, -60, -40, -20, -3, 0],
                        "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=340, id_clip="c4m", ref_y=[-3])


def fig_transizione_n4():
    xs = [0.6 + i * 1.9 / 300 for i in range(301)]
    curve = [(n, c, [(x, fc.db(fc.risposta_cascata(s, x))) for x in xs]) for n, c, s in _famiglie_n4()]
    return grafico_bode(curve, 0.6, 2.5, -50, 3, [0.6, 0.8, 1, 1.25, 1.5, 2, 2.5], [-50, -40, -30, -20, -10, -3, 0],
                        "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=340, id_clip="c4t", x_lin=True,
                        ref_y=[-3, -40], xlab={0.6: "0,6", 0.8: "0,8", 1: "1", 1.25: "1,25", 1.5: "1,5", 2: "2", 2.5: "2,5"})


def fig_fase_n4():
    xs = [i * 3.0 / 240 for i in range(1, 241)]
    curve = []
    for n, c, s in _tre_n4():
        curve.append((n, c, [(x, fc.fase_cascata_gradi(s, x)) for x in xs]))
    be = fc.bessel(N4, 1.0)
    pendenza = (fc.fase_cascata_gradi(be, 0.05) - fc.fase_cascata_gradi(be, 0.01)) / 0.04
    curve.append(("fase lineare ideale", "sd dash", [(0, 0), (3.0, pendenza * 3.0)]))
    return grafico_bode(curve, 0, 3.0, -420, 10, [0, 0.5, 1, 1.5, 2, 2.5, 3], [-360, -270, -180, -90, 0], "fase [°]",
                        "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=320, id_clip="c4f", x_lin=True,
                        ylab={-360: MENO + "360", -270: MENO + "270", -180: MENO + "180", -90: MENO + "90", 0: "0"},
                        xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2", 2.5: "2,5", 3: "3"})


def fig_ritardo_n4():
    xs = [0.02 + i * 3.0 / 240 for i in range(241)]
    curve = [(n, c, [(x, fc.ritardo_gruppo(s, x) * 2 * math.pi) for x in xs]) for n, c, s in _tre_n4()]
    return grafico_bode(curve, 0, 3.0, 0, 12, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 2, 4, 6, 8, 10, 12], "ritardo di gruppo · 2π f<tspan dy='3' font-size='9'>c</tspan>",
                        "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=320, id_clip="c4r", x_lin=True,
                        xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2", 2.5: "2,5", 3: "3"})


def fig_gradino_n4():
    curve = [(n, c, fc.risposta_gradino(s, 3.0, punti=300)) for n, c, s in _tre_n4()]
    return grafico_bode(curve, 0, 3.0, 0, 1.4, [0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.5, 1, 1.4], "V<tspan dy='3' font-size='9'>out</tspan><tspan dy='-3'>/V</tspan><tspan dy='3' font-size='9'>in</tspan>",
                        "tempo · f<tspan dy='3' font-size='9'>c</tspan>", altezza=320, id_clip="c4g", x_lin=True, ref_y=[1],
                        ylab={0: "0", 0.5: "0,5", 1: "1", 1.4: "1,4"}, xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2", 2.5: "2,5", 3: "3"})


def fig_impulso_n4():
    larghezza, inizio = 1.0, 0.4

    def u(t):
        return 1.0 if inizio <= t < inizio + larghezza else 0.0
    ingresso = [(i * 4.5 / 500, u(i * 4.5 / 500)) for i in range(501)]
    curve = [("ingresso (impulso)", "sd dash", ingresso)]
    for n, c, s in _tre_n4():
        curve.append((n, c, fc.risposta_ingresso(s, u, 4.5, punti=300)))
    return grafico_bode(curve, 0, 4.5, -0.35, 1.45, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], [-0.2, 0, 0.5, 1], "tensione", "tempo · f<tspan dy='3' font-size='9'>c</tspan>",
                        altezza=330, id_clip="c4i", x_lin=True, ref_y=[0, 1],
                        ylab={-0.2: MENO + "0,2", 0: "0", 0.5: "0,5", 1: "1"}, xlab={0: "0", 0.5: "0,5", 1: "1", 1.5: "1,5", 2: "2", 2.5: "2,5", 3: "3", 3.5: "3,5", 4: "4"})


def fig_fattore_forma():
    p = []
    p.append(testo(20, 24, "Fattore di forma: f a −40 dB divisa per f a −3 dB (quarto ordine; più basso = discesa più ripida)", "bd"))
    voci = []
    for nome, cls, sez in _famiglie_n4():
        voci.append((nome, fc.frequenza_attenuazione(sez, 40.0) / fc.f_3db(sez, riferimento="picco")))
    massimo = max(v for _, v in voci)
    for i, (nome, v) in enumerate(voci):
        y = 52 + i * 40
        larg = 360 * v / massimo
        classe = "fill-b" if "Chebyshev" in nome else ("fill-a" if nome == "Butterworth" else "fill-c")
        p.append(testo(20, y + 15, nome, "sm"))
        p.append(f'<rect class="{classe}" x="170" y="{y}" width="{larg:.1f}" height="22"/><rect class="ax" x="170" y="{y}" width="{larg:.1f}" height="22"/>')
        p.append(testo(170 + larg + 8, y + 16, f"{it(v, 2)}", "bd"))
    p.append(testo(20, 262, "Il Chebyshev raggiunge i 40 dB di attenuazione con una frequenza più vicina al taglio: transizione più stretta.", "sm"))
    p.append(testo(20, 280, "Il Bessel ha bisogno di una frequenza molto più alta: transizione larga.", "sm"))
    return 680, 296, "\n".join(p)


# ---------------------------------------------------------------------------------------------
# Quanti poli servono e difficoltà di realizzazione
# ---------------------------------------------------------------------------------------------

def fig_ordine_minimo(rapporto=3.0):
    p_curve = {}
    atts = list(range(5, 71))
    for fam, cls in (("butterworth", "sa"), ("chebyshev", "sc"), ("bessel", "sm")):
        pts = []
        for a in atts:
            n = fc.ordine_minimo(fam, a, rapporto, ripple_db=CH10, n_max=12)
            if n is not None:
                pts.append((a, n))
        # profilo a gradini: l'ordine vale n fino all'attenuazione successiva
        gradini = []
        for i, (a, n) in enumerate(pts):
            if i > 0 and n != pts[i - 1][1]:
                gradini.append((a, pts[i - 1][1]))
            gradini.append((a, n))
        p_curve[fam] = (cls, gradini)
    curve = [("Butterworth", "sa", p_curve["butterworth"][1]), ("Chebyshev 1 dB", "sc", p_curve["chebyshev"][1]), ("Bessel", "sm", p_curve["bessel"][1])]
    return grafico_bode(curve, 5, 70, 0, 12.5, [10, 20, 30, 40, 50, 60, 70], [0, 2, 4, 6, 8, 10, 12], "ordine minimo n",
                        "attenuazione richiesta a 3 f<tspan dy='3' font-size='9'>c</tspan><tspan dy='-3'> [dB]</tspan>", altezza=320, id_clip="omin", x_lin=True,
                        annot=[(67, 11.4, "il Bessel non va oltre ~34 dB a 3 fc", "end")])


def fig_qmax_famiglie():
    ns = list(range(2, 11))
    qmax = lambda sez: max((s.q for s in sez if s.ordine == 2), default=0.0)  # noqa: E731
    curve = [("Butterworth", "sa", [(n, qmax(fc.butterworth(n, 1.0))) for n in ns]),
             ("Chebyshev 1 dB", "sc", [(n, qmax(fc.chebyshev(n, CH10, 1.0))) for n in ns]),
             ("Chebyshev 3 dB", "se", [(n, qmax(fc.chebyshev(n, CH30, 1.0))) for n in ns]),
             ("Bessel", "sm", [(n, qmax(fc.bessel(n, 1.0))) for n in ns])]
    return grafico_bode(curve, 2, 10, 0, 40, [2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 10, 20, 30, 40], "Q della sezione più critica", "ordine n",
                        altezza=320, id_clip="qmx", x_lin=True,
                        marcatori=[(n, qmax(fc.chebyshev(n, CH10, 1.0)), "", 0, 0) for n in (4, 6, 8, 10)])


def schema_albero_scelta():
    p = []
    p.append(riquadro(230, 20, 220, 50, "", "w", ["Che cosa conta di più?", "(si parte dal requisito)"]))
    p.append(freccia(280, 70, 110, 120, "") + freccia(340, 70, 340, 120, "") + freccia(400, 70, 570, 120, ""))
    rami = [(20, "La forma d'onda", "impulsi, segnali nel tempo", "Bessel", "sm"), (240, "La piattezza in banda", "uso generale, anti-aliasing", "Butterworth", "a"),
            (460, "La selettività", "poco ordine, ripple tollerato", "Chebyshev", "c")]
    for x, t, s, nome, cls in rami:
        p.append(riquadro(x, 120, 200, 56, "", "", [t, s]))
        p.append(freccia(x + 100, 176, x + 100, 206, ""))
        cl = {"sm": "", "a": "a", "c": "c"}[cls]
        p.append(riquadro(x + 20, 206, 160, 44, "", cl, [nome]))
    spiega = [["ritardo quasi costante in banda,", "poca sovraelongazione, ma", "pendenza bassa"], ["risposta piatta, nessun", "ripple, pendenza media"], ["discesa ripida con meno", "poli, ma ripple e Q alti"]]
    for (x, *_), righe in zip(rami, spiega):
        for j, r in enumerate(righe):
            p.append(testo(x + 100, 270 + 15 * j, r, "sm", "middle"))
    return 680, 330, "\n".join(p)
