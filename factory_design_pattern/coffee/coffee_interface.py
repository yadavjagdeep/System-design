from abc import ABC, abstractmethod


class Coffee(ABC):

    def __init__(self, ingredients: object):
        self.milk = ingredients.get_milk()
        self.sugar = ingredients.get_sugar()
        self.bean = ingredients.get_bean()

    @abstractmethod
    def brew(self):
        raise NotImplementedError("Method must be implemented in child class !!!")

    @abstractmethod
    def boil(self):
        raise NotImplementedError("Method must be implemented in child class !!!")

