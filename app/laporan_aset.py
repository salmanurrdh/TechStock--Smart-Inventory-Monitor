from app.data import inventory

def laporan_aset():
    print("\n=== LAPORAN NILAI ASET ===")
    total = sum(b["jumlah"] * b["harga"] for b in inventory)
    print(f"Total Nilai Aset Industri: Rp{total:,.2f}\n")