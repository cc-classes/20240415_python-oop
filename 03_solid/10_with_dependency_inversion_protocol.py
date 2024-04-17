from typing import Protocol


class Notifier(Protocol):
    def notify(self, message: str) -> None:
        pass


class EmailNotifier:
    def notify(self, message: str) -> None:
        print(f"Email sent with message: '{message}'")


class SMSNotifier:
    def notify(self, message: str) -> None:
        print(f"SMS sent with message: '{message}'")


# static typing - type hints determine type at programming time
# vs
# duck-typing - type is resolve at runtime


class Notification:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message: str) -> None:
        self.notifier.notify(message)


email_notification = Notification(EmailNotifier())
# Output: Email sent with message: 'This is an email notification.'
email_notification.send("This is an email notification.")

sms_notification = Notification(SMSNotifier())
# Output: SMS sent with message: 'This is an SMS notification.'
sms_notification.send("This is an SMS notification.")


class PhoneNotifier:
    def notify(self, message: str) -> None:
        print(f"Phone sent with message: '{message}'")


phone_notification = Notification(PhoneNotifier())
# Output: Phone sent with message: 'This is an Phone notification.'
phone_notification.send("This is an Phone notification.")
