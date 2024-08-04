from enum import Enum


class EvictionPolicy(Enum):
    LRU = "lru"



class Storage(Enum):
    IN_MEMORY = "in_memory"
