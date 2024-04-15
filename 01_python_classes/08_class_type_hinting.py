class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        print("hi!")


def greet(person: Person) -> str:
    return f"Hello, {person.name}!"


# Correct usage
p = Person("Alice", 30)
print(greet(p))  # Output: Hello, Alice!

# Incorrect usage, static type checker would flag this as an error
q = "this is not a Person object"
# print(greet(q))  # This would cause a type error, as q is not a Person object
