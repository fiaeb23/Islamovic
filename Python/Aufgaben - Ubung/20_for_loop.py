
parkhaus = ["VW Golf", None, "Opel Astra"]

i = 0
while i < len(parkhaus):
    print(parkhaus[i])
    i = i + 1
            

# 1) iteriere über alle elemente der liste
for elem in parkhaus:
    print(elem)

print()
    
# 2) iteriere über alle indizes der liste
for i in range(len(parkhaus)): # [0, 1, 2]
    print(i)
    print(parkhaus[i])

print()
    
# 3) iteriere über alle indizes UND elemente der liste
for i, elem in enumerate(parkhaus):
    print(i)
    print(elem)

print()


mitarbeiter = [
    ["Alfred", 39, "IT" ],
    ["Bertha", 28, "Sales" ],
]

for name, alter, abteilung in mitarbeiter:
    print("Name:", name)
    print("Alter:", alter)
    print("Abteilung:", abteilung)
    print()