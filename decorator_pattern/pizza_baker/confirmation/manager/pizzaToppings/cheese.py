from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.toppings_interface import Toppings
from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.pizza_interface import Pizza
from decorator_pattern.pizza_baker.confirmation.utility.constants import PizzaToppings


class Cheese(Toppings):

    def __init__(self, pizza: Pizza):
        super().__init__(name=PizzaToppings.CHEESE.value, cost=8, pizza=pizza)
