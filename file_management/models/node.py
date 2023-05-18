from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T, next_node: None | T = None):
        self.data = data
        self.next_node = next_node
