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

def konfirmasi_menu(nama_menu):
    """Fungsi untuk konfirmasi sebelum menjalankan menu apapun"""
    print(f"\nAnda memilih '{nama_menu}'")
    konfirmasi = input("Apakah ini menu yang benar? (y/n) =  ").lower()
    return konfirmasi == 'y'

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
    pilih = input("Pilih menu (1-7): ")

    menu_options = {
        "1": ("Tambah Barang", tambah_barang),
        "2": ("Barang Masuk", barang_masuk),
        "3": ("Barang Keluar", barang_keluar),
        "4": ("Lihat Daftar Barang", tampilkan_barang),
        "5": ("Laporan Nilai Aset", laporan_aset),
        "6": ("Hapus Barang", menu_hapus_barang),
        "7": ("Keluar dari Aplikasi", None)
    }

    if pilih in menu_options:
        nama_menu, fungsi_menu = menu_options[pilih]
        
        if konfirmasi_menu(nama_menu):
            if pilih == "7":
                print("Terima kasih telah menggunakan Smart Inventory Monitor!\n")
                break
            else:
                fungsi_menu()  
        else:
            print("Dibatalkan oleh pengguna")
    else:
        print("Pilihan tidak valid. Silakan pilih 1-7.\n")