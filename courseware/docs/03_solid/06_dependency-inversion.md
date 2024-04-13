# Object-Oriented Python Programming Course

## Dependency Inversion Principle

The Dependency Inversion Principle (DIP) is the last of the SOLID principles and it promotes the decoupling of high-level modules (which contain the core functionality of your application) from low-level modules (which handle details such as database access, user interfaces, and other non-core functionality). 

According to the DIP:
- High-level modules should not depend on low-level modules, both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.

This principle allows for decoupling, making the system more modular, flexible, and adaptable to changes.

## Why Use DIP?

- To decouple your code to make it more reusable, maintainable, and testable.
- To make the system easier to modify and extend without affecting existing code.
- To improve code architecture by separating the high-level and low-level modules.

## DIP Example

Consider a simple notification system that notifies a user by email.

### Without Applying DIP:

```python
class EmailNotifier:
    def notify(self, message):
        # send an email notification
        print(f"Email sent with message: '{message}'")


class Notification:
    def __init__(self):
        self.notifier = EmailNotifier()

    def send(self, message):
        self.notifier.notify(message)


notification = Notification()
notification.send("This is an email notification.")
```

In this code, the `Notification` class is tightly coupled with `EmailNotifier`, which is a low-level module in the system.

### Applying DIP:

To apply the Dependency Inversion Principle, we can create an abstract base class for the notifier and pass the notifier as a parameter to the `Notification` class.

```python
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class EmailNotifier(Notifier):
    def notify(self, message):
        print(f"Email sent with message: '{message}'")


class SMSNotifier(Notifier):
    def notify(self, message):
        print(f"SMS sent with message: '{message}'")


class Notification:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send(self, message):
        self.notifier.notify(message)


email_notification = Notification(EmailNotifier())
email_notification.send("This is an email notification.")  # Output: Email sent with message: 'This is an email notification.'

sms_notification = Notification(SMSNotifier())
sms_notification.send("This is an SMS notification.")  # Output: SMS sent with message: 'This is an SMS notification.'
```

In this refactored code:

- `Notifier` is an abstract base class that defines the `notify` method.
- `EmailNotifier` and `SMSNotifier` are concrete classes that implement the `notify` method.
- The `Notification` class takes a `notifier` as a parameter and calls the `notify` method on it.

Now, the `Notification` class is decoupled from the specific notification mechanism (`EmailNotifier`). You can easily add new notification methods (like `SMSNotifier`) without modifying the `Notification` class, adhering to the Dependency Inversion Principle.