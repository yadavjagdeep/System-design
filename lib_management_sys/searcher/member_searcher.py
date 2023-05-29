from abc import ABC, abstractmethod

class BaseMemberSearcher(ABC):

    @abstractmethod
    def search(self) -> list:
        raise NotImplementedError("Implement in base class !!!")

