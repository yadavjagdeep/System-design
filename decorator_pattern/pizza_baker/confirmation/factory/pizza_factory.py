from decorator_pattern.pizza_baker.confirmation.utility.constants import Pizza
from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.wheat_base_pizza import WheatBase
from decorator_pattern.pizza_baker.confirmation.manager.pizzaBase.thin_crust_pizza import ThinCrust
from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.corn import Corn
from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.onion import Onion
from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.cheese import Cheese
from decorator_pattern.pizza_baker.confirmation.manager.pizzaToppings.mushroom import Mushroom


class PizzaFactory:

    @staticmethod
    def get_pizza(pizza_name: str):
        if pizza_name.lower() == Pizza.MUSHROOM_ONION_PIZZA.value:
            return Mushroom(Onion(WheatBase()))
        elif pizza_name.lower() == Pizza.CHEESE_CORN_PIZZA.value:
            return Cheese(Corn(ThinCrust()))
        else:
            raise RuntimeError(f"Pizza name = {pizza_name} is not known to system !!!")
