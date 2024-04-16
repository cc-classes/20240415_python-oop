from typing import Iterator
from history_entry import HistoryEntryDict
from history import History


class HistoryDict(History):
    __history_entries: list[HistoryEntryDict]

    def __init__(self) -> None:
        self.__history_entries = []

    def __generate_next_entry_id(self) -> int:
        entry_ids = [entry["id"] for entry in self.__history_entries]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        return next_entry_id

    def append_history_entry(self, op_name: str, op_value: float) -> None:
        self.__history_entries.append(
            {
                "id": self.__generate_next_entry_id(),
                "name": op_name,
                "operand": op_value,
            }
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.__history_entries:
            if entry["id"] == entry_id:
                self.__history_entries.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self.__history_entries.clear()

    def __iter__(self) -> Iterator[HistoryEntryDict]:
        return iter(self.__history_entries)
