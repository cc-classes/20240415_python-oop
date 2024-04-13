# Object-Oriented Python Programming Course

## Structural Design Patterns

Let's delve into each of the Structural Design Patterns with Python code examples.

### 1. **Adapter Pattern**

The Adapter Pattern allows incompatible interfaces to work together. This makes one class appear as another class by providing a wrapper around it.

#### Example:

```python
class OldSystem:
    def old_request(self):
        return "Old System Request"


class NewSystem:
    def request(self):
        return "New System Request"


class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.old_request()


# Client code
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.request())  # Output: Old System Request
```

In this example, the `Adapter` class makes `OldSystem` compatible with `NewSystem` by implementing the `request` method.

### 2. **Bridge Pattern**

The Bridge Pattern separates an object’s abstraction from its implementation, allowing the two to vary independently.

#### Example:

```python
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API1.circle at {x}:{y} radius {radius}"


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        return f"API2.circle at {x}:{y} radius {radius}"


class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Client code
circle1 = CircleShape(1, 2, 3, DrawingAPI1())
print(circle1.draw())  # Output: API1.circle at 1:2 radius 3

circle2 = CircleShape(2, 3, 4, DrawingAPI2())
print(circle2.draw())  # Output: API2.circle at 2:3 radius 4
```

### 3. **Composite Pattern**

The Composite Pattern is used to treat both individual objects and compositions of objects uniformly.

#### Example:

```python
class Component:
    def show(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"Leaf: {self.name}"


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, child):
        self.children.append(child)

    def show(self):
        return "Composite: [" + ", ".join(child.show() for child in self.children) + "]"


# Client code
leaf1 = Leaf("1")
leaf2 = Leaf("2")
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.show())  # Output: Composite: [Leaf: 1, Leaf: 2]
```

### 4. **Decorator Pattern**

The Decorator Pattern is used to add new functionality to an object dynamically without altering its structure.

#### Example:

```python
class Coffee:
    def cost(self):
        return 5


class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2


# Client code
coffee = Coffee()
print(coffee.cost())  # Output: 5

milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())  # Output: 7
```



### 5. Facade Pattern:

The facade pattern is used to define a simplified interface to a more complex subsystem. 

Example:

```python
class CPU:
    def freeze(self):
        print("Freezing processor.")

    def jump(self, position):
        print(f"Jumping to position {position}")

    def execute(self):
        print("Executing instructions.")


class Memory:
    def load(self, position, data):
        print(f"Loading data {data} at position {position}")


class HardDrive:
    def read(self, lba, size):
        return f"Data from sector {lba} with size {size}"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.hd.read("0x00", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


# Client Code
computer = ComputerFacade()
computer.start()
```

In this example, `ComputerFacade` provides a simplified interface (`start method`) to the subsystems `CPU`, `Memory`, and `HardDrive`.


### 6. **Flyweight Pattern**

The Flyweight Pattern minimizes memory usage or computational expenses by sharing as much as possible with related objects.

#### Example:

```python
class TreeType:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Tree:
    _types = {}

    def __new__(cls, name, color):
        if (name, color) not in cls._types:
            cls._types[(name, color)] = TreeType(name, color)
        return cls._types[(name, color)]


# Client code
tree1 = Tree("Pine", "Green")
tree2 = Tree("Pine", "Green")
assert tree1 == tree2  # They are the same object
```

### 7. **Proxy Pattern**

The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.

#### Example:

```python
class RealImage:
    def display(self):
        return "Displaying image"


class ProxyImage:
    def __init__(self):
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage()
        return self.real_image.display()


# Client code
proxy = ProxyImage()
print(proxy.display())  # Output: Displaying image
```

Each of these Structural Design Patterns serves different purposes and is used in different scenarios to help make the design and architecture of the software more efficient and cleaner.
