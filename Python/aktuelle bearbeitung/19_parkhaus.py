
# Freier Parkplatz -> None
# Belegter Parkplatz -> str
# - z.b. "VW Golf" oder "Opel Astra" 

# 3 Etagen mit je 4 Plätzen
parkhaus = [
    ["VW Golf", None, "Opel Astra", None], # 0
    ["Opel Astra", "Opel Astra", "Opel Astra", "VW Golf"], # 1
    [None, None, None, None]               # 2
]

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