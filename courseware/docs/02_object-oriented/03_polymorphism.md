# Object-Oriented Python Programming Course

## Object-Oriented Polymorphism Overview

Polymorphism is a fundamental concept of OOP that allows objects of different classes to be treated as objects of a common superclass. The two types of polymorphism in OOP are:

1. **Compile-time polymorphism (Method Overloading):**
   - This type is achieved by function overloading.
   - For example, operators are overloaded in Python to perform different operations based on the type of their operands.
  
2. **Runtime polymorphism (Method Overriding):**
   - Achieved by function overriding.
   - In Python, runtime polymorphism can be implemented using inheritance and the overridden methods of the base class.

Below, we'll explore some examples to demonstrate polymorphism in Python.

### Compile-time Polymorphism Example in Python:

In Python, we can use default arguments, variable-length arguments, etc., to achieve compile-time polymorphism. Below is an example of how we can overload a function to perform different tasks:

```python
class Greet:
    def hello(self, name=None):
        if name is not None:
            print(f'Hello {name}')
        else:
            print('Hello ')

# Create instance
obj = Greet()

# Call the method
obj.hello()

# Call the method with a parameter
obj.hello('Python')
```

Output:
```
Hello 
Hello Python
```

In the example above, we defined a method named `hello`, which can be called with or without a parameter. This is a very basic example of polymorphism in Python (compile-time polymorphism).

### Runtime Polymorphism Example in Python:

Below is an example demonstrating runtime polymorphism in Python:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

# Create instances
dog = Dog()
cat = Cat()

# Polymorphism: different object types are used with a common interface
make_animal_speak(dog)  # Output: Bark!
make_animal_speak(cat)  # Output: Meow!
```

In this example:

- `Animal` is a base class with a `speak` method.
- `Dog` and `Cat` are derived classes that override the `speak` method.
- The `make_animal_speak` function accepts an `Animal` object and calls its `speak` method.
- Even though `make_animal_speak` is written to work with `Animal` objects, it can work with any object of a subclass of `Animal`, thanks to polymorphism.

This example demonstrates runtime polymorphism in Python, as the `speak` method is overridden in `Dog` and `Cat` subclasses, and the correct version of the `speak` method is called at runtime based on the object passed to the `make_animal_speak` function.