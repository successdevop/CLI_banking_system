from service import *


def main():
    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Balance")
        print("6. History")
        print("7. Top_3_account")
        print("0. Exit")

        choice = input("> ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            check_balance()
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            top_3_richest_account()
        elif choice == "0":
            break
        else:
            print("Invalid number")
        print(users)
        print()


main()
