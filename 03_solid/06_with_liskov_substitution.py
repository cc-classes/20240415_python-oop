from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def move(self) -> None:
        pass


class FlyingBird(Bird):
    def move(self) -> None:
        print("Fly")


class Eagle(FlyingBird): ...


class Sparrow(FlyingBird): ...


class Ostrich(Bird):
    def move(self) -> None:
        print("Run")


def let_it_move(bird: Bird) -> None:
    bird.move()


sparrow = Sparrow()
ostrich = Ostrich()

let_it_move(sparrow)  # Output: Fly
let_it_move(ostrich)  # Output: Run
