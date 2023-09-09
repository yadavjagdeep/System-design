from decorator_pattern.pizza_baker.voilation.managers.db_manager.db_accessor import DBAccessor

class PizzaCostCalculator:

    def get_pizza_cost(self, pizza_base: str, pizza_toppings: list[str], additional_cost=None) -> float:
        cost = 0.0
        cost += DBAccessor.get_pizza_base_cost(pizza_base_name=pizza_base)

        for topping in pizza_toppings:
            cost += DBAccessor.get_cost_of_toppings(topping_name=topping)

        if additional_cost:
            cost += additional_cost
        return cost

