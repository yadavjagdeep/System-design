from decorator_pattern.pizza_baker.confirmation.apis.pizza import PizzaApi


if __name__ == "__main__":
    pizza = PizzaApi(pizza_name="cheese_corn_pizza")
    name = pizza.get_pizza_name()
    print(name)
    cost = pizza.get_pizza_cost()
    print(cost)
