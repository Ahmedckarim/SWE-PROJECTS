# expense tracker CLI Application
# Load And Save expenses 

# 1. Add expense
# 2. List expenses
# 3. Update expense
# 4. Delete expense
# 5. View summary
import json
import csv



json_file_name = "Expenses.json"

def menu():
    print("1. Add expense")
    print("2. List expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. View summary")
    print("6. Exit")

def load_expense():
    try:
        with open(json_file_name, "r") as file:
            return json.load( file)
        
    except FileNotFoundError:
        print("There are no expenses available.")
        return []
    except json.JSONDecodeError:
        print("Error: The Json file is corrupted or invalid.")
    
def save_expense(expenses):
    with open(json_file_name, "w") as file:
        json.dump(expenses, file)
        print("expense Saved")

def add_expense(expenses):
    description = input("Enter a description: ")
    amount = int(input("Enter an amount: "))

    if amount <= 0: 
        print("Amount can not be a zero or negative number.")
        return

    expense = {
        "description": description ,
        "Amount": amount,
    }
    expenses.append(expense)
    
    save_expense(expenses)
    print("Expense added successfully.")


 
def view_all_expenses():
    pass
def update_expense():
    pass
def delete_expense():
    pass
def view_sammury():
    pass

def main():

    
    while True:
        menu()
        expenses = load_expense()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all_expenses(expenses)
        elif choice == "3":
            update_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            view_sammury(expenses)
        elif choice == "6":
            print("Thanks for using this app. bye👋")
            break

main()
