# monthly_reports.py

from expense_management import calculate_total_expenses, calculate_expenses_by_category, get_all_expenses

def display_monthly_report(month):
    """Display all expenses for a given month."""
    expenses = get_all_expenses(month)
    if not expenses:
        print(f"No expenses recorded for {month}.")
        return
    print(f"Expenses for {month}:")
    for category, description, amount in expenses:
        print(f" - {category}: {description} - ${amount:.2f}")
    print(f"Total Expenses: ${calculate_total_expenses(month):.2f}")

def display_category_report(month, category):
    """Display total expenses for a specific category in a given month."""
    total = calculate_expenses_by_category(month, category)
    print(f"Total {category} expenses for {month}: ${total:.2f}")
