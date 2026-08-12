## Practice Lists and Dictionaries  

# skills = ["Python", "Git", "SQL", "Pandas"]
# skills.append("Machine Learning")
# skills.remove("Git")
#  print(skills)

# for i in skills:
#     print(i) 


# student = {
#     "name" : "Arpana",
#     "Age" : 26,
#     "Skill" : "Python"
# }

# # print(student["name"])
# student["city"] = "Sujanpur"
# student["Skill"] = "Python & SQL"
# print(student.items())


# print 1st student using loop
# students = [
#     {
#         "name" : "Arpana",
#         "skills" : ["Python","SQL"]
#     },

#     {
#         "name" : "John",
#         "skills" : ["Java","Spring"]
#     }
# ]

# # for student in students:
# #     if student["name"] == "Arpana":
# #         print(student["name"])
# #         for skill in student["skills"]:
# #             print(skill)

# print(students[1]["skills"][1])


student = {
    "name" : "Arpana",
    "Age" : 26
    }

import json
json_data = json.dumps(student)
print(json_data)