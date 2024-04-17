from pathlib import Path
from typing import Any, Protocol
import json
import yaml


class SaveToFile(Protocol):
    def save(self, file_name: Path, data: dict[str, Any]) -> None: ...


class SaveToJson:
    def save(self, file_name: Path, data: dict[str, Any]) -> None:
        output = {}
        for key in data:
            if not key.startswith("_"):
                output[key] = data[key]
        file_name.write_text(json.dumps(output))


class SaveToYaml:
    def save(self, file_name: Path, data: dict[str, Any]) -> None:
        file_name.write_text(yaml.dump(data))


class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        save_strategy: SaveToFile,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._save_strategy = save_strategy

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age}"

    def save_to_file(self, file_name: Path) -> None:
        self._save_strategy.save(file_name, self.__dict__)


def main() -> None:
    person = Person("John", "Doe", 30, SaveToJson())
    person.save_to_file(Path("person.json"))


if __name__ == "__main__":
    main()
