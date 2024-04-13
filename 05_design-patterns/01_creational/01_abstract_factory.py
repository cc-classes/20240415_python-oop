# Abstract Factory Pattern
#
# Family of related or dependent objects is created without specifying
# their concrete classes.

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


class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str:
        pass


class WindowsCheckbox(Checkbox):
    def check(self) -> str:
        return "Windows Checkbox Checked!"


class MacOSCheckbox(Checkbox):
    def check(self) -> str:
        return "MacOS Checkbox Checked!"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


# Client code
factory = WindowsFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()
print(button.click())  # Output: Windows Button Clicked!
print(checkbox.check())  # Output: Windows Checkbox Checked!
