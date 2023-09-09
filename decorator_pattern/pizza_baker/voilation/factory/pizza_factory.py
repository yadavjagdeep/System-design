
class PizzaFactory:

    @staticmethod
    def get_pizza(pizza_name: str):
        from decorator_pattern.pizza_baker.voilation.utility.constants import PizzaName
        from decorator_pattern.pizza_baker.voilation.managers.mashroom_onion_pizza import MashroomOnionPizza
        from decorator_pattern.pizza_baker.voilation.managers.cheese_corn_pizza import CheeseCornPizza
        if pizza_name.lower() == PizzaName.MASHROOM_ONION_PIZZA.value:
            return MashroomOnionPizza()
        elif pizza_name.lower() == PizzaName.CHEESE_CORN_PIZZA.value:
            return CheeseCornPizza()
        else:
            raise RuntimeError(f"Pizza name = {pizza_name} is not known to system !!!")
