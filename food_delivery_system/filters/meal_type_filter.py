from abstract_filter_class import FoodItemFilter

class MealTypeFilter(FoodItemFilter):

    def __init__(self, meal_type):
        self.meal_type = meal_type

    def filter(self, food_item) -> bool:
        if not food_item.meal_type == self.meal_type:
            return False
        return True

