#Variante 1

celsius = float(input("Trage die Temperatur in Celsius ein: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius ist %0.2f Fahrenheit' %(celsius, fahrenheit))


fahrenheit = float(input("Trage die Temperatur in Fahrenheit ein: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit ist: %0.2f Celsius' %(fahrenheit, celsius))


kelvin = float(input("Trage die Temperatur in Kelvin ein: "))
celsius = (kelvin - 273.15)
print('%.2f Kelvin ist: %0.2f Celsius' %(kelvin, celsius))




#Variante 2

print ("Umrechner für Celsius, Fahrenheit und Kelvin.")
print ("Bitte Eingabe: ")
c = float (input())

f = c * float (9/5) + 32
print (f)

k = float(c + 273.15)
print (k)


#Variante 3 
print (" Hallo Temperator")

fahrenheit = float (input ("Bitte gib die Temperatur in Fahrenheit an : "))

print ("du hast ", fahrenheit ,"°  Fahrenheit eingegeben.")

fahrenheitzahl = (fahrenheit)
celsius = (fahrenheit - 32 )*5/9
kelvin = (celsius + 273.15)


print (fahrenheitzahl, "°Fahrenheit") 
print (celsius,  " °Celsius")
print (kelvin , "Kelvin")

#Variante 4  

temp = input("Welche Temperatur soll umgewandelt werden? (bsp. 45F, 102C): ")
grad = int(temp[:-1])
i_einheit = temp[-1]

if i_einheit.upper() == "C":
    result = int(round((9 * grad) / 5 + 32))
    o_einheit = "Fahrenheit"

elif i_einheit.upper() == "F":
  result = int(round((grad - 32) * 5 / 9))
  o_einheit = "Celsius"

elif i_einheit.upper() == "K":
  result = int(round((grad - 273.15)))

elif i_einheit.upper() == "K":
  result = int(round((grad - 459,67)))
  o_einheit = "Kelvin"

else:
  print("Korrigiere die Eingabe.")
  quit()
print("Die Temperature in", o_einheit, "ist", result, "Grad.")