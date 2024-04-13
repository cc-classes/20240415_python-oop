# Visitor Pattern
#
# Adds further operations to objects without having to modify them.

from __future__ import annotations
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: AreaVisitor) -> float:
        pass


# While the Circle and Rectangle classes will not be modified,
# they must accept the visitor object.


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: AreaVisitor) -> float:
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def accept(self, visitor: AreaVisitor) -> float:
        return visitor.visit_rectangle(self)


class AreaVisitor:
    def visit_circle(self, circle: Circle) -> float:
        import math

        return math.pi * circle.radius * circle.radius

    def visit_rectangle(self, rectangle: Rectangle) -> float:
        return rectangle.width * rectangle.height


circle = Circle(5)
rectangle = Rectangle(4, 7)
area_calculator = AreaVisitor()

print(f"Area of circle: {circle.accept(area_calculator)}")
print(f"Area of rectangle: {rectangle.accept(area_calculator)}")
