x = int(input("Zahl: "))

if x > 10:
    print("Diese Zahl ist größer als 10!")
# implizit: x <= 10 -> True
elif x > 5:
    print("Diese Zahl liegt zwischen 6 und 10!")
# implizit: x <= 5 -> True
else:
    print("Diese Zahl ist höchstens 5!")