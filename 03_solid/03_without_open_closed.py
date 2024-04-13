from typing import Optional, Any


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height


# I needed to modify AreaCalculator to support new shapes,
# this violated the closed for modification principle
class AreaCalculator:
    def calculate_area(self, shape: Any) -> Optional[int]:
        if isinstance(shape, Rectangle):  # had to know the shape type
            return (
                shape.width * shape.height
            )  # had to know the area calculation for the shape
        # for adding another shape type, you have to modify the
        # AreaCalculator class this violates the Open/Closed Principle
        return None


rect = Rectangle(5, 4)
calc = AreaCalculator()
print(calc.calculate_area(rect))  # Output: 20


#   Higher           Lower
# AreaCalculator -> Rectangle

# Higher            Even Higher  Lower
# AreaCalculator -> Shape <- Rectangle
