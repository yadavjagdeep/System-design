from factory_design_pattern.pizza_shop.ingredients.ingredients_interface import Ingredients
from factory_design_pattern.pizza_shop.pizza_base.flat_bread import FlatBread
from factory_design_pattern.pizza_shop.pizza_toppings.onions import Onions
from factory_design_pattern.pizza_shop.pizza_toppings.cheese import Cheese
from factory_design_pattern.pizza_shop.pizza_toppings.pepperoni import Pepperoni
from factory_design_pattern.pizza_shop.pizza_sauces.tomato_sauce import TomatoSauce
from factory_design_pattern.pizza_shop.pizza_sauces.white_sauce import WhiteSauce
from factory_design_pattern.pizza_shop.pizza_sauces.sweet_pizza_sauce import SweetSauce


class CheeseNCornPizzaIngredients(Ingredients):

    def get_base(self):
        return FlatBread()

    def get_toppings(self) -> list:
        return [Onions(), Cheese(), Pepperoni()]

    def get_sauces(self) -> list:
        return [TomatoSauce(), WhiteSauce(), SweetSauce()]
