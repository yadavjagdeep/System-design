from decorator_pattern.pizza_baker.voilation.managers.base_pizza_manager import BasePizza
from decorator_pattern.pizza_baker.voilation.factory.pizza_factory import PizzaFactory


class Pizza:

    def __init__(self, pizza_name: str):
        self.pizza: BasePizza = PizzaFactory.get_pizza(pizza_name=pizza_name)

    def get_cost(self):
        return self.pizza.get_pizza_cost()

    def get_name(self):
        return self.pizza.get_pizza_name()
