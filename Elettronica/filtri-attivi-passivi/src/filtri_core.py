"""Logica di calcolo per filtri passivi RC/RLC e attivi Sallen-Key (solo libreria standard).

Convenzioni: frequenze in Hz, resistenze in ohm, capacità in farad, induttanze in henry.
Le funzioni di risposta restituiscono numeri complessi H(jf); modulo in dB e fase in gradi
si ottengono con `db()` e `fase_gradi()`.
"""
import cmath
import math
from dataclasses import dataclass
from functools import lru_cache

from serie import SERIE


# ---------------------------------------------------------------------------
# Utilità
# ---------------------------------------------------------------------------

def db(h):
    """Modulo in dB di una risposta complessa."""
    return 20.0 * math.log10(abs(h))


def fase_gradi(h):
    """Fase in gradi, nell'intervallo (-180, 180]."""
    return math.degrees(cmath.phase(h))


def arrotonda_serie(valore, serie="E96"):
    """Valore normalizzato più vicino (in scala logaritmica) al valore richiesto."""
    if valore <= 0:
        raise ValueError("il valore deve essere positivo")
    mantisse = SERIE[serie]
    decade = math.floor(math.log10(valore))
    candidati = [m * 10.0 ** d for d in (decade - 1, decade, decade + 1) for m in mantisse]
    return min(candidati, key=lambda c: abs(math.log(c / valore)))


def arrotonda_serie_per_eccesso(valore, serie="E12"):
    """Primo valore normalizzato maggiore o uguale a `valore` (tolleranza numerica 1e-9)."""
    mantisse = SERIE[serie]
    decade = math.floor(math.log10(valore))
    candidati = sorted(m * 10.0 ** d for d in (decade - 1, decade, decade + 1) for m in mantisse)
    for c in candidati:
        if c >= valore * (1 - 1e-9):
            return c
    raise ValueError("nessun valore normalizzato trovato")


# ---------------------------------------------------------------------------
# Filtri passivi
# ---------------------------------------------------------------------------

def rc_fc(r, c):
    """Frequenza di taglio a -3 dB di un RC del primo ordine."""
    return 1.0 / (2.0 * math.pi * r * c)


def h_rc_lp(f, fc):
    """Passa-basso del primo ordine: H = 1 / (1 + jf/fc)."""
    return 1.0 / (1.0 + 1j * f / fc)


def h_rc_hp(f, fc):
    """Passa-alto del primo ordine: H = (jf/fc) / (1 + jf/fc)."""
    x = 1j * f / fc
    return x / (1.0 + x)


def h_rc_lp_caricato(f, r, c, r_carico):
    """RC passa-basso con carico resistivo in parallelo al condensatore (equivalente di Thevenin)."""
    r_th = r * r_carico / (r + r_carico)
    guadagno_dc = r_carico / (r + r_carico)
    return guadagno_dc / (1.0 + 1j * f * 2.0 * math.pi * r_th * c)


def h_rc_lp_doppio(f, r1, c1, r2, c2):
    """Due celle RC passa-basso collegate direttamente (la seconda carica la prima).

    H = 1 / (1 + s(R1C1 + R2C2 + R1C2) + s^2 R1C1R2C2): non è il prodotto di due celle isolate.
    """
    s = 2j * math.pi * f
    return 1.0 / (1.0 + s * (r1 * c1 + r2 * c2 + r1 * c2) + s * s * r1 * c1 * r2 * c2)


@dataclass(frozen=True)
class RlcSerie:
    """Risonatore RLC serie con uscita sulla resistenza (passa-banda)."""
    r: float
    l: float
    c: float

    @property
    def f0(self):
        return 1.0 / (2.0 * math.pi * math.sqrt(self.l * self.c))

    @property
    def q(self):
        return math.sqrt(self.l / self.c) / self.r

    @property
    def banda(self):
        """Larghezza di banda a -3 dB."""
        return self.f0 / self.q

    def h(self, f):
        return h2_bp(f, self.f0, self.q)


