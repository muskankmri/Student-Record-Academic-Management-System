from utilities import read_number, print_line
def search_by_id(students):                 #search for a student using their ID
    student_id=read_number("Enter student ID: ")
    for student in students:
        if student["id"]==student_id:
            print("Student found:")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Semester:", student["semester"])
            return
    print("Student not found.")
def search_by_name(students):                #search for students by name
    name=input("Enter name: ")
    found=False
    for student in students:
        if name.lower() in student["name"].lower():
            print(
                student["id"],
                student["name"],
                student["branch"],
                student["semester"]
            )
            found=True
    if not found:
        print("Student not found.")
def sort_by_marks(student_marks):        #sort students based on their average marks
    averages=[]
    for student_id in student_marks:
        marks=list(student_marks[student_id].values())
        if len(marks)>0:
            average=sum(marks)/len(marks)
            averages.append((student_id,average))   
    for i in range(len(averages)):         #sort averages using selection sort
        smallest=i
        for j in range(i + 1, len(averages)):
            if averages[j][1]<averages[smallest][1]:
                smallest = j
        averages[i],averages[smallest]=averages[smallest],averages[i]
    print_line()
    print("STUDENTS SORTED BY AVERAGE")
    print_line()
    for student_id, average in averages:
        print(student_id, ":", round(average, 2))
def remove_duplicates():                    #remove duplicate values a set
    values=input("Enter values separated by spaces: ").split()
    unique_values=set(values)
    print("Original values:", values)
    print("After removing duplicates:", list(unique_values))
def kth_smallest():                        #find the kth smallest number using sorting
    values=input("Enter numbers separated by spaces: ").split()
    numbers=[]
    for value in values:
        if value.isdigit():
            numbers.append(int(value))
    if len(numbers)==0:
        print("No valid numbers entered.")
        return
    k=read_number("Enter k: ")
    if k<1 or k>len(numbers):
        print("Invalid k.")
        return
    for i in range(len(numbers)):         #sort numbers using selection sort
        smallest=i
        for j in range(i + 1, len(numbers)):
            if numbers[j]<numbers[smallest]:
                smallest=j
        numbers[i], numbers[smallest]=numbers[smallest], numbers[i]
    print("Sorted numbers:", numbers)
    print(k, "th smallest value:", numbers[k - 1])
def searching_menu(students, student_marks):        #display the search and data operations menu
    while True:
        print_line()
        print("SEARCH AND DATA OPERATIONS")
        print_line()
        print("1. Search Student by ID")
        print("2. Search Student by Name")
        print("3. Sort Students by Average")
        print("4. Remove Duplicates")
        print("5. Find Kth Smallest")
        print("6. Back")
        choice=read_number("Enter your choice: ")
        if choice==1:
            search_by_id(students)
        elif choice==2:
            search_by_name(students)
        elif choice==3:
            sort_by_marks(student_marks)
        elif choice==4:
            remove_duplicates()
        elif choice==5:
            kth_smallest()
        elif choice==6:
            break
        else:
            print("Invalid choice.")