# Functional requirements
# Display a menu with available operations:
# Addition✔️
# Subtraction✔️
# Multiplication✔️
# Division✔️
# Exit✔️
#  Ask the user to choose an operation.✔️
#  Ask for two numbers.✔️
#  Perform the selected operation.✔️
#  Display the result.✔️
#  Return to the menu after each calculation.✔️
#  Allow the user to exit the program.✔️
Result = 0
def Menu():
    print("Calculator program")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

def addition():
    print(" Enter numbers you want to add them.")
    try:
        Number1 = int(input("Number one: "))
        Number2 = int(input("Number Two: "))

        Result =  Number1 + Number2
        print(f"Result: {Result}")
    except ValueError:
        print("Please Inter valid numbers")


def subtraction():
    print(" Enter numbers you want to subtract them.")
    try:
        Number1 = int(input("Number one: "))
        Number2 = int(input("Number Two: "))

        Result =  Number1 - Number2
        print(f"Result: {Result}")
    except ValueError:
        print("Please Inter valid numbers")

def Multiplication():
    print(" Enter numbers you want to multiply them.")
    try:
        Number1 = int(input("Number one: "))
        Number2 = int(input("Number Two: "))

        Result =  Number1 * Number2
        print(f"Result: {Result}")
    except ValueError:
        print("Please Inter valid numbers")

def Division():
    print(" Enter numbers you want to add them.")
    try:
        Number1 = int(input("Number one: "))
        Number2 = int(input("Number Two: "))

        Result =  Number1 / Number2
        print(f"Result: {Result}")
    except ValueError:
            print("Please Inter valid numbers")
    except ZeroDivisionError:
        print("You can't divide by zore.")


def main():
    while True:
        Menu()
        operation = input("Enter your Operation: ")

        if operation == "1":
            addition()
 
        elif operation == "2":
            subtraction()

        elif operation == "3":
            Multiplication()
 
        elif operation == "4":
            Division()
 
        elif operation == "5":
            print("Good bye. See you later")
            break
        else:
            print("Invalid choice. Please Try again.")


main()
