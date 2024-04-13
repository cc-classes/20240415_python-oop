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