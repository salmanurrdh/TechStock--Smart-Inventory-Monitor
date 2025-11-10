from app.data import inventory

def tampilkan_barang():
    print("\n=== DAFTAR INVENTARIS ===")
    if not inventory:
        print("Belum ada data barang.\n")
        return
    for i, b in enumerate(inventory):
        status = "Stok Menipis!" if b["jumlah"] <= b["batas_min"] else "Aman"
        print(f"{i+1}. {b['nama']} | Stok: {b['jumlah']} | Harga: Rp{b['harga']:.2f} | {status}")
    print()