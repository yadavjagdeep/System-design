from factory_design_pattern.coffee_machine.factories.ingredients import Ingredients
from factory_design_pattern.coffee_machine.milk.cow_milk import CowMilk
from factory_design_pattern.coffee_machine.sugar.brown_sugar import BrownSugar
from factory_design_pattern.coffee_machine.bean.american_bean import AmericanBean


class CappuccinoIngredients(Ingredients):

    def get_milk(self):
        return CowMilk()

    def get_sugar(self):
        return BrownSugar()

    def get_bean(self):
        return AmericanBean()
