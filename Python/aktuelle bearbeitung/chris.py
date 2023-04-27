'''''
import random
import os


anzahl = 10
#spielfeld
spielfeld_s = [None] * anzahl  # [None, None, None, ....]
spielfeld_c = [None] * anzahl
#player
spielfeld_s[0] = "S"
spielfeld_c[0] = "C"

print (spielfeld_c)
print (spielfeld_s)


würfel_s = random.randint(1, 6)
würfel_c = random.randint(1, 6)


spielfeld_s_neu = 0
spielfeld_c_neu = 0

def würfeln():
    würfel = random.randint (1,6)
    return


würfel_s_zw = random.randint(1, 6)
würfel_c_zw = random.randint(1, 6)


while True:
    os.system("cls")
    print("Mensch ärgere dich nicht - arme Ritter Version")
    print(spielfeld_s)
    print(spielfeld_c)
    print()
    print("[1] Würfeln")
    print("[2] Neu anfangen (Reset)")
    print("[3] BONUS FELDER")
    print("[x] Exit")
    eingabe = input(">>> ")




    ## WÜRFELN ##
    if eingabe == "1":


        while True: #spielfeld_s.index("S") is not 10:


            ## SPIELER ##
            würfel_s = random.randint(1, 6)
            spielfeld_s[spielfeld_s.index("S")] = None
            spielfeld_s[würfel_s] = "S"
            print("Der Spieler ist um", spielfeld_s.index("S"), "weiter gerückt")




            ## BOT ##
            würfel_s = random.randint(1, 6)
            spielfeld_c[spielfeld_c.index("C")] = None
            spielfeld_c[würfel_c] = "C"
            print("Der Bot ist um", spielfeld_c.index("C"), "weiter gerückt")




            spielfeld_s = spielfeld_s_neu.index("S")
            spielfeld_s += würfel_s
            spielfeld_s_neu = spielfeld_s.index("S")
        






            ##########################################




            ## Gewonnen, Verloren und Tie ##
            if spielfeld_s_neu >= 10:
                print("Du hast Gewonnen!")
            elif spielfeld_c_neu >= 10:
                print("Der Computer hat Gewonnen!")
            elif spielfeld_c_neu >= 10 and spielfeld_s_neu >= 10:
                print("Unentschieden! Nochmal 10 Felder!")
                spielfeld_s[spielfeld_s.index("S")] = None
                spielfeld_c[spielfeld_c.index("C")] = None
                spielfeld_s = [None] * anzahl
                spielfeld_c = [None] * anzahl
                spielfeld_s[0] = "S"
                spielfeld_c[0] = "C"


            os.system("pause")
            break




    ## RESET ##
    if eingabe == "2":
        if "S" not in spielfeld_s and "C" not in spielfeld_c:
            print("Fehler, bitte Programm neu starten!")
            break
        else:
            spielfeld_s[spielfeld_s.index("S")] = None
            spielfeld_c[spielfeld_c.index("C")] = None
            spielfeld_s = [None] * anzahl
            spielfeld_c = [None] * anzahl
            spielfeld_s[0] = "S"
            spielfeld_c[0] = "C"




    ## EXPAND ##
    if eingabe == "3":
        if anzahl <= 10:
            print("Möchtest du die Rundenanzahl wirklich erhöhen bzw. ändern?")
            eingabe_mehrrunden = input(">>> ")
            if eingabe_mehrrunden == "Ja" or "ja" or "JA" or "ja":
                eingabe_mehrrunden_neu = input("Bitte Rundenangabe angeben: ")
                if eingabe_mehrrunden_neu.isdecimal():
                    spielfeld_s = [None] * int(eingabe_mehrrunden_neu)
                    spielfeld_c = [None] * int(eingabe_mehrrunden_neu)
                    spielfeld_s[0] = "S"
                    spielfeld_c[0] = "C"
                else:
                    print("Das habe ich nicht verstanden!")
                    os.system("pause")
            else:
                print("Abgebrochen - Zurück...")
                os.system("pause")
        else:
            print("Das habe ich nicht verstanden!")
            os.system("pause")




    ## EXIT ##
    if eingabe == "x":
        os.system("cls")
        print("Bye")
        os.system("pause")
        exit()
'''


import random
import os

anzahl = 10
spielfeld_s = [None] * anzahl
spielfeld_c = [None] * anzahl
spielfeld_s[0] = "S"
spielfeld_c[0] = "C"

def print_spielfeld():
    print("Mensch ärgere dich nicht - arme Ritter Version")
    print(spielfeld_s)
    print(spielfeld_c)

def reset_spielfeld():
    global spielfeld_s, spielfeld_c
    spielfeld_s[spielfeld_s.index("S")] = None
    spielfeld_c[spielfeld_c.index("C")] = None
    spielfeld_s = [None] * anzahl
    spielfeld_c = [None] * anzahl
    spielfeld_s[0] = "S"
    spielfeld_c[0] = "C"

def expand_spielfeld():
    global anzahl, spielfeld_s, spielfeld_c
    eingabe = input("Möchtest du die Rundenanzahl wirklich erhöhen bzw. ändern? (Ja/Nein) ")
    if eingabe.lower() == "ja":
        neue_groesse = input("Bitte Rundenangabe angeben: ")
        if neue_groesse.isdecimal():
            anzahl = int(neue_groesse)
            spielfeld_s = [None] * anzahl
            spielfeld_c = [None] * anzahl
            spielfeld_s[0] = "S"
            spielfeld_c[0] = "C"
        else:
            print("Falsche Eingabe!")
            os.system("pause")
    else:
        print("Abgebrochen.")
        os.system("pause")

while True:
    os.system("cls")
    print_spielfeld()
    print("[1] Würfeln")
    print("[2] Neu anfangen (Reset)")
    print("[3] BONUS FELDER")
    print("[x] Exit")
    eingabe = input(">>> ")

    if eingabe == "1":
        while True:
            wurfel_s = random.randint(1, 6)
            wurfel_c = random.randint(1, 6)
            spielfeld_s_neu = spielfeld_s.index("S") + wurfel_s
            spielfeld_c_neu = spielfeld_c.index("C") + wurfel_c

            spielfeld_s[spielfeld_s.index("S")] = None
            spielfeld_s[spielfeld_s_neu] = "S"
            print("Der Spieler ist um", wurfel_s, "weiter gerückt")

            spielfeld_c[spielfeld_c.index("C")] = None
            spielfeld_c[spielfeld_c_neu] = "C"
            print("Der Bot ist um", wurfel_c, "weiter gerückt")

            if spielfeld_s_neu >= anzahl:
                print("Du hast gewonnen!")
                os.system("pause")
                reset_spielfeld()
                break

            if spielfeld_c_neu >= anzahl:
                print("Der Computer hat gewonnen!")
                os.system
