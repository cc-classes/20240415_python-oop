# Composition example in Python
class Leg:
    def raise_leg(self) -> None:
        print("raise leg")

    def lower_leg(self) -> None:
        print("lower leg")


class Tail:
    pass


class Wing:
    pass


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

    def move(self) -> None:
        raise NotImplementedError


# Inheritance is a "is-a" relationship
# Composition is a "has-a" relationship


# Dog inherits from Animal
# Dog is an Animal ("is-a" relationship)
class Dog(Animal):
    def __init__(self) -> None:
        # Dog has a Leg ("has-a" relationship)
        # Dog has a Tail ("has-a" relationship)
        # the creation of the legs and tail is an example of composition
        # Dog is incorporating the functionality of Leg and Tail classes
        #   into its implementation
        self.leg1 = Leg()
        self.leg2 = Leg()
        self.leg3 = Leg()
        self.leg4 = Leg()
        self.tail = Tail()

    # def walk(self) -> None:
    #     self.leg1.raise_leg()
    #     self.leg2.lower_leg()

    def move(self) -> None:
        self.leg1.raise_leg()
        self.leg2.lower_leg()


class Bird:
    def __init__(self) -> None:
        self.leg1 = Leg()
        self.leg2 = Leg()
        self.left_wing = Wing()
        self.right_wing = Wing()

    def fly(self) -> None:
        self.leg1.raise_leg()
        self.leg2.raise_leg()


dog = Dog()
dog.walk()

bird = Bird()
bird.fly()
