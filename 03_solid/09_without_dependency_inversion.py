from typing import Protocol

# Notification -> EmailNotifier
#    |   \
#    |    > PhoneNotifier
#    v
# SMSNotifier


class NotifierService(Protocol):
    def notify(self, message: str) -> None: ...


class EmailNotifier:
    def notify(self, message: str) -> None:
        # send an email notification
        print(f"Email sent with message: '{message}'")


class PhoneNotifier:
    def notify(self, message: str) -> None:
        # send an phone notification
        print(f"Phone sent with message: '{message}'")


class SMSNotifier:
    def notify(self, message: str) -> None:
        # send an sms notification
        print(f"SMS sent with message: '{message}'")


class Notification:
    notifier: NotifierService

    def __init__(self, notification_type: str) -> None:
        if notification_type == "email":
            self.notifier = EmailNotifier()
        elif notification_type == "phone":
            self.notifier = PhoneNotifier()
        else:
            self.notifier = SMSNotifier()

    def send(self, message: str) -> None:
        self.notifier.notify(message)


notification = Notification("email")
notification.send("This is an email notification.")
