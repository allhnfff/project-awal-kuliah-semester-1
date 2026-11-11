"""3. Konversi Suhu."""


def konversi_suhu(nilai, mode):
    """Konversi suhu dengan mode "to_fahrenheit" atau "to_celcius"."""
    if mode == "to_fahrenheit":
        return nilai * 9 / 5 + 32
    if mode == "to_celcius":
        return (nilai - 32) * 5 / 9
    raise ValueError('mode harus "to_fahrenheit" atau "to_celcius"')


if __name__ == "__main__":
    print(konversi_suhu(100, "to_fahrenheit"))  # 212.0
    print(konversi_suhu(212, "to_celcius"))  # 100.0
