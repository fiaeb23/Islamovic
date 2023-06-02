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
        "name": "admin",
        "pin": "0000",
        "balance": 0
    },
    {
        "name": "Esad",
        "pin": "1234",
        "balance": 0
    },
    {
        "name": "Rafael",
        "pin": "9876",
        "balance": 100
    },

]

login_successful = False
tries = 1
while True:
    os.system("cls")
    print("Willkommen bei der PyBank!")
    print("Bitte einloggen!")
    print("Versuch", tries, "von", 3)
    name = input("Name: ")
    pin = input("PIN: ")
    
    for i in range(len(user_db)):
        elem = user_db[i]
        if elem["name"] == name and elem["pin"] == pin:
            login_successful = True
            idx = i
            break         

    tries += 1
    
    if login_successful:
        print("Erfolgreich eingeloggt!")
        os.system("pause")
        break
    elif tries <= 3:
        print("Das hat nicht geklappt. Versuchs nochmal!")
        os.system("pause")
    elif tries > 3:
        print("Du hast zu häufig falsche Daten eingegeben!")
        print("Das Programm wird jetzt beendet!")
        exit()

while True:
    os.system("cls")
    print("### Bank-System ###")
    print("Du hast folgende Optionen:")
    print("[1] Kontostand anzeigen")
    print("[2] Kontostand erhöhen")
    print("[3] Kontostand verringern")
    if user_db[idx]["name"] == "admin":
        print("[4] Admin-Menü")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        os.system("cls")
        print("Aktueller Kontostand:")
        print(f"{user_db[idx]['balance']:.2f} €")
        os.system("pause")
        
    elif eingabe == "2":
        while True:
            os.system("cls")
            print("Kontostand erhöhen:")
            print("Gib eine Zahl ein oder [x] um zu beenden!")
            value = input(">>> ")
            # value = value.split(".")
            
            if value.isdecimal() and int(value) > 0:
                value = int(value)
                user_db[idx]["balance"] += value
                print("Dir wurde", value, "gutgeschrieben!")
                os.system("pause")
                break
                
            elif value == "x":
                print("Alles klar, zurück ins Hauptmenü!")
                os.system("pause")
                break
                
            else:
                print("Das ist keine valide Eingabe!")
                os.system("pause")
        
    elif eingabe == "3":
        while True:
            os.system("cls")
            print("Kontostand erhöhen:")
            print("Gib eine Zahl ein oder [x] um zu beenden!")
            value = input(">>> ")
            # value = value.split(".")
            
            if value.isdecimal() and 0 < int(value):
                value = int(value)
                if value > user_db[idx]["balance"]:
                    print("Soviel Geld steht nicht zur Verfügung!")
                    os.system("pause")
                    continue
                    
                user_db[idx]["balance"] -= value
                print("Dein Kontostand wurde um", value, "verringert!")
                os.system("pause")
                break
            
            elif value == "x":
                print("Alles klar, zurück ins Hauptmenü!")
                os.system("pause")
                break
                
            else:
                print("Das ist keine valide Eingabe!")
                os.system("pause")
                
    elif eingabe == "4" and user_db[idx]["name"] == "admin":
        while True:
            os.system("cls")
            print("Willkommen im Admin-Menü")
            print("[1] Nutzer hinzufügen")
            if len(user_db) > 1:
                print("[2] Nutzer entfernen")
            print("[x] Zum Hauptmenü")
            print(user_db)
            eingabe = input(">>> ")
            
            if eingabe == "1":
                while True:
                    os.system("cls")
                    print("Nutzer hinzufügen")
                    print("Bitte Name eingeben (mind. 1 Zeichen!)")
                    new_name = input("Name: ")
                    
                    if len(new_name) == 0:
                        print("Name darf nicht leer sein!")
                        os.system("pause")
                        continue
                    
                    print("Bitte PIN eingeben (genau 4 Zeichen!)")
                    new_pin = input("PIN: ")
                    
                    if len(new_pin) != 4:
                        print("PIN muss genau 4 Zeichen lang sein!")
                        os.system("pause")
                        continue
                        
                    user_db.append(
                        {
                            "name": new_name,
                            "pin": new_pin,
                            "balance": 0
                        }
                    )
                    
                    print("Vielen Dank!")
                    os.system("pause")
                    break
    
            elif eingabe == "2" and len(user_db) > 1:
                while True:
                    os.system("cls")
                    print("Nutzer entfernen")
                    print("Welchen Nutzer willst du entfernen?")
                    
                    # user_db[1:], start=1 -> admin ignorieren
                    for i, elem in enumerate(user_db[1:], start=1):
                        print(f"[{i}] Name: {elem['name']}")
                        
                    eingabe = input(">>> ")
                    
                    if eingabe.isdecimal() and 1 <= int(eingabe) <= len(user_db):
                        print("Nutzer", user_db[int(eingabe)]["name"], "wird entfernt!")
                        user_db.pop(int(eingabe))
                        os.system("pause")
                        break
                        
                    else:
                        print("Das ist keine valide Eingabe!")
                        os.system("pause")
                        
            elif eingabe == "x":
                print("Es geht zurück ins Hauptmenü!")
                os.system("pause")
                break
                
            else:
                print("Das habe ich nicht verstanden!")
                os.system("pause")
            
    
    elif eingabe == "x":
        pass
        exit()
        
    else:
        print("Das habe ich nicht verstanden!")
        os.system("pause")


