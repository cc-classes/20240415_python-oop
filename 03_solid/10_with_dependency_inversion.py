from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"Email sent with message: '{message}'")


class SMSNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"SMS sent with message: '{message}'")


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
