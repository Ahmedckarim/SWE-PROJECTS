# Features
 ## 1. Add expense
 * Description
 * Amount
 * Category
 * Date
## 2. Save expenses to expenses.json
## 3. View expenses
## 4. Summarize totals
 * Total spending
 * Spending by category
## 5. Set a budge
## 6. Show remaining budget
## 7. Export expenses → CSV
## 8. Import expenses ← CSV
## 9. Data remains available after closing/reopening the program.




Expense
   │
   ├── description
   ├── amount
   ├── category
   └── date
       
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