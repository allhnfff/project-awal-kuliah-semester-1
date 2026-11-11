"""2. Cek Password."""


def cek_password(password):
    """Kembalikan "lemah" (< 6), "sedang" (6-10) atau "kuat" (> 10 karakter)."""
    panjang = len(password)
    if panjang < 6:
        return "lemah"
    if panjang <= 10:
        return "sedang"
    return "kuat"


if __name__ == "__main__":
    for pw in ["abc", "rahasia1", "passwordsangatpanjang"]:
        print(f"{pw!r}: {cek_password(pw)}")
