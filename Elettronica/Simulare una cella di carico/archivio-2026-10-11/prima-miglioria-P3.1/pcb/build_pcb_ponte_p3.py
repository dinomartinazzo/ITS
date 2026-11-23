#!/usr/bin/env python3
# build_pcb_ponte_p3.py — simulatore di cella di carico a ponte 348 ohm, rev P3, resistenze solo a foro.
# Genera direttamente i file KiCad 7 (testo S-expression): non richiede KiCad installato.
# Uso: python3 build_pcb_ponte_p3.py [cartella_uscita] [--stampe-proprie]
# Produce: .kicad_pcb/.kicad_pro/.kicad_prl, libreria footprint, BOM. Lo schema si genera con build_sch_ponte_p3.py.
# I Gerber, i fori e le stampe ufficiali si producono con esporta_con_kicad.sh (kicad-cli).
# Esegue anche un DRC proprio (distanze, bordo, fori) e il controllo di connettività delle reti.
import math, os, random, sys, uuid, json, csv

# ---------------------------------------------------------------- parametri
NAME = 'simulatore_ponte_348_p3'
OX, OY = 100.0, 100.0          # origine della scheda nel foglio KiCad [mm]
W, H = 51.5, 36.5              # dimensioni della scheda [mm]
TRACK = 0.3                    # larghezza piste [mm]
VIA_D, VIA_DRILL = 0.9, 0.4     # via: anello 0,25 mm (raccomandato JLCPCB)
SILK_H, SILK_T, SILK_LW = 1.0, 0.15, 0.15   # serigrafia: altezza testo, spessore, linee (minimi JLCPCB: 1,0 / 0,15 / 0,15)
CLEAR = 0.2                    # distanza minima rame-rame [mm]
EDGE = 0.3                     # distanza minima rame-bordo [mm]
rnd = random.Random(348)

def uid():
    return str(uuid.UUID(int=rnd.getrandbits(128), version=4))

SCH_NAME = 'simulatore_ponte_348_p3.kicad_sch'
NS = uuid.UUID('7c1f2c3a-0348-4b6e-9a7d-5f1c0de00348')
def sym_uuid(ref):
    return str(uuid.uuid5(NS, ref))

NETS = ['E+', 'E-', 'EXC+', 'EXC-', 'A+', 'A-', 'W1', 'W2', 'N1', 'N2']
NETID = {n: i + 1 for i, n in enumerate(NETS)}

# ---------------------------------------------------------------- modello
class Pad:
    def __init__(s, num, x, y, shape, w, h, drill, net, kind='thru'):
        s.num, s.x, s.y, s.shape, s.w, s.h, s.drill, s.net, s.kind = num, x, y, shape, w, h, drill, net, kind
        s.ref = ''
class FP:
    def __init__(s, lib, ref, value, x, y):
        s.lib, s.ref, s.value, s.x, s.y = lib, ref, value, x, y
        s.pads, s.lines, s.texts = [], [], []   # coordinate relative
class Track:
    def __init__(s, layer, net, pts, w=TRACK):
        s.layer, s.net, s.pts, s.w = layer, net, pts, w

fps, tracks, gtexts, edges, vias = [], [], [], [], []

def add_pad(fp, num, dx, dy, shape, size, drill, net, kind='thru'):
    p = Pad(num, fp.x + dx, fp.y + dy, shape, size, size, drill, net, kind)
    p.rel = (dx, dy); p.ref = fp.ref
    fp.pads.append(p)
    return p

def box(fp, x0, y0, x1, y1, layer='F.SilkS', w=SILK_LW):
    for a, b in (((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)), ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))):
        fp.lines.append((a, b, layer, w))

def axial_v(ref, value, x, y, n1, n2):
    """Resistenza assiale DIN0207 sulla scheda in verticale, passo 10,16 mm (pad 1 in alto); riferimento ruotato nel corpo."""
    fp = FP('R_Axial_DIN0207_P10.16mm_Rot90', ref, value, x, y)
    add_pad(fp, '1', 0, 0, 'rect', 1.6, 0.8, n1)
    add_pad(fp, '2', 0, 10.16, 'circle', 1.6, 0.8, n2)
    box(fp, -1.25, 1.93, 1.25, 8.23)
    fp.texts.append(('reference', ref, 0, 5.08, 'F.SilkS', SILK_H, 90))
    fp.texts.append(('value', value, 2.9, 5.08, 'F.Fab', 0.5, 90))
    fps.append(fp); return fp

def jumper(ref, value, x, y, n1, n2):
    """Ponticello a filo o resistenza 0,5-2 ohm: passo 5,08 mm in orizzontale (pad 1 a destra, pad 2 a sinistra)."""
    fp = FP('R_Axial_DIN0207_P5.08mm_Horizontal', ref, value, x, y)
    add_pad(fp, '1', 0, 0, 'rect', 1.6, 0.8, n1)
    add_pad(fp, '2', -5.08, 0, 'circle', 1.6, 0.8, n2)
    box(fp, -3.9, -0.6, -1.18, 0.6)
    fp.texts.append(('reference', ref, -2.54, 2.2, 'F.SilkS', SILK_H, 0))
    fp.texts.append(('value', value, -2.54, -1.9, 'F.Fab', 0.5, 0))
    fps.append(fp); return fp

def header(ref, value, x, y, n, nets, lib='PinHeader', label=None):
    fp = FP(f'{lib}_1x{n:02d}_P2.54mm_Vertical', ref, value, x, y)
    for i in range(n):
        add_pad(fp, str(i + 1), 0, i * 2.54, 'rect' if i == 0 else 'circle', 1.7, 1.0, nets[i])
    box(fp, -1.33, -1.33, 1.33, (n - 1) * 2.54 + 1.33)
    if label:
        fp.texts.append(('reference', ref, label[0], label[1], 'F.SilkS', SILK_H, label[2] if len(label) > 2 else 0))
    else:
        fp.texts.append(('reference', ref, 0, -2.4, 'F.SilkS', SILK_H, 0))
    fp.texts.append(('value', value, 0, n * 2.54, 'F.Fab', 0.6, 0))
    fps.append(fp); return fp

_nh = [0]
def hole(x, y, d=2.7):
    _nh[0] += 1
    ref = f'H{_nh[0]}'
    fp = FP('MountingHole_2.7mm_M2.5', ref, 'M2.5', x, y)
    p = Pad('', x, y, 'circle', d, d, d, None, 'npth'); p.rel = (0, 0); p.ref = ref
    fp.pads.append(p)
    fp.texts.append(('reference', ref, 0, -2.4, 'F.Fab', 0.6, 0))
    fp.texts.append(('value', 'M2.5', 0, 2.4, 'F.Fab', 0.6, 0))
    fps.append(fp); return fp

