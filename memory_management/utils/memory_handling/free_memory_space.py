from models.job_fragment import JobFragment
from models.page_table import PageTable
from utils.memory_handling.free_queue_list import free_queue_list
from utils.memory_handling.free_table_values import free_table_values


def free_memory_space(queue_list: list[JobFragment | None], memory_map: dict[str, PageTable | None], target_memory: int) -> tuple[int, list[JobFragment]]:
    # I will just use the first space that I find, because I might be
    # making it more complex than needed, IT COULD BE MADE EVEN MORE
    # EFFICIENTLY
    pending_jobs: list[JobFragment] = []
    possible_statuses_to_be_deallocated = ["Sleep", "Pending"]
    counter: int = 0
    index: int = -1
    possible_index: int = -1
    for idx, job_fragment in enumerate(queue_list):
        if job_fragment is None or job_fragment.current_state in possible_statuses_to_be_deallocated:
            counter += 1

            if counter == 1:
                possible_index = idx

            if counter == target_memory:
                index = possible_index
                break
        else:
            counter = 0
            possible_index = -1
            continue

    if index != -1:
        # Add pending jobs to a list so that we can put them back to the jobs list
        pending_jobs = [job_fragment for job_fragment in queue_list[index: index + counter]
                        if job_fragment is not None and job_fragment.current_state == "Pending" and
                        job_fragment.id not in [job.id for job in pending_jobs]]

        # Update the tables
        memory_indexes = [i for i in range(index, index + counter)]
        free_queue_list(queue_list, memory_indexes)
        free_table_values(
            memory_map, memory_indexes)

    return index, pending_jobs
