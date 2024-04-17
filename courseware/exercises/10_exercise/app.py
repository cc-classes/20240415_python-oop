from typing import Protocol


class Address(Protocol): ...


class Customer(Protocol):
    billing_address: Address
    mailing_address: Address


class Item(Protocol):
    upc: str
    name: str
    price: float


class Cart(Protocol):
    def add_item(self, item: Item, quantity: int) -> None:
        pass

    def remove_item(self, item: Item, quantity: int) -> None:
        pass

    def update_item(self, item: Item, quantity: int) -> None:
        pass


class Shipper(Protocol):
    def calculate(self, weight: float) -> float:
        pass


class UPSShipper:
    def calculate(self, weight: float) -> float:
        pass


class FedExShipper:
    def calculate(self, weight: float) -> float:
        pass


class Shipping(Protocol):
    def __init__(self, shipper: Shipper) -> None:
        pass

    def add_shipping_address(
        self, id: int, street: str, city: str, state: str, zip_code: str
    ) -> None:
        pass

    def remove_shipping_address(self, id: int) -> None:
        pass

    def notify_shipper(self) -> None:
        pass


class Order:
    customer: Customer
    cart: Cart
    shipping: Shipping
