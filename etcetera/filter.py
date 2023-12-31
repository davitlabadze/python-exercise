students = [
    {"name": "Hermione", "house": "Gryffiondor"},
    {"name": "Harry", "house": "Gryffiondor"},
    {"name": "Ron", "house": "Gryffiondor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# def is_gryffiondor(s):
#     if s["house"] == "Gryffiondor":
#         return True
#     else:
#         return False

def is_gryffiondor(s):
    return s["house"] == "Gryffiondor"

# gryffindors = filter(lambda s: s["house"] == "Gryffiondor",students)
gryffindors = filter(is_gryffiondor,students)

for gryffindor in sorted(gryffindors, key=lambda s:s["name"]):
    print(gryffindor["name"])