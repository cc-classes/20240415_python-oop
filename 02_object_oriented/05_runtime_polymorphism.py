class Animal:
    def speak(self) -> str:
        return "make noise"


class Dog(Animal):
    def speak(self) -> str:
        return "Bark!"


class Cat(Animal):
    ...
    # def speak(self) -> str:
    #     return "Meow!"


def make_animal_speak(animal: Animal) -> None:
    print(animal.speak())


# Create instances
dog = Dog()
cat = Cat()

# Polymorphism: different object types are used with a common interface
make_animal_speak(dog)  # Output: Bark!
make_animal_speak(cat)  # Output: Meow!
