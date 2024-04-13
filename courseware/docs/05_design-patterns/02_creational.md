# Object-Oriented Python Programming Course

## Creational Design Patterns

Let’s take a closer look at each of the Creational Design Patterns with Python code examples.

### 1. **Singleton Pattern**

The Singleton Pattern restricts a class from instantiating multiple objects. It's useful when one object controls access to a resource, such as a configuration manager or a connection pool.

#### Example:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Client code
singleton1 = Singleton()
singleton2 = Singleton()
assert singleton1 == singleton2  # They are the same object
```

### 2. **Factory Method Pattern**

The Factory Method Pattern provides an interface for creating objects in a super class but allows subclasses to alter the type of created objects.

#### Example:

```python
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked!"


class MacOSButton(Button):
    def click(self):
        return "MacOS Button Clicked!"


class ButtonFactory:
    def create_button(self, type):
        if type == 'Windows':
            return WindowsButton()
        elif type == 'MacOS':
            return MacOSButton()
        else:
            raise ValueError("Invalid type.")


# Client code
factory = ButtonFactory()
button = factory.create_button('Windows')
print(button.click())  # Output: Windows Button Clicked!
```

### 3. **Abstract Factory Pattern**

The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes.

#### Example:

```python
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked!"


class MacOSButton(Button):
    def click(self):
        return "MacOS Button Clicked!"


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox Checked!"


class MacOSCheckbox(Checkbox):
    def check(self):
        return "MacOS Checkbox Checked!"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()


# Client code
factory = WindowsFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()
print(button.click())  # Output: Windows Button Clicked!
print(checkbox.check())  # Output: Windows Checkbox Checked!
```

### 4. **Builder Pattern**

The Builder Pattern separates the construction of a complex object from its representation, enabling the same construction process to create different representations.

#### Example:

```python
class Computer:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def describe(self):
        return ", ".join(self.parts)


class ComputerBuilder:
    def build(self):
        raise NotImplementedError


class MyComputerBuilder(ComputerBuilder):
    def build(self):
        computer = Computer()
        computer.add('Case')
        computer.add('Motherboard')
        computer.add('CPU')
        computer.add('Memory')
        computer.add('Power Supply')
        return computer


# Client code
builder = MyComputerBuilder()
computer = builder.build()
print(computer.describe())  # Output: Case, Motherboard, CPU, Memory, Power Supply
```

### 5. **Prototype Pattern**

The Prototype Pattern is used to instantiate a new object by copying all of the properties of an existing object, creating an independent clone.

#### Example:

```python
import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"Car model: {self.model}, color: {self.color}"


# Client code
original_car = Car('Model S', 'Red')
cloned_car = original_car.clone()
cloned_car.color = 'Blue'

print(original_car)  # Output: Car model: Model S, color: Red
print(cloned_car)  # Output: Car model: Model S, color: Blue
```

This is a brief overview and example of each creational design pattern in Python. Each pattern has its own use cases and it’s important to know when to use each one in a software design scenario.
