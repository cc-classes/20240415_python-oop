from typing import TypedDict


class HistoryEntryDict(TypedDict):
    id: int
    name: str
    operand: float


class HistoryEntry:
    __id: int
    __name: str
    __operand: float

    def __init__(self, id: int, name: str, operand: float):
        self.__id = id
        self.__name = name
        self.__operand = operand

    def __str__(self) -> str:
        return f"{self.__id} {self.__name} {self.__operand}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def operand(self) -> float:
        return self.__operand
