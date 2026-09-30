from utilities import read_number,find_student,find_course,print_line
def enter_attendance(students, courses, enrollment, attendance):     #Enter and store attendance for a student
    student_id=read_number("Enter student ID: ")
    if find_student(students, student_id) is None:
        print("Student not found.")
        return
    course_code=input("Enter course code: ").strip().upper()
    if find_course(courses, course_code) is None:
        print("Course not found.")
        return
    if student_id not in enrollment or course_code not in enrollment[student_id]:
        print("Student is not enrolled in this course.")
        return        
    attended = read_number("Enter classes attended: ")
    total = read_number("Enter total classes: ")
    if total<=0:
        print("Total classes must be greater than 0.")
        return
    if attended>total:
        print("Classes attended cannot be greater than total classes.")
        return
    if student_id not in attendance:
        attendance[student_id] = {}
    attendance[student_id][course_code] = (attended, total)
    print("Attendance entered successfully.")
def calculate_percentage(attended, total):  #calculate attendance percentage
    return (attended / total) * 100
def display_attendance(students, attendance):  #display attendance records of students
    print_line()
    print("ATTENDANCE LIST")
    print_line()
    for student in students:
        student_id=student["id"]
        if student_id in attendance:
            print("Student:", student["name"])
            for course_code in attendance[student_id]:
                attended, total = attendance[student_id][course_code]
                percentage = calculate_percentage(attended, total)
                print(
                    course_code,
                    ":",
                    attended,
                    "/",
                    total,
                    "=",
                    round(percentage, 2),
                    "%"
                )
def low_attendance(students, attendance):    #find students whose attendance is below the given threshold
    threshold=read_number("Enter attendance threshold: ")
    print_line()
    print("LOW ATTENDANCE STUDENTS")
    print_line()
    found=False
    for student in students:
        student_id=student["id"]
        if student_id in attendance:
            for course_code in attendance[student_id]:
                attended, total=attendance[student_id][course_code]
                percentage=calculate_percentage(attended, total)
                if percentage<threshold:
                    print(
                        student["name"],
                        "-",
                        course_code,
                        "-",
                        round(percentage, 2),
                        "%"
                    )
                    found=True
    if not found:
        print("No students are below the threshold.")
def attendance_menu(students, courses, enrollment, attendance):
    while True:
        print_line()
        print("ATTENDANCE MANAGEMENT")
        print_line()
        print("1. Enter Attendance")
        print("2. Display Attendance")
        print("3. Find Low Attendance")
        print("4. Back")
        choice=read_number("Enter your choice:")
        if choice==1:
            enter_attendance(students,courses,enrollment,attendance)
        elif choice==2:
            display_attendance(students,attendance)
        elif choice==3:
            low_attendance(students,attendance)
        elif choice==4:
            break
        else:
            print("Invalid choice.")