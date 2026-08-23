# student management system
# Load and save students
# 1. add student 
# 2. view all students
# 3. Search student 
# 4. Update student 
# 5. Delete student 
# 6. Calculate average grade
# 7. Exist 
import json
 
file_name = "students.json"

def welcome():
    print("=== STUDENT MANEGEMENT SYSTEM ===")
    
    print("1. view all students")
    print("2. Add student ")
    print("3. Search student ")
    print("4. Update student ")
    print("5. Delete student")
    print("6. Calculate average grades")
    print("7. Exist")


def load_student():
    try:
        with open(file_name, "r") as file:
            students = json.load(file)
            return students
        
    except FileNotFoundError:
        print("there is no student")
        return []

def save_student(students):

    with open(file_name, "w") as file:
        json.dump(students, file)


def view_students(students):
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student['ID']}, Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

def add_student(students):
    try:
        student_ID = int(input("Enter student ID: "))
        if any(student["ID"] == student_ID for student in students):
            print("this ID already exist.\n")
            return
        
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        grades = []

        for i in range(3):
            grade = float(input(f"Enter grade {i + 1}: "))

            if grade < 0 or grade > 100:
                print("grade must be between 0 and 100.")
                return
            grades.append(grade)
        student = {
            "ID": student_ID,
            "name": name,
            "age": age,
            "grades": grades
        }
        
        
        students.append(student)
        print("Student added successfully!")
        save_student(students)
        
    except ValueError:
        print("Invalid input. Please enter numbers where required.")

def search_student(students):
    try:
        student_ID = int(input("Enter the student ID: "))
        for student in students:
            if student["ID"] == student_ID:
                print(f"ID: {student['ID']}, Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
                        
    except ValueError:
        print("Enter a valid ID")

def upgrade_student(students):
    try:
        student_ID = int(input("Enter the student ID: "))
        for student in students:
            if student["ID"] == student_ID:
                print("Enter the Updated student data.")

                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
        
                grades = []
        
                for i in range(3):
                    grade = float(input(f"Enter grade {i + 1}: "))
        
                    if grade < 0 or grade > 100:
                        print("grade must be between 0 and 100.")
                        return
                    grades.append(grade)
                update_student = {
                    "ID": student_ID,
                    "name": name,
                    "age": age,
                    "grades": grades
                }
                student["name"] = name
                student["age"] = age
                student["grades"] = grades

                save_student(students)
                print("Student Updated successfully.")
                return
        print("Student Id not found.")
    except ValueError:
        print("Invalid input. Please enter numbers where required.")

    
def delete_student():
    pass
def calculate_grade():
    pass

def main():
    students = load_student()
    view_students(students)
    welcome()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
             view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            upgrade_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            calculate_grade(students)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")



main()
