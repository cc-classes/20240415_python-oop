# Contract - were we define the interface between two things
# Implementation - were we define the actual code that makes the contract work

# Inheritance example in Python
# Animal is the base class, super class, or parent class
class Animal:
    def __init__(self, name: str, species: str) -> None:
        self._name = name
        self._species = species

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def tag_value(self) -> str:
        return f"{self._name}:{self._species}"

    # contract and implementation
    def eat(self, food: str) -> None:
        print(f"{self.name} is eating {food}")

    # contract only, no implementation
    def speak(self) -> str:
        raise NotImplementedError


# sub class, child class
class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Dog")

    def speak(self) -> str:
        return f"{self.name} says, 'Bark!'"


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Cat")

    def speak(self) -> str:
        return f"{self.name} says, 'Meow!'"

    def jump(self) -> None:
        print(f"{self.name} is jumping")


# the animal parameter is of type Animal
# any subclass of Animal (such as Cat or Dog) can
# be passed in
def spend_time_with_animal(animal: Animal) -> None:
    print(f"Spending time with {animal.name}")
    print(animal.speak())


dog = Dog("fido")
dog.name = "Rover"
dog.eat("Dog food")
print(dog.speak())  # Output: Bark!
spend_time_with_animal(dog)
print(dog.tag_value)  # Output: Rover:Dog

cat = Cat("pumpkin")
cat.name = "Lily"
cat.eat("Cat food")
print(cat.speak())
spend_time_with_animal(cat)
cat.jump()  # Output: Pumpkin is jumping
