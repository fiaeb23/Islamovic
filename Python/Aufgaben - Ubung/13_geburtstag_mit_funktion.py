
def zahl_eingeben(input_text, untergrenze, obergrenze):
    while True:
        eingabe = input(input_text)
        
        if eingabe.isdecimal() and untergrenze <= int(eingabe) <= obergrenze:
            print("Vielen Dank!")
            return int(eingabe)
        else:
            print("Das ist keine valide Eingabe!")

def alter_berechnen(eingabe,tag):
    alter = (tag - eingabe)
    print (alter)
        


def aktueller_tag(t,m,j):
    aktuelles_tag = 14
    aktuelles_monat = 4
    aktuelles_jahr = 2023
    tag = aktuelles_tag,aktuelles_monat,aktuelles_jahr
    print (tag)

 #   return alter 

zahl_eingeben()



# # 1) Eingabe des Geburtstags
# #    - Min: 1
# #    - Max: 31
# t = zahl_eingeben("Geburtstag: ", 1, 31)

# # 2) Eingabe des Geburtsmonats
# #    - Min: 1
# #    - Max: 12
# m = zahl_eingeben("Geburtsmonat: ", 1, 12)

# # 3) Eingabe des Geburtsjahres
# #    - Min: 1900
# #    - Max: 2022
# j = zahl_eingeben("Geburtsjahr: ", 1900, 2022)

# """
#     Diese Funktion soll mithilfe der Parameter:
#     - t (Geburtstag)
#     - m (Geburtsmonat)
#     - j (Geburtsjahr)
#     und der Variable `aktuelles_jahr` das Alter
#     einer Person berechnen.
#  """



# print(str(t)+"."+str(m)+"."+str(j)) 
# print(f"{t:02}.{m}.{j}")

