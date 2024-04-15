# Object-Oriented Programming - data and logic are combined and the logic is
# referred to as behaviors


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} says Woof!"


dog = Animal("Rover")
print(dog.speak())  # Output: Rover says Woof!
