class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")


def calculate_interest(account, account_type):
    if account_type == "savings":
        interest_rate = 0.05
        interest = account.balance * interest_rate
    elif account_type == "checking":
        interest_rate = 0.02
        interest = account.balance * interest_rate
    else:
        raise ValueError("Invalid account type.")
    
    return interest


def main() -> None:
    savings_account = BankAccount("1234567890", 1000)
    checking_account = BankAccount("9876543210", 500)

    savings_interest = calculate_interest(savings_account, "savings")
    checking_interest = calculate_interest(checking_account, "checking")

    print(f"Savings account interest: {savings_interest}")
    print(f"Checking account interest: {checking_interest}")

    
if __name__ == "__main__":
    main()