#!/usr/bin/env python3
"""Analisi nodale del simulatore passivo; solo libreria standard, nessuna misura hardware."""
import json
import math
import itertools


def solve(edges, fixed):
    # Contrazione dei cortocircuiti, inclusi i cursori ai fine corsa.
    parent = {}
    def root(n):
        parent.setdefault(n, n)
        if parent[n] != n:
            parent[n] = root(parent[n])
        return parent[n]
    for a, b, r in edges:
        if r == 0:
            parent[root(a)] = root(b)
    fixed = {root(n): v for n, v in fixed.items()}
    ee = [(root(a), root(b), r) for a, b, r in edges if r > 0]
    nodes = sorted({n for a, b, _ in ee for n in (a, b)} - fixed.keys())
    idx = {n: i for i, n in enumerate(nodes)}
    mat = [[0.0] * (len(nodes) + 1) for _ in nodes]
    for a, b, r in ee:
        if a == b:
            continue
        for n, other in ((a, b), (b, a)):
            if n not in idx:
                continue
            i = idx[n]
            mat[i][i] += 1 / r
            if other in idx:
                mat[i][idx[other]] -= 1 / r
            else:
                mat[i][-1] += fixed[other] / r
    for k in range(len(nodes)):
        pivot = max(range(k, len(nodes)), key=lambda i: abs(mat[i][k]))
        mat[k], mat[pivot] = mat[pivot], mat[k]
        factor = mat[k][k]
        if abs(factor) < 1e-15:
            raise ValueError('Rete flottante')
        mat[k] = [v / factor for v in mat[k]]
        for i in range(len(nodes)):
            if i != k:
                factor = mat[i][k]
                mat[i] = [x - factor * y for x, y in zip(mat[i], mat[k])]
    v = fixed | {n: mat[i][-1] for n, i in idx.items()}
    return {n: v[root(n)] for a, b, _ in edges for n in (a, b)}


def circuit(p=0.5, q=0.5, pot=200, r5=3650, r6=56000, pot2=10000,
            bridge=(348, 348, 348, 348), r7=909, r8=909,
            cable=0, zero=True, open_wiper=False):
    r1, r2, r3, r4 = bridge
    e = [('XP', 'EP', cable), ('XM', 'EM', cable),
         ('EP', 'AP', r1), ('AP', 'EM', r2),
         ('EP', 'AM', r3), ('AM', 'EM', r4),
         ('EP', 'N1', r7), ('N1', 'W1', p * pot),
         ('W1', 'N2', (1-p) * pot), ('N2', 'EM', r8)]
    if not open_wiper:
        e.append(('W1', 'AP', r5))
    if zero:
        e += [('EP', 'W2', q * pot2), ('W2', 'EM', (1-q)*pot2),
              ('W2', 'AP', r6)]
    return e


def output(**kw):
    v = solve(circuit(**kw), {'XP': 1, 'XM': 0})
    return v['AP'] - v['AM']


def resistance(a, b, short_exc=False, **kw):
    edges = circuit(**kw)
    if short_exc:
        edges += [('EP', 'EM', 0)]
    v = solve(edges, {a: 1, b: 0})
    # Use ports with no zero-ohm incident edges for current calculation.
    current = sum((v[a]-v[y])/r if x == a else (v[a]-v[x])/r
                  for x, y, r in edges if r > 0 and a in (x, y))
    return 1/current


def zero_corners(r6_nominal, divider_tolerance):
    missed, margins, max_offset = [], [], 0
    cases = 0
    for f in itertools.product((-1, 1), repeat=10):
        kw = dict(bridge=tuple(348*(1+.001*s) for s in f[:4]),
                  r7=909*(1+divider_tolerance*f[4]),
                  r8=909*(1+divider_tolerance*f[5]),
                  r6=r6_nominal*(1+.01*f[6]) + 110,
                  r5=3650*(1+.001*f[7]), pot=200*(1+.05*f[8]),
                  pot2=10000*(1+.10*f[9]))
        low, high = sorted(output(q=q, **kw) for q in (.01, .99))
        margins.append(min(-low, high)*1000)
        if low > 0 or high < 0:
            missed.append(max(low, -high)*1000)
        max_offset = max(max_offset, abs(output(**kw))*1000)
        cases += 1
    return dict(casi=cases, zero_non_raggiungibile=len(missed),
                margine_minimo_mV_V=min(margins),
                offset_centro_massimo_mV_V=max_offset,
                residuo_massimo_mV_V=max(missed,default=0))


