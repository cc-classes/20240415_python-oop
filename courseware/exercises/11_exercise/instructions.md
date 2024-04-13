# Exercise 11: Builder Pattern

1. Review the following code:

    ```python
    class Pizza:
        def __init__(self, size, crust_type, toppings, sauce, cheese):
            self.size = size
            self.crust_type = crust_type
            self.toppings = toppings
            self.sauce = sauce
            self.cheese = cheese

    pizza1 = Pizza("large", "thin", ["pepperoni", "mushrooms"], "tomato", "mozzarella")
    pizza2 = Pizza("medium", "thick", ["ham", "pineapple"], "bbq", "cheddar")
    pizza3 = Pizza("small", "regular", ["olives", "onions", "peppers"], "marinara", "parmesan")
    ```

2. The `Pizza` class has a constructor that takes five parameters. The `Pizza` class is tightly coupled to the order of the parameters. Refactor the `Pizza` class to use the builder pattern. The `Pizza` class should now have a `PizzaBuilder` class that constructs the `Pizza` object. Make your programming changes in the `end.py` file.
