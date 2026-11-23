#!/usr/bin/env python3
# build_sch_ponte_p3.py — schema elettrico KiCad 7 del simulatore a ponte 348 ohm, rev P3.
# Genera simulatore_ponte_348_p3.kicad_sch con simboli standard KiCad (Device:R, Device:R_Potentiometer,
# Connector_Generic:Conn_01x06, Mechanical:MountingHole; estratti da kicad-symbols 7.0.11, licenza CC-BY-SA 4.0 con
# eccezione per le librerie KiCad) e li lega ai footprint della scheda tramite gli stessi UUID (path) del .kicad_pcb.
# Uso: python3 build_sch_ponte_p3.py   (esegue prima build_pcb_ponte_p3.py per avere l'elenco dei componenti)
import json, os, sys, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pcb_ponte_p3 as P

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, P.NAME, P.NAME + '.kicad_sch')
SYM = json.load(open(os.path.join(HERE, 'simboli_kicad7.json'), encoding='utf8'))
ROOT = str(uuid.uuid5(P.NS, 'root'))
G = 2.54

def u(tag):
    return str(uuid.uuid5(P.NS, 'sch:' + tag))

# ------------------------------------------------------------------ geometria dei pin
PINS = {   # (x, y) dei pin nel simbolo (y verso l'alto), come nei file della libreria
    'Device:R': {'1': (0, 3.81), '2': (0, -3.81)},
    'Device:R_Potentiometer': {'1': (0, 3.81), '2': (3.81, 0), '3': (0, -3.81)},
    'Connector_Generic:Conn_01x06': {str(k + 1): (-5.08, 5.08 - 2.54 * k) for k in range(6)},
    'Mechanical:MountingHole': {},
}
def pin_pos(lib, num, x, y, rot=0, mirror_y=False):
    import math
    px, py = PINS[lib][num]
    if mirror_y: px = -px
    a = math.radians(rot)
    rx, ry = px * math.cos(a) - py * math.sin(a), px * math.sin(a) + py * math.cos(a)
    return (round(x + rx, 4), round(y - ry, 4))

# ------------------------------------------------------------------ elementi
wires, junctions, labels, symbols = [], [], [], []

def n(v): 
    s = f'{v:.4f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def wire(a, b, tag):
    wires.append((a, b, tag))

def junction(p, tag):
    junctions.append((p, tag))

def glabel(name, p, ang, tag):
    labels.append((name, p, ang, tag))

def place(lib, ref, value, fp, x, y, rot=0, mirror_y=False, ref_at=None, val_at=None, hide_ref=False):
    symbols.append(dict(lib=lib, ref=ref, value=value, fp=fp, x=x, y=y, rot=rot, mirror=mirror_y, ref_at=ref_at, val_at=val_at))

FP = {f.ref: f for f in P.fps}
def fpname(ref): return 'Simulatore:' + FP[ref].lib
def val(ref): return FP[ref].value

# coordinate (mm, foglio A4, origine in alto a sinistra)
YP_, YM_ = 50.8, 152.4                         # dorsali E+ ed E-
XB, XA, XR5, XC, XD = 63.5, 76.2, 104.14, 134.62, 165.1
Y5, Y6, YPOT = 101.6, 121.92, 101.6

def vres(ref, x, ytop_pin):
    """Resistenza verticale con il pin 1 in alto a ytop_pin."""
    y = ytop_pin + 3.81
    place('Device:R', ref, val(ref), fpname(ref), x, y, 0, False, ref_at=(x + 2.54, y - 1.27), val_at=(x + 2.54, y + 1.27))
    return pin_pos('Device:R', '1', x, y), pin_pos('Device:R', '2', x, y)

# resistori del ponte e dei rami
r3t, r3b = vres('R3', XB, YP_)
r4t, r4b = vres('R4', XB, YM_ - 7.62)
r1t, r1b = vres('R1', XA, YP_)
r2t, r2b = vres('R2', XA, YM_ - 7.62)
r7t, r7b = vres('R7', XC, YP_)
r8t, r8b = vres('R8', XC, YM_ - 7.62)
# R5 e R6 orizzontali: pin 1 (cursore) a destra, pin 2 (A+) a sinistra
def hres(ref, x, y):
    place('Device:R', ref, val(ref), fpname(ref), x, y, 270, False, ref_at=(x, y - 2.54), val_at=(x, y + 2.54))
    return pin_pos('Device:R', '1', x, y, 270), pin_pos('Device:R', '2', x, y, 270)
