# Object-Oriented Python Programming Course

## Liskov Substitution Principle (LSP) Deep Dive

The Liskov Substitution Principle (LSP) is the third principle in the SOLID principles. It states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This principle ensures that a subclass can be substituted for a superclass without affecting the behavior of the program.

## Why Use LSP?

- Ensures that a derived class does not affect the behavior of the parent class.
- Enhances code maintainability and scalability by ensuring that subclasses maintain the behavior of the superclass.
- Reduces the likelihood of errors in the codebase.

## LSP Example

Consider a scenario where you have a `Bird` class and you want to create a subclass `Ostrich`. An ostrich is a bird, but it cannot fly. This scenario is often where LSP violations occur.

### Without Applying LSP:

```python
class Bird:
    def fly(self):
        pass


class Ostrich(Bird):
    def fly(self):
        raise Exception("Can't fly")


def let_it_fly(bird):
    bird.fly()


bird = Bird()
ostrich = Ostrich()

let_it_fly(bird)  # works fine
let_it_fly(ostrich)  # raises Exception: "Can't fly"
```

In the above example, although `Ostrich` is a `Bird`, the `Ostrich` class violates the Liskov Substitution Principle because it does not properly substitute the `Bird` class (an ostrich cannot fly).

### Applying LSP:

To adhere to the Liskov Substitution Principle, you should refactor the classes to ensure that the `Ostrich` class can properly substitute the `Bird` class.

```python
from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class Sparrow(Bird):
    def move(self):
        print("Fly")


class Ostrich(Bird):
    def move(self):
        print("Run")


def let_it_move(bird: Bird):
    bird.move()


sparrow = Sparrow()
ostrich = Ostrich()

let_it_move(sparrow)  # Output: Fly
let_it_move(ostrich)  # Output: Run
```

In this refactored code:

- The `Bird` class is an abstract class with an abstract `move` method.
- The `Sparrow` and `Ostrich` classes are subclasses of `Bird` and provide their own implementations of the `move` method.
- The `let_it_move` function accepts a `Bird` object and calls its `move` method.

Now, the `Ostrich` class properly substitutes the `Bird` class without affecting the behavior of the `let_it_move` function, adhering to the Liskov Substitution Principle. The `Ostrich` class can be used wherever a `Bird` class is expected, and it behaves correctly.

In essence, to follow the Liskov Substitution Principle, ensure that subclasses maintain the behavior expected from objects of the superclass type. This often involves using abstract base classes and ensuring that subclasses adhere to the contract defined by the base class.