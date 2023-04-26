#print (" Hallo Temperator")

#fahrenheit = float (input ("Bitte gib die Temperatur in Fahrenheit an : "))

#print ("du hast ", fahrenheit ,"°  Fahrenheit eingegeben.")

#fahrenheitzahl = (fahrenheit)
#celsius = (fahrenheit - 32 )*5/9
#kelvin = (celsius + 273.15)


#print (fahrenheitzahl, "°Fahrenheit") 
#print (celsius,  " °Celsius")
#print (kelvin , "°kelvin")

#import random
#num = random.randrange(1, 100)
#print (num)


# zahl eingrenzen
#n = variable zb. user_nr
#if n < 1 or n > 10:
#else 
#    ...... 

import random

# Geheime Zahl zwischen 1 und 10 generieren
secret_number = random.randint(1, 10)



guess = int(input("Rate eine Zahl zwischen 1 und 10: "))


if guess == secret_number:
    print("Glückwunsch, du hast gut geraten")
else:
    if guess < 1 or guess > 10:
        print ("die Gesuchte Zahl zwischen  1, 10 !")
    else:
        guess = int(input("Versuch es noch einmal: "))
            
        if guess == secret_number:
           print("Glückwunsch, du hast zweite Versuch gut geraten!")
        else:
       
            if guess < secret_number:
                print("Die gesuchte Zahl ist höher als deine Vermutung.")
            else:
                print("Die gesuchte Zahl ist nicht  deine Vermutung.")
                print("Leider hast du die Zahl nicht erraten. Die geheime Zahl war", secret_number)

