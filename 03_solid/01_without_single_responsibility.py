class UserHandler:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_user_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"
    
    def get_user_summary(self) -> str:
        return f"Name: {self.name}"

    def load_user_from_db(self) -> None:
        pass

    def save_user_to_db(self) -> None:
        # Code to save user data to database
        pass
