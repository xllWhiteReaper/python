from models.file_fragment import FileFragment
from models.linked_list import LinkedList
from models.node import Node


class File:
    def __init__(self) -> None:
        self.size: float = 0
        self.file_fragments: LinkedList[FileFragment] = LinkedList[FileFragment](
        )

    def calculate_file_size(self) -> None:
        head: Node[FileFragment] | None = self.file_fragments.head
        if head is not None:
            while head is not None:
                self.size += head.data.size
                head = head.next_node
