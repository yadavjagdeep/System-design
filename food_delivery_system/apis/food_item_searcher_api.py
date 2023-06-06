"""
Searcher needs to be generic and should support OCP
Example searcher -> Get only those food items (name matches food_name) AND (mT is mealType) AND (cT in cuisines)

What we can observe is the first entity of the api 'food_name' basis that we will be getting data from db,
others are just filters only

- will fetch data basis matching name and apply filters on top of that

=> Each filter will take a food_item object as inpout and will return T/F
"""

class FoodItemSearcherApi:

    def get_food_item(self, food_name: str, meal_type, cuisine_type: list, star_rating):
        pass

