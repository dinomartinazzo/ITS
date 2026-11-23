"""Formattazione di numeri e tabelle HTML (virgola decimale, prefissi SI)."""
import math


# ---------------------------------------------------------------------------------------------

def it(x, dec=2, segno=False):
    """Numero con virgola decimale e segno meno tipografico."""
    s = f"{x:+.{dec}f}" if segno else f"{x:.{dec}f}"
    if float(s) == 0:  # evita «−0,00»: scarti sotto la precisione mostrata valgono zero
        s = s.lstrip("+-")
    return s.replace("-", "−").replace(".", ",")


def sig(x, cifre=4):
    """Numero con cifre significative, virgola decimale e segno meno tipografico."""
    return f"{x:.{cifre}g}".replace("-", "−").replace(".", ",")


def sci(x, cifre=4):
    """Notazione scientifica con apice: 1,151\u00b710\u2078."""
    m, e = f"{x:.{cifre - 1}e}".split("e")
    sup = str.maketrans("-0123456789", "\u207b\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")
    return f"{m.replace('.', ',')}\u00b710{str(int(e)).translate(sup)}"


def si(valore, unita, cifre=3):
    for soglia, pre in ((1e6, "M"), (1e3, "k"), (1.0, ""), (1e-3, "m"), (1e-6, "µ"), (1e-9, "n"), (1e-12, "p")):
        if abs(valore) >= soglia * 0.9995:
            return sig(valore / soglia, cifre) + " " + pre + unita
    return sig(valore, cifre) + " " + unita


def riga(celle, classi=None):
    classi = classi or [""] * len(celle)
    return "<tr>" + "".join(f'<td class="{c}">{v}</td>' if c else f"<td>{v}</td>" for v, c in zip(celle, classi)) + "</tr>"


def tabella(intest, righe, classi_intest=None, larga=False):
    classi_intest = classi_intest or [""] * len(intest)
    th = "".join(f'<th class="{c}">{h}</th>' if c else f"<th>{h}</th>" for h, c in zip(intest, classi_intest))
    corpo = "\n".join(righe)
    return (f'<div class="tbl{" wide" if larga else ""}"><table>\n<thead><tr>{th}</tr></thead>\n'
            f"<tbody>\n{corpo}\n</tbody></table></div>")


