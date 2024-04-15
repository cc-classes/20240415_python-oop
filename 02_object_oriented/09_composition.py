class Processor:
    def __init__(self, model: str) -> None:
        self.model = model

    def execute(self) -> None:
        print(f"Executing tasks using {self.model} processor")


class Memory:
    def __init__(self, capacity: str) -> None:
        self.capacity = capacity

    def load_data(self) -> None:
        print(f"Loading data into {self.capacity} memory")


class Storage:
    def __init__(self, type_: str) -> None:
        self.type = type_

    def store_data(self) -> None:
        print(f"Storing data in {self.type} storage")


class Computer:
    def __init__(self, processor: Processor, memory: Memory, storage: Storage):
        self.processor = processor
        self.memory = memory
        self.storage = storage

    def perform_operations(self) -> None:
        self.processor.execute()
        self.memory.load_data()
        self.storage.store_data()


# Create objects of Processor, Memory, and Storage
processor = Processor("Intel i7")
memory = Memory("16GB")
storage = Storage("SSD")

# Passing objects as parameters to the Computer class
computer = Computer(processor, memory, storage)

# Performing operations
computer.perform_operations()
