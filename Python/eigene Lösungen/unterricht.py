"""
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


"""



#Bank Beispiel

PIN = "1234"  # Der PIN für das Konto

balance = 1000  # Der Kontostand 

# Hauptmenü
def main_menu():
    print('BANK OF KRÖMER')
    print("Willkommen bei Ihrer Bank!")
    print(f"Ihr aktueller Kontostand beträgt: {balance} €")
    print("1. Geild einzahlen")
    print("2. Geld abheben")
    print("3. Beenden")

    auswahl = input("Wählen Sie eine Option aus (1-3): ")
    if auswahl == "1":
        increase_balance()
    elif auswahl == "2":
        decrease_balance()
    elif auswahl == "3":
        exit()
    else:
        print("Ungültige Eingabe!")
        main_menu()

# Funktion zur Erhöhung des Kontostands
def increase_balance():
    global balance
    amount = input("Geben Sie den Betrag ein, den Sie einzahlen wollen: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Ungültiger Betrag!")
        increase_balance()
        return
    balance += amount
    print(f"Ihr Kontostand beträgt jetzt: {balance} €")
    main_menu()

# Funktion zur Verringerung des Kontostands
def decrease_balance():
    global balance
    amount = input("Geben Sie den Betrag ein, um den Sie Ihren Kontostand verringern möchten: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Ungültiger Betrag!")
        decrease_balance()
        return
    if amount > balance:
        print("Sie haben nicht genug Geld auf Ihrem Konto!")
        decrease_balance()
        return
    balance -= amount
    print(f"Ihr Kontostand beträgt jetzt: {balance} €")
    main_menu()

# PIN-Abfrage
def login():
    pin = input("Geben Sie Ihre PIN ein: ")
    if pin == PIN:
        main_menu()
    else:
        print("Falsche PIN!")
        login()

login()  # Startet das Programm mit der PIN-Abfrage