from factory_design_pattern.coffee.coffee_interface import Coffee


class Robusta(Coffee):

    def __init__(self, RobustaIngredients: object):
        super().__init__(ingredients=RobustaIngredients)

    def brew(self):
        print(f"brew {self.__class__.__name__}")

    def boil(self):
        print(f"boil {self.__class__.__name__}")


