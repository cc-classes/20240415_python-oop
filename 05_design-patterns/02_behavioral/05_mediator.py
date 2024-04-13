# Mediator Pattern
#
# Reduces the connections between communicating objects, thereby reducing
# coupling and simplifying updates to the system.

from __future__ import annotations
from typing import Optional, Protocol


class Mediator(Protocol):
    def notify(self, sender: BaseComponent, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1: BaseComponent, component2: BaseComponent):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: BaseComponent, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            if isinstance(self._component2, Component2):
                self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            if isinstance(self._component1, Component1):
                self._component1.do_b()


class BaseComponent:
    def __init__(self, mediator: Optional[Mediator] = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Optional[Mediator]:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        if self.mediator:
            self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")

    def do_d(self) -> None:
        print("Component 2 does D.")
        if self.mediator:
            self.mediator.notify(self, "D")


# Client Code
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

c1.do_a()
c2.do_d()
