from factory_design_pattern.pizza_shop.ingredients.ingredients_interface import Ingredients
from factory_design_pattern.pizza_shop.pizza_base.pitta_bread import PittaBread
from factory_design_pattern.pizza_shop.pizza_toppings.pepperoni import Pepperoni
from factory_design_pattern.pizza_shop.pizza_toppings.mushroom import Mushroom
from factory_design_pattern.pizza_shop.pizza_toppings.cheese import Cheese
from factory_design_pattern.pizza_shop.pizza_toppings.onions import Onions
from factory_design_pattern.pizza_shop.pizza_sauces.sweet_pizza_sauce import SweetSauce
from factory_design_pattern.pizza_shop.pizza_sauces.tomato_sauce import TomatoSauce
from factory_design_pattern.pizza_shop.pizza_sauces.white_sauce import WhiteSauce


class FreshVeggiePizzaIngredients(Ingredients):

    def get_base(self):
        return PittaBread()

    def get_toppings(self) -> list:
        return [Onions(), Cheese(), Pepperoni(), Mushroom()]

    def get_sauces(self) -> list:
        return [TomatoSauce(), SweetSauce(), WhiteSauce()]
