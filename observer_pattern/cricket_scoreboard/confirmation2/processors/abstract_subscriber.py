from abc import ABC, abstractmethod


class Subscriber(ABC):

    @abstractmethod
    def update(self):
        raise NotImplementedError(f"subclass must implement the update method !!!")
