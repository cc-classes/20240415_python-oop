from __future__ import annotations
from calculator import Calculator
from history import History
from history_custom_object import HistoryCustomObject
from history_export import HistoryYamlFileExport
from user_input import (
    ConsoleInput,
)
from commands import Commands
from user_output import ConsoleOutput


class CalcAppProxy:
    def add_commands(self, commands: Commands) -> CalcAppProxy:
        self.__commands = commands
        return self

    def run(self) -> None:
        while True:
            command = self.__commands.next_command()

            if self.__commands.is_math_operation(command):
                self.__commands.math(command)
            elif command == "result":
                self.__commands.result()
            elif command == "history":
                self.__commands.show_history()
            elif command == "remove":
                self.__commands.remove_history_entry()
            elif command == "clear":
                self.__commands.clear_history()
            elif command == "save":
                self.__commands.save_history()
            elif command == "exit":
                break
            else:
                self.__commands.invalid()


if __name__ == "__main__":
    history = HistoryCustomObject()
    # history = HistoryDict()
    CalcAppProxy().add_commands(
        Commands(
            history,
            Calculator(history),
            HistoryYamlFileExport("history.yaml"),
            ConsoleInput(),
            ConsoleOutput(),
        )
    ).run()
