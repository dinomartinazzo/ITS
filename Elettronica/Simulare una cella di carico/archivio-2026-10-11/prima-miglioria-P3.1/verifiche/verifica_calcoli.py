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


def circuit(p=0.5, q=0.5, pot=200, r5=3650, r6=71500,
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
        e += [('EP', 'W2', q * 10000), ('W2', 'EM', (1-q)*10000),
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
        exact = (bottom/(top+bottom)-.5)/(3650+zw)/(1/174+1/(3650+zw)+1/74000)
        assert abs(output(p=p)-exact) < 1e-12
    assert abs(rin - 1/(1/348+1/2018+1/10000)) < 1e-8
    assert abs(output(p=0)+output(p=1)) < 1e-12
    assert abs(output()) < 1e-12
    assert abs(output(p=0, open_wiper=True)) < 1e-12
    missed_zero = []
    for factors in itertools.product((.999, 1.001), repeat=4):
        for r7, r8 in itertools.product((909*.99, 909*1.01), repeat=2):
            for r6 in (71500*.99, 71500*1.01):
                kw = dict(bridge=tuple(348*f for f in factors), r7=r7, r8=r8, r6=r6)
                low, high = sorted(output(q=q, **kw) for q in (0, 1))
                residual = max(low, -high, 0)
                if residual > 1e-12:
                    missed_zero.append(residual*1000)
    return {
        'unita': 'ohm, mA, mV/V, percento; modelli ideali, non misure',
        'carico_centro_ohm': rin,
        'carico_estremo_ohm': resistance('EP', 'EM', p=0),
        'corrente_3_2V_mA': 3200/rin, 'corrente_5V_mA': 5000/rin,
        'uscita_eccitazione_cortocircuitata_ohm': rout,
        'uscita_eccitazione_aperta_ohm': resistance('AP', 'AM'),
        'zero_mV_V': output(q=0)*1000,
        'nonlinearita_percento_semifondo_scala': nonlin,
        'punti': [{'p': p, 'mV_V': output(p=p)*1000,
                   'conteggi': output(p=p)*128*2**24} for p in (0,.25,.5,.75,1)],
        'fs_RV1_5_percento': [output(p=0,pot=r)*1000 for r in (190,210)],
        'fs_R5_1_percento': [output(p=0,r5=r)*1000 for r in (3650*.99,3650*1.01)],
        'fs_R5_alternative': {r: output(p=0,r5=r)*1000 for r in (7870,8060,43200)},
        'offset_R7_R8_opposti_mV_V': output(r7=909*.99,r8=909*1.01)*1000,
        'errori_cavo_percento': {r: (output(p=0,cable=r)/fs-1)*100 for r in (.5,1,2)},
        'rumore_termico_nV_radice_Hz': math.sqrt(4*1.380649e-23*300*rout)*1e9,
        'rumore_HX711_50nV_conteggi_a_3_2V': 50e-9/3.2*128*2**24,
        'angoli_tolleranze_zero_esaminati': 128,
        'angoli_zero_non_raggiungibile': len(missed_zero),
        'residuo_zero_massimo_angoli_mV_V': max(missed_zero, default=0),
        'limiti_angoli_zero': 'R1-R4 ±0,1%, R7-R8 ±1%, R6 ±1%; altri nominali, cursori ideali',
        'controlli_analitici': 'superati',
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, ensure_ascii=False))
