"""Test di filtri_core e serie. Esecuzione dalla radice del progetto:

    python3 -m unittest discover -s tests -v
"""
import math
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import filtri_cli  # noqa: E402
import filtri_core as fc  # noqa: E402
import serie  # noqa: E402


class TestSerie(unittest.TestCase):
    def test_numero_valori(self):
        self.assertEqual((len(serie.E12), len(serie.E24), len(serie.E96)), (12, 24, 96))

    def test_crescenti_e_nella_decade(self):
        for nome, valori in serie.SERIE.items():
            with self.subTest(nome):
                self.assertEqual(list(valori), sorted(valori))
                self.assertGreaterEqual(valori[0], 1.0)
                self.assertLess(valori[-1], 10.0)

    def test_e96_vicina_alla_progressione_geometrica(self):
        # la serie ufficiale non è un arrotondamento perfetto, ma resta entro l'1% del valore ideale
        for i, m in enumerate(serie.E96):
            self.assertAlmostEqual(m / 10.0 ** (i / 96.0), 1.0, delta=0.01)

    def test_arrotonda(self):
        self.assertEqual(fc.arrotonda_serie(1234.0, "E96"), 1240.0)
        self.assertEqual(fc.arrotonda_serie(0.0147, "E24"), 0.015)
        self.assertAlmostEqual(fc.arrotonda_serie(9.9, "E12"), 10.0)

    def test_arrotonda_per_eccesso(self):
        self.assertAlmostEqual(fc.arrotonda_serie_per_eccesso(68.3e-9, "E12"), 82e-9)
        self.assertAlmostEqual(fc.arrotonda_serie_per_eccesso(47e-9, "E12"), 47e-9)

    def test_valore_non_positivo(self):
        with self.assertRaises(ValueError):
            fc.arrotonda_serie(0.0)


class TestPassivi(unittest.TestCase):
    def test_rc_a_fc(self):
        f = fc.rc_fc(1.6e3, 100e-9)
        h = fc.h_rc_lp(f, f)
        self.assertAlmostEqual(abs(h), 1 / math.sqrt(2), places=12)
        self.assertAlmostEqual(fc.fase_gradi(h), -45.0, places=9)
        self.assertAlmostEqual(fc.db(h), -3.0103, places=4)

    def test_hp_complementare_a_lp_in_potenza(self):
        for x in (0.1, 1.0, 7.0):
            m2 = abs(fc.h_rc_lp(x, 1.0)) ** 2 + abs(fc.h_rc_hp(x, 1.0)) ** 2
            self.assertAlmostEqual(m2, 1.0, places=12)

    def test_carico_resistivo(self):
        r, c = 1e3, 100e-9
        h0 = fc.h_rc_lp_caricato(0.0, r, c, r)
        self.assertAlmostEqual(abs(h0), 0.5, places=12)
        # fc con carico = 1/(2 pi (R||RL) C): raddoppia se RL = R
        self.assertAlmostEqual(abs(fc.h_rc_lp_caricato(2 * fc.rc_fc(r, c), r, c, r)),
                               0.5 / math.sqrt(2), places=12)

    def test_cascata_rc_non_e_prodotto_di_celle_isolate(self):
        r, c = 1e3, 100e-9
        f = fc.rc_fc(r, c)
        isolato = abs(fc.h_rc_lp(f, f)) ** 2
        collegato = abs(fc.h_rc_lp_doppio(f, r, c, r, c))
        self.assertLess(collegato, isolato)
        # con celle uguali il polinomio è 1 + 3 sRC + (sRC)^2: a w = 1/RC il modulo vale 1/3
        self.assertAlmostEqual(collegato, 1.0 / 3.0, places=12)

    def test_rlc(self):
        rl = fc.RlcSerie(r=10.0, l=10e-3, c=100e-9)
        self.assertAlmostEqual(rl.f0, 1.0 / (2 * math.pi * math.sqrt(10e-3 * 100e-9)), places=6)
        self.assertAlmostEqual(rl.q, math.sqrt(10e-3 / 100e-9) / 10.0, places=9)
        self.assertAlmostEqual(abs(rl.h(rl.f0)), 1.0, places=9)
        # ai bordi della banda il modulo vale 1/sqrt(2)
        w0 = 2 * math.pi * rl.f0
        a = rl.r / (2 * rl.l)
        f1 = (-a + math.sqrt(a * a + w0 * w0)) / (2 * math.pi)
        self.assertAlmostEqual(abs(rl.h(f1)), 1 / math.sqrt(2), places=9)


