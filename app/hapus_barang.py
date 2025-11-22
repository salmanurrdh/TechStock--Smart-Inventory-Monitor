from app.database import hapus_barang

def menu_hapus_barang():
    try:
        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
        hapus_barang(id_barang)
    except ValueError:
        print("ID harus berupa angka.")