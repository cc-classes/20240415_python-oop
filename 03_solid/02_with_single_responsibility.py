class User:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age


class UserReporting:
    def __init__(self, user: User):
        self._user = user

    def get_user_details(self) -> str:
        return f"Name: {self._user.name}, Age: {self._user.age}"

    def get_user_summary(self) -> str:
        return f"Name: {self._user.name}"


class UserDatabase:
    def load_user_from_db(self) -> User:
        return User("Bob", 21)

    def save_user_to_db(self, user: User) -> None:
        # Code to save user data to database
        pass


# Usage
user = User(name="Alice", age=30)
db = UserDatabase()
db.save_user_to_db(user)
reporting = UserReporting(user)
reporting.get_user_details()
