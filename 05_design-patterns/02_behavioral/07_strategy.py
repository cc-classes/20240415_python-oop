# Strategy Pattern
#
# Allows selecting an algorithm’s implementation at runtime.

from abc import ABC, abstractmethod
from typing import Any


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: list[Any]) -> list[Any]:
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, dataset: list[Any]) -> list[Any]:
        # Bubble sort algorithm
        return sorted(dataset)


class QuickSortStrategy(SortingStrategy):
    def sort(self, dataset: list[Any]) -> list[Any]:
        # Quick sort algorithm
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2]
        left = [x for x in dataset if x < pivot]
        middle = [x for x in dataset if x == pivot]
        right = [x for x in dataset if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, dataset: list[Any]) -> list[Any]:
        return self._strategy.sort(dataset)


# Client code
dataset = [1, 5, 4, 3, 2, 8]
sorter = Sorter(BubbleSortStrategy())
print(sorter.sort(dataset))  # Output: [1, 2, 3, 4, 5, 8]

sorter = Sorter(QuickSortStrategy())
print(sorter.sort(dataset))  # Output: [1, 2, 3, 4, 5, 8]
