import random

print ("Spiel Schere,Stein,Papier mit mir")
print ("Wähle zwischen Schere (s),Stein (r),Papier (p)")

eingabe = input("Deine Wahl: ")

#def von Spielzuegen durch []
zuege = ["s", "p", "r"]

#abfrage vom der Eingabe, ob ein gueltiger zug 
if eingabe in zuege:

#zufallige ausgabe mit random.shuffle
  random.shuffle(zuege)
  KI = zuege [0]
  print ("KI " + KI)

#abfrage vom ergebnis der KI mit dem eigenen Ergebnis (verbund durch and)
if KI == eingabe:
    print ("Unentschieden")
if KI == "s" and eingabe == "p" : 
    print ("Du hast verloren!")
if KI == "s" and eingabe == "r" :     
    print ("Du hast verloren!")
if KI == "r" and eingabe == "p" : 
    print ("Du hast verloren!")
if KI == "r" and eingabe == "s" : 
    print ("Du hast verloren!")
if KI == "p" and eingabe == "s" : 
    print ("Du hast verloren!")
if KI == "p" and eingabe == "r" : 
    print ("Du hast verloren!")
else: 
    print ("Falsche Eingabe")