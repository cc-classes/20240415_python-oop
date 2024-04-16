from calculator import Calculator
from history import History
from history_custom_object import HistoryCustomObject
from user_input import (
    get_command,
)

from command import (
    is_math_command,
    command_math,
    command_show_history,
    command_remove_history_entry,
    command_clear_history,
    command_save_history,
    command_invalid,
    command_result,
)


class CalcApp:
    __history: History
    __calculator: Calculator

    def __init__(self, history: History, calculator: Calculator):
        self.__history = history
        self.__calculator = calculator

    def run(self) -> None:
        while True:
            command = get_command()

            if is_math_command(command):
                command_math(self.__history, self.__calculator, command)
            elif command == "result":
                command_result(self.__calculator)
            elif command == "history":
                command_show_history(self.__history)
            elif command == "remove":
                command_remove_history_entry(self.__history)
            elif command == "clear":
                command_clear_history(self.__history)
            elif command == "save":
                command_save_history(self.__history)
            elif command == "exit":
                break
            else:
                command_invalid()


if __name__ == "__main__":
    history = HistoryCustomObject()
    # history = HistoryDict()
    calc_app = CalcApp(history, Calculator(history))
    calc_app.run()
