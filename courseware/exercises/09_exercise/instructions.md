# Exercise 9: Explore Code Coupling

1. Review the following code. Can you find any examples of coupling in the code?

    ```python
    class Address:
        def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
            self.street = street
            self.city = city
            self.state = state
            self.zip_code = zip_code

    class Person:
        def __init__(
          self, first_name: str, last_name: str, street: str,
          city: str, state: str, zip_code: str) -> None:
            self.first_name = first_name
            self.last_name = last_name
            self.address = Address(street, city, state, zip_code)
    ```

2. In this example, the `Person` class is coupled to the `Address` class. Refactor the `Person` class to decouple the `Address` class. Review the in-class examples and select either the abstract class or protocol pattern to decouple the `Person` class from the `Address` class. Make your programming changes in the `end.py` file.
