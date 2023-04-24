
# 1) Eingabe des Geburtstags
#    - Min: 1
#    - Max: 31
while True:
    eingabe = input("Geburtstag: ")
    
    if eingabe.isdecimal() and 1 <= int(eingabe) <= 31:
        print("Vielen Dank!")
        t = int(eingabe)
        break
    else:
        print("Das ist keine valide Eingabe!")

# 2) Eingabe des Geburtsmonats
#    - Min: 1
#    - Max: 12
while True:
    eingabe = input("Geburtsmonat: ")
    
    if eingabe.isdecimal() and 1 <= int(eingabe) <= 12:
        print("Vielen Dank!")
        m = int(eingabe)
        break
    else:
        print("Das ist keine valide Eingabe!")


# 3) Eingabe des Geburtsjahres
#    - Min: 1900
#    - Max: 2022
while True:
    eingabe = input("Geburtsjahr: ")
    
    if eingabe.isdecimal() and 1900 <= int(eingabe) <= 2022:
        print("Vielen Dank!")
        j = int(eingabe)
        break
    else:
        print("Das ist keine valide Eingabe!")


print(str(t)+"."+str(m)+"."+str(j)) 