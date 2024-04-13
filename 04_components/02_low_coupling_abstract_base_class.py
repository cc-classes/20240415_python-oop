from abc import ABC, abstractmethod

# abstract class
class BaseClass(ABC):
    @abstractmethod
    def operation(self) -> str:
        return ""

# concrete classes
class ClassB(BaseClass):
    def operation(self) -> str:
        return "ClassB operation"


class ClassA:
    # high coupling to an abstract class
    def __init__(self, base_class: BaseClass):
        self.base_class = base_class

    def operation(self) -> str:
        return self.base_class.operation()


# Usage
b = ClassB()
a = ClassA(b)
print(a.operation())  # Output: ClassB operation
