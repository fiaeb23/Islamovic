"""
1) Erstelle eine DB (mit oder ohne Python)
2) Erstelle in dieser DB eine Tabelle persons
   - Orientiere dich an der Struktur der persons.csv
3) Füge in diese Tabelle die Inhalte der persons.csv ein
"""


'''
sql = """
    INSERT INTO employees_fav_tracks VALUES
        (1, 34), (2, 981), (3, 673)
    ;
"""
cur.execute(sql)

# 4a) Ergebnisse lesen (o.Ä.)
#rows = cur.fetchall()
#for row in rows:
#    print(row) 

# 4b) Ergebnisse bestätigen:
conn.commit()
''' 


import sqlite3
import csv

# Pfad zur CSV-Datei
csv_file_path = "C:/GITHUB/Islamovic/Python-T2/OOP/persons.csv"

# Pfad zur SQLite-Datenbank
db_path = "C:/GITHUB/Islamovic/Datenbank/csv_to_db.db"

# 1) Verbindung zur DB herstellen:
with sqlite3.connect(db_path) as conn:
    # 2) Cursor-Objekt erstellen:
    cur = conn.cursor()

    # 3) Tabelle "persons" erstellen (falls sie noch nicht existiert):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT
        )
    """)

    # 4) Daten aus der CSV-Datei in die Tabelle "persons" einfügen:
    with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Überspringe Header-Zeile (falls vorhanden)
        for row in csvreader:
            cur.execute
            (""" INSERT INTO persons (first_name, last_name,email)
                 VALUES (?, ?, ?) """, (row[0], row[1], (row[2])))

    # 5) Transaktion bestätigen:
    conn.commit()

# #Daten aus derTabelle anzeigen
# with sqlite3.connect(db_path) as conn:
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM persons")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
