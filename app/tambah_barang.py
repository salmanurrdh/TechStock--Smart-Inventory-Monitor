from app.database import add_new_item, get_all_inventory

def tambah_barang():
    print("\n--- Tambah Barang Baru ---")
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah stok awal: "))
    harga = float(input("Harga per unit (Rp): "))
    batas_min = int(input("Batas minimal stok: "))
    
    add_new_item(nama, jumlah, harga, batas_min)
    print(f"Barang '{nama}' berhasil ditambahkan!\n")