def rlc_q_con_resistenza_induttore(r, l, c, r_dc_induttore):
    """Q effettivo se l'induttore ha una resistenza serie non nulla."""
    return math.sqrt(l / c) / (r + r_dc_induttore)


# ---------------------------------------------------------------------------
# Sezioni del secondo ordine (forma canonica) e cascate
# ---------------------------------------------------------------------------

def h2_lp(f, f0, q, k=1.0):
    """Passa-basso: H = K / (1 - x^2 + jx/Q), x = f/f0."""
    x = f / f0
    return k / (1.0 - x * x + 1j * x / q)


def h2_hp(f, f0, q, k=1.0):
    """Passa-alto: H = -K x^2 / (1 - x^2 + jx/Q); per x grande tende a +K."""
    x = f / f0
    return -k * x * x / (1.0 - x * x + 1j * x / q)


def h2_bp(f, f0, q):
    """Passa-banda a guadagno unitario in f0: H = (jx/Q) / (1 - x^2 + jx/Q)."""
    x = f / f0
    return (1j * x / q) / (1.0 - x * x + 1j * x / q)


def picco_h2_lp(q):
    """Guadagno massimo di un passa-basso del secondo ordine a guadagno DC unitario.

    Esiste un picco solo per Q > 1/sqrt(2); vale Q / sqrt(1 - 1/(4Q^2)).
    """
    if q <= 1.0 / math.sqrt(2.0):
        return 1.0
    return q / math.sqrt(1.0 - 1.0 / (4.0 * q * q))


@dataclass(frozen=True)
class Sezione:
    """Sezione di un filtro: ordine 1 (solo f0) oppure ordine 2 (f0 e Q)."""
    ordine: int
    f0: float
    q: float = 0.0

    def h(self, f, passa="lp"):
        # `passa` può essere un valore GBW (numero) o None quando la sezione è chiamata da funzioni di cascata
        # generiche: in quel caso si intende il passa-basso
        lp = passa == "lp" or not isinstance(passa, str)
        if self.ordine == 1:
            return h_rc_lp(f, self.f0) if lp else h_rc_hp(f, self.f0)
        return h2_lp(f, self.f0, self.q) if lp else h2_hp(f, self.f0, self.q)


def risposta_cascata(sezioni, f, passa="lp"):
    """Prodotto delle risposte di sezioni isolate (valido se separate da buffer)."""
    h = 1.0 + 0j
    for s in sezioni:
        h *= s.h(f, passa)
    return h


