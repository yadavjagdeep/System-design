from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.pizza_interface import Pizza


class Toppings(Pizza):

    def __init__(self, name: str, cost: float, pizza: Pizza):
        super().__init__(name=name, cost=cost)
        self.pizza = pizza

    def get_name(self):
        return self._name + " " + self.pizza.get_name()

    def get_cost(self):
        return self._cost + self.pizza.get_cost()

