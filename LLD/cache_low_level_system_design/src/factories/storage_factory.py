from cache_low_level_system_design.src.utility.constants import  Storage

from cache_low_level_system_design.src.storage.abstract_storage import Repository
from cache_low_level_system_design.src.storage.in_memory_storage import InMemoryStorage


class StorageFactory:

    __MAP = {
        Storage.IN_MEMORY.value: InMemoryStorage
    }

    @classmethod
    def get_storage(cls, name: str, capacity: int=1000):
        storage: Repository.__class__ = cls.__MAP.get(name)

        if not storage:
            raise ValueError(f'Unknown Storage Name - {name}')

        return storage(capacity)
