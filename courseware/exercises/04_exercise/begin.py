class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        if not (isinstance(account_number, str) and len(account_number) == 10):
            raise ValueError("Invalid account number.")
        if not (isinstance(balance, (int, float)) and balance >= 0):
            raise ValueError("Invalid balance.")
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("Invalid deposit amount.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if not (isinstance(amount, (int, float)) and 0 < amount <= self.balance):
            raise ValueError("Invalid withdrawal amount.")
        self.balance -= amount


def main() -> None:
    account = BankAccount("1234567890", 1000)
    account.deposit(500)
    # account.deposit(-500)
    account.withdraw(200)
    # account.withdraw(-200)
    print(account.balance)
    

if __name__ == "__main__":
    main()