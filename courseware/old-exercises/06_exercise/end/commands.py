from calculator import Calculator
from history import History
from history_export import HistoryExport
from user_input import UserInput
from user_output import UserOutput


class Commands:
    def __init__(
        self,
        history: History,
        calculator: Calculator,
        history_export: HistoryExport,
        user_input: UserInput,
        user_output: UserOutput,
    ):
        self._history = history
        self._calculator = calculator
        self._history_export = history_export
        self._user_output = user_output
        self._user_input = user_input

    def next_command(self) -> str:
        return self._user_input.get_command()

    def math(self, op_name: str) -> None:
        operand = self._user_input.get_operand()
        self._history.append_history_entry(op_name, operand)
        self._user_output.put_result(self._calculator.result())

    def result(
        self,
    ) -> None:
        self._user_output.put_result(self._calculator.result())
        self._user_output.put_operation_count(
            self._calculator.operation_count()
        )

    def show_history(self) -> None:
        for entry in self._history:
            self._user_output.put_history_entry(entry)

    def remove_history_entry(self) -> None:
        self._history.remove_history_entry(
            self._user_input.get_entry_id_to_remove()
        )

    def clear_history(self) -> None:
        self._history.clear_history_entries()

    def save_history(self) -> None:
        self._history_export.save(self._history)

    def invalid(self) -> None:
        self._user_output.put_invalid_command()

    def is_math_operation(self, command: str) -> bool:
        return command in ["add", "subtract", "multiply", "divide"]
