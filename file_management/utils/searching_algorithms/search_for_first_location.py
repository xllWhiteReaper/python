from models.memory_fragment import MemoryFragment


def search_for_first_location(queue_list: list[MemoryFragment | None], target_memory: int) -> int:
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
            counter = 0
            possible_index = -1
            continue
    return index
