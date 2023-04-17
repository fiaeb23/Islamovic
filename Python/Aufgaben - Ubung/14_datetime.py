from datetime import datetime

jetzt = datetime.now()

print(jetzt.day)
print(jetzt.month)
print(jetzt.year)
print(jetzt.hour)
print(jetzt.minute)
print(jetzt.second)

print(jetzt.timestamp())

dt = "17.04.2023"
x = datetime.strptime(dt, "%d.%m.%Y") # -> datetime
print(x.strftime("%d.%m.%y")) # -> str

a = datetime.strptime("16.04.2023", "%d.%m.%Y")

print(jetzt - a)
