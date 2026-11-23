#!/usr/bin/env python3
"""Controlli statici sui file reali; non sostituisce ERC/DRC di KiCad."""
import json
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'pcb'))
import build_pcb_ponte_p3 as model


def parse(path):
    tokens = re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+', Path(path).read_text())
    stack, top = [], []
    cur = top
    for t in tokens:
        if t == '(':
            child = []
            cur.append(child)
            stack.append(cur)
            cur = child
        elif t == ')':
            cur = stack.pop()
        else:
            cur.append(json.loads(t) if t.startswith('"') else t)
    assert not stack
    return top[0]


def children(x, name):
    return [v for v in x if isinstance(v, list) and v and v[0] == name]


def one(x, name):
    return children(x, name)[0]


def xy(x):
    return tuple(round(float(v), 6) for v in x[1:3])


def board(path):
    doc = parse(path)
    pins, fps, segments, vias = {}, {}, [], []
    nets = {n[1]: n[2] for n in children(doc, 'net')}
    for fp in children(doc, 'footprint') + children(doc, 'module'):
        ref = next(t[2] for t in children(fp, 'fp_text') if t[1] == 'reference')
        at = one(fp, 'at')
        assert len(at) == 3, 'Rotazione footprint non gestita'
        x, y = xy(at)
        fps[ref] = fp[1]
        for pad in children(fp, 'pad'):
            if pad[2] == 'np_thru_hole':
                continue
            px, py = xy(one(pad, 'at'))
            pins[ref+'.'+pad[1]] = (one(pad, 'net')[2], round(x+px,6), round(y+py,6),
                                    xy(one(pad, 'size')), float(one(pad, 'drill')[1]))
    for s in children(doc, 'segment'):
        segments.append((one(s, 'layer')[1], nets[one(s, 'net')[1]],
                         tuple(sorted((xy(one(s, 'start')), xy(one(s, 'end'))))),
                         float(one(s, 'width')[1])))
    for v in children(doc, 'via'):
        vias.append((xy(one(v, 'at')), nets[one(v, 'net')[1]],
                     float(one(v, 'size')[1]), float(one(v, 'drill')[1])))
    return doc, pins, fps, sorted(segments), sorted(vias)


def schematic(path):
    doc = parse(path)
    wires = [tuple(xy(p) for p in one(w, 'pts')[1:]) for w in children(doc, 'wire')]
    labels = [(xy(one(l, 'at')), l[1]) for l in children(doc, 'global_label')]
    libs = {s[1]: s for s in children(one(doc, 'lib_symbols'), 'symbol')}
    pins = {}
    fps = {}
    for s in children(doc, 'symbol'):
        props = {p[1]: p[2] for p in children(s, 'property')}
        ref = props['Reference']
        fps[ref] = props['Footprint']
        at = one(s, 'at'); x,y = xy(at); angle = math.radians(float(at[3]))
        mirror = children(s, 'mirror')
        for sub in children(libs[one(s, 'lib_id')[1]], 'symbol'):
            for p in children(sub, 'pin'):
                px, py = xy(one(p, 'at'))
                if mirror and mirror[0][1] == 'y': px = -px
                if mirror and mirror[0][1] == 'x': py = -py
                pos = (round(x+px*math.cos(angle)-py*math.sin(angle),6),
                       round(y-px*math.sin(angle)-py*math.cos(angle),6))
                pins[ref+'.'+one(p, 'number')[1]] = pos
    return pins, fps, wire_nets(wires, labels, pins)


def wire_nets(wires, labels, pins):
    parent = {}
    def root(n):
        parent.setdefault(n,n)
        if parent[n] != n: parent[n] = root(parent[n])
        return parent[n]
    def union(a,b): parent[root(a)] = root(b)
    points = {p for w in wires for p in w} | set(pins.values()) | {p for p,_ in labels}
    for a,b in wires:
        union(a,b)
        for p in points:
            if model.pseg(p,a,b) < 1e-5: union(a,p)
    names = {}
    for p,name in labels:
        names.setdefault(root(p),set()).add(name)
    result = {}
    for pin,p in pins.items():
        ns = names.get(root(p), set())
        assert len(ns) == 1, (pin,ns)
        result[pin] = next(iter(ns))
    return result


