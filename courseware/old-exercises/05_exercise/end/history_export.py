from typing import Protocol
from abc import ABC, abstractmethod
from history import History


class HistoryExport(Protocol):
    def save(self, history: History) -> None:
        ...


class HistoryFileExport(ABC, HistoryExport):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @abstractmethod
    def save(self, history: History) -> None:
        ...


class HistoryJsonFileExport(HistoryFileExport):
    def __init__(self, file_name: str, indent: int = 2) -> None:
        super().__init__(file_name)
        self.indent = indent

    def save(self, history: History) -> None:
        import json

        with open(self.file_name, "w", encoding="UTF-8") as entries_json_file:
            json.dump(list(history), entries_json_file, indent=self.indent)


class HistoryCsvFileExport(HistoryFileExport):
    def __init__(self, file_name: str, doublequote: bool = False) -> None:
        super().__init__(file_name)
        self.doublequote = doublequote

    def save(self, history: History) -> None:
        import csv

        with open(self.file_name, "w", encoding="UTF-8") as entries_csv_file:
            fieldnames = [
                "id",
                "name",
                "operand",
            ]
            writer = csv.DictWriter(
                entries_csv_file,
                fieldnames=fieldnames,
                doublequote=self.doublequote,
            )

            writer.writeheader()
            for entry in history:
                writer.writerow(entry)


class HistoryYamlFileExport(HistoryFileExport):
    def save(self, history: History) -> None:
        import yaml

        with open(self.file_name, "w", encoding="UTF-8") as entries_yaml_file:
            yaml.dump(list(history))
            entries_yaml_file.write(yaml.dump(list(history)))
