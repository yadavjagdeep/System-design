from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.toppings_interface import Toppings
from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.pizza_interface import Pizza
from decorator_pattern.pizza_baker.confirmation.utility.constants import PizzaToppings


class Corn(Toppings):

    def __init__(self, pizza: Pizza):
        super().__init__(name=PizzaToppings.CORN.value, cost=4, pizza=pizza)
