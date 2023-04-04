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
