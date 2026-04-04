import random
from storage import save_data
from config import DATA_FILE, LOG_MSG


def account_and_pin_number_validator():


def authenticate(customers_data: list):
    acc = input("Enter account number: ")
    customer = next((c for c in customers_data if c["account_number"] == acc), None)
    if not customer:
        print("Account not found")
        return

    attempts = 3
    while True:
        acc = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if attempts < 1:
            customer["user_locked"] = True
            save_data(customers_data, DATA_FILE)
            return
        pin = input("Enter your pin: ")
        if pin != customer["pin"]:
            attempts -= 1
            print(f"You have {attempts} left")
        else:
            if pin == customer["pin"]:


def generate_id(customers_data: list):
    """
    this function generates a unique id for every account created for a customer in the
    bank
    :param: customer's database
    :return: an int value
    """
    customer_id = 1
    while True:
        if not any(acct["id"] == customer_id for acct in customers_data):
            return customer_id
        customer_id += 1


def generate_account_number(customers_data: list) -> str:
    """
    this function generates account number for users. It uses the while loop to generate
    10 random numbers stored in a list, which makes the customer unique account number
    :param: customer's database
    :return: a string of 10 random numbers
    """
    while True:
        acc = "".join(str(random.randint(1, 9)) for _ in range(10))
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


def generate_pin(customers_data: list) -> str:
    """
    this function generates pin for users. It uses the while loop to generate
    4 random numbers stored in a list, which makes the customer unique pin
    :param: customer's database
    :return: a string of 4 random numbers
    """
    while True:
        pin = "".join(str(random.randint(1, 9)) for _ in range(4))
        if not any(u["pin"] == pin for u in customers_data):
            return pin


def validate_amount_input(prompt) -> int:
    """
    this function takes the user input and checks if it is an actually number
    and that the number is also not negative
    :param prompt: user input
    :return: float number
    """
    while True:
        amount = input(prompt)
        if amount.isnumeric():
            if int(amount) > 0:
                return int(amount)
            else:
                print("Amount must be greater than 0")
        else:
            print("Invalid amount: (amount cannot be negative/empty)")


def find_receiver() -> dict:
    """
    this function searches for a user in our user's list. If the user exist, it returns
    the user otherwise it prints user not found
    :return: a user dictionary
    """
    receiver_info = {}

    while True:
        receiver_account_number = input("Enter receiver's account number: ")

        if receiver_account_number.isnumeric():
            if len(receiver_account_number) == 10:
                receiver_info["account_number"] = receiver_account_number
                break
        print("Invalid account number")
        print()

    for user_ in users:
        if receiver_info["account_number"] == user_["account_number"]:
            return user_
    print("account not found")


def find_user() -> dict:
    """
    this function searches for a user in our user's list. If the user exist, it returns
    the user otherwise it prints user not found
    :return: a user dictionary
    """
    data = {}

    while True:
        pin = input("Enter your PIN: ")
        account_number = input("Enter your account number: ")

        if pin.isnumeric() and account_number.isnumeric():
            if len(pin) == 4 and len(account_number) == 10:
                data["pin"] = pin
                data["account_number"] = account_number
                break
        print("Invalid PIN or account number")
        print()

    for user in users:
        if (data["pin"] == user["pin"]) and (data["account_number"] == user["account_number"]):
            return user
    print("user not found")
