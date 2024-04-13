# Object-Oriented Python Programming Course

## Python Class Overview

In Python, a class is a blueprint for creating objects. Objects have properties (often known as attributes) and behaviors (methods). Below is a brief explanation of how Python classes work, along with some code examples:

## Defining a Class

You can define a class using the `class` keyword. Below is an example where we define a simple `Person` class with `name` and `age` attributes and a `greet` method:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

## Instantiating a Class

You can create an object (an instance of a class) by calling the class name as if it were a function, passing any required arguments to the `__init__` method:

```python
person = Person("Alice", 30)
```

In the code above, `person` is now an instance of the `Person` class, with `name` set to "Alice" and `age` set to 30.

## Accessing Attributes and Methods

You can access the object's attributes and methods using the dot notation:

```python
# Accessing attributes
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# Calling a method
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

## Modifying Attributes

You can change the value of attributes:

```python
person.age = 35
print(person.age)  # Output: 35
```

## Getter and Setter Methods

In Python, getter and setter methods are used for retrieving and updating the values of attributes, respectively. This practice is also known as "Encapsulation," and it ensures that the internal representation of an object is hidden from the outside. Python provides a `property()` function and `@property` and `@<attribute>.setter` decorators to define getters and setters.

### Using `@property` and `@<attribute>.setter`

Below is an example of how to use the `@property` and `@<attribute>.setter` decorators to define getter and setter methods:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # the underscore denotes it as "protected" (conventionally private)

    @property
    def radius(self):
        """
        This is the getter method for the radius.
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        This is the setter method for the radius.
        It checks if the provided value is positive before setting it.
        """
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @property
    def diameter(self):
        """
        This is a getter method for the diameter.
        It does not have a corresponding setter as the diameter is derived from the radius.
        """
        return self._radius * 2

# Creating a Circle object
c = Circle(5)
print(c.radius)  # Output: 5
print(c.diameter)  # Output: 10

# Setting a new radius
c.radius = 3
print(c.radius)  # Output: 3
print(c.diameter)  # Output: 6

# Trying to set a negative radius will raise a ValueError
try:
    c.radius = -2
except ValueError as e:
    print(e)  # Output: Radius cannot be negative.
```

In this example:

- The `radius` attribute is marked as protected by prefixing it with an underscore (`self._radius`).
- The `@property` decorator is used to define a getter for the `radius`. When you use `c.radius`, it will return the value of `_radius`.
- The `@radius.setter` decorator is used to define a setter for the `radius`. When you assign a value to `c.radius`, it will check if the value is positive and then update `_radius`.
- The `diameter` is a read-only property, calculated based on the `radius`. There is no setter for `diameter`, making it a read-only attribute.

### Using `property()` function

Alternatively, you can use the `property()` function to create properties:

```python
class Square:
    def __init__(self, side):
        self._side = side

    def get_side(self):
        return self._side

    def set_side(self, value):
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
```

In this example:

- The `get_side` function is a getter for the `side` attribute, and `set_side` is a setter.
- The `side` attribute is created as a property by passing `get_side` and `set_side` to the `property()` function.
