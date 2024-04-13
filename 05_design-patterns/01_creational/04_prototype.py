# Prototype Pattern
#
# Create new objects by copying an existing object, known as the prototype.

from typing import Any
import copy


class Prototype:
    def clone(self) -> Any:
        return copy.deepcopy(self)


class Car(Prototype):
    def __init__(self, model: str, color: str) -> None:
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return f"Car model: {self.model}, color: {self.color}"


# Client code
original_car = Car("Model S", "Red")
cloned_car = original_car.clone()
cloned_car.color = "Blue"

print(original_car)  # Output: Car model: Model S, color: Red
print(cloned_car)  # Output: Car model: Model S, color: Blue
