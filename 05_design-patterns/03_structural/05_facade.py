# Facade Pattern
#
# Provides a unified interface to a set of interfaces in a subsystem.


class CPU:
    def freeze(self) -> None:
        print("Freezing processor.")

    def jump(self, position: str) -> None:
        print(f"Jumping to position {position}")

    def execute(self) -> None:
        print("Executing instructions.")


class Memory:
    def load(self, position: str, data: str) -> None:
        print(f"Loading data {data} at position {position}")


class HardDrive:
    def read(self, lba: str, size: str) -> str:
        return f"Data from sector {lba} with size {size}"


class ComputerFacade:
    def __init__(self) -> None:
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()

    def start(self) -> None:
        self.cpu.freeze()
        self.memory.load("0x00", self.hd.read("0x00", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


# Client Code
computer = ComputerFacade()
computer.start()
