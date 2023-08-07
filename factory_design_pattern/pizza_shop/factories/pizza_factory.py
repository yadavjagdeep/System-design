from factory_design_pattern.pizza_shop.constants import PizzaName
from factory_design_pattern.pizza_shop.factories.ingredients_factory import IngredientsFactory
from factory_design_pattern.pizza_shop.pizza.margarita_pizza import MargaritaPizza
from factory_design_pattern.pizza_shop.pizza.farmhouse_pizza import FarmHousePizza
from factory_design_pattern.pizza_shop.pizza.fresh_veggie_pizza import FreshVeggiePizza
from factory_design_pattern.pizza_shop.pizza.cheese_n_corn_pizza import CheeseNCornPizza


class PizzaFactory:

    @staticmethod
    def get_pizza(pizza_name: str):
        if pizza_name.lower() == PizzaName.MARGARITA.value:
            return MargaritaPizza(IngredientsFactory.get_ingredients(pizza_name=pizza_name))
        elif pizza_name.lower() == PizzaName.FARMHOUSE.value:
            return FarmHousePizza(IngredientsFactory.get_ingredients(pizza_name=pizza_name))
        elif pizza_name.lower() == PizzaName.CHEESE_N_CORN.value:
            return CheeseNCornPizza(IngredientsFactory.get_ingredients(pizza_name=pizza_name))
        elif pizza_name.lower() == PizzaName.FRESH_VEGGIE.value:
            return FreshVeggiePizza(IngredientsFactory.get_ingredients(pizza_name=pizza_name))
        else:
            raise RuntimeError(f"Unknown pizza {pizza_name} !!!")
