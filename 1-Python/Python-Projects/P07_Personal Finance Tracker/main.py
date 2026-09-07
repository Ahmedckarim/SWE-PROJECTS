import csv
import json
from datetime import datetime

file_name = "transaction.json"

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

def load_transactions():
    try:
        with open(file_name, "r") as file:
            transtions = json.dump(file)
            return transtions
    except FileNotFoundError:
        print("There is no transactions to show.")
        return []
    except json.JSONDecodeError:
        print("Error: The Json file is corrupted or invalid.")
    
def save_transtion(transtions):
    with open(file_name, "w") as file:
        json.dump(transtions, file)



def add_income(transtions):
    transtion_id = int(input("Enter transtion ID: "))
    amount = int(input("Enter an amount: "))
    category = int("Enter the transtion category: ")
    description = int("Enter the description: ")
    date = int("enter the transtion date: ")

    transtion = {
        "ID": transtion_id,
        "Amount": amount,
        "type": "Income",
        "Category": category,
        "Description": description,
        "Date": date
    }
    transtions.append(transtion)

    save_transtion(transtions)
    print("Transtion added seccussfully.")
    
def add_expense(transtions):
    transtion_id = int(input("Enter transtion ID: "))
    amount = int(input("Enter an amount: "))
    category = int("Enter the transtion category: ")
    description = int("Enter the description: ")
    date = int("enter the transtion date: ")

    transtion = {
        "ID": transtion_id,
        "Amount": amount,
        "type": "expense",
        "Category": category,
        "Description": description,
        "Date": date
    }
    transtions.append(transtion)


    
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