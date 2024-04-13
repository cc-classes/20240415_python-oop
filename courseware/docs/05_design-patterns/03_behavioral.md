# Object-Oriented Python Programming Course

## Behavioral Design Patterns

Let's delve deeper into each of the Behavioral Design Patterns with Python code examples.

### 1. **Chain of Responsibility Pattern**

The Chain of Responsibility Pattern passes the request along a chain of potential handlers until an object handles it.

#### Example:

```python
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class ConcreteHandlerA(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler

    def handle(self, request):
        if request == "A":
            print("Handler A handling request A")
        elif self._next_handler:
            self._next_handler.handle(request)


class ConcreteHandlerB(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler

    def handle(self, request):
        if request == "B":
            print("Handler B handling request B")
        elif self._next_handler:
            self._next_handler.handle(request)


# Client code
handlerA = ConcreteHandlerA()
handlerB = ConcreteHandlerB()
handlerA.set_next(handlerB)

handlerA.handle("A")  # Output: Handler A handling request A
handlerA.handle("B")  # Output: Handler B handling request B
```

### 2. **Command Pattern**

The Command Pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests.

#### Example:

```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def execute(self):
        print("Turn on the light")


class LightOffCommand(Command):
    def execute(self):
        print("Turn off the light")


class LightSwitch:
    def __init__(self, command: Command):
        self._command = command

    def operate(self):
        self._command.execute()


# Client code
switch = LightSwitch(LightOnCommand())
switch.operate()  # Output: Turn on the light

switch = LightSwitch(LightOffCommand())
switch.operate()  # Output: Turn off the light
```

### 3. Interpreter Pattern:

The Interpreter pattern is used to evaluate sentences in a language. Below is a basic example where we are interpreting a language that contains only addition and subtraction:

```python
class Expression:
    def interpret(self, context):
        pass


class Number(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self, context):
        return self._value


class Plus(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context):
        return self._left.interpret(context) + self._right.interpret(context)


class Minus(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context):
        return self._left.interpret(context) - self._right.interpret(context)


# Client Code
context = {}
expression = Plus(Number(3), Minus(Number(2), Number(1)))
print(expression.interpret(context))  # Output: 4
```

In the example above, `Number`, `Plus`, and `Minus` are interpreter expressions that evaluate numbers, addition, and subtraction respectively.

### 4. Iterator Pattern:

The Iterator pattern allows sequential access to elements in a collection without exposing the underlying representation of the collection. Below is an example in Python:

```python
class Iterator:
    def __iter__(self):
        return self

    def __next__(self):
        pass


class Numbers(Iterator):
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


# Client Code
numbers = Numbers(1, 5)
for num in numbers:
    print(num)  # Output: 1 2 3 4 5
```

In this example, the `Numbers` class is an iterator that iterates from a start number to an end number.

### 5. Mediator Pattern:

The Mediator pattern defines an object that centralizes communication between objects in a system. Below is an example in Python:

```python
class Mediator:
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()


class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")


class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


# Client Code
c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

c1.do_a()
c2.do_d()
```

In this example, `ConcreteMediator` is a mediator class that coordinates the interaction between `Component1` and `Component2`. Components `do_a` and `do_d` methods notify the mediator about events, and the mediator decides what should happen next.



### 6. **Observer Pattern**

The Observer Pattern defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.

#### Example:

```python
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class ConcreteObserver(Observer):
    def update(self, message: str):
        print(f"Observer received message: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


# Client code
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify("This is a message!")  # Output: Observer received message: This is a message!
```


### 7. **Strategy Pattern**

The Strategy Pattern defines a family of algorithms, encapsulates each one of them, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

#### Example:

```python
from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, dataset):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, dataset):
        # Bubble sort algorithm
        return sorted(dataset)


class QuickSortStrategy(SortingStrategy):
    def sort(self, dataset):
        # Quick sort algorithm
        if len(dataset) <= 1:
            return dataset
        pivot = dataset[len(dataset) // 2]
        left = [x for x in dataset if x < pivot]
        middle = [x for x in dataset if x == pivot]
        right = [x for x in dataset if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, dataset):
        return self._strategy.sort(dataset)


# Client code
dataset = [1, 5, 4, 3, 2, 8]
sorter = Sorter(BubbleSortStrategy())
print(sorter.sort(dataset))  # Output: [1, 2, 3, 4, 5, 8]

sorter = Sorter(QuickSortStrategy())
print(sorter.sort(dataset))  # Output: [1, 2, 3, 4, 5, 8]
```

