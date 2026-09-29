from utilities import read_number, read_non_empty, find_student, find_course, print_line
def add_course(courses):
    course_code = read_non_empty("Enter course code: ")

    if find_course(courses, course_code) is not None:
        print("Course already exists.")
        return

    course_name = read_non_empty("Enter course name: ")
    credits = read_number("Enter credits: ")

    courses.append((course_code, course_name, credits))

    print("Course added successfully.")
def display_courses(courses):
    print_line()
    print("COURSE LIST")
    print_line()

    if len(courses) == 0:
        print("No courses found.")
        return

    for course in courses:
        print(
            "Code:", course[0],
            "| Name:", course[1],
            "| Credits:", course[2]
        )
def assign_course(students, courses, enrollment):
    student_id = read_number("Enter student ID: ")

    if find_student(students, student_id) is None:
        print("Student not found.")
        return

    course_code = read_non_empty("Enter course code: ")

    if find_course(courses, course_code) is None:
        print("Course not found.")
        return

    if student_id not in enrollment:
        enrollment[student_id] = []
    if course_code in enrollment[student_id]:
        print("Student is already enrolled in this course.")
        return
    enrollment[student_id].append(course_code)
    print("Course assigned successfully.")
def show_student_courses(students, courses, enrollment):
    student_id = read_number("Enter student ID: ")
    if find_student(students, student_id) is None:
        print("Student not found.")
        return
    if student_id not in enrollment or len(enrollment[student_id]) == 0:
        print("No courses assigned.")
        return
    print_line()
    print("STUDENT COURSES")
    print_line()
    total_credits = 0
    for course_code in enrollment[student_id]:
        course = find_course(courses, course_code)

        if course is not None:
            print(
                "Code:", course[0],
                "| Name:", course[1],
                "| Credits:", course[2]
            )
            total_credits += course[2]
    print("Total Credits:", total_credits)
def course_menu(students, courses, enrollment):
    while True:
        print_line()
        print("COURSE MANAGEMENT")
        print_line()
        print("1. Add Course")
        print("2. Display Courses")
        print("3. Assign Course to Student")
        print("4. View Student Courses")
        print("5. Back")
        choice = read_number("Enter your choice: ")
        if choice == 1:
            add_course(courses)
        elif choice == 2:
            display_courses(courses)
        elif choice == 3:
            assign_course(students, courses, enrollment)
        elif choice == 4:
            show_student_courses(students, courses, enrollment)
        elif choice == 5:
            break
        else:
            print("Invalid choice.")