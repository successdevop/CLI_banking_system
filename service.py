import random

users = [{
        "name": "John",
        "account_number": "1234567890",
        "balance": 5000,
        "pin": "4444",
        "transactions": [
            ("deposit", 2000),
            ("withdraw", 1000)
        ]
    }]


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


def validate_amount_input(prompt) -> float:
    """
    this function takes the user input and checks if it is an actually number
    and that the number is also not negative
    :param prompt: user input
    :return: float number
    """
    amount = float(input(prompt))
    try:
        if amount > 0:
            return float(amount)
    except ValueError:
        print("Invalid amount: (amount cannot be negative/empty)")


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


print(users)