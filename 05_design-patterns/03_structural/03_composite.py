# Composite Pattern
#
# Allows individual objects and composites (group of objects) to be treated
# uniformly.


class Component:
    def show(self) -> str:
        return ""


class Leaf(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def show(self) -> str:
        return f"Leaf: {self.name}"


class Composite(Component):
    def __init__(self) -> None:
        self.children: list[Leaf] = []

    def add(self, child: Leaf) -> None:
        self.children.append(child)

    def show(self) -> str:
        return (
            "Composite: ["
            + ", ".join(child.show() for child in self.children)
            + "]"
        )


# Client code
leaf1 = Leaf("1")
leaf2 = Leaf("2")
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)

# whether a single object or a group of objects, they are treated the same
print(leaf1.show())  # Output: Leaf: 1
print(leaf2.show())  # Output: Leaf: 2
print(composite.show())  # Output: Composite: [Leaf: 1, Leaf: 2]
