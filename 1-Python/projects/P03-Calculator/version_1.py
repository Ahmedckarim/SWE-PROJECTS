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

def menu():
    print("=== Calculator program ===")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

def addition():
    print(" Enter numbers you want to add them.")
    try:
        number_1 = int(input("Number one: "))
        number_2 = int(input("Number Two: "))

        result =  number_1 + number_2
        print(f"Result: {result}")
    except ValueError:
        print("Please Inter valid numbers")


def subtraction():
    print(" Enter numbers you want to subtract them.")
    try:
        number_1 = int(input("Number one: "))
        number_2 = int(input("Number Two: "))

        result =  number_1 - number_2
        print(f"Result: {result}")
    except ValueError:
        print("Please Inter valid numbers")


def multiplication():
    print(" Enter numbers you want to multiply them.")
    try:
        number_1 = int(input("Number one: "))
        number_2 = int(input("Number Two: "))

        result =  number_1 * number_2
        print(f"Result: {result}")
    except ValueError:
        print("Please Inter valid numbers")

def division():
    print(" Enter numbers you want to devide them.")
    try:
        number_1 = int(input("Number one: "))
        number_2 = int(input("Number Two: "))

        result =  number_1 / number_2
        print(f"Result: {result}")
    except ValueError:
            print("Please Inter valid numbers")
    except ZeroDivisionError:
        print("You can't divide by zore.")


def main():
    while True:
        menu()
        operation = input("Enter your Operation: ")

        if operation == "1":
            addition()
 
        elif operation == "2":
            subtraction()

        elif operation == "3":
            multiplication()
 
        elif operation == "4":
            division()
 
        elif operation == "5":
            print("Good bye. See you later")
            break
        else:
            print("Invalid choice. Please Try again.")


main()
