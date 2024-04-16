class Printer:
    def print_document(self, document: str) -> None:
        pass

    def scan_document(self, document: str) -> None:
        pass

    def fax_document(self, document: str) -> None:
        pass


class Workstation:
    def __init__(self, printer: Printer) -> None:
        self.printer = printer

    def print(self, document: str) -> None:
        self.printer.print_document(document)


def main() -> None:
    printer = Printer()

    # does printer need scanning and faxing capabilities?
    # how can the interfact segregation principle be applied here?
    workstation = Workstation(printer)
    workstation.print("Document")


if __name__ == "__main__":
    main()
