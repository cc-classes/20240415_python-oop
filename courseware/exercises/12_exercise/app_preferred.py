from pathlib import Path
from typing import Any, Protocol
import json
import yaml


class SaveToFile(Protocol):
    def save(self, data: dict[str, Any]) -> None: ...


class SaveToJson:
    def __init__(self, file_name: Path):
        self.file_name = file_name

    def save(self, data: dict[str, Any]) -> None:
        self.file_name.write_text(json.dumps(data))


class SaveToYaml:
    def __init__(self, file_name: Path):
        self.file_name = file_name

    def save(self, data: dict[str, Any]) -> None:
        self.file_name.write_text(yaml.dump(data))


class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age}"

    def save_to_file(self, save_to_file: SaveToFile) -> None:
        save_to_file.save(self.__dict__)


def main() -> None:
    person = Person("John", "Doe", 30)
    person.save_to_file(SaveToJson(Path("person.json")))
    person.save_to_file(SaveToYaml(Path("person.json")))


if __name__ == "__main__":
    main()
