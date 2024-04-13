# This class has high cohesion, because it does only one thing: it performs
# math operations. Yes, there are multiple math operations but they are all
# math operations.


class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


# Usage
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.multiply(4, 2))  # Output: 8
