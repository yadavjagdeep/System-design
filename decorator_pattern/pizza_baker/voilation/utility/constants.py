from enum import Enum


class PizzaName(Enum):
    MUSHROOM_ONION_PIZZA = "mushroom_onion_pizza"
    CHEESE_CORN_PIZZA = "cheese_corn_pizza"


class PizzaBase(Enum):
    WHEAT_BASE = "wheat_base"
    THIN_CRUST_BASE = "thin_crust_base"


class PizzaToppings(Enum):
    MUSHROOM = "mushroom"
    CHEESE = "cheese"
    CORN = "corn"
    ONION = "onion"
