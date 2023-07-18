"""
Aufgabe 1:
Definiere eine Generator Function, welche...
...beim ersten Iterieren den int-Wert 1 zurückgibt
...beim zweiten Iterieren den int-Wert 2 zurückgibt
...beim dritten Iterieren den int-Wert 3 zurückgibt
"""
def fun_1():
    yield 1
    yield 2
    yield 3

x = fun_1()

print(next(x)) # Erwartete Ausgabe: 1
print(next(x)) # Erwartete Ausgabe: 2
print(next(x)) # Erwartete Ausgabe: 3
#print(next(x)) # StopIteration



"""
Aufgabe 2:
Setze eine Lotterie mit einer Generator Function um.

Dabei gilt:
- Die Lotterie gibt zunächst sechs Zahlen zwischen 1 und 50 zurück
- Anschließend gibt sie eine magische Zahl zwischen 1 und 10 zurück
"""
import random

def lottery():
    for i in random.sample(range(1, 51), 6):
        yield i
    
    yield random.randint(1, 10)

[print(i, end=" ") for i in lottery()]
"""Erwartete Ausgabe (z.b.)
7 37 48 17 36 31 4
"""
print()


"""
BONUS:
Definiere einen Generator zum ermitteln der Zahlen
der Fibonacci Folge (-> https://de.wikipedia.org/wiki/Fibonacci-Folge)
bis zum gegebenen limit (exkl. ende)

# Tipp: Erstelle in der Funktion Variablen mit den ersten beiden Fibonacci Zahlen
"""

def fibo(limit):
    a = 0
    b = 1
    
    while a < limit:
        yield a
        temp = a
        a = b
        b = b + temp
        # alternativ:
        #a, b = b, a+b

[print(i, end=" ") for i in fibo(5)]
"""Erwartete Ausgabe
0 1 1 2 3 
"""
print()

[print(i, end=" ") for i in fibo(10)]
"""Erwartete Ausgabe
0 1 1 2 3 5 8 
"""