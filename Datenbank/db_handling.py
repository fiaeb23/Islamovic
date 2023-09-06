# import sqlite3

# db_path = r"C:/Users/dvalassis/Downloads/chinook/chinook.db"


# # 1) Verbindung zur DB herstellen:
# with sqlite3.connect(db_path) as conn:

#     # 2) Cursor-Objekt erstellen:
#     cur = conn.cursor()

    # 3) SQL-Befehl ausführen:
    # sql = "SELECT * FROM artists;"
    # cur.execute(sql)

    # # 4) Ergebnisse lesen (o.Ä.)
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row[1])
        
        
""" Aufgaben:
1) Gebe alle Künstler aus, die mit "A" beginnen:

2) Gebe alle Lieder mit GenreId 1 aus:

3) Gebe alle Lieder aus, die mind. 5 Minuten lang sind:

4) Gebe die Gesamtgröße aller Lieder in GB aus:
"""

import sqlite3
import os 

db_path = r"C:/GITHUB/Islamovic/Datenbank/chinook/chinook.db"

with sqlite3.connect(db_path) as conn:

    cur = conn.cursor()

sql = "SELECT * FROM artists WHERE Name LIKE 'A%';"
cur.execute(sql)
artists = cur.fetchall() #alle Daten abfragen
for artist in artists:
    print(artist[1])
os.system("pause")

# sql = "SELECT * FROM tracks WHERE GenreId = 1;"
# cur.execute(sql)
# tracks = cur.fetchall()
# for track in tracks:
#     print(track[1])
# os.system("pause")

sql = "SELECT * FROM tracks WHERE Milliseconds >= 5*60*1000;"
cur.execute(sql)
long_tracks = cur.fetchall()
for track in long_tracks:
    print(f'{track[1]},{track[6]}')
os.system("pause")

sql = "SELECT SUM(Bytes) FROM tracks;"
cur.execute(sql)
total_bytes = cur.fetchone()[0] #bestimmte Zeile abfragen
total_gb = total_bytes / (1000 * 1000 * 1000)
print(f"Die Gesamtgröße aller Lieder beträgt {total_gb:.2f} GB")
