"""Figure con didascalia e tabelle del capitolo su Butterworth, Chebyshev e Bessel (valori calcolati)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
import disegno_famiglie as df  # noqa: E402
from disegno import figura  # noqa: E402
from formati import it, riga, sig, si, tabella  # noqa: E402

MENO = "−"
OHM = "Ω"
FAM = (("butterworth", "Butterworth"), ("chebyshev", "Chebyshev 1 dB"), ("bessel", "Bessel"))


def _fig(chiave, titolo, desc, svg, didascalia, cfg="cfg-b"):
    return figura(chiave, titolo, desc, svg, None, didascalia, cfg=cfg)


def _figure():
    f = {}
    f["FIG_TRE_IDEE"] = _fig("treidee", "Che cosa ottimizza ciascuna famiglia", "Tre piccoli grafici: modulo piatto del Butterworth, ripple costante del Chebyshev, ritardo quasi costante del Bessel in banda.", df.fig_tre_idee(),
                             "Ogni famiglia è la soluzione di un problema di ottimizzazione diverso. Butterworth rende il modulo il più piatto possibile in banda passante; Chebyshev rende equiampiezza il ripple in banda per ottenere una transizione più ripida; Bessel rende il ritardo di gruppo il più piatto possibile nella banda utile.")
    f["FIG_POLINOMI_CH"] = _fig("polch", "I polinomi di Chebyshev", "Polinomi di Chebyshev da T1 a T5: oscillano tra meno uno e più uno per x tra meno uno e uno e crescono rapidamente fuori.", df.fig_polinomi_chebyshev(),
                                "Ogni polinomio T<sub>n</sub> resta tra −1 e +1 per |x| ≤ 1 (zona colorata) e fuori da quell'intervallo cresce molto in fretta. Nel filtro, x = f/f<sub>c</sub>: dentro la banda passante il polinomio fa «oscillare» la risposta, fuori la fa precipitare.")
    f["FIG_EQUIRIPPLE"] = _fig("equiripple", "L'ondulazione costante in banda passante", "Banda passante di quattro Chebyshev da 1 dB con ordine da 2 a 5, normalizzati al massimo.", df.fig_equiripple_cheb(),
                               "Il ripple resta compreso tra 0 e −1 dB e la curva tocca alternativamente i due bordi della fascia. Sulla banda positiva, gli n + 1 estremi comprendono i due bordi della banda; per esempio, con n = 4 si hanno cinque estremi e due oscillazioni complete.")
    f["FIG_POLI_BW_N"] = _fig("polibw", "Poli di Butterworth da n = 3 a n = 6", "Quattro piani complessi con i poli di un Butterworth su una circonferenza, con il Q di ogni coppia.", df.fig_poli_butterworth_n(),
                              "I poli di un Butterworth di ordine n stanno sulla semicirconferenza sinistra, a intervalli di 180°/n. Le coppie più vicine all'asse jω hanno Q più alto.")
    f["FIG_POLI_CH_RIPPLE"] = _fig("polich", "Poli di Chebyshev al variare del ripple", "Tre piani complessi con i poli di un Chebyshev del quarto ordine per ripple di 0,5, 1 e 3 dB.", df.fig_poli_chebyshev_ripple(),
                                   "Aumentando il ripple l'ellisse su cui stanno i poli si stringe e i poli si avvicinano all'asse jω: la discesa diventa più ripida, ma il Q massimo cresce rapidamente.")
    f["FIG_POLI_BE_N"] = _fig("polibe", "Poli di Bessel da n = 2 a n = 4", "Tre piani complessi con i poli di un Bessel per ordine da 2 a 4, con il Q di ogni coppia.", df.fig_poli_bessel_n(),
                              "I poli del Bessel hanno Q basso (0,5–0,8) e sono lontani dall'asse jω: è la ragione per cui non c'è picco e la risposta è dolce.")
    f["FIG_CONFR_N4"] = _fig("confrn4", "Quarto ordine: ampiezza delle cinque varianti", "Risposta in ampiezza in dB di Bessel, Butterworth e Chebyshev da 0,5, 1 e 3 dB, tutti del quarto ordine.", df.fig_confronto_n4_modulo(),
                             "Alla stessa frequenza di taglio e allo stesso ordine, le famiglie differiscono nella banda di transizione: il Chebyshev scende prima e più in fretta, il Bessel più tardi e più dolcemente.")
    f["FIG_TRANS_N4"] = _fig("transn4", "La banda di transizione a confronto", "Ingrandimento della regione tra 0,6 e 2,5 volte la frequenza di taglio per le cinque varianti del quarto ordine.", df.fig_transizione_n4(),
                             "Ingrandita la zona che conta: a 2 f<sub>c</sub> il Butterworth attenua 24 dB circa, il Bessel meno di 14 dB, il Chebyshev da 3 dB più di 35 dB. Le linee tratteggiate segnano −3 e −40 dB.")
    f["FIG_FASE_N4"] = _fig("fasen4", "La fase: quanto è lineare", "Fase di Bessel, Butterworth e Chebyshev del quarto ordine confrontata con una fase lineare ideale.", df.fig_fase_n4(),
                             "Una fase lineare corrisponde a un ritardo costante e conserva la forma del segnale nelle componenti considerate. Il Bessel approssima bene questa condizione, nel caso mostrato, fino a circa 1,5 f<sub>c</sub>; il Chebyshev se ne allontana molto prima.")
    f["FIG_RITARDO_N4"] = _fig("ritn4", "Ritardo di gruppo a quarto ordine", "Ritardo di gruppo normalizzato di Bessel, Butterworth e Chebyshev del quarto ordine.", df.fig_ritardo_n4(),
                               "Il ritardo di gruppo del Bessel è quasi costante fino alla frequenza di taglio. Quello del Butterworth ha un rigonfiamento, quello del Chebyshev un picco molto alto vicino a f<sub>c</sub>: le componenti vicine a quella zona subiscono un ritardo maggiore.")
    f["FIG_GRADINO_N4"] = _fig("gradn4", "Risposta al gradino a quarto ordine", "Risposta al gradino di Bessel, Butterworth e Chebyshev del quarto ordine.", df.fig_gradino_n4(),
                               "Il Bessel sale senza quasi superare il valore finale; il Butterworth lo supera di circa il 11 %; il Chebyshev di oltre il 20 % e oscilla più a lungo.")
    f["FIG_IMPULSO_N4"] = _fig("impn4", "Un impulso rettangolare attraversa il filtro", "Impulso rettangolare in ingresso e uscita dei tre filtri del quarto ordine.", df.fig_impulso_n4(),
                               "Un impulso rettangolare contiene molte frequenze. Il Bessel tende a conservarne meglio la forma temporale nella banda utile, pur arrotondando i fronti; Butterworth e Chebyshev mostrano sovraelongazione e, soprattutto per Chebyshev, una coda oscillante.")
    f["FIG_FORMA"] = _fig("forma", "Il fattore di forma", "Barre che mostrano il rapporto tra la frequenza di attenuazione di 40 dB e quella di taglio per cinque filtri del quarto ordine.", df.fig_fattore_forma(),
                          "Il fattore di forma misura la stretta della transizione: più è piccolo, meno spazio occupa la zona di transizione. A parità di ordine il Chebyshev vince, il Bessel perde.")
    f["FIG_ORDINE_MIN"] = _fig("ordmin", "Quanti poli servono", "Ordine minimo in funzione dell'attenuazione richiesta a 3 volte la frequenza di taglio per le tre famiglie.", df.fig_ordine_minimo(),
                               "Per ottenere la stessa attenuazione a 3 f<sub>c</sub> il Chebyshev richiede meno poli del Butterworth, e il Bessel di più; oltre circa 34 dB il Bessel non ci arriva affatto, qualunque sia l'ordine.")
    f["FIG_QMAX"] = _fig("qmax", "Il Q della sezione più critica", "Q massimo delle sezioni in funzione dell'ordine per Butterworth, Chebyshev 1 e 3 dB e Bessel.", df.fig_qmax_famiglie(),
                         "Più alto è il Q, più il circuito è sensibile alle tolleranze e più banda serve all'amplificatore. Il Chebyshev ha Q molto alti già a ordine medio; il Bessel resta sempre sotto 2.")
    f["FIG_ALBERO"] = _fig("albero", "Come scegliere la famiglia", "Albero decisionale: dal requisito principale alla famiglia di filtri più adatta.", df.schema_albero_scelta(),
                           "La scelta parte dal requisito più importante, non dalla familiarità. Se non c'è un requisito particolare si parte da Butterworth.")
    return f


def _sezioni_testo(sez, fc_ref=1.0):
    """Elenco 'f0/fc · Q' delle sezioni, una per riga HTML."""
    righe = []
    for s in sez:
        righe.append(f"{it(s.f0 / fc_ref, 3)} · {it(s.q, 3)}" if s.ordine == 2 else f"{it(s.f0 / fc_ref, 3)} · 1° ord.")
    return "<br>".join(righe)


def _tabelle():
    t = {}
    # polinomi di Bessel
    righe = []
    for n in range(1, 6):
        c = fc.coefficienti_bessel(n)
        termini = []
        for k in range(n, -1, -1):
            if c[k] == 0:
                continue
            potenza = "" if k == 0 else ("s" if k == 1 else f"s<sup>{k}</sup>")
            coef = "" if (c[k] == 1 and k > 0) else str(c[k])
            termini.append(coef + potenza)
        sez = fc.bessel(n, 1.0) if n >= 2 else [fc.Sezione(1, 1.0)]
        qs = ", ".join(it(s.q, 4) for s in sez if s.ordine == 2) or "—"
        righe.append(riga([str(n), "θ<sub>" + str(n) + "</sub>(s) = " + " + ".join(termini), qs], ["n", "", "n"]))
    t["TAB_POLINOMI_BESSEL"] = tabella(["n", "Polinomio di Bessel inverso", "Q delle sezioni"], righe, ["n", "", "n"])

    # coefficienti Butterworth, Chebyshev, Bessel
    righe = []
    for n in range(2, 9):
        sez = fc.butterworth(n, 1.0)
        qs = ", ".join(it(s.q, 3) for s in sorted([s for s in sez if s.ordine == 2], key=lambda s: s.q))
        righe.append(riga([str(n), qs + (", 1° ordine" if n % 2 else "")], ["n", ""]))
    t["TAB_COEFF_BW"] = tabella(["n", "Q delle sezioni (f<sub>0</sub> = f<sub>c</sub>)"], righe, ["n", ""])
    righe = []
    for n in range(2, 7):
        celle = [str(n)]
        for r in (0.5, 1.0, 3.0):
            celle.append(_sezioni_testo(sorted(fc.chebyshev(n, r, 1.0), key=lambda s: s.q)))
        righe.append(riga(celle, ["n", "n", "n", "n"]))
    t["TAB_COEFF_CH"] = tabella(["n", "0,5 dB: f<sub>0</sub>/f<sub>c</sub> · Q", "1 dB: f<sub>0</sub>/f<sub>c</sub> · Q", "3 dB: f<sub>0</sub>/f<sub>c</sub> · Q"], righe, ["n", "n", "n", "n"])
    righe = []
    for n in range(2, 9):
        righe.append(riga([str(n), _sezioni_testo(sorted(fc.bessel(n, 1.0), key=lambda s: s.q))], ["n", "n"]))
    t["TAB_COEFF_BE"] = tabella(["n", "f<sub>0</sub>/f<sub>c</sub> · Q delle sezioni (f<sub>c</sub> a −3 dB)"], righe, ["n", "n"])

    # frequenza a -3 dB del Chebyshev
    righe = []
    for r in (0.1, 0.5, 1.0, 2.0, 3.0):
        righe.append(riga([sig(r, 2).replace(".", ",") + " dB"] + [it(fc.chebyshev_f3db_su_fc(n, r), 3) for n in (2, 3, 4, 5, 6)], ["", "n", "n", "n", "n", "n"]))
    t["TAB_F3DB_CH"] = tabella(["Ripple", "n = 2", "n = 3", "n = 4", "n = 5", "n = 6"], righe, ["", "n", "n", "n", "n", "n"])
    t["CH1_F3DB_N4"] = it(fc.chebyshev_f3db_su_fc(4, 1.0), 3)
    t["CH1_F3DB_N4_HZ"] = sig(fc.chebyshev_f3db_su_fc(4, 1.0) * 1000, 4)

    # confronto n = 4
    nomi = [("Bessel", fc.bessel(4, 1.0)), ("Butterworth", fc.butterworth(4, 1.0)), ("Chebyshev 0,5 dB", fc.chebyshev(4, 0.5, 1.0)),
            ("Chebyshev 1 dB", fc.chebyshev(4, 1.0, 1.0)), ("Chebyshev 3 dB", fc.chebyshev(4, 3.0, 1.0))]
    righe = []
    valori = {}
    for nome, sez in nomi:
        f3 = fc.f_3db(sez, riferimento="picco")
        ff = fc.frequenza_attenuazione(sez, 40.0) / f3
        g = fc.risposta_gradino(sez, 3.0, punti=900)
        over = max(0.0, max(y for _, y in g) - 1.0) * 100
        tau0 = fc.ritardo_gruppo(sez, 0.02)
        var = max(fc.ritardo_gruppo(sez, x / 20) for x in range(1, 21)) / tau0 - 1
        valori[nome] = (f3, ff, over, var)
        righe.append(riga([nome, it(f3, 3), it(fc.attenuazione_db(sez, 1.5), 1), it(fc.attenuazione_db(sez, 2.0), 1), it(fc.attenuazione_db(sez, 3.0), 1),
                           it(ff, 2), it(over, 1), it(var * 100, 0)], ["", "n", "n", "n", "n", "n", "n", "n"]))
    t["TAB_CONFRONTO_N4"] = tabella(["Quarto ordine", "f<sub>−3 dB</sub>/f<sub>c</sub>", "Att. a 1,5 f<sub>c</sub> [dB]", "a 2 f<sub>c</sub> [dB]", "a 3 f<sub>c</sub> [dB]",
                                     "Fattore di forma", "Sovra-elong. [%]", "Variazione ritardo fino a f<sub>c</sub> [%]"],
                                    righe, ["", "n", "n", "n", "n", "n", "n", "n"], larga=True)
    t["N4_OVER_BE"] = it(valori["Bessel"][2], 1)
    t["N4_OVER_BW"] = it(valori["Butterworth"][2], 1)
    t["N4_OVER_CH1"] = it(valori["Chebyshev 1 dB"][2], 1)
    t["N4_FORMA_BE"] = it(valori["Bessel"][1], 2)
    t["N4_FORMA_BW"] = it(valori["Butterworth"][1], 2)
    t["N4_FORMA_CH1"] = it(valori["Chebyshev 1 dB"][1], 2)
    t["N4_ATT2_BW"] = it(fc.attenuazione_db(fc.butterworth(4, 1.0), 2.0), 1)
    t["N4_ATT2_BE"] = it(fc.attenuazione_db(fc.bessel(4, 1.0), 2.0), 1)
    t["N4_ATT2_CH3"] = it(fc.attenuazione_db(fc.chebyshev(4, 3.0, 1.0), 2.0), 1)

    # ordine minimo
    righe = []
    for att in (20, 30, 40, 50, 60):
        celle = [f"{att} dB"]
        for rapp in (2.0, 3.0, 5.0):
            ns = [fc.ordine_minimo(fam, att, rapp, ripple_db=1.0, n_max=12) for fam, _ in FAM]
            celle.append(" / ".join(str(n) if n is not None else "—" for n in ns))
        righe.append(riga(celle, ["", "n", "n", "n"]))
    t["TAB_ORDINI"] = tabella(["Attenuazione richiesta", "a 2 f<sub>c</sub>", "a 3 f<sub>c</sub>", "a 5 f<sub>c</sub>"], righe, ["", "n", "n", "n"])
    # specifica concreta: 30 e 40 dB a 3 fc
    righe = []
    for fam, nome in FAM:
        n30 = fc.ordine_minimo(fam, 30, 3.0, ripple_db=1.0, n_max=12)
        n40 = fc.ordine_minimo(fam, 40, 3.0, ripple_db=1.0, n_max=12)
        amp = lambda n: str((n + 1) // 2) if n is not None else "—"  # noqa: E731
        righe.append(riga([nome, str(n30) if n30 else "—", amp(n30), str(n40) if n40 else "non raggiungibile", amp(n40)], ["", "n", "n", "n", "n"]))
    t["TAB_SPEC_TRE"] = tabella(["Famiglia", "Ordine per 30 dB", "Operazionali", "Ordine per 40 dB", "Operazionali"], righe, ["", "n", "n", "n", "n"])
    massimi = [(fc.attenuazione_db(fc.bessel(n, 1.0), 2.0), n) for n in range(2, 13)]
    mx, nmx = max(massimi)
    t["BE_MAX_2FC"] = it(mx, 1)
    t["BE_MAX_2FC_N"] = str(nmx)
    t["BE_MAX_3FC"] = it(max(fc.attenuazione_db(fc.bessel(n, 1.0), 3.0) for n in range(2, 13)), 0)
    # limite gaussiano del Bessel: |H| = exp(-a x^2) con -3 dB in x = 1, quindi a = ln(sqrt 2)
    t["BE_GAUSS_2FC"] = it(20 * math.log10(math.e) * 4 * math.log(math.sqrt(2)), 1)

    # Butterworth: attenuazione in banda passante per n = 1..6
    righe = []
    for n in range(1, 7):
        sez = fc.butterworth(n, 1.0)
        righe.append(riga([str(n)] + [it(fc.attenuazione_db(sez, x), 3) for x in (0.3, 0.5, 0.8, 1.0)], ["n"] * 5))
    t["TAB_BW_BANDA"] = tabella(["n", "a 0,3 f<sub>c</sub> [dB]", "a 0,5 f<sub>c</sub> [dB]", "a 0,8 f<sub>c</sub> [dB]", "a f<sub>c</sub> [dB]"], righe, ["n"] * 5)

    # Chebyshev n = 4, 1 dB: parametri della formula
    eps = math.sqrt(10 ** 0.1 - 1)
    a4 = math.asinh(1 / eps) / 4
    t["CH1_EPS"] = it(eps, 4)
    t["CH1_A"] = it(a4, 4)
    t["CH1_SINH"] = it(math.sinh(a4), 4)
    t["CH1_COSH"] = it(math.cosh(a4), 4)

    # errore del modulo a f0 per amplificatore con GBW finito, al variare di Q
    righe = []
    for rap in (20, 50, 100, 200, 500):
        celle = [str(rap)]
        for q in (0.5219, 1.3066, 3.559):
            c2 = 10e-9
            c1 = fc.arrotonda_serie_per_eccesso(4 * q * q * c2 * 1.01, "E12")
            r1, r2 = fc.sk_lp_unitario(1000.0, q, c1, c2)
            ideale = abs(fc.h_sk_lp(1000.0, r1, r2, c1, c2))
            reale = abs(fc.h_sk_lp(1000.0, r1, r2, c1, c2, gbw=rap * 1000.0))
            celle.append(it(fc.db(reale) - fc.db(ideale), 2, True))
        righe.append(riga(celle, ["n"] * 4))
    t["TAB_GBW_Q"] = tabella(["GBW / f<sub>0</sub>", "Q = 0,52 (Bessel)", "Q = 1,31 (Butterworth)", "Q = 3,56 (Chebyshev 1 dB)"], righe, ["n"] * 4)

    # Q massimo
    righe = []
    for n in range(2, 9):
        qm = lambda sez: max((s.q for s in sez if s.ordine == 2), default=0.0)  # noqa: E731
        righe.append(riga([str(n), it(qm(fc.bessel(n, 1.0)), 2), it(qm(fc.butterworth(n, 1.0)), 2), it(qm(fc.chebyshev(n, 1.0, 1.0)), 2), it(qm(fc.chebyshev(n, 3.0, 1.0)), 2)],
                          ["n"] * 5))
    t["TAB_QMAX"] = tabella(["n", "Bessel", "Butterworth", "Chebyshev 1 dB", "Chebyshev 3 dB"], righe, ["n"] * 5)
    t["QMAX_CH1_N6"] = it(max(s.q for s in fc.chebyshev(6, 1.0, 1.0) if s.ordine == 2), 1)
    t["QMAX_CH1_N4"] = it(max(s.q for s in fc.chebyshev(4, 1.0, 1.0) if s.ordine == 2), 2)

    # esempi di progetto
    def tab_esempio(sez, c_base):
        prog = fc.progetta_cascata_lp(sez, c_base)
        righe = []
        for i, (te, re) in enumerate(zip(sez, prog), 1):
            if isinstance(re, fc.SezioneRc1):
                righe.append(riga([str(i), "1° ordine", "—", si(re.r, OHM), "—", si(re.c, "F"), "—", sig(re.f0, 5), "—"], ["n"] * 9))
            else:
                righe.append(riga([str(i), it(te.f0, 1) + " Hz", it(te.q, 3), si(re.r1, OHM), si(re.r2, OHM), si(re.c1, "F"), si(re.c2, "F"), sig(re.f0, 5), it(re.q, 3)], ["n"] * 9))
        return prog, tabella(["Sez.", "f<sub>0</sub> obiettivo", "Q obiettivo", "R<sub>1</sub>", "R<sub>2</sub>", "C<sub>1</sub>", "C<sub>2</sub>", "f<sub>0</sub> reale [Hz]", "Q reale"], righe, ["n"] * 9, larga=True)
    prog_ch, t["TAB_ESEMPIO_CH4"] = tab_esempio(fc.chebyshev(4, 1.0, 1000.0), 2.2e-9)
    prog_be, t["TAB_ESEMPIO_BE4"] = tab_esempio(fc.bessel(4, 1000.0), 10e-9)
    prog_bw = fc.progetta_cascata_lp(fc.butterworth(4, 1000.0), 10e-9)
    righe = []
    for f in (250.0, 500.0, 1000.0, 1500.0, 2000.0, 3000.0, 5000.0):
        righe.append(riga([si(f, "Hz"), it(fc.db(fc.risposta_cascata_reale(prog_be, f)), 2), it(fc.db(fc.risposta_cascata_reale(prog_bw, f)), 2),
                           it(fc.db(fc.risposta_cascata_reale(prog_ch, f)), 2)], ["n"] * 4))
    t["TAB_ESEMPIO_RISP"] = tabella(["Frequenza", "Bessel [dB]", "Butterworth [dB]", "Chebyshev 1 dB [dB]"], righe, ["n"] * 4)
    t["ESCH_C2"] = "2,2 nF"
    t["ESBE_C2"] = "10 nF"
    return t


def blocchi_famiglie():
    b = {}
    b.update(_figure())
    b.update(_tabelle())
    return b
