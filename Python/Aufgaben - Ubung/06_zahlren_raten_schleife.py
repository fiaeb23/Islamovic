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
versuch = 1

while versuch < 3:
    print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
    usr_nr = int(input("Zahl: "))
    if versuch == 1:
        pass
    
    if bot_nr == usr_nr:
        print("Du hast gewonnen!")
        break
    else:
        versuch = versuch + 1
        if usr_nr < 1 or usr_nr > 10:
            print("Deine Zahl muss zwischen 1 und 10 liegen!")
        print("Das ist nicht richtig. Probiers nochmal!")
        
        if usr_nr > bot_nr:
            print("Die gesuchte Zahl ist kleiner!")
        else:
            print("Die gesuchte Zahl ist größer!")
            
            
"""
Erweitere das Programm:
- Die Meldungen:
  - Zahl muss zwischen 1 und 10 liegen
  - Gesuchte Zahl ist größer/kleiner
  sollen nur erscheinen, wenn man sich im ersten Versuch
  befindet.
- Die Meldung:
  - Du hast verloren
  soll nur erscheinen, wenn man sich im letzten versuch
  befindet und falsch geraten hat

"""
        
        
        


