from repository_pattern.in_memory_repository import InMemoryRepository
from dataclasses import dataclass


@dataclass
class User(InMemoryRepository):
    _id: str
    userId: str
    name: str
    email: str


@dataclass
class Order(InMemoryRepository):
    _id: str
    orderId: str
    product: str
    quantity: int
