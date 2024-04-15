from __future__ import annotations
from abc import ABC, abstractmethod


class CustomerIterator:
    def __init__(self, accounts: list[BankAccount]) -> None:
        self.__accounts = accounts
        self.__current_index = -1

    def __next__(self) -> BankAccount:
        self.__current_index += 1
        if self.__current_index >= len(self.__accounts):
            raise StopIteration()
        else:
            return self.__accounts[self.__current_index]


class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.__accounts: list[BankAccount] = []

    def add_account(self, account: BankAccount) -> None:
        self.__accounts.append(account)

    def display_info(self) -> None:
        print(f"{self.name} ({self.email})")

    def __iter__(self) -> CustomerIterator:
        return CustomerIterator(self.__accounts)


class BankAccount(ABC):
    def __init__(
        self, account_number: str, balance: float, customer: Customer
    ) -> None:
        # Initialize account_number and balance attributes
        self.account_number = account_number
        self.balance = balance
        # The Bank Account "has a" Customer - "has-a" composition relationship
        self.customer: Customer = customer

        # calling add_account is causing a change in another class
        # this changing of the state of something else is called
        # a side effect
        # self.customer.add_account(self)

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

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        print("In BankAccount withdraw method")

    def display_balance(self) -> None:
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


# Savings Account "is a" Bank Account - "is-a" relationship means inheritance
class SavingsAccount(BankAccount):
    def __init__(
        self,
        account_number: str,
        balance: float,
        interest_rate: float,
        customer: Customer,
    ) -> None:
        super().__init__(account_number, balance, customer)
        self.__interest_rate = interest_rate

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.balance *= self.__interest_rate


class CheckingAccount(BankAccount):
    def __init__(
        self,
        account_number: str,
        balance: float,
        withdrawal_fee: float,
        customer: Customer,
    ) -> None:
        super().__init__(account_number, balance, customer)
        self.__withdrawal_fee = withdrawal_fee

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.balance -= self.__withdrawal_fee


def main() -> None:
    customer = Customer("John Doe", "john.doe@johndoe.com")
    savings_account = SavingsAccount("1234567890", 1000.0, 1.05, customer)
    checking_account = CheckingAccount("0987654321", 500.0, 2.0, customer)

    customer.add_account(savings_account)
    customer.add_account(checking_account)

    customer.display_info()
    for account in customer:
        account.display_balance()
        account.deposit(100.0)
        account.display_balance()
        account.withdraw(50.0)
        account.display_balance()


if __name__ == "__main__":
    main()
