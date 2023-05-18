from models.file_block import FileBlock
from models.linked_list import LinkedList
from models.node import Node


class File:
    def __init__(self, allocation_time: float = 0, deallocation_time: float = 0) -> None:
        self.allocation_time: float = allocation_time
        self.deallocation_time: float = deallocation_time
        self.size: float = 0
        self.file_fragments: LinkedList[FileBlock] = LinkedList[FileBlock](
        )

    def calculate_file_size(self) -> None:
        self.size = 0
        head: Node[FileBlock] | None = self.file_fragments.head
        while head is not None:
            self.size += head.data.size
            head = head.next_node

    def append(self, *elements: FileBlock) -> None:
        for element in elements:
            self.file_fragments.append(element)
        self.calculate_file_size()
