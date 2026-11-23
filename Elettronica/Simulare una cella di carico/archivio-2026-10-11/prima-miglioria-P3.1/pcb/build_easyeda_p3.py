#!/usr/bin/env python3
# build_easyeda_p3.py — esporta scheda e schema nel vecchio formato KiCad 5.1 per l'importazione in EasyEDA
# (la documentazione EasyEDA dichiara KiCad 5.1/5.9; il formato KiCad 7 non è tra quelli dichiarati).
# Scrive in easyeda/: .kicad_pcb (v20171130), .sch (v4), -cache.lib, .pro. Uso: python3 build_easyeda_p3.py
import os, sys, uuid
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pcb_ponte_p3 as P
import build_sch_ponte_p3 as S

HERE = os.path.dirname(os.path.abspath(__file__))
NAME = 'simulatore_ponte_348_p3'
OUT = os.path.join(HERE, 'easyeda')
os.makedirs(OUT, exist_ok=True)
f = P.f

def q(s):
    return '"' + s.replace('"', "'") + '"'

# ------------------------------------------------------------------ scheda KiCad 5.1
def pcb51():
    o = ['(kicad_pcb (version 20171130) (host pcbnew 5.1.12)\n\n']
    ndraw = len(P.edges) + len(P.gtexts)
    o.append(f'  (general\n    (thickness 1.6)\n    (drawings {ndraw})\n    (tracks {sum(len(t.pts) - 1 for t in P.tracks) + len(P.vias)})\n'
             f'    (zones 0)\n    (modules {len(P.fps)})\n    (nets {len(P.NETS) + 1})\n  )\n\n  (page A4)\n  (layers\n')
    for n, nm, t in ((0, 'F.Cu', 'signal'), (31, 'B.Cu', 'signal'), (32, 'B.Adhes', 'user'), (33, 'F.Adhes', 'user'), (34, 'B.Paste', 'user'),
                     (35, 'F.Paste', 'user'), (36, 'B.SilkS', 'user'), (37, 'F.SilkS', 'user'), (38, 'B.Mask', 'user'), (39, 'F.Mask', 'user'),
                     (40, 'Dwgs.User', 'user'), (41, 'Cmts.User', 'user'), (42, 'Eco1.User', 'user'), (43, 'Eco2.User', 'user'),
                     (44, 'Edge.Cuts', 'user'), (45, 'Margin', 'user'), (46, 'B.CrtYd', 'user'), (47, 'F.CrtYd', 'user'), (48, 'B.Fab', 'user'), (49, 'F.Fab', 'user')):
        o.append(f'    ({n} {nm} {t})\n')
    o.append('  )\n\n  (setup\n    (last_trace_width 0.3)\n    (trace_clearance 0.2)\n    (zone_clearance 0.508)\n    (zone_45_only no)\n'
             '    (trace_min 0.2)\n    (via_size ' + f(P.VIA_D) + ')\n    (via_drill ' + f(P.VIA_DRILL) + ')\n    (via_min_size 0.4)\n    (via_min_drill 0.3)\n    (uvia_size 0.3)\n'
             '    (uvia_drill 0.1)\n    (uvias_allowed no)\n    (uvia_min_size 0.2)\n    (uvia_min_drill 0.1)\n    (edge_width 0.05)\n'
             '    (segment_width 0.2)\n    (pcb_text_width 0.3)\n    (pcb_text_size 1.5 1.5)\n    (mod_edge_width 0.15)\n    (mod_text_size 1 1)\n'
             '    (mod_text_width 0.15)\n    (pad_size 1.524 1.524)\n    (pad_drill 0.762)\n    (pad_to_mask_clearance 0.051)\n'
             '    (aux_axis_origin 0 0)\n    (visible_elements FFFFFF7F)\n    (pcbplotparams\n      (layerselection 0x010fc_ffffffff)\n'
             '      (usegerberextensions false)\n      (usegerberattributes true)\n      (usegerberadvancedattributes true)\n'
             '      (creategerberjobfile true)\n      (excludeedgelayer true)\n      (linewidth 0.100000)\n      (plotframeref false)\n'
             '      (viasonmask false)\n      (mode 1)\n      (useauxorigin false)\n      (hpglpennumber 1)\n      (hpglpenspeed 20)\n'
             '      (hpglpendiameter 15.000000)\n      (psnegative false)\n      (psa4output false)\n      (plotreference true)\n'
             '      (plotvalue true)\n      (plotinvisibletext false)\n      (padsonsilk false)\n      (subtractmaskfromsilk false)\n'
             '      (outputformat 1)\n      (mirror false)\n      (drillshape 1)\n      (scaleselection 1)\n      (outputdirectory ""))\n  )\n\n  (net 0 "")\n')
    for n in P.NETS:
        o.append(f'  (net {P.NETID[n]} {q(n)})\n')
    o.append('\n  (net_class Default "This is the default net class."\n    (clearance 0.2)\n    (trace_width 0.3)\n    (via_dia ' + f(P.VIA_D) + ')\n'
             '    (via_drill ' + f(P.VIA_DRILL) + ')\n    (uvia_dia 0.3)\n    (uvia_drill 0.1)\n')
    for n in P.NETS:
        o.append(f'    (add_net {q(n)})\n')
    o.append('  )\n\n')
    for fp in P.fps:
        o.append(f'  (module {q("Simulatore:" + fp.lib).strip(chr(34))} (layer F.Cu) (tedit 5F000000) (tstamp {P.sym_uuid(fp.ref)})\n'
                 f'    (at {f(fp.x + P.OX)} {f(fp.y + P.OY)})\n    (path /{P.sym_uuid(fp.ref)})\n')
        for kind, txt, dx, dy, layer, size, ang in fp.texts:
            a = f' {f(ang)}' if ang else ''
            o.append(f'    (fp_text {kind} {q(txt)} (at {f(dx)} {f(dy)}{a}) (layer {layer})\n      (effects (font (size {f(size)} {f(size)}) (thickness {f(P.SILK_T)})))\n    )\n')
        for (a, b, layer, w) in fp.lines:
            o.append(f'    (fp_line (start {f(a[0])} {f(a[1])}) (end {f(b[0])} {f(b[1])}) (layer {layer}) (width {f(w)}))\n')
        for p in fp.pads:
            if p.kind == 'npth':
                o.append(f'    (pad "" np_thru_hole circle (at {f(p.rel[0])} {f(p.rel[1])}) (size {f(p.w)} {f(p.h)}) (drill {f(p.drill)}) (layers *.Cu *.Mask))\n')
            else:
                o.append(f'    (pad {p.num} thru_hole {p.shape} (at {f(p.rel[0])} {f(p.rel[1])}) (size {f(p.w)} {f(p.h)}) (drill {f(p.drill)}) '
                         f'(layers *.Cu *.Mask)\n      (net {P.NETID[p.net]} {q(p.net)}))\n')
        o.append('  )\n\n')
    for a, b in P.edges:
        o.append(f'  (gr_line (start {f(a[0] + P.OX)} {f(a[1] + P.OY)}) (end {f(b[0] + P.OX)} {f(b[1] + P.OY)}) (layer Edge.Cuts) (width 0.05))\n')
    for txt, x, y, size, layer, just, gang in P.gtexts:
        js = ' '.join(filter(None, [just, 'mirror' if layer == 'B.SilkS' else '']))
        a = f' {f(gang)}' if gang else ''
        o.append(f'  (gr_text {q(txt)} (at {f(x + P.OX)} {f(y + P.OY)}{a}) (layer {layer})\n    (effects (font (size {f(size)} {f(size)}) (thickness {f(P.SILK_T)}))'
                 + (f' (justify {js})' if js else '') + ')\n  )\n')
    for t in P.tracks:
        for a, b in zip(t.pts[:-1], t.pts[1:]):
            o.append(f'  (segment (start {f(a[0] + P.OX)} {f(a[1] + P.OY)}) (end {f(b[0] + P.OX)} {f(b[1] + P.OY)}) (width {f(t.w)}) (layer {t.layer}) (net {P.NETID[t.net]}))\n')
    for vx, vy, vn in P.vias:
        o.append(f'  (via (at {f(vx + P.OX)} {f(vy + P.OY)}) (size {f(P.VIA_D)}) (drill {f(P.VIA_DRILL)}) (layers F.Cu B.Cu) (net {P.NETID[vn]}))\n')
    o.append(')\n')
    return ''.join(o)