class TestSecondoOrdine(unittest.TestCase):
    def test_lp_in_f0(self):
        for q in (0.5, 0.7071, 2.0):
            self.assertAlmostEqual(abs(fc.h2_lp(1.0, 1.0, q)), q, places=12)

    def test_picco(self):
        for q in (1.0, 1.3066, 5.0):
            m, _ = fc.picco_e_frequenza(lambda f: fc.h2_lp(f, 1.0, q), 0.01, 10.0, 20000)
            self.assertAlmostEqual(m, fc.picco_h2_lp(q), places=4)
        self.assertEqual(fc.picco_h2_lp(0.5), 1.0)

    def test_hp_asintoto(self):
        self.assertAlmostEqual(abs(fc.h2_hp(1e4, 1.0, 1.0, 2.0)), 2.0, places=6)


class TestSallenKey(unittest.TestCase):
    def test_lp_unitario_formula_vs_nodale(self):
        f0, q = 1000.0, 0.7071
        c2 = 10e-9
        c1 = 22e-9
        r1, r2 = fc.sk_lp_unitario(f0, q, c1, c2)
        f0e, qe = fc.sk_f0_q_unitario(r1, r2, c1, c2)
        self.assertAlmostEqual(f0e, f0, places=6)
        self.assertAlmostEqual(qe, q, places=9)
        for f in (10.0, 300.0, 1000.0, 3000.0, 20000.0):
            nodale = fc.h_sk_lp(f, r1, r2, c1, c2)
            canonica = fc.h2_lp(f, f0, q)
            self.assertAlmostEqual(abs(nodale - canonica), 0.0, places=9)

    def test_lp_unitario_c1_troppo_piccolo(self):
        with self.assertRaises(ValueError):
            fc.sk_lp_unitario(1000.0, 1.3066, 22e-9, 10e-9)

    def test_lp_componenti_uguali(self):
        f0, q, c = 1000.0, 2.0, 10e-9
        r, k, rf_rg = fc.sk_guadagno_componenti_uguali(f0, q, c)
        self.assertAlmostEqual(k, 3 - 1 / q, places=12)
        self.assertAlmostEqual(rf_rg, k - 1, places=12)
        for f in (100.0, 1000.0, 5000.0):
            nodale = fc.h_sk_lp(f, r, r, c, c, k)
            canonica = fc.h2_lp(f, f0, q, k)
            self.assertAlmostEqual(abs(nodale - canonica), 0.0, places=9)

    def test_hp_componenti_uguali(self):
        f0, q, c = 1000.0, 1.0, 10e-9
        r, k, _ = fc.sk_guadagno_componenti_uguali(f0, q, c)
        for f in (100.0, 1000.0, 5000.0):
            nodale = fc.h_sk_hp(f, r, r, c, c, k)
            canonica = fc.h2_hp(f, f0, q, k)
            self.assertAlmostEqual(abs(nodale - canonica), 0.0, places=9)

    def test_q_minimo_componenti_uguali(self):
        with self.assertRaises(ValueError):
            fc.sk_guadagno_componenti_uguali(1000.0, 0.4, 10e-9)

    def test_gbw_infinito_equivale_ideale(self):
        r1, r2 = fc.sk_lp_unitario(1000.0, 1.3066, 100e-9, 10e-9)
        ideale = fc.h_sk_lp(1000.0, r1, r2, 100e-9, 10e-9)
        reale = fc.h_sk_lp(1000.0, r1, r2, 100e-9, 10e-9, gbw=1e15)
        self.assertAlmostEqual(abs(ideale - reale), 0.0, places=9)

    def test_gbw_finito_alza_il_picco_di_q_alto(self):
        r1, r2 = fc.sk_lp_unitario(1000.0, 1.3066, 100e-9, 10e-9)
        ideale = abs(fc.h_sk_lp(1000.0, r1, r2, 100e-9, 10e-9))
        reale = abs(fc.h_sk_lp(1000.0, r1, r2, 100e-9, 10e-9, gbw=10e3))
        self.assertNotAlmostEqual(ideale, reale, places=2)

    def test_progetto_normalizzato_vicino_all_obiettivo(self):
        s = fc.progetta_sezione_sk(1000.0, 0.7071, 10e-9)
        self.assertAlmostEqual(s.f0 / 1000.0, 1.0, delta=0.03)
        self.assertAlmostEqual(s.q / 0.7071, 1.0, delta=0.05)


