class Employee:
    
    def __init__(self, first_name: str, department: str, email: str):
        self.first_name = first_name
        self.department = department
        self.email = email

class Task:

    def __init__(self, name: str, description: str, duration: int):
        self.name = name
        self.description = description
        self.__duration = duration
        
    def get_duration(self, emp: Employee) -> int:
        if emp.department == "Koordination":
            return self.__duration

        

t1 = Task("Kaffee kochen", "...", 1)

emp1 = Employee("Max", "IT", "max@company.de")
emp2 = Employee("Petra", "Koordination", "petra@company.de")

print(
    f"{emp1.first_name} versucht die Dauer von {t1.name} zu lesen:",
    t1.get_duration(emp1)
)

print(
    f"{emp2.first_name} versucht die Dauer von {t1.name} zu lesen:",
    t1.get_duration(emp2)
)