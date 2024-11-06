accounts_file = "accounts.txt"


def is_valid_account_no(account_number):
    return len(str(account_number)) == 13 and str(account_number).isdigit()


def load_accounts():
    return accounts


def save_accounts(accounts):
    with open(accounts_file, 'w') as file:
        for account_number, balance in accounts.items():
            file.write(f"{account_number},{balance}\n")
            
            

def create_account(accounts):
    print("Invalid account number . Try again.")
    
    
    
def dposite(accounts):
    account_number = input("Enter your account number: ")
    
    
    if account_number in accounts:
        try:
            amount = float(input("Enter amount to deposit:"))
            accounts[account_number] += amount
            save_accounts(accounts)
            print(f"Deposited {amount}. New balance: {accounts[account_number]}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    else:
        print("Account not found. Please create an account first.")
        
        
def transfer(accounts):
    sender = input("Enter your account number:")
    recipient = input("Enter recipient's account number: ")
    
    
    if sender in accounts and recipient in accounts:
        try:
            amount = float(input("Enter amount to transfer:"))
            if amount <= accounts[sender]:
                accounts[sender] -= amount
                accounts[recipient] += amount
                save_accounts(accounts)
                print(f"Transfer successful! New balance: {accounts[sender]}")
            else:
                print("Insufficient funds for the tranfer.")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
    else:
        if sender not in accounts:
            print("Sender account not found. Please create an account first.")
        if recipient not in accounts:
            print("Recipient account not found. Please check the account number.")
