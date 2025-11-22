from app.database import get_all_inventory, hapus_barang_nama

def menu_hapus_barang():
    # tampilkan daftar barang dulu
    inventory = get_all_inventory()
    if not inventory:
        print("Belum ada data barang.")
        return
    
    print("\nDaftar Barang:")
    for i, b in enumerate(inventory):
        print(f"{i+1}. {b['nama']} (Stok: {b['jumlah']}, Harga: Rp{b['harga']:,.2f})")
    
    try:
        nomor = int(input("Masukkan nomor barang yang ingin dihapus: "))
        if nomor < 1 or nomor > len(inventory):
            print("Nomor tidak valid.")
            return
        
        nama_barang = inventory[nomor-1]["nama"]
        konfirmasi = input(f"Yakin ingin menghapus '{nama_barang}'? (y/n): ").lower()
        if konfirmasi == "y":
            hapus_barang_nama(nama_barang)
        else:
            print("Penghapusan dibatalkan.")
    except ValueError:
        print("Input harus berupa angka.")