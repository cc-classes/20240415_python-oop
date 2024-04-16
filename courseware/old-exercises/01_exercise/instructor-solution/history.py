from __future__ import annotations
from typing import Iterator
from history_entry import HistoryEntry


class HistoryIterator:
    def __init__(self, history: list[HistoryEntry], iterator_id: int) -> None:
        self.__iterator_id = iterator_id
        self.__history = history
        self.__current_history_entry_index = -1

    def __next__(self) -> HistoryEntry:
        print(
            f"iterator id: {self.__iterator_id}, "
            f"index: {self.__current_history_entry_index}"
        )
        self.__current_history_entry_index += 1
        if self.__current_history_entry_index >= len(self.__history):
            raise StopIteration()
        else:
            return self.__history[self.__current_history_entry_index]


class History:
    def __init__(self) -> None:
        self.__history: list[HistoryEntry] = []
        self.__iterator_id = 0

    def __generate_next_entry_id(self) -> int:
        entry_ids = [entry.id for entry in self.__history]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        return next_entry_id

    def append_history_entry(self, op_name: str, op_value: float) -> None:
        self.__history.append(
            HistoryEntry(self.__generate_next_entry_id(), op_name, op_value)
        )

    def remove_history_entry(self, entry_id: int) -> None:
        for entry in self.__history:
            if entry.id == entry_id:
                self.__history.remove(entry)
                break

    def clear_entries(self) -> None:
        self.__history.clear()

    @property
    def result(self) -> float:
        the_result: float = 0.0
        for entry in self.__history:
            if entry.op_name == "add":
                the_result += entry.op_value
            elif entry.op_name == "subtract":
                the_result -= entry.op_value
            elif entry.op_name == "multiply":
                the_result *= entry.op_value
            elif entry.op_name == "divide":
                the_result /= entry.op_value
        return the_result

    # simplest option
    # def __iter__(self) -> Iterator[HistoryEntry]:
    #     return iter(self.__history)

    # more complicated, but we control iteration completely
    def __iter__(self) -> HistoryIterator:
        self.__iterator_id += 1
        return HistoryIterator(self.__history, self.__iterator_id)

    # which looks good for controlling, but fails when there
    # are multiple iterators
    # def __iter__(self) -> History:
    #     self.__iterator_id += 1
    #     self.__current_history_entry_index = -1
    #     return self

    # def __next__(self) -> HistoryEntry:
    #     print(
    #         f"iterator id: {self.__iterator_id}, "
    #         f"index: {self.__current_history_entry_index}"
    #     )
    #     self.__current_history_entry_index += 1
    #     if self.__current_history_entry_index >= len(self.__history):
    #         raise StopIteration()
    #     else:
    #         return self.__history[self.__current_history_entry_index]
