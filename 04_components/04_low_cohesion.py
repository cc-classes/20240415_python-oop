# The following class does multiple independent things, which is a sign of
# low cohesion. In this case, the class should be divided into multiple
# independent functions, no class is really needed.
from typing import Protocol


class MiscellaneousClass:
    def add(self, a: int, b: int) -> int:
        return a + b

    def read_file(self, filename: str) -> str:
        with open(filename, "r") as file:
            return file.read()

    def print_message(self, message: str) -> None:
        print(message)


# Usage
misc = MiscellaneousClass()
print(misc.add(5, 3))  # Output: 8
content = misc.read_file("example.txt")  # Assumes that 'example.txt' exists
misc.print_message("This is a message")  # Output: This is a message


# class Order:
#     # Managing data about the order
#     def set_order_id(self) -> None: ...

#     def set_order_recipient(self) -> None: ...

#     def set_order_address(self) -> None: ...

#     def set_order_items(self) -> None: ...

    
# # Managing the order shipping/delivery process
# class OrderDelivery(Protocol):
#     def print_order_shipping_label(self) -> None: ...


# class UberEatsOrderDelivery:
#     def __init__(self, order: Order):
#         self.order = order


#     def print_order_shipping_label(self) -> None: ...

# class DoorDashOrderDelivery:
#     def __init__(self, order: Order):
#         self.order = order


#     def print_order_shipping_label(self) -> None: ...
