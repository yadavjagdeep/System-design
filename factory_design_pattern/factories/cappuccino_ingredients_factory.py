from factory_design_pattern.factories.ingredients import Ingredients
from factory_design_pattern.milk.cow_milk import CowMilk
from factory_design_pattern.sugar.brown_sugar import BrownSugar
from factory_design_pattern.bean.american_bean import AmericanBean


class CappuccinoIngredients(Ingredients):

    def get_milk(self):
        return CowMilk()

    def get_sugar(self):
        return BrownSugar()

    def get_bean(self):
        return AmericanBean()
