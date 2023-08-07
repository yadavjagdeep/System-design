from factory_design_pattern.pizza_shop.ingredients.ingredients_interface import Ingredients
from factory_design_pattern.pizza_shop.pizza_base.flat_bread import FlatBread
from factory_design_pattern.pizza_shop.pizza_sauces.tomato_sauce import TomatoSauce
from factory_design_pattern.pizza_shop.pizza_sauces.salsa import Salsa
from factory_design_pattern.pizza_shop.pizza_toppings.onions import Onions


class MargaritaIngredients(Ingredients):

    def get_base(self):
        return FlatBread()

    def get_toppings(self) -> list:
        return [Onions()]

    def get_sauces(self) -> list:
        return [TomatoSauce(), Salsa()]
