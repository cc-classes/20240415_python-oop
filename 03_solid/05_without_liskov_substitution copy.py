from typing import Protocol


class IFlyingBird(Protocol):
    def fly(self) -> None:
        pass


class IAquaticBird(Protocol):
    def swim(self) -> None:
        pass


class Bird:
    def walk(self) -> None:
        pass


class Sparrow(Bird):
    def fly(self) -> None:
        pass


class Eagle(Bird):
    def fly(self) -> None:
        pass


class Penguin(Bird):
    def swim(self) -> None:
        pass


class Duck(Bird):
    def fly(self) -> None:
        pass

    def swim(self) -> None:
        pass


class Ostrich(Bird): ...


def let_it_fly(bird: IFlyingBird) -> None:
    bird.fly()


def let_it_swim(bird: IAquaticBird) -> None:
    bird.swim()


sparrow = Sparrow()
eagle = Eagle()
penguin = Penguin()
duck = Duck()
ostrich = Ostrich()

let_it_fly(sparrow)  # works fine
let_it_fly(eagle)

let_it_swim(penguin)
let_it_swim(duck)

let_it_fly(duck)
