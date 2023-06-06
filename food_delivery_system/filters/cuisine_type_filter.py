from abstract_filter_class import FoodItemFilter

class CuisineTypeFilter(FoodItemFilter):

    def __init__(self, cuisine_types: list):
        self.cuisine_types = cuisine_types

    def filter(self, food_item: object) -> bool:
        if not food_item.cuisine_type in self.cuisine_types:
            return False
        return True
