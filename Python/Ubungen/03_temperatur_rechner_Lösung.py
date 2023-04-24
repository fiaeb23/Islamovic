# EINGABE
print("Bitte Ganzzahl eingeben!")
eingabe_celsius = input("Bitte °C eingeben: ")


# VERARBEITUNG
in_fahrenheit = (int(eingabe_celsius) * 9/5) + 32
in_kelvin = int(eingabe_celsius) + 273.15



# AUSGABE
print("In Fahrenheit:", in_fahrenheit, "°F")
print("In Kelvin:", in_kelvin, "K")



