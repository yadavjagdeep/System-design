from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.pizza_interface import Pizza
from decorator_pattern.pizza_baker.confirmation.utility.constants import PizzaBase


class ThinCrust(Pizza):

    def __init__(self):
        super().__init__(name=PizzaBase.THIN_CRUST.value, cost=7.10)