def butterworth(n, fc=1.0):
    """Sezioni di un Butterworth di ordine n con frequenza di taglio a -3 dB `fc`."""
    sezioni = []
    for k in range(1, n // 2 + 1):
        q = 1.0 / (2.0 * math.sin((2 * k - 1) * math.pi / (2 * n)))
        sezioni.append(Sezione(2, fc, q))
    if n % 2:
        sezioni.append(Sezione(1, fc))
    return sezioni


def chebyshev(n, ripple_db, fc=1.0):
    """Sezioni di un Chebyshev di tipo I; `fc` è il limite della banda con ripple.

    Ogni sezione ha guadagno DC unitario: per n pari il ripple si legge da 0 a +ripple_db.
    """
    eps = math.sqrt(10.0 ** (ripple_db / 10.0) - 1.0)
    a = math.asinh(1.0 / eps) / n
    sezioni = []
    for k in range(1, n // 2 + 1):
        th = (2 * k - 1) * math.pi / (2 * n)
        sigma = math.sinh(a) * math.sin(th)
        omega = math.cosh(a) * math.cos(th)
        f0 = math.hypot(sigma, omega)
        sezioni.append(Sezione(2, f0 * fc, f0 / (2.0 * sigma)))
    if n % 2:
        sezioni.append(Sezione(1, math.sinh(a) * fc))
    return sezioni


def bessel2(fc=1.0):
    """Bessel del secondo ordine con taglio a -3 dB in `fc`.

    Parte da H = 3 / (s^2 + 3s + 3) (ritardo di gruppo unitario a bassa frequenza) e ricava
    per bisezione la pulsazione a -3 dB per riscalare f0.
    """
    def mod2(w):
        s = 1j * w
        return abs(3.0 / (s * s + 3.0 * s + 3.0)) ** 2

    lo, hi = 0.0, 10.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if mod2(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    w3 = 0.5 * (lo + hi)
    return Sezione(2, math.sqrt(3.0) / w3 * fc, 1.0 / math.sqrt(3.0))


def coefficienti_bessel(n):
    """Coefficienti a_k (k = 0..n) del polinomio di Bessel inverso: a_k = (2n-k)! / (2^(n-k) k! (n-k)!)."""
    return [math.factorial(2 * n - k) // (2 ** (n - k) * math.factorial(k) * math.factorial(n - k)) for k in range(n + 1)]


def _radici_polinomio(coeff_crescenti, iterazioni=500):
    """Radici complesse con il metodo di Durand-Kerner; coefficienti dal termine noto al grado massimo."""
    grado = len(coeff_crescenti) - 1
    c = [a / coeff_crescenti[-1] for a in coeff_crescenti]  # monico

    def valuta(z):
        v = 0j
        for a in reversed(c):
            v = v * z + a
        return v

    radici = [(0.4 + 0.9j) ** k for k in range(grado)]
    for _ in range(iterazioni):
        spostamento = 0.0
        for i in range(grado):
            den = 1 + 0j
            for j in range(grado):
                if j != i:
                    den *= radici[i] - radici[j]
            delta = valuta(radici[i]) / den
            radici[i] -= delta
            spostamento = max(spostamento, abs(delta))
        if spostamento < 1e-14:
            break
    return radici


def bessel(n, fc=1.0):
    """Sezioni di un Bessel passa-basso di ordine n con taglio a -3 dB in `fc` (guadagno DC unitario).

    I poli sono le radici del polinomio di Bessel inverso di grado n; la scala di frequenza è scelta in modo
    che |H| valga 1/sqrt(2) a fc. Restituisce le sezioni del secondo ordine (f0 crescente) più, per n dispari,
    la cella del primo ordine.
    """
    coeff = [float(a) for a in coefficienti_bessel(n)]
    radici = _radici_polinomio(coeff)

    def mod2(w):
        s = 1j * w
        v = 0j
        for a in reversed(coeff):
            v = v * s + a
        return (coeff[0] / abs(v)) ** 2

    lo, hi = 0.0, 20.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if mod2(mid) > 0.5:
            lo = mid
        else:
            hi = mid
    w3 = 0.5 * (lo + hi)
    sezioni = []
    for r in sorted([r for r in radici if r.imag > 1e-9], key=abs):
        sezioni.append(Sezione(2, abs(r) / w3 * fc, abs(r) / (-2.0 * r.real)))
    if n % 2:
        reale = [r for r in radici if abs(r.imag) <= 1e-9][0]
        sezioni.append(Sezione(1, abs(reale.real) / w3 * fc))
    return sezioni


def f_3db(sezioni, f_max=100.0, riferimento="dc"):
    """Frequenza a cui |H| scende di 3 dB (prima discesa sotto soglia, per bisezione).

    riferimento="dc": rispetto al guadagno in continua; "picco": rispetto al massimo in banda passante
    (convenzione dei testi per il Chebyshev di ordine pari, dove il massimo supera il valore in continua).
    """
    rif = 1.0
    if riferimento == "picco":
        rif = max(abs(risposta_cascata(sezioni, f)) for f in griglia_log(1e-3, f_max, 3000))
    soglia = rif / math.sqrt(2)
    f, rapporto = 1e-3, (f_max / 1e-3) ** (1.0 / 6000)
    trovato = None
    for _ in range(6000):
        if abs(risposta_cascata(sezioni, f)) < soglia:
            trovato = f
            break
        f *= rapporto
    if trovato is None:
        raise ValueError("nessuna discesa a -3 dB nell'intervallo")
    lo, hi = trovato / rapporto, trovato
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if abs(risposta_cascata(sezioni, m)) > soglia:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def chebyshev_f3db_su_fc(n, ripple_db):
    """Rapporto tra la frequenza a -3 dB e il limite della banda con ripple di un Chebyshev di tipo I."""
    eps = math.sqrt(10.0 ** (ripple_db / 10.0) - 1.0)
    return math.cosh(math.acosh(1.0 / eps) / n)


def polinomio_chebyshev(n, x):
    """Polinomio di Chebyshev T_n(x) con la ricorrenza T_{k+1} = 2 x T_k - T_{k-1}."""
    t0, t1 = 1.0, x
    if n == 0:
        return t0
    for _ in range(n - 1):
        t0, t1 = t1, 2.0 * x * t1 - t0
    return t1


@lru_cache(maxsize=None)
def _sezioni_famiglia_cache(famiglia, n, fc, ripple_db):
    if famiglia == "butterworth":
        return tuple(butterworth(n, fc))
    if famiglia == "chebyshev":
        return tuple(chebyshev(n, ripple_db, fc))
    if famiglia == "bessel":
        return tuple(bessel(n, fc))
    raise ValueError(f"famiglia sconosciuta: {famiglia}")


def sezioni_famiglia(famiglia, n, fc=1.0, ripple_db=1.0):
    """Sezioni teoriche di 'butterworth', 'chebyshev' o 'bessel' di ordine n (con cache)."""
    return list(_sezioni_famiglia_cache(famiglia, n, fc, ripple_db))


def attenuazione_db(sezioni, f):
    """Attenuazione (positiva) in dB rispetto al guadagno in continua."""
    return -db(risposta_cascata(sezioni, f))


def ordine_minimo(famiglia, att_db, rapporto_f, ripple_db=1.0, n_max=10):
    """Ordine minimo per attenuare almeno `att_db` a `rapporto_f` volte fc (fc = bordo della banda passante).

    Per Butterworth e Bessel fc è la frequenza a -3 dB; per Chebyshev il limite della banda con ripple.
    Restituisce None se n_max non basta.
    """
    for n in range(1, n_max + 1):
        if attenuazione_db(sezioni_famiglia(famiglia, n, 1.0, ripple_db), rapporto_f) >= att_db:
            return n
    return None


def frequenza_attenuazione(sezioni, att_db, f_max=200.0):
    """Frequenza oltre la quale l'attenuazione supera `att_db` (bisezione; discesa monotona oltre f_3db)."""
    lo, hi = f_3db(sezioni), f_max
    if attenuazione_db(sezioni, hi) < att_db:
        raise ValueError("attenuazione non raggiunta nell'intervallo")
    for _ in range(100):
        m = 0.5 * (lo + hi)
        if attenuazione_db(sezioni, m) < att_db:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def progetta_cascata_lp(sezioni_teoriche, c_base, serie_r="E96", serie_c="E12"):
    """Progetto a Sallen-Key unitari in cascata per qualsiasi lista di sezioni teoriche (qualsiasi famiglia)."""
    sezioni = []
    for s in sezioni_teoriche:
        if s.ordine == 2:
            sezioni.append(progetta_sezione_sk(s.f0, s.q, c_base, serie_r, serie_c))
        else:
            r = arrotonda_serie(1.0 / (2.0 * math.pi * s.f0 * c_base), serie_r)
            sezioni.append(SezioneRc1(s.f0, r, c_base))
    return sezioni


# ---------------------------------------------------------------------------
# Sallen-Key: modello nodale e progetto
# ---------------------------------------------------------------------------

def _risolvi_2x2(a11, a12, a21, a22, b1, b2):
    """Sistema 2x2 complesso con la regola di Cramer."""
    det = a11 * a22 - a12 * a21
    return (b1 * a22 - a12 * b2) / det, (a11 * b2 - b1 * a21) / det


def guadagno_reale(k, f, gbw=None):
    """Guadagno ad anello chiuso di un amplificatore non invertente con un solo polo.

    G = K / (1 + jK f/GBW); con gbw=None l'amplificatore è ideale e G = K.
    """
    if gbw is None:
        return complex(k)
    return k / (1.0 + 1j * k * f / gbw)


def h_sk_lp(f, r1, r2, c1, c2, k=1.0, gbw=None):
    """Sallen-Key passa-basso, soluzione nodale esatta.

    R1 collega l'ingresso al nodo Va, R2 collega Va all'ingresso non invertente, C1 (reazione)
    collega Va all'uscita, C2 collega l'ingresso non invertente a massa.
    """
    s = 2j * math.pi * f
    y1, y2 = 1.0 / r1, 1.0 / r2
    g = guadagno_reale(k, f, gbw)
    va, vp = _risolvi_2x2(y1 + y2 + s * c1, -(y2 + s * c1 * g),
                          -y2, y2 + s * c2,
                          y1, 0.0)
    return g * vp


def h_sk_hp(f, r1, r2, c1, c2, k=1.0, gbw=None):
    """Sallen-Key passa-alto, soluzione nodale esatta.

    C1 collega l'ingresso al nodo Va, C2 collega Va all'ingresso non invertente, R1 (reazione)
    collega Va all'uscita, R2 collega l'ingresso non invertente a massa.
    """
    s = 2j * math.pi * f
    y1, y2 = 1.0 / r1, 1.0 / r2
    g = guadagno_reale(k, f, gbw)
    va, vp = _risolvi_2x2(s * c1 + s * c2 + y1, -(s * c2 + y1 * g),
                          -s * c2, s * c2 + y2,
                          s * c1, 0.0)
    return g * vp


def sk_lp_unitario(f0, q, c1, c2):
    """Resistenze R1, R2 di un Sallen-Key passa-basso a guadagno 1 per C1, C2 assegnati.

    R1 + R2 = 1 / (Q w0 C2),  R1 R2 = 1 / (w0^2 C1 C2); servono C1 >= 4 Q^2 C2.
    f0 e Q sono simmetrici in R1 e R2: restituisce la coppia con R1 >= R2.
    """
    if c1 < 4.0 * q * q * c2 * (1 - 1e-9):
        raise ValueError(f"C1 deve essere almeno 4*Q^2*C2 = {4 * q * q * c2:.4g} F")
    w0 = 2.0 * math.pi * f0
    somma = 1.0 / (q * w0 * c2)
    prodotto = 1.0 / (w0 * w0 * c1 * c2)
    radice = math.sqrt(max(somma * somma - 4.0 * prodotto, 0.0))
    return (somma + radice) / 2.0, (somma - radice) / 2.0


def sk_f0_q_unitario(r1, r2, c1, c2):
    """f0 e Q effettivi di un Sallen-Key passa-basso a guadagno 1."""
    w0 = 1.0 / math.sqrt(r1 * r2 * c1 * c2)
    q = math.sqrt(r1 * r2 * c1 * c2) / (c2 * (r1 + r2))
    return w0 / (2.0 * math.pi), q


def sk_guadagno_componenti_uguali(f0, q, c):
    """Sallen-Key a componenti uguali (R1=R2=R, C1=C2=C) per LP o HP.

    Restituisce (R, K, Rf/Rg): f0 = 1/(2 pi R C), K = 3 - 1/Q, Rf/Rg = K - 1.
    Il guadagno di banda passante è K = 3 - 1/Q e un amplificatore non invertente richiede
    K >= 1, cioè Q >= 1/2; per Q che tende a infinito K tende a 3 (oscillazione).
    """
    if q < 0.5:
        raise ValueError("a componenti uguali serve Q >= 1/2 (K >= 1)")
    k = 3.0 - 1.0 / q
    r = 1.0 / (2.0 * math.pi * f0 * c)
    return r, k, k - 1.0


@dataclass(frozen=True)
class SezioneSkReale:
    """Sezione Sallen-Key a guadagno 1 con componenti già normalizzati."""
    f0_obiettivo: float
    q_obiettivo: float
    r1: float
    r2: float
    c1: float
    c2: float

    @property
    def f0(self):
        return sk_f0_q_unitario(self.r1, self.r2, self.c1, self.c2)[0]

    @property
    def q(self):
        return sk_f0_q_unitario(self.r1, self.r2, self.c1, self.c2)[1]

    def h(self, f, gbw=None):
        return h_sk_lp(f, self.r1, self.r2, self.c1, self.c2, 1.0, gbw)


def progetta_sezione_sk(f0, q, c2, serie_r="E96", serie_c="E12"):
    """Sezione SK unitaria: C2 assegnato, C1 = primo valore di serie >= 4 Q^2 C2, R poi in serie."""
    c1 = arrotonda_serie_per_eccesso(4.0 * q * q * c2, serie_c)
    r1, r2 = sk_lp_unitario(f0, q, c1, c2)
    return SezioneSkReale(f0, q, arrotonda_serie(r1, serie_r), arrotonda_serie(r2, serie_r), c1, c2)


@dataclass(frozen=True)
class SezioneRc1:
    """Cella RC del primo ordine con buffer (per ordini dispari)."""
    f0_obiettivo: float
    r: float
    c: float

    @property
    def f0(self):
        return rc_fc(self.r, self.c)

    def h(self, f, gbw=None):
        return h_rc_lp(f, self.f0)


def progetta_cascata_butterworth_lp(n, fc, c_base, serie_r="E96", serie_c="E12"):
    """Progetto completo di un Butterworth passa-basso a Sallen-Key unitari in cascata.

    `c_base` è il C2 di ogni sezione del secondo ordine e il C della cella del primo ordine.
    Restituisce la lista delle sezioni con componenti normalizzati.
    """
    sezioni = []
    for s in butterworth(n, fc):
        if s.ordine == 2:
            sezioni.append(progetta_sezione_sk(s.f0, s.q, c_base, serie_r, serie_c))
        else:
            r = arrotonda_serie(1.0 / (2.0 * math.pi * s.f0 * c_base), serie_r)
            sezioni.append(SezioneRc1(s.f0, r, c_base))
    return sezioni


def risposta_cascata_reale(sezioni, f, gbw=None):
    """Prodotto delle risposte delle sezioni reali (buffer ideali o con GBW finito)."""
    h = 1.0 + 0j
    for s in sezioni:
        h *= s.h(f, gbw)
    return h


def sovraelongazione_h2(q):
    """Sovraelongazione relativa alla risposta al gradino di un passa-basso del secondo ordine.

    Con zeta = 1/(2Q): exp(-pi zeta / sqrt(1 - zeta^2)) per zeta < 1, zero altrimenti.
    """
    zeta = 1.0 / (2.0 * q)
    if zeta >= 1.0:
        return 0.0
    return math.exp(-math.pi * zeta / math.sqrt(1.0 - zeta * zeta))


def poli_sezione(sezione):
    """Poli di una sezione passa-basso come coppie (sigma, omega) in unità di Hz (parte reale e immaginaria).

    Sezione del primo ordine: un polo reale in -f0. Secondo ordine con Q > 1/2: coppia complessa
    coniugata sigma = -f0/(2Q), omega = +-f0 sqrt(1 - 1/(4Q^2)); si restituisce quello con omega > 0.
    """
    if sezione.ordine == 1:
        return [(-sezione.f0, 0.0)]
    if sezione.q <= 0.5:
        raise ValueError("per Q <= 1/2 i poli sono reali: non gestiti")
    sigma = -sezione.f0 / (2.0 * sezione.q)
    omega = sezione.f0 * math.sqrt(1.0 - 1.0 / (4.0 * sezione.q * sezione.q))
    return [(sigma, omega), (sigma, -omega)]


def ritardo_gruppo(sezioni, f, passo_rel=1e-4):
    """Ritardo di gruppo (secondi) di una cascata passa-basso: -d(fase)/d(omega), per differenza centrata."""
    df = f * passo_rel
    fase_p = math.radians(fase_cascata_gradi(sezioni, f + df))
    fase_m = math.radians(fase_cascata_gradi(sezioni, f - df))
    return -(fase_p - fase_m) / (2.0 * math.pi * 2.0 * df)


def risposta_ingresso(sezioni, u_fun, t_max, punti=400, passi_per_punto=20):
    """Risposta di una cascata passa-basso a un ingresso u(t) qualsiasi, con Runge-Kutta del 4o ordine.

    Ogni sezione è descritta da x' = w0 (u - x) (primo ordine) oppure da
    x1' = x2, x2' = w0^2 (u - x1) - (w0/Q) x2 (secondo ordine); l'uscita è x1 e alimenta la sezione
    successiva. Restituisce [(t, y)] con t da 0 a t_max.
    """
    indici = []
    n = 0
    for s in sezioni:
        indici.append(n)
        n += s.ordine

    def derivata(x, u):
        d = [0.0] * n
        ingresso = u
        for s, i in zip(sezioni, indici):
            w0 = 2.0 * math.pi * s.f0
            if s.ordine == 1:
                d[i] = w0 * (ingresso - x[i])
                ingresso = x[i]
            else:
                d[i] = x[i + 1]
                d[i + 1] = w0 * w0 * (ingresso - x[i]) - (w0 / s.q) * x[i + 1]
                ingresso = x[i]
        return d

    dt = t_max / (punti * passi_per_punto)
    x = [0.0] * n
    uscita = [(0.0, 0.0)]
    t = 0.0
    for _ in range(punti):
        for _ in range(passi_per_punto):
            u0, um, u1 = u_fun(t), u_fun(t + 0.5 * dt), u_fun(t + dt)
            k1 = derivata(x, u0)
            k2 = derivata([a + 0.5 * dt * b for a, b in zip(x, k1)], um)
            k3 = derivata([a + 0.5 * dt * b for a, b in zip(x, k2)], um)
            k4 = derivata([a + dt * b for a, b in zip(x, k3)], u1)
            x = [a + dt * (b + 2 * c + 2 * d_ + e) / 6.0 for a, b, c, d_, e in zip(x, k1, k2, k3, k4)]
            t += dt
        uscita.append((t, x[indici[-1]]))
    return uscita


def risposta_gradino(sezioni, t_max, punti=400, passi_per_punto=20):
    """Risposta al gradino unitario di una cascata passa-basso (caso particolare di risposta_ingresso)."""
    return risposta_ingresso(sezioni, lambda _t: 1.0, t_max, punti, passi_per_punto)


def fase_cascata_gradi(sezioni, f, gbw=None):
    """Fase continua (non ridotta a (-180, 180]) di una cascata: somma delle fasi di sezione."""
    return sum(fase_gradi(s.h(f, gbw)) for s in sezioni)


def picco_e_frequenza(funzione, f_min, f_max, punti=4000):
    """Massimo del modulo di `funzione(f)` su una griglia logaritmica: (|H|max, f)."""
    migliore = (0.0, f_min)
    rapporto = (f_max / f_min) ** (1.0 / (punti - 1))
    f = f_min
    for _ in range(punti):
        m = abs(funzione(f))
        if m > migliore[0]:
            migliore = (m, f)
        f *= rapporto
    return migliore


def griglia_log(f_min, f_max, punti):
    """Frequenze equispaziate in scala logaritmica, estremi inclusi."""
    rapporto = (f_max / f_min) ** (1.0 / (punti - 1))
    return [f_min * rapporto ** i for i in range(punti)]
