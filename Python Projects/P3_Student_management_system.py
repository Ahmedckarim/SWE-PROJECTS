# student management system
# Load and save students
# 1. add student 
# 2. view all students
# 3. Search student 
# 4. Update student 
# 5. Delete student 
# 6. Calculate average grade
# 7. Exist 


students = []
def welcome():
    print("=== STUDENT MANEGEMENT SYSTEM ===")
    print("1. Add student ")
    print("2. view all students")
    print("3. Search student ")
    print("4. Update student ")
    print("5. Delete student")
    print("6. Calculate average grades")
    print("7. Exist")


def load_student():
    pass
def save_student():
    pass

def add_student():
    try:
        student_ID = int(input("Enter student ID: "))
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
        
    except ValueError:
        print("Invalid input. Please enter numbers where required.")

def view_students():
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student['ID']}, Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

def search_student():
    pass
def upgrade_student():
    pass
def delete_student():
    pass
def calculate_grade():
    pass

def main():
    welcome()
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            upgrade_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_grade()
        elif choice == "7":
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please try again.")



main()
