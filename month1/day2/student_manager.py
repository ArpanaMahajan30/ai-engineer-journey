students = []

def add_student(name: str,age: int,skills: list[str]) -> None:

    """Function to add a new student to the students list"""
    
    student = {
        "name" : name,
        "age" : age,
        "skills" : skills
    }
    students.append(student)

def view_students() -> None:

    """Function to view all students in the students list"""

    if not students:
        print("No students found.")
        return

    for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Skills: {', '.join(student['skills'])}")

def search_student(name: str) -> None:

    """Function to search for a student by name"""

    for student in students:
        if student["name"].lower() == name.lower():
            print (f"Found student: Name: {student['name']}, Age: {student['age']}, Skills: {', '.join(student['skills'])}")
            return
    print(f"Student with name {name} not found.")

def main():
   while True:
        print("\nStudent Manager Menu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        menu_choice = input("Enter your choice (1-4): ")

        if menu_choice == '1':
            try:
                name = input("Enter student name: ")
                if not name.strip():
                    print("Name cannot be empty.")
                    continue
                age = int(input("Enter student age: "))
                if age <= 0:
                    print("Age must be a positive integer.")
                    continue
                skills = input("Enter student skills (comma-separated): ").split(",")
                skills = [skill.strip() for skill in skills]  # Remove any extra spaces
                add_student(name, age, skills)
                print(f"Added student: {name}")
            except ValueError:
                print("Invalid input. Please enter a valid age.")
        elif menu_choice == '2':
            view_students()
        elif menu_choice == '3':
            name = input("Enter the name of the student to search: ")
            search_student(name)
        elif menu_choice == '4':
            print("Exiting Student Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()