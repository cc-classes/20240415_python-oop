from typing import Protocol


class ShoppingCart(Protocol):
    def add_item(self, item: int, quantity: int) -> None:
        pass

    def remove_item(self, item: int, quantity: int) -> None:
        pass

    def update_item(self, item: int, quantity: int) -> None:
        pass

    def add_shipping_address(
        self, id: int, street: str, city: str, state: str, zip_code: str
    ) -> None:
        pass

    def remove_shipping_address(self, id: int) -> None:
        pass
