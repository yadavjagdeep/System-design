from factory_design_pattern.coffee_machine.factories.ingredients import Ingredients
from factory_design_pattern.coffee_machine.milk.powder_milk import PowderMilk
from factory_design_pattern.coffee_machine.sugar.brown_sugar import BrownSugar
from factory_design_pattern.coffee_machine.bean.indian_baen import IndianBean


class RobustaIngredients(Ingredients):

    def get_milk(self):
        return PowderMilk()

    def get_sugar(self):
        return BrownSugar()

    def get_bean(self):
        return IndianBean()
