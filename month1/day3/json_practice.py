import json

student = {
    "name" : "Arpana",
    "age" : 26,
    "skills" : ["Python", "SQL"]
}

with open ("student.json", "w") as file:
    json.dump(student, file)

# Print name of student from student.json file
with open ("student.json", "r") as file:
    data = json.load(file)
    print("Name of student from student.json file:", data["name"])
        