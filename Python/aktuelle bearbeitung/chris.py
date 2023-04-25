import random
import os


anzahl = 10
spielfeld_s = [None] * anzahl  # [None, None, None, ....]
spielfeld_c = [None] * anzahl
spielfeld_s[0] = "S"
spielfeld_c[0] = "C"

print (spielfeld_c)
print (spielfeld_s)


würfel_s = random.randint(1, 6)
würfel_c = random.randint(1, 6)


spielfeld_s_neu = 0
spielfeld_c_neu = 0




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
            # alte Position = Spieler-Posi
            # Spieler-Posi += Würfel
            # Neue_Posi = spieler_posi






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
    #"""
