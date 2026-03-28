# Student Database Program

students = []          
usn_set = set()        

# UPDATED: No fixed limit → user decides how many students
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for Student", i+1)

    usn = input("Enter USN: ")

    # UPDATED: Proper duplicate checking (loop)
    while usn in usn_set:
        print("USN already exists! Enter a different USN.")
        usn = input("Enter USN again: ")

    usn_set.add(usn)

    name = input("Enter Name: ")

    m1 = int(input("Enter Marks 1: "))
    m2 = int(input("Enter Marks 2: "))
    m3 = int(input("Enter Marks 3: "))

    marks = (m1, m2, m3)   # Tuple for storing marks

    # Dictionary to store student data
    student = {
        "usn": usn,
        "name": name,
        "marks": marks
    }

    students.append(student)


print("\n----- Student Grades -----")

for s in students:

    usn = s["usn"]
    m1, m2, m3 = s["marks"]

    avg = (m1 + m2 + m3) / 3

    # Grade assignment using if-elif-else ladder
    if avg > 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    else:
        grade = "Satisfactory"

    # UPDATED: Better output formatting
    print("Name:", s["name"])
    print("USN:", usn)
    print("Average:", avg)
    print("Grade:", grade)
    print("---------------------")
