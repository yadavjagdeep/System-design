from factory_design_pattern.pizza_shop.constants import PizzaName


class IngredientsFactory:

    @staticmethod
    def get_ingredients(pizza_name: str):
        if pizza_name.lower() == PizzaName.MARGARITA.value:
            pass
        elif pizza_name.lower() == PizzaName.FARMHOUSE.value:
            pass
        elif pizza_name.lower() == PizzaName.CHEESE_N_CORN.value:
            pass
        elif pizza_name.lower() == PizzaName.FRESH_VEGGIE.value:
            pass
        else:
            raise RuntimeError(f"Unknown pizza {pizza_name} !!!")

