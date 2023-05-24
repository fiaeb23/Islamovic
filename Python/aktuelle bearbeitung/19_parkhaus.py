# Freier Parkplatz -> None
# Belegter Parkplatz -> str
# - z.b. "VW Golf" oder "Opel Astra" 

# 3 Etagen mit je 4 Plätzen

"""
Entwickle ein Parkhaus-System

In diesem Programm hat der Nutzer folgende Möglichkeiten:
1) Sein Auto in einer bestimmten Etage parken
   - dazu muss der Nutzer eine Etage eingeben
   - anschließend wird ihm der erste freie Platz zugewiesen
   - falls die Etage voll ist, weise den Nutzer darauf hin
2) Sein Auto in dem ersten freien Parkplatz des ganzen(!)
   Parkhauses zu parken
   - ablauf: schleife, welche die etagen durchläuft
             und eine, welche die plätze der aktuellen Etage prüft

Hinweis:
- teste dein Programm mit unterschiedlichen Parkhaus-konfigurationen:
  1) etage 1 voll, nutzer will in etage 1 parken
  2) alle etagen voll, nutzer will in etage 1 parken
  3) alle etagen voll, nutzer wählt menüpunkt 2
  4) alle plätze voll bis auf etage 3 letzter platz, nutzer wählt menüpunkt 2

"""


import os

parkhaus = [
    [None, None, None, None], # 0
    [None, None, None, None], # 1
    [None, None, None, None]  # 2
]


def park_car(etage=None, platz=None):
   if etage is not None:                                                                 # Nutzer möchte in einer bestimmten Etage parken
      if etage < 0 or etage >= len(parkhaus):
         print("Ungültige Etage")
         return
      freie_plaetze = [i for i, platz in enumerate(parkhaus[etage]) if platz is None]
      if not freie_plaetze:
         print(f"Auf Etage {etage} sind alle Plätze belegt.")
         return
      elif len(freie_plaetze) == 1:
         platz = freie_plaetze[0]
      else:
            print(f"Auf Etage {etage} sind folgende Plätze frei:")
            for i in freie_plaetze:
                print(i+1)
            platz = int(input("Bitte geben Sie den gewünschten Platz ein: "))
            if platz not in freie_plaetze:
               print("Ungültiger Platz")
               return
      kennzeichen = input("Bitte geben Sie das Kennzeichen Ihres Autos ein: ")
      parkhaus[etage][platz] = kennzeichen
      print(f"Ihr Auto wurde auf Etage {etage} Platz {platz} geparkt.")
      os.system("pause")
   else:                                                                                   # Nutzer möchte in erstem freien Platz im ganzen Parkhaus parken
      for i, etage in enumerate(parkhaus):
         for j, platz in enumerate(etage):
               if platz is None:
                  kennzeichen = input("Bitte geben Sie das Kennzeichen Ihres Autos ein: ")
                  parkhaus[i][j] = kennzeichen
                  print(f"Ihr Auto wurde auf Etage {i} Platz {j} geparkt.")
                  return
      print("Alle Plätze sind belegt.")
      os.system("pause")
    

while True:
    print("\n".join(" ".join(str(p) for p in etage) for etage in parkhaus))
    print("\n"+"Bitte wählen Sie eine Option:") 
    print("1) Auto in bestimmter Etage parken")
    print("2) Auto im ersten freien Parkplatz des ganzen Parkhauses parken")
    print("3) Programm beenden")
    
    auswahl = input("Auswahl: ")
    if auswahl == "1":
      etage = int(input("Bitte geben Sie die Etage ein (0-2): "))
      platz = int(input("Bitte geben Sie den Parkplatz ein (0-3): "))
      park_car(etage, platz)
    elif auswahl == "2":
      park_car()
    elif auswahl == "3":
        break
    else:
      print("Ungültige Eingabe.")