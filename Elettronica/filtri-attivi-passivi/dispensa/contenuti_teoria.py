"""Figure con didascalia e tabelle per la parte di teoria di base e gli esempi aggiunti."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import filtri_core as fc  # noqa: E402
import disegno_base as db  # noqa: E402
from disegno import figura  # noqa: E402
from formati import it, riga, sig, si, tabella  # noqa: E402


def _fig(chiave, titolo, desc, svg, didascalia, cfg=""):
    return figura(chiave, titolo, desc, svg, None, didascalia, cfg=cfg)


def blocchi_teoria():
    b = {}
    b["FIG_PERCORSO"] = _fig("percorso", "Il percorso della dispensa", "Quattro parti in sequenza: teoria di base, filtri passivi, filtri attivi, progetto e verifica.", db.schema_percorso(),
                             "Ogni parte si appoggia alla precedente. Se la teoria di base è già chiara si può partire dai filtri passivi.", cfg="cfg-d")
    b["FIG_IDRAULICA"] = _fig("idraulica", "Circuito elettrico e analogia con l'acqua", "Batteria, resistenza e corrente affiancate a pompa, tubo con restringimento e portata.", db.fig_idraulica(),
                              "Immaginare la corrente come acqua in un tubo aiuta: la tensione è la pressione della pompa, la resistenza è un restringimento. Più si stringe il tubo, meno acqua passa.", cfg="cfg-d")
    b["FIG_OHM"] = _fig("ohm", "Legge di Ohm: tensione e corrente in una resistenza", "Tre rette V = R I per resistenze di 100, 200 e 400 ohm.", db.fig_ohm(),
                        "Per una resistenza la tensione è proporzionale alla corrente. La pendenza della retta è la resistenza: più è ripida, più ohm ci sono.", cfg="cfg-d")
    b["FIG_SERIE_PAR"] = _fig("seriepar", "Resistenze in serie e in parallelo", "Due resistenze in serie e in parallelo con le formule della resistenza equivalente.", db.schema_serie_parallelo(),
                              "In serie la corrente è una sola e le resistenze si sommano. In parallelo la tensione è una sola e si sommano le correnti: il tubo ha due strade, passa più acqua e la resistenza totale scende.", cfg="cfg-d")
    b["FIG_PARTITORE"] = _fig("partitore", "Il partitore di tensione", "Due resistenze in serie con l'uscita presa tra loro e barra che mostra la ripartizione della tensione.", db.fig_partitore(),
                              "Due resistenze in serie dividono la tensione in proporzione ai loro valori: la più grande prende più tensione. Questo semplice circuito è l'idea alla base di ogni filtro RC.", cfg="cfg-d")
    b["FIG_CONDENSATORE"] = _fig("condensatore", "Il condensatore e l'analogia con la membrana", "Due armature separate da isolante e una membrana elastica in un tubo d'acqua.", db.fig_condensatore(),
                                 "Due piastre vicine immagazzinano carica: è un piccolo serbatoio di energia elettrica. Nell'analogia idraulica è una membrana che si tende: lascia passare l'acqua solo finché non è tesa.", cfg="cfg-d")
    b["FIG_CARICA_C"] = _fig("caricac", "Carica di un condensatore attraverso una resistenza", "Tensione che sale e corrente che scende, in funzione del tempo normalizzato alla costante di tempo.", db.fig_carica_condensatore(),
                             "All'inizio il condensatore è scarico e la corrente è massima; man mano che si carica la tensione sale e la corrente scende. La velocità è fissata da τ = RC: dopo τ la tensione ha raggiunto il 63 %.", cfg="cfg-d")
    b["FIG_COND_DC_AC"] = _fig("conddcac", "Il condensatore in continua e in alternata", "Circuito con generatore e condensatore: aperto in continua, trasparente in alternata ad alta frequenza.", db.schema_cond_dc_ac(),
                               "In continua il condensatore si carica una volta e poi blocca la corrente. In alternata si carica e si scarica di continuo: la corrente scorre avanti e indietro. Più la frequenza è alta, più facilmente «passa».", cfg="cfg-d")
    b["FIG_INDUTTORE"] = _fig("induttore", "L'induttore e il confronto con il condensatore", "Bobina con campo magnetico e tabella di confronto tra condensatore e induttore.", db.fig_induttore(),
                              "L'induttore è il «contrario» del condensatore: ciò che uno blocca, l'altro lascia passare. Per questo insieme formano circuiti risonanti.", cfg="cfg-d")
    b["FIG_SIN_CERCHIO"] = _fig("sincerchio", "La sinusoide come proiezione di un vettore che ruota", "Vettore che ruota su un cerchio e altezza del vettore tracciata nel tempo come sinusoide.", db.fig_sinusoide_cerchio(),
                                "Una sinusoide nasce da un movimento circolare: se un vettore ruota con velocità costante, la sua altezza nel tempo disegna una sinusoide. Un giro completo è un periodo.", cfg="cfg-d")
    b["FIG_PARAM_SIN"] = _fig("paramsin", "Ampiezza, frequenza e fase", "Tre coppie di sinusoidi che differiscono per ampiezza, frequenza e fase.", db.fig_parametri_sinusoide(),
                              "Ampiezza: quanto è alta. Frequenza: quante oscillazioni al secondo. Fase: dove parte rispetto a un riferimento.", cfg="cfg-d")
    b["FIG_PICCO_RMS"] = _fig("piccorms", "Valore di picco, picco-picco ed efficace", "Sinusoide con indicazione di picco, picco-picco e valore efficace.", db.fig_picco_rms(),
                              "Tre modi di misurare la stessa sinusoide. Il valore efficace è quello che produce lo stesso calore di una tensione continua: vale 0,707 volte il picco.", cfg="cfg-d")
    b["FIG_FASORI_RITARDO"] = _fig("fasoriritardo", "Fase e ritardo nel tempo", "Due fasori sfasati di 45 gradi e le due sinusoidi corrispondenti, una in ritardo di T/8.", db.fig_fasori_ritardo(),
                                   "Sfasare di un angolo significa ritardare nel tempo: 360° sono un periodo intero, quindi 45° sono un ottavo di periodo.", cfg="cfg-d")
    b["FIG_FASE_RCL"] = _fig("faserc", "Tensione e corrente in R, C e L", "Forme d'onda di tensione e corrente per resistenza, condensatore e induttore.", db.fig_fase_rcl(),
                             "Nella resistenza tensione e corrente sono in fase. Nel condensatore la corrente è in anticipo di 90°, nell'induttore in ritardo di 90°. Ricordarlo aiuta a capire tutti i filtri.", cfg="cfg-d")
    b["FIG_NUM_COMPLESSO"] = _fig("numcomplesso", "Il piano complesso", "Numero complesso 3 + j4 con modulo 5 e angolo di 53 gradi, e rotazione di 90 gradi con la moltiplicazione per j.", db.fig_numero_complesso(),
                                  "Un numero complesso è un punto del piano: la parte reale va in orizzontale, quella immaginaria in verticale. Il modulo è la distanza dall'origine, la fase è l'angolo.", cfg="cfg-d")
    b["FIG_SCATOLA"] = _fig("scatola", "Il filtro come scatola nera", "Un circuito con ingresso e uscita e tre esempi numerici di risposta a frequenze diverse.", db.schema_scatola_nera(),
                            "Un filtro si descrive dicendo che cosa esce per ogni frequenza che entra: ampiezza (e fase). Non serve sapere come è fatto dentro per usarlo.", cfg="cfg-d")
    b["FIG_SCALA_LOG"] = _fig("scalalog", "Scala lineare e scala logaritmica", "Confronto tra una retta numerica lineare e una logaritmica con i valori 1, 10, 100, 1000.", db.fig_scala_log(),
                              "Su una scala lineare 1, 10 e 100 si accalcano a sinistra. Su una scala logaritmica ogni moltiplicazione per 10 occupa lo stesso spazio.", cfg="cfg-d")
    b["FIG_SCALA_DB"] = _fig("scaladb", "La scala dei decibel", "Asse in decibel con i corrispondenti rapporti di ampiezza.", db.fig_scala_db(),
                             "Il decibel trasforma i prodotti in somme. Bastano pochi numeri a memoria: 0 dB = ×1, 6 dB = ×2, 20 dB = ×10, −3 dB = ×0,707.", cfg="cfg-d")
    b["FIG_LIN_VS_LOG"] = _fig("linlog", "Lo stesso filtro con frequenza lineare e logaritmica", "Risposta di un filtro RC tracciata con asse delle frequenze lineare e con asse logaritmico.", db.fig_lineare_vs_log(),
                               "La stessa curva è illeggibile su asse lineare e chiarissima su asse logaritmico. Per questo il diagramma di Bode usa l'asse logaritmico.", cfg="cfg-d")
    b["FIG_SETACCIO"] = _fig("setaccio", "Un filtro come un setaccio", "Spettro con un segnale utile e due disturbi prima e dopo un filtro passa-basso.", db.fig_filtro_setaccio(),
                             "Un filtro lascia passare le frequenze volute e attenua le altre, come un setaccio che trattiene i pezzi grossi. Qui il filtro lascia quasi intatto il segnale a 100 Hz e riduce molto i disturbi.", cfg="cfg-d")
    b["FIG_TIPI"] = _fig("tipi", "I quattro tipi di filtro", "Risposta ideale e reale di passa-basso, passa-alto, passa-banda ed elimina-banda.", db.fig_tipi_filtro(),
                         "Le quattro famiglie fondamentali. Il filtro ideale taglia di netto; quello reale ha un passaggio graduale: lo scopo del progetto è avvicinarsi all'ideale con il minimo di componenti.", cfg="cfg-d")
    b["FIG_SPECIFICHE"] = _fig("specifiche", "Il vocabolario di un filtro", "Risposta di un passa-basso con banda passante, banda di transizione, banda oscura, frequenza di taglio e pendenza.", db.fig_specifiche(),
                               "Le tre zone di un filtro passa-basso. Più è ripida la transizione, più ordine serve: ogni ordine aggiunge 20 dB/decade.", cfg="cfg-d")
    b["FIG_POLI_PEND"] = _fig("polipend", "Ogni polo aggiunge 20 dB/decade", "Risposta di una, due e tre celle RC uguali isolate.", db.fig_poli_pendenza(),
                              "Ogni cella RC del primo ordine «piega» la curva verso il basso di altri 20 dB per decade. L'ordine del filtro è proprio il numero di queste «piegature».", cfg="cfg-d")
    b["FIG_RC_ESEMPIO"] = _fig("rcesempio", "Esempio svolto: filtro RC in quattro passi", "Schema RC con i valori e quattro passaggi di calcolo numerico.", db.schema_rc_esempio(),
                               "Un esempio completo con i numeri: dai valori di R e C si ricavano costante di tempo, frequenza di taglio, attenuazione e fase a una frequenza scelta.", cfg="cfg-a")
    b["FIG_BARRE"] = _fig("barre", "Chi pesa di più prende più tensione", "Barre proporzionali alla resistenza e alla reattanza a tre frequenze diverse.", db.fig_barre_impedenza(),
                          "Lo stesso partitore di prima, ma con un condensatore al posto della seconda resistenza. Al variare della frequenza la reattanza cambia e con lei la frazione di tensione in uscita.", cfg="cfg-a")
    b["FIG_RETROAZIONE"] = _fig("retroazione", "La reazione negativa", "Schema a blocchi di un amplificatore con rete di reazione e calcolo del guadagno.", db.schema_retroazione(),
                                "Riportando all'ingresso una parte dell'uscita si ottiene un guadagno che dipende quasi solo dai componenti della rete di reazione, non dall'amplificatore. È il principio di tutti i circuiti con operazionale.", cfg="cfg-b")
    b["FIG_BUFFER"] = _fig("buffer", "Il buffer separa sorgente e carico", "Confronto tra un partitore con sorgente ad alta impedenza e lo stesso circuito con buffer.", db.schema_buffer_traduttore(),
                           "Senza buffer il carico «vede» la resistenza interna della sorgente e la tensione cala a un decimo; con il buffer la sorgente non è caricata e il carico riceve quasi tutta la tensione.", cfg="cfg-b")
    b["FIG_SK_ESEMPIO"] = _fig("skesempio", "Esempio: Sallen-Key con i valori calcolati", "Schema Sallen-Key a guadagno unitario con i valori dei componenti e i risultati di f0 e Q.", db.schema_sk_esempio(),
                               "Un filtro completo con i valori commerciali: i risultati reali sono vicinissimi all'obiettivo di 1 kHz e Q = 0,707.", cfg="cfg-b")
    b["FIG_CAMPIONAMENTO"] = _fig("campionamento", "Perché nasce l'aliasing", "Due sinusoidi a 1 kHz e 9 kHz che passano per gli stessi punti campionati a 10 kHz.", db.fig_campionamento_alias(),
                                  "Con un campione ogni 0,1 ms, un'onda a 9 kHz passa per gli stessi identici punti di un'onda a 1 kHz: il convertitore non può distinguerle. Per questo il filtro anti-aliasing deve eliminare i 9 kHz prima.", cfg="cfg-c")
    b["FIG_SCOPE"] = _fig("scope", "Schermo dell'oscilloscopio: come si leggono ampiezza e ritardo", "Griglia 10 per 8 divisioni con ingresso e uscita di un filtro RC e calcolo di rapporto e fase.", db.schermo_oscilloscopio(),
                          "Si conta il numero di divisioni e si moltiplica per la scala: 5 divisioni verticali a 0,2 V/div sono 1 V picco-picco; 0,6 divisioni orizzontali a 0,2 ms/div sono 0,125 ms, cioè 45° a 1 kHz.", cfg="cfg-a")
    return b


def tabelle_teoria():
    t = {}
    # tabella di scelta rapida di fc
    rs = (100.0, 1e3, 10e3, 100e3)
    cs = (1e-9, 10e-9, 100e-9, 1e-6)
    righe = []
    for r in rs:
        celle = [si(r, "Ω")]
        for c in cs:
            f = fc.rc_fc(r, c)
            celle.append(si(f, "Hz", 3))
        righe.append(riga(celle, [""] + ["n"] * len(cs)))
    t["TAB_FC_RC"] = tabella(["R \\ C"] + [si(c, "F") for c in cs], righe, [""] + ["n"] * len(cs))
    # tabella tensioni nei partitori d'esempio
    righe = []
    for r1, r2 in ((1e3, 1e3), (3e3, 1e3), (9e3, 1e3), (1e3, 9e3)):
        righe.append(riga([si(r1, "Ω"), si(r2, "Ω"), it(12 * r2 / (r1 + r2), 2) + " V", it(100 * r2 / (r1 + r2), 0) + " %"], ["n"] * 4))
    t["TAB_PARTITORI"] = tabella(["R₁", "R₂", "V<sub>out</sub> con V<sub>in</sub> = 12 V", "Frazione di V<sub>in</sub>"], righe, ["n"] * 4)
    # tabella reattanze a 100 nF e 10 mH
    righe = []
    for f in (50.0, 500.0, 5000.0, 50000.0):
        righe.append(riga([si(f, "Hz"), si(1 / (2 * math.pi * f * 100e-9), "Ω"), si(2 * math.pi * f * 10e-3, "Ω")], ["n"] * 3))
    t["TAB_REATT2"] = tabella(["Frequenza", "Condensatore 100 nF", "Induttore 10 mH"], righe, ["n"] * 3)
    return t


def blocchi_teoria_tutti():
    d = {}
    d.update(blocchi_teoria())
    d.update(tabelle_teoria())
    return d
