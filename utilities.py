def print_line():    #print a seperator line
    print("----------------------------------------")
def read_number(message):   #read and validate a numeric input
    value=input(message)
    while not value.isdigit():
        print("Please enter a valid number.")
        value=input(message).strip()
    return int(value)
def read_non_empty(message):    #read and validate non-empty input
    value=input(message).strip()
    while value=="":
        print("Input cannot be empty.")
        value=input(message).strip()
    return value
def find_student(students, student_id):     #find a student using their ID
    for student in students:
        if student["id"]==student_id:
            return student
    return None
def find_course(courses, course_code):     #find a course using its course code  
    for course in courses:
        if course[0]==course_code:
            return course
    return None