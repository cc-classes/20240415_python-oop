# Object-Oriented Python Programming Course

## Object-Oriented Encapsulation Overview

Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to the bundling of data with the methods that operate on that data, restricting the direct access to some of an object's components and can prevent the accidental modification of data. Encapsulation helps in data hiding and exposing only the necessary functionalities.

In Python, encapsulation is implemented using private and protected members. By convention, a name prefixed with an underscore (e.g., `_name`) should be treated as a non-public part of the API, and it is considered internal to the module/class. Names with double underscores (e.g., `__name`) are mangled to _classname__name, providing a stronger indication that they are intended to be private.

## Encapsulation Example in Python:

Below is a detailed example of encapsulation in Python. Here, we define a `Person` class with private attributes `__name` and `__age`. The class has methods to set and get the values of these attributes, ensuring that the age cannot be set to a negative value.

```python
class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative!")

# Creating an object of the Person class
person = Person("John", 30)

# Accessing the attributes via methods
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 30

# Attempting to set a negative age
person.set_age(-5)  # Output: Age cannot be negative!
print(person.get_age())  # Output: 30

# Attempting to access the private variables directly (will result in an AttributeError)
# print(person.__age)  # AttributeError: 'Person' object has no attribute '__age'

# The correct name mangling to access __age would be:
print(person._Person__age)  # Output: 30 (Not recommended to use, as it violates encapsulation)
```

In this example:

- `__name` and `__age` are private members (attributes) of the `Person` class.
- `get_name()`, `set_name(name)`, `get_age()`, and `set_age(age)` are public members (methods) that allow controlled access and modification to the private attributes.
- Direct access to `__age` using `person.__age` is denied, ensuring encapsulation.
- However, Python performs name mangling of private members, so it is technically possible to access `__age` outside the class with `_Person__age`, though it's generally considered bad practice.

This encapsulation example demonstrates how you can control the access and modification of attributes within a class, ensuring that the internal state of the object is maintained properly and preventing unintended side effects from external operations.