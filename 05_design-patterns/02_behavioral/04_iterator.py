# Iterator Pattern
#
# Provides a way to access the elements of an aggregate object sequentially
# without exposing its underlying representation.

from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")

class Iterator(Generic[T]):
    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> T:
        raise NotImplementedError


class Numbers(Iterator[int]):
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end

    def __next__(self) -> int:
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


# Client Code
numbers = Numbers(1, 5)

# The iterator pattern is commonly used in Python
for num in numbers:
    print(num)  # Output: 1 2 3 4 5
