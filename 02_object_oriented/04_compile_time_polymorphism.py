def cat_speak() -> None:
    print("Meow!")


def dog_speak() -> None:
    print("Bark!")


class Animal:
    def __init__(self, animal_type: str) -> None:
        self.animal_type = animal_type

    def speak(self) -> None:
        if self.animal_type == "dog":
            dog_speak()
        else:
            cat_speak()


dog = Animal("dog")
dog.speak()

cat = Animal("cat")
cat.speak()
