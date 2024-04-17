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


# low-level application specific detail
# dependency injection we connect a token to some low-level concrete implementation
def injector(service_token: str) -> Notifier:
    if service_token == "email":
        return EmailNotifier()
    elif service_token == "phone":
        return PhoneNotifier()
    else:
        return SMSNotifier()


# import os

# service_token = os.environ["NOTIFICATION_SERVICE"]
# if service_token == "email":
#     notification_service = EmailNotifier()
# elif service_token == "phone":
#     notification_service = PhoneNotifier()
# else:
#     notification_service = SMSNotifier()

phone_notification = Notification(injector("phone"))
# Output: Phone sent with message: 'This is an Phone notification.'
phone_notification.send("This is an Phone notification.")
