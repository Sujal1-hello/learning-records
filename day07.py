# Student Record System with Functions

students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\n===== Student Records =====")

        for student in students:
            print(f"Name : {student['Name']}")
            print(f"Roll : {student['Roll']}")
            print(f"Marks: {student['Marks']}")
            print("-------------------------")


while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")