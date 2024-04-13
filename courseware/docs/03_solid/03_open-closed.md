# Object-Oriented Python Programming Course

## Open/Closed Principle

The Open/Closed Principle (OCP), the second of the SOLID principles, states that software entities should be open for extension but closed for modification. This means that the behavior of a module can be extended without modifying its source code.

## Why Use OCP?

- Reduces the risk of introducing new bugs when adding new functionality because existing code is not altered.
- Promotes the development of scalable and maintainable code by encouraging the use of reusable components.

## OCP Example

Consider a scenario where you have a class that calculates the area of different geometric shapes.

### Without Applying OCP:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        # for adding another shape type, you have to modify the AreaCalculator class
        # this violates the Open/Closed Principle


rect = Rectangle(5, 4)
calc = AreaCalculator()
print(calc.calculate_area(rect))  # Output: 20
```

In this example, if you want to calculate the area for a new shape (like a circle), you have to modify the `AreaCalculator` class. This is not ideal as per the Open/Closed Principle.

### Applying OCP:

You can apply the Open/Closed Principle by using polymorphism to create a common interface for all shapes and implementing the `calculate_area` method for each shape.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()


rect = Rectangle(5, 4)
circ = Circle(3)
calc = AreaCalculator()
print(calc.calculate_area(rect))  # Output: 20
print(calc.calculate_area(circ))  # Output: 28.26
```

In this refactored code:

- The `Shape` class is an abstract base class with an abstract method `calculate_area`.
- The `Rectangle` and `Circle` classes inherit from `Shape` and implement the `calculate_area` method.
- The `AreaCalculator` class can calculate the area for any shape that implements the `Shape` interface.
- Now, to add a new shape, you just need to create a new class for the shape that inherits from `Shape` and implement the `calculate_area` method, without modifying the `AreaCalculator` class.

This approach adheres to the Open/Closed Principle by allowing the `AreaCalculator` class to support new shapes without modifying its source code.