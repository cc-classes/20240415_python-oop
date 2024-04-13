# is-a relationship with inheritance

class Person:
    def walk(self) -> None:
        print("walks")


class Parent(Person):
    def care_for_child(self) -> None:
        print("care for child")


class Student(Parent):
    def study(self) -> None:
        print("study for test")


# Create an instance of Child
# student = Student()
# student.walk()  # Output: Grandparent's Heritage
# student.care_for_child()  # Output: Parent's Property
# student.study()  # Output: Child's Property
