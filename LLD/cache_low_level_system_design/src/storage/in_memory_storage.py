from typing import Any

from cache_low_level_system_design.src.storage.abstract_storage import Repository
from cache_low_level_system_design.src.exceptions.exception import StorageFullException


class InMemoryStorage(Repository):

    def __init__(self, storage_size: int):
        self._capacity = storage_size
        self.__DATA_STORE = {}

    def get(self, _id: str) -> Any:
        return self.__DATA_STORE.get(_id)


    def add(self, data: Any) -> Any:

        if self.is_storage_full():
            raise StorageFullException('Cache Capacity Full ...')

        if not data.get('_id'):
            raise ValueError('_id is mandatory attribute for data creation  !!!')

        self.__DATA_STORE[data['_id']] = data

    def update(self, _id: str, data: Any) -> Any:
        if not self.__DATA_STORE.get(_id):
            raise ValueError(f'Unknown Key - {_id}')

        self.__DATA_STORE[_id] = data

    def delete(self, _id: str) -> Any:
        if not self.__DATA_STORE.get(_id):
            raise ValueError(f'Unknown Key - {_id}')

        self.__DATA_STORE.pop(_id)

    def get_all(self) -> Any:
        return self.__DATA_STORE


    def is_storage_full(self):
        return len(self.__DATA_STORE) == self._capacity
