import unittest

from studi_kasus.kasir import hitung_total_belanja
from studi_kasus.password import cek_password
from studi_kasus.suhu import konversi_suhu


class TestKasir(unittest.TestCase):
    def test_contoh_soal(self):
        self.assertEqual(hitung_total_belanja([10000, 5000, 2500], 10), 15750)

    def test_tanpa_diskon(self):
        self.assertEqual(hitung_total_belanja([1000, 2000]), 3000)

    def test_list_kosong(self):
        self.assertEqual(hitung_total_belanja([], 50), 0)

    def test_diskon_tidak_valid(self):
        with self.assertRaises(ValueError):
            hitung_total_belanja([1000], 120)


class TestPassword(unittest.TestCase):
    def test_batas_kategori(self):
        self.assertEqual(cek_password("12345"), "lemah")
        self.assertEqual(cek_password("123456"), "sedang")
        self.assertEqual(cek_password("1234567890"), "sedang")
        self.assertEqual(cek_password("12345678901"), "kuat")


class TestSuhu(unittest.TestCase):
    def test_konversi(self):
        self.assertEqual(konversi_suhu(100, "to_fahrenheit"), 212)
        self.assertEqual(konversi_suhu(32, "to_celcius"), 0)
        self.assertAlmostEqual(konversi_suhu(-40, "to_celcius"), -40)

    def test_mode_tidak_valid(self):
        with self.assertRaises(ValueError):
            konversi_suhu(10, "to_kelvin")


if __name__ == "__main__":
    unittest.main()
