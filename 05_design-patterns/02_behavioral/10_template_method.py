# Template Method Pattern

# Defines the skeleton of an algorithm in a method, deferring some steps to
# subclasses.

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook()

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print(
            "AbstractClass says: But I let subclasses override some operations"
        )

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    def hook(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def hook(self) -> None:
        print("ConcreteClass2 says: Overridden Hook")


# Client Code
print("Same client code can work with different subclasses:")
concrete_class1 = ConcreteClass1()
concrete_class1.template_method()

print("\n")

concrete_class2 = ConcreteClass2()
concrete_class2.template_method()