r5r, r5l = hres('R5', XR5, Y5)
r6r, r6l = hres('R6', XR5, Y6)
# potenziometri con il cursore a sinistra
place('Device:R_Potentiometer', 'RV1', val('RV1'), fpname('RV1'), XC, YPOT, 0, True, ref_at=(XC + 5.5, YPOT - 1.27), val_at=(XC + 5.5, YPOT + 1.27))
rv1 = {k: pin_pos('Device:R_Potentiometer', k, XC, YPOT, 0, True) for k in '123'}
YPOT2 = Y6
place('Device:R_Potentiometer', 'RV2', val('RV2'), fpname('RV2'), XD, YPOT2, 0, True, ref_at=(XD + 5.5, YPOT2 - 1.27), val_at=(XD + 5.5, YPOT2 + 1.27))
rv2 = {k: pin_pos('Device:R_Potentiometer', k, XD, YPOT2, 0, True) for k in '123'}
# ponticelli R9/R10 e connettore J1
XR9 = 38.1
place('Device:R', 'R9', val('R9'), fpname('R9'), XR9, YP_, 270, False, ref_at=(XR9, YP_ - 2.54), val_at=(XR9, YP_ + 2.54))
r9r, r9l = pin_pos('Device:R', '1', XR9, YP_, 270), pin_pos('Device:R', '2', XR9, YP_, 270)
place('Device:R', 'R10', val('R10'), fpname('R10'), XR9, YM_, 270, False, ref_at=(XR9, YM_ - 2.54), val_at=(XR9, YM_ + 2.54))
r10r, r10l = pin_pos('Device:R', '1', XR9, YM_, 270), pin_pos('Device:R', '2', XR9, YM_, 270)
XJ1, YJ1 = 30.48, 101.6
place('Connector_Generic:Conn_01x06', 'J1', val('J1'), fpname('J1'), XJ1, YJ1, 0, False, ref_at=(XJ1 + 0, YJ1 - 11.0), val_at=(XJ1, YJ1 + 13.0))
j1 = {str(k): pin_pos('Connector_Generic:Conn_01x06', str(k), XJ1, YJ1) for k in range(1, 7)}
place('Mechanical:MountingHole', 'H1', 'M2.5', fpname('H1'), 20.32, 175.26, ref_at=(20.32, 172.0), val_at=(20.32, 178.0))
place('Mechanical:MountingHole', 'H2', 'M2.5', fpname('H2'), 45.72, 175.26, ref_at=(45.72, 172.0), val_at=(45.72, 178.0))

# dorsali (spezzate sui pin, con giunzioni nei punti a T)
def rail(y, xs, name):
    pts = sorted(xs)
    for a, b in zip(pts[:-1], pts[1:]):
        wire((a, y), (b, y), f'{name}{a}')
    for x in pts[1:-1]:
        junction((x, y), f'{name}j{x}')
XSTART = 45.72
rail(YP_, [XSTART, XB, XA, XC, XD], 'Rp')
rail(YM_, [XSTART, XB, XA, XC, XD], 'Rm')
wire(r9r, (XSTART, YP_), 'r9a'); wire(r10r, (XSTART, YM_), 'r10a')
glabel('E+', (54.61, YP_), 0, 'lp'); glabel('E-', (54.61, YM_), 0, 'lm')
# rami A e B
wire(r3b, r4t, 'legB'); glabel('A-', (XB, 88.9), 0, 'la-')
wire(r1b, (XA, Y5), 'legA1'); wire((XA, Y5), (XA, Y6), 'legA2'); wire((XA, Y6), r2t, 'legA3')
junction((XA, Y5), 'jA5'); junction((XA, Y6), 'jA6'); glabel('A+', (XA, 88.9), 0, 'la+')
wire(r5l, (XA, Y5), 'r5l'); wire(r6l, (XA, Y6), 'r6l')
# ramo C e cursori
wire(r7b, rv1['1'], 'c1'); glabel('N1', (XC, 78.74), 0, 'ln1')
wire(r8t, rv1['3'], 'c2'); glabel('N2', (XC, 134.62), 0, 'ln2')
wire(r5r, rv1['2'], 'w1'); glabel('W1', (116.84, Y5), 0, 'lw1')
wire(r6r, rv2['2'], 'w2'); glabel('W2', (116.84, Y6), 0, 'lw2')
# RV2 agli estremi sulle dorsali
wire(rv2['1'], (XD, YP_), 'z1'); wire(rv2['3'], (XD, YM_), 'z2')
# J1: spezzoni con etichette
names = ['EXC+', 'E+', 'A+', 'A-', 'E-', 'EXC-']
for k in range(1, 7):
    x, y = j1[str(k)]
    wire((x - 7.62, y), (x, y), f'j1w{k}')
    glabel(names[k - 1], (x - 7.62, y), 180, f'j1l{k}')
