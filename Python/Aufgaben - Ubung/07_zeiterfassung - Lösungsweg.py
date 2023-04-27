"""
Entwickle ein Zeiterfassungsprogramm

Dabei soll der Nutzer für einen bestimmten Zeitraum
eintragen, wieviel er pro Tag gearbeitet hat.

Betrachtet wird der Zeitraum 01.03.2023 bis 04.03.2023.

Pro Tag gibt der Nutzer die geleistete Arbeitszeit ein
(z.B. 8 für Acht Stunden)

Anschließend wird die Summe der Arbeitszeiten gebildet & ausgegeben
und die durchschnittlich gearbeitete Zeit ausgegeben

Benötigt wird eine Nutzereingabe für die es bestimmte Bedingungen gibt:
- str.isdecimal() um zu prüfen, ob die Nutzereingabe NUR aus Zahlen besteht
  (z.B.
   eingabe = input("Arbeitszeit: ")
   print(eingabe.isdecimal()) # wenn True, dann hat Nutzer nur Zahlen eingegeben
- Die Arbeitszeit muss über 0 Stunden liegen
- Die Arbeitszeit darf nicht höher als 10 Stunden liegen
"""



summe = 0
counter = 1

while counter < 11:
    print(counter)
    summe = summe + counter
    counter = counter + 1
   
print("Summe:", summe)
print("Durchschnitt:", summe/(counter-1))




'''
summe = 0
counter = 1

print("Bitte Arbeitszeit als Ganzzahl eingeben:")
while counter < 11:

    if counter < 10:
        arbeitszeit = input("Für 0"+str(counter)+".03.2023: ")
    else:
        arbeitszeit = input("Für "+str(counter)+".03.2023: ")
        
    """ Alternativ mit f-strings:
    arbeitszeit = input(f"Für {int(counter):02}.03.2023: ") 
    """
    
    if arbeitszeit.isdecimal() and 0 < int(arbeitszeit) < 11:
        print("Vielen Dank!")
        summe = summe + int(arbeitszeit)
        counter = counter + 1
    else:
        print("Das ist keine valide Eingabe!")

print()   
print("Summe:", summe)
print("Durchschnitt:", summe/(counter-1))
'''