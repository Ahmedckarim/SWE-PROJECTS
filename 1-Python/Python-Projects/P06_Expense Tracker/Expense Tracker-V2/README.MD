# Expense Tracker

A simple command-line **Expense Tracker** built with **Python and Object-Oriented Programming (OOP)**.

The application allows users to record expenses, store them in a JSON file, calculate spending summaries, manage a budget, and import/export expenses using CSV files.

## Features

* Add a new expense

  * Description
  * Amount
  * Category
  * Date
* Save expenses to `expenses.json`
* Load saved expenses when the program starts
* View all expenses
* Calculate total spending
* View spending by category
* Set a budget
* Check remaining budget
* Export expenses to CSV
* Import expenses from CSV
* Persistent data storage

## Project Structure

```text
expense-tracker/
│
├── main.py
├── expense.py
├── expense_tracker.py
├── expenses.json
├── expenses.csv
├── README.md
└── .gitignore
```

## Class Structure

### Expense

The `Expense` class represents a single expense.

```text
Expense
   │
   ├── description
   ├── amount
   ├── category
   └── date
```

### ExpenseTracker

The `ExpenseTracker` class manages expenses and provides the main application functionality.

```text
ExpenseTracker
   │
   ├── add_expense()
   ├── save_data()
   ├── load_data()
   ├── view_expenses()
   ├── calculate_total()
   ├── category_summary()
   ├── remaining_budget()
   ├── export_csv()
   └── import_csv()
```

## Technologies

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON**
* **CSV**
* **File Handling**
* **Command-Line Interface (CLI)**

## How It Works

### 1. Add Expense

The user enters information about an expense:

```text
Description: Lunch
Amount: 5.50
Category: Food
Date: 2026-09-11
```

The expense is then stored by the application.

### 2. Save Data

Expenses are stored in:

```text
expenses.json
```

Example:

```json
[
    {
        "description": "Lunch",
        "amount": 5.5,
        "category": "Food",
        "date": "2026-09-11"
    }
]
```

### 3. View Expenses

The application displays all saved expenses.

```text
1. Lunch | $5.50 | Food | 2026-09-11
2. Transport | $3.00 | Transport | 2026-09-11
```

### 4. Calculate Total

The application calculates the total amount spent.

```text
Total spending: $8.50
```

The basic calculation is:

```python
total = sum(expense.amount for expense in expenses)
```

### 5. Spending by Category

Expenses can be summarized by category.

Example:

```text
Spending by category:

Food:       $25.50
Transport:  $15.00
Education:  $10.00
```

### 6. Set a Budget

The user can define a spending budget.

```text
Enter budget: $100
```

### 7. Remaining Budget

The application calculates how much money remains:

```text
Budget:          $100.00
Total spending:   $50.50
------------------------
Remaining:        $49.50
```

The calculation is:

```text
Remaining Budget = Budget - Total Spending
```

### 8. Export to CSV

Expenses can be exported to:

```text
expenses.csv
```

Example:

```csv
description,amount,category,date
Lunch,5.50,Food,2026-09-11
Transport,3.00,Transport,2026-09-11
```

### 9. Import from CSV

Previously exported expenses can be imported back into the application.

This makes it possible to move or restore expense data using a CSV file.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2. Enter the project directory

```bash
cd expense-tracker
```

### 3. Run the application

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

## Example Menu

```text
=========================
     EXPENSE TRACKER
=========================

1. Add Expense
2. View Expenses
3. Calculate Total
4. Category Summary
5. Set Budget
6. Remaining Budget
7. Export to CSV
8. Import from CSV
9. Exit

Choose an option:
```

## Data Persistence

The application uses a JSON file to keep expenses available after the program is closed.

When the program starts:

```text
Program starts
      │
      ▼
load_data()
      │
      ▼
expenses.json
      │
      ▼
Expenses loaded
```

When a new expense is added:

```text
Add Expense
     │
     ▼
Expense object
     │
     ▼
save_data()
     │
     ▼
expenses.json
```

Therefore, expenses remain available when the application is closed and opened again.

## Learning Objectives

This project is designed to practice:

* Python classes and objects
* Encapsulation
* Methods
* Lists and dictionaries
* File handling
* JSON serialization/deserialization
* CSV reading and writing
* Exception handling
* Data validation
* CLI application design
* Basic software project structure
* Git and GitHub

## Future Improvements

Possible improvements for future versions:

* [ ] Edit an expense
* [ ] Delete an expense
* [ ] Search expenses
* [ ] Filter by category
* [ ] Filter by date
* [ ] Monthly spending reports
* [ ] Multiple budgets
* [ ] Budget warnings
* [ ] Better input validation
* [ ] Unit tests
* [ ] SQLite database
* [ ] REST API
* [ ] Web interface

## Project Roadmap

```text
Python Basics
     │
     ▼
OOP
     │
     ▼
JSON File Storage
     │
     ▼
CSV Import/Export
     │
     ▼
Expense Tracker
     │
     ▼
SQL + PostgreSQL
     │
     ▼
FastAPI
     │
     ▼
Business Applications
```

## Author

**Ahmed**

This project is part of my journey to become a stronger **Python / Full-Stack / AI & Data developer**.

## License

This project is for learning and educational purposes.
