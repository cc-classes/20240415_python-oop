# Command Pattern
#
# Encapsulates a request as an object, allowing for parameterization, queuing
# of requests, and logging of the operations.

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    def execute(self) -> None:
        print("Turn on the light")


class LightOffCommand(Command):
    def execute(self) -> None:
        print("Turn off the light")


class LightSwitch:
    def __init__(self, command: Command):
        self._command = command

    def operate(self) -> None:
        self._command.execute()


# Client code
switch = LightSwitch(LightOnCommand())
switch.operate()  # Output: Turn on the light

switch = LightSwitch(LightOffCommand())
switch.operate()  # Output: Turn off the light
