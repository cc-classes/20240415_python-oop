# Inheritance example in Python
class Animal:
    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    # contract and implementation
    def eat(self, food: str) -> None:
        print(f"{self.name} is eating {food}")

    # contract only, no implementation
    def speak(self) -> str:
        raise NotImplementedError


class Dog:

    def __init__(self) -> None:
        self.animal = Animal()

    def speak(self) -> str:
        return f"{self.name} says, 'Bark!'"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says, 'Meow!'"

    def jump(self) -> None:
        print(f"{self.name} is jumping")


def spend_time_with_animal(animal: Animal) -> None:
    print(f"Spending time with {animal.get_name()}")
    print(animal.speak())


dog = Dog()
dog.set_name("Rover")
dog.eat("Dog food")
print(dog.speak())  # Output: Bark!
spend_time_with_animal(dog)

cat = Cat()
cat.set_name("Pumpkin")
cat.eat("Cat food")
print(cat.speak())
spend_time_with_animal(cat)
cat.jump()  # Output: Pumpkin is jumping
