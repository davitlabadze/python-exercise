
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

#=========================================================#
# students = []


# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)


# def get_name(student):
#     return student["name"]    

# for student in sorted(students, key=get_name, reverse=False):
#     print(f"{student['name']} is in {student['house']}")


# With Lambda

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

#=========================================================#

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name": row[0], "home": row[1]})
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

#=========================================================#

# import csv

# students = []

# with open("students1.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

import csv

name = input("What's your name?: ")
home = input("Where's yor home?: ")

# with open("employee.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home])

with open("employee.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

employees = []

with open("employee.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)
    
for employee in sorted(employees, key=lambda employee: employee["name"]):
    print(f"{employee['name']} is in {employee['home']}")
