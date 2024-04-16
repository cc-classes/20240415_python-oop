class HistoryEntry:
    _id: int
    _name: str
    _operand: float

    def __init__(self, id: int, name: str, operand: float):
        self._id = id
        self._name = name
        self._operand = operand

    def __str__(self) -> str:
        return f"{self._id} {self._name} {self._operand}"

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def operand(self) -> float:
        return self._operand