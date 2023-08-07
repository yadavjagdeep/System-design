from factory_design_pattern.coffee_machine.coffee.coffee_interface import Coffee


class Latte(Coffee):

    def __init__(self, LatteIngredients: object):
        super().__init__(ingredients=LatteIngredients)

    def brew(self):
        print(f"brew {self.__class__.__name__}")

    def boil(self):
        print(f"boil {self.__class__.__name__}")

