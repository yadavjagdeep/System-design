from factory_design_pattern.pizza_shop.ingredients.ingredients_interface import Ingredients
from factory_design_pattern.pizza_shop.pizza_base.flat_bread import FlatBread
from factory_design_pattern.pizza_shop.pizza_toppings.mushroom import Mushroom
from factory_design_pattern.pizza_shop.pizza_toppings.onions import Onions
from factory_design_pattern.pizza_shop.pizza_sauces.tomato_sauce import TomatoSauce
from factory_design_pattern.pizza_shop.pizza_sauces.sweet_pizza_sauce import SweetSauce
from factory_design_pattern.pizza_shop.pizza_sauces.white_sauce import WhiteSauce


class FarmhousePizzaIngredients(Ingredients):

    def get_base(self):
        return FlatBread()

    def get_toppings(self) -> list:
        return [Onions(), Mushroom()]

    def get_sauces(self) -> list:
        return [TomatoSauce(), SweetSauce(), WhiteSauce()]
