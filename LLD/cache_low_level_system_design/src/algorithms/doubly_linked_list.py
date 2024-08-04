
class DoublyLLNode:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev



class DoublyLL:

    def __init__(self):
        self.dummy_head = DoublyLLNode()
        self.dummy_tail = DoublyLLNode()

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head



    def add_node_at_tail(self, node: DoublyLLNode) -> None:

        tail_prev: DoublyLLNode = self.dummy_tail.prev

        tail_prev.next = node
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        node.prev = tail_prev


    def add_item_at_tail(self, data) -> DoublyLLNode:
        node: DoublyLLNode = DoublyLLNode(data)
        self.add_node_at_tail(node)
        return node


    def detach_node(self, node: DoublyLLNode) -> None:

        if node:
            node.prev.next = node.next
            node.next.prev = node.prev


    def is_item_present(self) -> bool:
        return self.dummy_head.next != self.dummy_tail


    def get_head_node(self) -> DoublyLLNode:
        if self.is_item_present():
            return self.dummy_head.next

    def get_tail_node(self) -> DoublyLLNode:
        if self.is_item_present():
            return self.dummy_tail.prev