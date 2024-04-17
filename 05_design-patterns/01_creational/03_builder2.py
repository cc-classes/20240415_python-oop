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


class MyComputerBuilder:
    def build(self) -> Computer:
        computer = Computer()
        computer.add("Case")
        computer.add("Motherboard")
        computer.add("CPU")
        computer.add("Memory")
        computer.add("Power Supply")
        return computer


# builders return the same object with different configurations, where the
# configurations and/or configuration rules are defined outside of the constructor
class YourComputerBuilder:
    def build(self) -> Computer:
        computer = Computer()
        computer.add("Case")
        computer.add("Motherboard")
        computer.add("CPU")
        computer.add("CPU")
        computer.add("Memory")
        computer.add("Power Supply")
        computer.add("Power Supply")
        return computer


# factory return different implementation of objects at runtime that
# implement the same contract
class ComputeBuilderFactory:
    def create_builder(self, type: str) -> ComputerBuilder:
        if type == "My":
            return MyComputerBuilder()
        elif type == "Your":
            return YourComputerBuilder()
        else:
            raise ValueError("Invalid type.")


# Client code
builder = ComputeBuilderFactory().create_builder("My")
computer = builder.build()
print(
    computer.describe()
)  # Output: Case, Motherboard, CPU, Memory, Power Supply
