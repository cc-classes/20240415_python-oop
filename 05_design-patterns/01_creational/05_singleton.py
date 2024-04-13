# Singleton Pattern
#
# Ensures a class has only one instance and provides a global point to
# access it.

from __future__ import annotations
from typing import Optional


class Singleton:
    _instance: Optional[Singleton] = None

    # The __new__ method is a special method in Python that is called when
    # an object is created. It is responsible for creating and returning a
    # new instance of the class. This method is called before the __init__
    # method, which is responsible for initializing the object's attributes.
    def __new__(cls) -> Singleton:
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Client code
singleton1 = Singleton()
singleton2 = Singleton()
assert singleton1 == singleton2  # They are the same object
