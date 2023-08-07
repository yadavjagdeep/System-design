from factory_design_pattern.pizza_shop.pizza.pizza_interface import Pizza


class MargaritaPizza(Pizza):

    def __init__(self, ingredients: object):
        self.ingredients = super().__init__(ingredients=ingredients)

    def bake_pizza(self):
        print(f"Baking {self.__class__.__name__} pizza !!!")

