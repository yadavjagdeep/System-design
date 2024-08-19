from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

T = TypeVar('T', bound='BaseModel')


class Repository(ABC, Generic[T]):

    @abstractmethod
    def get(self, id: Any) -> Any:
        raise NotImplementedError

    def add(self, entity: Any) -> Any:
        raise NotImplementedError

    def update(self, id: Any, entity: Any) -> Any:
        raise NotImplementedError

    def delete(self, id: Any) -> Any:
        raise NotImplementedError

    def list(self) -> Any:
        raise NotImplementedError
