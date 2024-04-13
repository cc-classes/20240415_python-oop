# Object-Oriented Python Programming Course

## Single Responsibility Principle

The Single Responsibility Principle (SRP), one of the SOLID principles, posits that a class should have only one reason to change, meaning it should only have one job or responsibility. Adhering to this principle makes the code more robust, maintainable, and scalable. It is easier to manage the codebase when classes are small and focused on a single concern.

## Why Use SRP?

- Simplifies code maintenance by isolating changes to one class.
- Enhances code readability by keeping classes small and focused.
- Promotes code reuse by creating highly cohesive and loosely coupled classes.

## SRP Example

Consider a scenario where you have a class that handles user information and also manages user data storage in a database.

### Without Applying SRP:

```python
class UserHandler:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_user_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def save_user_to_db(self):
        # Code to save user data to database
        pass
```

In the above example, the `UserHandler` class has two responsibilities: managing user information and handling the database storage for the user. This violates the SRP because the class has more than one reason to change (change in user data handling and change in database management).

### Applying SRP:

To adhere to the Single Responsibility Principle, you can separate the database handling and user data management into two different classes:

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_user_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Database:
    def save_user_to_db(self, user: User):
        # Code to save user data to database
        pass


# Usage
user = User(name="Alice", age=30)
db = Database()
db.save_user_to_db(user)
```

In this refactored code:

- The `User` class is only responsible for managing user information.
- The `Database` class handles the database operations.
- Each class now has a single responsibility, adhering to the SRP.

By ensuring that each class has only one responsibility, you make the code more modular, understandable, and maintainable, which is the essence of the Single Responsibility Principle.