def track(layer, net, pts, w=TRACK):
    tracks.append(Track(layer, net, [tuple(p) for p in pts], w))

def via(x, y, net):
    vias.append((x, y, net))

# ---------------------------------------------------------------- progetto (griglia 2,54 mm)
G = 2.54
YT = 3.0                          # dorsale E+ (in alto)
YB = YT + 12 * G                  # dorsale E- (in basso), 30,48 mm sotto
XJ = 7.0                          # colonna di J1 e dei ponticelli R9/R10
XB = XJ + 4 * G                   # ramo B (R3 sopra, R4 sotto): nodo A-
XA = XB + 2 * G                   # ramo A (R1 sopra, R2 sotto): nodo A+
XR2 = XA + 2 * G                  # R5/R6: pad lato A+
XR1 = XR2 + 4 * G                 # R5/R6: pad lato cursore
XC = XR1 + 2 * G                  # ramo C (R7 sopra, RV1 al centro, R8 sotto)
XD = XC + 2 * G                   # RV2 (zero)
YM = YT + 6 * G                   # linea di mezzeria (cursore RV1 e R5)
Y6 = YM + 3 * G                   # linea del cursore RV2 e di R6

axial_v('R3', '348R 0,1%', XB, YT, 'E+', 'A-')
axial_v('R4', '348R 0,1%', XB, YT + 8 * G, 'A-', 'E-')
axial_v('R1', '348R 0,1%', XA, YT, 'E+', 'A+')
axial_v('R2', '348R 0,1%', XA, YT + 8 * G, 'A+', 'E-')
axial_v('R7', '909R 1%', XC, YT, 'E+', 'N1')
axial_v('R8', '909R 1%', XC, YT + 8 * G, 'N2', 'E-')
def axial_h(ref, value, x, y, n1, n2):     # R5/R6 orizzontali: pad 1 (cursore) a destra, pad 2 (A+) a sinistra
    fp = FP('R_Axial_DIN0207_P10.16mm_Horizontal', ref, value, x, y)
    add_pad(fp, '1', 5.08, 0, 'rect', 1.6, 0.8, n1)
    add_pad(fp, '2', -5.08, 0, 'circle', 1.6, 0.8, n2)
    box(fp, -3.15, -1.25, 3.15, 1.25)
    fp.texts.append(('reference', ref, 0, 0, 'F.SilkS', SILK_H, 0))
    fp.texts.append(('value', value, 0, 1.9, 'F.Fab', 0.5, 0))
    fps.append(fp); return fp
axial_h('R5', '3k65 0,1%', (XR1 + XR2) / 2, YM, 'W1', 'A+')
axial_h('R6', '71k5 1%', (XR1 + XR2) / 2, Y6, 'W2', 'A+')
rv1 = header('RV1', '200R 10 giri SPAN', XC, YM - G, 3, ['N1', 'W1', 'N2'], label=(2.3, 0.54, 90))
rv2 = header('RV2', '10k 25 giri ZERO', XD, Y6 - G, 3, ['E+', 'W2', 'E-'], label=(2.3, 0.54, 90))
YJ = YM - 2.5 * G                  # J1: 6 pin centrati sulla mezzeria
YP = [YJ + G * i for i in range(6)]
j1 = header('J1', 'Conn_01x06', XJ, YJ, 6, ['EXC+', 'E+', 'A+', 'A-', 'E-', 'EXC-'], label=(2.2, -2.2))
XN = XJ + 2 * G                    # nodo E+/E- del ponte a destra di R9/R10
r9 = jumper('R9', 'ponte 0R (cavo)', XN, YT, 'E+', 'EXC+')
r10 = jumper('R10', 'ponte 0R (cavo)', XN, YB, 'E-', 'EXC-')
hole(3.0, 3.0); hole(3.0, H - 3.0)

F, B = 'F.Cu', 'B.Cu'
# dorsali
track(F, 'E+', [(XN, YT), (XD, YT)])                      # E+ : R9 - R3 - R1 - R7 - RV2
track(F, 'E-', [(XN, YB), (XD, YB)])                      # E- : R10 - R4 - R2 - R8 - RV2
track(F, 'EXC+', [(XJ, YT), (XJ, YP[0])])                 # R9 -> J1 pin 1
track(F, 'EXC-', [(XJ, YB), (XJ, YP[5])])                 # R10 -> J1 pin 6
track(F, 'E+', [(XN, YT), (XN, YP[1]), (XJ, YP[1])])      # SENSE+ (pin 2) dal nodo del ponte
track(F, 'E-', [(XN, YB), (XN, YP[4]), (XJ, YP[4])])      # SENSE- (pin 5)
# rami del ponte
track(F, 'A-', [(XB, YT + 4 * G), (XB, YT + 8 * G)])
track(F, 'A-', [(XB, YP[3]), (XJ, YP[3])])                # A- verso J1 pin 4
track(F, 'A+', [(XA, YT + 4 * G), (XA, YT + 8 * G)])
track(F, 'A+', [(XA, YP[2]), (XA - G, YP[2])])            # A+ verso J1 pin 3 (scavalca il ramo B sul lato rame)
via(XA - G, YP[2], 'A+'); via(XB - G, YP[2], 'A+')
track(B, 'A+', [(XA - G, YP[2]), (XB - G, YP[2])])
track(F, 'A+', [(XB - G, YP[2]), (XJ, YP[2])])
# R5 e R6
track(F, 'A+', [(XR2, YM), (XA, YM)])
track(F, 'A+', [(XR2, Y6), (XR2, YT + 8 * G), (XA, YT + 8 * G)])
track(F, 'W1', [(XR1, YM), (XC, YM)])                     # cursore RV1 -> R5
track(F, 'W2', [(XR1, Y6), (XD, Y6)])                     # cursore RV2 -> R6 (passa sotto il corpo di R8)
# ramo C
track(F, 'N1', [(XC, YT + 4 * G), (XC, YM - G)])
track(F, 'N2', [(XC, YM + G), (XC, YT + 8 * G)])
# RV2: estremi sulle dorsali
track(F, 'E+', [(XD, YT), (XD, Y6 - G)])
track(F, 'E-', [(XD, Y6 + G), (XD, YB)])

# bordo
for a, b in (((0, 0), (W, 0)), ((W, 0), (W, H)), ((W, H), (0, H)), ((0, H), (0, 0))):
    edges.append((a, b))

# serigrafia
def silk(txt, x, y, size=SILK_H, layer='F.SilkS', just='', ang=0):
    gtexts.append((txt, x, y, size, layer, just, ang))
