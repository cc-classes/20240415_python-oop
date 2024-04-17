from __future__ import annotations
from typing import Optional


class Pizza:
    size: Optional[str]
    crust_type: Optional[str]
    toppings: list[str]
    sauce: Optional[str]
    cheese: Optional[str]

    def __init__(self) -> None:
        self.size = None
        self.crust_type = None
        self.toppings = []
        self.sauce = None
        self.cheese = None


# chain-specific pizza config rules in the builder class not the pizza class


class PizzaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza()

    def set_size(self, size: str) -> PizzaBuilder:
        self.pizza.size = size
        return self

    def set_crust_type(self, crust_type: str) -> PizzaBuilder:
        self.pizza.crust_type = crust_type
        return self

    def add_topping(self, topping: str) -> PizzaBuilder:
        self.pizza.toppings.append(topping)
        return self

    def set_sauce(self, sauce: str) -> PizzaBuilder:
        self.pizza.sauce = sauce
        return self

    def set_cheese(self, cheese: str) -> PizzaBuilder:
        self.pizza.cheese = cheese
        return self  # enables the chain pattern

    def build(self) -> Pizza:
        return self.pizza


# Creating pizza instances using the builder pattern
pizza1 = (
    PizzaBuilder()
    .set_size("large")
    .set_crust_type("thin")
    .add_topping("pepperoni")
    .add_topping("mushrooms")
    .set_sauce("tomato")
    .set_cheese("mozzarella")
    .build()
)
pizza2 = (
    PizzaBuilder()
    .set_size("medium")
    .set_crust_type("thick")
    .add_topping("ham")
    .add_topping("pineapple")
    .set_sauce("bbq")
    .set_cheese("cheddar")
    .build()
)
pizza3 = (
    PizzaBuilder()
    .set_size("small")
    .set_crust_type("regular")
    .add_topping("olives")
    .add_topping("onions")
    .add_topping("peppers")
    .set_sauce("marinara")
    .set_cheese("parmesan")
    .build()
)

print(pizza1.__dict__)
print(pizza2.__dict__)
print(pizza3.__dict__)
