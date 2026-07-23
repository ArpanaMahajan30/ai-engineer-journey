expenses = []

def add_expense(name: str, amount: float):
    """Add an expense to the list."""
    expenses.append({"name": name, "amount": amount})

def view_expenses():
    """View all expenses"""
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expenses:")
        for expense in expenses:
            print(f"{expense['name']}: ${expense['amount']:.2f}")

def calculate_total():
    """Calculate the total of all expenses."""
    return sum(expense['amount'] for expense in expenses)

def search_expense():
    """Search for an expense by name."""
    search_name = input("Enter the name of the expense to search: ")
    found_expenses = [expense for expense in expenses if expense['name'].lower() == search_name.lower()]
    if found_expenses:
        print("Found:")
        for expense in found_expenses:
            print(f"{expense['name']}: ${expense['amount']:.2f}")
    else:
        print("No expense found with that name.")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Search Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter expense name: ")
            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            add_expense(name, amount)
            print(f"Added expense: {name} - ${amount:.2f}")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print(f"Total amount spent: ${calculate_total():.2f}")
        elif choice == '4':
            search_expense()
        elif choice == '5':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
