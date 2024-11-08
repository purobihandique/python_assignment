import json
from expense_management import expenses_by_month

def save_expenses_to_file(filename):
    """Save the current expenses to a file."""
    with open(filename, 'w') as file:
        json.dump(expenses_by_month, file)
    print(f"Expenses saved to {filename}.")

def load_expenses_from_file(filename):
    """Load expenses from a file."""
    global expenses_by_month
    try:
        with open(filename, 'r') as file:
            expenses_by_month = json.load(file)
            
            for month in expenses_by_month:
                expenses_by_month[month] = [tuple(expense) for expense in expenses_by_month[month]]
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing file found: {filename}. Starting fresh.")
    except json.JSONDecodeError:
        print("Error decoding the file. Starting with empty expenses.")
