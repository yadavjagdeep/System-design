"""
The repository pattern is an abstraction over the data store that decouples business logic from data access,
 providing a clean separation of concerns and a collection-like interface for interacting with the data store.
 """

from typing import Any
from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def get(self, _id: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Any:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def update(self, _id: Any, data: Any) -> Any:
        raise NotImplementedError
