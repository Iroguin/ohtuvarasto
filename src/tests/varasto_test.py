import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_negatiivinen_tilavuus(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_negatiivinen_alkusaldo(self):
        varasto = Varasto(10, -1)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_alkusaldo_mahtuu(self):
        varasto = Varasto(10, 5)
        self.assertAlmostEqual(varasto.saldo, 5)

    def test_konstruktori_alkusaldo_ei_mahdu(self):
        varasto = Varasto(10, 11)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        alkusaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, alkusaldo)

    def test_lisaa_varastoon_mahtuu_kokonaan(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisaa_varastoon_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen_maara(self):
        tulos = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(tulos, 0)

    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_varastosta_toimii(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(3)
        self.assertAlmostEqual(saatu_maara, 3)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_paljonko_mahtuu_toimii(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 5)

    def test_str_toimii(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")


if __name__ == '__main__':
    unittest.main()
