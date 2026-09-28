import json
import os

FILE = "accounts.json"


def load_accounts():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)

    return []


def save_accounts(accounts):
    with open(FILE, "w") as file:
        json.dump(accounts, file, indent=4)


def create_account(accounts):
    account = input("Enter account number: ")
    name = input("Enter account holder name: ")

    for acc in accounts:
        if acc["account"] == account:
            print("Account already exists.")
            return

    new_account = {
        "account": account,
        "name": name,
        "balance": 0,
        "transactions": []
    }

    accounts.append(new_account)
    save_accounts(accounts)

    print("Account created successfully!")


def find_account(accounts, number):
    for account in accounts:
        if account["account"] == number:
            return account

    return None


def deposit(accounts):
    number = input("Enter account number: ")
    account = find_account(accounts, number)

    if account is None:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
            return

        account["balance"] += amount

        account["transactions"].append(
            f"Deposited ₹{amount:.2f}"
        )

        save_accounts(accounts)

        print("Amount deposited successfully!")

    except ValueError:
        print("Enter a valid amount.")


def withdraw(accounts):
    number = input("Enter account number: ")
    account = find_account(accounts, number)

    if account is None:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Enter a valid amount.")
            return

        if amount > account["balance"]:
            print("Insufficient balance.")
            return

        account["balance"] -= amount

        account["transactions"].append(
            f"Withdrawn ₹{amount:.2f}"
        )

        save_accounts(accounts)

        print("Amount withdrawn successfully!")

    except ValueError:
        print("Enter a valid amount.")


def check_balance(accounts):
    number = input("Enter account number: ")
    account = find_account(accounts, number)

    if account is None:
        print("Account not found.")
        return

    print(f"Account Holder: {account['name']}")
    print(f"Balance: ₹{account['balance']:.2f}")


def transaction_history(accounts):
    number = input("Enter account number: ")
    account = find_account(accounts, number)

    if account is None:
        print("Account not found.")
        return

    print("\n===== TRANSACTION HISTORY =====")

    if not account["transactions"]:
        print("No transactions found.")
        return

    for transaction in account["transactions"]:
        print(transaction)


def main():
    accounts = load_accounts()

    while True:
        print("\n========== BANK MANAGEMENT SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            deposit(accounts)

        elif choice == "3":
            withdraw(accounts)

        elif choice == "4":
            check_balance(accounts)

        elif choice == "5":
            transaction_history(accounts)

        elif choice == "6":
            print("Thank you for using Bank Management System!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()