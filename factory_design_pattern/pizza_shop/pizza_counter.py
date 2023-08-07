from factory_design_pattern.pizza_shop.factories.pizza_factory import PizzaFactory


class PizzaCounter:

    def __init__(self, pizza_name: str):
        self.pizza = PizzaFactory.get_pizza(pizza_name=pizza_name)

    def bake(self):
        self.pizza.bake_pizza()

