import csv 

with open("students.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Skill"])
    writer.writerow(["Arpana", 26, "Python"])
    writer.writerow(["John", 30, "Java"])

# Read the CSV file and print the content 

with open("students.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Name"] == "Arpana":
            print(f"Name: {row['Name']}\nAge: {row['Age']}\nSkill: {row['Skill']}")
            break
        else:
            print("Student not found.")