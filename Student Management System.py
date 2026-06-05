students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "Roll No": roll,
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("No Student Records Found!")
        return

    print("\n----- STUDENT RECORDS -----")
    for student in students:
        print(f"Roll No : {student['Roll No']}")
        print(f"Name    : {student['Name']}")
        print(f"Course  : {student['Course']}")
        print(f"Marks   : {student['Marks']}")
        print("-" * 25)

def search_student():
    roll = input("Enter Roll No to Search: ")

    for student in students:
        if student["Roll No"] == roll:
            print("\nStudent Found!")
            print(student)
            return

    print("Student Not Found!")

def update_student():
    roll = input("Enter Roll No to Update: ")

    for student in students:
        if student["Roll No"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Course"] = input("Enter New Course: ")
            student["Marks"] = float(input("Enter New Marks: "))

            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for student in students:
        if student["Roll No"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
