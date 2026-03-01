# ----------------------------------------
# Mini Project: Student Management System
# ----------------------------------------

students = []   # List to store student dictionaries

# Function to add student
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    
    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Invalid input! Age must be number & marks must be decimal.")
        return

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully ")


# Function to view students
def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.")
        return

    for i, student in enumerate(students):
        print(f"{i+1}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")


# Function to search student
def search_student():
    print("\n--- Search Student ---")
    search_name = input("Enter name to search: ")

    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student Found ")
            print(student)
            found = True
            break

    if not found:
        print("Student not found ")


# Function to delete student
def delete_student():
    print("\n--- Delete Student ---")
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully ")
            return

    print("Student not found ")


# Main Menu Loop
while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program... Goodbye ")
        break
    else:
        print("Invalid choice! Please select 1-5.")
        
        
# x = "awosom"
# def fun():
#     global x 
#     x = "Fantestic"
    
# fun()
# print(type(x)) 

# # Dictionary
# thiisdict = {
#     "brand": "Ford",
#     "modal": "mastang",
#     "year" : 1964,
#     "color": ["red","white","blue"]             
#               }

# print(thiisdict)

