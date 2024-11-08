from expense_management import add_expense
from monthly_reports import display_monthly_report, display_category_report
from file_handling import save_expenses_to_file, load_expenses_from_file

def main():
    FILENAME = 'expenses.txt'
    load_expenses_from_file(FILENAME)
    
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Monthly Report")
        print("3. View Category Report")
        print("4. Save & Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            month = input("Enter month: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
                add_expense(month, category, description, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == '2':
            month = input("Enter month: ")
            display_monthly_report(month)
        
        elif choice == '3':
            month = input("Enter month: ")
            category = input("Enter category: ")
            display_category_report(month, category)
        
        elif choice == '4':
            save_expenses_to_file(FILENAME)
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
