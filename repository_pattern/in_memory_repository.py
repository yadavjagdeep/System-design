from typing import Any

from repository_pattern.base_repository import Repository


class InMemoryRepository(Repository):
    __DATA_STORE = {}

    @classmethod
    def get(cls, _id: Any) -> Any:
        return cls.__DATA_STORE.get(_id)

    @classmethod
    def get_all(cls) -> Any:
        return cls.__DATA_STORE

    @classmethod
    def add(cls, data: dict) -> Any:
        if not data.get('_id'):
            raise ValueError('_id in mandatory param to create data')
        cls.__DATA_STORE[data['_id']] = data

    @classmethod
    def update(cls, _id: Any, data: Any) -> Any:
        cls.__DATA_STORE[_id] = data

    @classmethod
    def delete(cls, _id: Any) -> Any:
        if _id not in cls.__DATA_STORE:
            raise ValueError(f'No data exits for _id - {_id}')
        cls.__DATA_STORE.pop(_id)
