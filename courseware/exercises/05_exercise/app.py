from abc import ABC, abstractmethod
from typing import Protocol


class IBankAccount(Protocol):
    balance: float
    account_number: str

    def deposit(self, amount: float) -> None:
        pass

    def withdraw(self, amount: float) -> None:
        pass

    def calculate_interest(self) -> float:
        pass


class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance.")

    @abstractmethod
    def calculate_interest(self) -> float:
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.05
        interest = self.balance * interest_rate
        return interest


class CheckingAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.02
        interest = self.balance * interest_rate
        return interest


class MoneyMarketAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.03
        interest = self.balance * interest_rate
        return interest


class CertificateDepositAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.06
        interest = self.balance * interest_rate
        return interest


def print_accounts(accounts: list[IBankAccount]) -> None:
    for account in accounts:
        print(f"Account number: {account.account_number}")
        print(f"Balance: {account.balance}")
        print(f"Interest: {account.calculate_interest()}")
        print()


def main() -> None:
    savings_account = SavingsAccount("1234567890", 1000)
    checking_account = CheckingAccount("9876543210", 500)
    money_market_account = MoneyMarketAccount("1357924680", 2000)
    certificate_deposit_account = CertificateDepositAccount("2468135790", 3000)

    accounts: list[IBankAccount] = [
        savings_account,
        checking_account,
        money_market_account,
        certificate_deposit_account,
    ]

    print_accounts(accounts)

    # savings_interest = calculate_interest(savings_account, "savings")
    # checking_interest = calculate_interest(checking_account, "checking")

    # print(f"Savings account interest: {savings_interest}")
    # print(f"Checking account interest: {checking_interest}")


if __name__ == "__main__":
    main()
