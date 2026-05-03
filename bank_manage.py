import json
import os

DATA_FILE = "accounts.json"


# Load existing data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Create account
def create_account(data):
    name = input("Enter your name: ")
    acc_no = input("Create account number: ")

    if acc_no in data:
        print("Account already exists!")
        return

    data[acc_no] = {
        "name": name,
        "balance": 0
    }

    save_data(data)
    print("Account created successfully!")


# Deposit money
def deposit(data):
    acc_no = input("Enter account number: ")

    if acc_no not in data:
        print("Account not found!")
        return

    amount = float(input("Enter amount: "))
    data[acc_no]["balance"] += amount

    save_data(data)
    print("Money deposited successfully!")


# Withdraw money
def withdraw(data):
    acc_no = input("Enter account number: ")

    if acc_no not in data:
        print("Account not found!")
        return

    amount = float(input("Enter amount: "))

    if amount > data[acc_no]["balance"]:
        print("Insufficient balance!")
    else:
        data[acc_no]["balance"] -= amount
        save_data(data)
        print("Money withdrawn successfully!")


# Check balance
def check_balance(data):
    acc_no = input("Enter account number: ")

    if acc_no not in data:
        print("Account not found!")
        return

    print(f"Name: {data[acc_no]['name']}")
    print(f"Balance: ₹{data[acc_no]['balance']}")


# Main menu
def main():
    data = load_data()

    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(data)
        elif choice == "2":
            deposit(data)
        elif choice == "3":
            withdraw(data)
        elif choice == "4":
            check_balance(data)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
