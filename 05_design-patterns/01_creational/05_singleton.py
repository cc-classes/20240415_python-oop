# Singleton Pattern
#
# Ensures a class has only one instance and provides a global point to
# access it.

from __future__ import annotations
from typing import Optional


# class Person:
#     def __init__(self, name: str) -> None:
#         self.name = name

#     @classmethod
#     def create_person(cls, name: str) -> Person:
#         print(type(cls))
#         print(f"Create person {name}")
#         return cls(name)

#     def print_name(self) -> None:
#         print(type(self))
#         print(self.name)


# # class type => class Person (type == class type) => self (type == class Person)

# # p = Person("John")
# # p.print_name()

# p3 = Person.create_person("Tim")

# # instance method and the first parameter will be the instance of class Person
# p3.print_name()

# # Python allows the instance to call the class method, but the first parameter
# # to the class method will still be the class object, not the instance object
# p3.create_person("Sally")

# # p2 = Person("Jane")
# # p2.print_name()


class Singleton:
    # class object attribute (not an instance attribute)
    _instance: Optional[Singleton] = None

    # The __new__ method is a special method in Python that is called when
    # an object is created. It is responsible for creating and returning a
    # new instance of the class. This method is called before the __init__
    # method, which is responsible for initializing the object's attributes.
    def __new__(cls) -> Singleton:
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.value = None


# Client code
singleton1 = Singleton()
singleton2 = Singleton()
assert singleton1 == singleton2  # They are the same object
