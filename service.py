import random
from operator import itemgetter

users = [{
    "name": "John",
    "account_number": "1234567890",
    "balance": 5000,
    "pin": "4444",
    "transactions": [
        ("deposit", 2000),
        ("withdraw", 1000),
        ("transfer", 4000)
    ]
},
    {
        "name": "faith",
        "account_number": "1238750642",
        "balance": 2000,
        "pin": "0415",
        "transactions": [
            ("deposit", 2000),
            ("withdraw", 1000),
        ]
    },
    {
        "name": "adam",
        "account_number": "5672890153",
        "balance": 7900,
        "pin": "0915",
        "transactions": [
            ("deposit", 2000),
            ("withdraw", 1000),
            ("deposit", 1000),
            ("withdraw", 3500),
        ]
    }
]


def generate_account_number() -> str:
    """
    this function generates account number for users. It uses the while loop to generate
    10 random numbers stored in a list, which makes the customer unique account number
    :return: a string of 10 random numbers
    """
    numbers = []
    while len(numbers) < 10:
        numbers.append(random.randint(1, 9))

    return "".join(str(num) for num in numbers)


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


def generate_pin() -> str:
    """
    this function generates pin for users. It uses the while loop to generate
    4 random numbers stored in a list, which makes the customer unique pin
    :return: a string of 4 random numbers
    """
    pin = []
    while len(pin) < 4:
        pin.append(random.randint(1, 9))

    return "".join(str(num) for num in pin)


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
            receiver_info = user_
            return receiver_info
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
            data = user
            return data
    print("user not found")


def create_account():
    """
    this function creates an account for users and store the information
    in our user's list
    """
    name = validate_name("Please enter your name: ")
    account_number = generate_account_number()
    pin = generate_pin()

    data = {"name": name, "account_number": account_number, "balance": 0, "pin": pin, "transactions": []}
    users.append(data)


def deposit():
    """
    this function takes the user amount and adds it to the user available balance
    after validating all user inputs
    :return: None
    """
    if len(users) == 0:
        return

    user = find_user()
    amount = validate_amount_input("Enter deposit amount: ")
    user["balance"] += amount
    user["transactions"].append(("deposit", amount))


def withdraw():
    """
    this function takes the user amount and subtracts it from the user available balance
    after validating all user inputs
    :return: None
    """
    if len(users) == 0:
        return

    user = find_user()
    amount = validate_amount_input("Enter withdrawal amount: ")
    if user["balance"] < amount:
        print("Insufficient balance")
    else:
        user["balance"] -= amount
        user["transactions"].append(("withdraw", amount))


def transfer():
    """
    this function transfers money from one user"s account to another user"s account using
    the account number for validation
    :return: None
    """
    if len(users) == 0:
        return

    user = find_user()
    amount = validate_amount_input("Enter transfer amount: ")
    receiver_user = find_receiver()
    if user["balance"] < amount:
        print("Insufficient balance")
    else:
        user["balance"] -= amount
        receiver_user["balance"] += amount
        user["transactions"].append(("transfer", amount))
        receiver_user["transactions"].append(("deposit", amount))


def check_balance():
    """
    this function prints a user's balance
    :return: None
    """
    user = find_user()
    print(f"Balance: #{user["balance"]}")


def transaction_history():
    """
    this function loops through a user's transaction list and displays the transaction history
    :return: None
    """
    user = find_user()
    for t_detail, t_amount in user["transactions"]:
        print(f"{t_detail.capitalize()}: {t_amount}")


def top_3_richest_account():
    """
    this account sorts through the user's list and prints the top 3 richest account
    :return: None
    """
    users.sort(key=itemgetter("balance"))
    top_3_accounts = users[-3:]

    for top_3 in reversed(top_3_accounts):
        print(f"Name: {top_3["name"]} - Balance: #{top_3["balance"]}")

