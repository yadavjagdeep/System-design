from dataclasses import dataclass
from typing import TypeVar, Type
from parking_lot_low_level_design.src.storage.in_memory_storage import InMemoryStorage

T = TypeVar('T', bound='BaseModel')


@dataclass
class BaseModel:
    storage = InMemoryStorage()

    @property
    def model_name(self) -> str:
        return self.__class__.__name__

    def add(self) -> T:
        return self.storage.add(self)

    @classmethod
    def get(cls: Type[T], id: str) -> T:
        data = cls.storage.get(id, cls.__name__)
        return cls(**data)

    def update(self) -> None:
        self.storage.update(self.id, self)

    @classmethod
    def delete(cls, id: str) -> None:
        cls.storage.delete(id, cls.__name__)

    @classmethod
    def list_all(cls: Type[T]) -> dict[str, T]:
        data = cls.storage.list(cls.__name__)
        return {id: cls(**attrs) for id, attrs in data.items()}
