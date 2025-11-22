from app.database import get_all_inventory, update_inventory
from app.tampilkan_barang import tampilkan_barang

def barang_masuk():
    print("\n--- Barang Masuk ---")
    inventory = get_all_inventory()
    tampilkan_barang()
        
    if not inventory:
        return
        
    idx = int(input("Pilih nomor barang: ")) - 1
    if idx < 0 or idx >= len(inventory):
        print("Nomor barang tidak valid!")
        return
            
    jumlah = int(input("Jumlah barang masuk: "))
    item_id = inventory[idx]["id"]
    new_jumlah = inventory[idx]["jumlah"] + jumlah
        
    update_inventory(item_id, new_jumlah)
    print(f"Stok '{inventory[idx]['nama']}' bertambah sebanyak {jumlah}.\n")