"""
Entwickle ein Bank-System

Der Nutzer hat einen Kontostand, welcher zu Beginn bei 100 liegt.
Im Hauptmenü wird dem Nutzer der aktuelle Kontostand angezeigt.

Über das Untermenü 1 kann der Nutzer den Kontostand erhöhen
- Der Geldbetrag MUSS eine Zahl sein
- Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

Über das Untermenü 2 kann der Nutzer den Kontostand verringern
- Der Geldbetrag MUSS eine Zahl sein
- Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

BONUS) Der Nutzer darf nicht mehr Geld abheben (Untermenü 2)
       als ihm zur Verfügung steht

BONUS_2) Implementiere eine PIN-Abfrage für das Konto
"""


import os

kontostand = 100  # 100€
pin = "0123"

if input("Bitte PIN eingeben: ") != pin:
    print("Diese PIN ist falsch!")
    exit()
    
print("PIN ist korrekt!")
input("Bitte [ENTER] drücken...")

while True:
    os.system("cls") 
    print("Du befindest dich im Bank-System")
    print("Aktueller Kontostand:", kontostand, "€")
    print("Du hast folgende Optionen:")
    print("[1] Kontostand erhöhen")
    print("[2] Kontostand verringern")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        while True:
            os.system("cls")
            print("Du möchtest deinen Kontostand erhöhen")
            print("Bitte Zahl eingeben oder [x] zum Beenden")   
            eingabe = input(">>> ")
            
            if eingabe.isdecimal():
                kontostand = kontostand + int(eingabe)
                print("Vielen Dank")
                print("Dein neuer Kontostand beträgt:", kontostand)
                input("Bitte [ENTER] drücken...")
                break
                
            elif eingabe == "x":
                print("Du kehrst jetzt in das Hauptmenü zurück.")
                input("Bitte [ENTER] drücken...")
                break
                
            else:
                print("Das habe ich nicht verstanden!")
                input("Bitte [ENTER] drücken...")
        
          
    elif eingabe == "2":
        while True:
            os.system("cls")
            print("Du möchtest deinen Kontostand verringern")
            print("Bitte Zahl eingeben oder [x] zum Beenden")   
            eingabe = input(">>> ")
            
            if eingabe.isdecimal():
                if int(eingabe) <= kontostand:
                    kontostand = kontostand - int(eingabe)
                    print("Vielen Dank")
                    print("Dein neuer Kontostand beträgt:", kontostand)
                    input("Bitte [ENTER] drücken...")
                    break
                else:
                    print("Soviel Geld steht dir nicht zur Verfügung!")
                    input("Bitte [ENTER] drücken...")
                
            elif eingabe == "x":
                print("Du kehrst jetzt in das Hauptmenü zurück.")
                input("Bitte [ENTER] drücken...")
                break
                
            else:
                print("Das habe ich nicht verstanden!")
                input("Bitte [ENTER] drücken...")
    
    
    elif eingabe == "x":
        print("Auf Wiedersehen!")
        exit()
    
    
    else:
        print("Das habe ich nicht verstanden!")
        input("Bitte [ENTER] drücken...")
    
