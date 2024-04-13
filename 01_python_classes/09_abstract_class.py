from abc import ABC, abstractmethod


# partial implementation and contract
class Shape(ABC):
    def set_name(self, name: str) -> None:
        self.name = name

    # contract only, no implementation
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    # it must implement the area method
    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, width: float):
        self.width = width

    # it must implement the area method
    def area(self) -> float:
        return self.width**2


def display_area(shape: Shape) -> None:
    print(shape.area())


# This will raise a TypeError because Shape is an abstract class
# shape = Shape()


rect = Rectangle(5, 3)
rect.set_name("some name")
display_area(rect)  # Output: 15

squ = Square(4)
display_area(squ)  # Output: 16
