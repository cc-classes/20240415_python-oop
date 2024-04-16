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


class CalcApp:
    __history: History

    def __init__(self, history: History) -> None:
        self.__history = history

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
            elif command == "exit":
                break
            else:
                command_invalid()


if __name__ == "__main__":
    calc_app = CalcApp(History())
    calc_app.run()
