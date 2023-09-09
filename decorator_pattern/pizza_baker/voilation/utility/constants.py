from enum import Enum


class PizzaName(Enum):
    MASHROOM_ONION_PIZZA = "mashroom_onion_pizza"
    CHEESE_CORN_PIZZA = "cheese_corn_pizza"


class PizzaBase(Enum):
    WHEAT_BASE = "wheat_base"
    THIN_CRUST_BASE = "thin_crust_base"

class PizzaToppings(Enum):
    MASHRROM = "mashroom"
    CHEESE = "cheese"
    CORN = "corn"
    ONION = "onion"
