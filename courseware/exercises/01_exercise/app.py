class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        # Initialize account_number and balance attributes
        self._account_number = account_number
        self._balance = balance

    # Define getter and setter methods for account_number and balance
    @property
    def account_number(self) -> str:
        return self._account_number.upper()

    @account_number.setter
    def account_number(self, account_number: str) -> None:
        if len(account_number) < 10:
            raise ValueError(
                "Account number must be at least 10 characters long."
            )
        self._account_number = account_number

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


def main() -> None:
    bank_account = BankAccount("a2rT412", 100.0)
    print(bank_account.account_number)
    print(bank_account.balance)
    bank_account.deposit(50.0)
    print(bank_account.balance)
    bank_account.withdraw(25.0)
    print(bank_account.balance)


if __name__ == "__main__":
    main()
