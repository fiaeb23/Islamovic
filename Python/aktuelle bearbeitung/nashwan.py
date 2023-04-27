# import datetime

# # Zunächst definieren wir die Start- und Enddaten des Zeitraums
# start_datum = datetime.date(2023, 3, 1)
# end_datum = datetime.date(2023, 3, 4)

# summe_arbeitszeit = 0
# anzahl_tage = 0

# for date in (start_datum + datetime.timedelta(i) for i in range((end_datum - start_datum).days + 1)):
#     date_string = date.strftime("%d.%m.%Y")
    
#     eingabe = input(f"Arbeitszeit am {date_string}: ")
 
#     while not (eingabe.isdecimal() and 0 < int(eingabe) <= 10):
#         print("Ungültige Eingabe")
#         print("Trage bitte eine gültige Zeit ein (zwischen 1-10)!")
#         eingabe = input()
             
#     summe_arbeitszeit += int(eingabe)
#     anzahl_tage += 1  

# if anzahl_tage > 0:
#     durchschnittliche_arbeitszeit = round(summe_arbeitszeit / anzahl_tage, 2)
#     print(f"Gesamtarbeitszeit: {summe_arbeitszeit} Stunden")
#     print(f"Durchschnittliche Arbeitszeit: {round(summe_arbeitszeit / anzahl_tage, 2)} Stunden pro Tag")



import os

kontostand = 100
PIN = 2468

print("HERZLICH WILKOMMEN BEI PY.BANK")
print("---------(*^^*)-------------")
username = input("schreiben Sie bitte ihre username: ")
    
 #While True:
  # print("HALLO:", username)
   
pin = input("schreiben Sie bitte ihre PIN")
    if pin == PIN:
        while True:
        print("lass uns los gehen")
            if eingabe.isdecimal():
            print("Vielen Dank")
            input("Bitte [ENTER] drücken...")
            
               
            while True:
            os.system("cls")
            print(" Sie haben :", kontostand ," € im konto")
            print("-------------------------------------------")
            m1 = print("für EINZAHLUNG drücken sie bitte [1]")
            m2 = print("für AUSZAHLUNG drücken sie bitte [2]")
            m3 = print("für KONTOSTAND drücken sie bitte [3]")
            m4 = print ("für  BEENDEN  drücken sie bitte [4]")
            print("-------------------------------------------")
            ausgabe = input("schreiben Sie ein Zahl ihres wünsch: ")
            print("ausgabe")
                        
            if ausgabe == 1:
                print("EINZAHLUNG ")    
            



    else:    
        print("Sie haben falsch PIN eingegeben")
                    
        
        


import os

kontostand = 100
pin = 1234

print("HERZLICH WILKOMMEN BEI PY.BANK")
print("---------(*^^*)-------------")
#username = int(input("schreiben Sie bitte ihre username: "))
    
while:
print("HALLO:")
  
PIN = int(input("schreiben Sie bitte ihre PIN"))

while pin != PIN :
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')

        os.system("cls")
        print("-------------------------------------------")
        m1 = print("für EINZAHLUNG drücken sie bitte [1]")
        print(" Sie haben :", kontostand ," € im konto")
        m2 = print("für AUSZAHLUNG drücken sie bitte [2]")
        m3 = print("für KONTOSTAND drücken sie bitte [3]")
        m4 = print ("für  BEENDEN  drücken sie bitte [4]")
        print("-------------------------------------------")
        ausgabe = input("schreiben Sie ein Zahl ihres wünsch: ")
        print("ausgabe")
                        
        if ausgabe == 1:
            print("EINZAHLUNG ")    
            



else:    
    print("Sie haben falsch PIN eingegeben")
