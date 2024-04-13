from typing import Protocol


class Shape(Protocol):
    def calculate_area(self) -> float:
        pass


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

    def calculate_circumference(self) -> float:
        return 2 * 3.14 * self.radius


class AreaCalculator:
    def calculate_area(self, shape: Shape) -> str:
        return f"Area Calculator: {shape.calculate_area()}"


def main(area_calc: AreaCalculator) -> None:
    rect = Rectangle(5, 4)
    circ = Circle(3)
    print(circ.calculate_circumference())
    print(f"rect area: {area_calc.calculate_area(rect)}")  # Output: 20
    print(f"circle area: {area_calc.calculate_area(circ)}")  # Output: 28.26


if __name__ == "__main__":
    main(AreaCalculator())
