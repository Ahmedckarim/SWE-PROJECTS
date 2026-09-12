from data_entry import get_amount, get_category, get_date , get_description

def menu():
    print("\n==============================")
    print(" Personal Finance TRACKER")
    print("==============================")

    print("1. Add transtion")
    print("5. Monthly Summary")
    print()
    print("10. Import from CSV")
    print("11. Exit")

    print("==============================")

def main():
    while True:
        menu()
        choice = input("Choice: ")
    pass


if __name__== "__main__":
    main()