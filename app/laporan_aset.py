from app.database import get_total_asset

def laporan_aset():
    print("\n=== LAPORAN NILAI ASET ===")
    total = get_total_asset()
    print(f"Total Nilai Aset Industri: Rp{total:,.2f}\n")