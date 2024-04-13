# Flyweight Pattern
#
# Minimizes memory usage or computational expenses by sharing as much as
# possible with related objects.

from __future__ import annotations
from typing import Any


class TreeType:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color


class Tree:
    _types: dict[tuple[str, str], TreeType] = {}

    def __new__(cls, name: str, color: str) -> Any:
        # look for an existing Tree object with the same name and color
        if (name, color) not in cls._types:
            # no existing Tree object was found, create a new one
            cls._types[(name, color)] = TreeType(name, color)

        # existing Tree object was found, return the object reference
        return cls._types[(name, color)]


# Client code
tree1 = Tree("Pine", "Green")
tree2 = Tree("Pine", "Green")
assert tree1 == tree2  # They are the same object
