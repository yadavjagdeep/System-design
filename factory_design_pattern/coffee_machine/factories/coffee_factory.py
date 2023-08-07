from factory_design_pattern.coffee_machine.coffee.cofee_type import CoffeeName
from factory_design_pattern.coffee_machine.coffee.cappuccino import Cappuccino
from factory_design_pattern.coffee_machine.coffee.latte import Latte
from factory_design_pattern.coffee_machine.coffee.robusta import Robusta

# class CoffeeFactory:
#
#     @staticmethod
#     def get_coffee(coffee_name: str):
#         if coffee_name.lower() == CoffeeName.CAPPUCCINO.value:
#             return Cappuccino(milk=CowMilk(), sugar=BrownSugar(), bean=AmericanBean())
#         elif coffee_name.lower() == CoffeeName.LATTE.value:
#             return Latte(milk=RegularMilk(), sugar=WhiteSugar(), bean=AmericanBean())
#         elif coffee_name.lower() == CoffeeName.ROBUSTA.value:
#             return Robusta(milk=CowMilk(), sugar=BrownSugar(), bean=IndianBean())
#         else:
#             raise Exception(f"Invalid coffee type = {coffee_name} !!!")


"""
This is a factory design patter on basic level
- One thing to note here is the coffee factory needs to know about a lot of concreate classes, eg. CowMilk, BrownSugar

- The coffee server class depends on coffee factory to get coffee object and coffee factory depends on a lot of concrete 
    classes.
- The coffee factory depends upon CowMilk, BrownSugar etc.

=> What we can see here is a Top-level entity is depending on low level entity, that violates dependency inversion 
    principle.

-> The top level dependency of coffee-sever on coffee factory can be ignored as it makes our life easier, but 
    dependence of coffee factory on a number of concreate class like milk and sugar is a problem
"""

# class CoffeeFactory:
#
#     @staticmethod
#     def get_coffee(coffee_name: str):
#         if coffee_name.lower() == CoffeeName.CAPPUCCINO.value:
#             return Cappuccino(milk=MilkFactory.get_milk("cappuccino"), sugar=SugarFactory.get_sugar("cappuccino"), \
#             bean=BeanFactory.get_bean("cappuccino"))
#         else:
#             raise Exception(f" Invalid coffee type = {coffee_name} !!!")


"""
To overcome this problem we can create 3 more factories one for milk, one for bean and one for sugar now the coffee
factory will depend only on these 3 factories.

- But this is not a good solution anyway, because the top level entity coffee factory still needs to know about all the 
    ingredients of coffee
    
- If a new ingredient say spice is added, then Coffee factory needs to know about that
"""

# TO overcome problems like this, we can use abstract factory
# create an abstract ingredients factory and for each coffee type extends them for their ingredients

from factory_design_pattern.coffee_machine.factories.cappuccino_ingredients_factory import CappuccinoIngredients
from factory_design_pattern.coffee_machine.factories.latte_ingredients_factory import LatteIngredients
from factory_design_pattern.coffee_machine.factories.robusta_ingredients_factory import RobustaIngredients


class CoffeeFactory:

    @staticmethod
    def get_coffee(coffee_name: str):
        if coffee_name.lower() == CoffeeName.CAPPUCCINO.value:
            return Cappuccino(CappuccinoIngredients())
        elif coffee_name.lower() == CoffeeName.LATTE.value:
            return Latte(LatteIngredients())
        elif coffee_name.lower() == CoffeeName.ROBUSTA.value:
            return Robusta(RobustaIngredients())
        else:
            raise Exception(f"Invalid coffee type = {coffee_name} !!!")


"""
Now neither coffee server nor coffee factory needs to know about the ingredients like milk, spice etc
"""