def report():
    fs = output(p=0)
    rin = resistance('EP', 'EM')
    rout = resistance('AP', 'AM', short_exc=True)
    points = [output(p=i/1000) for i in range(1001)]
    nonlin = max(abs(v - fs*(1-2*i/1000)) for i, v in enumerate(points)) / fs * 100
    # Cross-check against independent Thevenin reduction.
    for p in (0, .25, .5, .75, 1):
        top, bottom = 909+p*200, 909+(1-p)*200
        zw = top*bottom/(top+bottom)
        exact = (bottom/(top+bottom)-.5)/(3650+zw)/(1/174+1/(3650+zw)+1/58500)
        assert abs(output(p=p)-exact) < 1e-12
    assert abs(rin - 1/(1/348+1/2018+1/10000)) < 1e-8
    assert abs(output(p=0)+output(p=1)) < 1e-12
    assert abs(output()) < 1e-12
    assert abs(output(p=0, open_wiper=True)) < 1e-12
    # Riduzione indipendente anche fuori centro e con ponte disadattato.
    for p in (.1, .4, .9):
        for q in (.01, .37, .99):
            br = (347.652, 348.348, 348.348, 347.652)
            a, b = 909 + p*200, 909 + (1-p)*200
            g_signal = 1/(3650 + a*b/(a+b))
            g_zero = 1/(56000 + q*(1-q)*10000)
            ap = (1/br[0] + b/(a+b)*g_signal + (1-q)*g_zero) / (1/br[0]+1/br[1]+g_signal+g_zero)
            am = br[3]/(br[2]+br[3])
            assert abs(output(p=p,q=q,bridge=br) - (ap-am)) < 1e-12
    for rc in (.5, 1, 2):
        v = solve(circuit(p=0,cable=rc), {'XP':1,'XM':0})
        # Un riferimento prelevato ai nodi del ponte elimina la caduta nel modello resistivo.
        assert abs((v['AP']-v['AM'])/(v['EP']-v['EM']) - fs) < 1e-12
    improved = zero_corners(56000, .001)
    assert improved['zero_non_raggiungibile'] == 0
    return {
        'unita': 'ohm, mA, mV/V, percento; modelli ideali, non misure',
        'revisione_elettrica': 'P3.1, R6=56 kohm 1%, R7/R8=909 ohm 0,1%',
        'carico_centro_ohm': rin,
        'carico_estremo_ohm': resistance('EP', 'EM', p=0),
        'corrente_3_2V_mA': 3200/rin, 'corrente_5V_mA': 5000/rin,
        'uscita_eccitazione_cortocircuitata_ohm': rout,
        'uscita_eccitazione_aperta_ohm': resistance('AP', 'AM'),
        'zero_mV_V': output(q=0)*1000,
        'nonlinearita_percento_semifondo_scala': nonlin,
        'nonlinearita_percento_escursione_totale': nonlin/2,
        'punti': [{'p': p, 'mV_V': output(p=p)*1000,
                   'conteggi': output(p=p)*128*2**24} for p in (0,.25,.5,.75,1)],
        'fs_RV1_5_percento': [output(p=0,pot=r)*1000 for r in (190,210)],
        'fs_R5_1_percento': [output(p=0,r5=r)*1000 for r in (3650*.99,3650*1.01)],
        'fs_R5_alternative': {r: output(p=0,r5=r)*1000 for r in (7870,8060,43200)},
        'offset_R7_R8_opposti_mV_V': output(r7=909*.999,r8=909*1.001)*1000,
        'errori_cavo_percento': {r: (output(p=0,cable=r)/fs-1)*100 for r in (.5,1,2)},
        'rumore_termico_nV_radice_Hz': math.sqrt(4*1.380649e-23*300*rout)*1e9,
        'rumore_HX711_50nV_conteggi_a_3_2V': 50e-9/3.2*128*2**24,
        'confronto_zero_angoli': {'P3': zero_corners(71500, .01), 'P3.1': improved},
        'limiti_angoli_zero': 'R1-R4 e R5 ±0,1%, R6 ±1%, RV1 ±5% ipotizzato, RV2 ±10%; '
                             'R7/R8 ±1% P3 o ±0,1% P3.1. RV1 al centro elettrico; '
                             'RV2 corsa 1–99%, 110 ohm aggiunti a R6 come margine sul contatto. '
                             'Sweep agli estremi delle tolleranze, non prova hardware né garanzia di tutti i casi intermedi.',
        'controlli_analitici': 'superati',
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, ensure_ascii=False))