for lab, y in zip(('EXC+', 'SNS+', 'A+', 'A-', 'SNS-', 'EXC-'), YP):
    silk(lab, 0.8, y, SILK_H, 'F.SilkS', 'left')
silk('SPAN', XC + 2.6, YM + 2.2, SILK_H, 'F.SilkS', '', 90)
silk('ZERO', XD + 2.6, Y6 + 2.4, SILK_H, 'F.SilkS', '', 90)
silk('SIM. CELLA 348R', XA + 2.6, YT + 3.2, SILK_H, 'F.SilkS', 'left')
silk('+/-2 mV/V REV P3', XA + 2.6, YT + 5.4, SILK_H, 'F.SilkS', 'left')
silk('REV P3 10/2026', W / 2, H - 1.3, SILK_H, 'B.SilkS', '')



# ================================================================ uscita KiCad
def f(v):
    s = f'{v:.4f}'.rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s

def sx(v): return f(v + OX)
def sy(v): return f(v + OY)

def fp_text_block(kind, txt, x, y, layer, size, ang, ind):
    angs = f' {f(ang)}' if ang else ''
    return (f'{ind}(fp_text {kind} "{txt}" (at {f(x)} {f(y)}{angs}) (layer "{layer}")\n'
            f'{ind}    (effects (font (size {f(size)} {f(size)}) (thickness {f(SILK_T) if layer.endswith("SilkS") else "0.12"})))\n'
            f'{ind}  (tstamp {uid()})\n{ind})\n')

def pad_block(p, ind, with_net=True):
    nets = f'\n{ind}  (net {NETID[p.net]} "{p.net}")' if (with_net and p.net) else ''
    if p.kind == 'npth':
        return (f'{ind}(pad "" np_thru_hole circle (at {f(p.rel[0])} {f(p.rel[1])}) (size {f(p.w)} {f(p.h)}) '
                f'(drill {f(p.drill)}) (layers "*.Cu" "*.Mask") (tstamp {uid()}))\n')
    return (f'{ind}(pad "{p.num}" thru_hole {p.shape} (at {f(p.rel[0])} {f(p.rel[1])}) (size {f(p.w)} {f(p.h)}) '
            f'(drill {f(p.drill)}) (layers "*.Cu" "*.Mask"){nets}\n{ind}  (thermal_bridge_angle 45) (tstamp {uid()}))\n')

def fp_body(fp, ind, board):
    s = ''
    for kind, txt, dx, dy, layer, size, ang in fp.texts:
        s += fp_text_block(kind, txt, dx, dy, layer, size, ang, ind)
    for (a, b, layer, w) in fp.lines:
        s += (f'{ind}(fp_line (start {f(a[0])} {f(a[1])}) (end {f(b[0])} {f(b[1])})\n'
              f'{ind}  (stroke (width {f(w)}) (type default)) (layer "{layer}") (tstamp {uid()}))\n')
    for p in fp.pads:
        s += pad_block(p, ind, board)
    return s

def write_pcb(path):
    o = ['(kicad_pcb (version 20221018) (generator pcbnew)\n\n  (general\n    (thickness 1.6)\n  )\n\n  (paper "A4")\n  (layers\n']
    layers = [(0, 'F.Cu', 'signal'), (31, 'B.Cu', 'signal'), (32, 'B.Adhes', 'user', 'B.Adhesive'), (33, 'F.Adhes', 'user', 'F.Adhesive'),
              (34, 'B.Paste', 'user'), (35, 'F.Paste', 'user'), (36, 'B.SilkS', 'user', 'B.Silkscreen'), (37, 'F.SilkS', 'user', 'F.Silkscreen'),
              (38, 'B.Mask', 'user'), (39, 'F.Mask', 'user'), (40, 'Dwgs.User', 'user', 'User.Drawings'), (41, 'Cmts.User', 'user', 'User.Comments'),
              (42, 'Eco1.User', 'user', 'User.Eco1'), (43, 'Eco2.User', 'user', 'User.Eco2'), (44, 'Edge.Cuts', 'user'), (45, 'Margin', 'user'),
              (46, 'B.CrtYd', 'user', 'B.Courtyard'), (47, 'F.CrtYd', 'user', 'F.Courtyard'), (48, 'B.Fab', 'user'), (49, 'F.Fab', 'user')]
    layers += [(50 + i, f'User.{i + 1}', 'user') for i in range(9)]
    for l in layers:
        o.append(f'    ({l[0]} "{l[1]}" {l[2]}' + (f' "{l[3]}"' if len(l) > 3 else '') + ')\n')
    o.append('  )\n\n  (setup\n    (pad_to_mask_clearance 0)\n    (pcbplotparams\n      (layerselection 0x00010fc_ffffffff)\n'
             '      (plot_on_all_layers_selection 0x0000000_00000000)\n      (disableapertmacros false)\n      (usegerberextensions false)\n'
             '      (usegerberattributes true)\n      (usegerberadvancedattributes true)\n      (creategerberjobfile true)\n'
             '      (dashed_line_dash_ratio 12.000000)\n      (dashed_line_gap_ratio 3.000000)\n      (svgprecision 4)\n      (plotframeref false)\n'
             '      (viasonmask false)\n      (mode 1)\n      (useauxorigin false)\n      (hpglpennumber 1)\n      (hpglpenspeed 20)\n'
             '      (hpglpendiameter 15.000000)\n      (dxfpolygonmode true)\n      (dxfimperialunits true)\n      (dxfusepcbnewfont true)\n'
             '      (psnegative false)\n      (psa4output false)\n      (plotreference true)\n      (plotvalue true)\n      (plotinvisibletext false)\n'
             '      (sketchpadsonfab false)\n      (subtractmaskfromsilk false)\n      (outputformat 1)\n      (mirror false)\n      (drillshape 1)\n'
             '      (scaleselection 1)\n      (outputdirectory "")\n    )\n  )\n\n  (net 0 "")\n')
    for n in NETS:
        o.append(f'  (net {NETID[n]} "{n}")\n')
    o.append('\n')
    for fp in fps:
        attr = '(attr through_hole)' if fp.lib.startswith(('R_', 'Pin', 'Trimmer')) else ''
        o.append(f'  (footprint "Simulatore:{fp.lib}" (layer "F.Cu")\n    (tstamp {sym_uuid(fp.ref)})\n    (at {sx(fp.x)} {sy(fp.y)})\n'
                 f'    (property "Sheetfile" "{SCH_NAME}")\n    (property "Sheetname" "")\n    (path "/{sym_uuid(fp.ref)}")\n'
                 + (f'    {attr}\n' if attr else '') + fp_body(fp, '    ', True) + '  )\n\n')
    for t in tracks:
        for a, b in zip(t.pts[:-1], t.pts[1:]):
            o.append(f'  (segment (start {sx(a[0])} {sy(a[1])}) (end {sx(b[0])} {sy(b[1])}) (width {f(t.w)}) '
                     f'(layer "{t.layer}") (net {NETID[t.net]}) (tstamp {uid()}))\n')
    for (vx, vy, vn) in vias:
        o.append(f'  (via (at {sx(vx)} {sy(vy)}) (size {f(VIA_D)}) (drill {f(VIA_DRILL)}) (layers "F.Cu" "B.Cu") (net {NETID[vn]}) (tstamp {uid()}))\n')
    for a, b in edges:
        o.append(f'  (gr_line (start {sx(a[0])} {sy(a[1])}) (end {sx(b[0])} {sy(b[1])})\n    (stroke (width 0.1) (type default)) '
                 f'(layer "Edge.Cuts") (tstamp {uid()}))\n')
    for txt, x, y, size, layer, just, gang in gtexts:
        j = ''
        if just or layer == 'B.SilkS':
            j = ' (justify ' + ' '.join(filter(None, [just, 'mirror' if layer == 'B.SilkS' else ''])) + ')'
        gat = f' {f(gang)}' if gang else ''
        o.append(f'  (gr_text "{txt}" (at {sx(x)} {sy(y)}{gat}) (layer "{layer}") (tstamp {uid()})\n    (effects (font (size {f(size)} {f(size)}) '
                 f'(thickness {f(SILK_T)})){j})\n  )\n')
    o.append(')\n')
    open(path, 'w', encoding='utf8').write(''.join(o))

