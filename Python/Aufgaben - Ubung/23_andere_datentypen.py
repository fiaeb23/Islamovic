
# # Datentypen, welche mehrere Werte enthalten:

# # list
# # tuple
# # set
# # dict

# # Hausaufgabe:
# # Recherchiere zu den Datentypen tuple, set
# # 1) Wie sind sie aufgebaut? -> Syntax
# # 2) Was ist der Unterschied zu list?
# # 3) Wann werden sie verwendet?



# Tuple:

# Tuples sind in Python durch Kommas getrennte Werte, die in runden Klammern eingeschlossen sind.
# Der Unterschied zu einer Liste besteht darin, dass Tupel unveränderlich sind, d. h., ihre Elemente können nach der Erstellung nicht geändert werden.
# Tuples werden verwendet, um eine Sammlung von Elementen zu speichern, wenn die Reihenfolge und die Unveränderlichkeit der Elemente wichtig sind, z. B. beim Speichern von Koordinatenpaaren oder dem Definieren von Schlüssel-Wert-Paaren in einem Wörterbuch.

# Ein Tuple mit den Informationen einer Person: (Name, Alter, Stadt)
person = ("Alice", 30, "Berlin")
print(person)  # Ausgabe: ("Alice", 30, "Berlin")

# Zugriff auf einzelne Elemente im Tuple
name = person[0]
alter = person[1]
stadt = person[2]
print(name)  # Ausgabe: "Alice"
print(alter)  # Ausgabe: 30
print(stadt)  # Ausgabe: "Berlin"





# Set:

# Sets werden in Python durch geschweifte Klammern erstellt und die Elemente sind durch Kommas getrennt.
# Im Gegensatz zu Listen und Tupeln sind Sets ungeordnet und enthalten keine doppelten Elemente.
# Sets werden verwendet, um eine eindeutige Sammlung von Elementen zu speichern und Operationen wie Vereinigung, Schnittmenge und Differenz zwischen Sets auszuführen. Sie sind nützlich, wenn die Reihenfolge und Duplikate keine Rolle spielen und schnelle Such- oder Überprüfungsvorgänge erforderlich sind.

# Ein Set mit verschiedenen Buchstaben
letters = {"a", "b", "c"}
print(letters)  # Ausgabe: {"a", "b", "c"}

# Hinzufügen von Elementen zum Set
letters.add("d")
print(letters)  # Ausgabe: {"a", "b", "c", "d"}

# Entfernen von Elementen aus dem Set
letters.remove("b")
print(letters)  # Ausgabe: {"a", "c", "d"}

# Überprüfen der Elemente im Set
print("a" in letters)  # Ausgabe: True
print("z" in letters)  # Ausgabe: False
