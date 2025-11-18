from app.database import get_all_inventory

def tampilkan_barang():
    # Kode warna ANSI
    HIJAU = "\033[92m"   # Hijau terang
    KUNING = "\033[93m"  # Kuning terang
    MERAH = "\033[91m"   # Merah terang
    RESET = "\033[0m"    # Reset ke warna normal

    print("\n" + "="*80)
    print("DAFTAR INVENTARIS".center(80))
    print("="*80)
    
    inventory = get_all_inventory()
    
    if not inventory:
        print("Belum ada data barang.".center(80))
        print("="*80)
        return

    # Header tabel
    print(f"No.  {'Nama Barang':<15} {'Stok':<8} {'Harga':<15} {'Status':<10}")
    print("-" * 80)

    for i, b in enumerate(inventory):
        # Tentukan status berdasarkan jumlah stok
        if b["jumlah"] == 0:
            status = f"{MERAH}HABIS{RESET}"
        elif b["jumlah"] <= b["batas_min"]:
            status = f"{KUNING}STOK MENIPIS!{RESET}"
        else:
            status = f"{HIJAU}AMAN{RESET}"

        # Format harga dengan separator ribuan
        harga_formatted = f"Rp{b['harga']:,.2f}"
        
        # Tampilkan data dengan alignment
        print(f"{i+1:<4} {b['nama']:<15} {b['jumlah']:<8} {harga_formatted:<15} {status:<10}")

    print("="*80)
    print()