def write_library(d):
    os.makedirs(d, exist_ok=True)
    seen = set()
    for fp in fps:
        if fp.lib in seen:
            continue
        seen.add(fp.lib)
        attr = '  (attr through_hole)\n' if fp.lib.startswith(('R_', 'Pin', 'Trimmer')) else ''
        s = (f'(footprint "{fp.lib}" (version 20221018) (generator pcbnew)\n  (layer "F.Cu")\n' + attr
             + fp_body(fp, '  ', False) + ')\n')
        open(os.path.join(d, fp.lib + '.kicad_mod'), 'w', encoding='utf8').write(s)

def write_project(d):
    pro = {
        'board': {'design_settings': {'defaults': {'board_outline_line_width': 0.05, 'copper_line_width': 0.2,
                  'silk_line_width': SILK_LW, 'silk_text_size_h': SILK_H, 'silk_text_size_v': SILK_H, 'silk_text_thickness': SILK_T,
                  'pads': {'drill': 0.8, 'height': 1.6, 'width': 1.6}},
                  'rules': {'min_clearance': CLEAR, 'min_track_width': 0.2, 'min_through_hole_diameter': 0.3, 'min_via_diameter': 0.5, 'min_via_annular_width': 0.1, 'min_text_height': SILK_H, 'min_text_thickness': SILK_T, 'min_silk_clearance': 0.15,
                            'min_copper_edge_clearance': EDGE, 'min_hole_to_hole': 0.5, 'min_resolved_spokes': 2},
                  'rule_severities': {'clearance': 'error', 'copper_edge_clearance': 'error', 'shorting_items': 'error',
                                      'unconnected_items': 'error', 'hole_near_hole': 'error', 'track_width': 'error'}}},
        'meta': {'filename': NAME + '.kicad_pro', 'version': 1},
        'net_settings': {'classes': [{'name': 'Default', 'clearance': CLEAR, 'track_width': TRACK, 'via_diameter': VIA_D,
                                      'via_drill': VIA_DRILL, 'pcb_color': 'rgba(0, 0, 0, 0.000)'}], 'meta': {'version': 3},
                         'net_colors': None},
        'sheets': [], 'text_variables': {}}
    open(os.path.join(d, NAME + '.kicad_pro'), 'w', encoding='utf8').write(json.dumps(pro, indent=2))
    prl = {'board': {'active_layer': 0, 'visible_layers': 'fffffff_ffffffff', 'zone_display_mode': 0},
           'meta': {'filename': NAME + '.kicad_prl', 'version': 3}, 'project': {'files': []}}
    open(os.path.join(d, NAME + '.kicad_prl'), 'w', encoding='utf8').write(json.dumps(prl, indent=2))
    open(os.path.join(d, 'fp-lib-table'), 'w', encoding='utf8').write(
        '(fp_lib_table\n  (version 7)\n  (lib (name "Simulatore")(type "KiCad")(uri "${KIPRJMOD}/Simulatore.pretty")'
        '(options "")(descr "Footprint del simulatore di cella di carico"))\n)\n')

def write_bom(d):
    rows = [('R1,R2,R3,R4', 4, '348R 0,1%', 'R_Axial_DIN0207_P10.16mm_Rot90', 'Strato metallico 1/4 W 0,1%, 25 ppm/°C', 'Stesso lotto, appaiate con il multimetro'),
            ('R5', 1, '3k65 0,1%', 'R_Axial_DIN0207_P10.16mm_Horizontal', 'Strato metallico 1/4 W 0,1%', 'Determina il fondo scala'),
            ('R6', 1, '71k5 1%', 'R_Axial_DIN0207_P10.16mm_Horizontal', 'Strato metallico 1/4 W 1%', 'Agisce solo sullo zero'),
            ('R7,R8', 2, '909R 1%', 'R_Axial_DIN0207_P10.16mm_Rot90', 'Strato metallico 1/4 W 1% (0,1% se disponibili)', 'In serie al multigiri RV1'),
            ('R9,R10', 2, 'ponticello 0R', 'R_Axial_DIN0207_P5.08mm_Horizontal', 'Filo nudo o resistenza 0 ohm', 'Da montare sempre; sostituibili con 0,5-2 ohm per simulare il cavo'),
            ('RV1', 1, '200R 10 giri', 'PinHeader_1x03_P2.54mm_Vertical', 'Multigiri 200 ohm, strato metallico (già disponibile)', 'Pin 1 = lato R7, 2 = cursore, 3 = lato R8; SPAN'),
            ('RV2', 1, '10k 25 giri', 'PinHeader_1x03_P2.54mm_Vertical', 'Bourns 3296W-1-103LF', 'Pin 1 = E+, 2 = cursore, 3 = E-; ZERO. Impronta generica a 3 poli; verificare ingombro e orientamento prima del montaggio diretto, oppure collegare con tre fili.'),
            ('J1', 1, 'Conn_01x06', 'PinHeader_1x06_P2.54mm_Vertical', 'Pin header 1x6 passo 2,54 mm', '1 EXC+, 2 SENSE+, 3 A+, 4 A-, 5 SENSE-, 6 EXC-'),
            ('H1,H2', 2, 'M2.5', 'MountingHole_2.7mm_M2.5', 'Distanziale M2,5', '')]
    with open(os.path.join(d, NAME + '-bom.csv'), 'w', encoding='utf8', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL)
        w.writerow(['Rif', 'Q.ta', 'Valore', 'Footprint', 'Componente', 'Note'])
        w.writerows(rows)

