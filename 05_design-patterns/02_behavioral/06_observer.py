# Observer Pattern
#
# A one-to-many dependency between objects so that when one object changes
# state, all its dependents are notified and updated automatically.

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class ConcreteObserver(Observer):
    def update(self, message: str) -> None:
        print(f"Observer received message: {message}")


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


# Client code
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify(
    "This is a message!"
)  # Output: Observer received message: This is a message!
