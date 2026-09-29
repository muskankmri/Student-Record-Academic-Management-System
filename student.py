from utilities import read_number, read_non_empty, find_student, print_line
def add_student(students):
    student_id = read_number("Enter student ID: ")

    if find_student(students, student_id) is not None:
        print("Student ID already exists.")
        return

    name = read_non_empty("Enter student name: ")
    branch = read_non_empty("Enter branch: ")
    semester = read_number("Enter semester: ")

    student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "semester": semester
    }

    students.append(student)
    print("Student added successfully.")


def display_students(students):
    print_line()
    print("STUDENT LIST")
    print_line()

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(
            "ID:", student["id"],
            "| Name:", student["name"],
            "| Branch:", student["branch"],
            "| Semester:", student["semester"]
        )


def search_student(students):
    student_id = read_number("Enter student ID: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
    else:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Semester:", student["semester"])


def search_by_name(students):
    name = read_non_empty("Enter student name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Semester:", student["semester"])
            found = True

    if not found:
        print("Student not found.")


def update_student(students):
    student_id = read_number("Enter student ID to update: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    student["name"] = read_non_empty("Enter new name: ")
    student["branch"] = read_non_empty("Enter new branch: ")
    student["semester"] = read_number("Enter new semester: ")

    print("Student updated successfully.")


def delete_student(students):
    student_id = read_number("Enter student ID to delete: ")
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    print("Student deleted successfully.")


def student_menu(students):
    while True:
        print_line()
        print("STUDENT MANAGEMENT")
        print_line()
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Back")

        choice = read_number("Enter your choice: ")

        if choice == 1:
            add_student(students)
        elif choice == 2:
            display_students(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            search_by_name(students)
        elif choice == 5:
            update_student(students)
        elif choice == 6:
            delete_student(students)
        elif choice == 7:
            break
        else:
            print("Invalid choice.")