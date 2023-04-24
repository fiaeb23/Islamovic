""" Entwickle ein Kino-System

Der Nutzer hat folgende Optionen:
1) Den ersten freien Einzelplatz ermitteln
   - Gebe die Position des ersten freien Platzes aus
2) Den ersten freien Doppelplatz ermitteln
   - Gebe die Position des ersten freien Doppelplatzes aus
3) Kino verlassen
"""
import os

#               0,    1,   2,    3,    4
kino_reihe = ["X", None, "X", "X", None]
# "X" -> Platz belegt
# None -> Platz frei

while True:
    os.system("cls")
    print("Kino:", kino_reihe)
    print("Du hast folgende Optionen:")
    print("[1] Einzelplatz suchen")
    print("[2] Doppelplatz suchen")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        
        if None in kino_reihe:
            print("Freier Platz:", kino_reihe.index(None)+1)
            kino_reihe[kino_reihe.index(None)] = "X"
        else:
            print("Kein freier Platz gefunden!")
        
        os.system("pause")
    
    elif eingabe == "2":
        """
        [0] [1]  [2] [3]  [4]
        "X" None "X" "X" None
        """
        i = 0
        platz_gefunden = False
        
        #       < 5
        while i < len(kino_reihe)-1: # [0, 1, 2, 3]
            # print("i =", i)
            if kino_reihe[i] is None and kino_reihe[i+1] is None:
                print("Freier Doppelplatz:", i+1, "&", i+2)
                platz_gefunden = True
                kino_reihe[i] = "X"
                kino_reihe[i+1] = "X"
                break
            else:
                i = i + 1
        
        if platz_gefunden == False:
            print("Keinen freien Doppelplatz gefunden!")
        
        os.system("pause")
            
    elif eingabe == "x":
        print("Auf Wiedersehen!")
        exit()
        
    else:
        print("Das habe ich nicht verstanden!")
        os.system("cls")