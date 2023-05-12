from models.job_fragment import JobFragment
from models.page_table import PageTable
from utils.memory_handling.update_queue_list import update_queue_list
from utils.memory_handling.update_table_values import update_table_values


def free_memory_space(queue_list: list[JobFragment | None], memory_map: dict[str, PageTable], target_memory: int) -> int:
    # I will just use the first space that I find, because I might be
    # making it more complex than needed, IT COULD BE MADE EVEN MORE
    # EFFICIENTLY
    print("INSIDE freeing memory")
    counter: int = 0
    index: int = -1
    possible_index: int = -1
    for idx, job_fragment in enumerate(queue_list):
        if job_fragment is None:
            counter += 1

            if counter == 1:
                possible_index = idx

            if counter == target_memory:
                index = possible_index
                break
        else:
            if job_fragment.current_state == "Sleep":
                counter += 1
                continue
            counter = 0
            possible_index = -1
            continue

    if index != -1:
        # Update the tables
        memory_indexes = [i for i in range(index, index + counter)]
        update_queue_list(queue_list, memory_indexes)
        # update_table_values(
        #     memory_map, memory_indexes)

    return index


def free_memory_space1(queue_list: list[JobFragment | None], memory_map: dict[str, PageTable], target_memory: int) -> None:
    print("INSIDE freeing memory")
