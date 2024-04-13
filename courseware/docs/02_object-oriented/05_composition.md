# Object-Oriented Python Programming Course

## Object-Oriented Composition Overview

Composition is an Object-Oriented Programming (OOP) concept that models a "has a" relationship between objects, allowing you to build complex classes by combining simpler, self-contained classes. It provides a way to use objects of different classes to achieve code reuse, without inheriting attributes and behaviors from a parent class.

### Why Use Composition?

- To use functionality from multiple classes without the drawbacks of multiple inheritance.
- To build flexible and clean code architectures that are easy to understand, modify, and maintain.
- To maintain a focus on a clear division of concerns among classes.

### Composition Example:

Consider a scenario where we need to represent a computer system that contains a processor, memory, and a storage device. Instead of inheriting properties from parent classes, each class remains self-contained, and the `Computer` class includes objects of other classes.

Below is an example to demonstrate composition in Python:

```python
class Processor:
    def __init__(self, model: str):
        self.model = model

    def execute(self):
        print(f"Executing tasks using {self.model} processor")


class Memory:
    def __init__(self, capacity: str):
        self.capacity = capacity

    def load_data(self):
        print(f"Loading data into {self.capacity} memory")


class Storage:
    def __init__(self, type_: str):
        self.type = type_

    def store_data(self):
        print(f"Storing data in {self.type} storage")


class Computer:
    def __init__(self, processor: Processor, memory: Memory, storage: Storage):
        self.processor = processor
        self.memory = memory
        self.storage = storage

    def perform_operations(self):
        self.processor.execute()
        self.memory.load_data()
        self.storage.store_data()


# Create objects of Processor, Memory, and Storage
processor = Processor("Intel i7")
memory = Memory("16GB")
storage = Storage("SSD")

# Passing objects as parameters to the Computer class
computer = Computer(processor, memory, storage)

# Performing operations
computer.perform_operations()
```

Output:
```
Executing tasks using Intel i7 processor
Loading data into 16GB memory
Storing data in SSD storage
```

In the example above:

- The `Computer` class is composed of objects of `Processor`, `Memory`, and `Storage` classes.
- The `Computer` class does not inherit from `Processor`, `Memory`, or `Storage`. Instead, it contains an object of each class, allowing it to use their methods (`execute`, `load_data`, `store_data`).
- Each component class (`Processor`, `Memory`, `Storage`) is self-contained, focusing on its own responsibility, and can be used, modified, or extended independently of the other classes.

This example demonstrates how composition in Python can be used to combine functionality from multiple classes into a single class, while keeping each class self-contained, modular, and focused on its own responsibilities. It provides flexibility and a clean structure for managing complex interactions among various components in the system.