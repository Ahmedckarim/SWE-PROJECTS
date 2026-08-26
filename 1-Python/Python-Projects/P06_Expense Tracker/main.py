# expense tracker CLI Application
# Load And Save expenses 

# 1. Add expense
# 2. List expenses
# 3. Update expense
# 4. Delete expense
# 5. View summary



def menu():
    print("1. Add expense")
    print("2. List expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. View summary")
    print("6. Exit")

def load_expense():
    pass
def save_expense():
    pass

def add_expense():
    pass
def view_all_expenses():
    pass
def update_expense():
    pass
def delete_expense():
    pass
def view_sammury():
    pass

def main():

    expenses = load_expense()

    while True:
        menu()
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

menu()
