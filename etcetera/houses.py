students = [
    {"name": "Hermione", "house": "Gryffiondor"},
    {"name": "Harry", "house": "Gryffiondor"},
    {"name": "Ron", "house": "Gryffiondor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


# good 
# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# best
houses = set()
for student in students:
    houses.add(student["house"])


for house in sorted(houses):
    print(house)