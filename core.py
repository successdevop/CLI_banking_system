from datetime import datetime
from storage import load_data, save_data, log_data
from config import LOG_MSG, DATA_FILE
from utils import *


def create_account(customer_data: list):
    """
    this function creates an account for users and store the information
    in our customer's list
    :param customer_data: customer's database
    """
    customer_id = generate_id(customer_data)
    name = validate_name("Please enter your name: ")
    account_number = generate_secret_keys(customer_data, 10)
    pin = generate_secret_keys(customer_data, 4)

    customer = {"id": customer_id, "name": name, "account_number": account_number, "pin": pin, "balance": 0,
                "transactions": [], "created_at": datetime.now().isoformat(), "user_locked": False}

    customer_data.append(customer)
    save_data(customer_data, DATA_FILE)
    print(f"Thank you for creating an account with us {name.capitalize()}\nYour "
          f"account number is {customer['account_number']}")


def deposit(customers_data: list):
    """
    this function takes the user amount and adds it to the user available balance
    after validating all user inputs
    :return: None
    """
    user = authenticate(customers_data)
    if not user:
        return

    amount = validate_amount_input("Enter deposit amount: ")
    user["balance"] += amount
    user["transactions"].append(
        {
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        }
    )

    save_data(customers_data, DATA_FILE)
    msg = f"{user['name']} deposited {amount} to your account. Current balance: #{user['balance']}"
    log_data(msg, LOG_MSG)
    print(msg)


def withdraw():
    """
    this function takes the user amount and subtracts it from the user available balance
    after validating all user inputs
    :return: None
    """
    if len(users) == 0:
        return

    user = find_user()
    if not user:
        return

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
    receiver_user = find_receiver()

    if not user and not receiver_user:
        return

    amount = validate_amount_input("Enter transfer amount: ")
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
    if not user:
        return

    print(f"Balance: #{user["balance"]}")


def transaction_history():
    """
    this function loops through a user's transaction list and displays the transaction history
    :return: None
    """
    user = find_user()
    if not user:
        return

    for t_detail, t_amount in user["transactions"]:
        print(f"{t_detail.capitalize()}: {t_amount}")


def top_3_richest_account():
    """
    this account sorts through the user's list and prints the top 3 richest account
    :return: None
    """
    top_account = sorted(users, key=itemgetter("balance"), reverse=True)[:3]

    for top_3 in top_account:
        print(f"Name: {top_3["name"]} - Balance: #{top_3['balance']}")


