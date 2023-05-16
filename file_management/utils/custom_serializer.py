import json
from typing import Any
from models.file import File
from models.file_fragment import FileFragment
from models.job_fragment import JobFragment
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
        elif isinstance(o, JobFragment):
            return {
                "id": o.id,
                "start_time": o.start_time,
                "required_size": o.required_size,
                "execution_interval": o.execution_interval,
                "state_after_interval": o.state_after_interval,
                "current_state": o.current_state
            }
        elif isinstance(o, FileFragment):
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
            }
        # Add custom serializers here, before None
        elif o is None:
            return ""
        return super().default(o)
