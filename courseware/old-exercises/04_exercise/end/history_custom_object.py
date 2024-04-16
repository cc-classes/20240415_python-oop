from typing import Iterator

from history import History
from history_entry import HistoryEntry, HistoryEntryDict


class HistoryCustomObject(History):
    __history_entries: list[HistoryEntry]

    def __init__(self) -> None:
        self.__history_entries = []

    def calculate_result_from_history(self) -> float:
        result = 0.0

        for entry in self.__history_entries:
            if entry.name == "add":
                result += entry.operand
            elif entry.name == "subtract":
                result -= entry.operand
            elif entry.name == "multiply":
                result *= entry.operand
            elif entry.name == "divide":
                result /= entry.operand

        return result

    def __generate_next_entry_id(self) -> int:
        entry_ids = [entry.id for entry in self.__history_entries]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        return next_entry_id

    def append_history_entry(self, op_name: str, op_value: float) -> None:
        self.__history_entries.append(
            HistoryEntry(self.__generate_next_entry_id(), op_name, op_value)
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.__history_entries:
            if entry.id == entry_id:
                self.__history_entries.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self.__history_entries.clear()

    def __iter__(self) -> Iterator[HistoryEntryDict]:
        entries: list[HistoryEntryDict] = []

        for history_entry in self.__history_entries:
            entry: HistoryEntryDict = {
                "id": history_entry.id,
                "name": history_entry.name,
                "operand": history_entry.operand,
            }
            entries.append(entry)

        return iter(entries)
    
    def save_file

