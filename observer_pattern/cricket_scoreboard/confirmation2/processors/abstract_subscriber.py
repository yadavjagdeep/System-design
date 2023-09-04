from abc import ABC, abstractmethod


class Subscriber(ABC):

    @abstractmethod
    def update(self, runs: int, wickets: int, overs: float):
        raise NotImplementedError(f"subclass must implement the update method !!!")
