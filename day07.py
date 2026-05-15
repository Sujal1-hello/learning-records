# Student Record System (Basic)

students = []

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
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

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n--- Student Records ---")
            for student in students:
                print(f"Name: {student['Name']}")
                print(f"Roll: {student['Roll']}")
                print(f"Marks: {student['Marks']}")
                print("-----------------------")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")