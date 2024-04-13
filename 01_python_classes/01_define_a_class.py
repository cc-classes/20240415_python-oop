# full implementation and contract
# classes are used to create new object instances in Python,
# but the class itself is also an object instance
class Person:
    # constructor
    # self is not explicitly passed in by the caller
    # behind the scenes, Python will pass the new instance to __init__ as
    # the first parameter
    def __init__(self, name: str, age: int) -> None:
        # self points to the class instance
        self.name = name
        self.age = age

    # behavior, method, instance method
    # self is not explicitly passed in by the caller
    # when the instance is created, a bound version of this method is created
    # on the instance, the bound version receives the instance in the self
    # when it bound method is called
    def greet(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def get_age(self) -> int:
        return self.age

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            raise ValueError()
        self.age = new_age


person = Person("Alice", 30)
person2 = Person("John", 16)

person.greet()
person2.greet()

# Accessing attributes
print(person.name)  # Output: Alice
print(person.age)  # Output: 30

# Calling a method
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.

person.age = 35
person.set_age(-1)
print(person.get_age())  # Output: 35
