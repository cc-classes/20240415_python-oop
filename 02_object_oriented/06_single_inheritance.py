class Animal:
    def speak(self) -> None:
        print("Animal Speaking")


class Dog(Animal):
    def bark(self) -> None:
        print("Dog Barking")


# Create an instance of Dog
dog = Dog()
dog.speak()  # Output: Animal Speaking
dog.bark()  # Output: Dog Barking

animal = Animal()
animal.speak()
# animal.bark() # will not work, inheritance is one way
