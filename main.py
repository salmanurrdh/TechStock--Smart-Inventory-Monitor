inventory = []

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

def barang_masuk():
    print("\n--- Barang Masuk ---")
    tampilkan_barang()
    if not inventory:
        return
    idx = int(input("Pilih nomor barang: ")) - 1
    jumlah = int(input("Jumlah barang masuk: "))
    inventory[idx]["jumlah"] += jumlah
    print(f"Stok '{inventory[idx]['nama']}' bertambah sebanyak {jumlah}.\n")

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
        print("⚠ Jumlah keluar melebihi stok tersedia!\n")

def tampilkan_barang():
    print("\n=== DAFTAR INVENTARIS ===")
    if not inventory:
        print("Belum ada data barang.\n")
        return
    for i, b in enumerate(inventory):
        status = "⚠ Stok Menipis!" if b["jumlah"] <= b["batas_min"] else "Aman"
        print(f"{i+1}. {b['nama']} | Stok: {b['jumlah']} | Harga: Rp{b['harga']:.2f} | {status}")
    print()

def laporan_aset():
    print("\n=== LAPORAN NILAI ASET ===")
    total = sum(b["jumlah"] * b["harga"] for b in inventory)
    print(f"Total Nilai Aset Industri: Rp{total:,.2f}\n")

while True:
    print("""
========= SMART INVENTORY MONITOR =========
1. Tambah Barang
2. Barang Masuk
3. Barang Keluar
4. Lihat Daftar Barang
5. Laporan Nilai Aset
6. Keluar
===========================================
""")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        barang_masuk()
    elif pilih == "3":
        barang_keluar()
    elif pilih == "4":
        tampilkan_barang()
    elif pilih == "5":
        laporan_aset()
    elif pilih == "6":
        print("Terima kasih telah menggunakan Smart Inventory Monitor!\n")
        break
    else:
        print("⚠ Pilihan tidak valid. Silakan coba lagi.\n")
