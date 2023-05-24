"""
Schreibe ein Programm, welches für einen 
gegebenen Warenkorb folgendes berechnet:
1) Anzahl der Artikel
  - beachte die Anzahl jedes einzelnen Artikels
  - im Beispiel = 8
2) Gesamtpreis des Warenkorbs
  - beachte die anzahl jedes einzelnen Artikels
  - Im Beispiel = 2399 * 2 + 1999 * 4 + 29999 * 2

BONUS)
- Teuerster Artikel
  - beachte die Anzahl jedes einzelnen Artikels
- Günstigster Artikel
  - beachte die Anzahl jedes einzelnen Artikels
"""

warenkorb = [
#   [<name>    , <preis>, <anzahl>]
    ["Tastatur", 2399, 2],
    ["Maus", 1999, 4],
    ["Monitor", 29999, 2]
    ["xyz", 29999, 2]
]

#for artikel in warenkorb:
#    # artikel = ["Tastatur", 2399, 2]

gesamt_anzahl = 0
gesamt_preis = 0
teuerster_artikel_liste = []
teuerster_artikel = ["", float("-inf"), 1]
guenstigster_artikel = ["", float("inf"), 1]
for name, einzelpreis, anzahl in warenkorb:
    # name = "Tastatur"
    # einzelpreis = 2399
    # anzahl = 2
    gesamt_anzahl = gesamt_anzahl + anzahl
    gesamt_preis = gesamt_preis + einzelpreis * anzahl
    
    if einzelpreis * anzahl == teuerster_artikel[1] * teuerster_artikel[2]:
        teuerster_artikel_liste.append([name, einzelpreis, anzahl])
        teuerster_artikel = [name, einzelpreis, anzahl]
    
    if einzelpreis * anzahl > teuerster_artikel[1] * teuerster_artikel[2]:
        teuerster_artikel_liste = [[name, einzelpreis, anzahl]]
        teuerster_artikel = [name, einzelpreis, anzahl]
        
    if einzelpreis * anzahl < guenstigster_artikel[1] * guenstigster_artikel[2]:
        guenstigster_artikel = [name, einzelpreis, anzahl]
    
if len(warenkorb) > 0:
    print("Im Warenkorb befinden sich", gesamt_anzahl, "Artikel!")
    print("Der Gesamtpreis beträgt", str(gesamt_preis/100).replace(".", ","), "€")
    print("Der teuerste Artikel ist", teuerster_artikel[0], "...")
    print("...mit einem Preis von", str(teuerster_artikel[1]*teuerster_artikel[2]/100).replace(".", ","), "€")
    print("Der günstigste Artikel ist", guenstigster_artikel[0], "...")
    print("...mit einem Preis von", str(guenstigster_artikel[1]*guenstigster_artikel[2]/100).replace(".", ","), "€")
else:
    print("Der Warenkorb ist leer!")