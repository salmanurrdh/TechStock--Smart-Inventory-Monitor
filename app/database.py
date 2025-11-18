import sqlite3
import os

DB_FILE = "inventory.db"

def init_database():
    """Initialize database dan buat table jika belum ada"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jumlah INTEGER NOT NULL,
            harga REAL NOT NULL,
            batas_min INTEGER NOT NULL
        )
    ''')
    
    # Insert data default jika table kosong
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        default_data = [
            ('Ayam', 80, 35000.0, 15),
            ('Bebek', 40, 55000.0, 10),
            ('Sapi', 25, 120000.0, 5),
            ('Seafood', 60, 70000.0, 12),
            ('Kambing', 20, 110000.0, 5)
        ]
        cursor.executemany('''
            INSERT INTO inventory (nama, jumlah, harga, batas_min)
            VALUES (?, ?, ?, ?)
        ''', default_data)
    
    conn.commit()
    conn.close()

def get_connection():
    """Dapatkan koneksi database"""
    return sqlite3.connect(DB_FILE)

def get_all_inventory():
    """Ambil semua data inventory"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.close()
    
    # Convert ke format dictionary seperti sebelumnya
    inventory = []
    for row in results:
        inventory.append({
            "id": row[0],
            "nama": row[1],
            "jumlah": row[2],
            "harga": row[3],
            "batas_min": row[4]
        })
    return inventory

def update_inventory(item_id, new_jumlah):
    """Update jumlah stok barang"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE inventory 
        SET jumlah = ? 
        WHERE id = ?
    ''', (new_jumlah, item_id))
    conn.commit()
    conn.close()

def add_new_item(nama, jumlah, harga, batas_min):
    """Tambah barang baru"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inventory (nama, jumlah, harga, batas_min)
        VALUES (?, ?, ?, ?)
    ''', (nama, jumlah, harga, batas_min))
    conn.commit()
    conn.close()

def get_total_asset():
    """Hitung total nilai aset"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(jumlah * harga) FROM inventory")
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total