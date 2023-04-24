""" ZAHLEN-RATE-SPIEL

a) Schreibe ein Programm, welches den Nutzer die geheime
   Zahl des Computers (Ganzzahl zwischen 1 und 10) erraten lässt.
   - Der Nutzer hat bis zu 2 Versuche
   - Sollte er es im ersten Versuch schaffen, kommt es
     nicht zu einem zweiten Versuch
   - Sollte er es im ersten Versuch nicht schaffen, hat
     er im zweiten eine weitere Chance

bonus) Gebe dem Nutzer Tipps, ob er zu hoch oder zu 
       niedrig geraten hat.
"""
import random

# EINGABE
bot_nr = random.randint(1, 10) # zufälliger int zw. 1 und 10
print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
usr_nr = input("Zahl: ")

# VERARBEITUNG
usr_nr = int(usr_nr)
beide_zahlen_gleich = bot_nr == usr_nr

# AUSGABE
if beide_zahlen_gleich:
    print("Du hast gewonnen!")
else:
    if usr_nr < 1 or usr_nr > 10:
        print("Deine Zahl muss zwischen 1 und 10 liegen!")
    print("Das ist nicht richtig. Probiers nochmal!")
    
    if usr_nr > bot_nr:
        print("Die gesuchte Zahl ist kleiner!")
    else:
        print("Die gesuchte Zahl ist größer!")
    
    
    print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
    usr_nr = int(input("Zahl: "))
    if bot_nr == usr_nr:
        print("Du hast gewonnen!")
    else:
        print("Du hast leider verloren.")
        print("Bot hatte:", bot_nr)


