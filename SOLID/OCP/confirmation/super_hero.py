from abc import ABC, abstractmethod

class SuperHero(ABC):

    @abstractmethod
    def attack(self):
        raise NotImplementedError
