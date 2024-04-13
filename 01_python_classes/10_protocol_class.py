from typing import Protocol


# define a contract only
class Flyer(Protocol):
    def fly(self) -> str:
        pass

    def land(self) -> str:
        pass


# the classes that use the contract do not directly
# tie back to it
class Bird:
    def fly(self) -> str:
        return "Bird flying!"

    def land(self) -> str:
        return "landing"


class Airplane:
    def fly(self) -> str:
        return "Airplane flying!"

    def land(self) -> str:
        return "landing"


class Boat:
    def sail(self) -> str:
        return "Boat is sailing!"


def takeoff(flyer: Flyer) -> None:
    print(flyer.fly())


bird = Bird()
airplane = Airplane()
boat = Boat()
takeoff(bird)  # Output: Bird flying!
takeoff(airplane)  # Output: Airplane flying!
# takeoff(boat) # causes an error
