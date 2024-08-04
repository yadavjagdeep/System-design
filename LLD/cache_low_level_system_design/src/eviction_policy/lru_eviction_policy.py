from typing import Union

from cache_low_level_system_design.src.eviction_policy.abstract_eviction_policy import AbstractEvictionPolicy
from cache_low_level_system_design.src.algorithms.doubly_linked_list import DoublyLL, DoublyLLNode

from cache_low_level_system_design.src.factories.storage_factory import StorageFactory
from cache_low_level_system_design.src.utility.constants import  Storage


"""
- Data in LL is store in format, {'key': key, 'val': val}
"""

class LRUEvictionPolicy(AbstractEvictionPolicy):

    def __init__(self):
        self.linkedList: DoublyLL = DoublyLL()
        self._key_node_mapper = StorageFactory.get_storage(Storage.IN_MEMORY.value)

    def key_accessed(self, key: str) -> None:

        data: dict = self._key_node_mapper.get(key)

        if data:
            node: DoublyLLNode = data.get('val')
            self.linkedList.detach_node(node)
            self.linkedList.add_node_at_tail(node)
        else:
            node: DoublyLLNode = self.linkedList.add_item_at_tail(key)
            self._key_node_mapper.add({'_id': key, 'val': node})


    def evict_key(self) -> Union[str, None]:
        if not self.linkedList.is_item_present():
            return None

        head_node: DoublyLLNode = self.linkedList.get_head_node()
        self.linkedList.detach_node(head_node)

        return head_node.data  #  cache key is stored as data
