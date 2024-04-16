from __future__ import annotations
from typing import Protocol


class BankAccount:
    def __init__(
        self,
        account_number: str,
        balance: float,
        validator: IBankAccountValidator,
    ) -> None:
        self.__validator = validator
        if not self.__validator.validate_account_number(account_number):
            raise ValueError("Invalid account number.")
        if not self.__validator.validate_balance(balance):
            raise ValueError("Invalid balance.")
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if not self.__validator.validate_deposit(amount):
            raise ValueError("Invalid deposit amount.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if not self.__validator.validate_withdraw(amount, self.__balance):
            raise ValueError("Invalid withdrawal amount.")
        self.__balance -= amount


class IBankAccountValidator(Protocol):
    def validate_account_number(self, account_number: str) -> bool:
        ...

    def validate_balance(self, balance: float) -> bool:
        ...

    def validate_deposit(self, amount: float) -> bool:
        ...

    def validate_withdraw(self, amount: float, balance: float) -> bool:
        ...

class BankAccountValidator:
    def validate_account_number(self, account_number: str) -> bool:
        return isinstance(account_number, str) and len(account_number) == 10

    def validate_balance(self, balance: float) -> bool:
        return isinstance(balance, (int, float)) and balance >= 0

    def validate_deposit(self, amount: float) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

    def validate_withdraw(self, amount: float, balance: float) -> bool:
        return isinstance(amount, (int, float)) and 0 < amount <= balance


class OverdraftBankAccountValidator(BankAccountValidator):
    def validate_withdraw(self, amount: float, _: float) -> bool:
        return isinstance(amount, (int, float)) and 0 < amount


def main() -> None:
    validator = BankAccountValidator()
    account = BankAccount("1234567890", 1000, validator)
    account.deposit(500)
    # account.deposit(-500)
    account.withdraw(200)
    # account.withdraw(-200)
    print(account.balance)


if __name__ == "__main__":
    main()
