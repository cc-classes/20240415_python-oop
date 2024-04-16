from typing import Iterator
from history_entry import HistoryEntry


class History:
    _history_entries: list[HistoryEntry]

    def __init__(self, math_ops: dict[str, Any]) -> None:
        self._history_entries = []
        self.__math_ops = math_ops

    def calculate_result_from_history(self) -> float:
        result = 0.0

        for entry in self._history_entries:
            result = self.__math_ops[entry.name](result, entry.operand)

        return result

    def _generate_next_entry_id(self) -> int:
        entry_ids = [entry.id for entry in self._history_entries]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        return next_entry_id

    def append_history_entry(self, op_name: str, op_value: float) -> None:
        self._history_entries.append(
            HistoryEntry(self._generate_next_entry_id(), op_name, op_value)
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self._history_entries:
            if entry.id == entry_id:
                self._history_entries.remove(entry)
                break

    def clear_history_entries(self) -> None:
        self._history_entries.clear()

    def __iter__(self) -> Iterator[HistoryEntry]:
        return iter(self._history_entries)
