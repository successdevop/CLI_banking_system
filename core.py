from datetime import datetime
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
    msg = (f"Thank you for creating an account with us {name.capitalize()}. Your "
           f"account number is {customer['account_number']}")
    log_data(msg, LOG_MSG)
    print(msg)


def deposit(customers_data: list):
    """
    this function takes the user amount and adds it to the user available balance
    after validating all user inputs
    :param customers_data: customer's database
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


def withdraw(customers_data: list):
    """
    this function takes the user amount and subtracts it from the user available balance
    after validating all user inputs
    :param customers_data: customer's database
    :return: None
    """
    user = authenticate(customers_data)
    if not user:
        return

    amount = validate_amount_input("Enter withdrawal amount: ")
    if user["balance"] > amount:
        user["balance"] -= amount
        user["transactions"].append({
            "type": "withdrawal",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })

        save_data(customers_data, DATA_FILE)
        msg = f"{user['name'].capitalize()}, you made a withdrawal of #{amount}. Current balance: #{user['balance']}"
        log_data(msg, LOG_MSG)
        print(msg)
    else:
        print("Insufficient balance")


def transfer(customers_data: list):
    """
    this function transfers money from one user"s account to another user"s account using
    the account number for validation. And it also prevents user from transferring money
    to self
    :param customers_data: customer's database
    :return: None
    """

    customer = authenticate(customers_data)
    if not customer:
        return

    receiver_acct = find_user(customers_data)
    if not receiver_acct:
        return

    if customer == receiver_acct:
        print("You can't transfer to self")
        return

    amount = validate_amount_input("Enter transfer amount: ")
    if customer["balance"] > amount:
        customer["balance"] -= amount
        receiver_acct["balance"] += amount

        customer["transactions"].append(
            {
                "type": "transfer",
                "amount": amount,
                "timestamp": datetime.now().isoformat()
            }
        )

        receiver_acct["transactions"].append(
            {
                "type": "deposit",
                "amount": amount,
                "timestamp": datetime.now().isoformat()
            }
        )

        save_data(customers_data, DATA_FILE)
        msg = (f"{customer['name'].capitalize()}, made a transfer of #{amount} to {receiver_acct['name']}. "
               f"Current balance: #{customer['balance']}")
        log_data(msg, LOG_MSG)
        print(msg)
    else:
        print("Insufficient balance")


def check_balance(customers_data: list):
    """
    this function prints a user's balance
    :param customers_data: customer's database
    :return: None
    """
    customer = authenticate(customers_data)
    if not customer:
        return

    print(f"Balance: #{customer["balance"]}")


def transaction_history(customers_data: list):
    """
    this function loops through a user's transaction list and displays the transaction history
    :param customers_data: customer's database
    :return: None
    """
    customer = authenticate(customers_data)
    if not customer:
        return

    for t in customer["transactions"]:
        print(f"{t['timestamp'].split('T')[0]} {f'{t["type"]} Out' if t['type'] == 'transfer' else t['type']}: #{t['amount']}")


def analytics(customers_data: list):
    """
    this function show bank statistics
    """
    total_money_in_the_bank = sum(c["balance"] for c in customers_data)

    richest_customer = max(customers_data, key=lambda x: x.get("balance") or 0, default=None)

    oldest_acct = min(customers_data, key=lambda x: x.get("created_at") or 0)

    highest_transaction = max(customers_data, key=lambda x: len(x.get("transactions")) or 0)

    print(f"""
    ========= Bank Statistics 2026 =========
    Total money in the bank:    {total_money_in_the_bank}
    Richest bank customer:      {richest_customer['name']} (#{richest_customer['balance']})
    Oldest account holder:      Account number: {oldest_acct['account_number']} - Date created: 
                                    {oldest_acct['created_at']} - Account holder: {oldest_acct['name']}
    Account with highest transactions: Account holder: {highest_transaction['name']} - Transactions: 
                                            {highest_transaction['transactions']}
    """)


def top_3_richest_account(customers_data: list):
    """
    this account sorts through the user's list and prints the top 3 richest account
    :param customers_data: customer's database
    :return: None
    """
    top_account = sorted(customers_data, key=lambda x: x.get('balance') or 0, reverse=True)[:3]

    for top_3 in top_account:
        print(f"Name: {top_3['name']} - Balance: #{top_3['balance']}")
