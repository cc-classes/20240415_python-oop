# Interpreter Pattern
#
# Defines a representation for its grammar along with an interpreter that
# uses the representation to interpret sentences in the language.

from typing import Any, Protocol


class Expression(Protocol):
    def interpret(self, context: dict[Any, Any]) -> float:
        pass


class Number(Expression):
    def __init__(self, value: float):
        self._value = value

    def interpret(self, context: dict[Any, Any]) -> float:
        return self._value


class Plus(Expression):
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: dict[Any, Any]) -> float:
        return self._left.interpret(context) + self._right.interpret(context)


class Minus(Expression):
    def __init__(self, left: Expression, right: Expression):
        self._left = left
        self._right = right

    def interpret(self, context: dict[Any, Any]) -> float:
        return self._left.interpret(context) - self._right.interpret(context)


# Client Code

# The context dictionary is likely being used to store information that is
# relevant to the current context of the program. This could include
# variables, functions, or other data that is needed to execute the program.
# By using a dictionary, the program can easily access and modify this
# information as needed.
# In this example, the context dictionary is not being used only shown
context: dict[Any, Any] = {}

expression = Plus(Number(3), Minus(Number(2), Number(1)))
print(expression.interpret(context))  # Output: 4
