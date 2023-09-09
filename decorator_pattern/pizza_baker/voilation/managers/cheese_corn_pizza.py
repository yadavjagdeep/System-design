from decorator_pattern.pizza_baker.voilation.managers.base_pizza_manager import BasePizza
from decorator_pattern.pizza_baker.voilation.processors.cost_calculator import PizzaCostCalculator
from decorator_pattern.pizza_baker.voilation.utility.constants import PizzaName, PizzaBase, PizzaToppings


class CheeseCornPizza(BasePizza):

    def get_pizza_cost(self):

        pizza_toppings: list = [PizzaToppings.CHEESE.value, PizzaToppings.CORN.value]
        pizza_base: str = PizzaBase.THIN_CRUST_BASE.value
        cost: float = PizzaCostCalculator().get_pizza_cost(pizza_base, pizza_toppings)
        if not cost:
            raise RuntimeError("Failed to get cost !!!")
        return cost

    def get_pizza_name(self):
        return PizzaName.CHEESE_CORN_PIZZA.value
