"""Interfaccia a riga di comando per il progetto e l'analisi dei filtri.

Esempi (dalla radice del progetto):
    python3 src/filtri_cli.py rc --r 1.6k --c 100n
    python3 src/filtri_cli.py sk --f0 1k --q 0.7071 --c2 10n
    python3 src/filtri_cli.py butter --n 4 --fc 1k --c 10n
"""
import argparse
import math
import sys

import filtri_core as fc

# Prefissi SI ammessi nei valori da riga di comando
_PREFISSI = {"p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3, "k": 1e3, "M": 1e6, "G": 1e9}
_MOLTIPLICATORI_FREQ = (0.1, 0.5, 1.0, 2.0, 5.0, 10.0)


def parse_si(testo):
    """Converte un numero con prefisso SI opzionale ('1.6k', '100n', '2.2u')."""
    testo = testo.strip()
    if testo and testo[-1] in _PREFISSI:
        return float(testo[:-1]) * _PREFISSI[testo[-1]]
    return float(testo)


def formatta(valore, unita):
    """Formattazione con prefisso SI (3 cifre significative)."""
    if valore == 0:
        return f"0 {unita}"
    for soglia, prefisso in ((1e9, "G"), (1e6, "M"), (1e3, "k"), (1.0, ""), (1e-3, "m"),
                             (1e-6, "u"), (1e-9, "n"), (1e-12, "p")):
        if abs(valore) >= soglia * 0.9995:
            return f"{valore / soglia:.3g} {prefisso}{unita}"
    return f"{valore:.3g} {unita}"


def _riga_risposta(f, h):
    return f"{formatta(f, 'Hz'):>10}  {fc.db(h):8.2f} dB  {fc.fase_gradi(h):8.1f} gradi"


def cmd_rc(args):
    f0 = fc.rc_fc(args.r, args.c)
    print(f"RC: R = {formatta(args.r, 'ohm')}, C = {formatta(args.c, 'F')}")
    print(f"fc = {f0:.2f} Hz  (tau = {formatta(args.r * args.c, 's')})")
    print("\nPassa-basso")
    for m in _MOLTIPLICATORI_FREQ:
        print(_riga_risposta(m * f0, fc.h_rc_lp(m * f0, f0)))
    print("\nPassa-alto")
    for m in _MOLTIPLICATORI_FREQ:
        print(_riga_risposta(m * f0, fc.h_rc_hp(m * f0, f0)))
    if args.carico:
        r_th = args.r * args.carico / (args.r + args.carico)
        print(f"\nCarico {formatta(args.carico, 'ohm')}: guadagno DC = "
              f"{args.carico / (args.r + args.carico):.4f}, fc = {fc.rc_fc(r_th, args.c):.2f} Hz")
    return 0


def cmd_sk(args):
    try:
        s = fc.progetta_sezione_sk(args.f0, args.q, args.c2, args.serie_r, args.serie_c)
    except ValueError as e:
        print(f"Errore: {e}", file=sys.stderr)
        return 2
    print(f"Sallen-Key passa-basso, guadagno 1: f0 = {args.f0:g} Hz, Q = {args.q:g}")
    print(f"C1 (reazione) = {formatta(s.c1, 'F')}, C2 (a massa) = {formatta(s.c2, 'F')}")
    print(f"R1 = {formatta(s.r1, 'ohm')}, R2 = {formatta(s.r2, 'ohm')}  (serie {args.serie_r})")
    print(f"Valori effettivi: f0 = {s.f0:.1f} Hz ({(s.f0 / args.f0 - 1) * 100:+.2f}%), "
          f"Q = {s.q:.4f} ({(s.q / args.q - 1) * 100:+.2f}%)")
    return 0


def cmd_butter(args):
    sezioni = fc.progetta_cascata_butterworth_lp(args.n, args.fc, args.c, args.serie_r, args.serie_c)
    print(f"Butterworth passa-basso di ordine {args.n}, fc = {args.fc:g} Hz")
    for i, s in enumerate(sezioni, 1):
        if isinstance(s, fc.SezioneRc1):
            print(f"Sezione {i} (1o ordine, con buffer): R = {formatta(s.r, 'ohm')}, "
                  f"C = {formatta(s.c, 'F')}, f0 = {s.f0:.1f} Hz")
        else:
            print(f"Sezione {i} (Sallen-Key): R1 = {formatta(s.r1, 'ohm')}, R2 = {formatta(s.r2, 'ohm')}, "
                  f"C1 = {formatta(s.c1, 'F')}, C2 = {formatta(s.c2, 'F')} -> "
                  f"f0 = {s.f0:.1f} Hz, Q = {s.q:.4f} (obiettivo {s.q_obiettivo:.4f})")
    print("\nRisposta con i valori normalizzati (amplificatori ideali)")
    for m in _MOLTIPLICATORI_FREQ:
        f = m * args.fc
        h = fc.risposta_cascata_reale(sezioni, f)
        print(f"{formatta(f, 'Hz'):>10}  {fc.db(h):8.2f} dB  {fc.fase_cascata_gradi(sezioni, f):8.1f} gradi")
    return 0


def costruisci_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="comando", required=True)

    rc = sub.add_parser("rc", help="analisi di un RC del primo ordine")
    rc.add_argument("--r", type=parse_si, required=True, help="resistenza in ohm (es. 1.6k)")
    rc.add_argument("--c", type=parse_si, required=True, help="capacita' in F (es. 100n)")
    rc.add_argument("--carico", type=parse_si, default=None, help="resistenza di carico in ohm")
    rc.set_defaults(func=cmd_rc)

    sk = sub.add_parser("sk", help="progetto di una sezione Sallen-Key passa-basso a guadagno 1")
    sk.add_argument("--f0", type=parse_si, required=True)
    sk.add_argument("--q", type=float, required=True)
    sk.add_argument("--c2", type=parse_si, required=True, help="capacita' verso massa")
    sk.add_argument("--serie-r", default="E96", choices=("E12", "E24", "E96"))
    sk.add_argument("--serie-c", default="E12", choices=("E12", "E24"))
    sk.set_defaults(func=cmd_sk)

    bw = sub.add_parser("butter", help="Butterworth passa-basso a sezioni Sallen-Key in cascata")
    bw.add_argument("--n", type=int, required=True, help="ordine (1..8)")
    bw.add_argument("--fc", type=parse_si, required=True, help="frequenza di taglio a -3 dB")
    bw.add_argument("--c", type=parse_si, required=True, help="capacita' base C2 di ogni sezione")
    bw.add_argument("--serie-r", default="E96", choices=("E12", "E24", "E96"))
    bw.add_argument("--serie-c", default="E12", choices=("E12", "E24"))
    bw.set_defaults(func=cmd_butter)
    return p


def main(argv=None):
    args = costruisci_parser().parse_args(argv)
    if getattr(args, "n", 1) < 1 or getattr(args, "n", 1) > 8:
        print("Errore: l'ordine deve essere compreso tra 1 e 8", file=sys.stderr)
        return 2
    for nome in ("r", "c", "c2", "f0", "fc", "q", "carico"):
        v = getattr(args, nome, None)
        if v is not None and not (math.isfinite(v) and v > 0):
            print(f"Errore: --{nome.replace('_', '-')} deve essere positivo", file=sys.stderr)
            return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
