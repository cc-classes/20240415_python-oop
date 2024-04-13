# has-a relationship through composition

from typing import Protocol


class Grandparent(Protocol):
    def heritage(self) -> None: ...


class Grandparent1:
    def heritage(self) -> None:
        print("Grandparent's Heritage")


class Parent:
    def __init__(self, grandparent: Grandparent):
        self.grandparent = grandparent

    def property(self) -> None:
        print("Parent's Property")


class Child:
    def __init__(self, grandparent: Grandparent, parent: Parent):
        self.grandparent = grandparent
        self.parent = parent

    def own_property(self) -> None:
        print("Child's Property")


# Create an instance of Child
gp1 = Grandparent1()
child = Child(gp1, Parent(gp1))
child.grandparent.heritage()  # Output: Grandparent's Heritage
child.parent.property()  # Output: Parent's Property
child.own_property()  # Output: Child's Property
