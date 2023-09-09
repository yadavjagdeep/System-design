from decorator_pattern.pizza_baker.voilation.managers.base_pizza_manager import BasePizza
from decorator_pattern.pizza_baker.voilation.processors.cost_calculator import PizzaCostCalculator
from decorator_pattern.pizza_baker.voilation.utility.constants import PizzaName, PizzaBase, PizzaToppings


class MushroomOnionPizza(BasePizza):

    def get_pizza_cost(self):

        pizza_toppings: list = [PizzaToppings.MUSHROOM.value, PizzaToppings.ONION.value]
        pizza_base: str = PizzaBase.WHEAT_BASE.value
        cost: float = PizzaCostCalculator().get_pizza_cost(pizza_base, pizza_toppings)
        if not cost:
            raise RuntimeError("Failed to get cost !!!")
        return cost

    def get_pizza_name(self):
        return PizzaName.MUSHROOM_ONION_PIZZA.value
