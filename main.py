# ==========================================
# Project Title: Pocket Expense Tracker
# Course: SQE | Semester: Fall 2023
# ==========================================

import os

# SECURITY FLAW 1: Hardcoded Admin Credentials (Snyk easily catch karega)
ADMIN_PASSWORD = "SuperSecretPassword123"

# Global data storage (In-memory list of dictionaries)
expenses = [
    {"amount": 500, "category": "Food", "description": "Lunch with friends"},
    {"amount": 1200, "category": "Travel", "description": "Fuel"},
]

def show_menu():
    print("\n=== POCKET EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Filter Expenses by Category")
    print("5. Exit")

def add_expense():
    print("\n--- Add New Expense ---")
    try:
        # BUG 1 (Logical): Humne lower limit check nahi ki. User negative expense bhi daal sakta hai!
        amount = float(input("Enter amount (PKR): "))
        category = input("Enter category (e.g., Food, Travel, Utilities): ").strip()
        description = input("Enter description: ").strip()
        
        new_expense = {"amount": amount, "category": category, "description": description}
        expenses.append(new_expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Amount must be a number.")

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    # Proper programming logic using Loops
    for index, exp in enumerate(expenses, 1):
        print(f"{index}. {exp['category']}: PKR {exp['amount']} ({exp['description']})")

def view_total():
    # BUG 2 (Logical): Total calculate karte waqt function direct global variable ko bina zero handles ke sum kar raha hai, 
    # Aur agar list khali ho ya strings aa jayein toh crash ho sakta hai.
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Money Spent: PKR {total}")

def filter_by_category():
    print("\n--- Filter by Category ---")
    # Clean input and enforce lowercase casing
    cat = input("Enter category name to filter: ").strip().lower()
    found = False
    
    for exp in expenses:
        # Standardizing both stored values and input keys to prevent case-sensitivity bugs
        if exp['category'].lower() == cat:
            print(f"- PKR {exp['amount']} | {exp['description']}")
            found = True
            
    if not found:
        print(f"No expenses found in '{cat}' category.")

def admin_login():
    # SECURITY FLAW 2: Insecure Input / Authentication Bypass potential
    print("\n--- Admin Verification ---")
    password = input("Enter admin password to access system: ")
    if password == ADMIN_PASSWORD:
        print("Access Granted!")
        return True
    else:
        print("Access Denied!")
        return False

def main():
    # Admin login verification check at start
    if not admin_login():
        return

    # Main Application Loop
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        
        # Conditional Logic (if-else)
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_total()
        elif choice == '4':
            filter_by_category()
        elif choice == '5':
            print("Thank you for using Pocket Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()