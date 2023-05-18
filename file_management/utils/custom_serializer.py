import json
from typing import Any
from models.file import File
from models.file_block import FileBlock
from models.memory_fragment import MemoryFragment
from models.linked_list import LinkedList
from models.node import Node

from models.page_table import PageTable


class CustomSerializer(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, PageTable):
            return {
                "memory_addresses": o.memory_addresses,
                "job_id": o.job_id
            }
        elif isinstance(o, MemoryFragment):
            return {
                "id": o.id,
                "start_time": o.start_time,
                "required_size": o.required_size,
                "execution_interval": o.execution_interval,
                "state_after_interval": o.state_after_interval,
                "current_state": o.current_state
            }
        elif isinstance(o, FileBlock):
            return {
                "size": o.size,
                "metadata": o.metadata,
                "metadata_size": o.metadata_size,
            }
        elif isinstance(o, Node):
            return {
                "data": o.data,
                "next_node": o.next_node,
            }
        elif isinstance(o, LinkedList):
            return {
                "head": o.head,
                "tail": o.tail,
            }
        elif isinstance(o, File):
            return {
                "size": o.size,
                "file_fragments": o.file_fragments,
                "allocation_time": o.allocation_time,
                "deallocation_time": o.deallocation_time,
            }
        # Add custom serializers here, before None
        elif o is None:
            return ""
        return super().default(o)
