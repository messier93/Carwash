# Carwash
Program ini adalah sistem manajemen antrian car wash berbasis Python yang menggunakan konsep Queue (FIFO) untuk antrian kendaraan dan Stack (LIFO) untuk riwayat kendaraan yang sudah selesai dicuci. Data disimpan secara permanen menggunakan file teks (.txt), sehingga data tidak hilang saat program ditutup.

# Kelompok 13 - HDC
- Chelsea Claudia Hutapea  
- Dyas Arum Paramitha  
- Haura Nur Hafizhah  

# Fitur Program

# Manajemen Antrian (Queue)
- Menambah antrian kendaraan
- Menampilkan daftar antrian
- Memproses antrian (Sedang Dicuci / Selesai)
- Menghapus antrian
- Mencari data kendaraan berdasarkan plat nomor

# Pembayaran
- Status pembayaran: Lunas / Belum Lunas
- Pelunasan pembayaran sebelum kendaraan diproses selesai

# Riwayat (Stack)
- Menyimpan kendaraan yang sudah selesai dicuci
- Menampilkan riwayat terakhir (LIFO)
- Menampilkan riwayat berdasarkan tanggal (sorting)

# Konsep Struktur Data
- Queue (FIFO) digunakan untuk antrian kendaraan
- Stack (LIFO) digunakan untuk riwayat kendaraan
- Sorting digunakan untuk pengurutan riwayat berdasarkan tanggal

# Penyimpanan Data
Program menggunakan dua file utama:
- carwash.txt → menyimpan data antrian aktif
- history.txt → menyimpan riwayat kendaraan selesai
  
Format data:
plat,status,pembayaran,tanggal

# Cara Menjalankan Program
1. Pastikan Python sudah terinstall
2. Jalankan file utama:
   python antriancucimobil.py
3. Gunakan menu yang tersedia di terminal

# Menu Program
1. Tambah Antrian
2. Tampilkan Antrian
3. Proses Antrian
4. Hapus Antrian
5. Cari Plat
6. Lihat Riwayat Terakhir
7. Lihat Riwayat Berdasarkan Tanggal
8. Bayar / Lunasi Pembayaran
0. Keluar

# Teknologi
- Python 3
- File Handling (.txt)
- Modul datetime

# Catatan
- Data otomatis tersimpan setiap ada perubahan
- Jangan mengubah file txt secara manual karena bisa menyebabkan error parsing
- Program berjalan di terminal (CLI)
