# Decorator Pattern
#
# Adds new functionality to an object dynamically without altering
# its structure.

from typing import Protocol

class Coffee(Protocol):
    def cost(self) -> float:...

class BlackCoffee:
    def cost(self) -> float:
        return 5

# Decorator Class
class Milk:
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost() + 2
    
# Decorator Class    
class Sugar:
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost() + 1
    

# Client code
coffee = BlackCoffee()
print(coffee.cost())  # Output: 5

milk_coffee = Milk(coffee)
print(milk_coffee.cost())  # Output: 7

sugar_milk_coffee = Sugar(milk_coffee)
print(sugar_milk_coffee.cost())  # Output: 8