# Object-Oriented Python Programming Course

## Type Hints Overview

Type hints are a feature of Python (introduced in PEP 484) that allow you to explicitly indicate the expected type of a variable, function parameter, or return value. While type hints are not enforced at runtime, they can be very useful for understanding the expected behavior of code, and are often used with static type checkers, linters, and IDEs to catch potential bugs before runtime.

### Type Hinting with Classes

In Python, you can use classes as type hints to indicate the expected type of a variable or function parameter. The type hints are specified using the `:` symbol after a variable name, or `->` to annotate the return type of a function. Here's an example:

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def greet(person: Person) -> str:
    return f"Hello, {person.name}!"

# Correct usage
p = Person("Alice", 30)
print(greet(p))  # Output: Hello, Alice!

# Incorrect usage, static type checker would flag this as an error
q = "this is not a Person object"
# print(greet(q))  # This would cause a type error, as q is not a Person object
```

In the example above:

- The `Person` class's `__init__` method expects two parameters: `name`, which should be a string (`str`), and `age`, which should be an integer (`int`).
- The `greet` function expects a `person` parameter, which should be an instance of the `Person` class, and it is annotated to return a string (`str`).

### Type Checking with `mypy`

While Python itself does not enforce type hints, you can use a static type checker like `mypy` to check the types in your codebase.

To check your code with `mypy`, you can install it using pip and run it from the command line:

```bash
pip install mypy
mypy your_file.py
```

`mypy` will analyze your code and report any type errors it finds. For example, if you try to pass a string to the `greet` function in the example above, `mypy` will report a type error.

## Abstract and Protocol Class Overview

In Python, both abstract classes and protocol classes are used for defining a common interface for a group of related classes. However, they have some differences, mainly in their enforcement levels and use cases. Let's take a detailed look at both and explore their similarities and differences.

### Abstract Classes

An abstract class in Python is a class that cannot be instantiated (you cannot create objects of an abstract class type) and is meant to be subclassed by other classes. It can define abstract methods that have no implementation in the abstract class itself but must be implemented by any concrete (non-abstract) subclasses.

You can use the `abc` module in Python to create abstract classes.

#### Example of Abstract Class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

# shape = Shape()  # This will raise a TypeError because Shape is an abstract class
rect = Rectangle(5, 3)
print(rect.area())  # Output: 15
```

#### Abstract Class Properties:

- Abstract classes can define abstract methods as well as concrete methods.
- Subclasses of an abstract class must implement all abstract methods.

### Protocol Classes

Protocol classes are introduced in Python 3.8 as part of the `typing` module. They are used for structural subtyping, which is a way of specifying interface contracts in a codebase. Unlike abstract classes, protocol classes do not enforce that classes inheriting from them implement their methods. However, type checkers like `mypy` can use protocol classes to perform type checking.

#### Example of Protocol Class:

```python
from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> str:
        pass

class Bird:
    def fly(self) -> str:
        return "Bird flying!"

class Airplane:
    def fly(self) -> str:
        return "Airplane flying!"

def takeoff(flyer: Flyer) -> None:
    print(flyer.fly())

bird = Bird()
airplane = Airplane()
takeoff(bird)  # Output: Bird flying!
takeoff(airplane)  # Output: Airplane flying!
```

#### Protocol Class Properties:

- Protocol classes define only the interface (method signatures) and no implementation.
- They do not enforce method implementation.
- They are used mainly for static type checking.

### Abstract vs Protocol Comparison:

1. **Enforcement:**
   - **Abstract Classes:** Enforce that subclasses must implement the abstract methods at runtime.
   - **Protocol Classes:** Do not enforce method implementation at runtime but are used by type checkers to check that a class conforms to the required interface.

2. **Use Case:**
   - **Abstract Classes:** Use when you want to enforce a common interface for subclasses and potentially provide some default implementation.
   - **Protocol Classes:** Use when you want to perform type checking against an expected interface, without enforcing implementation.

3. **Method Implementation:**
   - **Abstract Classes:** Can include both abstract methods (without implementation) and concrete methods (with implementation).
   - **Protocol Classes:** Typically only include method signatures, with no expectation of implementation.

In summary, use abstract classes when you want to enforce a certain class structure at runtime, and use protocol classes when you are more interested in static type checking without enforcing a class hierarchy.