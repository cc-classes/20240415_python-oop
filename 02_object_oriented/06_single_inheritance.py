class Animal:
    def move(self) -> None:
        print("Animal moving")


class Dog(Animal):
    def bark(self) -> None:
        print("Dog Barking")


# Create an instance of Dog
dog = Dog()
dog.move()  # Output: Animal moving
dog.bark()  # Output: Dog Barking

animal = Animal()
animal.move()
# animal.bark() # will not work, inheritance is one way
