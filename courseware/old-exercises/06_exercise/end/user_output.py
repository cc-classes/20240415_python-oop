from typing import Protocol

from history_entry import HistoryEntryDict


class UserOutput(Protocol):
    def put_result(self, result: float) -> None:
        pass

    def put_operation_count(self, operation_count: int) -> None:
        pass

    def put_invalid_command(self) -> None:
        pass

    def put_history_entry(self, entry: HistoryEntryDict) -> None:
        pass


class ConsoleOutput:
    def put_result(self, result: float) -> None:
        print(f"Result: {result}")

    def put_operation_count(self, operation_count: int) -> None:
        print(f"Operation Count: {operation_count}")

    def put_invalid_command(self) -> None:
        print("Invalid command. Please try again.")

    def put_history_entry(self, entry: HistoryEntryDict) -> None:
        print(entry)
