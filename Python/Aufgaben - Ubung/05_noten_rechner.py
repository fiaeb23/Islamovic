"""
Übung 1:
Eine Schule möchte die Ermittlung der Noten ihrer Schüler 
digital durchführen.

Dabei soll der Lehrer (=Nutzer) eine Punktzahl eingeben 
und eine Note ausgegeben bekommen.

Die Note wird anhand folgender Formel berechnet:

weniger als 35 Punkte -> 6
mind. 35 Punkte -> 5
mind. 50 Punkte -> 4
mind. 60 Punkte -> 3
mind. 75 Punkte -> 2
mind. 85 Punkte -> 1

Anmerkung: Die Maximalpunktzahl beträgt 100 Punkte!
Anmerkung: Die Minimalpunktzahl beträgt 0 Punkte!
"""

# EINGABE
punkte = int(input("Punktzahl: "))

if punkte < 0:
    print("Fehlerhafte Eingabe!")
    print("Die Minimalpunktzahl beträgt 0 Punkte!")

elif punkte < 35: # implizit: punkte ist mind. 0
    print("Note 6")

elif punkte < 50: # implizit: punkte ist mind. 35
    print("Note 5")

elif punkte < 60: # implizit: punkte ist mind. 50
    print("Note 4")

elif punkte < 75: # implizit: punkte ist mind. 60
    print("Note 3")

elif punkte < 85: # implizit: punkte ist mind. 75    
    print("Note 2")

elif punkte <= 100: # implizit: punkte ist mind. 85
    print("Note 1")

else: # implizit: punkte ist größer als 100
    print("Fehlerhafte Eingabe!")
    print("Die Maximalpunktzahl beträgt 100 Punkte!")
   

    

