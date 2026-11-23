"""Esercizi della dispensa con svolgimento passo-passo: ogni numero è calcolato con src/filtri_core.py."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

import filtri_core as fc  # noqa: E402
from formati import it, sci, sig, si  # noqa: E402

OHM = "Ω"
MENO = "−"


def _sub(base, pedice):
    return f"{base}<sub>{pedice}</sub>"


FC = _sub("f", "c")
F0 = _sub("f", "0")


def _ex(testo, passi):
    corpo = "".join(f"<p>{p}</p>" for p in passi)
    return (f'<li><p class="ex-t">{testo}</p>'
            f'<details class="sv"><summary>Svolgimento</summary><div class="sv-b">{corpo}</div></details></li>')


def _rapporto_doppio():
    """Rapporto fc(3 dB)/fc(singola cella) per due celle RC identiche collegate direttamente."""
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if abs(fc.h_rc_lp_doppio(mid, 1.0, 1.0 / (2 * math.pi), 1.0, 1.0 / (2 * math.pi))) > 1 / math.sqrt(2):
            lo = mid
        else:
            hi = mid
    return lo


def _gbw_minimo(q, c1, c2, limite_db=0.5):
    f0 = 1000.0
    r1, r2 = fc.sk_lp_unitario(f0, q, c1, c2)
    ideale, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1, r2, c1, c2), 10, 1e5)
    risultati = []
    for rap in (5, 10, 20, 50, 100, 1000):
        reale, _ = fc.picco_e_frequenza(lambda f: fc.h_sk_lp(f, r1, r2, c1, c2, gbw=rap * f0), 10, 1e5)
        risultati.append((rap, fc.db(reale) - fc.db(ideale)))
    for rap, err in risultati:
        if err <= limite_db:
            return rap, err, risultati
    return None, None, risultati


def html_esercizi():
    parti = []

    # ---------------------------------------------------------------- Teoria di base
    e = []
    i_a = 5.0 / 220.0
    e.append(_ex("Una resistenza da 220 \u03a9 è collegata a una batteria da 5 V. Calcolare la corrente e la potenza dissipata.",
                 ["Si usa la legge di Ohm: I = V/R.", f"I = 5/220 = {it(i_a * 1000, 1)} mA.",
                  f"La potenza è P = V \u00b7 I = 5 \u00b7 {it(i_a, 4)} = {it(5 * i_a * 1000, 1)} mW (anche P = V\u00b2/R)."]))
    rs3 = (1000.0, 2200.0, 4700.0)
    par3 = 1.0 / sum(1 / r for r in rs3)
    e.append(_ex("Tre resistenze da 1 k\u03a9, 2,2 k\u03a9 e 4,7 k\u03a9: calcolare la resistenza totale collegandole in serie e in parallelo.",
                 [f"In serie si sommano: 1 + 2,2 + 4,7 = {it(sum(rs3) / 1000, 1)} k\u03a9.",
                  f"In parallelo si sommano gli inversi: 1/R = 1/1000 + 1/2200 + 1/4700 = {sig(sum(1 / r for r in rs3) * 1000, 4)} mS, quindi R = {si(par3, OHM, 4)}.",
                  "Controllo: la serie è maggiore della resistenza più grande, il parallelo è minore della più piccola."]))
    r1_p = 10000.0 * (10.0 / 2.5 - 1)
    e.append(_ex("Da una tensione di 10 V si vogliono ottenere 2,5 V con un partitore in cui R<sub>2</sub> = 10 k\u03a9. Calcolare R<sub>1</sub>.",
                 ["Dal partitore: V<sub>out</sub>/V<sub>in</sub> = R<sub>2</sub>/(R<sub>1</sub> + R<sub>2</sub>) = 2,5/10 = 0,25.",
                  "Quindi R<sub>1</sub> + R<sub>2</sub> = R<sub>2</sub>/0,25 = 4 R<sub>2</sub>, cioè R<sub>1</sub> = 3 R<sub>2</sub>.",
                  f"R<sub>1</sub> = 3 \u00b7 10 k\u03a9 = {si(r1_p, OHM)}. Verifica: 10 \u00b7 10/(30 + 10) = 2,5 V."]))
    tau4 = 47e3 * 22e-9
    e.append(_ex("Un condensatore da 22 nF si carica attraverso una resistenza da 47 k\u03a9. Calcolare la costante di tempo, la tensione dopo \u03c4 e il tempo per arrivare al 99 %.",
                 [f"\u03c4 = R C = 47000 \u00b7 22\u00b710\u207b\u2079 = {si(tau4, 's', 4)}.",
                  "Dopo \u03c4 la tensione ha raggiunto 1 \u2212 e\u207b\u00b9 = 63,2 % del valore finale.",
                  f"Per il 99 %: 1 \u2212 e\u207b\u1d57\u2044\u03c4 = 0,99, quindi t = \u03c4 ln(100) = {it(math.log(100), 2)} \u03c4 = {si(math.log(100) * tau4, 's', 3)}."]))
    vp5 = 3.0 * math.sqrt(2)
    e.append(_ex("Una sinusoide di 440 Hz ha valore efficace di 3,0 V. Calcolare il periodo, il valore di picco e il valore picco-picco. Qual è il periodo a 8 kHz?",
                 [f"Periodo T = 1/f = 1/440 = {si(1 / 440, 's', 4)}.",
                  f"V<sub>p</sub> = V<sub>rms</sub> \u00b7 \u221a2 = 3,0 \u00b7 1,414 = {it(vp5, 2)} V; V<sub>pp</sub> = 2 V<sub>p</sub> = {it(2 * vp5, 2)} V.",
                  f"A 8 kHz: T = 1/8000 = {si(1 / 8000, 's', 4)}."]))
    z6 = complex(6, -8)
    e.append(_ex("Dato z = 6 \u2212 j8, calcolare modulo e fase. Calcolare poi j \u00b7 z e dire di quanto è ruotato.",
                 [f"Modulo: |z| = \u221a(6\u00b2 + 8\u00b2) = \u221a100 = {it(abs(z6), 0)}.",
                  f"Fase: arctan(\u22128/6) = {it(math.degrees(math.atan2(z6.imag, z6.real)), 1)}\u00b0 (quarto quadrante).",
                  f"j \u00b7 z = j6 \u2212 j\u00b2 8 = 8 + j6; il modulo resta {it(abs(1j * z6), 0)} e la fase diventa {it(math.degrees(math.atan2((1j * z6).imag, (1j * z6).real)), 1)}\u00b0: è ruotato di +90\u00b0."]))
    e.append(_ex("Convertire in decibel il rapporto 0,25. Convertire 40 dB e \u221226 dB in rapporti di tensione. Due filtri in cascata attenuano di 12 dB e 14 dB: quanto attenuano insieme?",
                 [f"20 log\u2081\u2080(0,25) = {it(20 * math.log10(0.25), 2)} dB.",
                  f"40 dB \u2192 10^(40/20) = {it(10 ** 2, 0)}; \u221226 dB \u2192 10^(\u221226/20) = {it(10 ** (-26 / 20), 4)}.",
                  f"In cascata i decibel si sommano: 12 + 14 = 26 dB, cioè un fattore {it(10 ** (-26 / 20), 4)} sulla tensione (circa 1/20)."]))
    e.append(_ex("Calcolare la reattanza di un condensatore da 470 nF a 50 Hz e a 5 kHz, e quella di un induttore da 10 mH a 5 kHz.",
                 [f"X<sub>C</sub> = 1/(2\u03c0 f C): a 50 Hz: {si(1 / (2 * math.pi * 50 * 470e-9), OHM, 4)}; a 5 kHz: {si(1 / (2 * math.pi * 5000 * 470e-9), OHM, 4)}.",
                  f"X<sub>L</sub> = 2\u03c0 f L = 2\u03c0 \u00b7 5000 \u00b7 0,01 = {si(2 * math.pi * 5000 * 10e-3, OHM, 4)}.",
                  "Il condensatore ha una reattanza che scende di 100 volte quando la frequenza sale di 100 volte; l'induttore fa il contrario."]))
    parti.append(("Teoria di base", 1, e))

    # ---------------------------------------------------------------- Parte I
    e = []
    # 1
    r = 1.0 / (2 * math.pi * 2000.0 * 47e-9)
    rn = fc.arrotonda_serie(r, "E96")
    fce = fc.rc_fc(rn, 47e-9)
    e.append(_ex(
        f"Dimensionare un passa-basso RC con {FC} = 2 kHz e C = 47 nF. Scegliere R nella serie E96 e calcolare la {FC} effettiva.",
        [f"Si inverte la {{{{eq:fc_rc}}}}: R = 1/(2π {FC} C) = 1/(2π · 2000 · 47·10⁻⁹) = {si(r, OHM, 4)}.",
         f"Il valore E96 più vicino è {si(rn, OHM)}.",
         f"Con quel valore {FC} = 1/(2π · {sig(rn, 4)} · 47·10⁻⁹) = {sig(fce, 5)} Hz, cioè {it((fce / 2000 - 1) * 100, 2, True)} % rispetto all'obiettivo."]))
    # 2
    rl = 10e3
    rth = rn * rl / (rn + rl)
    e.append(_ex(f"Il filtro dell'esercizio 1 alimenta un carico di 10 k{OHM} in parallelo al condensatore. Calcolare guadagno in continua e nuova {FC}.",
                 [f"Equivalente di Thevenin visto dal condensatore: V<sub>th</sub>/V<sub>in</sub> = R<sub>L</sub>/(R + R<sub>L</sub>) = 10000/({sig(rn, 4)} + 10000) = {it(rl / (rn + rl), 3)}.",
                  f"R<sub>th</sub> = R ∥ R<sub>L</sub> = {sig(rn, 4)} · 10000/({sig(rn, 4)} + 10000) = {si(rth, OHM, 4)}.",
                  f"Nuova frequenza di taglio: 1/(2π R<sub>th</sub> C) = {sig(fc.rc_fc(rth, 47e-9), 5)} Hz; guadagno in continua {it(20 * math.log10(rl / (rn + rl)), 2)} dB."]))
    # 3
    e.append(_ex(f"Un passa-basso RC ha {FC} = 1 kHz. Calcolare modulo (anche in dB) e fase a 3 kHz.",
                 [f"x = f/{FC} = 3. |H| = 1/√(1 + x²) = 1/√10 = {it(1 / math.sqrt(10), 3)}.",
                  f"In decibel: 20 log<sub>10</sub>(0,316) = {it(20 * math.log10(1 / math.sqrt(10)), 2)} dB.",
                  f"Fase: φ = −arctan(x) = −arctan(3) = {it(-math.degrees(math.atan(3)), 1)}°."]))
    # 4
    dt = 80e-6
    phi = -360 * 1000.0 * dt
    fcm = 1000.0 / math.tan(math.radians(abs(phi)))
    e.append(_ex("In laboratorio, a 1 kHz, l'uscita di un passa-basso RC ritarda di 80 µs rispetto all'ingresso. Ricavare lo sfasamento, la frequenza di taglio e l'attenuazione attesa.",
                 [f"φ = −360° · f · Δt = −360 · 1000 · 80·10⁻⁶ = {it(phi, 1)}°.",
                  f"Dalla fase φ = −arctan(f/{FC}) si ricava {FC} = f/tan|φ| = 1000/tan({it(abs(phi), 1)}°) = {sig(fcm, 4)} Hz.",
                  f"Modulo atteso: |H| = cosφ = {it(math.cos(math.radians(phi)), 3)}, cioè {it(20 * math.log10(math.cos(math.radians(phi))), 2)} dB (per un RC del primo ordine |H| = cosφ)."]))
    # 5
    rapp = _rapporto_doppio()
    fcs = 1000.0 / rapp
    r_es = 1.0 / (2 * math.pi * fcs * 100e-9)
    rn5 = fc.arrotonda_serie(r_es, "E96")
    e.append(_ex(f"Due celle RC identiche, collegate direttamente, devono dare una {FC} complessiva di 1 kHz a −3 dB, con C = 100 nF. Calcolare R.",
                 [f"Per due celle uguali la frequenza a −3 dB è {it(rapp, 3)} volte quella della singola cella (capitolo {{{{cap:carico}}}}).",
                  f"{FC} della singola cella = 1000/{it(rapp, 3)} = {sig(fcs, 5)} Hz.",
                  f"R = 1/(2π {sig(fcs, 5)} · 100·10⁻⁹) = {si(r_es, OHM, 4)}; valore E96 {si(rn5, OHM)}, che dà una {FC} complessiva di {sig(fc.rc_fc(rn5, 100e-9) * rapp, 5)} Hz."]))
    # 6
    c6 = 1.0 / (2 * math.pi * 10.0 * 100e3)
    c6n = fc.arrotonda_serie(c6, "E12")
    fc6 = fc.rc_fc(100e3, c6n)
    e.append(_ex(f"Un passa-alto RC deve bloccare la continua e le derive sotto 10 Hz su un ingresso di 100 k{OHM}. Scegliere C (serie E12) e calcolare l'attenuazione a 1 Hz.",
                 [f"C = 1/(2π {FC} R) = 1/(2π · 10 · 100000) = {si(c6, 'F', 4)}; valore E12 {si(c6n, 'F')}.",
                  f"{FC} effettiva = 1/(2π · 100000 · {sig(c6n * 1e9, 3)}·10⁻⁹) = {sig(fc6, 4)} Hz.",
                  f"A 1 Hz: |H| = (f/{FC})/√(1 + (f/{FC})²) = {it(abs(fc.h_rc_hp(1.0, fc6)), 4)}, cioè {it(fc.db(fc.h_rc_hp(1.0, fc6)), 1)} dB."]))
    # 7
    c7 = 100e-9
    w0 = 2 * math.pi * 5000.0
    l7 = 1.0 / (w0 * w0 * c7)
    z0 = math.sqrt(l7 / c7)
    r7 = z0 / 10.0
    q_dcr = z0 / (r7 + 5.0)
    e.append(_ex(f"Progettare un passa-banda RLC serie con {F0} = 5 kHz, Q = 10 e C = 100 nF. Calcolare L e R, la banda e la tensione sul condensatore alla risonanza per V<sub>in</sub> = 1 V. Come cambia Q con un induttore che ha DCR = 5 {OHM}?",
                 [f"Dalla {{{{eq:f0_lc}}}}: L = 1/((2π {F0})² C) = {si(l7, 'H', 4)}.",
                  f"√(L/C) = {si(z0, OHM, 4)}; R = √(L/C)/Q = {si(r7, OHM, 4)}.",
                  f"Banda B = {F0}/Q = {sig(5000 / 10, 4)} Hz. A risonanza V<sub>C</sub> = Q V<sub>in</sub> = 10 V.",
                  f"Con il DCR: Q = √(L/C)/(R + DCR) = {sig(z0, 4)}/({sig(r7, 4)} + 5) = {it(q_dcr, 2)}; la banda sale a {sig(5000 / q_dcr, 4)} Hz."]))
    # 8
    fl, fh = 4800.0, 5300.0
    e.append(_ex("Un passa-banda ha frequenze a −3 dB di 4800 Hz e 5300 Hz. Calcolare f₀, la banda e Q.",
                 [f"La frequenza centrale è la media geometrica: {F0} = √(f<sub>L</sub> f<sub>H</sub>) = √(4800 · 5300) = {sig(math.sqrt(fl * fh), 5)} Hz.",
                  f"Banda B = f<sub>H</sub> − f<sub>L</sub> = {int(fh - fl)} Hz.",
                  f"Q = {F0}/B = {sig(math.sqrt(fl * fh), 5)}/{int(fh - fl)} = {it(math.sqrt(fl * fh) / (fh - fl), 2)}."]))
    parti.append(("Parte I — Passivi", 1, e))

    # --------------------------------------------------------------- Parte II
    e = []
    # 9
    s9 = fc.progetta_sezione_sk(2000.0, 1 / math.sqrt(2), 4.7e-9)
    q9 = 1 / math.sqrt(2)
    w9 = 2 * math.pi * 2000.0
    r1i, r2i = fc.sk_lp_unitario(2000.0, q9, s9.c1, s9.c2)
    e.append(_ex(f"Progettare un Sallen-Key Butterworth del secondo ordine a guadagno 1 con {F0} = 2 kHz e C<sub>2</sub> = 4,7 nF, usando le serie E12 (condensatori) ed E96 (resistenze).",
                 [f"Per il Butterworth Q = 1/√2. Condizione {{{{eq:c1_c2}}}}: C<sub>1</sub> ≥ 4Q²C<sub>2</sub> = 2 · 4,7 nF = {si(4 * q9 * q9 * 4.7e-9, 'F', 3)}; si sceglie C<sub>1</sub> = {si(s9.c1, 'F')} (E12).",
                  f"R<sub>1</sub> + R<sub>2</sub> = 1/(Q ω<sub>0</sub> C<sub>2</sub>) = {si(r1i + r2i, OHM, 5)}; R<sub>1</sub>R<sub>2</sub> = 1/(ω<sub>0</sub>² C<sub>1</sub> C<sub>2</sub>) = {sci(r1i * r2i, 4)} {OHM}².",
                  f"Radici: R<sub>1</sub> = {si(r1i, OHM, 5)}, R<sub>2</sub> = {si(r2i, OHM, 5)}. Valori E96: {si(s9.r1, OHM)} e {si(s9.r2, OHM)}.",
                  f"Verifica con i valori normalizzati: {F0} = {sig(s9.f0, 5)} Hz ({it((s9.f0 / 2000 - 1) * 100, 2, True)} %), Q = {sig(s9.q, 4)} ({it((s9.q / q9 - 1) * 100, 2, True)} %)."]))
    # 10
    r10, k10, rf10 = fc.sk_guadagno_componenti_uguali(1000.0, 2.0, 10e-9)
    picco10 = max(abs(fc.h2_lp(f, 1000.0, 2.0, k10)) for f in fc.griglia_log(100, 5000, 3000))
    e.append(_ex(f"Un Sallen-Key a componenti uguali ha {F0} = 1 kHz, Q = 2 e C = 10 nF. Calcolare R, K, la coppia R<sub>f</sub>, R<sub>g</sub> e il picco massimo.",
                 [f"R = 1/(2π {F0} C) = 1/(2π · 1000 · 10·10⁻⁹) = {si(r10, OHM, 4)}.",
                  f"K = 3 − 1/Q = 3 − 0,5 = {it(k10, 2)}, quindi R<sub>f</sub>/R<sub>g</sub> = K − 1 = {it(rf10, 2)}: per esempio R<sub>g</sub> = 10 k{OHM} e R<sub>f</sub> = 15 k{OHM}.",
                  f"Il guadagno di banda è K = {it(k10, 2)}, cioè {it(fc.db(k10), 1)} dB; il picco massimo vale K · Q/√(1 − 1/(4Q²)) = {it(picco10, 2)}, cioè {it(fc.db(picco10), 1)} dB."]))
    # 11
    kk = 2.8
    qa, qb = 1 / (3 - kk * 0.99), 1 / (3 - kk * 1.01)
    e.append(_ex(f"In un Sallen-Key a componenti uguali K = {it(kk, 1)} con R<sub>f</sub> e R<sub>g</sub> all'1 %. Calcolare Q nominale e l'intervallo di Q se K varia dell'1 % in più o in meno.",
                 [f"Q = 1/(3 − K) = 1/(3 − {it(kk, 1)}) = {it(1 / (3 - kk), 2)}.",
                  f"K minimo = {it(kk * 0.99, 3)} → Q = {it(qa, 2)}; K massimo = {it(kk * 1.01, 3)} → Q = {it(qb, 2)}.",
                  f"Q varia da {it((qa / (1 / (3 - kk)) - 1) * 100, 0, True)} % a {it((qb / (1 / (3 - kk)) - 1) * 100, 0, True)} %: con Q alto K è molto sensibile alla tolleranza, ed è questa la ragione per cui in quei casi si preferisce la versione a guadagno unitario."]))
    # 12
    prog12 = fc.progetta_cascata_butterworth_lp(3, 500.0, 22e-9)
    rig = []
    for i, sz in enumerate(prog12, 1):
        if isinstance(sz, fc.SezioneRc1):
            rig.append(f"Sezione {i} (primo ordine, con buffer): R = {si(sz.r, OHM)}, C = {si(sz.c, 'F')}, {F0} = {sig(sz.f0, 4)} Hz.")
        else:
            rig.append(f"Sezione {i}: Q = {it(sz.q_obiettivo, 3)}, C<sub>1</sub> = {si(sz.c1, 'F')}, C<sub>2</sub> = {si(sz.c2, 'F')}, R<sub>1</sub> = {si(sz.r1, OHM)}, R<sub>2</sub> = {si(sz.r2, OHM)} → {F0} = {sig(sz.f0, 4)} Hz, Q = {it(sz.q, 3)}.")
    a500 = fc.db(fc.risposta_cascata_reale(prog12, 500.0))
    a2k = fc.db(fc.risposta_cascata_reale(prog12, 2000.0))
    e.append(_ex("Progettare un Butterworth passa-basso del terzo ordine con f<sub>c</sub> = 500 Hz, con C base di 22 nF. Verificare l'ampiezza a 500 Hz e a 2 kHz.",
                 ["Il terzo ordine è una sezione del secondo ordine con Q = 1 (f₀ = f<sub>c</sub>) più una cella del primo ordine con f₀ = f<sub>c</sub>."] + rig
                 + [f"Risposta con i valori normalizzati: {it(a500, 2)} dB a 500 Hz e {it(a2k, 1)} dB a 2 kHz (ideale: −3,01 dB e {it(-10 * math.log10(1 + 4 ** 6), 1)} dB)."]))
    parti.append(("Parte II — Attivi", 9, e))

    # ------------------------------------------------------------- Parte III
    e = []
    # 13
    righe = []
    for n in (3, 4, 5, 6):
        righe.append(f"n = {n}: {it(-fc.db(fc.risposta_cascata(fc.butterworth(n, 1500.0), 9000.0)), 1)} dB")
    e.append(_ex("Per un ADC a 12 bit con campionamento a 10 kSPS e banda utile di 1 kHz, assumere un disturbo sinusoidale a fondo scala a 9 kHz da portare sotto 1 LSB. Trovare l'ordine Butterworth minimo con f<sub>c</sub> = 1,5 kHz.",
                 [f"Attenuazione richiesta: 20 log<sub>10</sub>(4096) = {it(20 * math.log10(4096), 1)} dB.",
                  "Attenuazione a 9 kHz con f<sub>c</sub> = 1,5 kHz (|H| = 1/√(1 + (9/1,5)<sup>2n</sup>)): " + "; ".join(righe) + ".",
                  f"Il più piccolo ordine che soddisfa la richiesta è n = 5; l'attenuazione a 1 kHz è {it(-fc.db(fc.risposta_cascata(fc.butterworth(5, 1500.0), 1000.0)), 2)} dB, accettabile in banda utile."]))
    # 14
    n14 = None
    for n in range(2, 9):
        if -fc.db(fc.risposta_cascata(fc.butterworth(n, 5000.0), 45000.0)) >= 20 * math.log10(2 ** 16):
            n14 = n
            break
    e.append(_ex("Per un ADC a 16 bit, banda utile di 5 kHz e campionamento a 50 kSPS, assumere un disturbo sinusoidale a fondo scala a 45 kHz (che si ripiega a 5 kHz) da portare sotto 1 LSB. Trovare l'ordine Butterworth minimo con f<sub>c</sub> = 5 kHz.",
                 [f"Attenuazione richiesta: 20 log<sub>10</sub>(2¹⁶) = {it(20 * math.log10(2 ** 16), 1)} dB a 45 kHz, dove f/f<sub>c</sub> = 9.",
                  f"n = {n14 - 1}: {it(-fc.db(fc.risposta_cascata(fc.butterworth(n14 - 1, 5000.0), 45000.0)), 1)} dB (insufficiente); n = {n14}: {it(-fc.db(fc.risposta_cascata(fc.butterworth(n14, 5000.0), 45000.0)), 1)} dB.",
                  f"L'ordine minimo è n = {n14}, cioè tre sezioni del secondo ordine."]))
    # 15
    rap, err, ris = _gbw_minimo(1.3066, 100e-9, 10e-9)
    e.append(_ex("Usando i risultati del capitolo {{cap:limiti-reali}}, trovare il GBW minimo per una sezione con Q = 1,3 e f<sub>0</sub> = 20 kHz in modo che il picco non superi l'ideale di più di 0,5 dB.",
                 ["L'errore dipende solo dal rapporto GBW/f₀: " + "; ".join(f"GBW/f₀ = {r}: {it(v, 2, True)} dB" for r, v in ris) + ".",
                  f"Il primo valore tabulato con errore ≤ 0,5 dB è GBW/f₀ = {rap}.",
                  f"GBW ≥ {rap} · 20 kHz = {si(rap * 20e3, 'Hz')}; con un margine di sicurezza si sceglie un operazionale da qualche MHz."]))
    # 16
    sr = 2 * math.pi * 50e3 * 1.0 * 1e-6
    e.append(_ex("Un segnale sinusoidale di 2 V<sub>pp</sub> a 50 kHz attraversa un buffer. Calcolare lo slew rate minimo.",
                 ["Ampiezza di picco V<sub>p</sub> = 1 V.", f"Pendenza massima: 2π f V<sub>p</sub> = 2π · 50000 · 1 = {it(sr, 3)} V/µs.",
                  f"Con un margine di 3 volte si cercano operazionali con SR di almeno {it(3 * sr, 2)} V/µs."]))
    # 17
    kb, temp = 1.380649e-23, 300.0
    vn = math.sqrt(4 * kb * temp * 47e3 * 20e3)
    lsb = 3.3 / 4096
    e.append(_ex("Una resistenza di 47 kΩ a 300 K lavora in una banda di 20 kHz. Calcolare il rumore termico efficace e confrontarlo con l'LSB di un ADC a 12 bit con fondo scala 3,3 V.",
                 [f"v<sub>n</sub> = √(4kTRB) = √(4 · 1,38·10⁻²³ · 300 · 47000 · 20000) = {it(vn * 1e6, 2)} µV rms.",
                  f"LSB = 3,3/4096 = {it(lsb * 1e3, 3)} mV.", f"Rapporto: {it(vn / lsb * 100, 2)} % dell'LSB: trascurabile per questo ADC, ma il rumore cresce con √R e andrebbe riconsiderato per ADC di 16 bit o più."]))
    # 18
    s = fc.progetta_cascata_butterworth_lp(2, SK_FC_E, SK_C2_E)[0]
    f0n, qn = fc.sk_f0_q_unitario(s.r1, s.r2, s.c1, s.c2)
    f0s, qs = [], []
    for a in (0.99, 1.01):
        for b in (0.99, 1.01):
            for c in (0.95, 1.05):
                for d in (0.95, 1.05):
                    fv, qv = fc.sk_f0_q_unitario(s.r1 * a, s.r2 * b, s.c1 * c, s.c2 * d)
                    f0s.append(fv)
                    qs.append(qv)
    f01, q01 = [], []
    for a in (0.99, 1.01):
        for b in (0.99, 1.01):
            for c in (0.99, 1.01):
                for d in (0.99, 1.01):
                    fv, qv = fc.sk_f0_q_unitario(s.r1 * a, s.r2 * b, s.c1 * c, s.c2 * d)
                    f01.append(fv)
                    q01.append(qv)
    e.append(_ex("Il Sallen-Key del secondo ordine del capitolo {{cap:lab-attivi}} usa resistenze all'1 % e condensatori al 5 %. Stimare il caso peggiore su f₀ e Q.",
                 ["Si calcola f₀ e Q per tutte le 16 combinazioni di estremi di R<sub>1</sub>, R<sub>2</sub>, C<sub>1</sub>, C<sub>2</sub>.",
                  f"Valori nominali: f₀ = {sig(f0n, 5)} Hz, Q = {sig(qn, 4)}.",
                  f"f₀ varia tra {sig(min(f0s), 5)} e {sig(max(f0s), 5)} Hz ({it((min(f0s) / f0n - 1) * 100, 1, True)} % / {it((max(f0s) / f0n - 1) * 100, 1, True)} %); Q varia tra {it(min(qs), 3)} e {it(max(qs), 3)} ({it((min(qs) / qn - 1) * 100, 1, True)} % / {it((max(qs) / qn - 1) * 100, 1, True)} %).",
                  f"Dominano i condensatori: con condensatori all'1 % e resistenze all'1 % gli stessi estremi danno f\u2080 tra {sig(min(f01), 5)} e {sig(max(f01), 5)} Hz ({it((min(f01) / f0n - 1) * 100, 1, True)} % / {it((max(f01) / f0n - 1) * 100, 1, True)} %) e Q tra {it(min(q01), 3)} e {it(max(q01), 3)}."]))
    # 19
    o_be = fc.sovraelongazione_h2(1 / math.sqrt(3)) * 100
    o_bw = fc.sovraelongazione_h2(1 / math.sqrt(2)) * 100
    o_ch = fc.sovraelongazione_h2(fc.chebyshev(2, 1.0, 1.0)[0].q) * 100
    e.append(_ex("Un segnale di vibrazione con impulsi brevi deve essere filtrato a 500 Hz senza distorcere la forma degli impulsi e con una sovraelongazione inferiore all'1 %. Scegliere la famiglia di filtri del secondo ordine.",
                 [f"Sovraelongazione al gradino con Q: exp(−πζ/√(1 − ζ²)) con ζ = 1/(2Q).",
                  f"Bessel (Q = 0,577): {it(o_be, 2)} %; Butterworth (Q = 0,707): {it(o_bw, 1)} %; Chebyshev 1 dB (Q = {it(fc.chebyshev(2, 1.0, 1.0)[0].q, 3)}): {it(o_ch, 1)} %.",
                  "Solo il Bessel rispetta il limite dell'1 %. In più ha il ritardo di gruppo più costante; il prezzo è una pendenza minore in banda oscura."]))
    # 20
    fb20, fs20, bit20 = 2000.0, 20000.0, 10
    need = 20 * math.log10(2 ** bit20)
    f_al = fs20 - fb20
    n20 = None
    for n in range(2, 9):
        if -fc.db(fc.risposta_cascata(fc.butterworth(n, 3000.0), f_al)) >= need:
            n20 = n
            break
    prog20 = fc.progetta_cascata_butterworth_lp(n20, 3000.0, 4.7e-9)
    righe = []
    for i, sz in enumerate(prog20, 1):
        if isinstance(sz, fc.SezioneRc1):
            righe.append(f"sezione {i}: R = {si(sz.r, OHM)}, C = {si(sz.c, 'F')}")
        else:
            righe.append(f"sezione {i} (Q = {it(sz.q_obiettivo, 3)}): R<sub>1</sub> = {si(sz.r1, OHM)}, R<sub>2</sub> = {si(sz.r2, OHM)}, C<sub>1</sub> = {si(sz.c1, 'F')}, C<sub>2</sub> = {si(sz.c2, 'F')}")
    a2 = -fc.db(fc.risposta_cascata_reale(prog20, 2000.0))
    a18 = -fc.db(fc.risposta_cascata_reale(prog20, f_al))
    e.append(_ex("Progettare, con la procedura del capitolo {{cap:progetto}}, un filtro anti-aliasing per un ADC a 10 bit con campionamento a 20 kSPS e banda utile di 2 kHz. Assumere un disturbo sinusoidale a fondo scala a 18 kHz da portare sotto 1 LSB; attenuazione in banda utile ≤ 0,5 dB.",
                 [f"Specifica: attenuazione ≥ 20 log<sub>10</sub>(2¹⁰) = {it(need, 1)} dB a f<sub>s</sub> − f<sub>b</sub> = 18 kHz e ≤ 0,5 dB a 2 kHz.",
                  f"Si prova un Butterworth con f<sub>c</sub> = 3 kHz: n = {n20 - 1} dà {it(-fc.db(fc.risposta_cascata(fc.butterworth(n20 - 1, 3000.0), f_al)), 1)} dB a 18 kHz (insufficiente), n = {n20} dà {it(-fc.db(fc.risposta_cascata(fc.butterworth(n20, 3000.0), f_al)), 1)} dB; a 2 kHz {it(-fc.db(fc.risposta_cascata(fc.butterworth(n20, 3000.0), 2000.0)), 2)} dB.",
                  f"Con C<sub>2</sub> = 4,7 nF (E12) e resistenze E96: " + "; ".join(righe) + ".",
                  f"Verifica con i valori normalizzati: {it(a2, 2)} dB a 2 kHz e {it(a18, 1)} dB a 18 kHz. Resta da misurare con la scheda del capitolo {{{{cap:lab-attivi}}}}."]))
    # famiglie: ordine minimo, Bessel, Chebyshev
    nb = fc.ordine_minimo("butterworth", 30, 3.0)
    nc = fc.ordine_minimo("chebyshev", 30, 3.0, ripple_db=1.0)
    ne = fc.ordine_minimo("bessel", 30, 3.0, n_max=12)
    e.append(_ex("Un filtro passa-basso deve attenuare almeno 30 dB a 3 volte la frequenza di taglio. Trovare l'ordine minimo per Butterworth, Chebyshev da 1 dB e Bessel, e il numero di operazionali Sallen-Key necessari.",
                 ["Si calcola l'attenuazione a x = 3 per ogni ordine. Butterworth: 10 log<sub>10</sub>(1 + 3<sup>2n</sup>): "
                  + "; ".join(f"n = {n}: {it(fc.attenuazione_db(fc.butterworth(n, 1.0), 3.0), 1)} dB" for n in range(2, 6)) + ".",
                  f"Il Butterworth richiede n = {nb}; il Chebyshev da 1 dB (attenuazione a 3 f<sub>c</sub> per n = 3: {it(fc.attenuazione_db(fc.chebyshev(3, 1.0, 1.0), 3.0), 1)} dB) richiede n = {nc}; "
                  f"il Bessel richiede n = {ne} (a 3 f<sub>c</sub> con n = {ne - 1}: {it(fc.attenuazione_db(fc.bessel(ne - 1, 1.0), 3.0), 1)} dB).",
                  f"Un operazionale realizza due poli: Butterworth {(nb + 1) // 2}, Chebyshev {(nc + 1) // 2}, Bessel {(ne + 1) // 2} (con una cella RC aggiuntiva per n dispari)."]))
    be4 = sorted(fc.bessel(4, 2000.0), key=lambda s: s.q)
    e.append(_ex("Progettare le sezioni teoriche di un Bessel del quarto ordine con frequenza di taglio a \u22123 dB di 2 kHz, usando la tabella dei coefficienti (f<sub>0</sub>/f<sub>c</sub> = 1,430 e 1,603; Q = 0,522 e 0,806). Quali valori minimi di C<sub>1</sub> servono se C<sub>2</sub> = 10 nF?",
                 [f"f<sub>0</sub> = (f<sub>0</sub>/f<sub>c</sub>) \u00b7 f<sub>c</sub>: {sig(be4[0].f0, 5)} Hz e {sig(be4[1].f0, 5)} Hz.",
                  f"Condizione C<sub>1</sub> \u2265 4Q\u00b2C<sub>2</sub>: sezione 1 (Q = {it(be4[0].q, 3)}): {si(4 * be4[0].q ** 2 * 10e-9, 'F', 3)}; sezione 2 (Q = {it(be4[1].q, 3)}): {si(4 * be4[1].q ** 2 * 10e-9, 'F', 3)}.",
                  "Si scelgono i valori E12 maggiori di quei minimi e si calcolano le resistenze come nel capitolo {{cap:sk-lp}}."]))
    eps = math.sqrt(10 ** 0.1 - 1)
    ch = fc.chebyshev(4, 1.0, 1.0)
    e.append(_ex("Un Chebyshev del quarto ordine con ripple di 1 dB ha il bordo della banda con ripple a 1 kHz. Calcolare \u03b5, la frequenza a \u22123 dB, il Q massimo e dire in quanti punti la curva tocca i bordi della fascia di ripple.",
                 [f"\u03b5 = \u221a(10<sup>R/10</sup> \u2212 1) = \u221a(10<sup>0,1</sup> \u2212 1) = {it(eps, 4)}.",
                  f"f<sub>\u22123 dB</sub> = f<sub>c</sub> \u00b7 cosh(acosh(1/\u03b5)/n) = 1000 \u00b7 cosh(acosh({it(1 / eps, 3)})/4) = {sig(fc.chebyshev_f3db_su_fc(4, 1.0) * 1000, 4)} Hz.",
                  f"Le due sezioni hanno Q = {it(min(s.q for s in ch), 3)} e Q = {it(max(s.q for s in ch), 3)}: il Q massimo è {it(max(s.q for s in ch), 2)}.",
                  "Punti di contatto con i bordi della fascia: n + 1 = 5, cioè due oscillazioni complete."]))
    parti.append(("Sintesi", 13, e))

    out = []
    contatore = 1
    for titolo, _, voci in parti:
        out.append(f"<h3>{titolo}</h3>")
        out.append(f'<ol class="ex" start="{contatore}">' + "".join(voci) + "</ol>")
        contatore += len(voci)
    return "\n".join(out)


SK_FC_E, SK_C2_E = 1000.0, 10e-9
