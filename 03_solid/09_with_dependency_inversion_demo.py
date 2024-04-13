from typing import Protocol

#  (Biz Logic)      (Dividing Line)   (Data Layer)
# Notification -> NotifierService <- EmailNotifier
#                   ^   ^
#                   |    \ PhoneNotifier
#                   |
#                SMSNotifier


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

    def __init__(self, notifier: NotifierService) -> None:
        self.notifier = notifier

    def send(self, message: str) -> None:
        self.notifier.notify(message)


notification = Notification(EmailNotifier())
notification.send("This is an email notification.")
