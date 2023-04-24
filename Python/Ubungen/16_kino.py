
#kino_reihe = ["X", None, "X", None, None]
# "X" -> Platz belegt
# None -> Platz frei

""" 
Entwickle ein Kino-System

Der Nutzer hat folgende Optionen:
1) Den ersten freien Einzelplatz ermitteln
   - Gebe die Position des ersten freien Platzes aus
2) Den ersten freien Doppelplatz ermitteln
   - Gebe die Position des ersten freien Doppelplatzes aus
3) Kino verlassen
"""

import os

kino = [
    ["X", None, "X", None, None],
    [None, None, "X", "X", None],
    [None, None, "X", "X", None],
    [None, "X", "X", "X", None],
    [None, "X", None, None, "X"]
]

def freier_einzelplatz(reihe):
    for i in range(len(reihe)):
        if reihe[i] == None:
            return i
    return -1                                                                         # -1 wenn kein None vorhanden, Kein platz vorhanden

def freier_doppelplatz(reihe):                                                        #-1 bis zum vorletzten der Liste zählen, Doppelplatz besteht aus zwei nebeneinander liegenden Plätzen
    for i in range(len(reihe) - 1):
        if reihe[i] == None and reihe[i+1] == None:                                
            return i
    return -1                                                                         # Wenn kein freier Doppelplatz vorhanden ist, gib -1 zurück


while True:
    print("\n Bitte wählen Sie eine Option:")
    print("1) Einzelplatz buchen")
    print("2) Doppelplatz buchen")
    print("3) Kino verlassen")
    auswahl = input()

    if auswahl == "1":
        freie_plaetze = []
        for i, reihe in enumerate(kino):                                               #enumerate Nummerierung erstellen
            freier_platz = freier_einzelplatz(reihe)
            if freier_platz != -1:
                freie_plaetze.append((i, freier_platz))                                #append fügt positionen ein
        if freie_plaetze:
            for reihe, platz in freie_plaetze:
                print(f"Freier Einzelplatz in Reihe {reihe+1}, Platz {platz+1}")
        else:
            print("Es gibt keinen freien Einzelplatz.")
        os.system("pause")
    elif auswahl == "2":
        freie_plaetze = []
        for i, reihe in enumerate(kino):
            freier_platz = freier_doppelplatz(reihe)
            if freier_platz != -1:
                freie_plaetze.append((i, freier_platz))
        if freie_plaetze:
            for reihe, platz in freie_plaetze:
                print(f"Freier Doppelplatz in Reihe {reihe+1}, Plätze {platz+1} und {platz+2}")     #Freier Doppelplatz in Reihe 4(Reihe+1), Plätze 3 (Platz 1) und 4 (Platz 2)
        else:
            print("Es gibt keinen freien Doppelplatz.")
        os.system("pause")
    elif auswahl == "3":
        print("Vielen Dank für Ihren Besuch. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option.")