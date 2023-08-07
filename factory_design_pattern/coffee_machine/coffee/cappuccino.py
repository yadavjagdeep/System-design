from factory_design_pattern.coffee_machine.coffee.coffee_interface import Coffee


class Cappuccino(Coffee):

    def __init__(self, CappuccinoIngredients: object):
        super().__init__(ingredients=CappuccinoIngredients)

    def brew(self):
        print(f"brew {self.__class__.__name__}")

    def boil(self):
        print(f"boil {self.__class__.__name__}")

