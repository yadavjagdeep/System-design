class FoodItem:
    # TODO: Will use builder-pattern here
    def __init__(self, food_id: int,
                 name: str,
                 description: str,
                 price_inr: float,
                 meal_type: object,
                 cuisine_type: object,
                 restaurant_id: int,
                 is_available: bool):
        self.food_id = food_id
        self.name = name
        self.description = description
        self.price_inr = price_inr
        self.meal_type = meal_type
        self.cuisine_type = cuisine_type
        self.restaurant_id = restaurant_id
        self.is_available = is_available




