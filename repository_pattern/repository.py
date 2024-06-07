from repository_pattern.in_memory_repository import InMemoryRepository
from dataclasses import dataclass


@dataclass
class User(InMemoryRepository):
    _id: str
    userId: str
    name: str
    email: str

    @InMemoryRepository.repo.getter
    def repo(self) -> str:
        return 'user'


@dataclass
class Order(InMemoryRepository):
    _id: str
    orderId: str
    product: str
    quantity: int

    @InMemoryRepository.repo.getter
    def repo(self) -> str:
        return 'order'
