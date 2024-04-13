# Exercise 10: Explore Code Cohesion

1. Review the following protocol code. Does the code have high or low cohesion?

    ```python
    class ShoppingCart(Protocol):
        
        def add_item(self, item: int, quantity: int) -> None:
            pass

        def remove_item(self, item: int, quantity: int) -> None:
            pass
        
        def update_item(self, item: int, quantity: int) -> None:
            pass
        
        def add_shipping_address(
                self, id: int, street: str, city: str, state: str, zip_code: str) -> None:
            pass
        
        def remove_shipping_address(self, id: int) -> None:
            pass
    ```

2. The above protocol has low cohesion. Refactor the protocol to have high cohesion (this means creating more protocols). Make your programming changes in the `end.py` file.
