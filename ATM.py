name = ""
address = ""
contact = ""
balance = 0
def menu():
    print("\n===== BANK =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")
def new_acc():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    contact = input("Enter your contact no: ")
    balance = int(input("Enter initial deposit: "))
    print("\nYour account has been created successfully!")
    print("Initial Balance: Rs.", balance)
    return name, address, contact, balance
def deposit_money(balance):
    print("\n===== DEPOSIT MONEY =====")
    money = int(input("Enter money to deposit: "))
    balance = balance + money
    print("Money deposited successfully!")
    print("Your current balance is: Rs.", balance)
    return balance
def withdraw_money(balance):
    print("\n===== WITHDRAW MONEY =====")
    money = int(input("Enter money you want to withdraw: "))
    if money <= balance:
        balance = balance - money
        print("Please collect your cash.")
        print("Your current balance is: Rs.", balance)
    else:
        print("You don't have sufficient balance.")
    return balance
def account_details(name, address, contact, balance):
    print("\n===== ACCOUNT DETAILS =====")
    print("Name:", name)
    print("Address:", address)
    print("Contact No:", contact)
    print("Balance: Rs.", balance)
for i in range(5):
    menu()
    ch = int(input("\nEnter your choice: "))
    if ch == 1:
        name, address, contact, balance = new_acc()
    elif ch == 2:
        balance = deposit_money(balance)
    elif ch == 3:
        balance = withdraw_money(balance)
    elif ch == 4:
        account_details(name, address, contact, balance)
    elif ch == 5:
        print("\nThank you for using ATM!")
        break
    else:
        print("\nInvalid choice!")