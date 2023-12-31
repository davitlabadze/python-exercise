students = [
    {"name": "Hermione", "house": "Gryffiondor"},
    {"name": "Harry", "house": "Gryffiondor"},
    {"name": "Ron", "house": "Gryffiondor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffiondors = [
    student["name"] for student in students if student["house"] == "Gryffiondor"
]

for gryffiondor in sorted(gryffiondors):
    print(gryffiondor)