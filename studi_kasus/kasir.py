"""1. Kasir Sederhana - Hitung Total Belanja."""


def hitung_total_belanja(harga_barang, diskon=0):
    """Jumlahkan semua harga lalu terapkan diskon (dalam persen, 0-100)."""
    if not 0 <= diskon <= 100:
        raise ValueError("diskon harus di antara 0 dan 100")
    if any(harga < 0 for harga in harga_barang):
        raise ValueError("harga barang tidak boleh negatif")

    total = sum(harga_barang)
    return total - total * diskon / 100


if __name__ == "__main__":
    print(hitung_total_belanja([10000, 5000, 2500], 10))  # 15750.0
