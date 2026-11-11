import unittest

from studi_kasus.nilai_siswa import analisis_nilai, kategori_nilai
from studi_kasus.validasi_user import validasi_user


class TestNilaiSiswa(unittest.TestCase):
    def test_analisis(self):
        hasil = analisis_nilai([80, 90, 70])
        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["tertinggi"], 90)
        self.assertEqual(hasil["terendah"], 70)
        self.assertEqual(hasil["kategori"], "B")

    def test_batas_kategori(self):
        self.assertEqual(kategori_nilai(85), "A")
        self.assertEqual(kategori_nilai(84.9), "B")
        self.assertEqual(kategori_nilai(70), "B")
        self.assertEqual(kategori_nilai(55), "C")
        self.assertEqual(kategori_nilai(40), "D")
        self.assertEqual(kategori_nilai(39), "E")

    def test_list_kosong(self):
        with self.assertRaises(ValueError):
            analisis_nilai([])


class TestValidasiUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validasi_user("Budi", 20, "budi@mail.com"), ("valid", []))

    def test_semua_salah(self):
        status, alasan = validasi_user("  ", 0, "budimail.com")
        self.assertEqual(status, "tidak valid")
        self.assertEqual(len(alasan), 3)



if __name__ == "__main__":
    unittest.main()
