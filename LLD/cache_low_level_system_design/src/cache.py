from typing import Any

from cache_low_level_system_design.src.factories.storage_factory import StorageFactory
from cache_low_level_system_design.src.factories.eviction_policy_factory import EvictionPolicyFactory
from cache_low_level_system_design.src.utility.constants import  Storage, EvictionPolicy
from cache_low_level_system_design.src.storage.abstract_storage import Repository
from cache_low_level_system_design.src.eviction_policy.abstract_eviction_policy import AbstractEvictionPolicy

from cache_low_level_system_design.src.exceptions.exception import StorageFullException, NotFoundException

class Cache:

    def __init__(self, capacity:int=5):
        self.eviction_policy: AbstractEvictionPolicy = EvictionPolicyFactory.get_eviction_policy(EvictionPolicy.LRU.value)
        self.storage: Repository = StorageFactory.get_storage(Storage.IN_MEMORY.value, capacity)


    def put(self, key: str, val: Any):
        try:
            self.storage.add({'_id': key, 'val': val})
            self.eviction_policy.key_accessed(key)

        except StorageFullException:
            print('Storage is full trying to evict')
            evict_key: str = self.eviction_policy.evict_key()

            if not evict_key:
                raise RuntimeError("Unexpected state, Storage is full and no key to evict")

            self.storage.delete(evict_key)
            self.put(key, val)


    def get(self, key: str):
        try:
            val = self.storage.get(key)
            self.eviction_policy.key_accessed(key)
            return val
        except NotFoundException:
            print('Tried to access non-existing key !!!')
            return None

