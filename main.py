from core import *
from utils import find_user, display_options_menu
from storage import load_data


def main():
    bank_data = load_data(DATA_FILE)

    # if not bank_data:
    #     print("No data")
    #     return

    while True:
        display_options_menu()

        choice = input("> ")

        if choice == "1":
            create_account(bank_data)
        elif choice == "2":
            deposit(bank_data)
        elif choice == "3":
            withdraw(bank_data)
        elif choice == "4":
            transfer(bank_data)
        elif choice == "5":
            check_balance(bank_data)
        elif choice == "6":
            transaction_history(bank_data)
        elif choice == "7":
            analytics(bank_data)
        elif choice == "8":
            top_3_richest_account(bank_data)
        elif choice == "9":
            find_user(bank_data)
        elif choice == "0":
            break
        else:
            print("Invalid number")
        print()


main()
