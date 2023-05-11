import json
from typing import Any
from models.job import Job

from models.page_table import PageTable


class CustomSerializer(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, PageTable):
            return {
                "memory_addresses": o.memory_addresses,
                "job_id": o.job_id
            }
        elif isinstance(o, Job):
            return {
                "id": o.id,
                "start_time": o.start_time,
                "required_size": o.required_size,
                "execution_interval": o.execution_interval,
                "state_after_interval": o.state_after_interval,
                "current_state": o.current_state
            }
            # Add custom serializers here, before None 
        elif isinstance(o, None):
            return ""
        return super().default(o)
