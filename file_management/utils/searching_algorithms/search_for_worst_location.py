import math
from models.job_fragment import JobFragment


def search_for_worst_location(queue_list: list[JobFragment | None], target_memory: int) -> int:
    counter: int = 0
    index: int = -1
    possible_index: int = -1
    continuos_none_max_counter: int = -1
    for idx, job_fragment in enumerate(queue_list):
        # find for most None together

        if job_fragment is None:
            counter += 1

            if counter == 1:
                possible_index = idx

            # for real looking at the worst location
            if counter >= target_memory and continuos_none_max_counter < counter:
                index = possible_index
                continuos_none_max_counter = counter

        else:
            counter = 0
            possible_index = -1
            continue

    if index != -1:
        # found the worst optimal initial index
        # now it will return the index that will cause the most fragmentation
        deviation = continuos_none_max_counter - target_memory
        if deviation % 2 == 0:
            return index + int(deviation / 2)
        else:
            return index + math.floor(deviation / 2)

    return index
