from enum import Enum


class PizzaBase(Enum):
    WHEAT_BASE = "wheat_base"
    THIN_CRUST = "thin_crust"


class PizzaToppings(Enum):
    MUSHROOM = ""
    ONION = "onion"
    CHEESE = "cheese"
    OLIVE = "olive"
    CORN = "corn"


class Pizza(Enum):
    MUSHROOM_ONION_PIZZA = "mushroom_onion_pizza"
    CHEESE_CORN_PIZZA = "cheese_corn_pizza"
