from models.job_fragment import JobFragment
from models.page_table import PageTable


def deallocate_memory(queue_list: list[JobFragment | None], memory_map: dict[str, PageTable], job_id: str):
    MEMORY_TABLE = memory_map.get(job_id)
    if MEMORY_TABLE is not None:
        for address in MEMORY_TABLE.memory_addresses:
            queue_list[address] = None
    print(
        f"Deallocated memory for job with id {job_id}")