# ------------------------------------------------------------------ schema legacy (v4) e libreria cache
def mil(v): return int(round(v * 1000 / 25.4))

LIB = {
 'R': dict(pins=[('1', 0, 150, 'D'), ('2', 0, -150, 'U')], draw=['S -40 -100 40 100 0 1 10 N'], fp_h=80),
 'R_H': dict(pins=[('1', 150, 0, 'L'), ('2', -150, 0, 'R')], draw=['S -100 -40 100 40 0 1 10 N'], fp_h=0),
 'POT_WL': dict(pins=[('1', 0, 150, 'D'), ('2', -150, 0, 'R'), ('3', 0, -150, 'U')],
                draw=['S -40 -100 40 100 0 1 10 N', 'P 2 0 1 0 -100 0 -40 0 N'], fp_h=80),
 'CONN_01X06': dict(pins=[(str(k + 1), -200, 200 - 100 * k, 'R') for k in range(6)], draw=['S -150 250 50 -350 0 1 10 f'], fp_h=0),
 'MOUNTINGHOLE': dict(pins=[], draw=['C 0 0 50 0 1 10 N'], fp_h=0),
}
def symname(s):
    if s['lib'] == 'Device:R': return 'R_H' if s['rot'] in (90, 270) else 'R'
    if s['lib'] == 'Device:R_Potentiometer': return 'POT_WL'
    if s['lib'] == 'Connector_Generic:Conn_01x06': return 'CONN_01X06'
    return 'MOUNTINGHOLE'

