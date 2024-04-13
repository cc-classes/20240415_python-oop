from typing import Protocol

# Consider the following scenario:

# Class A -> (depends on) Class B

# To implement the "D" of SOLID, we can invert the dependency one of two ways:

# Option 1
# Class A <- Class B

# Option 2
# Class A -> ProtocolClass <- Class B

# If you do option 2, the "L" of SOLID comes into play. The concrete class(es)
# implementation must honor the intention of the base class.


class ProtocolClass(Protocol):
    def operation(self) -> str: ...


class ClassB:
    def operation(self) -> str:
        return "ClassB operation"


class ClassA:
    def __init__(self, protocol_class: ProtocolClass):
        self.protocol_class = protocol_class

    def operation(self) -> str:
        return self.protocol_class.operation()


# Usage
b = ClassB()
a = ClassA(b)
print(a.operation())  # Output: ClassB operation
