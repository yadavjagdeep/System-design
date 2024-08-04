from cache_low_level_system_design.src.utility.constants import EvictionPolicy
from cache_low_level_system_design.src.eviction_policy.abstract_eviction_policy import AbstractEvictionPolicy
from cache_low_level_system_design.src.eviction_policy.lru_eviction_policy import LRUEvictionPolicy

class EvictionPolicyFactory:

    __POLICY_MAP = {
        EvictionPolicy.LRU.value: LRUEvictionPolicy
    }

    @classmethod
    def get_eviction_policy(cls, name: str):
        policy: AbstractEvictionPolicy.__class__ = cls.__POLICY_MAP.get(name)

        if not policy:
            raise ValueError(f'Unknown eviction policy name - {name}')

        return policy()
