from pathlib import Path
import json
import yaml


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age}"
    
    def save_to_file(self, file_name: Path) -> None:
        file_name.write_text(json.dumps(self.__dict__))
        #file_name.write_text(yaml.dump(self.__dict__))


def main() -> None:
    person = Person("John", "Doe", 30)
    person.save_to_file(Path("person.yaml"))


if __name__ == "__main__":
    main()