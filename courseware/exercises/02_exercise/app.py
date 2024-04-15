# # Function Overriding
# # Function Overloading


# class A:
#     def display(self) -> None:
#         print("A")


# class B(A):
#     # display override the display method in class A
#     def display(self) -> None:
#         print("B")

#     def cool_a(self, name: str) -> None:
#         print(f"B {name}")

#     # overloading in the traditional sense is not possible in Python
#     def cool_b(self, name: str, message: str) -> None:
#         print(f"B {name} {message}")

#     # manual way of overloading by writing your own to interogate the arguments,
#     # then choose one method implementation over another
#     def cool(self, *args: str) -> None:
#         if len(args) == 1:
#             self.cool_a(args[0])
#         elif len(args) == 2:
#             self.cool_b(args[0], args[1])


# b = B()
# b.display()
# b.cool("a", "b")


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

    def display_balance(self) -> None:
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        # if amount < 0.01:
        #     raise ValueError("Amount is invalid, must be a penny or more.")
        # if amount > self.balance:
        #     raise ValueError("Insufficient funds.")
        # self.balance -= amount
        self.balance *= 1.02


class CheckingAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount < 0.01:
            raise ValueError("Amount is invalid, must be a penny or more.")
        total_amount = amount + 1
        if total_amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= total_amount


def perform_transactions(account: BankAccount) -> None:
    account.deposit(1000)
    account.withdraw(500)
    account.display_balance()


def main() -> None:
    accounts: list[BankAccount] = [
        SavingsAccount("SA001wwwwwwwwwwwwwwww", 1000),
        CheckingAccount("CA001wwwwwwwwwwwwwwww", 1000),
        BankAccount("BA001wwwwwwwwwwwwwwww", 1000),
    ]

    for account in accounts:
        print(f"Performing transactions for {type(account).__name__}:")
        perform_transactions(account)
        print()


if __name__ == "__main__":
    main()
