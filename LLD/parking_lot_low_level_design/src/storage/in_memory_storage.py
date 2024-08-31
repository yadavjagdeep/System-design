# from parking_lot_low_level_design.src.storage.abstract_storage import Repository
from typing import TypeVar, Dict, Any

T = TypeVar('T', bound='BaseModel')

class InMemoryStorage:
    def __init__(self):
        self.storage: Dict[str, Dict[str, Dict[str, Any]]] = {}

    def _get_model_storage(self, model_name: str) -> Dict[str, Any]:
        if model_name not in self.storage:
            self.storage[model_name] = {}
        return self.storage[model_name]

    def get(self, id: str, model_name: str) -> dict:
        model_storage = self._get_model_storage(model_name)
        if id not in model_storage:
            raise ValueError(f'No record found for id - {id} in model {model_name}')
        return model_storage[id]

    def add(self, entity: T) -> T:
        model_name = entity.model_name
        model_storage = self._get_model_storage(model_name)
        if not entity.id:
            raise ValueError('id is a mandatory attribute to create record !!!')
        model_storage[entity.id] = entity.__dict__
        return entity

    def update(self, id: str, entity: T) -> None:
        model_name = entity.model_name
        model_storage = self._get_model_storage(model_name)
        if id not in model_storage:
            raise ValueError(f'No record with id - {id} to update in model {model_name} !!!')
        model_storage[id] = entity.__dict__

    def list(self, model_name: str) -> dict:
        return self._get_model_storage(model_name)

    def delete(self, id: str, model_name: str) -> None:
        model_storage = self._get_model_storage(model_name)
        if id not in model_storage:
            raise ValueError(f'No record with id - {id} to delete in model {model_name} !!!')
        del model_storage[id]
