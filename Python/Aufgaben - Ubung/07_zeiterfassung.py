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



# summe = 0
# counter = 1

# while counter < 11:
#     print(counter)
#     summe = summe + counter
#     counter = counter + 1
   
# print("Summe:", summe)
# print("Durchschnitt:", summe/(counter-1))



#AUFGABE

#Zeiterfassungsprogramm

print ("Zeiterfassungsprogramm")
#definierung
import datetime
start_date = datetime.date (2023, 3, 1)                                                                               #startdatum
end_date = datetime.date (2023, 3, 4)                                                                                 #enddatum

total_hours = 0                                                                                                       #definierung von gesamtzeit (beginn bei 0)
num_days = 0                                                                                                          #definierung von gesamttage (beginn bei 0)

#befehl                                                                                                                                                                         
for single_date in (start_date + datetime.timedelta(i) for i in range((end_date - start_date).days + 1)):             #stardatum + datumformat(i) für i definiere die Range (enddatum+startdatum).days + 1 
#                                                                                                                                                                          #(definiertung) von num_days + 1            
    print(f"Trage deine Arbeitszeit ein {single_date.strftime('%d-%m-%Y')}: ")                                        #single_date.strftime('%Y-%m-%d')} = definierung vom string in datum d-m-Y
    hours_worked = input()                                                                                            #eingabe stunden

    while not (hours_worked.isdecimal() and int(hours_worked) > 0 and int(hours_worked) <= 10):                       #abfrage eingebene Zahl zwischen 10
        
        print("Falsche Eingabe! Bitte Trage eine Zahl zwischen 1 und 10 ein: ")                                       #erneute eingabe
        hours_worked = input()                                                                                        #eingabe stunde

    
    
    total_hours += int(hours_worked)                                                                                  #gesamtzeit -> füge gearbeitete stunden in gesamt ein
    num_days += 1                                                                                                     #rechne plus 1 Tag

average_hours = total_hours / num_days                                                                                #berechne durschnitt aus gesamtstunden/tage

print (f"Gesamtearbeitszeit: {total_hours}")
print (f"Durschnittlich hast du pro Tag {average_hours} gearbeitet")



#Variable 2 

# print("Zeiterfassungsprogramm")

# import datetime

# start_datum = datetime.date(2023, 3, 1)
# ende_datum = datetime.date(2023, 3, 4)

# gesamte_arbeitzeit = 0
# gesamte_tage = 0

# for i in range((ende_datum - start_datum).days + 1):
#     datum = start_datum + datetime.timedelta(i)
#     datum_string = datum.strftime("%d.%m.%Y")
    
#     arbeitszeit = input(f"Trage deine Arbeitszeit für den {datum_string} ein: ")

#     while not (arbeitszeit.isdecimal() and (int(arbeitszeit) > 0) and (int(arbeitszeit) <= 10)):
#         print("Falsche Eingabe, trage eine korrekte Zahl zwischen 1-10 ein!")
#         arbeitszeit = input()

#     gesamte_arbeitzeit += int(arbeitszeit)
#     gesamte_tage += 1

# if gesamte_tage > 0:
#     print("Gesamte Arbeitszeit:", gesamte_arbeitzeit)
#     print("Durchschnitt:", gesamte_arbeitzeit / gesamte_tage)
# else:
#     print("Keine Arbeitszeiten eingegeben.")



#VARIABLE 3

# import datetime

# start_datum = "01.03.2023"
# end_datum = "04.03.2023"

# # Konvertierung der Datumsangaben in das datetime-Format
# start_datum = datetime.datetime.strptime(start_datum, "%d.%m.%Y")
# end_datum = datetime.datetime.strptime(end_datum, "%d.%m.%Y")

# # Berechnung des Zeitraums zwischen den Datumsangaben
# zeitraum = end_datum - start_datum

# # Initialisierung der Variablen
# summe_arbeitszeit = 0
# anzahl_tage = 0

# # Schleife über alle Tage des Zeitraums
# for i in range(zeitraum.days + 1):
#     datum = start_datum + datetime.timedelta(days=i)
#     tag = datum.day
#     monat = datum.month
#     jahr = datum.year

#     # Nutzereingabe für die Arbeitszeit des Tages
#     eingabe = input(f"Arbeitszeit am {tag}.{monat}.{jahr}: ")

#     # Überprüfung, ob die Eingabe nur aus Zahlen besteht und zwischen 0 und 10 liegt
#     while not (eingabe.isdecimal() and 0 < int(eingabe) <= 10):
#         print("Ungültige Eingabe")
#         print("Trage bitte eine gültige Zeit ein (zwischen 1-10)!")
#         eingabe = input()

#     # Addieren der Arbeitszeit zum Gesamtwert und Inkrementierung des Tageszählers
#     summe_arbeitszeit += int(eingabe)
#     anzahl_tage += 1

# # Ausgabe der Gesamt- und Durchschnittsarbeitszeit, wenn mindestens ein Tag erfasst wurde
# if anzahl_tage > 0:
#     durchschnittliche_arbeitszeit = summe_arbeitszeit / anzahl_tage
#     print(f"Gesamtarbeitszeit: {summe_arbeitszeit} Stunden")
#     print(f"Durchschnittliche Arbeitszeit: {durchschnittliche_arbeitszeit} Stunden pro Tag")
# else:
#     print("Keine Arbeitszeit erfasst.")
