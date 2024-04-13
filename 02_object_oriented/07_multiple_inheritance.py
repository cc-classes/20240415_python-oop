# this example of multiple is more similar to the mixin pattern
# from the Python class review

# the multiple inheritance here is not too bad, because:

# 1. there are no __init__ functions
# 2. the method names inherited from each class are unique


class Father:
    def gardening(self) -> None:
        print("Loves gardening")


class Mother:
    def reading(self) -> None:
        print("Loves reading")


class Child(Father, Mother):
    def sports(self) -> None:
        print("Loves sports")


# Create an instance of Child
child = Child()
child.gardening()  # Output: Loves gardening
child.reading()  # Output: Loves reading
child.sports()  # Output: Loves sports
