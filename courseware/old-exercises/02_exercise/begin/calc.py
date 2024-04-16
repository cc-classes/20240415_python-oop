import sys
from typing import Protocol, Type

from history import History
from user_input import (
    get_command,
)

from command import (
    is_math_command,
    command_math,
    command_show_history,
    command_remove_history_entry,
    command_clear_history,
    command_invalid,
)

class CalcApp(Protocol):

    def __init__(self, history: History):
        ...

    def run(self) -> None:
        ...

class CalcApp1:
    __history: History

    def __init__(self, history: History):
        self.__history = history

    def __about(self) -> None:
        print("Calc App 1 - The calculator of the future!")

    def __quit(self) -> None:
        print("Bye!")
        sys.exit(0)

    def run(self) -> None:
        while True:
            command = get_command()

            if is_math_command(command):
                command_math(self.__history, command)
            elif command == "history":
                command_show_history(self.__history)
            elif command == "remove":
                command_remove_history_entry(self.__history)
            elif command == "clear":
                command_clear_history(self.__history)
            elif command == "about":
                self.__about()
            elif command == "quit":
                self.__quit()
            else:
                command_invalid()


class CalcApp2:
    __history: History

    def __init__(self, history: History):
        self.__history = history

    def __about(self) -> None:
        print("Calc App 2 - The calculator of the future!")

    def __quit(self) -> None:
        print("Bye!")
        sys.exit(0)

    def run(self) -> None:
        while True:
            command = get_command()

            match command:
                case "add" | "subtract" | "multiply" |"divide":
                    command_math(self.__history, command)
                case "history":
                    command_show_history(self.__history)
                case "remove":
                    command_remove_history_entry(self.__history)
                case "clear":
                    command_clear_history(self.__history)
                case "about":
                    self.__about()
                case "quit":
                    self.__quit()
                case _:
                    command_invalid()

# DO NOT MODIFY THIS FUNCTION
def start_app(
    calc_app_class: Type[CalcApp], history_class: Type[History]
) -> None:
    # creating an instance of History
    # creating an instance of CalcApp
    calc_app = calc_app_class(history_class())
    calc_app.run()


if __name__ == "__main__":
    # start_app(CalcApp1, History)
    # where CalcApp2 is the new class
    start_app(CalcApp2, History)