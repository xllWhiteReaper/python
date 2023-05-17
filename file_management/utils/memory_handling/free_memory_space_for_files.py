from models.memory_fragment import MemoryFragment
from models.page_table import PageTable
# from utils.debugger import json_stringify
from utils.memory_handling.free_memory_space import POSSIBLE_STATUSES_TO_BE_DEALLOCATED
from utils.memory_handling.free_queue_list import free_queue_list
from utils.memory_handling.free_table_values import free_table_values


def free_memory_space_for_files(
    queue_list: list[MemoryFragment | None],
    memory_map: dict[str, PageTable | None],
    target_memory: int,
    available_indexes: list[int]
) -> tuple[list[int], list[MemoryFragment]]:
    freed_indexes: list[int] = [*available_indexes]
    pending_jobs: list[MemoryFragment] = []

    for idx, job_fragment in enumerate(queue_list):
        if len(freed_indexes) == target_memory:
            break

        if job_fragment is not None and job_fragment.current_state in POSSIBLE_STATUSES_TO_BE_DEALLOCATED:
            freed_indexes.append(idx)

    if len(freed_indexes) == target_memory:
        # Add pending jobs to a list so that we can put them back to the jobs list
        for index in freed_indexes:
            job_fragment = queue_list[index]
            if job_fragment is not None and job_fragment.current_state == "Pending":
                pending_jobs.append(job_fragment)

        # Update the tables
        free_queue_list(queue_list, freed_indexes)

        free_table_values(
            memory_map, freed_indexes)

    return freed_indexes, pending_jobs
