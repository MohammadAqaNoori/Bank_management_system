def create_account(name, initial_balance):
    # Generate account number
    account_number = generate_account_number()
    # Create account with name and initial balance
    accounts[account_number] = {'name': name, 'balance': initial_balance}
    return account_number

def deposit(account_number, amount):
    # Add amount to the account balance
    accounts[account_number]['balance'] += amount
    return accounts[account_number]['balance']

def withdraw(account_number, amount):
    # Check if sufficient funds are available
    if accounts[account_number]['balance'] >= amount:
        # Withdraw amount from the account balance
        accounts[account_number]['balance'] -= amount
        return accounts[account_number]['balance']
    else:
        return "Insufficient funds. Withdrawal not processed."

def check_balance(account_number):
    # Return the current balance of the account
    return accounts[account_number]['balance']

def main():
    while True:
        print("Choose an option:")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            account_number = create_account(name, initial_balance)
            print(f"Account created successfully. Account number: {account_number} Account of: {name}")
        
        elif choice == '2':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            new_balance = deposit(account_number, amount)
            print(f"Amount deposited successfully. New balance: {new_balance} Account of: {name}")
        
        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            new_balance = withdraw(account_number, amount)
            if isinstance(new_balance, str):
                print(new_balance)
            else:
                print(f"Withdrawal successful. New balance: {new_balance} Account of: {name}")
        
        elif choice == '4':
            account_number = int(input("Enter account number: "))
            balance = check_balance(account_number)
            print(f"Current balance: {balance} Account of: {name}")
        
        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Dictionary to store accounts with account number as key
accounts = {}

def generate_account_number():
    return len(accounts) + 1
main()