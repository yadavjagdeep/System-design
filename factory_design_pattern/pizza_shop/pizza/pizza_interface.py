from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self, ingredients: object):
        self.pizza_base = ingredients.get_base()
        self.pizza_topping = ingredients.get_topping()
        self.pizza_sauces = ingredients.get_sauces()

    @abstractmethod
    def bake_pizza(self):
        raise NotImplementedError("subclass must implement bake_pizza method !!!")

