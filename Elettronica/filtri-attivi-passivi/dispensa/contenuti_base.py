"""Tabelle e figure della prima parte della dispensa (RC, RLC, Sallen-Key, famiglie, limiti)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import filtri_core as fc  # noqa: E402
from disegno import (figura, grafico_bode, hero_art, schema_rc, schema_rlc, schema_sk_k,  # noqa: E402,F401
                     schema_sk_lp, serie_db, serie_fase)
from formati import it, riga, sci, sig, si, tabella  # noqa: E402
from parametri import MOLT, RC_C, RC_R, RLC_C, RLC_L, RLC_R, SK_C2, SK_FC  # noqa: E402


def blocchi_base():
    b = {}
    f0 = fc.rc_fc(RC_R, RC_C)
    b["RC_FC"] = sig(f0, 5)
    b["RC_FC_INT"] = sig(f0, 4)
    b["RC_TAU"] = si(RC_R * RC_C, "s")

    # --- RC: tabella valori e grafico -------------------------------------------------------
    righe = []
    for m in MOLT:
        hl, hh = fc.h_rc_lp(m * f0, f0), fc.h_rc_hp(m * f0, f0)
        righe.append(riga([sig(m), si(m * f0, "Hz"), sig(abs(hl), 4), it(fc.db(hl)), it(fc.fase_gradi(hl), 1),
                           it(fc.db(hh)), it(fc.fase_gradi(hh), 1, True)],
                          ["n"] * 7))
    b["TAB_RC"] = tabella(["f/f<sub>c</sub>", "Frequenza", "|H| LP", "LP [dB]", "LP fase [°]", "HP [dB]", "HP fase [°]"],
                          righe, ["n"] * 7)
    b["FIG_BODE_RC"] = figura(
        1, "Risposta in ampiezza e fase del filtro RC",
        "Curve di ampiezza in decibel e di fase del passa-basso e del passa-alto RC in funzione di f/fc.",
        grafico_bode([("passa-basso", "sa", serie_db(lambda f: fc.h_rc_lp(f, 1), 0.01, 100)),
                      ("passa-alto", "sb", serie_db(lambda f: fc.h_rc_hp(f, 1), 0.01, 100))],
                     0.01, 100, -40, 3, [0.01, 0.1, 1, 10, 100], [-40, -30, -20, -10, -3, 0],
                     "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", id_clip="c1", legenda_pos="basso-destra", ref_y=[-3]),
        None, "Le due curve si incontrano a −3 dB in f/f<sub>c</sub> = 1. Oltre la frequenza di taglio l'ampiezza scende di 20 dB per decade (−6 dB per ottava).")
    b["FIG_FASE_RC"] = figura(
        2, "Fase del filtro RC",
        "Fase del passa-basso (da 0 a −90 gradi) e del passa-alto (da +90 a 0 gradi) in funzione di f/fc.",
        grafico_bode([("passa-basso", "sa", serie_fase(lambda f: fc.h_rc_lp(f, 1), 0.01, 100)),
                      ("passa-alto", "sb", serie_fase(lambda f: fc.h_rc_hp(f, 1), 0.01, 100))],
                     0.01, 100, -90, 90, [0.01, 0.1, 1, 10, 100], [-90, -45, 0, 45, 90],
                     "fase [°]", "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=260, id_clip="c2", legenda_pos="alto-destra"),
        None, "A f<sub>c</sub> la fase vale ±45°. La fase tende a −90° (LP) e a 0° (HP) ad alta frequenza.")
    b["FIG_SCHEMA_RC"] = figura(3, "Celle RC del primo ordine", "Schemi del passa-basso (R in serie, C a massa) e del passa-alto (C in serie, R a massa).",
                                schema_rc(), None, "Nel passa-basso la tensione di uscita è prelevata ai capi di C; nel passa-alto ai capi di R. Il condensatore lascia passare la corrente alternata e blocca la continua.")

    # --- carico resistivo -------------------------------------------------------------------
    righe = []
    for rl in (None, 100e3, 10e3, 1.6e3):
        if rl is None:
            righe.append(riga(["nessuno (∞)", "1,000", "0,00", sig(f0, 5)], ["", "n", "n", "n"]))
        else:
            r_th = RC_R * rl / (RC_R + rl)
            g = rl / (RC_R + rl)
            righe.append(riga([si(rl, "Ω"), it(g, 3), it(20 * math.log10(g)), sig(fc.rc_fc(r_th, RC_C), 5)], ["", "n", "n", "n"]))
    b["TAB_CARICO"] = tabella(["Carico R<sub>L</sub>", "Guadagno DC", "Guadagno DC [dB]", "f<sub>c</sub> [Hz]"], righe, ["", "n", "n", "n"])

    # --- due celle RC collegate -------------------------------------------------------------
    righe = []
    for m in (0.1, 0.374, 1.0, 2.0, 10.0):
        f = m * f0
        s = fc.h_rc_lp(f, f0)
        doppio_iso = s * s
        doppio_col = fc.h_rc_lp_doppio(f, RC_R, RC_C, RC_R, RC_C)
        righe.append(riga([sig(m), it(fc.db(s)), it(fc.db(doppio_iso)), it(fc.db(doppio_col))], ["n"] * 4))
    b["TAB_DOPPIO"] = tabella(["f/f<sub>c</sub> della singola cella", "1 cella [dB]", "2 celle isolate [dB]", "2 celle collegate [dB]"], righe, ["n"] * 4)
    lo, hi = 1.0, f0
    for _ in range(80):
        mid = (lo + hi) / 2
        if abs(fc.h_rc_lp_doppio(mid, RC_R, RC_C, RC_R, RC_C)) > 1 / math.sqrt(2):
            lo = mid
        else:
            hi = mid
    b["DOPPIO_RAPP"] = it(lo / f0, 3)
    b["DOPPIO_ISO_RAPP"] = it(math.sqrt(math.sqrt(2) - 1), 3)
    b["FIG_DOPPIO"] = figura(
        4, "Una cella, due celle isolate, due celle collegate",
        "Confronto in decibel tra una cella RC, il prodotto di due celle isolate e due celle realmente collegate in cascata.",
        grafico_bode([("1 cella", "sm dash", serie_db(lambda f: fc.h_rc_lp(f, 1.0), 0.01, 100)),
                      ("2 celle isolate", "sa", serie_db(lambda f: fc.h_rc_lp(f, 1.0) ** 2, 0.01, 100)),
                      ("2 celle collegate", "sb", serie_db(lambda f: fc.h_rc_lp_doppio(f, 1.0, 1.0 / (2 * math.pi), 1.0, 1.0 / (2 * math.pi)), 0.01, 100))],
                     0.01, 100, -60, 3, [0.01, 0.1, 1, 10, 100], [-60, -40, -20, -3, 0],
                     "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan> della singola cella", id_clip="c4", legenda_pos="basso-sinistra", ref_y=[-3]),
        None, "La seconda cella carica la prima: la curva reale (verde petrolio) è più bassa e più «morbida» del prodotto ideale (ambra).")

    # --- RLC ----------------------------------------------------------------------------------
    righe = []
    for r in RLC_R:
        rl = fc.RlcSerie(r, RLC_L, RLC_C)
        righe.append(riga([si(r, "Ω"), sig(rl.f0, 5), it(rl.q, 2), sig(rl.banda, 4), it(fc.db(rl.h(rl.f0 * 0.5)), 1)], ["", "n", "n", "n", "n"]))
    b["TAB_RLC"] = tabella(["R", "f<sub>0</sub> [Hz]", "Q", "Banda a −3 dB [Hz]", "Attenuazione a f<sub>0</sub>/2 [dB]"], righe, ["", "n", "n", "n", "n"])
    rl10 = fc.RlcSerie(10.0, RLC_L, RLC_C)
    b["RLC_F0"] = sig(rl10.f0, 5)
    b["RLC_Z0"] = sig(math.sqrt(RLC_L / RLC_C), 4)
    b["RLC_Q_DCR"] = it(fc.rlc_q_con_resistenza_induttore(10.0, RLC_L, RLC_C, 5.0), 1)
    b["RLC_Q_NOM"] = it(rl10.q, 1)
    xs = fc.griglia_log(0.3, 3.0, 300)
    curve = []
    for (r, cls) in zip(RLC_R, ("sa", "sb", "sc")):
        rl = fc.RlcSerie(r, RLC_L, RLC_C)
        curve.append((f"Q = {it(rl.q, 1)}  (R = {int(r)} Ω)", cls, [(x, fc.db(rl.h(x * rl.f0))) for x in xs]))
    b["FIG_RLC"] = figura(
        5, "Passa-banda RLC al variare di Q",
        "Risposta in ampiezza del passa-banda RLC serie in funzione di f/f0 per tre valori di Q.",
        grafico_bode(curve, 0.3, 3.0, -40, 3, [0.3, 0.5, 1, 2, 3], [-40, -30, -20, -10, -3, 0],
                     "ampiezza [dB]", "f / f₀", id_clip="c5", legenda_pos="basso-sinistra", ref_y=[-3]),
        None, "Aumentando Q (diminuendo R) la banda si restringe attorno a f<sub>0</sub>; il guadagno al centro resta 0 dB perché l'uscita è sulla resistenza.")
    b["FIG_SCHEMA_RLC"] = figura(6, "RLC serie con uscita sulla resistenza", "Schema del circuito RLC serie, con uscita ai capi della resistenza.",
                                 schema_rlc(), None, "Alla risonanza le reattanze di L e C si annullano e la corrente è limitata solo da R: tutta la tensione di ingresso cade su R.")

    # --- Q del secondo ordine -----------------------------------------------------------------
    righe = []
    for q in (0.5, 1 / math.sqrt(2), 1.0, 2.0, 5.0):
        pm, pf = fc.picco_e_frequenza(lambda f, q=q: fc.h2_lp(f, 1.0, q), 0.05, 5.0, 8000)
        righe.append(riga([it(q, 4), it(fc.db(fc.h2_lp(1.0, 1.0, q))), it(fc.db(pm)) if pm > 1.0005 else "nessun picco",
                           it(pf, 3) if pm > 1.0005 else "—"], ["n", "n", "n", "n"]))
    b["TAB_Q"] = tabella(["Q", "|H(f<sub>0</sub>)| [dB]", "Picco massimo [dB]", "Frequenza del picco [f/f<sub>0</sub>]"], righe, ["n"] * 4)
    b["FIG_Q"] = figura(
        7, "Effetto di Q sul passa-basso del secondo ordine",
        "Risposta in ampiezza di un passa-basso del secondo ordine per Q da 0,5 a 5.",
        grafico_bode([("Q = 0,5", "sm", serie_db(lambda f: fc.h2_lp(f, 1, 0.5), 0.1, 10)),
                      ("Q = 0,707", "sa", serie_db(lambda f: fc.h2_lp(f, 1, 1 / math.sqrt(2)), 0.1, 10)),
                      ("Q = 1", "sb", serie_db(lambda f: fc.h2_lp(f, 1, 1.0), 0.1, 10)),
                      ("Q = 2", "sc", serie_db(lambda f: fc.h2_lp(f, 1, 2.0), 0.1, 10)),
                      ("Q = 5", "se", serie_db(lambda f: fc.h2_lp(f, 1, 5.0), 0.1, 10))],
                     0.1, 10, -50, 20, [0.1, 0.2, 0.5, 1, 2, 5, 10], [-40, -20, -3, 0, 20],
                     "ampiezza [dB]", "f / f₀", altezza=320, id_clip="c7", legenda_pos="basso-sinistra", ref_y=[0]),
        None, "Q = 1/√2 è il caso maximally flat (Butterworth): nessun picco e −3 dB in f<sub>0</sub>. Per Q maggiore compare un picco vicino a f<sub>0</sub>, per Q minore il ginocchio si smorza.")

    # --- Butterworth: Q e attenuazioni --------------------------------------------------------
    righe = []
    for n in range(1, 7):
        sez = fc.butterworth(n, 1.0)
        qs = ", ".join(it(s.q, 4) for s in sorted([s for s in sez if s.ordine == 2], key=lambda s: s.q))
        if n % 2:
            qs = (qs + ", " if qs else "") + "1º ordine"
        righe.append(riga([str(n), qs, it(-fc.db(fc.risposta_cascata(sez, 2.0)), 1), it(-fc.db(fc.risposta_cascata(sez, 10.0)), 1), str(20 * n)],
                          ["n", "", "n", "n", "n"]))
    b["TAB_BW"] = tabella(["Ordine n", "Q delle sezioni (f<sub>0</sub> = f<sub>c</sub>)", "Attenuazione a 2f<sub>c</sub> [dB]", "a 10f<sub>c</sub> [dB]", "Pendenza asintotica [dB/dec]"],
                          righe, ["n", "", "n", "n", "n"])
    b["FIG_BW"] = figura(
        8, "Butterworth passa-basso dal primo al sesto ordine",
        "Risposta in ampiezza di filtri Butterworth passa-basso per ordini da 1 a 6.",
        grafico_bode([(f"n = {n}", cls, serie_db(lambda f, n=n: fc.risposta_cascata(fc.butterworth(n, 1.0), f), 0.1, 10))
                      for n, cls in ((1, "sm"), (2, "sa"), (3, "sb"), (4, "sc"), (6, "se"))],
                     0.1, 10, -100, 3, [0.1, 0.2, 0.5, 1, 2, 5, 10], [-100, -80, -60, -40, -20, -3, 0],
                     "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", altezza=320, id_clip="c8", legenda_pos="basso-sinistra", ref_y=[-3]),
        None, "Tutte le curve passano per −3 dB in f/f<sub>c</sub> = 1; ogni ordine in più aggiunge 20 dB/decade di pendenza.")

    # --- confronto famiglie -------------------------------------------------------------------
    bw2, ch2, be2 = fc.butterworth(2, 1.0)[0], fc.chebyshev(2, 1.0, 1.0)[0], fc.bessel2(1.0)
    righe = []
    for nome, s in (("Butterworth", bw2), ("Chebyshev 1 dB", ch2), ("Bessel", be2)):
        h2 = lambda f, s=s: fc.h2_lp(f, s.f0, s.q)
        pm, _ = fc.picco_e_frequenza(h2, 0.05, 3.0, 4000)
        righe.append(riga([nome, it(s.f0, 4), it(s.q, 4), it(max(fc.db(pm), 0.0)), it(fc.db(h2(2.0)), 1)], ["", "n", "n", "n", "n"]))
    b["TAB_FAMIGLIE"] = tabella(["Famiglia (n = 2)", "f<sub>0</sub>/f<sub>c</sub>", "Q", "Picco [dB]", "Ampiezza a 2f<sub>c</sub> [dB]"], righe, ["", "n", "n", "n", "n"])
    b["FIG_FAMIGLIE"] = figura(
        9, "Tre famiglie di filtri del secondo ordine",
        "Confronto tra Butterworth, Chebyshev con ripple di 1 dB e Bessel del secondo ordine.",
        grafico_bode([("Bessel", "sm", serie_db(lambda f: fc.h2_lp(f, be2.f0, be2.q), 0.1, 10)),
                      ("Butterworth", "sa", serie_db(lambda f: fc.h2_lp(f, bw2.f0, bw2.q), 0.1, 10)),
                      ("Chebyshev 1 dB", "sc", serie_db(lambda f: fc.h2_lp(f, ch2.f0, ch2.q), 0.1, 10))],
                     0.1, 10, -50, 3, [0.1, 0.2, 0.5, 1, 2, 5, 10], [-50, -40, -30, -20, -10, -3, 0],
                     "ampiezza [dB]", "f / f<tspan dy='3' font-size='9'>c</tspan>", id_clip="c9", legenda_pos="basso-sinistra", ref_y=[-3]),
        None, "Bessel e Butterworth hanno −3 dB in f<sub>c</sub>; per Chebyshev f<sub>c</sub> è il limite della banda con ripple (qui 0 dB a DC e ripple fino a +1 dB nella banda passante di una sezione con guadagno DC unitario).")

    # --- Chebyshev 4 ordine: Q delle sezioni --------------------------------------------------
    righe = []
    for n, r in ((2, 0.5), (2, 1.0), (4, 0.5), (4, 1.0)):
        for s in sorted(fc.chebyshev(n, r, 1.0), key=lambda s: s.q):
            righe.append(riga([str(n), sig(r), it(s.f0, 4), it(s.q, 4)], ["n"] * 4))
    b["TAB_CHEB"] = tabella(["Ordine", "Ripple [dB]", "f<sub>0</sub>/f<sub>c</sub>", "Q"], righe, ["n"] * 4)

    # --- Sallen-Key: progetto e verifica ------------------------------------------------------
    sk2 = fc.progetta_cascata_butterworth_lp(2, SK_FC, SK_C2)
    sk4 = fc.progetta_cascata_butterworth_lp(4, SK_FC, SK_C2)
    sk3 = fc.progetta_cascata_butterworth_lp(3, SK_FC, SK_C2)

    def riga_sk(n, i, s):
        if isinstance(s, fc.SezioneRc1):
            return riga([str(n), str(i), "1º ordine", "—", si(s.r, "Ω"), "—", si(s.c, "F"), "—",
                         sig(s.f0, 5), "—", "—"], ["n", "n", "", "n", "n", "n", "n", "n", "n", "n", "n"])
        err = (s.q / s.q_obiettivo - 1) * 100
        return riga([str(n), str(i), "SK", it(s.q_obiettivo, 4), si(s.r1, "Ω"), si(s.r2, "Ω"), si(s.c1, "F"), si(s.c2, "F"),
                     sig(s.f0, 5), it(s.q, 4), it(err, 2, True) + "%"], ["n", "n", "", "n", "n", "n", "n", "n", "n", "n", "n"])
    righe = []
    for n, sez in ((2, sk2), (3, sk3), (4, sk4)):
        for i, s in enumerate(sez, 1):
            righe.append(riga_sk(n, i, s))
    b["TAB_SK_PROGETTO"] = tabella(
        ["n", "Sez.", "Q obiettivo", "R<sub>1</sub>", "R<sub>2</sub>", "C<sub>1</sub>", "C<sub>2</sub>", "f<sub>0</sub> [Hz]", "Q reale", "Errore Q"],
        righe, ["n"] * 10)

    # esempio di calcolo della sezione 2 di Butterworth con Q = 1/sqrt(2)
    s2 = sk2[0]
    q2 = 1 / math.sqrt(2)
    r1i, r2i = fc.sk_lp_unitario(SK_FC, q2, s2.c1, s2.c2)
    b["EX_C1_MIN"] = si(4 * q2 * q2 * SK_C2, "F")
    b["EX_C1"] = si(s2.c1, "F")
    b["EX_SOMMA"] = si(r1i + r2i, "Ω", 5)
    b["EX_PROD"] = sci(r1i * r2i, 4)
    b["EX_R1"] = si(r1i, "Ω", 5)
    b["EX_R2"] = si(r2i, "Ω", 5)
    b["EX_R1N"] = si(s2.r1, "Ω")
    b["EX_R2N"] = si(s2.r2, "Ω")
    b["EX_F0"] = sig(s2.f0, 5)
    b["EX_Q"] = sig(s2.q, 4)

    def tabella_risposta(sez, freqs):
        righe = []
        for f in freqs:
            h = fc.risposta_cascata_reale(sez, f)
            righe.append(riga([si(f, "Hz"), sig(abs(h), 4), it(fc.db(h)), it(fc.fase_cascata_gradi(sez, f), 1)], ["n"] * 4))
        return tabella(["Frequenza", "|H|", "Ampiezza [dB]", "Fase [°]"], righe, ["n"] * 4)

    freq_lab = (50, 100, 500, 1000, 2000, 5000, 10000)
    b["TAB_RISP_N2"] = tabella_risposta(sk2, freq_lab)
    b["TAB_RISP_N4"] = tabella_risposta(sk4, freq_lab)
    pm4, pf4 = fc.picco_e_frequenza(lambda f: sk4[0].h(f), 100, 5000, 4000)
    b["SK4_S1_PICCO"] = it(fc.db(pm4))
    b["SK4_S1_PICCO_F"] = sig(pf4, 3)
    b["SK4_S1_PICCO_F_INT"] = f"{pf4:.0f}"
    pm4b, _ = fc.picco_e_frequenza(lambda f: sk4[1].h(f), 100, 5000, 4000)
    b["SK4_S2_PICCO"] = it(fc.db(pm4b))
    b["SK2_FC"] = sig(SK_FC, 4)
    c1p = s2.c1 * 1.1
    b["SK2_C1P_F0"] = sig(fc.sk_f0_q_unitario(s2.r1, s2.r2, c1p, s2.c2)[0], 4)
    b["SK2_C1P_Q"] = sig(fc.sk_f0_q_unitario(s2.r1, s2.r2, c1p, s2.c2)[1], 3)

    # Sallen-Key: grafici dei Butterworth reali n=2,4
    b["FIG_SK_RISP"] = figura(
        10, "Risposta dei filtri Sallen-Key progettati",
        "Ampiezza in dB del Butterworth di secondo e quarto ordine con valori normalizzati, e della sola prima sezione del quarto ordine.",
        grafico_bode([("n = 2", "sa", serie_db(lambda f: fc.risposta_cascata_reale(sk2, f), 50, 20000)),
                      ("n = 4", "sc", serie_db(lambda f: fc.risposta_cascata_reale(sk4, f), 50, 20000)),
                      ("sez. 1 di n = 4 (Q = 1,30)", "sm dash", serie_db(lambda f: sk4[0].h(f), 50, 20000))],
                     50, 20000, -90, 6, [50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000], [-80, -60, -40, -20, -3, 0],
                     "ampiezza [dB]", "frequenza [Hz]", altezza=320, id_clip="c10", legenda_pos="basso-sinistra", ref_y=[-3]),
        None, "Curve calcolate con i valori normalizzati E96/E12 della tabella del progetto e amplificatori ideali. La sezione a Q più alto presenta un picco di circa +3 dB.", cfg="cfg-b")
    b["FIG_SK"] = figura(11, "Sallen-Key passa-basso a guadagno unitario",
                         "R1 e R2 in serie dall'ingresso all'ingresso non invertente, C2 a massa, C1 dal nodo intermedio all'uscita; l'operazionale è un buffer.",
                         schema_sk_lp(), None, "C1 riporta in ingresso una frazione dell'uscita (reazione positiva): è ciò che alza Q senza induttori. L'operazionale come buffer isola il filtro dal carico.", cfg="cfg-b")
    b["FIG_SK_LP_K"] = figura(12, "Sallen-Key passa-basso a componenti uguali", "R, R, C, C con guadagno K ottenuto dalla rete Rf/Rg sull'ingresso invertente.",
                              schema_sk_k("lp"), None, "Qui f<sub>0</sub> = 1/(2πRC) e Q = 1/(3 − K), con K = 1 + R<sub>f</sub>/R<sub>g</sub>.", cfg="cfg-b")
    b["FIG_SK_HP_K"] = figura(13, "Sallen-Key passa-alto a componenti uguali", "Versione duale: C, C in serie, R verso massa e R in reazione, con rete Rf/Rg.",
                              schema_sk_k("hp"), None, "È il circuito duale del precedente: R e C scambiano i ruoli e restano uguali f<sub>0</sub>, Q e K.", cfg="cfg-b")

    # --- K e Q a componenti uguali ------------------------------------------------------------
    righe = []
    for q in (0.5, 0.7071, 1.0, 2.0, 5.0):
        k = 3 - 1 / q
        pm, _ = fc.picco_e_frequenza(lambda f, q=q, k=k: fc.h2_lp(f, 1.0, q, k), 0.05, 5.0, 8000)
        righe.append(riga([it(q, 4), it(k, 3), it(k - 1, 3), it(fc.db(k), 2), it(fc.db(max(pm, k)), 2)], ["n"] * 5))
    b["TAB_K"] = tabella(["Q", "K = 3 − 1/Q", "R<sub>f</sub>/R<sub>g</sub>", "Guadagno di banda [dB]", "Picco massimo [dB]"], righe, ["n"] * 5)

    # equal-component esempio
    r, k, rf = fc.sk_guadagno_componenti_uguali(1000.0, 2.0, 10e-9)
    b["EQ_R"] = si(r, "Ω")
    b["EQ_K"] = it(k, 2)
    b["EQ_PICCO"] = it(fc.db(max(abs(fc.h2_lp(f, 1000.0, 2.0, k)) for f in fc.griglia_log(100, 5000, 3000))), 1)

    # --- GBW ------------------------------------------------------------------------------------
    r1a, r2a = fc.sk_lp_unitario(SK_FC, 1 / math.sqrt(2), 22e-9, 10e-9)
    r1b, r2b = fc.sk_lp_unitario(SK_FC, 1.3066, 100e-9, 10e-9)
    righe = []
    ida, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1a, r2a, 22e-9, 10e-9), 10, 1e5)
    idb, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9), 10, 1e5)
    for rap in (5, 10, 20, 50, 100, 1000):
        gbw = rap * SK_FC
        pa, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1a, r2a, 22e-9, 10e-9, gbw=gbw), 10, 1e5)
        pb, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9, gbw=gbw), 10, 1e5)
        a10 = fc.db(fc.h_sk_lp(10 * SK_FC, r1b, r2b, 100e-9, 10e-9, gbw=gbw))
        righe.append(riga([str(rap), it(fc.db(pa) - fc.db(ida), 2, True), it(fc.db(pb) - fc.db(idb), 2, True), it(a10, 1)], ["n"] * 4))
    a10_id = fc.db(fc.h_sk_lp(10 * SK_FC, r1b, r2b, 100e-9, 10e-9))
    righe.append(riga(["∞ (ideale)", "0,00", "0,00", it(a10_id, 1)], ["n"] * 4))
    b["TAB_GBW"] = tabella(["GBW / f<sub>0</sub>", "Errore del picco, Q = 0,707 [dB]", "Errore del picco, Q = 1,307 [dB]", "Ampiezza a 10f<sub>0</sub>, Q = 1,307 [dB]"],
                           righe, ["n"] * 4)
    b["FIG_GBW"] = figura(
        14, "Effetto del prodotto guadagno–banda sulla sezione a Q alto",
        "Risposta della sezione Sallen-Key con Q 1,307 e f0 1 kHz per amplificatore ideale e con GBW pari a 100, 20 e 10 volte f0.",
        grafico_bode([("ideale", "sd", [(f, fc.db(fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9))) for f in fc.griglia_log(200, 5000, 200)]),
                      ("GBW = 100 f₀", "sb", [(f, fc.db(fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9, gbw=100 * SK_FC))) for f in fc.griglia_log(200, 5000, 200)]),
                      ("GBW = 20 f₀", "sa", [(f, fc.db(fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9, gbw=20 * SK_FC))) for f in fc.griglia_log(200, 5000, 200)]),
                      ("GBW = 10 f₀", "se", [(f, fc.db(fc.h_sk_lp(f, r1b, r2b, 100e-9, 10e-9, gbw=10 * SK_FC))) for f in fc.griglia_log(200, 5000, 200)])],
                     200, 5000, -50, 6, [200, 500, 1000, 2000, 5000], [-40, -30, -20, -10, 0, 3],
                     "ampiezza [dB]", "frequenza [Hz]", id_clip="c14", legenda_pos="basso-sinistra"),
        None, "Con GBW limitato il picco sale e la pendenza in banda oscura aumenta rispetto al modello ideale. Il modello usa un solo polo e uscita ideale: non include l'impedenza di uscita dell'amplificatore.", cfg="cfg-c")
    # rumore termico e slew rate
    k_b, temp = 1.380649e-23, 300.0
    b["NOISE_10K"] = it(math.sqrt(4 * k_b * temp * 10e3) * 1e9, 1)
    b["NOISE_10K_1K"] = it(math.sqrt(4 * k_b * temp * 10e3 * 1000.0) * 1e6, 2)
    b["SR_1K"] = it(2 * math.pi * 1e3 * 1.0 * 1e-6, 4)
    b["SR_100K"] = it(2 * math.pi * 1e5 * 1.0 * 1e-6, 2)

    # --- anti-aliasing -----------------------------------------------------------------------
    righe = []
    for n in range(2, 7):
        celle = [str(n)]
        for fcut in (1000.0, 1500.0):
            sez = fc.butterworth(n, fcut)
            celle += [it(-fc.db(fc.risposta_cascata(sez, 1000.0)), 2), it(-fc.db(fc.risposta_cascata(sez, 9000.0)), 1)]
        righe.append(riga(celle, ["n"] * 5))
    b["TAB_ALIAS"] = tabella(["n", "f<sub>c</sub> = 1 kHz: attenuazione a 1 kHz [dB]", "a 9 kHz [dB]", "f<sub>c</sub> = 1,5 kHz: a 1 kHz [dB]", "a 9 kHz [dB]"], righe, ["n"] * 5)
    b["ALIAS_12"] = it(20 * math.log10(2 ** 12), 1)
    b["ALIAS_16"] = it(20 * math.log10(2 ** 16), 1)
    b["ALIAS_N6_45"] = it(-fc.db(fc.risposta_cascata(fc.butterworth(6, 5000.0), 45000.0)), 1)
    b["ALIAS_N5_45"] = it(-fc.db(fc.risposta_cascata(fc.butterworth(5, 5000.0), 45000.0)), 1)

    # --- risposte numeriche agli esercizi ------------------------------------------------------
    r_es1 = 1.0 / (2 * math.pi * 2000.0 * 47e-9)
    r_es1n = fc.arrotonda_serie(r_es1, "E96")
    r_th = r_es1n * 10e3 / (r_es1n + 10e3)
    fc_single = SK_FC / float(it(lo / f0, 3).replace(",", "."))
    r_es3 = 1.0 / (2 * math.pi * fc_single * 100e-9)
    w0 = 2 * math.pi * 5000.0
    c_es4 = 100e-9
    l_es4 = 1.0 / (w0 * w0 * c_es4)
    r_es4 = math.sqrt(l_es4 / c_es4) / 10.0
    s5 = fc.progetta_sezione_sk(2000.0, 1 / math.sqrt(2), 4.7e-9)
    b["SOL1"] = f"R = {si(r_es1, chr(0x3a9), 4)} → E96: {si(r_es1n, chr(0x3a9))}, f<sub>c</sub> = {sig(fc.rc_fc(r_es1n, 47e-9), 5)} Hz"
    b["SOL2"] = f"guadagno DC {it(10e3 / (r_es1n + 10e3), 3)}, f<sub>c</sub> = {sig(fc.rc_fc(r_th, 47e-9), 5)} Hz"
    b["SOL3"] = f"f<sub>c</sub> della singola cella = {sig(fc_single, 5)} Hz → R = {si(r_es3, chr(0x3a9))} (E96: {si(fc.arrotonda_serie(r_es3, 'E96'), chr(0x3a9))})"
    b["SOL4"] = f"L = {si(l_es4, 'H')}, R = √(L/C)/Q = {si(r_es4, chr(0x3a9))}"
    b["SOL5"] = (f"C<sub>1</sub> = {si(s5.c1, 'F')}, C<sub>2</sub> = {si(s5.c2, 'F')}, R<sub>1</sub> = {si(s5.r1, chr(0x3a9))}, R<sub>2</sub> = {si(s5.r2, chr(0x3a9))} "
                 f"→ f<sub>0</sub> = {sig(s5.f0, 5)} Hz, Q = {sig(s5.q, 4)}")
    b["SOL6"] = f"K = 2,5, R<sub>f</sub>/R<sub>g</sub> = 1,5, R = {si(r, chr(0x3a9))}; picco di circa {b['EQ_PICCO']} dB sopra 0 dB"
    b["SOL7"] = f"n = 6 (n = 5 dà {b['ALIAS_N5_45']} dB, n = 6 dà {b['ALIAS_N6_45']} dB; richiesti {b['ALIAS_16']} dB)"
    return b


