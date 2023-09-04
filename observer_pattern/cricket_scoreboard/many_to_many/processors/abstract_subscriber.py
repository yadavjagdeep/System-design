from abc import ABC, abstractmethod
from observer_pattern.cricket_scoreboard.many_to_many.processors.abstract_publisher import Publisher


class Subscriber(ABC):

    @abstractmethod
    def update(self, publisher: Publisher):
        raise NotImplementedError(f"subclass must implement the update method !!!")
