from sample_data import students, courses, enrollment, student_marks, attendance
from utilities import read_number, print_line
from student import student_menu
from courses import course_menu
from marks import marks_menu
from attendance import attendance_menu
from analysis import analysis_menu
from searching import searching_menu
def main():
    while True:
        print_line()
        print("STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM")
        print_line()
        print("1. Student Management")
        print("2. Course Management")
        print("3. Marks Management")
        print("4. Attendance Management")
        print("5. Performance Analysis")
        print("6. Search and Data Operations")
        print("7. Exit")
        choice=read_number("Enter your choice: ")
        if choice==1:
            student_menu(students, enrollment, student_marks, attendance)
        elif choice==2:
            course_menu(students, courses, enrollment)
        elif choice==3:
            marks_menu(students, courses, enrollment, student_marks)
        elif choice==4:
            attendance_menu(students, courses, enrollment, attendance)
        elif choice==5:
            analysis_menu(students, student_marks)
        elif choice==6:
            searching_menu(students, student_marks)
        elif choice==7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")
if __name__=="__main__":
    main()