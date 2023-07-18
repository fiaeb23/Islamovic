"""
Aufgabe: Implementieren eines Putzplans mit zufälliger Aufgabenzuordnung
"""
import random

def aufgabe_zuteilen(personen, aufgaben):

    while len(aufgaben) > 0 and len(personen) > 0:
        rnd_person = random.choice(personen)
        rnd_aufgabe = random.choice(aufgaben)
        personen.remove(rnd_person)
        aufgaben.remove(rnd_aufgabe)
        yield (rnd_person, rnd_aufgabe)

mitbewohner = ["Agatha", "Berkan", "Charlie"]
todo_liste = [
    "den Boden staubsaugen",
    "die Fenster putzen",
    "nichts tun"]

for person, aufgabe in aufgabe_zuteilen(mitbewohner, todo_liste):
    print(person, "muss", aufgabe)


"""
Aufgabe: Aus Dateien nur bestimmte Zeilen speichern
"""

# Szenario: Unterordner mit beliebig vielen log-Dateien (z.b. 3)
#           Zeilen, die mit "#" beginnen sollen ausgelesen werden
#           Alle anderen Zeilen ignorieren!
#           Achtung: Es steht nicht genügend Speicher zur Verfügung,
#                    um alle Zeilen der Dateien zu speichern!

import sys

def filter_lines_by(file_obj, char):
    for line in file_obj:
        if line.startswith(char):
            yield line


files = ["data/log_01.txt", "data/log_02.txt", "data/log_03.txt"]

for file_name in files:
    print("---", file_name, "---")
    with open(file_name, encoding="utf-8") as file:
        # 1. alle Zeilen mit "#"
        #filtered_lines = [line for line in filter_lines_by(file, "#")]
        #print(filtered_lines)
        #print(sys.getsizeof(filtered_lines), "bytes")
        
        # 2. nach und nach zeilen mit "#" lesen
        try:
            while True:
                elem = next(filter_lines_by(file, "#"))
                print(elem, end="")
                input("...")
        except StopIteration:
            print("Dateiende erreicht.")

    print("------------------------------")    
    
    
    