def cache_lib():
    o = ['EESchema-LIBRARY Version 2.4\n#encoding utf-8\n']
    for nm, d in LIB.items():
        o.append(f'#\n# Simulatore_{nm}\n#\nDEF Simulatore_{nm} {"H" if nm == "MOUNTINGHOLE" else "R"} 0 40 {"Y" if nm != "R_H" else "N"} N 1 F N\n'
                 f'F0 "{"H" if nm == "MOUNTINGHOLE" else ("J" if nm.startswith("CONN") else "R")}" 80 0 50 H V C CNN\nF1 "Simulatore_{nm}" 0 0 50 H V C CNN\n'
                 'F2 "" 0 0 50 H I C CNN\nF3 "" 0 0 50 H I C CNN\nDRAW\n')
        for dr in d['draw']:
            o.append(dr + '\n')
        for (num, x, y, orient) in d['pins']:
            o.append(f'X ~ {num} {x} {y} 0 {orient} 50 50 1 1 P\n')
        o.append('ENDDRAW\nENDDEF\n')
    o.append('#\n#End Library\n')
    return ''.join(o)

def sch51():
    o = ['EESchema Schematic File Version 4\nEELAYER 30 0\nEELAYER END\n$Descr A4 11693 8268\nencoding utf-8\nSheet 1 1\n'
         'Title "Simulatore di cella di carico a ponte 348 ohm"\nDate "2026-10-11"\nRev "P3"\nComp ""\n'
         'Comment1 "Resistenze a foro"\nComment2 "Dispensa: dispensa_simulatore_ponte_348.html"\nComment3 ""\nComment4 ""\n$EndDescr\n']
    for k, s in enumerate(S.symbols):
        nm = symname(s)
        x, y = mil(s['x']), mil(s['y'])
        o.append(f'$Comp\nL Simulatore:{nm} {s["ref"]}\nU 1 1 {P.sym_uuid(s["ref"])[:8].upper()}\nP {x} {y}\n'
                 f'F 0 "{s["ref"]}" H {x + 70} {y - 50} 50  0000 L CNN\nF 1 "{s["value"]}" H {x + 70} {y + 50} 50  0000 L CNN\n'
                 f'F 2 "{s["fp"]}" H {x} {y} 50  0001 C CNN\nF 3 "~" H {x} {y} 50  0001 C CNN\n'
                 f'\t1    {x} {y}\n\t1    0    0    -1  \n$EndComp\n')
    for (a, b, tag) in S.wires:
        o.append(f'Wire Wire Line\n\t{mil(a[0])} {mil(a[1])} {mil(b[0])} {mil(b[1])}\n')
    for (p, tag) in S.junctions:
        o.append(f'Connection ~ {mil(p[0])} {mil(p[1])}\n')
    for (name, p, ang, tag) in S.labels:
        o.append(f'Text GLabel {mil(p[0])} {mil(p[1])} {0 if ang == 0 else 2} 50   Passive ~ 0\n{name}\n')
    o.append('$EndSCHEMATC\n')
    return ''.join(o)

if __name__ == '__main__':
    base = os.path.join(OUT, NAME)
    open(base + '.kicad_pcb', 'w', encoding='utf8').write(pcb51())
    open(base + '.sch', 'w', encoding='utf8').write(sch51())
    open(base + '-cache.lib', 'w', encoding='utf8').write(cache_lib())
    open(base + '.pro', 'w', encoding='utf8').write('update=22/05/2015 07:44:53\nversion=1\nlast_client=kicad\n[general]\nversion=1\nRootSch=\nBoardNm=\n'
                                                      '[pcbnew]\nversion=1\nLastNetListRead=\nUseCmpFile=1\nPadDrill=0.762000000000\nPadDrillOvalY=0.762000000000\n'
                                                      'PadSizeH=1.524000000000\nPadSizeV=1.524000000000\n[eeschema]\nversion=1\nLibDir=\n[eeschema/libraries]\n')
    print('scritti in', OUT)
