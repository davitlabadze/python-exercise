students = ["Hermione","Harry","Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name":student,"house":"Gryffindor"})


gryffindors = [{"name":student,"house":"Gryffinder"} for student in students]

# one dict
# gryffindors = {student:"Gryffinder" for student in students} 


print(gryffindors)