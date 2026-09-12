import csv
import json
from datetime import date

file_name = "transaction.json"




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
    try:
        transtion_id = int(input("Enter transtion ID: "))
        if any(transtion["ID"] == transtion_id for transtion in transtions):
            print("This transtion ID already exist.")
            return
        amount = int(input("Enter an amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        category = input("Enter the transtion category: ")
        if not category:
            print("category can not be empty.")
            return
        description = input("Enter the description: ")
        if not description:
            print("Description can not be empty.")
            return
        transaction_date = input("Enter the transaction date (YYYY-MM-DD): ")

        transtion = {
            "ID": transtion_id,
            "Amount": amount,
            "type": "Income",
            "Category": category,
            "Description": description,
            "Date": transaction_date
        }
        transtions.append(transtion)

        save_transtion(transtions)
        print("Transtion added seccussfully.")
    except ValueError:
        print("Please enter numbers where reqiered.")

    
def add_expense(transtions):
    try:
        transtion_id = int(input("Enter transtion ID: "))
        if any(transtion["ID"] == transtion_id for transtion in transtions):
            print("This transtion ID already exist.")
            return
        amount = int(input("Enter an amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        category = input("Enter the transtion category: ")
        if not category:
            print("category can not be empty.")
            return
        description = input("Enter the description: ")
        if not description:
            print("Description can not be empty.")
            return
        transaction_date = input("Enter the transaction date (YYYY-MM-DD): ")
        transtion = {
            "ID": transtion_id,
            "Amount": amount,
            "type": "Expense",
            "Category": category,
            "Description": description,
            "transaction_date": date
        }
        transtions.append(transtion)
        
        save_transtion(transtions)
        print("Transtion added seccussfully.")
    except ValueError:
        print("Please enter numbers where reqiured.")

    
def view_transtions(transtions):    
    if transtions:
        for transtion in transtions:
            print(f"ID:{transtion["ID"]} Amount:{transtion["Amount"]} type:{transtion["type"]} Category:{transtion["Category"]} Description:{transtion["Description"]} Date: {transtion["Date"]}")
    else:
        print("There is no transtions yet.")


    
def view_categories(transtions):
    if transtions:
        for transtion in transtions:
            print(f"{transtion["Category"]}")
    else: 
        print("There is no transtions yet.")

def monthly_summary():
    pass

def total_income(transtions):
    Total_Income = 0

    for transtion in transtions:
        if transtion["type"] == "Income":
            Total_Income += transtion["Amount"]

    print(f"Total Income: {Total_Income}")
    return Total_Income

    
def total_expenses(transtions):
    Total_Expenses = 0

    for transtion in transtions:
        if transtion["type"] == "Expense":
            Total_Expenses += transtion["Amount"]
            
    print(f"Total expense: {Total_Expenses}")
    return Total_Expenses


def Current_balance(transtions):
    income = total_income(transtions)
    expense = total_expenses(transtions)

    Balance = income - expense

    print(f"Current Balance: {Balance}")



def export_to_CSV():
    pass
def import_from_CSV():
    pass


