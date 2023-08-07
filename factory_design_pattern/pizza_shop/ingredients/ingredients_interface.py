from abc import ABC, abstractmethod


class Ingredients(ABC):

    @abstractmethod
    def get_base(self):
        raise NotImplementedError(f"subclass must implement get_base method !!!")

    @abstractmethod
    def get_toppings(self):
        raise NotImplementedError(f"subclass must implement get_toppings method !!!")

    @abstractmethod
    def get_sauces(self):
        raise NotImplementedError(f"subclass must implement get_sauces method !!!")

