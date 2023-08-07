from factory_design_pattern.pizza_shop.constants import PizzaName
from factory_design_pattern.pizza_shop.ingredients.margarita_ingredients import MargaritaIngredients
from factory_design_pattern.pizza_shop.ingredients.farmhouse_pizza_ingredients import FarmhousePizzaIngredients
from factory_design_pattern.pizza_shop.ingredients.fresh_veggie_pizza_ingredients import FreshVeggiePizzaIngredients
from factory_design_pattern.pizza_shop.ingredients.cheese_n_corn_pizza_ingredients import CheeseNCornPizzaIngredients


class IngredientsFactory:

    @staticmethod
    def get_ingredients(pizza_name: str):
        if pizza_name.lower() == PizzaName.MARGARITA.value:
            return MargaritaIngredients()
        elif pizza_name.lower() == PizzaName.FARMHOUSE.value:
            return FarmhousePizzaIngredients()
        elif pizza_name.lower() == PizzaName.CHEESE_N_CORN.value:
            return CheeseNCornPizzaIngredients()
        elif pizza_name.lower() == PizzaName.FRESH_VEGGIE.value:
            return FreshVeggiePizzaIngredients()
        else:
            raise RuntimeError(f"Unknown pizza {pizza_name} !!!")

