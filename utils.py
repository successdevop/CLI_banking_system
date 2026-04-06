import random
from storage import save_data
from config import DATA_FILE


def authenticate(customers_data: list):
    """
    this function authenticate users by first of all confirming that the account number enter is correct.
    It checks the customer's data to make this confirmation. If the account is correct, it returns
    the user with the account else it prints account not found.
    If the account is found, it checks if the user account is locked, if it is locked, it prints a
    message telling the user to visit the bank to unblock the account else it asks the user to enter
    their PIN. The user has three attempts to enter their pin else the account is Locked. If the user
    meets all the conditions, the user can carry out their transaction
    :param customers_data: customers database
    """
    customer = find_user(customers_data)
    if not customer:
        return

    if customer["user_locked"]:
        print("Account is locked, user cannot transact, please visit your bank")
        return

    attempts = 3
    while True:
        if attempts < 1:
            customer["user_locked"] = True
            save_data(customers_data, DATA_FILE)
            print("Account locked")
            return

        pin = input("Enter your pin: ")
        if pin != customer["pin"]:
            attempts -= 1
            print(f"You have {'No attempts' if attempts == 0 else attempts} left")
        else:
            if pin == customer["pin"]:
                return customer


def generate_id(customers_data: list) -> int:
    """
    this function generates a unique id for every account created for a customer in the
    bank
    :param customers_data: customer's database
    :return: an int value
    """
    customer_id = 1
    while True:
        if not any(acct["id"] == customer_id for acct in customers_data):
            return customer_id
        customer_id += 1


def generate_secret_keys(customers_data: list, range_value: int) -> str:
    """
    this function is used to generate secret keys of any number of character. It can be
    used to generate account_numbers, PIN e.t.c. It uses the while lop to generate any
    amount of number required(range_value)
    :param range_value: the number of secret keys to be generated
    :param customers_data: customer's database
    :return: a string of unique random numbers
    """
    while True:
        acc = "".join(str(random.randint(1, 9)) for _ in range(range_value))
        if not any(user["account_number"] == acc for user in customers_data):
            return acc


def validate_name(prompt) -> str:
    """
    this function validates the user's name
    :param prompt: it takes the user input from the CLI
    :return: a string that must be or greater than three characters
    """
    while True:
        name = input(prompt).strip()
        if name and len(name) >= 3:
            return name
        print("Name cannot be empty and must be at-least 3 characters")


def validate_amount_input(prompt) -> float:
    """
    this function takes the user input and checks if it is an actually number
    and that the number is also not negative
    :param prompt: user input
    :return: float number
    """
    while True:
        amount = input(prompt)
        if amount.isnumeric():
            if float(amount) > 0:
                return float(amount)
            else:
                print("Amount must be greater than 0")
        else:
            print("Invalid amount: (amount cannot be negative/empty)")


def find_user(customers_data: list):
    """
    this function searches for a user in our customer's list. If the user exist, it returns
    the user otherwise it prints user not found
    :param customers_data: customer's database
    :return: a user dictionary
    """
    acc = input("Enter account number: ")
    if not acc.isnumeric() or len(acc) != 10:
        print("Invalid account number")
        return

    customer = next((c for c in customers_data if c["account_number"] == acc), None)
    if not customer:
        print("Account not found")
        return

    return customer


def display_options_menu():
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Balance")
    print("6. Transaction History")
    print("7. Analytics")
    print("8. Top_3_account")
    print("9. Find User")
    print("0. Exit")
