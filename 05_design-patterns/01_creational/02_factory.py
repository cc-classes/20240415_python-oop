# Factory Method Pattern
#
# Define an interface for creating an object, but allow subclasses to alter
# the type of objects that will be created.

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self) -> str:
        pass


class WindowsButton(Button):
    def click(self) -> str:
        return "Windows Button Clicked!"


class MacOSButton(Button):
    def click(self) -> str:
        return "MacOS Button Clicked!"


class ButtonFactory:
    def create_button(self, type: str) -> Button:
        if type == "Windows":
            return WindowsButton()
        elif type == "MacOS":
            return MacOSButton()
        else:
            raise ValueError("Invalid type.")


# Client code
factory = ButtonFactory()
button = factory.create_button("Windows")
print(button.click())  # Output: Windows Button Clicked!
