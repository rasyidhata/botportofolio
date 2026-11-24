import sqlite3 

# # Membuka file basis data
con = sqlite3.connect('marvel.db')

# # Membuat tabel
# with con:
#     con.execute("""
#         CREATE TABLE marvel (
#             ID INTEGER PRIMARY KEY,
#             name TEXT,
#             superpower TEXT,
#             status TEXT
# );
#     """)

#     sql = 'INSERT INTO marvel (ID, name, superpower, status) values(?, ?, ?, ?)'

# # Menentukan data untuk kueri
# data = [
#     (1, 'Iron Man', 'Iron Suite', 'Baik'),
#     (2, 'Thor', 'Mjolnir', 'Baik'),
#     (3, 'Loki', 'Illusion', 'Baik'),
#     (4, 'Dr. Doom', 'Magic', 'Jahat'),
# ]

# # Menambahkan semua data sekaligus menggunakan kueri iteratif
# with con:
#     con.executemany(sql, data)

# with con:
#     # con.execute("UPDATE marvel SET status = 'Gugur' WHERE name = ?;", ('Shang Chi',))
#    con.execute("UPDATE marvel SET status = 'Dewa' WHERE id = ?", (3,))

with con:
    con.execute("DELETE FROM marvel WHERE name = ?",('Iron Man',))