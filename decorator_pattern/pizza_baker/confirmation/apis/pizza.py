from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.pizza_interface import Pizza
from decorator_pattern.pizza_baker.confirmation.factory.pizza_factory import PizzaFactory


class PizzaApi:

    def __init__(self, pizza_name: str):
        self.pizza: Pizza = PizzaFactory.get_pizza(pizza_name=pizza_name)

    def get_pizza_name(self):
        return self.pizza.get_name()

    def get_pizza_cost(self):
        return self.pizza.get_cost()
