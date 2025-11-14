# 🔰 Studi Kasus Level Mudah

## 1. Kasir Sederhana – Hitung Total Belanja
Buat fungsi yang menerima:
- daftar harga barang (array/list angka)
- diskon dalam persen (0–100)

Fungsi harus:
- menjumlahkan semua harga
- menerapkan diskon
- mengembalikan nilai total yang sudah didiskon

Contoh:
~~~
input = [10000, 5000, 2500], diskon 10%
output = 15750
~~~

---

## 2. Cek Password
Buat fungsi yang menerima sebuah string (password) dan mengembalikan:
- "lemah" jika panjang < 6
- "sedang" jika 6–10 karakter
- "kuat" jika > 10 karakter

---

## 3. Konversi Suhu
Buat fungsi yang mengonversi:
- Celcius → Fahrenheit
- Fahrenheit → Celcius

Gunakan parameter mode:
- `to_fahrenheit`
- `to_celcius`

---

# 🟡 Studi Kasus Level Menengah

## 4. Manajemen Nilai Siswa
Buat fungsi yang menerima list nilai siswa (0–100) lalu mengembalikan:
- nilai rata-rata
- nilai tertinggi
- nilai terendah
- kategori berdasarkan rata-rata:
  - A (≥85)
  - B (70–84)
  - C (55–69)
  - D (40–54)
  - E (<40)

Output boleh berupa dictionary/objek.

---

## 5. Validasi Data Pengguna
Buat fungsi `validasi_user(nama, umur, email)`.

Validasi:
- `nama` tidak boleh kosong
- `umur` harus > 0
- email harus mengandung "@"

Kembalikan `"valid"` atau `"tidak valid"` beserta alasannya.

---

## 6. Hitung Gaji Karyawan
Buat fungsi yang menerima:
- gaji_pokok
- jam_lembur

Aturan lembur:
- lembur dibayar 20.000/jam
- jika lembur > 40 jam, kelebihannya dibayar 30.000/jam

Fungsi mengembalikan total gaji.

---

# 🔴 Studi Kasus Level Lanjutan

## 7. Sistem Booking Hotel
Buat fungsi yang menerima:
- tipe kamar (`standard`, `deluxe`, `suite`)
- jumlah malam
- membership (`none`, `silver`, `gold`)

Aturan harga kamar:
- standard = 300k/malam
- deluxe = 500k/malam
- suite = 800k/malam

Diskon membership:
- none = 0%
- silver = 10%
- gold = 20%

Fungsi harus menghitung total biaya setelah diskon.

---

## 8. Aplikasi To-Do List Sederhana
Buat minimal 3 fungsi:
- `tambah_tugas(list, tugas)`
- `hapus_tugas(list, tugas)`
- `tampilkan_tugas(list)`

Simulasikan alur:
1. Tambah beberapa tugas.
2. Hapus satu.
3. Tampilkan list terakhir.

---

## 9. Analisis Data Penjualan Online
Buat fungsi `analisis_penjualan(data)`.

Format data:
~~~
[
  { "item": "baju", "qty": 3, "harga": 100000 },
  { "item": "celana", "qty": 2, "harga": 150000 }
]
~~~

Fungsi harus menghitung:
- total transaksi
- item paling banyak terjual
- pendapatan total

Output berupa objek/dictionary.
