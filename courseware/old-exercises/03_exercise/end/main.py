from typing import Protocol


class Printable(Protocol):
    def print_document(self, document: str) -> None: ...


class Scannable(Protocol):
    def scan_document(self, document: str) -> None: ...


class Faxable(Protocol):
    def fax_document(self, document: str) -> None: ...


class InkJetPrinter:
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")


class MultiFuncPrinter:
    def print_document(self, document: str) -> None:
        print(f"Printing: {document}")

    def scan_document(self, document: str) -> None:
        print(f"Scanning: {document}")

    def fax_document(self, document: str) -> None:
        print(f"Faxing: {document}")


class Workstation:
    def __init__(self, printer: Printable) -> None:
        self.printer = printer

    def print(self, document: str) -> None:
        self.printer.print_document(document)


def main() -> None:
    printer = MultiFuncPrinter()

    # does printer need scanning and faxing capabilities?
    workstation = Workstation(printer)
    workstation.print("Document")


if __name__ == "__main__":
    main()
