# Memento Pattern
#
# Captures and externalizes an object's internal state so the object can be
# restored to this state later.


class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state


class Originator:
    _state = ""

    def set(self, state: str) -> None:
        print(f"Originator: Setting state to {state}")
        self._state = state

    def create_memento(self) -> Memento:
        print(f"Originator: Creating memento with state {self._state}")
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        # print(f"Originator: Restoring state to {self._state}")

    def get_state(self) -> str:
        return self._state


class Caretaker:
    def __init__(self) -> None:
        self._mementos: list[Memento] = []

    def add_memento(self, memento: Memento) -> None:
        self._mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self._mementos[index]


# Client Code
originator = Originator()
caretaker = Caretaker()

originator.set("State1")
originator.set("State2")
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set("State3")
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set("State4")
originator.restore(caretaker.get_memento(0))
originator.restore(caretaker.get_memento(1))

print(originator.get_state())
