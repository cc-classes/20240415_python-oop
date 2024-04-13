class Bird:
    def fly(self) -> None:
        pass


class Ostrich(Bird):
    def fly(self) -> None:
        raise Exception("Can't fly")


def let_it_fly(bird: Bird) -> None:
    bird.fly()


bird = Bird()
ostrich = Ostrich()

let_it_fly(bird)  # works fine
let_it_fly(ostrich)  # raises Exception: "Can't fly"
