import personal_finance_tracker


def menu():
    print("\n==============================")
    print(" Personal Finance TRACKER")
    print("==============================")

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

    print("==============================")

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
            view_categories(transtions)
        elif chioce == "5":
            monthly_summary()
        elif chioce == "6":
            total_income(transtions)
        elif chioce == "7":
            total_expenses(transtions)
        elif chioce == "8":
            Current_balance(transtions)
        elif chioce == "9":
            export_to_CSV()
        elif chioce == "10":
            import_from_CSV()
        elif chioce == "11":
            print("Exiting...")
            return
        else:
            print("Invalid choice. please enter a valid choice.")



main()