class TestFamiglie(unittest.TestCase):
    def test_butterworth_q(self):
        self.assertAlmostEqual(fc.butterworth(2)[0].q, 1 / math.sqrt(2), places=12)
        q4 = sorted(s.q for s in fc.butterworth(4))
        self.assertAlmostEqual(q4[0], 0.5412, places=4)
        self.assertAlmostEqual(q4[1], 1.3066, places=4)
        q3 = fc.butterworth(3)
        self.assertEqual([s.ordine for s in q3], [2, 1])
        self.assertAlmostEqual(q3[0].q, 1.0, places=12)

    def test_butterworth_a_fc_e_pendenza(self):
        for n in (1, 2, 3, 4, 5, 6):
            sez = fc.butterworth(n, 1.0)
            self.assertAlmostEqual(abs(fc.risposta_cascata(sez, 1.0)), 1 / math.sqrt(2), places=9)
            # a 10 fc l'attenuazione approssima 20 n dB
            self.assertAlmostEqual(-fc.db(fc.risposta_cascata(sez, 10.0)), 20 * n, delta=0.05)

    def test_chebyshev_ripple(self):
        for n, r in ((3, 1.0), (4, 1.0), (4, 0.5), (5, 3.0)):
            sez = fc.chebyshev(n, r, 1.0)
            m = [abs(fc.risposta_cascata(sez, f)) for f in fc.griglia_log(0.01, 1.0, 4000)]
            self.assertAlmostEqual(20 * math.log10(max(m) / min(m)), r, places=2)

    def test_bessel2(self):
        s = fc.bessel2(1.0)
        self.assertAlmostEqual(s.q, 1 / math.sqrt(3), places=12)
        self.assertAlmostEqual(abs(fc.h2_lp(1.0, s.f0, s.q)), 1 / math.sqrt(2), places=9)

    def test_cascata_reale_butterworth(self):
        sez = fc.progetta_cascata_butterworth_lp(4, 1000.0, 10e-9)
        self.assertEqual(len(sez), 2)
        h = abs(fc.risposta_cascata_reale(sez, 1000.0))
        self.assertAlmostEqual(fc.db(h), -3.01, delta=0.6)

    def test_cascata_dispari_ha_cella_rc(self):
        sez = fc.progetta_cascata_butterworth_lp(3, 1000.0, 10e-9)
        self.assertIsInstance(sez[-1], fc.SezioneRc1)


class TestTempoEPoli(unittest.TestCase):
    def test_gradino_primo_ordine(self):
        f0 = 1.0 / (2 * math.pi)  # tau = 1 s
        r = fc.risposta_gradino([fc.Sezione(1, f0)], 5.0, punti=500)
        for t, y in r[::100]:
            self.assertAlmostEqual(y, 1 - math.exp(-t), places=6)

    def test_gradino_secondo_ordine_sovraelongazione(self):
        for q in (0.7071, 1.0, 2.0):
            f0 = 1.0 / (2 * math.pi)  # w0 = 1 rad/s
            r = fc.risposta_gradino([fc.Sezione(2, f0, q)], 40.0, punti=4000)
            picco = max(y for _, y in r) - 1.0
            self.assertAlmostEqual(picco, fc.sovraelongazione_h2(q), places=4)
            self.assertAlmostEqual(r[-1][1], 1.0, places=3)

    def test_nessuna_sovraelongazione_sotto_q_critico(self):
        self.assertEqual(fc.sovraelongazione_h2(0.5), 0.0)
        self.assertEqual(fc.sovraelongazione_h2(0.3), 0.0)

    def test_gradino_cascata_valore_finale(self):
        sez = fc.butterworth(4, 1.0)
        r = fc.risposta_gradino(sez, 3.0, punti=600)
        self.assertAlmostEqual(r[-1][1], 1.0, places=2)

    def test_poli_butterworth_su_circonferenza(self):
        for n in (2, 3, 4, 5):
            for s in fc.butterworth(n, 1.0):
                for sigma, omega in fc.poli_sezione(s):
                    self.assertAlmostEqual(math.hypot(sigma, omega), 1.0, places=12)
                    self.assertLessEqual(sigma, 0.0)

    def test_poli_chebyshev_su_ellisse(self):
        # per Chebyshev i poli stanno sull'ellisse sigma^2/sinh^2(a) + omega^2/cosh^2(a) = 1
        n, r = 4, 1.0
        eps = math.sqrt(10 ** (r / 10) - 1)
        a = math.asinh(1 / eps) / n
        for s in fc.chebyshev(n, r, 1.0):
            for sigma, omega in fc.poli_sezione(s):
                self.assertAlmostEqual(sigma ** 2 / math.sinh(a) ** 2 + omega ** 2 / math.cosh(a) ** 2, 1.0, places=9)

    def test_poli_q_basso(self):
        with self.assertRaises(ValueError):
            fc.poli_sezione(fc.Sezione(2, 1.0, 0.4))

    def test_ritardo_gruppo_primo_ordine(self):
        # tau_g = tau / (1 + (f/fc)^2); a bassa frequenza tau_g = tau = 1/(2 pi fc)
        f0 = 1000.0
        self.assertAlmostEqual(fc.ritardo_gruppo([fc.Sezione(1, f0)], 1.0) * 2 * math.pi * f0, 1.0, places=4)
        self.assertAlmostEqual(fc.ritardo_gruppo([fc.Sezione(1, f0)], f0) * 2 * math.pi * f0, 0.5, places=4)

    def test_bessel_ritardo_piu_piatto_di_butterworth(self):
        be, bw = fc.bessel2(1.0), fc.butterworth(2, 1.0)[0]
        r0_be = fc.ritardo_gruppo([be], 0.01)
        r0_bw = fc.ritardo_gruppo([bw], 0.01)
        scarto_be = abs(fc.ritardo_gruppo([be], 0.5) / r0_be - 1)
        scarto_bw = abs(fc.ritardo_gruppo([bw], 0.5) / r0_bw - 1)
        self.assertLess(scarto_be, scarto_bw)


