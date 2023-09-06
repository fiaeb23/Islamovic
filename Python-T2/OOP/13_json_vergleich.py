import json

# Load the two JSON files
with open("C:/GITHUB/Islamovic/Python-T2/OOP/13_all_meals.json", "r", encoding="utf-8") as file1:
    meals1 = json.load(file1)

with open("C:/GITHUB/Islamovic/Python-T2/OOP/13_all_meals_florian.json", "r", encoding="utf-8") as file2:
    meals2 = json.load(file2)

# Ensure that both meals1 and meals2 are lists
if not isinstance(meals1, list):
    meals1 = []
if not isinstance(meals2, list):
    meals2 = []

# Find the differences in meals
differences = [meal for meal in meals1 if meal not in meals2] + [meal for meal in meals2 if meal not in meals1]

# Save the differences in a new JSON file
if differences:
    with open("C:/GITHUB/Islamovic/Python-T2/OOP/13_vergleich.json", "w", encoding="utf-8") as difference_file:
        json.dump({"meals": differences}, difference_file, ensure_ascii=False, indent=4)
    print("The different meals have been saved in '13_vergleich.json'.")
else:
    print("No differences in meals found.")
