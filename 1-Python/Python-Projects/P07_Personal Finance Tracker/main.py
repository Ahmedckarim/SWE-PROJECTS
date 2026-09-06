
def menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Categories")
    print("5. Monthly Summary")
    print("6. Total Income")
    print("7. Total Expenses")
    print("8. Current Balance")
    print("9. Export to CSV")
    print("10. Import from CSV")
    print("11. Exit")


def add_income():
    pass
def add_expense():
    pass
def view_transtions():
    pass
def view_Categories():
    pass
def Monthly_Summary():
    pass
def Total_Income():
    pass
def Total_Expenses():
    pass
def Current_Balance():
    pass
def Export_to_CSV():
    pass
def Import_from_CSV():
    pass



def main():
    while True:
        menu()
        chioce = input("Enter your choice: ")

        if chioce == "1":
            add_income()
        elif chioce == "2":
            add_expense()
        elif chioce == "3":
            view_transtions()
        elif chioce == "4":
            view_Categories()
        elif chioce == "5":
            Monthly_Summary()
        elif chioce == "6":
            Total_Income()
        elif chioce == "7":
            Total_Expenses()
        elif chioce == "8":
            Current_Balance()
        elif chioce == "9":
            Export_to_CSV()
        elif chioce == "10":
            Import_from_CSV()
        elif chioce == "11":
            print("Exiting...")
            return
        else:
            print("Invalid choice. please enter a valid choice.")



main()