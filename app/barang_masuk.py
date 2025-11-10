from app.data import inventory
from app.tampilkan_barang import tampilkan_barang

def barang_masuk():
    print("\n--- Barang Masuk ---")
    tampilkan_barang()
    if not inventory:
        return
    idx = int(input("Pilih nomor barang: ")) - 1
    jumlah = int(input("Jumlah barang masuk: "))
    inventory[idx]["jumlah"] += jumlah
    print(f"Stok '{inventory[idx]['nama']}' bertambah sebanyak {jumlah}.\n")