""" POLYMORPHIE IN OOP
1) Definition:
- Elternklasse hat Methoden, 
  welche pro Kindklasse eine andere Funktionalität haben
2) 
"""
class Car:
    
    def drive(self):
        print("Wroom!")
        
class SportCar(Car):
    
    def drive(self):
        super().drive() # Car().drive()
        print("WroomWroom!")
        
class Van(Car):

    def drive(self):
        print("Wroooom!")
        
my_sport_car = SportCar()
my_sport_car.drive()

my_van = Van()
my_van.drive()


""" ABSTRAKTE KLASSEN
1) Definition:
- Klasse, die als Oberbegriff für andere Klassen
  gilt

2) In Python:
- abc Modul verwenden
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def eat(self):
        pass
        
class Dog(Animal):

    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
    def eat(self, food):
        print(self.name, "isst", food)
    
class Bird(Animal):
    
    def __init__(self, name, feather_color):
        self.name = name
        self.feather_color = feather_color
        
    def eat(self, food):
        print(self.name, "isst", food)

my_dog = Dog("John", "brown")
my_dog.eat("Steak")


""" FUNKTIONS- & OPERATORÜBERLADUNG
1) Definition:
- Klassen "beibringen" mit Python-Funktionen 
  und -Operatoren zurechtzukommen

2) In Python:

"""

class Computer:

    def __init__(self, cpu: str, ram: int):
        self.cpu = cpu
        self.ram = ram
        
    def __repr__(self) -> str:
        return f"Computer(cpu='{self.cpu}', ram={self.ram}GB)"
        
    def __add__(self, other: int):
        new_ram = self.ram + other
        return Computer(self.cpu, new_ram)
        
    def __iadd__(self, other: int):
        self.ram += other
        return self
        
    def __sub__(self, other: int):
        new_ram = self.ram - other
        return Computer(self.cpu, new_ram)

    def __getitem__(self, key: str):
        return f"{key} = {self.__dict__[key]}"
        
    
my_pc = Computer(cpu="i7", ram=8) + 8
print(my_pc)
#new_pc = my_pc + 8
print(my_pc.ram) # 16
my_pc = my_pc - 8
print(my_pc.ram) # 8

my_pc += 8
print(my_pc.ram)

print(my_pc["cpu"])













