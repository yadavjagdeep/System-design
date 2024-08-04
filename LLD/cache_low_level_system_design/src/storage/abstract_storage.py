from typing import Any
from abc import ABC


class Repository(ABC):

    def get(self, _id: str) -> Any:
        raise NotImplementedError

    def update(self, _id: str, data: Any) -> Any:
        raise NotImplementedError


    def add(self, data: Any) -> Any:
        raise NotImplementedError

    def get_all(self) -> Any:
        raise NotImplementedError

    def delete(self, _id: Any) -> Any:
        raise NotImplementedError
