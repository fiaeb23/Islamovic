"""
Erstelle ein CLI-Tool mit dem sich ein Nutzerprofil darstellen lässt

Hole zunächst folgende Informationen vom Nutzer:
1) Name
   - Ein Name muss aus mind. 3 Zeichen bestehen
   - Ein Name darf keine Zahlen enthalten
2) Geburtsjahr
   - Es muss ein valides und "realistisches" Geburtsjahr sein
   - Das Mindestalter zur Nutzung des Programms ist 18
3) Wohnort
   - Ein Wohnort muss aus mind. 5 Zeichen bestehen
   - Ein Wohnort darf keine Zahlen enthalten
   
Anschließend kann der Nutzer über ein Menü:
- Seinen Namen verändern
  (beachte die Namens-Regeln!)
- Sein Geburtsjahr verändern
  (beachte die Geburtsjahr-Regeln!)
- Seinen Wohnort verändern
  (beachte die Wohnort-Regeln!)
- Programm beenden

Tipp: Verwende die len()-Funktion
"""
import os

while True:
    os.system("cls")
    print("Willkommen im Nutzerprofil!")
    print("Bitte einen Namen eingeben.")
    print("Ein Name muss mind. 3 Zeichen lang sein")
    print("und darf keine Zahlen enthalten.")
    name = input(">>> ")
    if len(name) < 3:
        print("Der Name muss mind. 3 Zeichen lang sein!")
        os.system("pause")
        continue
    
    nr = 0
    zahl_gefunden = False
    while not zahl_gefunden and nr <= 9:
        if str(nr) in name:
            print("Der Name darf keine Zahlen enthalten!")
            os.system("pause")
            zahl_gefunden = True
        nr = nr + 1
        
    if zahl_gefunden:
        continue
        
    break
    
print("Yay das hat geklappt!")
os.system("pause")

while True:
    os.system("cls")
    print("Bitte ein Geburtsjahr eingeben.")
    print("Das Mindestalter beträgt 18.")
    geburtsjahr = input(">>> ")
    
    if geburtsjahr.isdecimal() and 1900 <= int(geburtsjahr) <= 2005:
        geburtsjahr = int(geburtsjahr)
        break
    else:
        print("Das ist kein valides Geburtsjahr!")
        os.system("pause")

print("Yay das hat geklappt!")
os.system("pause")

while True:
    os.system("cls")
    print("Willkommen im Nutzerprofil!")
    print("Bitte einen Wohnort eingeben.")
    print("Ein Wohnort muss mind. 5 Zeichen lang sein")
    print("und darf keine Zahlen enthalten.")
    wohnort = input(">>> ")
    if len(wohnort) < 5:
        print("Der Wohnort muss mind. 5 Zeichen lang sein!")
        os.system("pause")
        continue
    
    nr = 0
    zahl_gefunden = False
    while not zahl_gefunden and nr <= 9:
        if str(nr) in wohnort:
            print("Der Wohnort darf keine Zahlen enthalten!")
            os.system("pause")
            zahl_gefunden = True
        nr = nr + 1
        
    if zahl_gefunden:
        continue
        
    break
    
print("Yay das hat geklappt!")
os.system("pause")


while True:
    os.system("cls")
    print("Hallo", name, "("+str(2023 - geburtsjahr)+")", "aus", wohnort)
    print("Du bist im Hauptmenü")
    print("Du hast folgende Optionen:")
    print("[1] Name verändern")
    print("[2] Geburtsjahr verändern")
    print("[3] Wohnort verändern")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        
        while True:
            os.system("cls")
            print("Bitte einen Namen eingeben oder 'x' zum verlassen")
            print("Ein Name muss mind. 3 Zeichen lang sein")
            print("und darf keine Zahlen enthalten.")
            eingabe = input(">>> ")
            
            if eingabe == "x":
                os.system("pause")
                break
            
            if len(eingabe) < 3:
                print("Der Name muss mind. 3 Zeichen lang sein!")
                os.system("pause")
                continue
            
            nr = 0
            zahl_gefunden = False
            while not zahl_gefunden and nr <= 9:
                if str(nr) in eingabe:
                    print("Der Name darf keine Zahlen enthalten!")
                    os.system("pause")
                    zahl_gefunden = True
                nr = nr + 1
                
            if zahl_gefunden:
                continue
            
            name = eingabe
            break
        
    elif eingabe == "2":
        
        while True:
            os.system("cls")
            print("Bitte ein Geburtsjahr eingeben oder 'x' zum verlassen.")
            print("Das Mindestalter beträgt 18.")
            eingabe = input(">>> ")
            
            if eingabe == "x":
                os.system("pause")
                break
            
            if eingabe.isdecimal() and 1900 <= int(eingabe) <= 2005:
                geburtsjahr = int(eingabe)
                break
            else:
                print("Das ist kein valides Geburtsjahr!")
                os.system("pause")
        
    elif eingabe == "3":
        
        while True:
            os.system("cls")
            print("Bitte einen Wohnort eingeben oder 'x' zum verlassen")
            print("Ein Wohnort muss mind. 5 Zeichen lang sein")
            print("und darf keine Zahlen enthalten.")
            eingabe = input(">>> ")
            
            if eingabe == "x":
                os.system("pause")
                break
            
            if len(eingabe) < 5:
                print("Der Wohnort muss mind. 5 Zeichen lang sein!")
                os.system("pause")
                continue
            
            nr = 0
            zahl_gefunden = False
            while not zahl_gefunden and nr <= 9:
                if str(nr) in eingabe:
                    print("Der Wohnort darf keine Zahlen enthalten!")
                    os.system("pause")
                    zahl_gefunden = True
                nr = nr + 1
                
            if zahl_gefunden:
                continue
            
            wohnort = eingabe
            break
        
    elif eingabe == "x":
        print("Auf Wiedersehen!")
        exit()
    
    else:
        print("Das habe ich nicht verstanden!")
        os.system("pause")
        
    