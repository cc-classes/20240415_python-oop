# class Person:
#     def walk(self) -> None:
#         print("walks")


# class Parent(Person):
#     def care_for_child(self) -> None:
#         print("care for child")

#     # use polymorphism to change the walk method
#     def walk(self) -> None:
#         print("walks fast")


# p = Parent()
# p.walk()
# p.care_for_child()

# abstract class verison of person mobility
# useful if we had a partial implementation of PersonMobility
# from abc import ABC, abstractmethod


# class PersonMobility(ABC):
#     @abstractmethod
#     def walk(self) -> None: ...


# class PersonFastMobility(PersonMobility):
#     def walk(self) -> None:
#         print("walks fast")


# class PersonSlowMobility(PersonMobility):
#     def walk(self) -> None:
#         print("walks slow")

from typing import Protocol

# using the Protocol is better than the Abstract Class if Person Mobility has
# no partial implementation
class PersonMobility(Protocol):
    def walk(self) -> None: ...


class PersonFastMobility:
    def walk(self) -> None:
        print("walks fast")


class PersonSlowMobility:
    def walk(self) -> None:
        print("walks slow")


class Parent:
    def __init__(self, mobility: PersonMobility):
        self.mobility = mobility

    def walk(self) -> None:
        self.mobility.walk()

    def care_for_child(self) -> None:
        print("care for child")


p = Parent(PersonFastMobility())
p.walk()
p.care_for_child()
