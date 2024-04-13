# Chain of Responsibility Pattern
#
# Passes the request along a chain of potential handlers until an object
# handles it.

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> None:
        pass

    @abstractmethod
    def handle(self, request: str) -> None:
        pass


class ConcreteHandlerA(Handler):
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Optional[Handler]) -> None:
        self._next_handler = handler

    def handle(self, request: str) -> None:
        if request == "A":
            print("Handler A handling request A")
        elif self._next_handler:
            print(f"Received {request}, Handing off to Handler B")
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Optional[Handler]) -> None:
        self._next_handler = handler

    def handle(self, request: str) -> None:
        if request == "B":
            print("Handler B handling request B")
        elif self._next_handler:
            self._next_handler.handle(request)


# Client code
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.set_next(handler_b)

# handler_a.handle("A")  # Output: Handler A handling request A
handler_a.handle("B")  # Output: Handler B handling request B
