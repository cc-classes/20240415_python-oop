from typing import Protocol


class Notification(Protocol):
    def send_notification(self, message: str) -> None: ...


class EmailNotification:
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")


class SMSNotification:
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")


class BankAccount:
    def __init__(
        self, account_number: str, balance: float, notification: Notification
    ):
        self.account_number = account_number
        self.balance = balance
        self.notification = notification

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.notification.send_notification(
            f"Deposit of {amount} made to account {self.account_number}"
        )

    def withdraw(self, amount: float) -> None:
        if self.balance >= amount:
            self.balance -= amount
            self.notification.send_notification(
                f"Withdrawal of {amount} made from account {self.account_number}"
            )
        else:
            raise ValueError("Insufficient balance.")


def main() -> None:
    account1 = BankAccount("1234567890", 1000.0, EmailNotification())
    account1.deposit(500.0)
    account1.withdraw(200.0)

    account2 = BankAccount("9876543210", 500.0, SMSNotification())
    account2.deposit(1000.0)
    account2.withdraw(800.0)


if __name__ == "__main__":
    main()