# ================================================================ DRC e connettività
def shapes_of(pad, layer):
    if pad.kind == 'npth':
        return None
    if pad.shape == 'rect':
        h = pad.w / 2
        return ('rect', (pad.x - h, pad.y - h, pad.x + h, pad.y + h), 0.0)
    return ('disc', (pad.x, pad.y), pad.w / 2)

def trk_shapes(t):
    return [('cap', (a, b), t.w / 2) for a, b in zip(t.pts[:-1], t.pts[1:])]

def pseg(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    u = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
    return math.hypot(px - (ax + u * dx), py - (ay + u * dy))

def ccw(a, b, c): return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
def seg_x(a, b, c, d):
    return ccw(a, c, d) * ccw(b, c, d) < 0 and ccw(a, b, c) * ccw(a, b, d) < 0
def sseg(a, b, c, d):
    if seg_x(a, b, c, d): return 0.0
    return min(pseg(a, c, d), pseg(b, c, d), pseg(c, a, b), pseg(d, a, b))

def rect_edges(r):
    x0, y0, x1, y1 = r
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    return [(pts[i], pts[(i + 1) % 4]) for i in range(4)]
def in_rect(p, r): return r[0] <= p[0] <= r[2] and r[1] <= p[1] <= r[3]

def dist(s1, s2):
    k1, g1, r1 = s1; k2, g2, r2 = s2
    if k1 == 'rect' and k2 == 'rect':
        dx = max(g2[0] - g1[2], g1[0] - g2[2], 0); dy = max(g2[1] - g1[3], g1[1] - g2[3], 0)
        return math.hypot(dx, dy) - r1 - r2
    if k2 == 'rect':
        return dist(s2, s1)
    if k1 == 'rect':
        if k2 == 'disc':
            p = g2
            d = 0 if in_rect(p, g1) else min(pseg(p, a, b) for a, b in rect_edges(g1))
        else:
            a2, b2 = g2
            if in_rect(a2, g1) or in_rect(b2, g1): d = 0
            else: d = min(sseg(a2, b2, a, b) for a, b in rect_edges(g1))
        return d - r1 - r2
    if k1 == 'disc' and k2 == 'disc':
        return math.hypot(g1[0] - g2[0], g1[1] - g2[1]) - r1 - r2
    if k1 == 'disc':
        return pseg(g1, *g2) - r1 - r2
    if k2 == 'disc':
        return pseg(g2, *g1) - r1 - r2
    return sseg(g1[0], g1[1], g2[0], g2[1]) - r1 - r2

def run_checks():
    errs, info = [], []
    pads = [p for fp in fps for p in fp.pads]
    cu = []   # (layer, net, shape, label)
    for layer in ('F.Cu', 'B.Cu'):
        for p in pads:
            if p.kind == 'thru':
                cu.append((layer, p.net, shapes_of(p, layer), f'pad {p.ref}.{p.num}'))
        for i, t in enumerate(tracks):
            if t.layer == layer:
                for j, sh in enumerate(trk_shapes(t)):
                    cu.append((layer, t.net, sh, f'pista#{i}.{j} {t.net}'))
        for k, (vx, vy, vn) in enumerate(vias):
            cu.append((layer, vn, ('disc', (vx, vy), VIA_D / 2), f'via#{k} {vn}'))
    n = 0
    for i in range(len(cu)):
        for j in range(i + 1, len(cu)):
            a, b = cu[i], cu[j]
            if a[0] != b[0] or a[1] == b[1]: continue
            d = dist(a[2], b[2]); n += 1
            if d < CLEAR - 1e-6:
                errs.append(f'DISTANZA {d:.3f} < {CLEAR}: {a[3]} / {b[3]} ({a[0]})')
    info.append(f'coppie rame verificate: {n}')
    ed = [('cap', (a, b), 0.05) for a, b in edges]
    for lay, net, sh, lab in cu:
        for e in ed:
            d = dist(sh, e)
            if d < EDGE - 1e-6: errs.append(f'BORDO {d:.3f} < {EDGE}: {lab}')
    holes = [(p.x, p.y, p.drill / 2, f'{p.ref}.{p.num}') for p in pads] + [(vx, vy, VIA_DRILL / 2, f'via#{k}') for k, (vx, vy, vn) in enumerate(vias)]
    for i in range(len(holes)):
        for j in range(i + 1, len(holes)):
            a, b = holes[i], holes[j]
            g = math.hypot(a[0] - b[0], a[1] - b[1]) - a[2] - b[2]
            if g < 0.5 - 1e-6: errs.append(f'FORI vicini {g:.3f}: {a[3]} / {b[3]}')
    for p in pads:
        if p.kind == 'thru':
            ann = (p.w - p.drill) / 2
            if ann < 0.25 - 1e-6: errs.append(f'anello {ann:.2f} su {p.ref}.{p.num}')
    for t in tracks:
        if t.w < 0.2: errs.append(f'pista troppo stretta {t.w}')
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b): parent[find(a)] = find(b)
    objs = []
    for p in pads:
        if p.kind == 'thru':
            for layer in ('F.Cu', 'B.Cu'):
                objs.append((('pad', id(p)), layer, shapes_of(p, layer), p.net))
    for i, t in enumerate(tracks):
        for j, sh in enumerate(trk_shapes(t)):
            objs.append((('trk', i), t.layer, sh, t.net))
    for k, (vx, vy, vn) in enumerate(vias):
        for layer in ('F.Cu', 'B.Cu'):
            objs.append((('via', k), layer, ('disc', (vx, vy), VIA_D / 2), vn))
    for a in range(len(objs)):
        for b in range(a + 1, len(objs)):
            A, B_ = objs[a], objs[b]
            if A[1] == B_[1] and A[3] == B_[3] and dist(A[2], B_[2]) <= 0.001:
                union(A[0], B_[0])
    byn = {}
    for p in pads:
        if p.kind == 'thru': byn.setdefault(p.net, []).append(p)
    for net, ps in byn.items():
        roots = {find(('pad', id(p))) for p in ps}
        if len(ps) > 1 and len(roots) > 1:
            errs.append(f'NON CONNESSA rete {net}: {len(roots)} gruppi ({", ".join(p.ref + "." + p.num for p in ps)})')
        info.append(f'rete {net:5s}: {len(ps)} pad, {"connessa" if len(roots) == 1 else "NON connessa"}')
    for i, t in enumerate(tracks):
        r = find(('trk', i))
        if not any(find(('pad', id(p))) == r for p in pads if p.kind == 'thru'):
            errs.append(f'pista #{i} ({t.net}) isolata dai pad')
    for k, (vx, vy, vn) in enumerate(vias):
        r = find(('via', k))
        nconn = sum(1 for i, t in enumerate(tracks) if find(('trk', i)) == r and t.layer == 'F.Cu') and sum(1 for i, t in enumerate(tracks) if find(('trk', i)) == r and t.layer == 'B.Cu')
        if not nconn: errs.append(f'via #{k} ({vn}) non collega i due strati')
    return errs, info

