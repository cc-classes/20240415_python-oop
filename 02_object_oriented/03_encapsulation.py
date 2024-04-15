class Animal:
    def __init__(self, name: str) -> None:
        # private member (accessible only in the class,
        # not subclasses and
        # not publicly)
        self.__name = name

        # protected member (accessible everywhere, but
        # communicates to other
        # developers that the property is internal use only)
        # typically used when you a member that intended to be
        # internal use
        # but accessible by the subclass
        self._name = name

        # public member (accessible everywhere)
        self.name = name


# animal = Animal("dog")
# print(animal.__name)
# animal.__name = "cat"
# print(animal.__name)


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

        # cannot access this, not even in the
        # subclass
        # print(self.__name)

        # can access in the subclass, but others
        # should not use it
        print(self._name)

        # can access in the subclass and anywhere else
        print(self.name)



animal = Dog("fido")
# print(animal.__name)


# class Person:
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age

#     def get_name(self) -> str:
#         return self.__name

#     def set_name(self, name: str) -> None:
#         self.__name = name

#     def get_age(self) -> int:
#         return self.__age

#     def set_age(self, age: int) -> None:
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Age cannot be negative!")


# # Creating an object of the Person class
# person = Person("John", 30)

# # Accessing the attributes via methods
# print(person.get_name())  # Output: John
# print(person.get_age())  # Output: 30

# # Attempting to set a negative age
# person.set_age(-5)  # Output: Age cannot be negative!
# print(person.get_age())  # Output: 30

# # Attempting to access the private variables directly (will
# # result in an AttributeError)
# # print(person.__age)  # AttributeError: 'Person' object has
# # no attribute '__age'

# # The correct name mangling to access __age would be:
# # Output: 30 (Not recommended to use, as it violates encapsulation)
# # print(person._Person__age)
