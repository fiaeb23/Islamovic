"""
1) Lies die person_data.csv ein
   (mit csv.reader oder csv.DictReader)
# """
# import csv

# with open(r"C:\GITHUB\Islamovic\Python - T2\OOP\person_data.csv", encoding="utf-8") as file:
#     csv_file = csv.reader(file)
    
#     for line in list(csv_file)[1:]:
#         print(
#             f"id: {line[0]}",
#             f"first_name: {line[1]}",
#             f"last_name: {line[2]}", 
#             f"location: {line[3]}",
#             f"fav_color: {line[4]}", 
#             f"department: {line[5]}"  
#         )

"""
2) In welchem Land befinden sich die meisten Personen (laut person_data.csv)?
"""

"""
3) Schreibe alle Personen aus Portugal (location=Portugal) in eine eigene
   csv-Datei.
"""

"""
BONUS) Erstelle pro Wert der Spalte department eine eigene csv Datei,
       die alle Mitarbeiter des jeweiligen departments enthält.
"""
import csv

#1.lesen und ausgeben
with open(r"C:\GITHUB\Islamovic\Python - T2\OOP\person_data.csv", encoding="utf-8") as file:
    csv_file = csv.reader(file)
    
    for line in list(csv_file)[1:]:
        print(
            f"id: {line[0]}",
            f"first_name: {line[1]}",
            f"last_name: {line[2]}", 
            f"location: {line[3]}",
            f"fav_color: {line[4]}", 
            f"department: {line[5]}"  
        )

#2.Anzahl der Personen pro Department zählen
department_count = {}

with open(r"C:\GITHUB\Islamovic\Python - T2\OOP\person_data.csv", encoding="utf-8") as file:
    csv_file = csv.reader(file)

    #next(csv_file)  #Überspringen der Header-Zeile
    
    for line in csv_file:
        department = line[5]  #Department = Index 5

        if department in department_count:
            department_count[department] += 1
        else:
            department_count[department] = 1

most_common_department = max(department_count, key=department_count.get)
total_people_in_most_common_department = department_count[most_common_department]

print(f"Das Department mit den meisten Personen ist {most_common_department} mit {total_people_in_most_common_department} Personen.")

#3.Alle Personen aus Portugal

# Pfad ursprüngliche Datei
input_file_path = r"C:GITHUB\Islamovic\Python - T2\OOP\person_data.csv"

# Pfad zur Zieldatei
output_file_path = r"C:GITHUB\Islamovic\Python - T2\OOP\person_portugal.csv"

#auslesen
with open(input_file_path, encoding="utf-8") as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)
    
    # Filtern 
    portugal_people = [row for row in csv_reader if row[3] == "Portugal"]
    sorted_portugal_people = sorted(portugal_people, key=lambda x: int(x[0]))  # Nach der ID sortieren

#Einfügen in Zieldatei
with open(output_file_path, mode="w", encoding="utf-8", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    
    #Header-Zeile Zieldatei erstellen
    csv_writer.writerow(header)
    
    # Schreiben Sie die sortierten Personen aus Portugal in die Datei
    csv_writer.writerows(sorted_portugal_people)

print("Personen aus Portugal wurden in die Datei 'person_portugal.csv' geschrieben und sortiert.")
