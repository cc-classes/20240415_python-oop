# ClassA is tightly coupled to ClassB, which means that ClassA cannot
# function without ClassB.

# Coupling can be reduced by using an abstract base class or a protocol

# Class A -> Class B

class ClassB:
    def operation(self) -> str:
        return "ClassB operation"


class ClassA:
    def __init__(self) -> None:
        self.class_b = ClassB() # high coupling to a concrete class

    def operation(self) -> str:
        return self.class_b.operation()


# Usage
a = ClassA()
print(a.operation())  # Output: ClassB operation
