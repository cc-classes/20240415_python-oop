from history import History


class Calculator:
    def __init__(self, history: History):
        self._history = history

    def result(self) -> float:
        result = 0.0

        for entry in self._history:
            if entry["name"] == "add":
                result += entry["operand"]
            elif entry["name"] == "subtract":
                result -= entry["operand"]
            elif entry["name"] == "multiply":
                result *= entry["operand"]
            elif entry["name"] == "divide":
                result /= entry["operand"]

        return result

    def operation_count(self) -> int:
        return len(list(self._history))
