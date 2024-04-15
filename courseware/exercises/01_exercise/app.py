class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        # Initialize account_number and balance attributes
        self.account_number = account_number
        self.balance = balance

    # Define getter and setter methods for account_number and balance
    @property
    def account_number(self) -> str:
        return self.__account_number.upper()

    @account_number.setter
    def account_number(self, account_number: str) -> None:
        if len(account_number) < 10:
            raise ValueError(
                "Account number must be at least 10 characters long."
            )
        self.__account_number = account_number

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float) -> None:
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount


def main() -> None:
    bank_account = BankAccount("a2rT412DF1234", -1)
    print(bank_account.account_number)
    print(bank_account.balance)
    bank_account.deposit(50.0)
    print(bank_account.balance)
    bank_account.withdraw(25.0)
    print(bank_account.balance)


if __name__ == "__main__":
    main()
