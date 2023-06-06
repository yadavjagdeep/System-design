from abstract_filter_class import FoodItemFilter

class StarRatingBasedFilter(FoodItemFilter):

    def __init__(self, star_rating: object):
        self.star_rating = star_rating

    def filter(self, food_item: object) -> bool:
        if not food_item.star_rating.value >= self.star_rating.value:
            return False
        return True

