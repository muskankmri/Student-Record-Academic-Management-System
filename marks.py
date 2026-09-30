from utilities import read_number, find_student, find_course, print_line
def get_grade(marks):                #assign a grade based on marks
    if marks>=90:
        return"S"
    elif marks>=80:
        return"A"
    elif marks>=70:
        return"B"
    elif marks>=60:
        return"C"
    elif marks>=50:
        return"D"
    elif marks>=40:
        return"E"
    else:
        return"F"
def enter_marks(students, courses, enrollment, student_marks):        #enter and store marks for a student
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
    marks=read_number("Enter marks out of 100: ")
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return
    if student_id not in student_marks:
        student_marks[student_id]={}
    student_marks[student_id][course_code]=marks
    print("Marks entered successfully.")
def display_marks(students, courses, student_marks):   #display marks and grades of all students
    print_line()
    print("MARKS LIST")
    print_line()
    for student in students:
        student_id=student["id"]
        if student_id in student_marks:
            print("Student:", student["name"])
            for course_code in student_marks[student_id]:
                marks = student_marks[student_id][course_code]
                print(course_code, ":", marks, "Grade:", get_grade(marks))
def student_performance(students, student_marks):              #calculate and display the performance of a student
    student_id=read_number("Enter student ID: ")
    if find_student(students, student_id) is None:
        print("Student not found.")
        return
    if student_id not in student_marks or len(student_marks[student_id]) == 0:
        print("No marks found.")
        return
    marks_list=list(student_marks[student_id].values())
    total=sum(marks_list)
    average=total/len(marks_list)
    percentage=average
    highest=max(marks_list)
    lowest=min(marks_list)
    print_line()
    print("STUDENT PERFORMANCE")
    print_line()
    print("Total:", total)
    print("Average:", average)
    print("Percentage:", percentage, "%")
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Overall Grade:", get_grade(average))
def marks_menu(students, courses, enrollment, student_marks):        #display the marks management menu
    while True:
        print_line()
        print("MARKS MANAGEMENT")
        print_line()
        print("1. Enter Marks")
        print("2. Display All Marks")
        print("3. View Student Performance")
        print("4. Back")
        choice=read_number("Enter your choice: ")
        if choice==1:
            enter_marks(students, courses, enrollment, student_marks)
        elif choice==2:
            display_marks(students, courses, student_marks)
        elif choice==3:
            student_performance(students, student_marks)
        elif choice==4:
            break
        else:
            print("Invalid choice.")