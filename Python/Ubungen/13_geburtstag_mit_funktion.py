
def zahl_eingeben(input_text, untergrenze, obergrenze):
    while True:
        eingabe = input(input_text)
        
        if eingabe.isdecimal() and untergrenze <= int(eingabe) <= obergrenze:
            print("Vielen Dank!")
            return int(eingabe)
        else:
            print("Das ist keine valide Eingabe!")

def alter_berechnen(t, m, j):
    aktuelles_jahr = 2023
    geburtsdatum = j * 10000 + m * 100 + t                          # z.B. 19900520 -> 1990.05.20
    aktuelles_datum = aktuelles_jahr * 10000 + 4 * 100 + 14         # z.B. 20230414 -> 2023.04.14         
    alter = (aktuelles_datum - geburtsdatum) // 10000
    return alter

# def alter_berechnen(t, m, j):
#     aktuelles_jahr = 2023
#     alter = aktuelles_jahr - j - ((aktuelles_jahr, m < t) <= (j, m >= t))
#     return alter

def tag():
    aktuelles_tag = 14
    aktuelles_monat = 4
    aktuelles_jahr = 2023
    return aktuelles_tag, aktuelles_monat, aktuelles_jahr


print("Bitte geben Sie Ihr Geburtsdatum ein:")
t = zahl_eingeben("Gebe den Tag ein (1-31): ", 1, 31)
m = zahl_eingeben("Gebe den Monat ein (1-12): ", 1, 12)
j = zahl_eingeben("Gebe das Jahr ein (1900-2022): ", 1900, 2022)


alter = alter_berechnen(t, m, j)
print("Ihr Alter ist:", alter)



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

