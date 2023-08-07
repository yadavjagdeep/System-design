from abc import ABC, abstractmethod


class Ingredients(ABC):

    @abstractmethod
    def get_milk(self):
        raise NotImplementedError("Not Implemented !!! ")

    @abstractmethod
    def get_sugar(self):
        raise NotImplementedError("Not Implemented !!! ")

    @abstractmethod
    def get_bean(self):
        raise NotImplementedError("Not Implemented !!! ")