# ================================================================ anteprima SVG (vista dall'alto e dal retro)
def write_svg(path, side='top', scale=14.0):
    mir = (side == 'bottom')
    def X(x): return (W - x if mir else x) * scale
    def Y(y): return y * scale
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * scale}" height="{H * scale}" viewBox="0 0 {W * scale} {H * scale}">',
         f'<rect width="{W * scale}" height="{H * scale}" fill="#14502a"/>']
    first, second = ('B.Cu', 'F.Cu') if side == 'top' else ('F.Cu', 'B.Cu')
    colors = {'F.Cu': '#d23b3b', 'B.Cu': '#3d6bd6'}
    def draw_tracks(layer, op):
        for t in tracks:
            if t.layer == layer:
                pts = ' '.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in t.pts)
                o.append(f'<polyline points="{pts}" fill="none" stroke="{colors[layer]}" stroke-width="{t.w * scale:.1f}" '
                         f'stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>')
    draw_tracks(first, 0.55); draw_tracks(second, 1.0)
    for fp in fps:
        for p in fp.pads:
            if p.kind == 'npth':
                o.append(f'<circle cx="{X(p.x):.1f}" cy="{Y(p.y):.1f}" r="{p.drill / 2 * scale:.1f}" fill="#0b0b0b"/>'); continue
            if p.shape == 'rect':
                o.append(f'<rect x="{X(p.x) - p.w / 2 * scale:.1f}" y="{Y(p.y) - p.w / 2 * scale:.1f}" width="{p.w * scale:.1f}" height="{p.w * scale:.1f}" fill="#d9b94a"/>')
            else:
                o.append(f'<circle cx="{X(p.x):.1f}" cy="{Y(p.y):.1f}" r="{p.w / 2 * scale:.1f}" fill="#d9b94a"/>')
            o.append(f'<circle cx="{X(p.x):.1f}" cy="{Y(p.y):.1f}" r="{p.drill / 2 * scale:.1f}" fill="#0b0b0b"/>')
    for (vx, vy, vn) in vias:
        o.append(f'<circle cx="{X(vx):.1f}" cy="{Y(vy):.1f}" r="{VIA_D / 2 * scale:.1f}" fill="#d9b94a"/><circle cx="{X(vx):.1f}" cy="{Y(vy):.1f}" r="{0.2 * scale:.1f}" fill="#0b0b0b"/>')
    want = 'F.SilkS' if side == 'top' else 'B.SilkS'
    if side == 'top':
        for fp in fps:
            for (a, b, layer, w) in fp.lines:
                if layer == 'F.SilkS':
                    o.append(f'<line x1="{X(fp.x + a[0]):.1f}" y1="{Y(fp.y + a[1]):.1f}" x2="{X(fp.x + b[0]):.1f}" y2="{Y(fp.y + b[1]):.1f}" stroke="#f1f1f1" stroke-width="{w * scale:.1f}"/>')
            for kind, txt, dx, dy, layer, size, ang in fp.texts:
                if layer == 'F.SilkS':
                    cx, cy = X(fp.x + dx), Y(fp.y + dy)
                    rot = f' transform="rotate({-ang} {cx:.1f} {cy:.1f})"' if ang else ''
                    o.append(f'<text x="{cx:.1f}" y="{cy + size * scale * 0.35:.1f}" font-family="DejaVu Sans Mono,monospace" '
                             f'font-size="{size * scale:.1f}" fill="#f1f1f1" text-anchor="middle"{rot}>{txt}</text>')
    for txt, x, y, size, layer, just, gang in gtexts:
        if layer == want:
            anchor = 'start' if just == 'left' else 'middle'
            if mir: anchor = 'end' if just == 'left' else 'middle'
            tr = f' transform="rotate({-gang} {X(x):.1f} {Y(y):.1f})"' if gang else ''
            o.append(f'<text x="{X(x):.1f}" y="{Y(y) + size * scale * 0.35:.1f}" font-family="DejaVu Sans Mono,monospace" font-size="{size * scale:.1f}" '
                     f'fill="#f1f1f1" text-anchor="{anchor}"{tr}>{txt}</text>')
    o.append(f'<rect x="0.5" y="0.5" width="{W * scale - 1}" height="{H * scale - 1}" fill="none" stroke="#f5d742" stroke-width="1.4"/>')
    o.append('</svg>')
    open(path, 'w', encoding='utf8').write('\n'.join(o))



# ================================================================ maschere 1:1 (nero su bianco) per stampa
def write_master_svg(path, layer, mirrored):
    sc = 1.0   # 1 unità SVG = 1 mm
    def X(x): return W - x if mirrored else x
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
         f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for t in tracks:
        if t.layer == layer:
            pts = ' '.join(f'{X(x):.3f},{y:.3f}' for x, y in t.pts)
            o.append(f'<polyline points="{pts}" fill="none" stroke="#000" stroke-width="{t.w}" stroke-linecap="round" stroke-linejoin="round"/>')
    for fp in fps:
        for p in fp.pads:
            if p.kind != 'thru': continue
            if p.shape == 'rect':
                o.append(f'<rect x="{X(p.x) - p.w / 2:.3f}" y="{p.y - p.w / 2:.3f}" width="{p.w}" height="{p.w}" fill="#000"/>')
            else:
                o.append(f'<circle cx="{X(p.x):.3f}" cy="{p.y:.3f}" r="{p.w / 2}" fill="#000"/>')
            o.append(f'<circle cx="{X(p.x):.3f}" cy="{p.y:.3f}" r="0.2" fill="#fff"/>')   # centro foro per la punta
    for (vx, vy, vn) in vias:
        o.append(f'<circle cx="{X(vx):.3f}" cy="{vy:.3f}" r="{VIA_D / 2}" fill="#000"/><circle cx="{X(vx):.3f}" cy="{vy:.3f}" r="0.15" fill="#fff"/>')
    o.append(f'<rect x="0.05" y="0.05" width="{W - 0.1}" height="{H - 0.1}" fill="none" stroke="#000" stroke-width="0.1" stroke-dasharray="1 1"/>')
    o.append('</svg>')
    open(path, 'w', encoding='utf8').write('\n'.join(o))

