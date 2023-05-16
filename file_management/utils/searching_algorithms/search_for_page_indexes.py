from models.memory_fragment import MemoryFragment
from utils.memory_handling.free_memory_space import POSSIBLE_STATUSES_TO_BE_DEALLOCATED


def search_for_page_indexes(queue_list: list[MemoryFragment | None], target_memory: int) -> list[int]:
    available_indexes: list[int] = []
    for idx, job_fragment in enumerate(queue_list):
        if len(available_indexes) == target_memory:
            break
        if job_fragment is None or job_fragment.current_state in POSSIBLE_STATUSES_TO_BE_DEALLOCATED:
            available_indexes.append(idx)
    return available_indexes