def legacy(path):
    text = Path(path).read_text()
    lib = Path(str(path).replace('.sch','-cache.lib')).read_text()
    defs = {}
    for name, body in re.findall(r'^DEF (\S+)[^\n]*\n(.*?)^ENDDEF',lib,re.M|re.S):
        defs[name] = [(v[2], int(v[3]), int(v[4])) for l in body.splitlines()
                      if (v:=l.split()) and v[0]=='X']
    pins = {}
    for body in re.findall(r'\$Comp\n(.*?)\$EndComp',text,re.S):
        name,ref = re.search(r'^L (\S+) (\S+)',body,re.M).groups()
        # KiCad legacy cache resolves library:name as library_name.
        key = name.replace(':','_')
        x,y = map(int,re.search(r'^P (\d+) (\d+)',body,re.M).groups())
        a,b,c,d = map(int,body.strip().splitlines()[-1].split())
        for num,px,py in defs[key]:
            pins[ref+'.'+num] = (x+a*px+b*py,y+c*px+d*py)
    wires = [((int(a),int(b)),(int(c),int(d))) for a,b,c,d in
             re.findall(r'Wire Wire Line\s+(\d+) (\d+) (\d+) (\d+)',text)]
    labels = [((int(x),int(y)),name) for x,y,name in
              re.findall(r'Text GLabel (\d+) (\d+)[^\n]*\n([^\n]+)',text)]
    return wire_nets(wires,labels,pins)


def report():
    base = ROOT/'pcb'/model.NAME/model.NAME
    doc,pins,fps,segments,vias = board(base.with_suffix('.kicad_pcb'))
    expected = {p.ref+'.'+p.num:(p.net,round(p.x+model.OX,6),round(p.y+model.OY,6),
                               (p.w,p.h),p.drill)
                for fp in model.fps for p in fp.pads if p.kind=='thru'}
    assert pins == expected, 'Pad/reti diversi dal modello'
    expected_segments = sorted((t.layer,t.net,tuple(sorted(((round(a[0]+model.OX,6),round(a[1]+model.OY,6)),
                                                          (round(b[0]+model.OX,6),round(b[1]+model.OY,6))))),t.w)
                               for t in model.tracks for a,b in zip(t.pts[:-1],t.pts[1:]))
    assert segments == expected_segments, 'Piste diverse dal modello'
    assert vias == sorted(((round(x+model.OX,6),round(y+model.OY,6)),n,model.VIA_D,model.VIA_DRILL)
                          for x,y,n in model.vias)
    errors,details = model.run_checks()
    assert not errors, errors
    _,sch_fps,sch_nets = schematic(base.with_suffix('.kicad_sch'))
    assert sch_nets == {k:v[0] for k,v in pins.items()}, 'Schema/PCB: reti diverse'
    assert sch_fps == fps, 'Schema/PCB: footprint diversi'
    legacy_base = ROOT/'pcb/easyeda'/model.NAME
    _,lp,lf,ls,lv = board(legacy_base.with_suffix('.kicad_pcb'))
    assert (pins,fps,segments,vias) == (lp,lf,ls,lv), 'PCB legacy diverso'
    assert legacy(legacy_base.with_suffix('.sch')) == sch_nets, 'Schema legacy diverso'
    return {'pin_verificati':len(pins), 'componenti_inclusi_fori':len(fps),
            'segmenti':len(segments),'vie':len(vias),'errori_controlli_geometrici_python':errors,
            'reti_schema_pcb_legacy':'coincidenti', 'dettagli':details,
            'limiti':'Controlli statici Python; ERC/DRC KiCad e importazione EasyEDA non eseguiti in questa revisione.'}


if __name__ == '__main__':
    print(json.dumps(report(),indent=2,ensure_ascii=False))
