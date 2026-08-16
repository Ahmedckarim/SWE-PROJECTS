Calculator  based on CL

Version1  Functional requirements
    Display a menu with available operations:
    Addition
    Subtraction
    Multiplication
    Division
    Exit

    Ask the user to choose an operation.
    Ask for two numbers.
    Perform the selected operation.
    Display the result.
    Return to the menu after each calculation.
    Allow the user to exit the program.

I bulid V1 for first try and get some errors lie ( variable naming, using global variable (Result), wrong masseges or language errors. ). then I solve them.

The main problem was repeated a lot of code.

    Look at these three functions:

        addition()
        subtraction()
        Multiplication()
        Division()

    They all do:

        Ask for number 1
        Ask for number 2
        Convert input
        Perform operation
        Print result
        Handle ValueError

    Only the actual operation changes.

Next I'll build v2 to solve, improve and add these extra  features.

    Add exponentiation.
    Add modulus.
    Add square root.
    Keep a calculation history.
    Allow the user to clear the history.

