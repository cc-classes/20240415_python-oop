from typing import Iterator, Protocol, Any
from history_entry import HistoryEntryDict


class History(Protocol):
    def append_history_entry(self, op_name: str, op_value: float) -> None:
        pass

    def remove_history_entry(self, entry_id: int) -> None:
        pass

    def clear_history_entries(self) -> None:
        pass

    def __iter__(self) -> Iterator[HistoryEntryDict]:
        pass

    def __next__(self) -> HistoryEntryDict:
        pass
