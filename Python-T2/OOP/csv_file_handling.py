import csv

# 1) csv Datei einlesen
"""
with open(r"Desktop\persons.csv", encoding="utf-8") as file:
    csv_file = csv.reader(file)
    
    for line in list(csv_file)[1:]:
        print(
            f"Vorname: {line[0]}",
            f"Nachname: {line[1]}",
            f"Email: {line[2]}"
        )
"""

# 2) csv Datei einlesen mit DictReader
"""
with open(r"Desktop\persons.csv", encoding="utf-8") as file:
    csv_file = csv.DictReader(
        file, 
        fieldnames=("vorname", "nachname", "email"),
        delimiter=",",
        quotechar='"',
        skipinitialspace=True
    )
    
    for line in csv_file:
        print(line)
        break
"""

# 3) csv Datei schreiben mit writer
"""
with open(r"Desktop\new_data.csv", "w", newline="") as file:
    csv_file = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    
    # header schreiben
    csv_file.writerow(["product_name", "price", "quantity"])
    
    # daten schreiben
    csv_file.writerow(["Tastatur", 30, 10])
    csv_file.writerow(["Monitor", 100, 4])
"""
    
# 4) csv Datei schreiben mit DictWriter
with open(r"Desktop\new_data.csv", "w", newline="") as file:
    csv_file = csv.DictWriter(file, fieldnames=("product_name", "price", "quantity"))
    
    # header schreiben
    csv_file.writeheader()
    
    # daten schreiben
    csv_file.writerow({"product_name": "Tastatur", "price": 30, "quantity": 10})
    csv_file.writerow({"product_name": "Monitor", "price": 100, "quantity": 4})
    