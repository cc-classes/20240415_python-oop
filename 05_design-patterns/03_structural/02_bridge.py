# Bridge Pattern
#
# Separates an object’s abstraction from its implementation, allowing the
# two to vary independently.


class DrawingAPI:
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return ""

# partial class
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f"API1.circle at {x}:{y} radius {radius}"


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f"API2.circle at {x}:{y} radius {radius}"


# partial class
class CircleShape:
    def __init__(
        self, x: float, y: float, radius: float, drawing_api: DrawingAPI
    ) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    # the data is stored on the CircleShape object, but the drawing is
    # delegated to a DrawingAPI object
    def draw(self) -> str:
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Client code
circle1 = CircleShape(1, 2, 3, DrawingAPI1())
print(circle1.draw())  # Output: API1.circle at 1:2 radius 3

circle2 = CircleShape(2, 3, 4, DrawingAPI2())
print(circle2.draw())  # Output: API2.circle at 2:3 radius 4
