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
            transtions = json.load(file)
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
    category = input("Enter the transtion category: ")
    description = input("Enter the description: ")
    date = input("enter the transtion date: ")

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
    category = input("Enter the transtion category: ")
    description = input("Enter the description: ")
    date = input("enter the transtion date: ")

    transtion = {
        "ID": transtion_id,
        "Amount": amount,
        "type": "Expense",
        "Category": category,
        "Description": description,
        "Date": date
    }
    transtions.append(transtion)
    
    save_transtion(transtions)
    print("Transtion added seccussfully.")

    
def view_transtions(transtions):    
    if transtions:
        for transtion in transtions:
            print(f"ID:{transtion["ID"]} Amount:{transtion["Amount"]} type:{transtion["type"]} Category:{transtion["Category"]} Description:{transtion["Description"]} Date: {transtion["Date"]}")
    else:
        print("There is no transtions yet.")


    
def view_Categories(transtions):
    if transtions:
        for transtion in transtions:
            print(f"{transtion["Category"]}")
    else: 
        print("There is no transtions yet.")

def Monthly_Summary():
    pass
def Total_Income(transtions):
    Total_Income = 0

    for transtion in transtions:
        if transtion["type"] == "Income":
            Total_Income += transtion["Amount"]

    print(f"Total Income: {Total_Income}")
    return Total_Income

    
def Total_Expenses(transtions):
    Total_Expenses = 0

    for transtion in transtions:
        if transtion["type"] == "Expense":
            Total_Expenses += transtion["Amount"]
            
    print(f"Total expense: {Total_Expenses}")
    return Total_Expenses


def Current_Balance(transtions):
    Total_Income = Total_Income(transtions)
    Total_Expenses = Total_Expenses(transtions)

    Balance = Total_Income - Total_Expenses

    print(f"Current Balance: {Balance}")



def Export_to_CSV():
    pass
def Import_from_CSV():
    pass



def main():
    transtions = load_transactions()

    while True:
        menu()
        chioce = input("Enter your choice: ")

        if chioce == "1":
            add_income(transtions)
        elif chioce == "2":
            add_expense(transtions)
        elif chioce == "3":
            view_transtions(transtions)
        elif chioce == "4":
            view_Categories(transtions)
        elif chioce == "5":
            Monthly_Summary()
        elif chioce == "6":
            Total_Income(transtions)
        elif chioce == "7":
            Total_Expenses(transtions)
        elif chioce == "8":
            Current_Balance(transtions)
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