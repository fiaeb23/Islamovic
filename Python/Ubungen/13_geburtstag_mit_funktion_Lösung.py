
def zahl_eingeben(input_text, untergrenze, obergrenze):
    while True:
        eingabe = input(input_text)
        
        if eingabe.isdecimal() and untergrenze <= int(eingabe) <= obergrenze:
            print("Vielen Dank!")
            return int(eingabe)
        else:
            print("Das ist keine valide Eingabe!")

def alter_berechnen(t, m, j):
    """
    Diese Funktion soll mithilfe der Parameter:
    - t (Geburtstag)
    - m (Geburtsmonat)
    - j (Geburtsjahr)
    und den Variablen 
    - aktueller_tag
    - aktueller_monat
    - aktuelles_jahr 
    das Alter einer Person berechnen.
    """
    
    if type(t) != int or type(m) != int or type(j) != int:
        return None
    
    aktueller_tag = 14
    aktueller_monat = 4
    aktuelles_jahr = 2023
    # t = 1
    # m = 1
    # j = 2000
    if m < aktueller_monat:
        return aktuelles_jahr - j
    elif m == aktueller_monat:
        if t <= aktueller_tag:
            return aktuelles_jahr - j
        else:
            return aktuelles_jahr - j - 1
    else:
        return aktuelles_jahr - j - 1


# 1) Eingabe des Geburtstags
#    - Min: 1
#    - Max: 31
x = zahl_eingeben("Geburtstag: ", 1, 31)

# 2) Eingabe des Geburtsmonats
#    - Min: 1
#    - Max: 12
y = zahl_eingeben("Geburtsmonat: ", 1, 12)

# 3) Eingabe des Geburtsjahres
#    - Min: 1900
#    - Max: 2022
z = zahl_eingeben("Geburtsjahr: ", 1900, 2022)


print(str(x)+"."+str(y)+"."+str(z)) 

print("Du bist", alter_berechnen(x, y, z), "Jahre alt")

