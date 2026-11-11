"""4. Manajemen Nilai Siswa."""


def kategori_nilai(rata_rata):
    """Tentukan kategori A-E berdasarkan nilai rata-rata."""
    if rata_rata >= 85:
        return "A"
    if rata_rata >= 70:
        return "B"
    if rata_rata >= 55:
        return "C"
    if rata_rata >= 40:
        return "D"
    return "E"


def analisis_nilai(daftar_nilai):
    """Hitung rata-rata, nilai tertinggi, terendah, dan kategori."""
    if not daftar_nilai:
        raise ValueError("daftar nilai tidak boleh kosong")
    if any(not 0 <= nilai <= 100 for nilai in daftar_nilai):
        raise ValueError("nilai harus di antara 0 dan 100")

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    return {
        "rata_rata": rata_rata,
        "tertinggi": max(daftar_nilai),
        "terendah": min(daftar_nilai),
        "kategori": kategori_nilai(rata_rata),
    }


if __name__ == "__main__":
    print(analisis_nilai([80, 90, 75, 60, 95]))
