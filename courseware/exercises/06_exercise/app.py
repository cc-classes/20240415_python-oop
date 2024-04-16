from abc import ABC


class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount


class SavingsAccount(BankAccount):
    def __init__(
        self, account_number: str, balance: float, interest_rate: float
    ):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")


class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)

    def transfer(self, amount: float, account: BankAccount) -> None:
        self.balance -= amount
        account.deposit(amount)


class CheckingAccount2(BankAccount):
    def __init__(self, account_number: str, balance: float):
        super().__init__(account_number, balance)


def perform_withdrawal(account: SavingsAccount, amount: float) -> None:
    account.withdraw(amount)
    print(
        f"Withdrawn {amount} from account {account.account_number}. New balance: {account.balance}"
    )


def main() -> None:
    # Create objects and test the functionality
    savings_account = SavingsAccount("1234567890", 1000.0, 0.05)
    checking_account = CheckingAccount("9876543210", 500.0)

    perform_withdrawal(savings_account, 200.0)
    # Raises NotImplementedError, is this the expected behavior?
    # perform_withdrawal(checking_account, 100.0)


if __name__ == "__main__":
    main()
