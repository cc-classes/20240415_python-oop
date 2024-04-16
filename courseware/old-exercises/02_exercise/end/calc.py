import sys
from typing import Type
from abc import ABC, abstractmethod

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

class CalcApp(ABC):
    _history: History

    def __init__(self, history: History):
        self._history = history

    def about(self) -> None:
        print("Calc App - The calculator of the future!")

    def quit(self) -> None:
        print("Bye!")
        sys.exit(0)

    @abstractmethod
    def run(self) -> None:
        ...



class CalcAppIf(CalcApp):

    def run(self) -> None:
        while True:
            command = get_command()

            if is_math_command(command):
                command_math(self._history, command)
            elif command == "history":
                command_show_history(self._history)
            elif command == "remove":
                command_remove_history_entry(self._history)
            elif command == "clear":
                command_clear_history(self._history)
            elif command == "about":
                self.about()
            elif command == "quit":
                self.quit()
            else:
                command_invalid()


class CalcAppMatch(CalcApp):

    def run(self) -> None:
        while True:

            command = get_command()

            match command:
                case "add" | "subtract" | "multiply" |"divide":
                    command_math(self._history, command)
                case "history":
                    command_show_history(self._history)
                case "remove":
                    command_remove_history_entry(self._history)
                case "clear":
                    command_clear_history(self._history)
                case "about":
                    self.about()
                case "quit":
                    self.quit()
                case _:
                    command_invalid()


# DO NOT MODIFY THIS FUNCTION
def start_app(
    calc_app_class: Type[CalcApp], history_class: [Type[History]]
) -> None:
    calc_app = calc_app_class(history_class())
    calc_app.run()


if __name__ == "__main__":
    start_app(CalcAppMatch, History)
    # where CalcApp2 is the new class
    # start_app(CalcApp2, History)
