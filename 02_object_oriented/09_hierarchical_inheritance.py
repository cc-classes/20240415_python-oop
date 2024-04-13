class Parent:
    def family_name(self) -> None:
        print("Smith")


class Daughter(Parent):
    def first_name(self) -> None:
        print("Emma")


class Son(Parent):
    def first_name(self) -> None:
        print("John")


# Create instances
daughter = Daughter()
son = Son()

daughter.family_name()  # Output: Smith
daughter.first_name()  # Output: Emma

son.family_name()  # Output: Smith
son.first_name()  # Output: John
