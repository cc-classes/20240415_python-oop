# Builder Pattern
#
# Allows constructing a complex object step by step, often used for objects
# with many optional components or configurations.


class Computer:
    cpu: str
    memory: str
    drive: str

    def __init__(self, cpu: str, memory: str, drive: str) -> None:
        self.cpu = cpu
        self.memory = memory
        self.drive = drive

    def describe(self) -> str:
        return f"{self.cpu}, {self.memory}, {self.drive}"


class ComputerBuilder:
    cpu: str
    memory: str
    drive: str

    def __init__(self) -> None:
        self.cpu = "arm64"
        self.memory = "16gb"
        self.drive = "100GB"

    def add_cpu(self, cpu: str) -> None:
        if cpu == "x64":
            self.memory = "64gb"
        self.cpu = f"cpu: {cpu}"

    def add_memory(self, memory: str) -> None:
        self.memory = f"memory: {memory}"

    def add_drive(self, drive: str) -> None:
        self.drive = f"drive: {drive}"

    def build(self) -> Computer:
        return Computer(self.cpu, self.memory, self.drive)


# # Client code
builder = ComputerBuilder()
builder.add_cpu("x64")
builder.add_drive("1TB")
computer = builder.build()

print(computer.describe())  # Output: cpu: x64, memory: 32gb, drive: 100GB
