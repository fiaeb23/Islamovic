"""
1) Definiere einen Decorator, der eine dekorierte Funktion 2x ausführt
"""

def double(func):
    
    def wrapper():
        func()
        func()

    return wrapper

@double
def say_hello():
    print("Hello")

say_hello()
# Erwartete Ausgabe:
# Hello
# Hello

"""
2) Definiere einen Decorator, der prüft, ob ein Nutzer angemeldet ist
   - Sollte der Nutzer angemeldet sein, führe Funktion aus
   - Ansonsten gebe eine Fehlermeldung (Exception) aus
"""

def login_required(func):

    def wrapper():
        if USER is not None:
            func()
        else:
            raise Exception("User is not logged in!")

    return wrapper

@login_required
def share_post():
    print("Succesfully shared post")

USER = "Bobo"
share_post() # Erw. Ausgabe: "Succesfully shared post"

USER = None
#share_post() # Erw. Ausgabe: Exception(...)

"""
BONUS) Definiere einen Decorator, der die Werte aller Parameter der dekorierten Funktion zurückgibt

- Dabei sollte es keine Rolle spielen, ob die Funktion mit keyword arguments aufgerufen wird oder nicht 
- Ein print pro Parameter
"""

def debug(func):

    def wrapper(*args, **kwargs):
        
        for elem in args:
            print(elem)
        
        for elem in kwargs.values():
            print(elem)
            
        return func(*args, **kwargs)

    return wrapper

@debug
def add(x, y):
    return x + y

print(add(1, 2))
# Erw. Ausgabe:
# 1
# 2
# 3

print(add(x=10, y=4))
# Erw. Ausgabe:
# 10
# 4
# 14

print(add(3, y=8))
# Erw. Ausgabe:
# 3
# 8
# 11


"""
ULTRABONUS) Definiere einen Decorator, der die dekorierte Funktion nur zurückgibt, 
            wenn der Rückgabetyp der Funktion dem Type Hint entspricht

- Schaue dir func.__annotations__ innerhalb der wrapper()-Funktion an 
- Tipp: Nutze die isinstance()- oder die type()-Funktion
"""

def check_type(func):

    def wrapper(*args, **kwargs):
        rtype = func.__annotations__["return"]
        result = func(*args, **kwargs)
        
        if rtype == type(result):
            return result
        

    return wrapper

@check_type
def get_str(x) -> str:
    return x

print(get_str("bla")) # Erw. Ausgabe: "bla"
print(get_str(123))   # Erw. Ausgabe: None


