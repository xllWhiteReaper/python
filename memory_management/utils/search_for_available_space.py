import math
from models.job import Job


def search_for_available_space(queue_list: list[Job | None], queue_type: str, target_memory: int):
    if queue_type == "best":
        search_for_best_location(queue_list, target_memory)
    elif queue_type == "first":
        search_for_best_location(queue_list, target_memory)
    elif queue_type == "worst":
        search_for_best_location(queue_list, target_memory)


def search_for_best_location(queue_list: list[Job | None], target_memory: int) -> int:
    queue_size = len(queue_list)
    counter: int = 0
    first_index: int = -1
    index: int = -1
    possible_index: int = -1
    for idx, job_fragment in enumerate(queue_list):

        if job_fragment is None:
            counter += 1

            if counter == 1:
                possible_index = idx

            if counter == target_memory and first_index == -1:
                first_index = possible_index

            if counter == target_memory and idx == (queue_size - 1):
                index = possible_index
                break

            if counter == target_memory and idx < (queue_size - 1) and queue_list[idx + 1] is not None:
                index = possible_index
                break

        else:
            counter = 0
            possible_index = -1
            continue
    if index == -1 and first_index != -1:
        # didn't find the most optimal index
        return first_index

    return index


def search_for_first_location(queue_list: list[Job | None], target_memory: int):
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


def search_for_worst_location(queue_list: list[Job | None], target_memory: int):
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
