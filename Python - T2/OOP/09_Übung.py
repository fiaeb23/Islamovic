
class Book:

    def __init__(self, title: str, authors: list[str], count_loaned: int):
        self.title = title
        self.authors = authors
        self.__count_loaned = count_loaned
        
    def check_new(self) -> bool:
        return self.__count_loaned >= 40
 
class Employee:

    def __init__(self, first_name: str, job_title: str, contract: str):
        self.first_name = first_name
        self.job_title = job_title
        self.__contract = contract
        
    def read_contract(self, job_title: str) -> str:
        if job_title == "Chef":
            return self.__contract
        else:
            return ""
        
b = Book(
    title = "Harry Python",
    authors = ["Klaus", "Lisa"],
    count_loaned = 39
)

print(
    "Neues Buch notwendig?",
    b.check_new()
)

print(b._Book__count_loaned)
print(b.__dict__)
#print(b.__count_loaned)


emp1 = Employee(
    first_name = "Klaus",
    job_title = "IT",
    contract = "........."
)

emp2 = Employee(
    first_name = "Lisa",
    job_title = "Chef",
    contract = "..........."
)

print(
    f"{emp1.first_name} liest den Vertrag von {emp2.first_name}:",
    emp2.read_contract(emp1.job_title)
)

print(
    f"{emp2.first_name} liest den Vertrag von {emp1.first_name}:",
    emp1.read_contract(emp2.job_title)
)

