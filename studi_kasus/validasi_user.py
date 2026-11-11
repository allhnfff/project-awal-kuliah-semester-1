"""5. Validasi Data Pengguna."""


def validasi_user(nama, umur, email):
    """Kembalikan (status, daftar_alasan); status "valid" atau "tidak valid"."""
    alasan = []
    if not nama or not nama.strip():
        alasan.append("nama tidak boleh kosong")
    if umur <= 0:
        alasan.append("umur harus lebih dari 0")
    if "@" not in email:
        alasan.append('email harus mengandung "@"')

    status = "valid" if not alasan else "tidak valid"
    return status, alasan


if __name__ == "__main__":
    print(validasi_user("Budi", 20, "budi@mail.com"))
    print(validasi_user("", 0, "budimail.com"))
