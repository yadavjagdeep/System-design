from abc import ABC, abstractmethod

class FoodItemFilter(ABC):

    @abstractmethod
    def filter(self, food_item: object) -> bool:
        raise NotImplementedError("Implement to support filter !!!")
