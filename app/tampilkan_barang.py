from app.data import inventory

def tampilkan_barang():
    # Kode warna ANSI
    HIJAU = "\033[92m"   # Hijau terang
    KUNING = "\033[93m"  # Kuning terang
    MERAH = "\033[91m"   # Merah terang
    RESET = "\033[0m"    # Reset ke warna normal

    print("\n=== DAFTAR INVENTARIS ===")
    if not inventory:
        print("Belum ada data barang.\n")
        return

    for i, b in enumerate(inventory):
        # Tentukan status berdasarkan jumlah stok
        if b["jumlah"] == 0:
            status = f"{MERAH}Barang Habis!{RESET}"
        elif b["jumlah"] <= b["batas_min"]:
            status = f"{KUNING}Stok Menipis!{RESET}"
        else:
            status = f"{HIJAU}Aman{RESET}"

        # Tampilkan data barang
        print(f"{i+1}. {b['nama']} | Stok: {b['jumlah']} | Harga: Rp{b['harga']:.2f} | {status}")
    print()