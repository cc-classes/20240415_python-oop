class Square:
    def __init__(self, side: int) -> None:
        self._side = side

    def get_side(self) -> int:
        return self._side

    def set_side(self, value: int) -> None:
        if value < 0:
            raise ValueError("Side cannot be negative.")
        self._side = value

    side = property(get_side, set_side)


# Creating a Square object
s = Square(4)
print(s.side)  # Output: 4

# Setting a new side length
s.side = 5
print(s.side)  # Output: 5

# Trying to set a negative side length will raise a ValueError
try:
    s.side = -3
except ValueError as e:
    print(e)  # Output: Side cannot be negative.
