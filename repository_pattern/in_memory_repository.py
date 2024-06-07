from typing import Any
from collections import defaultdict

from repository_pattern.base_repository import Repository


class InMemoryRepository(Repository):
    __DATA_STORE = defaultdict(dict)

    @property
    def repo(self) -> str:
        raise Exception("Subclass must implement @InMemoryRepository.repo.getter")

    def get(self, _id: Any) -> Any:
        return self.__DATA_STORE.get(self.repo, {}).get(_id)

    def get_all(self) -> Any:
        return self.__DATA_STORE.get(self.repo)

    def add(self, data: dict) -> Any:
        print(f'property - {self.repo}')
        if not data.get('_id'):
            raise ValueError('_id in mandatory param to create data')
        self.__DATA_STORE[self.repo][data['_id']] = data

    def update(self, _id: Any, data: Any) -> Any:
        self.__DATA_STORE[self.repo][_id] = data

    def delete(self, _id: Any) -> Any:
        if _id not in self.__DATA_STORE.get(self.repo):
            raise ValueError(f'No data exits for _id - {_id}')
        self.__DATA_STORE[self.repo].pop(_id)
