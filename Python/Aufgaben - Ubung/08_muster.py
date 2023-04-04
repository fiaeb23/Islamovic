# """
# Erzeuge folgendes Muster mithilfe einer while-Schleife:

# *
# **
# ***
# ****

# Die Anzahl der "*" in der letzten Reihe hängt von der 
# Variable `anzahl` ab.
# """
# anzahl = 4

# while ???:
#     ...
# """
# Erzeuge folgendes Muster mithilfe einer while-Schleife:
# 1
# 12
# 123
# 1234

# Die letzte Zahl in der letzten Zeile hängt von der Variable
# `anzahl` ab.
# """
# anzahl = 4

#Aufgabe 1 

# anzahl = 5
# counter = 1 
# while counter <= anzahl: 
#     print ("*" *counter )     # Wenn es mit einem numerischen Wert multipliziert wird. Zum Beispiel ergibt 3 * 4 den Wert 12.
#                               # In diesem Fall ist "counter" eine Variable, die einen numerischen Wert speichert. Wenn also "*" mit "counter" multipliziert wird, wird ein String generiert, der aus einer Anzahl von Sternchen besteht, die der Wert von "counter" ist.
#     counter += 1





#Aufgabe 2
anzahl = 10

a = 1                           # a = beginn der anzahl der schleife mit vorherigen zahlen
while a <= anzahl:              # abfrage 
    b = 1                       # festlegung von x
    while b <= a:               # abfrage x soll gelich i sein (8)
        print(b, end=' ')       # ausgabe jede zahl in der gleichen zeile
        b += 1                  # größe der Schritte
    print()
    a += 1                      # anzahl der beigefügten Zahlen





#Muster Lösung

# anzahl = 4
# counter = 1
# text = ""
# while counter <= anzahl:
#     text = text  +str(counter)
#     print(text)
#     counter = counter +1




#ALTERNATIVE VARIABLEN 

# anzahl = 5

# for anzahl in range(1, anzahl + 1):

#     for x in range(1, anzahl + 1):

#         print(x, end=' ')

#     print() 


###########

# rows = int(input("Enter Pyramid Pattern Rows = "))

# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(' ', end = '')
#     for k in range(1, (2 * i)):
#         print('*', end = '')
#     print()



