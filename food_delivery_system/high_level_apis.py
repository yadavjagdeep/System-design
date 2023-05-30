"""
Some of the high-level APIS we can think of are:

1. searchFoodItem(food_name: str, filters: list) -> list[food_items]
2. searchRestaurants(restaurant_name: str, filters: list)-> list[restaurants]
3. getRestaurantsById(restaurant_id: uuid) -> restaurant
4. getFoodById(food_id: uuid) -> food
5. updateOrderStatus(order_id: uuid, status: str)
6. addToCart(user_token, food_id)
7. placeOrderApi(token, payment_mode, payment_info)

"""