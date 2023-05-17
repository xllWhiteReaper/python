
from typing import TypeVar, Generic

from models.node import Node

T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: None | Node[T] = None
        self.tail: None | Node[T] = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: T) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, data: T) -> None:
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is not None:
                    previous_node.next_node = current_node.next_node
                    if current_node.next_node is None:
                        self.tail = previous_node
                else:
                    self.head = current_node.next_node
                    if self.head is None:
                        self.tail = None
                return
            previous_node = current_node
            current_node = current_node.next_node

    def __str__(self) -> str:
        node_values = []
        current_node = self.head
        while current_node is not None:
            node_values.append(str(current_node.data))
            current_node = current_node.next_node
        return " -> ".join(node_values)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next_node
