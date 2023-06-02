"""
Erstelle ein Bank-Programm

Ersteinmal loggt der Nutzer sich ein.
Sollte der Login erfolgreich sein 
(=name & pin korrekt),
kann er auf das Programm zugreifen.

Der Nutzer hat folgende Optionen:
1) Kontostand anzeigen (in x.xx €)
2) Kontostand erhöhen
3) Kontostand verringern
   - beachte: man kann nicht mehr abheben als auf dem Konto ist

BONUS)
Entwickle ein User-Management-Menü. Hier kann ein Admin folgendes:
1) Nutzer hinzufügen
2) Nutzer entfernen
"""
import os

user_db = [
    {
        "name": "Esad",
        "pin": "1234",
        "balance": 0
    },
    {
        "name": "Rafael",
        "pin": "9876",
        "balance": 100
    }
]

# TODO: Login-System implementieren

while True:
    os.system("cls")
    print("### Bank-System ###")
    print("Du hast folgende Optionen:")
    print("[1] Kontostand anzeigen")
    print("[2] Kontostand erhöhen")
    print("[3] Kontostand verringern")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        pass
        
    elif eingabe == "2":
        pass
        
    elif eingabe == "3":
        pass
        
    elif eingabe == "x":
        pass
        exit()
        
    else:
        print("Das habe ich nicht verstanden!")
        os.system("pause")