# ================================================================ Gerber / Excellon
FONT = {
 '0': [[(0,0),(4,0),(4,6),(0,6),(0,0)], [(1,1),(3,5)]], '1': [[(1,5),(2,6),(2,0)], [(1,0),(3,0)]],
 '2': [[(0,6),(4,6),(4,3),(0,3),(0,0),(4,0)]], '3': [[(0,6),(4,6),(4,0),(0,0)], [(1,3),(4,3)]],
 '4': [[(0,6),(0,3),(4,3)], [(4,6),(4,0)]], '5': [[(4,6),(0,6),(0,3),(4,3),(4,0),(0,0)]],
 '6': [[(4,6),(0,6),(0,0),(4,0),(4,3),(0,3)]], '7': [[(0,6),(4,6),(4,0)]],
 '8': [[(0,0),(4,0),(4,6),(0,6),(0,0)], [(0,3),(4,3)]], '9': [[(4,3),(0,3),(0,6),(4,6),(4,0),(0,0)]],
 'A': [[(0,0),(0,4),(2,6),(4,4),(4,0)], [(0,3),(4,3)]],
 'B': [[(0,0),(0,6),(3,6),(4,5),(4,4),(3,3),(0,3)], [(3,3),(4,2),(4,1),(3,0),(0,0)]],
 'C': [[(4,5),(3,6),(1,6),(0,5),(0,1),(1,0),(3,0),(4,1)]], 'D': [[(0,0),(0,6),(3,6),(4,5),(4,1),(3,0),(0,0)]],
 'E': [[(4,6),(0,6),(0,0),(4,0)], [(0,3),(3,3)]], 'F': [[(4,6),(0,6),(0,0)], [(0,3),(3,3)]],
 'G': [[(4,5),(3,6),(1,6),(0,5),(0,1),(1,0),(3,0),(4,1),(4,3),(2,3)]],
 'H': [[(0,0),(0,6)], [(4,0),(4,6)], [(0,3),(4,3)]], 'I': [[(1,6),(3,6)], [(2,6),(2,0)], [(1,0),(3,0)]],
 'J': [[(4,6),(4,1),(3,0),(1,0),(0,1)]], 'K': [[(0,0),(0,6)], [(4,6),(0,3),(4,0)]],
 'L': [[(0,6),(0,0),(4,0)]], 'M': [[(0,0),(0,6),(2,3),(4,6),(4,0)]], 'N': [[(0,0),(0,6),(4,0),(4,6)]],
 'O': [[(1,0),(0,1),(0,5),(1,6),(3,6),(4,5),(4,1),(3,0),(1,0)]],
 'P': [[(0,0),(0,6),(3,6),(4,5),(4,4),(3,3),(0,3)]], 'Q': [[(1,0),(0,1),(0,5),(1,6),(3,6),(4,5),(4,1),(3,0),(1,0)], [(2,2),(4,0)]],
 'R': [[(0,0),(0,6),(3,6),(4,5),(4,4),(3,3),(0,3)], [(2,3),(4,0)]],
 'S': [[(4,5),(3,6),(1,6),(0,5),(0,4),(1,3),(3,3),(4,2),(4,1),(3,0),(1,0),(0,1)]],
 'T': [[(0,6),(4,6)], [(2,6),(2,0)]], 'U': [[(0,6),(0,1),(1,0),(3,0),(4,1),(4,6)]],
 'V': [[(0,6),(2,0),(4,6)]], 'W': [[(0,6),(1,0),(2,3),(3,0),(4,6)]], 'X': [[(0,6),(4,0)], [(0,0),(4,6)]],
 'Y': [[(0,6),(2,3),(4,6)], [(2,3),(2,0)]], 'Z': [[(0,6),(4,6),(0,0),(4,0)]],
 '+': [[(2,1),(2,5)], [(0,3),(4,3)]], '-': [[(0,3),(4,3)]], '.': [[(2,0),(2,0.4)]], '/': [[(0,0),(4,6)]],
 'm': [[(0,0),(0,4)], [(0,3),(1,4),(2,3),(3,4),(4,3),(4,0)], [(2,3),(2,0)]],
 'k': [[(0,0),(0,6)], [(4,4),(0,2)], [(1,3),(4,0)]], ' ': [],
}

def text_strokes(txt, x0, y0, size, justify, mirror, ang=0):
    """Segmenti (polilinee) in coordinate scheda per un testo; y0 = centro verticale."""
    u = size / 6.0
    adv = 5.5 * u
    total = len(txt) * adv - 1.5 * u
    if justify == 'left':
        start = 0.0
    else:
        start = -total / 2.0
    out = []
    for i, ch in enumerate(txt):
        key = ch if ch in FONT else ch.upper()
        for poly in FONT.get(key, []):
            pts = []
            for cx, cy in poly:
                dx = start + i * adv + cx * u
                if mirror: dx = -dx
                dy = (3 - cy) * u
                if ang:   # rotazione antioraria vista dall'alto (y verso il basso)
                    a = math.radians(ang)
                    dx, dy = dx * math.cos(a) + dy * math.sin(a), -dx * math.sin(a) + dy * math.cos(a)
                pts.append((x0 + dx, y0 + dy))
            out.append(pts)
    return out

