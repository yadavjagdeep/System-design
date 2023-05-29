from abc import ABC, abstractmethod

class BaseBookSearcher(ABC):

    @abstractmethod
    def search(self) -> list:
        raise NotImplementedError("Implement in base class !!!")