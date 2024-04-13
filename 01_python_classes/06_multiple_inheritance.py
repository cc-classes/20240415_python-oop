#       Animal
#     /      \
#    Fish    Bird
#     \      /
#     FlyingFish


class Animal:
    def __init__(self) -> None:
        print("Animal constructor")


class Fish(Animal):
    def __init__(self) -> None:
        print("Fish constructor")
        super().__init__()

    def swim(self) -> str:
        return "Swimming!"
    
    def do_it(self) -> None:
        print("Fish did it!")


class Bird(Animal):
    def __init__(self) -> None:
        print("Bird constructor")
        super().__init__()

    def fly(self) -> str:
        return "Flying!"
    
    def do_it(self) -> None:
        print("Bird did it!")    


class FlyingFish(Fish, Bird):
    def __init__(self) -> None:
        print("Flying Fish constructor")
        super().__init__()


flying_fish = FlyingFish()
flying_fish.do_it()
# print(flying_fish.swim())  # Output: Swimming!
# print(flying_fish.fly())  # Output: Flying!

print(FlyingFish.__mro__)

# print(Fish.__mro__)