class Gerber:
    def __init__(s, function, polarity='Positive'):
        s.ap, s.cmds, s.function, s.pol = {}, [], function, polarity
    def aperture(s, kind, *dims):
        key = (kind,) + tuple(round(d, 4) for d in dims)
        if key not in s.ap: s.ap[key] = 10 + len(s.ap)
        return s.ap[key]
    def sel(s, d): s.cmds.append(f'D{d}*')
    @staticmethod
    def c(v): return int(round(v * 1e6))
    def pt(s, x, y): return f'X{s.c(x)}Y{s.c(H - y)}'
    def flash(s, x, y, kind, *dims):
        s.sel(s.aperture(kind, *dims)); s.cmds.append(s.pt(x, y) + 'D03*')
    def draw(s, pts, w):
        s.sel(s.aperture('C', w))
        s.cmds.append(s.pt(*pts[0]) + 'D02*')
        for p in pts[1:]: s.cmds.append(s.pt(*p) + 'D01*')
    def save(s, path):
        o = ['G04 Generato da build_pcb_ponte_p3.py*', '%MOMM*%', '%FSLAX46Y46*%',
             f'%TF.GenerationSoftware,build_pcb_ponte_p3.py,rev P3*%', f'%TF.FileFunction,{s.function}*%',
             f'%TF.FilePolarity,{s.pol}*%', '%LPD*%', 'G01*']
        for key, d in s.ap.items():
            k = key[0]
            o.append(f'%ADD{d}C,{key[1]:.6f}*%' if k == 'C' else f'%ADD{d}R,{key[1]:.6f}X{key[2]:.6f}*%')
        o += s.cmds + ['M02*']
        open(path, 'w', encoding='utf8').write('\n'.join(o) + '\n')

def write_gerbers(d):
    os.makedirs(d, exist_ok=True)
    P = lambda sfx: os.path.join(d, f'{NAME}-{sfx}')
    for layer, sfx, fn in (('F.Cu', 'F_Cu.gtl', 'Copper,L1,Top'), ('B.Cu', 'B_Cu.gbl', 'Copper,L2,Bot')):
        g = Gerber(fn)
        for t in tracks:
            if t.layer == layer:
                g.draw(t.pts, t.w)
        for fp in fps:
            for p in fp.pads:
                if p.kind == 'thru':
                    (g.flash(p.x, p.y, 'R', p.w, p.w) if p.shape == 'rect' else g.flash(p.x, p.y, 'C', p.w))
        for vx, vy, vn in vias:
            g.flash(vx, vy, 'C', VIA_D)
        g.save(P(sfx))
    for layer, sfx, fn in (('F', 'F_Mask.gts', 'Soldermask,Top'), ('B', 'B_Mask.gbs', 'Soldermask,Bot')):
        g = Gerber(fn)
        for fp in fps:
            for p in fp.pads:
                if p.kind == 'thru':
                    (g.flash(p.x, p.y, 'R', p.w + 0.1, p.w + 0.1) if p.shape == 'rect' else g.flash(p.x, p.y, 'C', p.w + 0.1))
                else:
                    g.flash(p.x, p.y, 'C', p.drill)
        g.save(P(sfx))
    g = Gerber('Legend,Top')
    for fp in fps:
        for (a, b, layer, w) in fp.lines:
            if layer == 'F.SilkS': g.draw([(fp.x + a[0], fp.y + a[1]), (fp.x + b[0], fp.y + b[1])], w)
        for kind, txt, dx, dy, layer, size, ang in fp.texts:
            if layer == 'F.SilkS':
                for pts in text_strokes(txt, fp.x + dx, fp.y + dy, size, 'center', False, ang): g.draw(pts, 0.12)
    for txt, x, y, size, layer, just, gang in gtexts:
        if layer == 'F.SilkS':
            for pts in text_strokes(txt, x, y, size, just or 'center', False, gang): g.draw(pts, 0.12)
    g.save(P('F_Silkscreen.gto'))
    g = Gerber('Legend,Bot')
    for txt, x, y, size, layer, just, gang in gtexts:
        if layer == 'B.SilkS':
            for pts in text_strokes(txt, x, y, size, just or 'center', True, gang): g.draw(pts, 0.12)
    g.save(P('B_Silkscreen.gbo'))
    g = Gerber('Profile,NP')
    for a, b in edges: g.draw([a, b], 0.1)
    g.save(P('Edge_Cuts.gm1'))
    # fori
    tools = {}
    for fp in fps:
        for p in fp.pads:
            tools.setdefault((p.kind, round(p.drill, 3)), []).append((p.x, p.y))
    for vx, vy, vn in vias:
        tools.setdefault(('thru', 0.4), []).append((vx, vy))
    for kind, sfx in (('thru', 'PTH.drl'), ('npth', 'NPTH.drl')):
        sel = sorted(k for k in tools if k[0] == kind)
        o = ['M48', '; DRILL file generato da build_pcb_ponte_p3.py', 'FMAT,2', 'METRIC,TZ']
        for i, k in enumerate(sel, 1): o.append(f'T{i}C{k[1]:.3f}')
        o += ['%', 'G90', 'G05']
        for i, k in enumerate(sel, 1):
            o.append(f'T{i}')
            for x, y in tools[k]: o.append(f'X{x:.3f}Y{H - y:.3f}')
        o.append('M30')
        open(P(sfx), 'w', encoding='utf8').write('\n'.join(o) + '\n')

def write_pdf(svgs, pdf, chrome='/usr/bin/google-chrome'):
    """Stampa 1:1 con Chrome headless (pagina grande quanto la scheda)."""
    import subprocess, tempfile
    html = ('<!doctype html><meta charset=utf-8><style>@page{size:%smm %smm;margin:0}html,body{margin:0}'
            'svg{display:block;page-break-after:always}</style>' % (W, H)) + ''.join(open(sv, encoding='utf8').read() for sv in svgs)
    tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf8'); tmp.write(html); tmp.close()
    subprocess.run([chrome, '--headless=new', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer',
                    f'--print-to-pdf={pdf}', 'file://' + tmp.name], check=True, capture_output=True)
    os.unlink(tmp.name)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), NAME)
    os.makedirs(out, exist_ok=True)
    errs, info = run_checks()
    print('\n'.join(info))
    print('ERRORI:', len(errs))
    for e in errs: print('  ', e)
    if errs:
        raise SystemExit('Generazione interrotta: correggere gli errori prima di scrivere i file.')
    write_pcb(os.path.join(out, NAME + '.kicad_pcb'))
    write_library(os.path.join(out, 'Simulatore.pretty'))
    write_project(out)
    write_bom(out)
    if '--stampe-proprie' in sys.argv:   # Gerber/anteprime di prova generati dallo script (quelli ufficiali vengono da kicad-cli)
        write_svg(os.path.join(out, 'anteprima_lato_componenti.svg'), 'top')
        write_svg(os.path.join(out, 'anteprima_lato_rame.svg'), 'bottom')
        write_gerbers(os.path.join(out, 'gerber_script'))
        st = os.path.join(out, 'stampa_1a1_script'); os.makedirs(st, exist_ok=True)
        write_master_svg(os.path.join(st, 'rame_lato_componenti.svg'), 'F.Cu', False)
        write_master_svg(os.path.join(st, 'rame_lato_saldature_SPECCHIATO.svg'), 'B.Cu', True)
    print('scritti i file in', out)


