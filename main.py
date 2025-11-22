import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.database import init_database
from app.tambah_barang import tambah_barang
from app.barang_masuk import barang_masuk
from app.barang_keluar import barang_keluar
from app.tampilkan_barang import tampilkan_barang
from app.hapus_barang import menu_hapus_barang
from app.laporan_aset import laporan_aset

# Initialize database saat aplikasi start
init_database()

while True:
    print("""
========= SMART INVENTORY MONITOR =========
1. Tambah Barang
2. Barang Masuk
3. Barang Keluar
4. Lihat Daftar Barang
5. Laporan Nilai Aset
6. Hapus Barang
7. Keluar
===========================================
""")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        barang_masuk()
    elif pilih == "3":
        barang_keluar()
    elif pilih == "4":
        tampilkan_barang()
    elif pilih == "5":
        laporan_aset()
    elif pilih == "6":
        menu_hapus_barang()
    elif pilih == "7":
        print("Terima kasih telah menggunakan Smart Inventory Monitor!\n")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")