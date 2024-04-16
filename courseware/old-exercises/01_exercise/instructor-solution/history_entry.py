class HistoryEntry:

    def __init__(self, id: int, op_name: str, op_value: float):
        self.__id = id
        self.__op_name = op_name
        self.__op_value = op_value

    @property
    def id(self) -> int:
        return self.__id

    @property
    def op_name(self) -> str:
        return self.__op_name

    @property
    def op_value(self) -> float:
        return self.__op_value

