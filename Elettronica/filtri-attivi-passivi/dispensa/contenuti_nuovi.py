"""Figure con didascalia e tabelle numeriche aggiunte nella versione estesa della dispensa."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import filtri_core as fc  # noqa: E402
import disegno_didattico as dd  # noqa: E402
from disegno import figura  # noqa: E402
from formati import it, riga, sci, sig, si, tabella  # noqa: E402
from parametri import MOLT, RC_C, RC_R, RLC_C, RLC_L, RLC_R, SK_C2, SK_FC  # noqa: E402

MENO = "−"
FC = "f<sub>c</sub>"
F0 = "f<sub>0</sub>"


def _figure():
    f = {}
    f["FIG_LUOGO"] = figura(
        "luogo", "Il passa-basso RC nel piano complesso",
        "Semicerchio descritto dalla risposta H(jω), con ω = 2πf, e triangolo delle tensioni a f = fc.", dd.fig_luogo_rc(), None,
        "Il segnale di ingresso è il vettore V<sub>in</sub> lungo l'asse reale; la tensione sul condensatore è V<sub>in</sub> moltiplicata per H(jω), cioè accorciata e ruotata. "
        "Aumentando la frequenza il punto percorre il semicerchio da 1 a 0. A f = f<sub>c</sub> la tensione sulla resistenza e quella sul condensatore sono perpendicolari: "
        "il loro vettore somma è V<sub>in</sub>.")
    f["FIG_OSC"] = figura(
        "osc", "Ingresso e uscita del passa-basso a f = f<sub>c</sub>",
        "Due sinusoidi: l'uscita ha ampiezza 0,707 e ritardo di un ottavo di periodo rispetto all'ingresso.", dd.fig_oscillogramma(), None,
        "Un circuito lineare restituisce una sinusoide della stessa frequenza, con ampiezza e fase modificate. Qui l'uscita ha ampiezza 0,707 e ritarda di T/8, cioè di 45°. "
        "Questa è l'immagine che si osserva all'oscilloscopio nelle misure del capitolo {{cap:lab-passivi}}.")
    f["FIG_ASINT"] = figura(
        "asint", "Diagramma di Bode reale e asintotico",
        "Risposta del passa-basso RC e spezzata asintotica con scarto massimo di 3 dB in fc.", dd.fig_bode_asintotico(), None,
        "Il diagramma asintotico, fatto di due rette (0 dB e −20 dB/decade) che si incontrano in f<sub>c</sub>, è l'approssimazione che si traccia a mano. "
        "Lo scarto massimo rispetto alla curva reale è 3 dB in f<sub>c</sub>; mezza decade prima o dopo è circa 1 dB.")
    f["FIG_REATT_RC"] = figura(
        "reattrc", "Reattanza del condensatore e resistenza",
        "Grafico logaritmico di XC in funzione della frequenza e della resistenza R costante.", dd.fig_reattanza_rc(), None,
        "La reattanza del condensatore scende di 10 volte per ogni decade. Dove X<sub>C</sub> supera R il condensatore «pesa» come un circuito aperto e l'uscita segue l'ingresso; "
        "dove X<sub>C</sub> è minore di R l'uscita è cortocircuitata. L'incrocio dei due grafici è la frequenza di taglio.")
    f["FIG_GRADINO_RC"] = figura(
        "gradrc", "Risposta al gradino del circuito RC",
        "Carica esponenziale del condensatore con marcatori a 1, 2, 3, 4 e 5 costanti di tempo.", dd.fig_gradino_rc(), None,
        "Se l'ingresso passa bruscamente da 0 a V<sub>in</sub> l'uscita sale con una curva esponenziale. La tangente iniziale raggiungerebbe il valore finale in un tempo τ = RC, "
        "ma nello stesso tempo la curva arriva solo al 63,2 %.")
    f["FIG_THEVENIN"] = figura(
        "thev", "Equivalente di Thevenin del carico",
        "Circuito RC con resistenza di carico in parallelo al condensatore e relativo equivalente di Thevenin.", dd.schema_thevenin(), None,
        "Visto dal condensatore, tutto ciò che sta a sinistra (generatore, R e R<sub>L</sub>) equivale a un unico generatore V<sub>th</sub> con una resistenza serie R<sub>th</sub>. "
        "Il circuito è tornato un RC semplice, di cui si conoscono tutte le formule.")
    f["FIG_CASCATA_RC"] = figura(
        "cascrc", "Cascata di celle RC con e senza buffer",
        "Due celle RC collegate direttamente e due celle separate da un buffer.", dd.schema_cascata_rc(), None,
        "Nella cascata diretta la seconda cella assorbe una corrente dal nodo del primo condensatore e ne altera la tensione; con un buffer le due celle non si influenzano.")
    f["FIG_ZOUT"] = figura(
        "zout", "Partitore tra impedenza di uscita e impedenza di ingresso",
        "Generatore con impedenza di uscita e carico con impedenza di ingresso formano un partitore di tensione.", dd.schema_zout_zin(), None,
        "Qualsiasi sorgente reale ha un'impedenza di uscita e qualsiasi carico un'impedenza di ingresso: quando si collegano, la tensione si ripartisce come in un partitore. "
        "La regola pratica è che l'impedenza di ingresso sia almeno 10 volte (meglio 100) quella di uscita.")
    f["FIG_REATT_LC"] = figura(
        "reattlc", "Reattanze di L e di C",
        "Reattanza di un induttore da 10 mH e di un condensatore da 100 nF in funzione della frequenza, con una resistenza di 100 ohm.", dd.fig_reattanze_lc(), None,
        "La reattanza dell'induttore sale con la frequenza, quella del condensatore scende: si incontrano a f<sub>0</sub>. Poiché le due reattanze hanno segno opposto, "
        "in quel punto si annullano a vicenda e rimane solo la resistenza.")
    f["FIG_FASORI_RIS"] = figura(
        "fasoris", "Fasori alla risonanza",
        "Tensioni su R, L e C alla risonanza: V_L e V_C uguali e opposte, pari a Q volte la tensione di ingresso.", dd.fig_fasori_risonanza(), None,
        "Alla risonanza V<sub>L</sub> e V<sub>C</sub> sono opposte e si annullano, ma ciascuna è Q volte più grande della tensione di ingresso: per questo un circuito risonante ad alto Q può avere tensioni molto più alte di quelle applicate.")
    f["FIG_LAB_COLL"] = figura(
        "labcoll", "Collegamento degli strumenti",
        "Generatore con resistenza serie, circuito in prova e oscilloscopio con due canali, con massa comune.", dd.schema_collegamento_lab(), None,
        "Il canale 1 misura l'ingresso nel punto P, a circuito collegato; il canale 2 misura l'uscita nel punto Q. La massa dell'oscilloscopio è la stessa del generatore e del circuito: un'unica massa evita misure falsate.")
    f["FIG_LISS"] = figura(
        "liss", "Figure di Lissajous per la misura di fase",
        "Ellissi ottenute con ingresso su X e uscita su Y per sfasamenti di 0, 45 e 90 gradi.", dd.fig_lissajous(), None,
        "In modo XY la figura è una retta se i segnali sono in fase, un cerchio se sono in quadratura (a parità di ampiezza) e un'ellisse inclinata nei casi intermedi. "
        "L'intercetta sull'asse Y rispetto al massimo dà direttamente il seno dello sfasamento.")
    f["FIG_OPAMP"] = figura(
        "opamp", "Operazionale ideale: non invertente e buffer",
        "Amplificatore non invertente con Rf e Rg e inseguitore di tensione, con le proprietà dell'operazionale ideale.", dd.schema_opamp_regole(), None,
        "Con reazione negativa l'operazionale porta le due entrate allo stesso potenziale. In un non invertente questo fissa la tensione ai capi di R<sub>g</sub> a V<sub>in</sub>, "
        "da cui il guadagno 1 + R<sub>f</sub>/R<sub>g</sub>; nel buffer R<sub>f</sub> = 0 e R<sub>g</sub> infinita danno guadagno 1.", cfg="cfg-b")
    f["FIG_SK_STATI"] = figura(
        "skstati", "Come funziona il Sallen-Key nelle tre zone di frequenza",
        "Il circuito Sallen-Key con i condensatori aperti, normali o in cortocircuito a bassa, media e alta frequenza.", dd.schema_sk_stati(), None,
        "A bassa frequenza i condensatori sono aperti e il segnale passa invariato; ad alta frequenza C<sub>2</sub> lo porta a massa; vicino a f<sub>0</sub> C<sub>1</sub> riporta in ingresso parte dell'uscita "
        "(reazione positiva) e determina il picco. È il punto in cui si decide Q.", cfg="cfg-b")
    f["FIG_QK"] = figura(
        "qk", "Q in funzione del guadagno K",
        "Curva Q = 1/(3 - K) con evidenza della crescita rapida per K vicino a 3.", dd.fig_q_vs_k(), None,
        "Q cresce lentamente fino a K ≈ 2 e poi in modo molto rapido: per K = 2,9 vale 10, per K = 2,95 vale 20. Una piccola variazione di R<sub>f</sub>/R<sub>g</sub> ha quindi un effetto grande sul Q.", cfg="cfg-b")
    f["FIG_POLI"] = figura(
        "poli", "Poli di Butterworth, Chebyshev e Bessel nel piano s",
        "Posizione dei poli per un Butterworth del quarto ordine, un Chebyshev da 1 dB del quarto ordine e un Bessel del secondo ordine.", dd.fig_poli_s(), None,
        "I poli di un filtro stabile stanno a sinistra dell'asse immaginario. Butterworth li dispone su una circonferenza (massima piattezza), Chebyshev su un'ellisse più stretta (più selettività, con ripple), "
        "Bessel su una curva che dà il ritardo più costante. Più i poli sono vicini all'asse immaginario, più alto è il Q e più marcato il picco.", cfg="cfg-b")
    f["FIG_GRADINO_Q"] = figura(
        "gradq", "Risposta al gradino di un secondo ordine al variare di Q",
        "Risposta al gradino per Q uguale a 0,5, 0,707, 1, 2 e 5 in funzione del tempo normalizzato.", dd.fig_gradino_q(), None,
        "Con Q = 0,5 non c'è sovraelongazione; con Q = 0,707 è piccola (4,3 %); con Q crescente le oscillazioni si fanno più ampie e durano di più. Il Q che nel dominio della frequenza dà il picco, nel tempo dà l'oscillazione smorzata.", cfg="cfg-b")
    f["FIG_GRADINO_FAM"] = figura(
        "gradfam", "Risposta al gradino delle tre famiglie (secondo ordine)",
        "Confronto di sovraelongazione tra Bessel, Butterworth e Chebyshev del secondo ordine.", dd.fig_gradino_famiglie(), None,
        "Bessel sale senza quasi sovraelongazione, Butterworth ne ha una piccola, Chebyshev è più veloce nel salire ma supera il valore finale di più e oscilla più a lungo.", cfg="cfg-b")
    f["FIG_RITARDO"] = figura(
        "rit", "Ritardo di gruppo delle tre famiglie",
        "Ritardo di gruppo normalizzato in funzione della frequenza per Bessel, Butterworth e Chebyshev del secondo ordine.", dd.fig_ritardo_gruppo(), None,
        "Il ritardo di gruppo descrive il ritardo delle componenti vicine in frequenza. Il Bessel lo mantiene approssimativamente costante nella banda utile, riducendo la distorsione temporale; non lo rende costante a tutte le frequenze. "
        "Nel Chebyshev il ritardo varia maggiormente e presenta un picco vicino al limite della banda.", cfg="cfg-b")
    f["FIG_RIPPLE"] = figura(
        "ripple", "Ripple in banda passante di Butterworth e Chebyshev",
        "Zoom della banda passante per Butterworth e per Chebyshev con ripple di 1 e di 3 dB, ordine 4.", dd.fig_ripple(), None,
        "Un Butterworth di ordine 4 è piatto fino a circa 0,5 f<sub>c</sub> e poi scende; i Chebyshev oscillano tra 0 dB e il ripple fissato, ma cadono molto più rapidamente appena fuori banda. "
        "Con il guadagno di continua normalizzato a 1 il ripple compare tra 0 e +R dB.", cfg="cfg-b")
    f["FIG_CASC_SOMMA"] = figura(
        "cascsomma", "Due sezioni in cascata: le curve in dB si sommano",
        "Risposta della sezione 1, della sezione 2 e del filtro di quarto ordine risultante.", dd.fig_cascata_somma(), None,
        "La sezione a Q alto ha un picco di circa 3 dB, la sezione a Q basso un ginocchio smorzato; sommate in dB danno la risposta piatta e ripida del quarto ordine. Ciascuna sezione da sola scende solo di 40 dB/decade.", cfg="cfg-b")
    f["FIG_CASC_BLOCCHI"] = figura(
        "cascbl", "Quarto ordine come cascata di due sezioni",
        "Schema a blocchi di due sezioni Sallen-Key del secondo ordine in cascata.", dd.schema_cascata_blocchi(), None,
        "Ogni sezione ha un proprio Q: il prodotto delle risposte, cioè la somma in dB, riproduce il filtro desiderato.", cfg="cfg-b")
    f["FIG_AO"] = figura(
        "ao", "Guadagno dell'operazionale ad anello aperto e chiuso",
        "Guadagno in dB di un operazionale ad anello aperto con GBW 1 MHz e ad anello chiuso per K = 1, 10 e 100.", dd.fig_guadagno_ao(), None,
        "Il guadagno ad anello aperto A(f) scende di 20 dB/decade. Con reazione il guadagno è K finché K è molto minore di A(f); poi segue A(f). "
        "Nel modello a polo dominante la banda a −3 dB è circa GBW/K: per un buffer (K = 1) è circa GBW, per K = 100 circa GBW/100. I valori sono illustrativi, non di un componente reale.", cfg="cfg-c")
    f["FIG_SLEW"] = figura(
        "slew", "Slew rate: l'uscita non segue la pendenza richiesta",
        "Sinusoide di 100 kHz e uscita limitata da uno slew rate di 0,3 V/us.", dd.fig_slew(), None,
        "Se la pendenza richiesta dalla sinusoide, 2πfV<sub>p</sub>, supera lo slew rate, l'uscita viaggia a pendenza costante e la forma d'onda diventa triangolare, con perdita di ampiezza e distorsione.", cfg="cfg-c")
    f["FIG_TOLL"] = figura(
        "toll", "Effetto delle tolleranze dei condensatori",
        "Risposta del Sallen-Key del secondo ordine con C1 e C2 variati del 10 per cento.", dd.fig_tolleranze(), None,
        "Una variazione del 10 % dei condensatori sposta la risposta di qualche punto percentuale in frequenza e modifica il Q; con condensatori al 5 % e resistenze all'1 % l'effetto totale resta nell'ordine di pochi punti percentuali.", cfg="cfg-c")
    f["FIG_MONOALIM"] = figura(
        "monoalim", "Sallen-Key con alimentazione singola",
        "Partitore di riferimento Vcc/2 e filtro Sallen-Key con ingresso accoppiato in alternata e C2 collegato al riferimento.", dd.schema_sk_monoalim(), None,
        "Con una sola alimentazione si crea un riferimento a V<sub>cc</sub>/2 con un partitore disaccoppiato; tutti i ritorni a massa del filtro vanno al riferimento e non a massa vera.", cfg="cfg-c")
    f["FIG_ALIAS"] = figura(
        "alias", "Aliasing nel dominio della frequenza",
        "Spettro prima del campionamento, dopo il campionamento senza filtro e dopo il campionamento con filtro di quarto ordine.", dd.fig_aliasing(), None,
        "Campionando a f<sub>s</sub>, una componente da f<sub>s</sub>/2 a f<sub>s</sub> si ripiega a f<sub>s</sub> − f: qui 9 kHz diventa 1 kHz e si sovrappone al segnale utile, da cui non è più distinguibile. Componenti in bande di Nyquist superiori si ripiegano secondo la stessa periodicità e alternanza. "
        "Il filtro deve eliminarla prima del campionamento.", cfg="cfg-c")
    f["FIG_MASCHERA"] = figura(
        "mask", "Maschera di specifica e filtri candidati",
        "Zone vietate della risposta (banda passante e banda oscura) con tre filtri Butterworth candidati.", dd.fig_maschera(), None,
        "La specifica si disegna come due zone proibite. Il filtro è accettabile se la curva le evita entrambe: qui solo il quinto ordine con f<sub>c</sub> = 1,5 kHz.", cfg="cfg-c")
    f["FIG_FLUSSO_PROG"] = figura(
        "flussoprog", "Procedura di progetto",
        "Sequenza dei sei passi dal requisito alla misura, con ritorno se la specifica non è rispettata.", dd.schema_flusso_progetto(), None,
        "Il progetto è iterativo: se la misura o la verifica dei limiti reali non rispetta la specifica si torna a rivedere famiglia, ordine o componenti.", cfg="cfg-c")
    f["FIG_FLUSSO_DIAG"] = figura(
        "flussodiag", "Diagnostica: dal sintomo alla verifica",
        "Quattro sintomi tipici con la verifica da eseguire per ciascuno.", dd.schema_flusso_diagnostica(), None,
        "Si parte dal sintomo, non dalla causa presunta: ogni verifica è un'azione con un risultato leggibile.", cfg="cfg-c")
    return f


def _tabelle():
    t = {}
    f0 = fc.rc_fc(RC_R, RC_C)
    tau = RC_R * RC_C

    # decibel
    righe = []
    for r in (10, 2, math.sqrt(2), 1.0, 1 / math.sqrt(2), 0.5, 0.1, 0.01):
        righe.append(riga([sig(r, 4), it(20 * math.log10(r), 2, True), sig(r * r, 4), it(10 * math.log10(r * r), 2, True)], ["n"] * 4))
    t["TAB_DB"] = tabella(["Rapporto di tensioni", "[dB]", "Rapporto di potenze", "[dB]"], righe, ["n"] * 4)

    # reattanze
    righe = []
    for f in (100.0, 1000.0, 10000.0, 100000.0):
        righe.append(riga([si(f, "Hz"), si(1 / (2 * math.pi * f * RC_C), "Ω"), si(2 * math.pi * f * RLC_L, "Ω")], ["n"] * 3))
    t["TAB_REATT"] = tabella(["Frequenza", "X<sub>C</sub> con C = 100 nF", "X<sub>L</sub> con L = 10 mH"], righe, ["n"] * 3)

    # gradino RC
    righe = []
    for k in (0.5, 1, 2, 3, 4, 5):
        v = 1 - math.exp(-k)
        righe.append(riga([sig(k, 3), it(v * 100, 1), it((1 - v) * 100, 2), si(k * tau, "s")], ["n"] * 4))
    t["TAB_GRADINO_RC"] = tabella(["t / τ", "V<sub>out</sub> raggiunta [%]", "Scarto residuo [%]", "t con τ = 160 µs"], righe, ["n"] * 4)
    t["RC_TAU_US"] = sig(tau * 1e6, 4)
    t["RC_TR"] = si(math.log(9) * tau, "s", 3)
    t["RC_TR_COEFF"] = it(math.log(9), 3)
    t["RC_T1PC"] = si(math.log(100) * tau, "s", 3)
    t["RC_T01PC"] = si(math.log(1000) * tau, "s", 3)
    t["RC_TR_FC"] = it(math.log(9) / (2 * math.pi), 3)
    t["RC_FC_CIFRE"] = sig(f0, 5)

    # tensioni RLC
    righe = []
    for r in RLC_R:
        rl = fc.RlcSerie(r, RLC_L, RLC_C)
        righe.append(riga([si(r, "Ω"), it(rl.q, 2), it(rl.q, 2) + " V", si(1.0 / r, "A")], ["", "n", "n", "n"]))
    t["TAB_RLC_TENSIONI"] = tabella(["R", "Q", "V<sub>L</sub> = V<sub>C</sub> con V<sub>in</sub> = 1 V", "Corrente I = V<sub>in</sub>/R"], righe, ["", "n", "n", "n"])

    # gradino famiglie
    righe = []
    for nome, sez, t_max in (("Bessel, n = 2", [fc.bessel2(1.0)], 3.0), ("Butterworth, n = 2", fc.butterworth(2, 1.0), 3.0),
                             ("Chebyshev 1 dB, n = 2", fc.chebyshev(2, 1.0, 1.0), 3.0),
                             ("Butterworth, n = 4", fc.butterworth(4, 1.0), 3.0), ("Chebyshev 1 dB, n = 4", fc.chebyshev(4, 1.0, 1.0), 3.0)):
        r = fc.risposta_gradino(sez, t_max, punti=900)
        picco = max(y for _, y in r) - 1.0
        qs = ", ".join(it(s.q, 3) for s in sorted([s for s in sez if s.ordine == 2], key=lambda s: s.q))
        righe.append(riga([nome, qs, it(max(picco, 0) * 100, 1)], ["", "n", "n"]))
    t["TAB_GRADINO_FAM"] = tabella(["Filtro", "Q delle sezioni", "Sovraelongazione al gradino [%]"], righe, ["", "n", "n"])
    r4 = fc.risposta_gradino(fc.butterworth(4, 1.0), 3.0, punti=900)
    t["OVER_BW4"] = it((max(y for _, y in r4) - 1.0) * 100, 1)
    bessel_over = fc.sovraelongazione_h2(1 / math.sqrt(3))
    t["OVER_BESSEL"] = it(bessel_over * 100, 2)
    t["OVER_BW2"] = it(fc.sovraelongazione_h2(1 / math.sqrt(2)) * 100, 1)
    t["OVER_CH2"] = it(fc.sovraelongazione_h2(fc.chebyshev(2, 1.0, 1.0)[0].q) * 100, 1)

    # ritardo di gruppo
    righe = []
    for nome, sez in (("Bessel", [fc.bessel2(1.0)]), ("Butterworth", fc.butterworth(2, 1.0)), ("Chebyshev 1 dB", fc.chebyshev(2, 1.0, 1.0))):
        v = [fc.ritardo_gruppo(sez, x) * 2 * math.pi for x in (0.02, 0.5, 1.0)]
        variazione = (max(v) / v[0] - 1) * 100
        righe.append(riga([nome, it(v[0], 3), it(v[1], 3), it(v[2], 3), it(variazione, 0, True) + " %"], ["", "n", "n", "n", "n"]))
    t["TAB_RITARDO"] = tabella(["Famiglia (n = 2)", "a DC", "a 0,5 f<sub>c</sub>", "a f<sub>c</sub>", "Massima variazione fino a f<sub>c</sub>"],
                               righe, ["", "n", "n", "n", "n"])

    # tolleranze
    s = fc.progetta_cascata_butterworth_lp(2, SK_FC, SK_C2)[0]
    f0n, qn = fc.sk_f0_q_unitario(s.r1, s.r2, s.c1, s.c2)
    righe = []
    for nome, k1, k2 in (("nominale", 1.0, 1.0), ("C₁ +10 %", 1.1, 1.0), ("C₁ −10 %", 0.9, 1.0), ("C₂ +10 %", 1.0, 1.1),
                         ("C₂ −10 %", 1.0, 0.9), ("C₁ e C₂ +10 %", 1.1, 1.1)):
        f0v, qv = fc.sk_f0_q_unitario(s.r1, s.r2, s.c1 * k1, s.c2 * k2)
        righe.append(riga([nome, sig(f0v, 5), it((f0v / f0n - 1) * 100, 1, True) + " %", it(qv, 3), it((qv / qn - 1) * 100, 1, True) + " %"],
                          ["", "n", "n", "n", "n"]))
    t["TAB_TOLL"] = tabella(["Variazione", "f<sub>0</sub> [Hz]", "Δf<sub>0</sub>", "Q", "ΔQ"], righe, ["", "n", "n", "n", "n"])
    # caso peggiore per componenti al 1 % (R) e al 5 % (C)
    f0s, qs_ = [], []
    for a in (0.99, 1.01):
        for b in (0.99, 1.01):
            for c in (0.95, 1.05):
                for d in (0.95, 1.05):
                    fv, qv = fc.sk_f0_q_unitario(s.r1 * a, s.r2 * b, s.c1 * c, s.c2 * d)
                    f0s.append(fv)
                    qs_.append(qv)
    t["TOLL_F0_MIN"] = it((min(f0s) / f0n - 1) * 100, 1, True)
    t["TOLL_F0_MAX"] = it((max(f0s) / f0n - 1) * 100, 1, True)
    t["TOLL_Q_MIN"] = it((min(qs_) / qn - 1) * 100, 1, True)
    t["TOLL_Q_MAX"] = it((max(qs_) / qn - 1) * 100, 1, True)

    # slew rate e rumore
    righe = []
    for f in (1e3, 1e4, 1e5, 1e6):
        righe.append(riga([si(f, "Hz"), it(2 * math.pi * f * 1.0 * 1e-6, 4 if f < 1e4 else 3), it(2 * math.pi * f * 5.0 * 1e-6, 3)], ["n"] * 3))
    t["TAB_SLEW"] = tabella(["Frequenza", "SR minimo con V<sub>p</sub> = 1 V [V/µs]", "con V<sub>p</sub> = 5 V [V/µs]"], righe, ["n"] * 3)
    kb, temp = 1.380649e-23, 300.0
    righe = []
    for r in (1e3, 10e3, 100e3):
        dens = math.sqrt(4 * kb * temp * r)
        righe.append(riga([si(r, "Ω"), it(dens * 1e9, 1), it(dens * math.sqrt(1e3) * 1e6, 2), it(dens * math.sqrt(20e3) * 1e6, 2)], ["n"] * 4))
    t["TAB_RUMORE"] = tabella(["R", "Densità [nV/√Hz]", "In 1 kHz [µV rms]", "In 20 kHz [µV rms]"], righe, ["n"] * 4)

    # maschera di specifica
    righe = []
    for n, fcut in ((4, 1000.0), (4, 1500.0), (5, 1500.0), (6, 1500.0)):
        sez = fc.butterworth(n, fcut)
        a1, a9 = -fc.db(fc.risposta_cascata(sez, 1000.0)), -fc.db(fc.risposta_cascata(sez, 9000.0))
        esito = "sì" if (a1 <= 0.5 and a9 >= 72.0) else ("no: banda passante" if a1 > 0.5 else "no: banda oscura")
        righe.append(riga([str(n), sig(fcut, 4), it(a1, 2), it(a9, 1), esito], ["n", "n", "n", "n", ""]))
    t["TAB_MASCHERA"] = tabella(["n", "f<sub>c</sub> [Hz]", "Attenuazione a 1 kHz [dB]", "a 9 kHz [dB]", "Rispetta la specifica?"], righe, ["n", "n", "n", "n", ""])
    sez5 = fc.butterworth(5, 1500.0)
    t["MASK_N5_1K"] = it(-fc.db(fc.risposta_cascata(sez5, 1000.0)), 2)
    t["MASK_N5_9K"] = it(-fc.db(fc.risposta_cascata(sez5, 9000.0)), 1)
    t["MASK_N4_9K"] = it(-fc.db(fc.risposta_cascata(fc.butterworth(4, 1500.0), 9000.0)), 1)

    # esempio di progetto: n = 5, fc = 1,5 kHz, C base 4,7 nF
    prog = fc.progetta_cascata_butterworth_lp(5, 1500.0, 4.7e-9)
    righe = []
    for i, sz in enumerate(prog, 1):
        if isinstance(sz, fc.SezioneRc1):
            righe.append(riga([str(i), "—", si(sz.r, "Ω"), "—", si(sz.c, "F"), "—", sig(sz.f0, 5), "—"], ["n"] * 8))
        else:
            righe.append(riga([str(i), it(sz.q_obiettivo, 3), si(sz.r1, "Ω"), si(sz.r2, "Ω"), si(sz.c1, "F"), si(sz.c2, "F"), sig(sz.f0, 5), it(sz.q, 3)], ["n"] * 8))
    t["TAB_ESEMPIO_PROG"] = tabella(["Sez.", "Q obiettivo", "R<sub>1</sub>", "R<sub>2</sub>", "C<sub>1</sub>", "C<sub>2</sub>", "f<sub>0</sub> [Hz]", "Q reale"], righe, ["n"] * 8)
    t["PROG_A1K"] = it(-fc.db(fc.risposta_cascata_reale(prog, 1000.0)), 2)
    t["PROG_A9K"] = it(-fc.db(fc.risposta_cascata_reale(prog, 9000.0)), 1)

    # schede di misura (valori attesi precompilati, colonne di misura vuote)
    righe = []
    for m in MOLT:
        h = fc.h_rc_lp(m * f0, f0)
        righe.append([sig(m), si(m * f0, "Hz"), it(fc.db(h)), it(fc.fase_gradi(h), 1)])
    t["SCHEDA_RC"] = dd.tabella_misura_vuota(["f/f<sub>c</sub>", "Frequenza", "Atteso [dB]", "Atteso [°]"], righe,
                                             ["V<sub>out</sub> [V<sub>pp</sub>]", "Misurato [dB]", "Δt [µs]", "Fase [°]"])
    freq_lab = (50, 100, 500, 1000, 2000, 5000, 10000)
    for chiave, ordine in (("SCHEDA_N2", 2), ("SCHEDA_N4", 4)):
        sez = fc.progetta_cascata_butterworth_lp(ordine, SK_FC, SK_C2)
        righe = []
        for f in freq_lab:
            h = fc.risposta_cascata_reale(sez, f)
            righe.append([si(f, "Hz"), it(fc.db(h)), it(fc.fase_cascata_gradi(sez, f), 1)])
        t[chiave] = dd.tabella_misura_vuota(["Frequenza", "Atteso [dB]", "Atteso [°]"], righe,
                                            ["V<sub>out</sub> [V<sub>pp</sub>]", "Misurato [dB]", "Δt [µs]", "Fase [°]"])
    return t


def blocchi_nuovi():
    from esercizi import html_esercizi  # import locale: esercizi usa gli stessi moduli
    b = {}
    b.update(_figure())
    b.update(_tabelle())
    b["ESERCIZI_HTML"] = html_esercizi()
    return b
