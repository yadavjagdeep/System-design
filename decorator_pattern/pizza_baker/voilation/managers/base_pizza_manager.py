from abc import ABC, abstractmethod


class BasePizza(ABC):

    @abstractmethod
    def get_pizza_cost(self):
        raise NotImplementedError("subclass must implement the get_pizza_cost method !!!")

    @abstractmethod
    def get_pizza_name(self):
        raise NotImplementedError("subclass must implement the get_pizza_name method !!!")
