"""
The unit of work design pattern is all about managing transactions involving multiple database operations.
It essentially groups these operations into a single unit, ensuring data consistency.

Why unit of work?

Imagine you're building an e-commerce application. A user might add a new item in their cart and then checkout.
This involves multiple database interactions - updating the inventory for each item, creating a new order record, and
potentially updating user information.

If we perform these updates one-by-one, and something goes wrong in midway (like a network failure), we might end up
with inconsistent data. Maybe the order record created by the inventory isn't updated.
This is where transactions come in.

Transactions for consistency

A database transaction ensures that either all operations within it succeed, or none of them do.
This maintains data integrity.
The unit of work acts as wrapper around these transactions.

How it works

The unit of work typically involves two collaborating components:

1. Unit of work class: This class manages the lifecycle of the transaction. It provides methods to:
-> Register operations to be performed (like insert, update, delete on data)
-> Commit the transaction making all changers permanent
-> Rollback the transaction, undoing the changes if anything goes wrong.

2. Repositories: These are the classes responsible for data access logic specific to different entities
(e.g., User repository, Product repository). They interact with the database but are unaware of the transactions.
They simply track the changes made to their respective entities.

"""

from typing import Any


class UnitOfWork:

    def __init__(self):
        self._new_entities: list[Any] = []
        self._update_entities: list[Any] = []
        self._removed_entities: list[Any] = []
        self._original_states: dict[str, dict[Any, Any]] = {}
        self.repositories: dict[str, Any] = {}

    def register_repository(self, name: str, repo: Any):
        self.repositories[name] = repo
        if name not in self._original_states:
            self._original_states[name] = {}

    def register_new(self, entity, repo_name: str):
        self._new_entities.append((repo_name, entity))

    def register_update(self, entity, repo_name: str):
        # save the original state of entity before updating
        original_entity = self.repositories[repo_name].get(entity._id)

        if original_entity:
            self._original_states[repo_name][entity._id] = original_entity

        self._update_entities.append((repo_name, entity))

    def register_removed(self, entity, repo_name: str):
        # save the original state of entity before removing
        original_entity = self.repositories[repo_name].get(entity._id)
        if original_entity:
            self._original_states[repo_name][entity._id] = original_entity

        self._removed_entities.append((repo_name, entity))

    def commit(self):
        try:
            for repo_name, entity in self._new_entities:
                self.repositories[repo_name].add(entity.__dict__)

            for repo_name, entity in self._update_entities:
                self.repositories[repo_name].add(entity.__dict__)

            for repo_name, entity in self._removed_entities:
                self.repositories[repo_name].add(entity.__dict__)

            self._clear()
        except Exception as e:
            self.rollback()
            raise e

    def rollback(self):
        for repo_name, entity in self._original_states.items():
            for _id, original_entity in entity.items():
                self.repositories[repo_name].update(_id, original_entity)
        for repo_name, entity in self._new_entities:
            self.repositories[repo_name].delete(entity._id)

        for repo_name, entity in self._removed_entities:
            self.repositories[repo_name].add(entity._id)
        self._clear()

    def _clear(self):
        self._new_entities.clear()
        self._update_entities.clear()
        self._removed_entities.clear()
        self._original_states.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
