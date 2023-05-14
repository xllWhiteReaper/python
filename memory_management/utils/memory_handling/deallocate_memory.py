from models.job_fragment import JobFragment
from models.page_table import PageTable
from utils.memory_handling.free_queue_list import free_queue_list
from utils.memory_handling.free_table_values import free_table_values


def deallocate_memory(queue_list: list[JobFragment | None], memory_map: dict[str, PageTable | None], job_id: str):
    MEMORY_TABLE = memory_map.get(job_id)
    if MEMORY_TABLE is not None:
        free_queue_list(queue_list, MEMORY_TABLE.memory_addresses)
        free_table_values(memory_map, MEMORY_TABLE.memory_addresses)
