from app.data import inventory
from app.tampilkan_barang import tampilkan_barang

def barang_keluar():
    print("\n--- Barang Keluar ---")
    tampilkan_barang()
    if not inventory:
        return
    idx = int(input("Pilih nomor barang: ")) - 1
    jumlah = int(input("Jumlah barang keluar: "))
    if jumlah <= inventory[idx]["jumlah"]:
        inventory[idx]["jumlah"] -= jumlah
        print(f"Stok '{inventory[idx]['nama']}' berkurang sebanyak {jumlah}.\n")
    else:
        print("Jumlah keluar melebihi stok tersedia!\n")