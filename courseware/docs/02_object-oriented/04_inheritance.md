# Object-Oriented Python Programming Course

## Object-Oriented Inheritance Overview

Inheritance in Object-Oriented Programming (OOP) is a feature that allows a class (subclass/derived/child class) to acquire the properties and behaviors (methods) of another class (superclass/base/parent class). The main advantages of inheritance include code reusability, a hierarchical class structure, and the ability to add additional features to existing code without modifying it.

In Python, inheritance is defined by creating new classes based on existing ones, thus promoting reusability and a logical class structure.

Below are some more specific types of inheritance:

1. **Single Inheritance**: One base class and one derived class.
2. **Multiple Inheritance**: One derived class inheriting from multiple base classes.
3. **Multilevel Inheritance**: A chain of classes inheriting from each other.
4. **Hierarchical Inheritance**: Multiple derived classes inheriting from a single base class.

Let's explore each with an example.

### Single Inheritance

In single inheritance, a class inherits from a single base class.

```python
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog Barking")

# Create an instance of Dog
dog = Dog()
dog.speak()  # Output: Animal Speaking
dog.bark()   # Output: Dog Barking
```

In this example, `Dog` is derived from the `Animal` class and inherits its `speak` method.

### Multiple Inheritance

In multiple inheritance, a class can inherit from more than one base class.

```python
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
```

Here, `Child` is inheriting from both `Father` and `Mother` classes.

### Multilevel Inheritance

In multilevel inheritance, a class is derived from a base class, which is itself derived from another base class.

```python
class Grandparent:
    def heritage(self) -> None:
        print("Grandparent's Heritage")


class Parent(Grandparent):
    def property(self) -> None:
        print("Parent's Property")


class Child(Parent):
    def own_property(self) -> None:
        print("Child's Property")


# Create an instance of Child
child = Child()
child.heritage()  # Output: Grandparent's Heritage
child.property()  # Output: Parent's Property
child.own_property()  # Output: Child's Property
```

In this example, `Child` is derived from `Parent`, which is in turn derived from `Grandparent`.

### Hierarchical Inheritance

In hierarchical inheritance, more than one derived class is created from a single base class.

```python
class Parent:
    def family_name(self):
        print("Smith")

class Daughter(Parent):
    def first_name(self):
        print("Emma")

class Son(Parent):
    def first_name(self):
        print("John")

# Create instances
daughter = Daughter()
son = Son()

daughter.family_name()  # Output: Smith
daughter.first_name()   # Output: Emma

son.family_name()       # Output: Smith
son.first_name()        # Output: John
```

Here, both `Daughter` and `Son` classes are derived from the `Parent` class.

These examples cover the major types of inheritance in Python and demonstrate how classes can be structured in hierarchical relationships, allowing properties and methods to be inherited from one class to another.