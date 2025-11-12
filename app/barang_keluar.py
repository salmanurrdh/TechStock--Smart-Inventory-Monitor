from app.data import inventory
from app.tampilkan_barang import tampilkan_barang

def barang_keluar():
    print("\n--- Barang Keluar ---")
    tampilkan_barang()
    if not inventory:
        return
    
    while True:
        try:
            idx = int(input("Pilih nomor barang: ")) - 1
            if idx < 0 or idx >= len(inventory):
                print("Nomor barang tidak ditemukan! Silakan coba lagi.\n")
                continue

            jumlah = int(input("Jumlah barang keluar: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!\n")
                continue

            if jumlah <= inventory[idx]["jumlah"]:
                inventory[idx]["jumlah"] -= jumlah
                print(f"Stok '{inventory[idx]['nama']}' berkurang sebanyak {jumlah}.\n")
                break  # keluar dari loop jika sukses
            else:
                print("Jumlah keluar melebihi stok tersedia! Silakan pilih ulang barang.\n")
                continue  # kembali ke input nomor barang

        except ValueError:
            print("Input tidak valid! Harap masukkan angka.\n")
            continue