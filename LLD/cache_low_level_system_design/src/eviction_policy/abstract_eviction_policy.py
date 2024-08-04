from abc import ABC, abstractmethod

class AbstractEvictionPolicy(ABC):

    @abstractmethod
    def key_accessed(self, key):
        raise NotImplementedError


    @abstractmethod
    def evict_key(self):
        raise NotImplementedError
