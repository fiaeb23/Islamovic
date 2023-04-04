# import os

# while True:
#     os.system("cls") # Bildschirm säubern
#     print("Du befindest dich im Hauptmenü")
#     print("Du hast folgende Optionen:")
#     print("[1] Untermenü 1")
#     print("[2] Untermenü 2")
#     print("[x] Programm beenden")
#     eingabe = input(">>> ")
    
#     if eingabe == "1":
#         while True:
#             os.system("cls")
#             print("Du befindest dich im Untermenü 1")
#             print("Bitte Zahl eingeben oder 'x' zum Beenden")   
#             eingabe = input(">>> ")
            
#             if eingabe.isdecimal():
#                 print("Vielen Dank")
#                 input("Bitte [ENTER] drücken...")
#                 break
                
#             elif eingabe == "x":
#                 print("Du kehrst jetzt in das Hauptmenü zurück.")
#                 input("Bitte [ENTER] drücken...")
#                 break
                
#             else:
#                 print("Das habe ich nicht verstanden!")
#                 input("Bitte [ENTER] drücken...")
        
          
#     elif eingabe == "2":
#         pass
    
    
#     elif eingabe == "x":
#         print("Auf Wiedersehen!")
#         exit()
    
    
#     else:
#         print("Das habe ich nicht verstanden!")
#         input("Bitte [ENTER] drücken...")
    
# """

# """
# Entwickle ein Bank-System

# Der Nutzer hat einen Kontostand, welcher zu Beginn bei 100 liegt.
# Im Hauptmenü wird dem Nutzer der aktuelle Kontostand angezeigt.

# Über das Untermenü 1 kann der Nutzer den Kontostand erhöhen
# - Der Geldbetrag MUSS eine Zahl sein
# - Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

# Über das Untermenü 2 kann der Nutzer den Kontostand verringern
# - Der Geldbetrag MUSS eine Zahl sein
# - Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

# BONUS) Der Nutzer darf nicht mehr Geld abheben (Untermenü 2)
#        als ihm zur Verfügung steht

# BONUS_2) Implementiere eine PIN-Abfrage für das Konto
# """













import os

PIN = "1010"                                                                # Der PIN für das Konto

balance = 1000                                                              # Der Kontostand 

def main_menu():                                                            #definierung menü
    print('BANK OF KRÖMER')
    print("Willkommen bei Ihrer Bank!")
    print(f"Ihr aktueller Kontostand beträgt: {balance} €")
    print("[1]. Geild einzahlen")
    print("[2]. Geld abheben")
    print("[3]. Beenden")

    auswahl = input (">>> ")
    if auswahl == "1":
        geld_einzahlen()
    elif auswahl == "2":
        geld_abheben()
    elif auswahl == "3":
        exit()
    else:
        print("Ungültige Eingabe!")
        main_menu()

def geld_einzahlen():
    global balance
    print(f"Ihr aktueller Kontostand beträgt: {balance} €")
    einzahlung = input ("Geben Sie den Betrag ein, den Sie einzahlen wollen: ")
    einzahlung = float(einzahlung)
    balance += einzahlung 

    print (f"Ihr neuer Kontostand beträgt jetzt: {balance} €")
    os.system("cls")
    main_menu()


def geld_abheben():
    global balance
    
    print(f"Ihr aktueller Kontostand beträgt: {balance} €")
    abhebung = input ("Geben Sie den Betrag ein, den Sie auszahlen wollen: ")
    abhebung = float(abhebung)
    if abhebung > balance:
        print ("Sie haben nicht genug Geld auf dem Konto.")
        geld_abheben()

    balance -= abhebung
    print (f"Ihr neuer Kontostand beträgt jetzt: {balance} €")
    os.system("cls")
    main_menu()


def login():
    pin = input('Geben Sie Ihren PIN ein:  ')
    if pin == PIN:
        print('PIN korrekt!')
        main_menu()
    else:
        print("Falscher PIN!")
        login()                                                                 # restart bei login
login()                                                                         # Startet das Programm mit der PIN-Abfrage



