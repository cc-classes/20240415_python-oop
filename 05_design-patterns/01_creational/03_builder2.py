# Builder Pattern
#
# Allows constructing a complex object step by step, often used for objects
# with many optional components or configurations.

from typing import Protocol


class Computer:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def describe(self) -> str:
        return ", ".join(self.parts)


class ComputerBuilder(Protocol):
    def build(self) -> Computer:
        pass


class MyComputerBuilder(ComputerBuilder):
    def build(self) -> Computer:
        computer = Computer()
        computer.add("Case")
        computer.add("Motherboard")
        computer.add("CPU")
        computer.add("Memory")
        computer.add("Power Supply")
        return computer


# Client code
builder = MyComputerBuilder()
computer = builder.build()
print(
    computer.describe()
)  # Output: Case, Motherboard, CPU, Memory, Power Supply
