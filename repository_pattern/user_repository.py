from repository_pattern.in_memory_repository import InMemoryRepository
from dataclasses import dataclass


@dataclass
class User(InMemoryRepository):
    _id: str
    userId: str
    name: str
    email: str
