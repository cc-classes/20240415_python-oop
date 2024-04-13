# In Python, an iterable is any object capable of returning its members one
# at a time. This is done by implementing the `__iter__()` method which
# returns an iterator object. The iterator object then implements the
# `__next__()` method to get the next value.

# Common examples of iterable objects include lists, tuples, strings, and
# dictionaries. You can iterate over these using a `for` loop.

# For example, when you use a `for` loop to go over a list, Python internally
# uses an iterator to loop over each item in the list.

# In the code you provided, the `CartIterator` class is an iterator because
# it implements the `__next__()` method. However, to make a `Cart` object
# iterable, it would need to implement the `__iter__()` method that returns an
# instance of `CartIterator`.


class Product:
    def __init__(self, id: int, name: str, price: float) -> None:
        self.__id = id
        self.__name = name
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price


# The CartIterator class is used to iterate over the products in the cart
# The __next__ method is required to make the CartIterator object an iterator
class CartIterator:
    def __init__(self, products: list[Product]) -> None:
        self.__products = products
        self.__current_index = -1

    def __next__(self) -> Product:
        self.__current_index += 1
        if self.__current_index >= len(self.__products):
            raise StopIteration()
        else:
            return self.__products[self.__current_index]


class Cart:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def __generate_next_product_id(self) -> int:
        product_ids = [product.id for product in self.__products]

        if len(product_ids) == 0:
            next_product_id = 1
        else:
            next_product_id = max(product_ids) + 1

        return next_product_id

    def add_product(self, product_name: str, product_price: float) -> None:
        self.__products.append(
            Product(
                self.__generate_next_product_id(), product_name, product_price
            )
        )

    def remove_product(self, product_id: int) -> None:
        for product in self.__products:
            if product.id == product_id:
                self.__products.remove(product)
                break

    def empty_cart(self) -> None:
        self.__products.clear()

    @property
    def total(self) -> float:
        return sum([product.price for product in self.__products])

    # The __iter__ method is required to make the Cart object iterable
    def __iter__(self) -> CartIterator:
        return CartIterator(self.__products)


def main() -> None:
    cart = Cart()
    cart.add_product("Apple", 1.0)
    cart.add_product("Banana", 2.0)
    cart.add_product("Orange", 3.0)

    print("Total:", cart.total)

    # The Cart object is iterable because it implements the __iter__ method
    # The CartIterator object is returned by the __iter__ method
    # Returning a new CartIterator object each time the __iter__ method is
    # called allows us to iterate over the products in the cart multiple times

    for product in cart:
        print(f"Product: {product.name}, Price: {product.price}")


if __name__ == "__main__":
    main()
