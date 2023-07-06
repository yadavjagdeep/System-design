from factory_design_pattern.factories.ingredients import Ingredients
from factory_design_pattern.milk.regular_milk import RegularMilk
from factory_design_pattern.sugar.white_sugar import WhiteSugar
from factory_design_pattern.bean.american_bean import AmericanBean


class LatteIngredients(Ingredients):

    def get_milk(self):
        return RegularMilk()

    def get_sugar(self):
        return WhiteSugar()

    def get_bean(self):
        return AmericanBean()

