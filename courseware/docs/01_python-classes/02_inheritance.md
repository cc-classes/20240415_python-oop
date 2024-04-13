# Object-Oriented Python Programming Course

## Inheritance and Composition

Inheritance and composition are two major concepts in object-oriented programming that deal with class organization and reuse.

### Inheritance

**Inheritance** is a mechanism by which one class can inherit the attributes and methods from another class. It provides a way to create a new class using previously defined classes. The new class, known as a derived class or child class, inherits attributes and behavior (methods) of the existing class, called a base class or parent class.

#### Pros:
- Promotes code reusability.
- Provides a way to establish a relationship between the parent and child classes.

#### Cons:
- Can lead to a tightly coupled code (if not used properly), making the codebase more fragile and harder to maintain.
- Can lead to confusion when dealing with overridden methods and attributes.
  
#### Example in Python:

```python
# Inheritance example in Python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

dog = Dog()
print(dog.speak())  # Output: Bark!
```

In the above example, `Dog` is a derived class that inherits from the `Animal` base class.

### Composition

**Composition** refers to combining simple objects or data types into more complex ones. It’s a way to build complex objects by using other objects. Objects can be assembled to achieve more complex functionality.

#### Pros:
- Provides better flexibility and is often considered a better method for code organization.
- Allows objects to change their behavior at run-time by changing their components.

#### Cons:
- Can lead to a system with many small objects that interact with each other, which can make the design more complicated.
  
#### Example in Python:

```python
# Composition example in Python
class Leg:
    pass

class Tail:
    pass

class Dog:
    def __init__(self):
        self.leg1 = Leg()
        self.leg2 = Leg()
        self.leg3 = Leg()
        self.leg4 = Leg()
        self.tail = Tail()

dog = Dog()
```

In this example, a `Dog` is composed of four `Leg` objects and one `Tail` object.

### Inheritance and Composition Summary

- Use **inheritance** when there is a clear, hierarchical relationship between classes and you want to reuse base class code in derived class.
- Use **composition** when you want to assemble different kinds of objects to achieve more complex functionality, or when you want to change the behavior of an object at runtime by changing its components. It's more flexible and is generally a better way to achieve code reuse and better design principles.

## What is Multiple Inheritance?

**Multiple Inheritance** is a feature in some object-oriented programming languages where a class can inherit attributes and methods from more than one parent class. It allows for the creation of a class that reuses the code from multiple classes, forming a more complex class structure.

### Using Multiple Inheritance in Python

In Python, you can create a class that inherits from multiple parent classes by listing the parent classes in parentheses in the class definition:

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

In this example, `Child` is a derived class that inherits from both `Parent1` and `Parent2`.

### Example: Creating a FlyingFish Class

Imagine we have two parent classes: `Fish`, which has a `swim` method, and `Bird`, which has a `fly` method. We want to create a `FlyingFish` class that can both fly and swim.

```python
class Fish:
    def swim(self):
        return "Swimming!"

class Bird:
    def fly(self):
        return "Flying!"

class FlyingFish(Fish, Bird):
    pass

flying_fish = FlyingFish()
print(flying_fish.swim())  # Output: Swimming!
print(flying_fish.fly())  # Output: Flying!
```

In this example, `FlyingFish` inherits from both `Fish` and `Bird`, so objects of the `FlyingFish` class can call both `swim` and `fly` methods.

### Caution with Multiple Inheritance

While multiple inheritance allows for powerful and flexible code, it can also lead to complexities, particularly with respect to method resolution order (MRO). Python uses the C3 Linearization or C3 superclass linearization algorithm to handle multiple inheritance and determine the order in which parent classes are accessed.

To view the MRO of a class, you can use the `__mro__` attribute or the `mro()` method:

```python
print(FlyingFish.__mro__)
# Output: (<class '__main__.FlyingFish'>, <class '__main__.Fish'>, <class '__main__.Bird'>, <class 'object'>)
```

In this example, the MRO is `FlyingFish`, `Fish`, `Bird`, and `object`. This is the order Python will use to search for methods or attributes.

In general, use multiple inheritance cautiously and consider alternative design patterns.

### Multiple Inheritance Pattern: Mixin

In Python, a Mixin is a type of multiple inheritance where a class provides methods that can be used by other classes but does not serve as a standalone class itself. Mixins are a way to compose classes together and reuse code in a modular fashion. They're used to "mix in" additional behavior to a class without affecting the class hierarchy.

### Implementing the Mixin Pattern in Python

Here's how you can use Mixins in Python:

#### Step 1: Create the Mixin Class

First, create the mixin class that contains the methods you want to reuse. It should not inherit from any other class and should not be used as a standalone class.

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
```

In this example, the `JSONMixin` class has a `to_json` method that converts an object's attributes to a JSON string.

#### Step 2: Use the Mixin Class with Other Classes

Now you can use the mixin with other classes, using multiple inheritance.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JSONPerson(JSONMixin, Person):
    pass
```

In this example, `JSONPerson` inherits from both `JSONMixin` and `Person`. So, `JSONPerson` objects have a `to_json` method, as well as `name` and `age` attributes.

#### Step 3: Create Objects and Use Methods from the Mixin

Now you can create objects of the class that uses the mixin and use the methods provided by the mixin.

```python
p = JSONPerson("Alice", 30)
print(p.to_json())  # Output: {"name": "Alice", "age": 30}
```

In this example, the `p` object has a `to_json` method from the `JSONMixin` class, and it works as expected, converting the `p` object's attributes to a JSON string.

### Mixin Example with Multiple Mixins

Here is an example using multiple mixins:

```python
class XMLMixin:
    def to_xml(self):
        from xml.etree.ElementTree import Element, tostring
        from xml.dom import minidom

        elem = Element(self.__class__.__name__)
        for key, value in self.__dict__.items():
            child = Element(key)
            child.text = str(value)
            elem.append(child)
        raw_xml = tostring(elem)
        pretty_xml = minidom.parseString(raw_xml).toprettyxml()
        return pretty_xml

class JSONXMLPerson(JSONMixin, XMLMixin, Person):
    pass

person = JSONXMLPerson("Bob", 40)
print(person.to_json())
print(person.to_xml())
```

In this example, `JSONXMLPerson` inherits from two mixin classes, `JSONMixin` and `XMLMixin`, as well as the `Person` class. Objects of this class have both `to_json` and `to_xml` methods, allowing them to be converted to either JSON or XML format.

### Multiple Inheritance Conclusion

In summary, the mixin pattern in Python leverages multiple inheritance to provide a powerful and flexible way to reuse code. By creating small, focused mixin classes, you can compose classes with precisely the functionality they need, without creating complex class hierarchies or duplicating code.