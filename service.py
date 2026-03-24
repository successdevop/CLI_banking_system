import random

users = []


def generate_account_number() -> str:
    numbers = []
    while len(numbers) < 10:
        numbers.append(random.randint(1, 9))

    return "".join(str(num) for num in numbers)


def validate_name(prompt):
    while True:
        name = input(prompt).strip()
        if name and len(name) >= 3:
            return name
        print("Name cannot be empty and must be at-least 3 characters")


def generate_pin() -> str:
    pin = []
    while len(pin) < 4:
        pin.append(random.randint(1, 9))

    return "".join(str(num) for num in pin)


def create_account():
    name = validate_name("Please enter your name: ")
    account_number = generate_account_number()
    pin = generate_pin()

    data = {"name": name, "account_number": account_number, "balance": 0, "pin": pin, "transactions": []}
    users.append(data)


create_account()
print(users)