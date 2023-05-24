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
import os
warenkorb = [
#   [<name>    , <preis>, <anzahl>]
    ["Tastatur", 2399, 2],
    ["Maus", 1999, 4],
    ["Monitor", 29999, 2]
]

for name ,preis ,anzahl in (warenkorb):
    os.system("cls")
    ausgabe = print([name , (preis)]) 
    print(name, preis, anzahl)
    print([preis])
    print(anzahl)
    print("Anzahl der Artikel",warenkorb[0][2] + warenkorb[1][2] + warenkorb[2][2], "Stöcke in der Warenkorb")
    print("Gesamtpreis des Warenkorbs",warenkorb[0][2]*warenkorb[0][1]  + warenkorb[1][2]*warenkorb[1][1]  + warenkorb[2][2] * warenkorb[2][1] , "€ ist die Gesamtpreis")
  	
    guenstigster_artikel = min(warenkorb[0][1],warenkorb[1][1],warenkorb[2][1])
    teuerster_artikel = max(warenkorb[0][1],warenkorb[1][1],warenkorb[2][1])
    
    print("\nDer günstigste Artikel kostet", guenstigster_artikel, "Euro.")
    print("Der  teuerste Artikel kostet", teuerster_artikel, "Euro.")

    '''
    Teuerster_Artikel = 0
    while True:
      warenkorb[0][1] >= Teuerster_Artikel
      print( "der Teuerster_Artikel ist",warenkorb[0][0],"")
      print("nashwan",warenkorb[0][1])
      warenkorb[0][1] = Teuerster_Artikel
      input(">>>>")
      (exit)
      

      if warenkorb[1][1] >= Teuerster_Artikel:
        print( "der Teuerster_Artikel ist",warenkorb[1][0],"")
        warenkorb[1][1] = Teuerster_Artikel
        (exit)

        input(">>>>")
      elif warenkorb[2][1] >= Teuerster_Artikel:
        print( "der Teuerster_Artikel ist",warenkorb[2][0],"")
        warenkorb[2][1] = Teuerster_Artikel
        
        input(">>>>")
        print(Teuerster_Artikel)
        input(">>>>>")
        (exit)
      else:
          break

    '''