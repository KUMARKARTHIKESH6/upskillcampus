# ============================================================
#  Banking Information System
#  Run with:  python BankingInformationSystem.py
# ============================================================

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("  [ERROR] Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"  [SUCCESS] Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("  [ERROR] Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(f"  [ERROR] Insufficient balance. Current balance: Rs. {self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"  [SUCCESS] Rs. {amount:.2f} withdrawn successfully.")

    def display(self):
        print("  ----------------------------------------")
        print(f"  Account Holder : {self.account_holder}")
        print(f"  Account Number : {self.account_number}")
        print(f"  Current Balance: Rs. {self.balance:.2f}")
        print("  ----------------------------------------")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  [ERROR] Invalid input. Please enter a numeric value.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  [ERROR] Invalid input. Please enter a whole number.")


def main():
    print("========================================")
    print("     WELCOME TO BANKING INFO SYSTEM     ")
    print("========================================")

    # Get account holder name
    while True:
        name = input("Enter Account Holder Name  : ").strip()
        if name:
            break
        print("  [ERROR] Name cannot be empty.")

    # Get account number
    while True:
        acc_number = get_int("Enter Account Number (int)  : ")
        if acc_number > 0:
            break
        print("  [ERROR] Account number must be a positive integer.")

    # Get initial balance
    while True:
        initial_balance = get_float("Enter Initial Balance (Rs.)  : ")
        if initial_balance >= 0:
            break
        print("  [ERROR] Initial balance cannot be negative.")

    # Create account
    account = BankAccount(name, acc_number, initial_balance)
    print("\n  Account created successfully!")
    account.display()

    # Menu loop
    while True:
        print("\n========================================")
        print("              MAIN MENU                 ")
        print("========================================")
        print("  1. Deposit")
        print("  2. Withdraw")
        print("  3. Check Balance")
        print("  4. Exit")
        print("----------------------------------------")

        choice = get_int("  Enter your choice (1-4): ")

        if choice == 1:
            amount = get_float("\n  Enter deposit amount (Rs.): ")
            account.deposit(amount)

        elif choice == 2:
            amount = get_float("\n  Enter withdrawal amount (Rs.): ")
            account.withdraw(amount)

        elif choice == 3:
            print("\n  --- Account Details ---")
            account.display()

        elif choice == 4:
            print("\n========================================")
            print("  Thank you for using Banking Info System")
            print(f"  Goodbye, {account.account_holder}!")
            print("========================================")
            break

        else:
            print("  [ERROR] Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
