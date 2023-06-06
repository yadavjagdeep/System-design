
class FoodItemSearcher:

    def search(self, food_item_name, filters: list[object]):
        if not food_item_name:
            raise Exception("Food item cannot be null")

        data_access_result = DataAccessor.get_food_item_with_name(food_item_name)
        food_items: list = DataAccessObjectConvertor.convert_to_food_items(data_access_result)
        for _filter in filters:
            filtered_food_item = []
            for _food_item in food_items:
                if _filter.filter(_food_item):
                    filtered_food_item.append(_food_item)
            food_items = filtered_food_item

        return food_items

