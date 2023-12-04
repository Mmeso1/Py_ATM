import random
import os
import sys
import time

# This function is used to clear the terminal for a better UI
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# This is used to generate the header text on the terminal
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    header = f"\033[1m{text}\033[0m"
    print(' ' * padding + header)

# This is used to generate the left header text on the terminal
def print_left(text):
    terminal_width = os.get_terminal_size().columns
    header = f"\033[1m{text}\033[0m"
    print(header.ljust(terminal_width))


# Initialize the user_data array as a global variable
user_data = []

# This is where the account creation method starts from
def account_creation():
    print_centered("ACCOUNT CREATION")

    while True:
        name = input("Enter your full name: ")
        pin = input("\nEnter your PIN (It should not be more than 8 digits): ")

        if len(name.split(" ")) >= 2 and len(pin) <= 8:
            break

        clear_terminal()
        print_centered("ACCOUNT CREATION")
        print_centered("\nEither your full name is not entered or your PIN is more than 8 digits.")

    account_number = ''.join(random.sample('0123456789', 10))

    clear_terminal()
    print_centered("ACCOUNT CREATION")
    print("!! Account Creation Successful !!")
    print(f"\nThis is your account number: --- {account_number} ---")
    print("\n!! Try not to forget it, as you will be asked for it during authentication !!")

    user_info = {
        "name": name,
        "account_number": account_number,
        "pin": pin
    }

    user_data.append(user_info)


# This is where the login method starts from
def login():
    print_centered("LOGIN")
    account_number = input("Enter your account number: ")
    pin = input("Enter your pin: ")

    for user in user_data:
        if user["account_number"] == account_number and user["pin"] == pin:
            print("!! Login Successful !!")
        else:
            print("Invalid account number or pin. Please try again.")
            time.sleep(2)  # Pause the program execution for 5 seconds
            clear_terminal()
            login()  # Prompt for login again if the credentials are invalid


# THIS IS WHERE THE HOME VIEW FUNCTION STARTS FROM
def home_view():
    global account_balance
    time.sleep(1)
    clear_terminal()
    print_centered("!! WELCOME !!")
    print_left("\nWhich of these operations will you like to carry out: ")
    print_left("1. Withdraw")
    print_left("2. Deposit")
    print_left("3. Check Account balance")
    print_left("4. Exit Program")

    page = input("\n\nResponse : ")

    if page == '1':
        withdraw()
    elif page == '2':
        deposit()
    elif page == '3':
        print_centered("ACCOUNT BALANCE")
        print(f"This is your account balance: {account_balance}")
        home_view()
    elif page == '4':
        sys.exit()
    else:
        print_left("Invalid Response")
        home_view()

account_balance = 0

# THIS IS WHERE THE WITHDRAW FUNCTION STARTS FROM
def withdraw():
    global account_balance
    time.sleep(1)
    clear_terminal()
    print_centered("WITHDRAWAL PAGE")
    value = int(input("Amount (to withdraw): "))
    if value <= account_balance:
        print_left("!! Withdrawal Successful !!")
        account_balance -= value
        print(f"This is your current account balance: {account_balance}")
    else:
        print_left("!! Unsuccessful !!")
        print(f"This is your current account balance: {account_balance}")

    while True:
        reply = input("\n---------------------- Press 1 to go to the login page ----------------------: ")
        if reply == '1':
            break
        else:
            print("Invalid input. Please enter '1' to go to the login page.")

    home_view()

# THIS IS WHERE THE DEPOSIT FUNCTION STARTS FROM
def deposit():
    time.sleep(1)
    clear_terminal()
    global account_balance
    print_centered("DEPOSIT PAGE")

    while True:
        value = int(input("Amount (to deposit): "))
        if value > 0:
            print_left("!! Deposit Successful !!")
            account_balance += value
            print(f"This is your current account balance: {account_balance}")
            break
        else:
            print_left("!! Unsuccessful !!")
            print("Deposit a reasonable amount")

    while True:
        reply = input("\n---------------------- Press 1 to go to the login page ----------------------: ")
        if reply == '1':
            break
        else:
            print("Invalid input. Please enter '1' to go to the login page.")

    home_view()

 
    

account_creation()
login()
home_view()
