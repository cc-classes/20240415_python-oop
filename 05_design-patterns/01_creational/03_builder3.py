from __future__ import annotations
from typing import Protocol


class Validator(Protocol):
    def validate(self) -> bool:
        pass


class RequiredValidator:
    def validate(self) -> bool:
        return True


class MinValueValidator:
    def __init__(self, min_value: int) -> None:
        self.min_value = min_value

    def validate(self) -> bool:
        return True


class MaxValueValidator:
    def __init__(self, max_value: int) -> None:
        self.max_value = max_value

    def validate(self) -> bool:
        return True


class InputField:
    validators: list[Validator]

    def __init__(self, name: str) -> None:
        self.name = name
        self.validators = []

    def add_validators(self, validators: list[Validator]) -> None:
        self.validators.extend(validators)


class ValidationBuilder:
    validators: list[Validator]

    def __init__(self, input_field: InputField) -> None:
        self.input_field = input_field
        self.validators = []

    def add_required(self) -> ValidationBuilder:
        self.validators.append(RequiredValidator())
        return self

    def add_min_value(self, min_value: int) -> ValidationBuilder:
        self.validators.append(MinValueValidator(min_value))
        return self

    def add_max_value(self, max_value: int) -> ValidationBuilder:
        self.validators.append(MaxValueValidator(max_value))
        return self

    def build(self) -> InputField:
        self.input_field.add_validators(self.validators)
        return self.input_field


input = (
    ValidationBuilder(InputField("age"))
        .add_required().add_min_value(18).build() # chain pattern
)

print(input)