wire(r9l, (r9l[0] - 7.62, r9l[1]), 'r9w'); glabel('EXC+', (r9l[0] - 7.62, r9l[1]), 180, 'r9l')
wire(r10l, (r10l[0] - 7.62, r10l[1]), 'r10w'); glabel('EXC-', (r10l[0] - 7.62, r10l[1]), 180, 'r10l')

# ------------------------------------------------------------------ scrittura
def prop(name, value, at, hide=False, size=1.27, just='', ang=0):
    j = f' (justify {just})' if just else ''
    h = ' hide' if hide else ''
    return (f'    (property "{name}" "{value}" (at {n(at[0])} {n(at[1])} {ang})\n'
            f'      (effects (font (size {size} {size})){j}{h})\n    )\n')

def lib_block(lib):
    b = SYM[lib]
    first, rest = b.split('\n', 1)
    nm = lib.split(':')[1]
    first = first.replace(f'(symbol "{nm}"', f'(symbol "{lib}"', 1)
    return '    ' + first + '\n' + '\n'.join('  ' + l if l else l for l in rest.split('\n'))

def write():
    o = [f'(kicad_sch (version 20230121) (generator eeschema)\n\n  (uuid {ROOT})\n\n  (paper "A4")\n\n'
         '  (title_block\n    (title "Simulatore di cella di carico a ponte 348 ohm")\n    (date "2026-10-11")\n    (rev "P3")\n'
         '    (comment 1 "Resistenze a foro. Dispensa: dispensa_simulatore_ponte_348.html")\n'
         '    (comment 2 "Fondo scala +/-1,994 mV/V, Zout 341 ohm, carico 297 ohm")\n  )\n\n  (lib_symbols\n']
    for lib in SYM:
        o.append(lib_block(lib) + '\n')
    o.append('  )\n\n')
    for (p, tag) in junctions:
        o.append(f'  (junction (at {n(p[0])} {n(p[1])}) (diameter 0) (color 0 0 0 0)\n    (uuid {u("j" + tag)})\n  )\n')
    for (a, b, tag) in wires:
        o.append(f'  (wire (pts (xy {n(a[0])} {n(a[1])}) (xy {n(b[0])} {n(b[1])}))\n    (stroke (width 0) (type default))\n    (uuid {u("w" + tag)})\n  )\n')
    for (name, p, ang, tag) in labels:
        just = 'right' if ang == 180 else 'left'
        o.append(f'  (global_label "{name}" (shape passive) (at {n(p[0])} {n(p[1])} {ang})\n    (effects (font (size 1.27 1.27)) (justify {just}))\n'
                 f'    (uuid {u("l" + tag)})\n    (property "Intersheetrefs" "${{INTERSHEET_REFS}}" (at 0 0 0)\n      (effects (font (size 1.27 1.27)) hide)\n    )\n  )\n')
    for s in symbols:
        mir = ' (mirror y)' if s['mirror'] else ''
        ref_at = s['ref_at'] or (s['x'] + 3, s['y'] - 2)
        val_at = s['val_at'] or (s['x'] + 3, s['y'] + 2)
        pins = ''.join(f'    (pin "{k}" (uuid {u("p" + s["ref"] + k)}))\n' for k in PINS[s['lib']])
        o.append(f'  (symbol (lib_id "{s["lib"]}") (at {n(s["x"])} {n(s["y"])} {s["rot"]}){mir} (unit 1)\n'
                 f'    (in_bom yes) (on_board yes) (dnp no)\n    (uuid {P.sym_uuid(s["ref"])})\n'
                 + prop('Reference', s['ref'], ref_at, just=(('right' if s['mirror'] else 'left') if s['rot'] == 0 else ''), ang=(90 if s['rot'] in (90, 270) else 0))
                 + prop('Value', s['value'], val_at, just=(('right' if s['mirror'] else 'left') if s['rot'] == 0 else ''), ang=(90 if s['rot'] in (90, 270) else 0))
                 + prop('Footprint', s['fp'], (s['x'], s['y']), hide=True)
                 + prop('Datasheet', '~', (s['x'], s['y']), hide=True)
                 + pins +
                 f'    (instances\n      (project "{P.NAME}"\n        (path "/{ROOT}"\n          (reference "{s["ref"]}") (unit 1)\n        )\n      )\n    )\n  )\n')
    o.append('\n  (sheet_instances\n    (path "/" (page "1"))\n  )\n)\n')
    open(OUT, 'w', encoding='utf8').write(''.join(o))

if __name__ == '__main__':
    write()
    print('schema scritto:', OUT, '| simboli', len(symbols), '| fili', len(wires), '| etichette', len(labels))