### 8. **Memento Pattern**

The Memento Pattern is used to capture the current state of an object and store it in such a manner that it can be restored at a later time without breaking the rules of encapsulation.

#### Example:

Below is a simple example demonstrating the Memento pattern in Python:

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    _state = ""

    def set(self, state):
        print(f"Originator: Setting state to {state}")
        self._state = state

    def create_memento(self):
        print(f"Originator: Creating memento with state {self._state}")
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()
        print(f"Originator: Restoring state to {self._state}")


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Client Code
originator = Originator()
caretaker = Caretaker()

originator.set("State1")
originator.set("State2")
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set("State3")
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set("State4")
originator.restore(caretaker.get_memento(0))
originator.restore(caretaker.get_memento(1))
```

In this example:
- `Memento` is the memento class that will hold the state.
- `Originator` is the class whose state we want to capture. It has methods to set the state, create a memento to store the state, and restore the state from a memento.
- `Caretaker` is responsible for keeping the mementos. 

Output of the code:

```plaintext
Originator: Setting state to State1
Originator: Setting state to State2
Originator: Creating memento with state State2
Originator: Setting state to State3
Originator: Creating memento with state State3
Originator: Setting state to State4
Originator: Restoring state to State2
Originator: Restoring state to State3
```

Here, after changing states to "State1", "State2", "State3", and "State4", we then restored the state back to "State2" and "State3" using the mementos stored in the `Caretaker`.


### 9. **State Pattern**

The State Pattern allows an object to change its behavior when its internal state changes.

#### Example:

```python
from abc import ABC, abstractmethod


class DrawingTool(ABC):
    def __init__(self, tool_name: str):
        self.tool_name = tool_name

    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError


class RectSelectionTool(DrawingTool):
    def __init__(self) -> None:
        super().__init__("RectSelectionTool")

    def handle(self) -> None:
        print("Select with a rectangle")


class LassoSelectionTool(DrawingTool):
    def __init__(self) -> None:
        super().__init__("LassoSelectionTool")

    def handle(self) -> None:
        print("Select with a lasso")


class DrawingApp:
    def active_tool(self) -> str:
        return self._tool.tool_name

    def change_tool(self, tool: DrawingTool) -> None:
        self._tool = tool

    def use_tool(self) -> None:
        self._tool.handle()


# Client code
app = DrawingApp()

app.change_tool(RectSelectionTool())
app.use_tool()

app.change_tool(LassoSelectionTool())
app.use_tool()
```

Absolutely! Below are Python examples for the Template Method and Visitor Patterns:

### 10. Template Method Pattern:

In the Template Method pattern, an abstract class exposes defined way(s)/template(s) to execute its methods. Subclasses can override the method implementations as per need, but the invocation is to be in the same way as defined by the abstract class.

Below is an example:

```python
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook()

    def base_operation1(self):
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    @abstractmethod
    def required_operations1(self):
        pass

    def hook(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 says: Implemented Operation1")


class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def hook(self):
        print("ConcreteClass2 says: Overridden Hook")


# Client Code
print("Same client code can work with different subclasses:")
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()

print("\n")

concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
```

In this example, `AbstractClass` provides a template method `template_method()` which consists of a series of method calls, including abstract methods `required_operations1()` which must be implemented by all concrete subclasses, and a `hook()` method which is optional to override.

### 11. Visitor Pattern:

The Visitor pattern is a behavioral design pattern that allows you to add further operations to objects without having to modify them. It involves two primary types: the Element class (which is the class that has details to be operated upon) and the Visitor class (which has operations to be performed). The pattern is particularly useful when dealing with a structure of many objects of varying types, and operations upon these objects need to be decoupled from the objects themselves.

Here's an example in Python:

```python
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
```

In this example:
- `Circle` and `Rectangle` are our `ConcreteElement` classes, each implementing the `accept` method which allows a visitor to visit them.
- `AreaVisitor` is our `ConcreteVisitor` class that implements operations (in this case, calculating areas) for each type of shape.
- When we want to calculate the area for a shape, we ask the shape to "accept" the area calculator visitor. The shape then calls the appropriate method on the visitor, passing itself as an argument.

This setup decouples the shape classes from the logic of calculating areas. If we want to introduce a new operation (e.g., perimeter calculation), we can do so by introducing a new visitor without changing the shape classes. Similarly, if we introduce a new shape, we'd only need to modify the visitor classes.

Each of these Behavioral Design Patterns helps in structuring the interactions between objects, allowing for efficient communication and delegation among objects.
