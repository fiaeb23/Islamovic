print("Zeiterfassungsprogramm")

import datetime

start_datum = datetime.date(2023, 3, 1)
ende_datum = datetime.date(2023, 3, 4)

gesamte_arbeitzeit = 0
gesamte_tage = 0

for i in range((ende_datum - start_datum).days + 1):
    datum = start_datum + datetime.timedelta(i)
    datum_string = datum.strftime("%d.%m.%Y")

    arbeitszeit = input(f"Trage deine Arbeitszeit für den {datum_string} ein: ")

    while not (arbeitszeit.isdecimal() and (int(arbeitszeit) > 0) and (int(arbeitszeit) <= 10)):
        print("Falsche Eingabe, trage eine korrekte Zahl zwischen 1-10 ein!")
        arbeitszeit = input()

    gesamte_arbeitzeit += int(arbeitszeit)
    gesamte_tage += 1

if gesamte_tage > 0:
    print("Gesamte Arbeitszeit:", gesamte_arbeitzeit)
    print("Durchschnitt:", gesamte_arbeitzeit / gesamte_tage)
else:
    print("Keine Arbeitszeiten eingegeben.")
