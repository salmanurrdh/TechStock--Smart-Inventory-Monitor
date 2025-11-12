from app.data import inventory

def tambah_barang():
    print("\n--- Tambah Barang Baru ---")
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah stok awal: "))
    harga = float(input("Harga per unit (Rp): "))
    batas_min = int(input("Batas minimal stok: "))
    inventory.append({
        "nama": nama,
        "jumlah": jumlah,
        "harga": harga,
        "batas_min": batas_min
    })
    print(f"Barang '{nama}' berhasil ditambahkan!\n")