from utilities import read_number, print_line
from marks import get_grade
def get_student_average(student_id, student_marks):   #calculate the average marks of a student
    if student_id not in student_marks:               # Check whether the student has marks
        return -1
    marks=list(student_marks[student_id].values())   #get all marks of the student
    if len(marks)==0:                                #Return -1 if no marks are available
        return -1
    return sum(marks)/len(marks)                     #calculate and return the student's average

    print_line()
    print("GRADE DISTRIBUTION")
    print_line()
    for grade in grades:
        print(grade,":",grades[grade])        
def class_report(students, student_marks):     #Generate a complete class performance report   
    print_line()
    print("CLASS PERFORMANCE REPORT")
    print_line()
    class_average(students, student_marks)
    print()
    find_topper(students, student_marks)
    print()
    find_lowest(students, student_marks)
    print()
    grade_distribution(students, student_marks)
def analysis_menu(students, student_marks):       #Display the performance analysis menu
    while True:
        print_line()
        print("PERFORMANCE ANALYSIS")
        print_line()
        print("1. Class Average")
        print("2. Find Topper")
        print("3. Find Lowest Performer")
        print("4. Grade Distribution")
        print("5. Complete Class Report")
        print("6. Back")
        choice=read_number("Enter your choice: ")  #Perform the selected analysis
        if choice==1:
            class_average(students, student_marks)
        elif choice==2:
            find_topper(students, student_marks)
        elif choice==3:
            find_lowest(students, student_marks)
        elif choice==4:
            grade_distribution(students, student_marks)
        elif choice==5:
            class_report(students, student_marks)
        elif choice==6:
            break
        else:
            print("Invalid choice.")
def class_average(students, student_marks):   #Calculate the average marks of the whole class 
    averages=[]
    for student in students:                   #Check each student
        average=get_student_average(student["id"], student_marks)      #calculate the student's average 
        if average>0:                          # Add the average if marks are available
            averages.append(average)
    if len(averages)==0:                        # Display message if no marks are available
        print("No marks available.")
        return
    average=sum(averages)/len(averages)             # Calculate the class average 
    print("Class Average:", round(average, 2))
def find_topper(students, student_marks):            # Find the student with the highest average
    topper=None
    highest_average=-1
    for student in students:                          # Check every student
        average=get_student_average(student["id"], student_marks)  # Update topper if a higher average is found
        if average>highest_average and average>0:
            highest_average=average
            topper=student
    if topper is None:                                  # Display the topper or show that marks are unavailable
        print("No marks available.")
    else:
        print("Topper:", topper["name"])
        print("Average:", round(highest_average, 2))
def find_lowest(students, student_marks):              # Find the student with the lowest valid average
    lowest_student=None
    lowest_average=101
    for student in students:                                #Check every student                             
        average=get_student_average(student["id"], student_marks)      # Calculate the student's average
        if average>0 and average<lowest_average:
            lowest_average=average
            lowest_student=student
    if lowest_student is None:                         # Display the lowest performer
        print("No marks available.")
    else:
        print("Lowest Performer:", lowest_student["name"])
        print("Average:", round(lowest_average, 2))
def grade_distribution(students, student_marks):           # Display the number of students in each grade
    grades={
        "S": 0,
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0
    }
    for student in students:
        average=get_student_average(student["id"], student_marks)
        if average>0:
            grade=get_grade(average)
            grades[grade]+=1