class TestFamiglieEstese(unittest.TestCase):
    def test_coefficienti_bessel(self):
        self.assertEqual(fc.coefficienti_bessel(2), [3, 3, 1])
        self.assertEqual(fc.coefficienti_bessel(3), [15, 15, 6, 1])
        self.assertEqual(fc.coefficienti_bessel(4), [105, 105, 45, 10, 1])

    def test_bessel_q_noti(self):
        # valori delle tabelle di progetto (indipendenti dalla normalizzazione di frequenza)
        self.assertAlmostEqual(fc.bessel(2)[0].q, 0.5774, places=4)
        self.assertAlmostEqual(fc.bessel(3)[0].q, 0.6910, places=4)
        q4 = sorted(s.q for s in fc.bessel(4))
        self.assertAlmostEqual(q4[0], 0.5219, places=4)
        self.assertAlmostEqual(q4[1], 0.8055, places=4)

    def test_bessel_2_coincide_con_bessel2(self):
        a, b = fc.bessel(2)[0], fc.bessel2(1.0)
        self.assertAlmostEqual(a.f0, b.f0, places=6)
        self.assertAlmostEqual(a.q, b.q, places=9)

    def test_bessel_meno_3_db_a_fc(self):
        for n in range(2, 8):
            sez = fc.bessel(n, 1.0)
            self.assertAlmostEqual(fc.db(fc.risposta_cascata(sez, 1.0)), -3.0103, places=3)

    def test_bessel_ritardo_costante(self):
        sez = fc.bessel(4, 1.0)
        r0 = fc.ritardo_gruppo(sez, 0.01)
        self.assertLess(abs(fc.ritardo_gruppo(sez, 0.4) / r0 - 1), 0.01)
        bw = fc.butterworth(4, 1.0)
        self.assertGreater(abs(fc.ritardo_gruppo(bw, 0.4) / fc.ritardo_gruppo(bw, 0.01) - 1), 0.05)

    def test_f3db_chebyshev_formula(self):
        for n, r in ((3, 1.0), (4, 1.0), (4, 0.5), (5, 3.0)):
            sez = fc.chebyshev(n, r, 1.0)
            self.assertAlmostEqual(fc.f_3db(sez, riferimento="picco"), fc.chebyshev_f3db_su_fc(n, r), places=4)

    def test_f3db_butterworth(self):
        for n in (1, 3, 4):
            self.assertAlmostEqual(fc.f_3db(fc.butterworth(n, 2.0)), 2.0, places=5)

    def test_polinomio_chebyshev(self):
        self.assertAlmostEqual(fc.polinomio_chebyshev(2, 0.3), 2 * 0.3 ** 2 - 1, places=12)
        self.assertAlmostEqual(fc.polinomio_chebyshev(4, 0.5), 8 * 0.5 ** 4 - 8 * 0.5 ** 2 + 1, places=12)
        for x in (-1.0, -0.4, 0.2, 1.0):
            self.assertLessEqual(abs(fc.polinomio_chebyshev(5, x)), 1.0 + 1e-12)

    def test_ordine_minimo(self):
        for att, rapp in ((20, 2.0), (40, 2.0), (60, 3.0)):
            nb = fc.ordine_minimo("butterworth", att, rapp)
            nc = fc.ordine_minimo("chebyshev", att, rapp)
            ne = fc.ordine_minimo("bessel", att, rapp, n_max=12)
            self.assertLessEqual(nc, nb)
            if ne is not None:  # il Bessel tende a una gaussiana e a volte non raggiunge la specifica
                self.assertGreaterEqual(ne, nb)
            # l'ordine trovato rispetta la specifica e quello inferiore no
            self.assertGreaterEqual(fc.attenuazione_db(fc.butterworth(nb, 1.0), rapp), att)
            self.assertLess(fc.attenuazione_db(fc.butterworth(nb - 1, 1.0), rapp), att)

    def test_fase_cascata_sezioni_teoriche_passa_basso(self):
        # la fase di un passa-basso parte da 0 e scende verso -90 gradi per ogni polo
        for sez in (fc.butterworth(4, 1.0), fc.bessel(4, 1.0), fc.chebyshev(3, 1.0, 1.0)):
            self.assertAlmostEqual(fc.fase_cascata_gradi(sez, 1e-4), 0.0, places=1)
            self.assertAlmostEqual(fc.fase_cascata_gradi(sez, 1e3), -90.0 * sum(s.ordine for s in sez), delta=1.0)

    def test_bessel_limite_gaussiano(self):
        # il Bessel tende a una gaussiana: a 2 fc l'attenuazione non supera ~14,2 dB per nessun ordine (picco a n = 6)
        valori = [fc.attenuazione_db(fc.bessel(n, 1.0), 2.0) for n in range(2, 13)]
        self.assertLess(max(valori), 14.5)
        self.assertGreater(valori[-1], 12.0)  # n = 12 si avvicina al limite gaussiano di circa 12 dB

    def test_frequenza_attenuazione(self):
        sez = fc.butterworth(4, 1.0)
        f40 = fc.frequenza_attenuazione(sez, 40.0)
        self.assertAlmostEqual(fc.attenuazione_db(sez, f40), 40.0, places=6)
        self.assertAlmostEqual(f40, 10 ** (40 / 80) * 1.0, delta=0.01)  # 10 log(1+x^8) = 40

    def test_risposta_ingresso_gradino_e_impulso(self):
        sez = fc.butterworth(2, 1.0)
        g1 = fc.risposta_gradino(sez, 2.0, punti=200)
        g2 = fc.risposta_ingresso(sez, lambda t: 1.0, 2.0, punti=200)
        self.assertEqual(g1, g2)
        impulso = fc.risposta_ingresso(sez, lambda t: 1.0 if 0.0 <= t < 1.0 else 0.0, 6.0, punti=400)
        self.assertAlmostEqual(impulso[-1][1], 0.0, places=3)
        self.assertGreater(max(y for _, y in impulso), 0.5)

    def test_progetta_cascata_bessel_e_chebyshev(self):
        for sez in (fc.bessel(4, 1000.0), fc.chebyshev(4, 1.0, 1000.0)):
            prog = fc.progetta_cascata_lp(sez, 10e-9)
            for teorica, reale in zip(sez, prog):
                self.assertAlmostEqual(reale.f0 / teorica.f0, 1.0, delta=0.05)
                if teorica.ordine == 2:
                    self.assertAlmostEqual(reale.q / teorica.q, 1.0, delta=0.08)


