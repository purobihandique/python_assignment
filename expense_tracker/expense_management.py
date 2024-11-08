expenses_by_month = {}

def add_expense(month, category, description, amount):
    """Add an expense to the specified month."""
    expense = (category, description, amount)
    if month in expenses_by_month:
        expenses_by_month[month].append(expense)
    else:
        expenses_by_month[month] = [expense]
    print(f"Added expense: {expense}")

def calculate_total_expenses(month):
    """Calculate total expenses for a specific month."""
    if month in expenses_by_month:
        return sum(expense[2] for expense in expenses_by_month[month])
    return 0

def calculate_expenses_by_category(month, category):
    """Calculate total expenses for a specific category in a month."""
    if month in expenses_by_month:
        return sum(expense[2] for expense in expenses_by_month[month] if expense[0] == category)
    return 0

def get_all_expenses(month):
    """Retrieve all expenses for a specific month."""
    return expenses_by_month.get(month, [])
