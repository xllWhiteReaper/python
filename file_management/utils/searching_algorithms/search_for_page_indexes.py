from models.memory_fragment import MemoryFragment
from models.page_table import PageTable
from utils.memory_handling.free_memory_space_for_files import free_memory_space_for_files


def search_for_page_indexes(
    queue_list: list[MemoryFragment | None],
    memory_map: dict[str, (PageTable | None)],
    target_memory: int
) -> tuple[list[int], list[MemoryFragment]]:
    pending_jobs: list[MemoryFragment] = []
    available_indexes: list[int] = []
    for idx, job_fragment in enumerate(queue_list):
        if len(available_indexes) == target_memory:
            break
        if job_fragment is None:
            available_indexes.append(idx)

    if len(available_indexes) < target_memory:
        return free_memory_space_for_files(queue_list, memory_map, target_memory, available_indexes)

    return available_indexes, pending_jobs
