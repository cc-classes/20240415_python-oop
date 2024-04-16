from typing import Protocol


class UserInput(Protocol):
    def get_command(self) -> str:
        pass

    def get_entry_id_to_remove(self) -> int:
        pass

    def get_operand(self) -> float:
        pass

    def get_save_file_name(self) -> str:
        pass


class ConsoleInput:
    def get_command(self) -> str:
        return input("Enter a command > ")

    def get_entry_id_to_remove(self) -> int:
        return int(input("Enter an entry id to remove > "))

    def get_operand(self) -> float:
        return float(input("Enter an operand > "))

    def get_save_file_name(self) -> str:
        return input("Enter a file name to save the history to > ")