class TestCli(unittest.TestCase):
    def test_parse_si(self):
        self.assertAlmostEqual(filtri_cli.parse_si("1.6k"), 1600.0)
        self.assertAlmostEqual(filtri_cli.parse_si("100n"), 100e-9)
        self.assertAlmostEqual(filtri_cli.parse_si("47"), 47.0)
        with self.assertRaises(ValueError):
            filtri_cli.parse_si("abc")

    def test_formatta(self):
        self.assertEqual(filtri_cli.formatta(8660.0, "ohm"), "8.66 kohm")
        self.assertEqual(filtri_cli.formatta(82e-9, "F"), "82 nF")

    def test_comandi_validi(self):
        self.assertEqual(filtri_cli.main(["rc", "--r", "1.6k", "--c", "100n"]), 0)
        self.assertEqual(filtri_cli.main(["butter", "--n", "3", "--fc", "1k", "--c", "10n"]), 0)

    def test_ingressi_non_validi(self):
        self.assertEqual(filtri_cli.main(["butter", "--n", "9", "--fc", "1k", "--c", "10n"]), 2)
        self.assertEqual(filtri_cli.main(["sk", "--f0", "1k", "--q", "0", "--c2", "10n"]), 2)
        self.assertEqual(filtri_cli.main(["rc", "--r=-1k", "--c", "100n"]), 2)


if __name__ == "__main__":
    unittest.main()
